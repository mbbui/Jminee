# -*- coding: utf-8 -*-
"""Main Controller"""
import pylons
from tg import TGController
from routes import url_for
from tg.decorators import Decoration
from tg import expose, flash, require, url, lurl, request, redirect, validate, config
from tg.i18n import ugettext as _, lazy_ugettext as l_
import tw

from jminee.lib import send_email
from datetime import datetime

from jminee.lib.base import BaseController
from jminee.model import DBSession, metadata, Registration, User

from formencode.validators import UnicodeString
from jminee.lib import validators

class RegistrationController(BaseController):
    config['renderers']=['json']
    
    @expose('json')
    def error(self, *args, **kw):
        print pylons.tmpl_context.form_errors
        error_list=pylons.tmpl_context.form_errors
        Registration.clear_expired()
        return dict(success=False, errors=error_list)
   
    @expose('json')
    @validate(dict(email_address=validators.UniqueEmailValidator(),
                   user_name=validators.UniqueUserValidator(),
                   password_confirm=validators.PasswordMatch('password', 'password_confirm')),                   
               error_handler=error)    
    def submit(self, *args, **kw):
        hooks = config['hooks'].get('registration.before_registration', [])
        for func in hooks:
            func(kw)
        try:
            new_reg = Registration()
            new_reg.email_address = kw['email_address']
            new_reg.user_name = kw['user_name']
            new_reg.password = kw['password']
            new_reg.code = Registration.generate_code(kw['email_address'])
            DBSession.add(new_reg)
            DBSession.flush()

            #hooks = config['hooks'].get('registration.after_registration', [])
            #for func in hooks:
            #    func(new_reg, kw)

            email_data = {'sender':config['registration.email_sender'],
                      'subject':_('Please confirm your registration'),
                      'body':'''
Please click on this link to confirm your registration

%s
''' % (url_for(self.mount_point+'/activate', code=new_reg.code, email=new_reg.email_address, qualified=True))}

            #hooks = config['hooks'].get('registration.on_complete', [])
            #for func in hooks:
            #    func(email_data)

            send_email(new_reg.email_address, email_data['sender'], email_data['subject'], email_data['body'])
        except Exception as e:
            print e
            return dict(success=False)
        return dict(success=True)

    
    @expose()
    @validate(dict(code=UnicodeString(not_empty=True),
                  email=validators.UniqueEmailValidator(not_empty=True)), error_handler=error)
    def activate(self, email, code):
        reg = Registration.get_inactive(email, code)
        if not reg:
            return dict(success=False)

        u = User(user_name=reg.user_name,
                           display_name=reg.user_name,
                           email_address=reg.email_address,
                           password=reg.password)
     
        DBSession.add(u)

        reg.user = u
        reg.password = '******'
        reg.activated = datetime.now()
               
        return redirect('/')
