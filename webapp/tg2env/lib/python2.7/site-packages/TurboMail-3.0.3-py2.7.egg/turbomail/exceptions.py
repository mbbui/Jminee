# encoding: utf-8

"""Exceptions used by TurboMail to report common errors."""


__all__ = [
        'MailException',
        'MailNotEnabledException', 
        'MailConfigurationException',
        'TransportException', 
        'TransportExhaustedException',
        'ManagerException'
    ]



class MailException(Exception):
    """The base for all TurboMail exceptions."""
    pass


class MailNotEnabledException(MailException):
    """Attempted to use TurboMail before being enabled."""
    
    def __str__(self):
        return "An attempt was made to use a facility of the TurboMail " \
               "framework but outbound mail hasn't been enabled in the " \
               "config file [via mail.on]."


class MailConfigurationException(MailException):
    """There was an error in the configuration of TurboMail."""
    
    pass


class TransportException(MailException):
    """The base for all TurboMail Transport exceptions."""
    
    pass


class TransportExhaustedException(MailException):
    """Attempted to use TurboMail before being enabled."""
    
    def __str__(self):
        return "This Transport instance is no longer capable of delivering mail."


class ManagerException(MailException):
    """The base for all TurboMail Manager exceptions."""
    pass
