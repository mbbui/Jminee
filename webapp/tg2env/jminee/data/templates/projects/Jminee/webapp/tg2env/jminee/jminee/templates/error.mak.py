# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1339116573.354508
_enable_loop = True
_template_filename = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/error.mak'
_template_uri = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/error.mak'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        message = context.get('message', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n                      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n<head>\n  <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>\n  <title>An Error has Occurred </title>\n</head>\n\n<body>\n\t')
        # SOURCE LINE 10

        import re
        mf = re.compile(r'(</?)script', re.IGNORECASE)
        def fixmessage(message):
            return mf.sub(r'\1noscript', message)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['re','mf','fixmessage'] if __M_key in __M_locals_builtin_stored]))
        # SOURCE LINE 15
        __M_writer(u'\n\t\n\t<div>')
        # SOURCE LINE 17
        __M_writer(fixmessage(message) )
        __M_writer(u'</div>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


