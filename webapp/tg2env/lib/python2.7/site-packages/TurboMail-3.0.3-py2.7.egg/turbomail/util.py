# encoding: utf-8

"""TurboMail utility functions and support classes."""


from turbomail.compat import Header, formataddr, parseaddr
from turbomail.email_validator import EmailValidator, ValidationException


__all__ = ['Address', 'AddressList']



class Address(object):
    """Validated electronic mail address class.
    
    This class knows how to validate and format e-mail addresses.  It
    uses Python's built-in `parseaddr` and `formataddr` helper
    functions and helps guarantee a uniform base for all e-mail
    address operations.
    
    The AddressList unit tests provide comprehensive testing of this
    class as well."""
    
    def __init__(self, name_or_email, email=None):
        if email == None:
            if isinstance(name_or_email, AddressList):
                assert len(name_or_email) > 0
                name_or_email = str(name_or_email[0])
            if isinstance(name_or_email, basestring):
                self.name, self.address = parseaddr(name_or_email)
            elif not isinstance(name_or_email, basestring):
                self.name, self.address = name_or_email
        else:
            self.name = name_or_email
            self.address = email
        if not self.is_valid_address(self.address):
            raise ValueError, 'Invalid e-mail address.'
    
    def __cmp__(self, other):
        if isinstance(other, (Address, basestring)):
            return cmp(str(self), str(other))
        elif isinstance(other, tuple):
            return cmp((self.name, self.address), other)
        return cmp(self, other)
    
    def __repr__(self):
        return 'Address(\'%s\')' % str(self)
    
    def __str__(self):
        return self.encode()
    
    def encode(self, encoding="ascii"):
        assert self.address, "You must specify an address."
        name_string = self.name
        if isinstance(name_string, unicode):
            name_string = str(Header(name_string, encoding))
        
        # Encode punycode for internationalized domains.
        localpart, domain = self.address.split('@', 1)
        if isinstance(domain, unicode):
            domain = domain.encode('idna')
        address = '@'.join((localpart, domain))
        
        return formataddr((name_string, address)).replace('\n', '')
    
    def is_valid_address(self, address):
        try:
            EmailValidator().validate_or_raise(address)
            return True
        except ValidationException:
            return False


class AddressList(list):
    def __init__(self, addresses=[], encoding=None):
        super(AddressList, self).__init__()
        
        self.encoding = encoding
        if isinstance(addresses, basestring):
            addresses = addresses.split(',')
        
        elif isinstance(addresses, tuple):
            addresses = [addresses]
        
        if addresses is not None:
            self.extend(addresses)
    
    def __repr__(self):
        if not self:
            return "AddressList()"
        
        return "AddressList(\"" + "\", \"".join([str(i) for i in self]) + "\")"
    
    def __str__(self):
        return self.encode(self.encoding)
    
    def encode(self, encoding="ascii"):
        addresses = []
        for address in self:
            addresses.append(address.encode(encoding))
        return ", ".join(addresses)
    
    def __setitem__(self, k, value):
        if not isinstance(value, Address):
            value = Address(value)
        super(AddressList, self).__setitem__(k, value)
    
    def extend(self, value):
        values = []
        for i in value:
            if not isinstance(i, Address):
                i = Address(i)
            values.append(i)
        super(AddressList, self).extend(values)
    
    def append(self, value):
        self.extend([value])
    
    def addresses(self):
        return AddressList([i.address for i in self])
    addresses = property(addresses)
    
    def string_addresses(self):
        """Return a list of string representations of the addresses suitable for
        usage in an SMTP transaction."""
        address_strings = []
        for address in self:
            address_strings.append(str(address))
        return address_strings
    string_addresses = property(string_addresses)
    
    def protected(cls, field):
        def fget(self):
            return getattr(self, field)
        
        def fset(self, value):
            if not isinstance(value, AddressList):
                value = AddressList(value)
            setattr(self, field, AddressList(value))
        
        def fdel(self):
            setattr(self, field, AddressList())
        
        return property(fget, fset, fdel)
    protected = classmethod(protected)
