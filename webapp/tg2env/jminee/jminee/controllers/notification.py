'''
Created on Jan 6, 2013

@author: bachbui
'''

# -*- coding: utf-8 -*-
"""Main Controller"""
import logging
from tg import expose, flash, require, url, lurl, request, redirect
from tg.i18n import ugettext as _, lazy_ugettext as l_
from jminee import model
from repoze.what import predicates
from jminee.controllers.secure import SecureController
from jminee.controllers.registration import RegistrationController
from jminee.controllers.topic import TopicController
from jminee.model import DBSession, metadata
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController

from jminee.lib.base import BaseController
from jminee.controllers.error import ErrorController
from jminee.lib.errorcode import ErrorCode

__all__ = ['RootController']

log = logging.getLogger(__name__)

class NotificationController(BaseController):
    
    @expose()
    def email_notification(self, *args, **kw):
        print args
        print kw
    