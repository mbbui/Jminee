# -*- coding: utf-8 -*-
"""Main Controller"""
import logging
from tg import expose, flash, require, url, lurl, request, redirect
from tg.i18n import ugettext as _, lazy_ugettext as l_
from jminee import model
from repoze.what import predicates
from jminee.controllers.secure import SecureController
from jminee.controllers.registration import RegistrationController
from jminee.controllers.message import MessageController
from jminee.model import DBSession, metadata
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController

from jminee.lib.base import BaseController
from jminee.controllers.error import ErrorController
from jminee.lib.errorcode import ErrorCode

__all__ = ['RootController']

log = logging.getLogger(__name__)

class RootController(BaseController):
    """
    The root controller for the jminee application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    registration = RegistrationController()
    message = MessageController()
    error = ErrorController()    
    
    #@expose('json')
    @expose('jminee.templates.index')
    def index(self):
        """Handle the front-page."""
        log.info("Root index")
        return dict(page='index')
    
    @expose('json')
    def login(self,came_from):
        ''' This function implementation is a quick hack:
            when user has not logined but try to access
            page that requires login, repoze.who will
            call this function
        '''
        return dict(success=False, error_code=ErrorCode.UNAUTHENTICATED)
        
    @expose('jminee.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('jminee.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(environment=request.environ)

    @expose('jminee.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params=kw)
    @expose('jminee.templates.authentication')
    def auth(self):
        """Display some information about auth* on this application."""
        return dict(page='auth')

    @expose('jminee.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('jminee.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('json')
    def post_login(self, came_from=lurl('/')):
        login_counter = request.environ['repoze.who.logins']
                
        if not request.identity:
            login_counter = request.environ['repoze.who.logins'] + 1
            if login_counter > 0:
                return dict(success=False, 
                            error_code=ErrorCode.WRONGUSERPASSWORD, 
                            __logins=login_counter)            
        
        return dict(success=True)
   
    @expose('json')
    def post_logout(self, came_from=lurl('/')):
        return dict(success=True)

    @expose('json')
    def testlogin(self):
        if not request.identity:
            return dict(success=False)
        return dict(success=True, user_name=request.identity['repoze.who.userid'])