# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008-2010, Gustavo Narea <me@gustavonarea.net>.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################

"""
Tests for the repoze.what SQL quickstart.

"""

from os import path
import sys
from unittest import TestCase

from repoze.who.interfaces import IAuthenticator
from repoze.who.plugins.basicauth import BasicAuthPlugin
from repoze.who.plugins.auth_tkt import AuthTktCookiePlugin
from repoze.who.plugins.sa import SQLAlchemyAuthenticatorPlugin, \
                                  SQLAlchemyUserMDPlugin
from repoze.who.plugins.friendlyform import FriendlyFormPlugin
from repoze.what.middleware import AuthorizationMetadata
from repoze.what.plugins.quickstart import setup_sql_auth, \
                                           find_plugin_translations
from repoze.who.utils import resolveDotted
from zope.interface import implements

from tests import databasesetup
from tests.fixture.model import User, Group, Permission, DBSession
from tests import MockApplication, FIXTURE_DIR


class TestSetupAuth(TestCase):
    """Tests for the setup_sql_auth() function"""
    
    def setUp(self):
        super(TestSetupAuth, self).setUp()
        databasesetup.setup_database()
    
    def tearDown(self):
        super(TestSetupAuth, self).tearDown()
        databasesetup.teardownDatabase()
    
    def _in_registry(self, app, registry_key, registry_type):
        assert registry_key in app.name_registry, ('Key "%s" not in registry' %
                                                   registry_key)
        assert isinstance(app.name_registry[registry_key], registry_type), \
               'Registry key "%s" is of type "%s" (not "%s")' % \
               (registry_key, app.name_registry[registry_key].__class__.__name__,
                registry_type.__name__)
    
    def _makeApp(self, **who_args):
        app_with_auth = setup_sql_auth(MockApplication(), User, Group, Permission,
                                       DBSession, **who_args)
        return app_with_auth

    def test_no_extras(self):
        app = self._makeApp()
        self._in_registry(app, 'main_identifier', FriendlyFormPlugin)
        self._in_registry(app, 'authorization_md', AuthorizationMetadata)
        self._in_registry(app, 'sql_user_md', SQLAlchemyUserMDPlugin)
        self._in_registry(app, 'cookie', AuthTktCookiePlugin)
        self._in_registry(app, 'sqlauth', SQLAlchemyAuthenticatorPlugin)
        self._in_registry(app, 'form', FriendlyFormPlugin)
    
    def test_form_doesnt_identify(self):
        app = self._makeApp(form_identifies=False)
        assert 'main_identifier' not in app.name_registry
    
    def test_additional_identifiers(self):
        identifiers = [('http_auth', BasicAuthPlugin('1+1=2'))]
        app = self._makeApp(identifiers=identifiers)
        self._in_registry(app, 'main_identifier', FriendlyFormPlugin)
        self._in_registry(app, 'http_auth', BasicAuthPlugin)
    
    def test_non_default_form_plugin(self):
        app = self._makeApp(form_plugin=BasicAuthPlugin('1+1=2'))
        self._in_registry(app, 'main_identifier', BasicAuthPlugin)
    
    def test_additional_authenticators(self):
        authenticators = [("mock_auth", MockAuthenticator())]
        app = self._makeApp(authenticators=authenticators)
        self._in_registry(app, 'mock_auth', MockAuthenticator)
        self._in_registry(app, 'sqlauth', SQLAlchemyAuthenticatorPlugin)
    
    def test_no_default_authenticator(self):
        authenticators = [("mock_auth", MockAuthenticator())]
        app = self._makeApp(authenticators=authenticators,
                            use_default_authenticator=False)
        self._in_registry(app, 'mock_auth', MockAuthenticator)
        assert "sqlauth" not in app.name_registry
    
    def test_custom_login_urls(self):
        login_url = '/myapp/login'
        login_handler = '/myapp/login_handler'
        post_login_url = '/myapp/welcome_back'
        logout_handler = '/myapp/logout'
        post_logout_url = '/myapp/see_you_later'
        login_counter_name = '__failed_logins'
        app = self._makeApp(login_url=login_url, login_handler=login_handler,
                            logout_handler=logout_handler,
                            post_login_url=post_login_url,
                            post_logout_url=post_logout_url,
                            login_counter_name=login_counter_name)
        form = app.name_registry['form']
        self.assertEqual(form.login_form_url, login_url)
        self.assertEqual(form.login_handler_path, login_handler)
        self.assertEqual(form.post_login_url, post_login_url)
        self.assertEqual(form.logout_handler_path, logout_handler)
        self.assertEqual(form.post_logout_url, post_logout_url)
        self.assertEqual(form.login_counter_name, login_counter_name)

    def test_stdout_logging(self):
        """Test using a stdout for logging"""
        log_level = "debug"
        log_file = "stdout"
        app = self._makeApp(log_level=log_level, log_file=log_file)
        logger = app.logger
        self.assertEqual(logger.level, 10)
        handler = app.logger.handlers[0]
        self.assertEqual(handler.stream, sys.stdout)

    def test_stderr_logging(self):
        """Test using a stderr for logging"""
        log_level = "warning"
        log_file = "stderr"
        app = self._makeApp(log_level=log_level, log_file=log_file)
        logger = app.logger
        self.assertEqual(logger.level, 30)
        handler = app.logger.handlers[0]
        self.assertEqual(handler.stream, sys.stderr)

    def test_file_logging(self):
        """Test using a log file for logging"""
        log_level = "info"
        log_file = path.join(FIXTURE_DIR, "file.log")
        app = self._makeApp(log_level=log_level, log_file=log_file)
        logger = app.logger
        self.assertEqual(logger.level, 20)
        handler = app.logger.handlers[0]
        self.assertEqual(handler.stream.name, log_file)

    def test_no_groups_or_permissions(self):
        """Groups and permissions must be optional"""
        app = setup_sql_auth(MockApplication(), User, None, None, DBSession)
        self._in_registry(app, 'authorization_md', AuthorizationMetadata)
        # Testing that in fact it works:
        environ = {}
        identity = {'repoze.who.userid': u'rms'}
        md = app.name_registry['authorization_md']
        md.add_metadata(environ, identity)
        expected_credentials = {
            'repoze.what.userid': u'rms',
            'groups': tuple(),
            'permissions': tuple()}
        self.assertEqual(expected_credentials, 
                         environ['repoze.what.credentials'])

    def test_timeout(self):
        """AuthTktCookiePlugin's timeout and reissue_time must be supported"""
        app = setup_sql_auth(MockApplication(), User, None, None, DBSession,
                             cookie_timeout=2, cookie_reissue_time=1)
        self._in_registry(app, "cookie", AuthTktCookiePlugin)
        identifier = app.name_registry['cookie']
        # Making sure the arguments were passed:
        self.assertEqual(identifier.timeout, 2)
        self.assertEqual(identifier.reissue_time, 1)

    def test_charset(self):
        """It should be possible to override the default character encoding."""
        charset = "us-ascii"
        app = self._makeApp(charset=charset)
        form = app.name_registry['form']
        self.assertEqual(form.charset, charset)


