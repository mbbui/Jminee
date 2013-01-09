# -*- coding: utf-8 -*-
"""
Functional test suite for the root controller.

This is an example of how functional tests can be written for controllers.

As opposed to a unit-test, which test a small unit of functionality,
functional tests exercise the whole application and its WSGI stack.

Please read http://pythonpaste.org/webtest/ for more information.

"""
from nose.tools import assert_true

from jminee.tests import TestController


class TestRootController(TestController):
    """Tests for the method in the root controller."""

    def test_creatingtopic(self):
        """The front page is working properly"""
        response = self.app.get('/topic/creat_topic?title="Test creating topic"&members=bachbui@gmail.com&members=newuser')
        

  