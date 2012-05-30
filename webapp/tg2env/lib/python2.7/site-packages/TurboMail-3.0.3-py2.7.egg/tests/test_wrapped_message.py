#!/usr/bin/env python
# encoding: utf-8

import email

import logging
import unittest


from turbomail import WrappedMessage

logging.disable(logging.WARNING)

rfc822_msg = '''From: author@example.com
To: recipient@example.com
Message-ID: <20081231.21713.17885@localhost.localdomain>
Subject: Test Message

This is a test.'''

class TestWrappedMessage(unittest.TestCase):
    """Test WrappedMessage class which contains pre-built messages."""
    
    def setUp(self):
        self.message = WrappedMessage(('Author', 'author@example.com'),
                                      ('Recipient', 'recipient@example.com'),
                                      rfc822_msg)
        self.parsed_msg = email.message_from_string(str(self.message))
        self.msg_id = self.parsed_msg['Message-ID']
    
    def test_can_instantiate_wrapped_message_without_arguments(self):
        WrappedMessage()
    
    def test_set_smtp_from(self):
        msg = WrappedMessage('foo@example.com')
        self.assertEqual('foo@example.com', str(msg.smtp_from))
    
    def test_recipients(self):
        recipients = ['bar@example.com', 'baz@example.com']
        msg = WrappedMessage('foo@example.com', to=recipients)
        self.assertEqual(recipients, msg.recipients)
    
    def test_extract_id_from_msg_body(self):
        self.assertEqual(self.msg_id, self.message.id)
    
    def test_return_custom_id_if_no_body(self):
        self.message.message = None
        self.assertNotEqual(self.msg_id, self.message.id)
        self.assertNotEqual(None, self.message.id)
    
    def test_return_custom_id_if_no_id_in_body(self):
        del self.parsed_msg['Message-ID']
        self.message.message = self.parsed_msg.as_string()
        self.assertNotEqual(self.msg_id, self.message.id)
        self.assertNotEqual(None, self.message.id)
    
    def test_message_id_can_handle_broken_header(self):
        self.message.message = 'Foo Bar'
        self.assertNotEqual(self.msg_id, self.message.id)
        self.assertNotEqual(None, self.message.id)
    
    def test_id_and_msg_change_after_body_change(self):
        # Test property access/cache id
        self.message.id
        self.message.email_msg
        del self.parsed_msg['Message-ID']
        self.parsed_msg['Message-ID'] = 'Foo'
        self.message.message = self.parsed_msg.as_string()
        self.assertEqual('Foo', self.message.id)
        self.assertEqual('Foo', self.message.email_msg['Message-ID'])
    
    def test_parsed_message(self):
        msg = self.message.email_msg
        self.assertEqual('author@example.com', msg['From'])
        self.assertEqual('recipient@example.com', msg['To'])
        self.assertEqual(self.msg_id, msg['Message-ID'])
        self.assertEqual('Test Message', msg['Subject'])
    
    def test_can_not_set_headers_parsed_message(self):
        """Test that only an immutable wrapper is returned so that users can not
        change the message itself (this won't have any effect anyway)."""
        try:
            self.message.email_msg['Message-ID'] = 'changed'
            self.fail('Message ID must not be changed')
        except TypeError:
            pass
    
    def test_can_not_delete_headers_from_parsed_message(self):
        try:
            del self.message.email_msg['Message-ID']
            self.fail('Message ID must not be deleted')
        except TypeError:
            pass
    
    def test_immutable_proxy_implements_all_protocols(self):
        msg = self.message.email_msg
        self.failUnless('Message-ID' in msg)
        self.assertEqual(len(self.parsed_msg), len(msg))
    
    def test_replace_header_is_intercepted(self):
        msg = self.message.email_msg
        self.assertRaises(TypeError, lambda: getattr(msg.replace_header('Message-ID', 'evil')))
        self.assertEqual(self.msg_id, msg['Message-ID'])

