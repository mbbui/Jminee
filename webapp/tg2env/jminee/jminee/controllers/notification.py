'''
Created on Jan 6, 2013

@author: bachbui
'''

# -*- coding: utf-8 -*-
"""Main Controller"""
import logging
import simplejson as json

from routes import url_for
from tg import expose, flash, require, url, lurl, request, redirect, config
from tg.i18n import ugettext as _, lazy_ugettext as l_
from jminee import model
from repoze.what import predicates
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
from mako.template import Template

from jminee.controllers.secure import SecureController
from jminee.controllers.registration import RegistrationController
from jminee.controllers.topic import TopicController
from jminee.model import DBSession, metadata

from jminee.lib import send_email2
from jminee.lib.base import BaseController
from jminee.controllers.error import ErrorController
from jminee.lib.errorcode import ErrorCode, ExceptionProcessing

__all__ = ['NotificationController']

log = logging.getLogger(__name__)

class UserNotification(object):
    def __init__(self, **not_str): 
        self.__dict__.update(not_str)      
    
              
class NotificationController(BaseController):
    
    @expose()
    def user_notification(self):
        try:
            body = json.loads(request.body)
            notif = UserNotification(**json.loads(body['Message']))
            if notif.type=='new-topic':
                self.send_newtopic_notif(notif)
            elif notif.type=='new-subject':
                self.send_newsubject_notif(notif)                
            elif notif.type=='new-comment':
                self.send_newcomment_notif(notif)
            elif notif.type=='invitation':    
                self.send_newtopic_notif(notif)
                
        except Exception as e:
            ExceptionProcessing.gotException(self, e, log)
    
    @expose('jminee.templates.error')
    def error(self, *args, **kw):        
        return dict(kw)
    
    def send_newtopic_notif(self, notif):
        sender = config['registration.email_sender']
        if notif['type'] in ('new topic','add_member'):
            subject='{user_name} invited you to join topic "{topic}" on Jminee'.format(**notif)
        elif notif['type']=='new_subject':
            subject='{user_name} created subject "{subject}" on topic "{topic}" on Jminee'.format(**notif)
        elif notif['type']=='new_comment':
            subject='{user_name} commented on subject "{subject}" of topic "{topic}" on Jminee'.format(**notif)
                
        richmail = Template(filename='jminee/templates/emailnotification.mak')
        plainmail = '{user_name} invited you to join topic "{topic}" on Jminee (http://www.jminee.com)'\
                        .format(**notif)  
        
#        print richmail.render(**notif)
        for receiver in notif['registered_users']:
            send_email2(receiver, sender, subject, plainmail, richmail.render(**notif))

    
    def got_url(self):
        return "http://www.jminee.com:8080/"