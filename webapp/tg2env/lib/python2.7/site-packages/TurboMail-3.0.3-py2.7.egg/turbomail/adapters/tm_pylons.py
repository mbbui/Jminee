# encoding: utf-8

"""Pylons (and thus TurboGears 2) helper functions."""


import atexit
import re

from paste.deploy.converters import asbool
from pylons import config

from turbomail.control import interface


__all__ = ['start_extension', 'shutdown_extension']



class FakeConfigObj(object):
    """TODO: Docstring incomplete."""
    
    def __init__(self, real_config):
        self._config = real_config
        self._nr_regex = re.compile('^(\d+)$')
    
    def get(self, option, default):
        value = self._config.get(option, default)
        return self._convert(option, value)
    
    def _convert(self, option, value):
        if value is not None:
            boolean_options = (
                    'mail.smtp.tls',
                    'mail.tls',
                    'mail.smtp.debug', 
                    'mail.debug'
                )
            
            should_be_bool = (option.endswith('.on') or (option in boolean_options))
            
            if should_be_bool:
                value = asbool(value)
            
            elif hasattr(value, 'isdigit') and value.isdigit():
                value = int(value)
        
        return value
    
    def update(self, new_value_dict):
        self._config.update(new_value_dict)


def start_extension():
    # There is no guarantee that atexit calls shutdown but Pylons does not 
    # provide other mechanisms!
    atexit.register(shutdown_extension)
    
    # interface.start will exit immediately if TurboMail is not enabled.
    interface.start(FakeConfigObj(config))


def shutdown_extension():
    interface.stop()
