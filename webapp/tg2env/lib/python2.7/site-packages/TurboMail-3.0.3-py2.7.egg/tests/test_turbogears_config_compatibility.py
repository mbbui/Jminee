#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Test that interface.config does not need to be a real dict."""

from pymta.api import IMTAPolicy
from pymta.test_util import SMTPTestCase

from turbomail.control import interface
from turbomail.message import Message
from turbomail.managers.immediate import ImmediateManager
from turbomail.transports.smtp import SMTPTransportFactory


class TurboGearsFakeConfig(object):
    def __init__(self, config):
        self.config = config.copy()
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def update(self, values):
        self.config.update(values)


class TestTurboGearsConfigWorks(SMTPTestCase):
    
    def setUp(self):
        real_config = {'mail.on': True, 'mail.manager': 'immediate', 
                       'mail.transport': 'smtp', 'mail.brand': False}
        self.config = TurboGearsFakeConfig(real_config)
        self.fake_setuptools =  {'immediate': ImmediateManager,
                                 'smtp': SMTPTransportFactory()}
        super(TestTurboGearsConfigWorks, self).setUp()
        
        self.msg = Message('foo@example.com', 'to@example.com', 'Test', 
                           plain='Plain text body')
    
    def tearDown(self):
        interface.stop(force=True)
        interface.config = {'mail.on': False}
        super(TestTurboGearsConfigWorks, self).tearDown()
    
    def init_mta(self, policy_class=IMTAPolicy):
        super(TestTurboGearsConfigWorks, self).init_mta(policy_class)
        self.connection_string = '%s:%s' % (self.hostname, self.listen_port)
        self.config.update({'mail.smtp.server': self.connection_string})
        # We must not assume that TurboMail is installed with egg-info
        interface.start(self.config, extra_classes=self.fake_setuptools)
    
    
    def test_message_sending_does_not_assume_dict_for_interface_config(self):
        self.msg.send()
        
        queue = self.deliverer.received_messages
        self.assertEqual(1, queue.qsize())


