# encoding: utf-8

"""MIME-encoded electronic mail message classes."""


import logging
import os
import time
import warnings

from datetime import datetime

from turbomail import release
from turbomail.compat import Header, MIMEBase, MIMEImage, MIMEMultipart, MIMEText, encode_base64, formatdate, make_msgid
from turbomail.util import Address, AddressList
from turbomail.control import interface


__all__ = ['Message']

log = logging.getLogger("turbomail.message")



class NoDefault(object):
    pass


class BaseMessage(object):
    def __init__(self, smtp_from=None, to=None, kw=None):
        self.merge_if_set(kw, smtp_from, 'smtp_from')
        self._smtp_from = AddressList(self.pop_deprecated(kw, 'smtp_from', 'smtpfrom'))
        self._to = AddressList(self.pop_deprecated(kw, 'to', 'recipient', value=to))
        self.nr_retries = self.kwpop(kw, 'nr_retries', default=3)
    
    smtp_from = AddressList.protected('_smtp_from')
    to = AddressList.protected('_to')
    
    def merge_if_set(self, kw, value, name):
        if value not in [None, '']:
            kw[name] = value
    
    def kwpop(self, kw, name, configkey=None, default=None, old_configkey=None):
        if name in kw:
            value = kw.pop(name)
        else:
            if configkey == None:
                configkey = 'mail.message.%s' % name
            value = interface.config.get(configkey, NoDefault)
            
            if value == NoDefault and old_configkey != None:
                value = interface.config.get(old_configkey, NoDefault)
                if value != NoDefault:
                    msg = 'Falling back to deprecated configuration option "%s", please use "%s" instead'
                    warnings.warn(msg % (old_configkey, configkey), 
                                  category=DeprecationWarning)
            if value == NoDefault:
                value = default
        return value
    
    def pop_deprecated(self, kw, new_name, deprecated_name, value=None):
        deprecated_value = self.kwpop(kw, deprecated_name)
        if deprecated_value != None:
            self._warn_about_deprecated_property(deprecated_name, new_name)
            value = deprecated_value
        elif value == None:
            value = self.kwpop(kw, new_name)
        return value
    
    def send(self):
        return interface.send(self)
    
    # --------------------------------------------------------------------------
    # Deprecated properties 
    def _warn_about_deprecated_property(self, deprecated_name, new_name):
        msg = 'Property "%s" is deprecated, please use "%s" instead'
        warnings.warn(msg % (deprecated_name, new_name), category=DeprecationWarning)
    
    def get_smtpfrom(self):
        self._warn_about_deprecated_property('smtpfrom', 'smtp_from')
        return self.smtp_from
    
    def set_smtpfrom(self, smtpfrom):
        self._warn_about_deprecated_property('smtpfrom', 'smtp_from')
        self.smtp_from = smtpfrom
    smtpfrom = property(fget=get_smtpfrom, fset=set_smtpfrom)
    
    def get_recipient(self):
        self._warn_about_deprecated_property('recipient', 'to')
        return self.to
    
    def set_recipient(self, recipient):
        self._warn_about_deprecated_property('recipient', 'to')
        self.to = recipient
    recipient = property(fget=get_recipient, fset=set_recipient)


