#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Test that most interfaces of TurboMail 2.x are working in TurboMail 3.x'''

import email
import unittest
import warnings

import turbomail
from turbomail import Message, MailNotEnabledException
from turbomail.api import Transport
from turbomail.control import interface
from turbomail.managers.immediate import ImmediateManager
from turbomail.transports.debug import DebugTransportFactory

from tests.test_wrapped_message import rfc822_msg


class TurboMailTestCase(unittest.TestCase):
    def setUp(self):
        super(TurboMailTestCase, self).setUp()
        self._old_config = interface.config.copy()
    
    def tearDown(self):
        interface.stop(force=True)
        interface.config = self._old_config
        warnings.resetwarnings()
        super(TurboMailTestCase, self).tearDown()
    
    def _ignore_warning(self, msg_regex):
        warnings.filterwarnings('ignore', msg_regex, category=DeprecationWarning)


class TestTurboMail2xCompatibility(TurboMailTestCase):
    
    def setUp(self):
        super(TestTurboMail2xCompatibility, self).setUp()
        self._ignore_warning('Property ".+" is deprecated.*')
        self._ignore_warning('Please specify the author using.*')
        self._ignore_warning('.*enqueue.*')
        self._ignore_warning('.*WrappedMessage.*')
        self._ignore_warning('.*deprecated configuration option.*')
        self._ignore_warning('Configuration key ".+" is deprecated.*')
    
    def test_message_instantiation_with_positional_parameters(self):
        message = Message('from@example.com', 'to@example.com', 'Test')
        message.plain = 'Hello world!'
        msg_string = str(message)
        self.failUnless('From: from@example.com' in msg_string)
        self.failUnless('To: to@example.com' in msg_string)
        self.failUnless('Subject: Test' in msg_string)
    
    def test_message_instantiation_with_keyword_parameters(self):
        message = Message(sender='from@example.com', recipient='to@example.com',
                          subject='Test')
        message.plain = 'Hello world!'
        msg_string = str(message)
        self.failUnless('From: from@example.com' in msg_string)
        self.failUnless('To: to@example.com' in msg_string)
        self.failUnless('Subject: Test' in msg_string)
    
    def test_message_instantiation_with_tuples(self):
        message = Message(('Foo Bar', 'from@example.com'), 
                          ('To', 'to@example.com'), 'Test')
        message.plain = 'Hello world!'
        msg_string = str(message)
        self.failUnless('From: Foo Bar <from@example.com>' in msg_string)
        self.failUnless('To: To <to@example.com>' in msg_string)
        self.failUnless('Subject: Test' in msg_string)
    
    def test_message_plain_text_as_callable(self):
        message = Message('from@example.com', 'to@example.com', 'Test')
        message.plain = lambda: 'Hello world!'
        msg_string = str(message)
        self.failUnless('Hello world!' in msg_string)
    
    def test_message_properties(self):
        message = Message('from@example.com', 'to@example.com', 'Test')
        message.plain = 'Hello world!'
        
        property_names = ['bcc', 'cc', 'date', 'disposition', 'encoding',
                          'headers', 'organization', 'plain', 'priority',
                          'recipient', 'replyto', 'rich', 'sender', 'smtpfrom',
                          'subject']
        for name in property_names:
            getattr(message, name)
        
        args = dict(zip(property_names, ['foo@example.com'] * len(property_names)))
        Message(**args)
    
    def test_use_deprecated_smtp_from(self):
        message = Message(smtpfrom='smtpfrom@example.com')
        self.assertEqual('smtpfrom@example.com', str(message.smtp_from))
        self.assertEqual(message.smtpfrom, message.smtp_from)
        message.smtpfrom = 'smtp_from@example.com'
        self.assertEqual('smtp_from@example.com', str(message.smtp_from))
        self.assertEqual(message.smtpfrom, message.smtp_from)
    
    def test_use_deprecated_reply_to(self):
        message = Message(replyto='replyto@example.com')
        self.assertEqual('replyto@example.com', str(message.reply_to))
        self.assertEqual(message.replyto, message.reply_to)
        message.replyto = 'reply_to@example.com'
        self.assertEqual('reply_to@example.com', str(message.reply_to))
        self.assertEqual(message.replyto, message.reply_to)
    
    def test_use_deprecated_recipient(self):
        message = Message(recipient='recipient@example.com')
        self.assertEqual('recipient@example.com', str(message.to))
        self.assertEqual(message.recipient, message.to)
        message.recipient = 'to@example.com'
        self.assertEqual('to@example.com', str(message.to))
        self.assertEqual(message.recipient, message.to)
    
    def test_use_sender_for_author_if_no_author_given(self):
        message = Message(sender='sender@example.com', to='to@example.com', 
                          subject='Test')
        self.assertEqual('sender@example.com', str(message.sender))
        message.plain = 'Hello world!'
        msg_string = str(message)
        self.failUnless('From: sender@example.com' in msg_string)
        self.failUnless('To: to@example.com' in msg_string)
        self.failUnless('Subject: Test' in msg_string)
        self.failIf('Sender: ' in msg_string)
        self.assertEqual('sender@example.com', str(message.sender))
    
    def test_message_enqueue_not_enabled(self):
        message = Message('from@example.com', 'to@example.com', 'Test')
        message.plain = 'Hello world!'
        self.assertRaises(MailNotEnabledException, turbomail.enqueue, message)
    
    def test_mail_encoding_is_used_as_fallback(self):
        interface.config['mail.encoding'] = 'ISO-8859-1'
        message = Message('from@example.com', 'to@example.com', 'Test')
        message.plain = 'Hello world!'
        msg = email.message_from_string(str(message))
        self.assertEqual('text/plain; charset="iso-8859-1"', msg['Content-Type'])
        self.assertEqual('quoted-printable', msg['Content-Transfer-Encoding'])
    
    def test_message_enqueue(self):
        config = {'mail.on': True}
        fake_setuptools =  {'immediate': ImmediateManager,
                            'debug': DebugTransportFactory}
        interface.start(config, extra_classes=fake_setuptools)
        
        message = Message('from@example.com', 'to@example.com', 'Test')
        message.plain = 'Hello world!'
        turbomail.enqueue(message)
    
    def test_can_send_pregenerated_messages_with_dict(self):
        config = {'mail.on': True}
        fake_setuptools =  {'immediate': ImmediateManager,
                            'debug': DebugTransportFactory}
        interface.start(config, extra_classes=fake_setuptools)
        
        msg_info = dict(sender='from@example.com', recipients='to@example.com',
                        message=rfc822_msg)
        turbomail.enqueue(msg_info)
    
    def test_transports_fall_back_to_old_configuration_keys(self):
        interface.config['mail.debug'] = True
        interface.config['mail.truth'] = 42
        t = Transport()
        
        self.assertEqual(42, t.config_get('mail.smtp.debug', None, 'mail.truth'))
        self.assertEqual(True, t.config_get('mail.smtp.debug', None))