class TestPluginTranslationsFinder(TestCase):
    
    def test_it(self):
        # --- Setting it up ---
        dummy_fn = 'tests.fixture.model:dummy_validate_password' 
        translations = {
            'validate_password': 'pass_checker',
            'user_name': 'member_name',
            'users': 'members',
            'group_name': 'team_name',
            'groups': 'teams',
            'permission_name': 'perm_name',
            'permissions': 'perms',
            'dummy_validate_password': dummy_fn
            }
        plugin_translations = find_plugin_translations(translations)
        # --- Testing it ---
        # Group translations
        group_translations = {
            'item_name': translations['user_name'],
            'items': translations['users'],
            'section_name': translations['group_name'],
            'sections': translations['groups'],
            }
        self.assertEqual(group_translations, 
                         plugin_translations['group_adapter'])
        # Permission translations
        perm_translations = {
            'item_name': translations['group_name'],
            'items': translations['groups'],
            'section_name': translations['permission_name'],
            'sections': translations['permissions'],
            }
        self.assertEqual(perm_translations, 
                         plugin_translations['permission_adapter'])
        # Authenticator translations
        auth_translations = {
            'user_name': translations['user_name'],
            'validate_password': translations['validate_password'],
            'dummy_validate_password': resolveDotted(dummy_fn)
            }
        self.assertEqual(auth_translations, 
                         plugin_translations['authenticator'])
        # MD Provider translations
        md_translations = {'user_name': translations['user_name']}
        self.assertEqual(md_translations, 
                         plugin_translations['mdprovider'])


#{ Test utilities


class MockAuthenticator(object):
    """A repoze.who authenticator that does nothing."""
    implements(IAuthenticator)
    
    # IAuthenticator
    def authenticate(self, environ, identity):
        pass


#}

