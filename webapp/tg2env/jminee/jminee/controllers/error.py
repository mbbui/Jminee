# -*- coding: utf-8 -*-
"""Error controller"""

from tg import request, expose
from jminee.lib.errorcode import ErrorCode

import pylons

__all__ = ['ErrorController']


class ErrorController(object):
    """
    Generates error documents as and when they are required.

    The ErrorDocuments middleware forwards to ErrorController when error
    related status codes are returned from the application.

    This behaviour can be altered by changing the parameters to the
    ErrorDocuments middleware in your config/middleware.py file.
    
    """

    @expose('jminee.templates.error')
    def document(self, *args, **kwargs):
        """Render the error document"""
        resp = request.environ.get('pylons.original_response')
        default_message = ("<p>We're sorry but we weren't able to process "
                           " this request.</p>")
        values = dict(prefix=request.environ.get('SCRIPT_NAME', ''),
                      code=request.params.get('code', resp.status_int),
                      message=request.params.get('message', default_message))
        return values
    
    @classmethod
    @expose('json')
    def error(cls, *args, **kw):
        error_list=pylons.tmpl_context.form_errors
        return dict(success=False, errors=error_list)
    
    @classmethod
    @expose('json')
    def failed_input_validation(cls, *args, **kw):
        error_list=pylons.tmpl_context.form_errors
        return dict(success=False, error_code=ErrorCode.INVALIDATEDINPUT, errors=error_list)
    
    @classmethod
    @expose('json')
    def failed_activation(cls, *args, **kw):
        return dict(success=False, error_code=ErrorCode.FAILEDACTIVATION)