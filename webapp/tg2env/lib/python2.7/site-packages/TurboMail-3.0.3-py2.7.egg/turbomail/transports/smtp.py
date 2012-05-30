# encoding: utf-8

"""Deliver messages using (E)SMTP."""


import logging
import socket

from smtplib import SMTP, SMTPException, SMTPRecipientsRefused, SMTPSenderRefused, SMTPServerDisconnected

from turbomail.api import Transport, TransportFactory
from turbomail.compat import get_message
from turbomail.control import interface
from turbomail.exceptions import MailConfigurationException, TransportExhaustedException


__all__ = ['load']

log = logging.getLogger("turbomail.transport")
deliverylog = logging.getLogger("turbomail.delivery")



def load():
    return SMTPTransportFactory()


class SMTPTransport(Transport):
    def __init__(self):
        super(SMTPTransport, self).__init__()
        log.debug("SMTPTransport created.")
        
        self.server = self.config_get('mail.smtp.server', None)
        if self.server == None:
            raise MailConfigurationException('no server configured for smtp ("mail.smtp.server")')
        self.username = self.config_get("mail.smtp.username")
        self.password = self.config_get("mail.smtp.password")
        self.use_tls = self.config_get("mail.smtp.tls", None)
        self.debug = self.config_get("mail.smtp.debug", False)
        
        self.max_number_of_messages_per_connection = \
            self.config_get('mail.smtp.max_messages_per_connection', default=1, tm2_key='jobs')
        
        self.connection = None
        self.nr_messages_sent_with_this_connection = None
    
    def close_connection(self):
        if self.is_connected():
            log.debug("Closing SMTP connection.")
            try:
                try:
                    self.connection.quit()
                except SMTPServerDisconnected:
                    pass
                except (SMTPException, socket.error), e:
                    msg = 'Exception occured when stopping connection' + unicode(e)
                    log.exception(msg)
            finally:
                self.connection = None
    
    def stop(self):
        super(SMTPTransport, self).stop()
        self.close_connection()
    
    def is_connected(self):
        return getattr(self.connection, 'sock', None) is not None
    
    def _encrypt_connection_with_tls_if_configured(self, connection):
        # TODO: Testcase: Always use ehlo for possibly encrypted connections.
        connection.ehlo()
        
        server_provides_tls = connection.has_extn('STARTTLS')
        # TODO: Testcase self.tls = False (-> no TLS)
        if (self.use_tls is None) and (not server_provides_tls):
            log.info("TLS unavailable. Messages will be delivered insecurely.")
            return
        elif self.use_tls == False:
            return
        connection.starttls()
        connection.ehlo()
        log.info("TLS enabled on SMTP server.")
    
    def connect_to_server(self):
        connection = SMTP()
        connection.set_debuglevel(self.debug)
        log.info("Connecting to SMTP server %s." % self.server)
        connection.connect(self.server)
        
        self._encrypt_connection_with_tls_if_configured(connection)
        if self.username and self.password:
            log.info("Authenticating as %s." % self.username)
            connection.login(self.username, self.password)
        return connection
    
    def connect_to_server_if_nessary(self):
        if not self.is_connected():
            self.connection = self.connect_to_server()
            self.nr_messages_sent_with_this_connection = 0
    
    def can_send_more_messages_on_this_connection(self):
        return self.nr_messages_sent_with_this_connection < self.max_number_of_messages_per_connection
    
    def send_with_smtp(self, message):
        try:
            self.nr_messages_sent_with_this_connection += 1
            sender = str(message.envelope_sender)
            recipients = message.recipients.string_addresses
            self.connection.sendmail(sender, recipients, str(message))
        except SMTPSenderRefused, e:
            # The envelope sender was refused.  This is bad.
            deliverylog.error("%s REFUSED %s %s" % (message.id, e.__class__.__name__, get_message(e)))
            raise
        except SMTPRecipientsRefused, e:
            # All recipients were refused.  Log which recipients.
            # This allows you to automatically parse your logs for bad e-mail addresses.
            deliverylog.warning("%s REFUSED %s %s" % (message.id, e.__class__.__name__, get_message(e)))
            raise
        except SMTPServerDisconnected, e:
            raise TransportExhaustedException
        except Exception, e:
            cls_name = e.__class__.__name__
            deliverylog.debug("%s EXCEPTION %s" % (message.id, cls_name), exc_info=True)
            
            if message.nr_retries >= 0:
                deliverylog.warning("%s DEFERRED %s" % (message.id, cls_name))
                message.nr_retries -= 1
                interface.manager.deliver(message)
                return
            else:
                deliverylog.error("%s REFUSED %s" % (message.id, cls_name), exc_info=True)
                raise
    
    def deliver(self, message):
        log.info("Attempting delivery of message %s." % message.id)
        deliverylog.info("%s DELIVER" % message.id)
        
        self.connect_to_server_if_nessary()
        try:
            self.send_with_smtp(message)
        finally:
            if not self.can_send_more_messages_on_this_connection():
                self.close_connection()
        deliverylog.info("%s SENT" % message.id)


class SMTPTransportFactory(TransportFactory):
    name = "smtp"
    transport = SMTPTransport
