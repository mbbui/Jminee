# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2007, Agendaless Consulting and Contributors.
# Copyright (c) 2008, Florent Aide <florent.aide@gmail.com>.
# Copyright (c) 2008-2009, Gustavo Narea <me@gustavonarea.net>.
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
"""Test suite for the repoze.what Quickstart plugin."""

import os

#{ Useful variables


_here = os.path.abspath(os.path.dirname(__file__))
FIXTURE_DIR = os.path.join(_here, "fixture")


#{ Fixture


def tearDown():
    """Remove temporary files."""
    os.remove(os.path.join(FIXTURE_DIR, "file.log"))


#{ Mock objects


class MockApplication(object):
    """Fake WSGI application."""
    
    def __init__(self, status=None, headers=None):
        self.status = status
        self.headers = headers
    
    def __call__(self, environ, start_response):
        self.environ = environ
        start_response(self.status, self.headers)
        return ['response body']

#}
