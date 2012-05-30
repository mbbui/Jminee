# encoding: utf-8

"""Compatibility module that exports symbols in a unified way on different 
versions of Python."""


# Python 2.3 does not have the built-in type 'set'
try:
    set = set

except NameError:
    from sets import Set as set


# In Python 2.5 the email modules were renamed for PEP-8 compliance
try:
    from email import charset
    from email.encoders import encode_base64
    from email.header import Header
    from email.mime.base import MIMEBase
    from email.mime.image import MIMEImage
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.utils import formataddr, formatdate, make_msgid, parseaddr, parsedate_tz

except ImportError:
    from email import Charset as charset
    from email.Encoders import encode_base64
    from email.Header import Header
    from email.MIMEBase import MIMEBase
    from email.MIMEImage import MIMEImage
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.Utils import formataddr, formatdate, make_msgid, parseaddr, parsedate_tz


def get_message(e):
    # In Python 2.6 direct access to the property e.message is deprecated 
    # (see PEP 352). To circumvent the DeprecationWarnings we just use the same
    # algorithm as Python 2.6 itself. Furthermore e.message won't work for 
    # Python 2.3 so probably it's best just to access e.args[0] for Python 2.x.
    if hasattr(e, 'args') and len(e.args) == 1:
        return e.args[0]
    else:
        return ''
