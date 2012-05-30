#!/usr/bin/env python
# encoding: utf-8
"""Test the TurboMail Message class."""

import logging
import unittest

from turbomail.util import Address, AddressList


logging.disable(logging.WARNING)


class TestAddress(unittest.TestCase):
    def test_punycode(self):
        addr = Address("Foo", u"foo@exámple.test")
        self.assertEqual("Foo <foo@xn--exmple-qta.test>", str(addr))
    
    def test_initialization_with_addresslist_which_contains_only_email(self):
        emailaddress = 'foo@example.com'
        address = Address(AddressList(emailaddress))
        self.assertEqual(emailaddress, str(address))
    
    def test_initialization_with_addresslist_which_contains_tuple(self):
        name = 'Foo'
        emailaddress = 'foo@example.com'
        address = Address(AddressList((name, emailaddress)))
        self.assertEqual('%s <%s>' % (name, emailaddress), str(address))
    
    def test_initialization_with_tuple(self):
        name = 'Foo'
        emailaddress = 'foo@example.com'
        address = Address((name, emailaddress))
        self.assertEqual('%s <%s>' % (name, emailaddress), str(address))
    
    def test_initialization_with_string(self):
        emailaddress = 'foo@example.com'
        address = Address(emailaddress)
        self.assertEqual('%s' % emailaddress, str(address))
    
    def test_validation_truncates_at_second_at_character(self):
        # This is basically due to Python's parseaddr behavior.
        self.assertEqual('bad@user', Address("bad@user@example.com"))
    
    def test_validation_rejects_addresses_without_at(self):
        # TODO: This may be actually a valid input - some mail systems allow to
        # use only the local part which will be qualified by the MTA
        self.assertRaises(ValueError, Address, "baduser.example.com")
    
    def test_validation_accepts_uncommon_local_parts(self):
        Address("good-u+s+er@example.com")
        # This address caused 100% CPU load for 50s in Python's (2.5.2) re 
        # module on Fedora Linux 10 (AMD x2 4200).
        Address('steve.blackmill.rules.for.all@bar.blackmill-goldworks.example')
        Address('customer/department=shipping@example.com')
        Address('$A12345@example.com ')
        Address('!def!xyz%abc@example.com ')
        Address('_somename@example.com')
        Address('!$&*-=^`|~#%\'+/?_{}@example.com')
    
# TODO: Later
#    def test_validation_accepts_quoted_local_parts(self):
#        Address('"Fred Bloggs"@example.com ')
#        Address('"Joe\\Blow"@example.com ')
#        Address('"Abc@def"@example.com ')
#        Address('"Abc\@def"@example.com')
    
    def test_validation_accepts_multilevel_domains(self):
        Address('foo@my.my.company-name.com')
        Address('blah@foo-bar.example.com')
        Address('blah@duckburg.foo-bar.example.com')
    
    def test_validation_accepts_domain_without_tld(self):
        self.assertEqual('user@company', Address('user@company'))
    
    def test_validation_rejects_local_parts_starting_or_ending_with_dot(self):
        self.assertRaises(ValueError, Address, ".foo@example.com")
        self.assertRaises(ValueError, Address, "foo.@example.com")
    
    def test_validation_rejects_double_dot(self):
        self.assertRaises(ValueError, Address, "foo..bar@example.com")
    
# TODO: Later
#    def test_validation_rejects_special_characters_if_not_quoted(self):
#        for char in '()[]\;:,<>':
#            localpart = 'foo%sbar' % char
#            self.assertRaises(ValueError, Address, '%s@example.com' % localpart)
#            Address('"%s"@example.com' % localpart)
    
# TODO: Later
#    def test_validation_accepts_ip_address_literals(self):
#        Address('jsmith@[192.168.2.1]')



class TestAddressList(unittest.TestCase):
    """Test the AddressList helper class."""
    
    addresses = AddressList.protected('_addresses')
    
    def setUp(self):
        self._addresses = AddressList()
    
    def tearDown(self):
        del self.addresses
    
    def test_assignment(self):
        self.assertEqual([], self.addresses)
    
    def test_assign_single_address(self):
        address = "user@example.com"
        self.addresses = address
        
        self.assertEqual(self.addresses, [address])
        self.assertEqual(str(self.addresses), address)
    
    def test_assign_list_of_addresses(self):
        addresses = ["user1@example.com", "user2@example.com"]
        self.addresses = addresses
        self.assertEqual(", ".join(addresses), str(self.addresses))
        self.assertEqual(addresses, self.addresses)
    
    def test_assign_single_named_address(self):
        addresses = ("Test User", "user@example.com")
        self.addresses = addresses
        string_value = "%s <%s>" % addresses
        self.assertEqual(string_value, str(self.addresses))
        self.assertEqual([string_value], self.addresses)
    
    def test_assign_list_of_named_addresses(self):
        addresses = [("Test User 1", "user1@example.com"), 
                     ("Test User 2", "user2@example.com")]
        self.addresses = addresses
        
        string_addresses = map(lambda value: str(Address(*value)), addresses)
        self.assertEqual(", ".join(string_addresses), str(self.addresses))
        self.assertEqual(string_addresses, self.addresses)
    
    def test_init_accepts_string_list(self):
        addresses = "user1@example.com, user2@example.com"
        self.addresses = addresses
        
        self.assertEqual(addresses, str(self.addresses))
    
    def test_validation_strips_multiline_addresses(self):
        self.addresses = "user.name+test@info.example.com"
        evil_lines = ["eviluser@example.com", "To: spammeduser@example.com", 
                      "From: spammeduser@example.com"]
        evil_input = "\n".join(evil_lines)
        self.addresses.append(evil_input)
        self.assertEqual(["user.name+test@info.example.com", evil_lines[0]], 
                         self.addresses)
    
    def test_return_addresses_as_strings(self):
        self.addresses = u'foo@exámple.test'
        encoded_address = 'foo@xn--exmple-qta.test'
        self.assertEqual([encoded_address], self.addresses.string_addresses)

