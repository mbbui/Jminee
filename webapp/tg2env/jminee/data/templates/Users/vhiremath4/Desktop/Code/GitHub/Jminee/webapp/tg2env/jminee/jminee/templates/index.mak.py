# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1338224199.395316
_enable_loop = True
_template_filename = '/Users/vhiremath4/Desktop/Code/GitHub/Jminee/webapp/tg2env/jminee/jminee/templates/index.mak'
_template_uri = '/Users/vhiremath4/Desktop/Code/GitHub/Jminee/webapp/tg2env/jminee/jminee/templates/index.mak'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n\n    <head>\n        <title>Jminee - Notifications Simplified</title>\n        <meta charset="utf-8">\n<script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>\n        <script type="text/javascript" src="javascript/ember-0.9.8.1.min.js"></script>\n        <link type="text/css" rel="stylesheet" href="/css/styles.css">\n    </head>\n\n    <body>\n    </body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


