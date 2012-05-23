# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009, Gustavo Narea <me@gustavonarea.net>.
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
Utilities to use :mod:`repoze.what` v1 in a Pylons or TurboGears 2 application.

"""

# Let's make all the utilities available in this namespace:

from repoze.what.plugins.pylonshq.utils import booleanize_predicates, \
                                               debooleanize_predicates, \
                                               is_met, not_met

from repoze.what.plugins.pylonshq.protectors import ActionProtector, \
                                                    ControllerProtector


__all__ = ['ActionProtector', 'ControllerProtector', 'booleanize_predicates',
           'debooleanize_predicates', 'is_met', 'not_met']
