# encoding: utf-8

"""TurboMail UTF-8 quoted-printable encoding extension."""


import logging

from turbomail.api import Extension
from turbomail.compat import charset


__all__ = ['interface', 'UTF8QuotedPrintable']

log = logging.getLogger("turbomail.extension.utf8qp")



class UTF8QuotedPrintable(Extension):
    name = 'utf8qp'
    
    def start(self):
        super(UTF8QuotedPrintable, self).start()
        
        log.info("Configuring UTF-8 character set to use Quoted-Printable encoding.")
        charset.add_charset('utf-8', charset.SHORTEST, charset.QP, 'utf-8')
        charset.add_charset('utf8', charset.SHORTEST, charset.QP, 'utf8')
    
    def stop(self):
        super(UTF8QuotedPrintable, self).stop()
        
        log.info("Configuring UTF-8 character set to use Base-64 encoding.")
        charset.add_charset('utf-8', charset.SHORTEST, charset.BASE64, 'utf-8')
        charset.add_charset('utf8', charset.SHORTEST, charset.BASE64, 'utf8')


interface = UTF8QuotedPrintable()
