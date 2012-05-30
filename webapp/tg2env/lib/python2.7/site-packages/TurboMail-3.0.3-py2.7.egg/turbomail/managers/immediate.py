# encoding: utf-8

"""Blocking immediate delivery manager.

This delivers messages as soon as it is enqueued, without using threading."""


import logging

from turbomail.api import Manager
from turbomail.exceptions import TransportExhaustedException


__all__ = ['load']

log = logging.getLogger("turbomail.manager")



def load():
    return ImmediateManager()


class ImmediateManager(Manager):
    name = "immediate"
    
    def __init__(self):
        log.info("Immediate manager starting up.")
        self.transport = None
        super(ImmediateManager, self).__init__()
        log.info("Immediate manager ready.")
    
    def _shutdown_transport(self):
        if self.transport is not None:
            self.transport.stop()
        self.transport = None
    
    def stop(self):
        self._shutdown_transport()
        super(ImmediateManager, self).stop()
    
    def deliver(self, message):
        log.info("Attempting delivery of message %s." % message.id)
        
        # If the parent fails, we fail.
        if not super(ImmediateManager, self).deliver(message):
            log.debug("Parent failure.")
            return False
        
        if not self.transport:
            self.transport = self.get_new_transport()
        try:
            self.transport.deliver(message)
            log.info("Delivery of message %s successful." % message.id)
        except TransportExhaustedException:
            log.debug("Transport exhausted.")
            self._shutdown_transport()
            self.deliver(message)
        except:
            log.error("Delivery of message %s failed." % message.id)
            raise
        return True
