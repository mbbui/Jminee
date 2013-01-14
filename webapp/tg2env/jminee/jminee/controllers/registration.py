# -*- coding: utf-8 -*-
"""Main Controller"""
import pylons
from tg import TGController
from routes import url_for
from tg.decorators import Decoration
from tg import expose, flash, require, url, lurl, request, redirect, validate, config
from tg.i18n import ugettext as _, lazy_ugettext as l_
import tw
import logging

from jminee.lib import send_email
from datetime import datetime

from jminee.lib.base import BaseController
from jminee.model import DBSession, metadata, Registration, User, ResetPassword

from formencode.validators import UnicodeString, String, Email
from jminee.lib import validators
from jminee.controllers.error import ErrorController
from jminee.lib.errorcode import ErrorCode

log = logging.getLogger(__name__)
    
class RegistrationController(BaseController):
    config['renderers']=['json']
    
    @expose('jminee.templates.error')
    def error(self, *args, **kw):        
        return dict(kw)
        
    @expose('json')
    @validate(dict(email_address=validators.UniqueEmailValidator(not_empty=True),
                   password=String(not_empty=True)),                   
              error_handler=ErrorController.failed_input_validation)    
    def index(self, *args, **kw):
        try:
            log.info('User registration: %s'%str(kw))
            new_reg = Registration()
            new_reg.email_address = kw['email_address']
            new_reg.user_name = kw['email_address']
            new_reg.password = kw['password']
            new_reg.code = Registration.generate_code(kw['email_address'])
            DBSession.add(new_reg)
            DBSession.flush()

            email_data = {'sender':config['registration.email_sender'],
                      'subject':_('Message from Jminee'),
                      'body':'''
Please click on this link to confirm your registration

%s
''' % (url_for(self.mount_point+'/activate', code=new_reg.code, email=new_reg.email_address, qualified=True))}

        
            send_email(new_reg.email_address, email_data['sender'], email_data['subject'], email_data['body'])
        except Exception as e:
            log.exception('Got exception')
            return dict(success=False)
        return dict(success=True, email=kw['email_address'])
    
    @expose('json')
    @validate(dict(code=UnicodeString(not_empty=True),
                   password=String(not_empty=True),
                   email_address=Email(not_empty=True)),
              error_handler=ErrorController.failed_input_validation)      
    def reset_password(self, *agrs, **kw):
        try:
            log.info('User reset password: %s'%str(kw))
            ResetPassword.clear_expired_user(kw['email_address'])
            reset = ResetPassword.get_inactive(kw['email_address'], kw['code'])
            if not reset:
                return dict(success=False, error_code=ErrorCode.NORESETRECORD)
            
            user=DBSession.query(User).filter_by(email_address=kw['email_address']).first()
            user.password = kw['password']
            
            reset.email = kw['email_address'] 
            reset.reset = datetime.now()
        
            DBSession.flush()
            return dict(success=True)
        except Exception as e:
            log.exception('Got exception')
            return dict(success=False, error_code=ErrorCode.OTHERS)
            
    
    @expose('json')
    @validate(dict(email=Email(not_empty=True)))      
    def email_exist(self, *agrs, **kw):
        try:
            log.info('Check email existence: %s'%str(kw))
            
            user=DBSession.query(User).filter_by(email_address=kw['email']).first()
            if user:
                return dict(success=True, email_exist=True)
            return dict(success=True, email_exist=False)
        
        except Exception as e:
            log.exception('Got exception')
            return dict(success=False, error_code=ErrorCode.OTHERS)
    
    @expose('jminee.templates.index')
#    @validate(dict(code=UnicodeString(not_empty=True),
#                  email=validators.UniqueEmailValidator(not_empty=True)),
#              error_handler=errorhtml)
    def activate(self, email, code):
        try:
            log.info('User activation email=%s code=%s'%(email, code))
            Registration.clear_expired_user(email)
            
            reg = Registration.get_inactive(email, code)
            if not reg:
                user=DBSession.query(User).filter_by(email_address=email).first()
                if user:
                    return dict()
                else:
                    return redirect('/registration/error')
    
            u = User(user_name=reg.user_name,
                               display_name=reg.user_name,
                               email_address=reg.email_address,
                               password=reg.password)
         
            DBSession.add(u)
    
            reg.user = u
            reg.password = '******'
            reg.activated = datetime.now()
            return dict()        
        except:
            log.exception('Got exception')
            #TODO return error page
            return redirect('/registration/error', message='Sorry your account cannot be activated. Please send email to ...')
#            return redirect('/registration/errorhtml')
    
    @expose('json')
    @validate(dict(email_address=Email(not_empty=True)), 
              error_handler=ErrorController.failed_input_validation)
    def forget_password(self, *args, **kw):
        try:
            email_address = kw['email_address']
            user=DBSession.query(User).filter_by(email_address=email_address).first()
            if not user:
                return dict(success=False, error_code=ErrorCode.NONEXISTEDUSER)
                                                
            log.info("Reset password: %s"%email_address)
            reset_pwd = ResetPassword()
            reset_pwd.email_address=email_address
            reset_pwd.code = Registration.generate_code(email_address)
            
            DBSession.add(reset_pwd)
            DBSession.flush()
            
            email_data = {'sender':config['registration.email_sender'],
                      'subject':_('Message from Jminee'),
                      'body':'''
Please click on this link to reset your password

%s
''' % (url_for(self.mount_point+'/confirm_reset', code=reset_pwd.code, email=reset_pwd.email_address, qualified=True))}

        
            send_email(reset_pwd.email_address, email_data['sender'], email_data['subject'], email_data['body'])
        except Exception as e:
            log.exception('Got exception')
            return dict(success=False)
        return dict(success=True)
    
    @expose()
    @validate(dict(code=UnicodeString(not_empty=True),
                  email=validators.UniqueEmailValidator(not_empty=True)), error_handler=error)
    def confirm_reset(self, email, code):
        return redirect('/')
    
    