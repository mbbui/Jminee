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
Miscellaneous utilities for :mod:`repoze.what` when used in a Pylons
application.

"""

from pylons import request

from repoze.what.predicates import Predicate


__all__ = ['is_met', 'not_met', 'booleanize_predicates',
           'debooleanize_predicates']


#{ Evaluators


def is_met(predicate):
    """
    Evaluate the :mod:`repoze.what` ``predicate`` checker and return ``True``
    if it's met.
    
    :param predicate: The :mod:`repoze.what` predicate checker to be evaluated.
    :return: ``True`` if it's met; ``False`` otherwise.
    :rtype: bool
    
    """
    return predicate.is_met(request.environ)


def not_met(predicate):
    """
    Evaluate the :mod:`repoze.what` ``predicate`` checker and return ``False``
    if it's met.
    
    :param predicate: The :mod:`repoze.what` predicate checker to be evaluated.
    :return: ``False`` if it's met; ``True`` otherwise.
    :rtype: bool
    
    """
    return not predicate.is_met(request.environ)


#{ Booleanizers


def booleanize_predicates():
    """
    Make :mod:`repoze.what` predicates evaluable without passing the 
    ``environ`` explicitly.
    
    .. warning::
    
        The use of this function is **strongly discouraged**. Use
        :func:`is_met` or :func:`not_met` instead.
    
    """
    Predicate.__nonzero__ = lambda self: self.is_met(request.environ)


def debooleanize_predicates():
    """
    Stop :mod:`repoze.what` predicates from being evaluable without passing the 
    ``environ`` explicitly.
    
    This function reverts :func:`booleanize_predicates`.
    
    """
    del Predicate.__nonzero__


#}
