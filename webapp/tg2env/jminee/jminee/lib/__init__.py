# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from smtplib import SMTP
import sys
from tg import config

try:
    import turbomail
except ImportError:
    turbomail = None

def _plain_send_mail(sender, recipient, subject, body):
    header_charset = 'ISO-8859-1'
    for body_charset in 'US-ASCII', 'ISO-8859-1', 'UTF-8':
        try:
            body.encode(body_charset)
        except UnicodeError:
            pass
        else:
            break

    sender_name, sender_addr = parseaddr(sender)
    recipient_name, recipient_addr = parseaddr(recipient)

    sender_name = str(Header(unicode(sender_name), header_charset))
    recipient_name = str(Header(unicode(recipient_name), header_charset))

    sender_addr = sender_addr.encode('ascii')
    recipient_addr = recipient_addr.encode('ascii')

    msg = MIMEText(body.encode(body_charset), 'plain', body_charset)
    msg['From'] = formataddr((sender_name, sender_addr))
    msg['To'] = formataddr((recipient_name, recipient_addr))
    msg['Subject'] = Header(unicode(subject), header_charset)

    smtp = SMTP(config.get('registration.smtp_host', 'localhost'))
    if config.get('registration.smtp_login'):
        try:
            smtp.starttls()
        except:
            pass
        smtp.login(config.get('registration.smtp_login'), config.get('registration.smtp_passwd'))
    smtp.sendmail(sender, recipient, msg.as_string())
    smtp.quit()

def send_email(to_addr, from_addr, subject, body):
    # Using turbomail if it exists, 'dumb' method otherwise
    if turbomail and config.get('mail.on'):
        msg = turbomail.Message(from_addr, to_addr, subject)
        msg.plain = body
        turbomail.send(msg)
    else:
        _plain_send_mail(from_addr, to_addr, subject, body)
        
def send_email2(to_addr, from_addr, subject, plain, rich):
    # Using turbomail if it exists, 'dumb' method otherwise
    if turbomail and config.get('mail.on'):
        msg = turbomail.Message(from_addr, to_addr, subject)
        if rich:
            msg.rich = rich
        msg.plain = plain
        turbomail.send(msg)
    else:
        ##TODO: should raise exception here
        pass        
