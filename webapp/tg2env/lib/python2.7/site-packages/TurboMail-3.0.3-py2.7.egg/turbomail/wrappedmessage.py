# encoding: utf-8

import email

from turbomail.compat import make_msgid
from turbomail.message import BaseMessage
from turbomail.util import Address, AddressList


__all__ = ['WrappedMessage']



class ImmutableProxy(object):
    """This is a wrapper for email.Message so that a user can not modify the
    Message instance easily - actually modifications won't have any effect on
    the underlying message class but with this wrapper newbies won't fall into
    the trap."""
    def __init__(self, obj):
        self._obj = obj
    
    def __contains__(self, name):
        return (name in self._obj)
    
    def __getattr__(self, name):
        if name is not None:
            for prefix in ['set_', 'replace_', 'add_', 'del_']:
                if name.startswith(prefix):
                    raise TypeError('This instance is not mutable!')
            if name in ['attach']:
                raise TypeError('This instance is not mutable!')
        return getattr(self._obj, name)
    
    def __getitem__(self, name):
        return self._obj[name]
    
    def __len__(self):
        return len(self._obj)


class WrappedMessage(BaseMessage):
    """This is a wrapper for arbitrary messages so you can send RFC822 messages 
    that were previously assembled (e.g. read from the filesystem)."""
    
    def __init__(self, smtp_from=None, to=None, message=None, **kw):
        super(WrappedMessage, self).__init__(smtp_from=smtp_from, to=to, kw=kw)
        self.message = message
        self._id = None
        self._email_msg = None
        if len(kw) > 0:
            parameter_name = kw.keys()[0]
            error_msg = "__init__() got an unexpected keyword argument '%s'"
            raise TypeError(error_msg % parameter_name)
    
    def __setattr__(self, name, value):
        "Reset cached values if new ones are set."
        super(WrappedMessage, self).__setattr__(name, value)
        if name == 'message':
            # Prevent recursion - circumvent __setattr__
            self.__dict__['_id'] = None
            self.__dict__['_email_msg'] = None
    
    def __str__(self):
        return self.message
    
    def envelope_sender(self):
        """Returns the address of the envelope sender address (SMTP from)."""
        return Address(self.smtp_from)
    envelope_sender = property(envelope_sender)
    
    def id(self):
        """Get an ID for the message which is used for logging.
        The idea is to use the message id if it is available, otherwise a 
        generated message id."""
        if self._id is None:
            msg_id = None
            if self.message is not None:
                if self.email_msg is not None:
                    msg_id = self.email_msg['Message-ID']
            if msg_id is None:
                msg_id = make_msgid()
            self.__dict__['_id'] = msg_id
        return self._id
    id = property(id)
    
    def email_msg(self):
        """Return an email.Message built from the current message. 
        
        Please note that updating properties in the returned Message will not 
        update the real message content (msg). If you change the message content,
        a previously returned Message from this method will not be updated, 
        instead a new Message instance will be returned if you call this method
        again."""
        if self._email_msg is None:
            msg = email.message_from_string(str(self))
            self.__dict__['_email_msg'] = ImmutableProxy(msg)
        return self._email_msg
    email_msg = property(email_msg)
    
    def recipients(self):
        return AddressList(self.to)
    recipients = property(recipients)
