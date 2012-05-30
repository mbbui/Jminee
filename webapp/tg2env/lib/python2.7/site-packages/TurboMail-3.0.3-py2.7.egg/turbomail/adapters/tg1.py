# encoding: utf-8

"""TurboGears automatic startup/shutdown extension."""


from turbogears import config
from turbomail.control import interface


__all__ = ['start_extension', 'shutdown_extension']



def start_extension():
    # interface.start will exit immediately if TurboMail is not enabled.
    interface.start(config)


def shutdown_extension():
    interface.stop()
