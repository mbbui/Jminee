# encoding: utf-8

import warnings

from turbomail.control import interface
from turbomail.exceptions import *
from turbomail.message import *
from turbomail.wrappedmessage import *


__all__ = ['send', 'enqueue', 'Message', 'WrappedMessage']



def send(message):
    '''Send a message via TurboMail.'''
    
    return interface.send(message)


def enqueue(message):
    '''Compatability function; use send(message) instead.'''
    
    warnings.warn(
            '"enqueue(message)" is deprecated, please use send(message) instead.',
            category=DeprecationWarning
        )
    
    return send(message)
