# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009-2010, Gustavo Narea <me@gustavonarea.net>.
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
Parser of configuration files for the repoze.what Quickstart plugin.

"""
from os import path
from ConfigParser import ConfigParser

from pkg_resources import EntryPoint

from repoze.what.plugins.quickstart import setup_sql_auth

__all__ = ("add_auth_from_config", "BadConfigurationException",
           "MissingOptionError", "BadOptionError")


_SUPPORTED_TRANSLATIONS = (
    "validate_password",
    "dummy_validate_password",
    "users",
    "user_name",
    "groups",
    "group_name",
    "permissions",
    "permission_name")


def add_auth_from_config(app, global_conf, config_file):
    """
    Add authentication and authorization middleware.
    
    :param app: The WSGI application to be secured.
    :param global_conf: The PasteDeploy global configuration.
    :type global_conf: dict
    :param config_file: The path to the configuration file for the quickstart
        plugin.
    :type config_file: basestring
    
    ``global_conf`` is not used at present, but could be used in the future.
    
    :raises repoze.what.plugins.quickstart.MissingOptionError: If one of the 
        mandatory options (``dbsession``, ``user_class``, ``group_class``, 
        ``permission_class``) is missing.
    :raises repoze.what.plugins.quickstart.BadOptionError: If an option has an
        invalid value.
    
    """
    auth_config = _AuthConf(config_file)
    auth_config.find_options()
    
    # Validating the configuration:
    if "dbsession" not in auth_config.options:
        raise MissingOptionError("The database session is missing")
    elif "user_class" not in auth_config.options:
        raise MissingOptionError("The SQLAlchemy-based user class is missing")
    elif "group_class" not in auth_config.options:
        raise MissingOptionError("The SQLAlchemy-based group class is missing")
    elif "permission_class" not in auth_config.options:
        raise MissingOptionError("The SQLAlchemy-based permission class is "
                                 "missing")
    
    app_with_auth = setup_sql_auth(app, **auth_config.options)
    return app_with_auth


#{ Exceptions


class BadConfigurationException(Exception):
    """
    Base exception for errors in a repoze.what-quickstart configuration file.
    
    """
    pass


class MissingOptionError(BadConfigurationException):
    """
    Exception raised when a mandatory option in the configuration file is
    missing.
    
    """
    pass


class BadOptionError(BadConfigurationException):
    """
    Exception raised when an option has an invalid value.
    
    """
    pass


#{ Internal utilities


class _AuthConf(object):
    """
    Parser of repoze.what-quickstart configuration files.
    
    """
    def __init__(self, path_to_conf):
        """
        
        :param path_to_conf: The path to the repoze.what-quickstart
            configuration file.
        
        """
        root_dir = path.dirname(path_to_conf)
        self.parser = ConfigParser(defaults={'here': root_dir})
        self.parser.read(path_to_conf)
        self.options = {'translations': {}}
    
    def find_options(self):
        """
        Parse the configuration file and extract the auth options.
        
        :raises BadOptionError: If an option has an invalid value.
        
        """
        # Adding general options:
        self._add_object("general", "dbsession")
        self._add_string("general", "charset")
        
        # Adding authentication options:
        self._add_object("authentication", "user_class")
        self._add_object("authentication", "form_plugin")
        self._add_boolean("authentication", "form_identifies")
        self._add_string("authentication", "cookie_name")
        self._add_string("authentication", "cookie_secret")
        self._add_integer("authentication", "cookie_timeout")
        self._add_integer("authentication", "cookie_reissue_time")
        self._add_string("authentication", "login_url")
        self._add_string("authentication", "login_handler")
        self._add_string("authentication", "post_login_url")
        self._add_string("authentication", "logout_handler")
        self._add_string("authentication", "post_logout_url")
        self._add_string("authentication", "login_counter_name")
        self._add_string("authentication", "log_level")
        self._add_string("authentication", "log_file")
        self._add_boolean("authentication", "skip_authentication")

        # Adding authorization options:
        self._add_object("authorization", "group_class")
        self._add_object("authorization", "permission_class")
        
        # Adding translations:
        for translation in _SUPPORTED_TRANSLATIONS:
            if self.parser.has_option("translations", translation):
                value = self.parser.get("translations", translation)
                self.options['translations'][translation] = value
    
    def _add_string(self, section, option):
        """
        Add the ``option`` if it's defined.
        
        """
        if self.parser.has_option(section, option):
            value = self.parser.get(section, option)
            self.options[option] = value
    
    def _add_boolean(self, section, option):
        """
        Add the ``option`` as a boolean if it's defined.
        
        """
        if self.parser.has_option(section, option):
            try:
                value = self.parser.getboolean(section, option)
            except ValueError:
                value = self.parser.get(section, option)
                raise BadOptionError('Option %s ("%s") is not a boolean' %
                                     (option, value))
            else:
                self.options[option] = value
    
    def _add_integer(self, section, option):
        """
        Add the ``option`` as a integer if it's defined.
        
        """
        if self.parser.has_option(section, option):
            try:
                value = self.parser.getint(section, option)
            except ValueError:
                value = self.parser.get(section, option)
                raise BadOptionError('Option %s ("%s") is not an integer' %
                                     (option, value))
            else:
                self.options[option] = value
    
    def _add_object(self, section, option):
        """
        Resolve object ``option`` if it's defined and load it to the options.
        
        :raises BadOptionError: If the value of ``option`` cannot be resolved.
        
        """
        if self.parser.has_option(section, option):
            value = self.parser.get(section, option)
            try:
                object_ = EntryPoint.parse("x=%s" % value).load(False)
            except (ValueError, ImportError):
                raise BadOptionError('Option %s ("%s") cannot be resolved' %
                                     (option, value))
            else:
                self.options[option] = object_


#}
