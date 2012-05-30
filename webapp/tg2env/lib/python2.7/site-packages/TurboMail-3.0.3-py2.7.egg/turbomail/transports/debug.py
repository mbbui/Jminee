# encoding: utf-8

"""Deliver to the logging system and store a cache."""


import copy
import logging

from turbomail.api import TransportFactory, Transport


__all__ = ['load']

log = logging.getLogger("turbomail.transport")
deliverylog = logging.getLogger("turbomail.delivery")



def load():
    return DebugTransportFactory()


class DebugTransport(Transport):
    def __init__(self):
        super(DebugTransport, self).__init__()
        log.debug("Debug transport setup.")
        self._sent_mails = []
    
    def deliver(self, message):
        log.info("Attempting delivery of message %s." % message.id)
        deliverylog.info("%s DELIVER" % message.id)
        msg_string = str(message)
        self._sent_mails.append(msg_string)
        for i in msg_string.split("\n"):
            deliverylog.debug("%s BODY %s" % (message.id, str(i)))
        
        deliverylog.info("%s SENT" % message.id)
        return True
    
    def get_sent_mails(self):
        return copy.copy(self._sent_mails)


class DebugTransportFactory(TransportFactory):
    name = "debug"
    transport = DebugTransport
