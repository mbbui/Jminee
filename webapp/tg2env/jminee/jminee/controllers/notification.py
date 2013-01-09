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

              
class NotificationController(BaseController):
    
    @expose()
    def user_notification(self):
        try:
            log.info("Notification: %s"%str(request.body))
            body = json.loads(request.body)
            if body['Type'] == 'Notification':
                notif = json.loads(body['Message'])
                if notif['type'] in ('new-topic', 'new-subject', 'new-comment', 'add_member'):    
                    self.send_topic_notif(notif)
                
        except Exception as e:
            ExceptionProcessing.gotException(e, log)
       
    def send_topic_notif(self, notif):
        sender = config['registration.email_sender']
        if notif['type'] in ('new_topic','add_member'):
            subject='{user_name} invited you to join topic "{topic}" on Jminee'.format(**notif)
        elif notif['type']=='new_subject':
            subject='{user_name} created subject "{subject}" in topic "{topic}" on Jminee'.format(**notif)
        elif notif['type']=='new_comment':
            subject='{user_name} commented in "{topic} > {subject}" on Jminee'.format(**notif)
                
        richmail = Template(filename='jminee/templates/topicnotification.mak')
        plainmail = '{user_name} invited you to join topic "{topic}" on Jminee (http://www.jminee.com)'\
                        .format(**notif)  
        
#        print richmail.render(**notif)
        for receiver in notif['registered_users']:
            send_email2(receiver, sender, subject, plainmail, richmail.render(**notif))

    
    def got_url(self):
        return "http://www.jminee.com:8080/"