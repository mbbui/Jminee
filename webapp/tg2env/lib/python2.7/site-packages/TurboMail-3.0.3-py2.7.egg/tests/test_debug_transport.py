#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Test that the debug transport stores all "sent" mails.'''

import unittest

from turbomail.control import interface
from turbomail import Message, WrappedMessage
from turbomail.managers.immediate import ImmediateManager
from turbomail.transports.debug import DebugTransportFactory

class TestDebugTransportStoresAllMail(unittest.TestCase):
    
    def setUp(self):
        config = {'mail.on': True, 
                  'mail.manager': 'immediate', 'mail.transport': 'debug',}
        # conciously using classes and instances for fake_setuptools so that
        # the test also checks that TurboMail will do the right thing.
        fake_setuptools =  {'immediate': ImmediateManager,
                            'debug': DebugTransportFactory()}
        interface.start(config, extra_classes=fake_setuptools)
        self.msg = Message('foo@example.com', 'to@example.com', 'Test', 
                           plain='Plain text body')
    
    def transport(self):
        return interface.manager.transport
    transport = property(transport)
    
    def tearDown(self):
        interface.stop(force=True)
        interface.config = {'mail.on': False}
    
    def test_fetch_sent_messages(self):
        msg_string = str(self.msg)
        self.msg.send()
        
        stored_mails = self.transport.get_sent_mails()
        self.assertEqual(1, len(stored_mails))
        self.assertEqual(msg_string, str(stored_mails[0]))
    
    def test_message_send_themselves(self):
        msg_string = str(self.msg)
        self.msg.send()
        
        stored_mails = self.transport.get_sent_mails()
        self.assertEqual(1, len(stored_mails))
        self.assertEqual(msg_string, str(stored_mails[0]))
    
    def test_wrapped_messages_send_themselves(self):
        msg_string = 'Subject: Test\n\nJust testing...'
        msg = WrappedMessage('foo@example.com', 'to@example.com', msg_string)
        msg.send()
        
        stored_mails = self.transport.get_sent_mails()
        self.assertEqual(1, len(stored_mails))
        self.assertEqual(msg_string, str(stored_mails[0]))

