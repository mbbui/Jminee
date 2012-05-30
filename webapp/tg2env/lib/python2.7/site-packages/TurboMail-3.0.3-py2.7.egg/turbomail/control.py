# encoding: utf-8

"""TurboMail startup and shutdown interface.

To start and stop TurboMail in your own applications::

  import turbomail
  
  turbomail.interface.config = {'mail.on': True, ...}
  turbomail.interface.start()
  
  message = turbomail.Message(...)
  turbomail.interface.send(message)
  
  turbomail.interface.stop()

Remember to configure your outbound settings in the config dictionary.

TurboMail will, by default, immediately delete any messages remaining in
the queue and wait on any in-progress deliveries.
"""


import logging
import warnings

import pkg_resources

from turbomail.exceptions import MailNotEnabledException


__all__ = ['extension']

log = logging.getLogger("turbomail.control")



class ControlClass(object):
    """Control TurboMail startup and shutdown."""
    
    def __init__(self):
        self.running = False
        self._loaded_extensions = []
        self.config = dict()
        self.manager = None
    
    def __load_single_entry(self, group, name):
        for entrypoint in pkg_resources.iter_entry_points(group, name):
            return entrypoint.load()
        
        return None
    
    def _is_extension_enabled(self, extension_name):
        config_name = "mail.%s.on" % extension_name
        return self.config.get(config_name, False)
    
    def _initialize_extension(self, extension_name, extension):
        log.info("Loading extension '%s'." % extension_name)
        
        if hasattr(extension, 'interface'):
            extension = extension.interface
        
        elif hasattr(extension, 'load'):
            extension = extension.load()
        
        if hasattr(extension, 'start'):
            extension.start()
        
        self._loaded_extensions.append(extension)
    
    def _find_and_initialize_extensions_with_setuptools(self):
        extensions = pkg_resources.iter_entry_points("turbomail.extensions")
        for entrypoint in extensions:
            extension_name = entrypoint.name
            log.debug("Found extension '%s'." % extension_name)
            if self._is_extension_enabled(extension_name):
                extension = entrypoint.load()
                self._initialize_extension(extension_name, extension)
    
    def _initialize_extensions_from_dict(self, extra_classes):
        for extension_name in extra_classes:
            if self._is_extension_enabled(extension_name):
                extension = extra_classes[extension_name]
                self._initialize_extension(extension_name, extension)
    
    def initialize_enabled_extensions(self, extra_classes):
        if extra_classes is None:
            self._find_and_initialize_extensions_with_setuptools()
        else:
            self._initialize_extensions_from_dict(extra_classes)
    
    def start(self, config, extra_classes=None):
        self.config = config
        if not self.config.get("mail.on", False):
            return
        
        log.info("TurboMail extension starting up.")
        
        def load(t, default, extra_classes):
            extension = self.config.get("mail.%s" % t, default)
            if extra_classes != None and extension in extra_classes:
                controller = extra_classes[extension]
                if isinstance(controller, type):
                    controller = controller()
            else:
                entry_point = "turbomail.%ss" % t
                controller = self.__load_single_entry(entry_point, extension)
            if not controller:
                self.config.update({"mail.on": False})
                log.error("Unable to locate %s %s, TurboMail disabled." % (extension, t))
                self.stop(force=True)
                return
            setattr(self, t, controller)
            if hasattr(getattr(self, t), 'load'):
                setattr(self, t, getattr(self, t).load())
            if hasattr(getattr(self, t), 'start'):
                getattr(self, t).start()
        
        # Load the requested manager and transport.
        load('manager', 'immediate', extra_classes)
        load('transport', 'debug', extra_classes)
        
        self.initialize_enabled_extensions(extra_classes)
        self.running = True
    
    def _stop_all_loaded_extensions(self):
        for extension in self._loaded_extensions:
            if hasattr(extension, 'stop'):
                extension.stop()
        self._loaded_extensions = []
    
    def stop(self, force=False):
        if not self.running and not force: 
            return
        log.info("TurboMail extension shutting down.")
        
        self._stop_all_loaded_extensions()
        if self.manager and hasattr(self.manager, "stop"): 
            self.manager.stop()
        self.manager = None
        self.running = False
    
    def send(self, message):
        if not self.manager:
            raise MailNotEnabledException
        if isinstance(message, dict):
            from turbomail import WrappedMessage
            text = 'Sending pre-generated messages in dicts is deprecated, ' + \
                   'please use WrappedMessage instead.' 
            warnings.warn(text, category=DeprecationWarning)
            message = WrappedMessage(message['sender'], message['recipients'], 
                                     message['message'])
        return self.manager.deliver(message)


interface = ControlClass()
