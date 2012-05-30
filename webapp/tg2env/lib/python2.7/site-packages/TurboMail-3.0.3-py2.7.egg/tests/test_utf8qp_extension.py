# encoding: utf-8
"""Test the TurboMail Message class."""

import email
import logging
import unittest

from turbomail.control import interface
from turbomail.extensions.utf8qp import UTF8QuotedPrintable
from turbomail.managers.immediate import ImmediateManager
from turbomail.message import Message
from turbomail.transports.debug import DebugTransportFactory

logging.disable(logging.WARNING)


class TestUTF8QPExtension(unittest.TestCase):
    
    def build_message(self):
        msg = Message('from@example.com', 'to@example.com', 
                      subject='Test message subject.',
                      plain='This is a test message plain text body.'
                     )
        return msg
    
    def setUp(self):
        self._old_config = interface.config.copy()
        self.config = {'mail.on': True}
        self.fake_setuptools =  {'immediate': ImmediateManager,
                                 'debug': DebugTransportFactory,
                                 'utf8qp': UTF8QuotedPrintable()}
        self.message = self.build_message()
    
    def tearDown(self):
        interface.stop(force=True)
        interface.config = self._old_config
    
    def test_utf8qp_extension_reconfigures_utf8_setting(self):
        self.config['mail.utf8qp.on'] =  True
        interface.start(self.config, extra_classes=self.fake_setuptools)
        
        self.message.encoding = 'utf-8'
        msg = email.message_from_string(str(self.message))
        self.assertEqual('text/plain; charset="utf-8"', msg['Content-Type'])
        self.assertEqual('quoted-printable', msg['Content-Transfer-Encoding'])
    
    def test_with_extension_utf8_encoding_uses_base64(self):
        self.config['mail.utf8qp.on'] =  False
        interface.start(self.config, extra_classes=self.fake_setuptools)
        
        self.message.encoding = 'utf-8'
        msg = email.message_from_string(str(self.message))
        self.assertEqual('text/plain; charset="utf-8"', msg['Content-Type'])
        self.assertEqual('base64', msg['Content-Transfer-Encoding'])

