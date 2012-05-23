# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1333601587.232914
_enable_loop = True
_template_filename = '/home/marvin/src/tg2/tests/test_stack/rendering/templates/mako_noop.mak'
_template_uri = 'mako_noop.mak'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<p>This is the mako index page</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


