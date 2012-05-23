# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1337744964.82812
_enable_loop = True
_template_filename = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/index.mak'
_template_uri = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/index.mak'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['sidebar_bottom', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(escape(parent.sidebar_top()))
        __M_writer(u'\n\n<div id="getting_started">\n  <h2>Presentation</h2>\n  <p>TurboGears 2 is rapid web application development toolkit designed to make your life easier.</p>\n  <ol id="getting_started_steps">\n    <li class="getting_started">\n      <h3>Code your data model</h3>\n      <p> Design your data model, Create the database, and Add some bootstrap data.</p>\n    </li>\n    <li class="getting_started">\n      <h3>Design your URL architecture</h3>\n      <p> Decide your URLs, Program your controller methods, Design your \n          templates, and place some static files (CSS and/or JavaScript). </p>\n    </li>\n    <li class="getting_started">\n      <h3>Distribute your app</h3>\n      <p> Test your source, Generate project documents, Build a distribution.</p>\n    </li>\n  </ol>\n</div>\n<div class="clearingdiv" />\n<div class="notice"> Thank you for choosing TurboGears. \n</div>\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_bottom(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  Welcome to TurboGears 2.1, standing on the shoulders of giants, since 2007\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


