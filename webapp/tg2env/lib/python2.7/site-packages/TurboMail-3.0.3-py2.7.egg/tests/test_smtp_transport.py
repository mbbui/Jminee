#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import smtplib
import socket

from pymta.api import IMTAPolicy, PolicyDecision
from pymta.test_util import SMTPTestCase

from turbomail import Message, WrappedMessage
from turbomail.control import interface
from turbomail.compat import set
from turbomail.exceptions import MailConfigurationException
from turbomail.managers.immediate import ImmediateManager
from turbomail.transports.smtp import SMTPTransportFactory

from tests.test_tm2_compatibility import TurboMailTestCase

logging.disable(logging.WARNING)


class TestSMTPTransport(SMTPTestCase, TurboMailTestCase):
    
    def setUp(self):
        self.config = {'mail.on': True, 'mail.manager': 'immediate', 
                       'mail.transport': 'smtp', 'mail.brand': False}
        self.fake_setuptools =  {'immediate': ImmediateManager,
                                 'smtp': SMTPTransportFactory()}
        super(TestSMTPTransport, self).setUp()
        self._ignore_warning('Configuration key ".+" is deprecated.*')
        self.msg = self.build_message()
    
    def build_message(self):
        return Message('foo@example.com', 'to@example.com', 'Test', 
                       plain='Plain text body')
    
    def init_mta(self, policy_class=IMTAPolicy):
        super(TestSMTPTransport, self).init_mta(policy_class)
        self.connection_string = '%s:%s' % (self.hostname, self.listen_port)
        config = self.config.copy()
        config.update({'mail.smtp.server': self.connection_string})
        # We must not assume that TurboMail is installed with egg-info
        interface.start(config, extra_classes=self.fake_setuptools)
    
    def test_send_simple_message(self):
        self.init_mta()
        self.msg_string = str(self.msg)
        self.msg.send()
        
        queue = self.get_received_messages()
        self.assertEqual(1, queue.qsize())
        msg = queue.get()
        self.assertEqual('foo@example.com', msg.smtp_from)
        self.assertEqual(['to@example.com'], msg.smtp_to)
        self.assertEqual(self.msg_string, msg.msg_data)
    
    def test_smtp_from(self):
        "Test that smtp_from is being honored and used as envelope sender."
        self.init_mta()
        self.msg.smtp_from = 'devnull@foo.example'
        self.msg.send()
        
        queue = self.get_received_messages()
        self.assertEqual(1, queue.qsize())
        msg = queue.get()
        self.assertEqual('devnull@foo.example', msg.smtp_from)
    
    def test_no_default_for_smtp_server(self):
        """Test that the user is forced to configure the SMTP server to use
        explicitely to minize the likelihood that mails are sent out although
        they shouldn't due to misconfigurations."""
        # We must not assume that TurboMail is installed with egg-info
        interface.start(self.config, extra_classes=self.fake_setuptools)
        
        self.assertRaises(MailConfigurationException, self.msg.send)
    
    def test_refused_sender_is_handled_correctly(self):
        class SenderRejectionPolicy(IMTAPolicy):
            def accept_from(self, sender, message):
                return False
        self.init_mta(policy_class=SenderRejectionPolicy)
        self.assertRaises(smtplib.SMTPSenderRefused, self.msg.send)
        
        queue = self.get_received_messages()
        self.assertEqual(0, queue.qsize())
    
    def test_refused_recipients_are_handled_correctly(self):
        class RecipientRejectionPolicy(IMTAPolicy):
            def accept_rcpt_to(self, sender, message):
                return False
        self.init_mta(policy_class=RecipientRejectionPolicy)
        self.assertRaises(smtplib.SMTPRecipientsRefused, self.msg.send)
        
        queue = self.get_received_messages()
        self.assertEqual(0, queue.qsize())
    
    def test_send_messages_also_to_cc_recipients(self):
        self.init_mta()
        self.msg.cc = 'cc@example.com'
        self.msg.send()
        
        queue = self.get_received_messages()
        self.assertEqual(1, queue.qsize())
        msg = queue.get()
        self.assertEqual(set(['to@example.com', 'cc@example.com']), 
                         set(msg.smtp_to))
    
    def test_smtp_can_send_wrapped_messages(self):
        self.init_mta()
        msg_string = 'Subject: Test\n\nJust testing...'
        msg = WrappedMessage('devnull@example.com', 'mike@example.com', msg_string)
        msg.send()
        
        queue = self.get_received_messages()
        self.assertEqual(1, queue.qsize())
        msg = queue.get()
        self.assertEqual('devnull@example.com', msg.smtp_from)
        self.assertEqual(['mike@example.com'], msg.smtp_to)
    
    def get_connection(self):
        # We can not use the id of transport.connection because sometimes Python
        # returns the same id for new, but two different instances of the same
        # object (Fedora 10, Python 2.5):
        # class Bar: pass
        # id(Bar()) == id(Bar())  -> True
        sock = getattr(interface.manager.transport.connection, 'sock', None)
        return sock
    
    def get_transport(self):
        return interface.manager.transport
    
    def test_close_connection_when_max_messages_per_connection_was_reached(self):
        self.config['mail.smtp.max_messages_per_connection'] = 2
        self.init_mta()
        self.msg.send()
        first_connection = self.get_connection()
        self.msg.send()
        second_connection = self.get_connection()
        
        queue = self.get_received_messages()
        self.assertEqual(2, queue.qsize())
        self.assertNotEqual(first_connection, second_connection)
    
    def test_close_connection_when_max_messages_per_connection_was_reached_even_on_errors(self):
        self.config['mail.smtp.max_messages_per_connection'] = 1
        class RejectHeloPolicy(IMTAPolicy):
            def accept_helo(self, sender, message):
                return False
        self.init_mta(policy_class=RejectHeloPolicy)
        
        self.msg.send()
        self.assertEqual(False, self.get_transport().is_connected())
    
    def test_reopen_connection_when_server_closed_connection(self):
        self.config['mail.smtp.max_messages_per_connection'] = 2
        class DropEverySecondConnectionPolicy(IMTAPolicy):
            def accept_msgdata(self, sender, message):
                if not hasattr(self, 'nr_connections'):
                    self.nr_connections = 0
                self.nr_connections = (self.nr_connections + 1) % 2
                decision = PolicyDecision(True)
                drop_this_connection = (self.nr_connections == 1)
                decision._close_connection_after_response = drop_this_connection
                return decision
        self.init_mta(policy_class=DropEverySecondConnectionPolicy)
        
        self.msg.send()
        first_connection = self.get_connection()
        self.msg.send()
        second_connection = self.get_connection()
        
        queue = self.get_received_messages()
        self.assertEqual(2, queue.qsize())
        opened_new_connection = (first_connection != second_connection)
        self.assertEqual(True, opened_new_connection)
    
    def test_smtp_shutdown_ignores_socket_errors(self):
        self.config['mail.smtp.max_messages_per_connection'] = 2
        class CloseConnectionAfterDeliveryPolicy(IMTAPolicy):
            def accept_msgdata(self, sender, message):
                decision = PolicyDecision(True)
                decision._close_connection_after_response = True
                return decision
        self.init_mta(policy_class=CloseConnectionAfterDeliveryPolicy)
        
        self.msg.send()
        smtp_transport = self.get_transport()
        interface.stop(force=True)
        
        queue = self.get_received_messages()
        self.assertEqual(1, queue.qsize())
        self.assertEqual(False, smtp_transport.is_connected())
    
    def test_handle_server_which_rejects_all_connections(self):
        class RejectAllConnectionsPolicy(IMTAPolicy):
            def accept_new_connection(self, peer):
                return False
        self.init_mta(policy_class=RejectAllConnectionsPolicy)
        
        self.assertRaises(smtplib.SMTPServerDisconnected, self.msg.send)
    
    def test_handle_error_when_server_is_not_running_at_all(self):
        self.init_mta()
        self.assertEqual(None, self.get_transport())
        interface.config['mail.smtp.server'] = 'localhost:47115'
        
        self.assertRaises(socket.error, self.msg.send)
    
    def test_can_retry_failed_connection(self):
        self.config['mail.message.nr_retries'] = 4
        class DropFirstFourConnectionsPolicy(IMTAPolicy):
            def accept_msgdata(self, sender, message):
                if not hasattr(self, 'nr_connections'):
                    self.nr_connections = 0
                self.nr_connections += 1
                return (self.nr_connections > 4)
        self.init_mta(policy_class=DropFirstFourConnectionsPolicy)
        
        msg = self.build_message()
        self.assertEqual(4, msg.nr_retries)
        msg.send()
        
        queue = self.get_received_messages()
        self.assertEqual(1, queue.qsize())