class Message(BaseMessage):
    """Simple e-mail message class."""
    
    def __init__(self, author=None, to=None, subject=None, **kw):
        """Instantiate a new Message object.
        
        No arguments are required, as everything can be set using class
        properties.  Alternatively, I{everything} can be set using the
        constructor, using named arguments.  The first three positional
        arguments can be used to quickly prepare a simple message.
        """
        super(Message, self).__init__(to=to, kw=kw)
        
        kwpop = lambda *args, **kwargs: self.kwpop(kw, *args, **kwargs)
        pop_deprecated = lambda name, old_name: self.pop_deprecated(kw, name, old_name)
        
        self.merge_if_set(kw, author, 'author')
        self._author = AddressList(kwpop('author'))
        self._cc = AddressList(kwpop("cc"))
        self._bcc = AddressList(kwpop("bcc"))
        self._sender = AddressList(kwpop("sender"))
        self._reply_to = AddressList(pop_deprecated('reply_to', 'replyto'))
        self._disposition = AddressList(kwpop("disposition"))
        
        self.subject = subject
        self.date = kwpop("date")
        
        self.encoding = kwpop("encoding", default='us-ascii', 
                              old_configkey='mail.encoding')
        
        self.organization = kwpop("organization")
        self.priority = kwpop("priority")
        
        self.plain = kwpop("plain", default=None)
        self.rich = kwpop("rich", default=None)
        self.attachments = kwpop("attachments", default=[])
        self.embedded = kwpop("embedded", default=[])
        self.headers = kwpop("headers", default=[])
        
        self._id = kw.get("id", None)
        
        self._processed = False
        self._dirty = False
        if len(kw) > 0:
            parameter_name = kw.keys()[0]
            error_msg = "__init__() got an unexpected keyword argument '%s'"
            raise TypeError(error_msg % parameter_name)
    
    author = AddressList.protected('_author')
    bcc = AddressList.protected('_bcc')
    cc = AddressList.protected('_cc')
    disposition = AddressList.protected('_disposition')
    reply_to = AddressList.protected('_reply_to')
    sender = AddressList.protected('_sender')
    
    def __setattr__(self, name, value):
        """Set the dirty flag as properties are updated."""
        super(Message, self).__setattr__(name, value)
        if name not in ('bcc', '_dirty', '_processed'): 
            self.__dict__['_dirty'] = True
    
    def __str__(self):
        return self.mime.as_string()
    
    def _get_authors(self):
        # Just for better readability. I put this method here because a wrapped
        # message must only have one author (smtp_from) so this method is only
        # useful in a TurboMail Message.
        return self.author
    
    def _set_authors(self, value):
        self.author = value
    authors = property(_get_authors, _set_authors)
    
    def id(self):
        if not self._id or (self._processed and self._dirty):
            self.__dict__['_id'] = make_msgid()
            self._processed = False
        return self._id
    id = property(id)
    
    def envelope_sender(self):
        """Returns the address of the envelope sender address (SMTP from, if not
        set the sender, if this one isn't set too, the author)."""
        envelope_sender = None
        # TODO: Make this check better as soon as SMTP from and sender are 
        # Addresses, not AddressLists anymore.
        if self.smtp_from != None and len(self.smtp_from) > 0:
            envelope_sender = self.smtp_from
        elif self.sender != None and len(self.sender) > 0:
            envelope_sender = self.sender
        else:
            envelope_sender = self.author
        return Address(envelope_sender)
    envelope_sender = property(envelope_sender)
    
    def recipients(self):
        return AddressList(self.to + self.cc + self.bcc)
    recipients = property(recipients)
    
    def mime_document(self, plain, rich=None):
        if not rich:
            message = plain
        
        else:
            message = MIMEMultipart('alternative')
            message.attach(plain)
        
            if not self.embedded:
                message.attach(rich)
        
            else:
                embedded = MIMEMultipart('related')
                embedded.attach(rich)
                for attachment in self.embedded: embedded.attach(attachment)
                message.attach(embedded)
        
        if self.attachments:
            attachments = MIMEMultipart()
            attachments.attach(message)
            for attachment in self.attachments: attachments.attach(attachment)
            message = attachments
        
        return message
    
    def _build_date_header_string(self, date_value):
        """Gets the date_value (may be None, basestring, float or 
        datetime.datetime instance) and returns a valid date string as per 
        RFC 2822."""
        if isinstance(date_value, datetime):
            date_value = time.mktime(date_value.timetuple())
        if not isinstance(date_value, basestring):
            date_value = formatdate(date_value, localtime=True)
        return date_value
    
    def _build_header_list(self, author, sender):
        date_value = self._build_date_header_string(self.date)
        headers = [
                ('Sender', sender),
                ('From', author),
                ('Reply-To', self.reply_to),
                ('Subject', self.subject),
                ('Date', date_value),
                ('To', self.to),
                ('Cc', self.cc),
                ('Disposition-Notification-To', self.disposition),
                ('Organization', self.organization),
                ('X-Priority', self.priority),
            ]
        
        if interface.config.get("mail.brand", True):
            headers.extend([
                    ('X-Mailer', "%s %s" % (release.name, release.version)),
                ])
        if isinstance(self.headers, dict):
            for key in self.headers:
                headers.append((key, self.headers[key]))
        else:
            headers.extend(self.headers)
        return headers
    
    def _add_headers_to_message(self, message, headers):
        for header in headers:
            if isinstance(header, (tuple, list)):
                if header[1] is None or ( isinstance(header[1], list) and not header[1] ): continue
                header = list(header)
                if isinstance(header[1], unicode):
                    header[1] = Header(header[1], self.encoding)
                elif isinstance(header[1], AddressList):
                    header[1] = header[1].encode(self.encoding)
                header[1] = str(header[1])
                message.add_header(*header)
            elif isinstance(header, dict):
                message.add_header(**header)
    
    def mime(self):
        """Produce the final MIME message."""
        author = self.author
        sender = self.sender
        if not author and sender:
            msg = 'Please specify the author using the "author" property. ' + \
                  'Using "sender" for the From header is deprecated!'
            warnings.warn(msg, category=DeprecationWarning)
            author = sender
            sender = []
        if not author:
            raise ValueError('You must specify an author.')
        
        assert self.subject, "You must specify a subject."
        assert len(self.recipients) > 0, "You must specify at least one recipient."
        assert self.plain, "You must provide plain text content."
        
        if len(author) > 1 and len(sender) == 0:
            raise ValueError('If there are multiple authors of message, you must specify a sender!')
        if len(sender) > 1:
            raise ValueError('You must not specify more than one sender!')
        
        if not self._dirty and self._processed and not interface.config.get("mail.debug", False):
            return self._mime
        
        self._processed = False
        
        plain = MIMEText(self._callable(self.plain).encode(self.encoding), 'plain', self.encoding)
        
        rich = None
        if self.rich:
            rich = MIMEText(self._callable(self.rich).encode(self.encoding), 'html', self.encoding)
        
        message = self.mime_document(plain, rich)
        headers = self._build_header_list(author, sender)
        self._add_headers_to_message(message, headers)
        
        self._mime = message
        self._processed = True
        self._dirty = False
        
        return message
    mime = property(mime)
    
    def attach(self, file, name=None):
        """Attach an on-disk file to this message."""
        
        part = MIMEBase('application', "octet-stream")

        if isinstance(file, (str, unicode)):
            fp = open(file, "rb")
        else:
            assert name is not None, "If attaching a file-like object, you must pass a custom filename, as one can not be inferred."
            fp = file
        
        part.set_payload(fp.read())
        encode_base64(part)

        part.add_header('Content-Disposition', 'attachment', filename=os.path.basename([name, file][name is None]))
            
        self.attachments.append(part)
    
    def embed(self, file, name=None):
        """Attach an on-disk image file and prepare for HTML embedding.
        
        This method should only be used to embed images.
        
        @param file: The path to the file you wish to attach, or an
                     instance of a file-like object.
        
        @param name: You can optionally override the filename of the
                     attached file.  This name will appear in the
                     recipient's mail viewer.  B{Optional if passing
                     an on-disk path.  Required if passing a file-like
                     object.}
        @type name: string
        """
        
        if isinstance(file, (str, unicode)):
            fp = open(file, "rb")
            name = os.path.basename(file)
        else:
            assert name is not None, "If embedding a file-like object, you must pass a custom filename."
            fp = file
        
        part = MIMEImage(fp.read(), name=name)
        fp.close()
        
        del part['Content-Disposition']
        part.add_header('Content-Disposition', 'inline', filename=name)
        part.add_header('Content-ID', '<%s>' % name)
        
        self.embedded.append(part)
    
    def _callable(self, var):
        if callable(var):
            return var()
        return var
    
    # --------------------------------------------------------------------------
    # Deprecated properties 
    
    def get_replyto(self):
        self._warn_about_deprecated_property('replyto', 'reply_to')
        return self.reply_to
    
    def set_replyto(self, replyto):
        self._warn_about_deprecated_property('replyto', 'reply_to')
        self.reply_to = replyto
    replyto = property(fget=get_replyto, fset=set_replyto)
