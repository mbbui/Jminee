# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1354988209.872805
_enable_loop = True
_template_filename = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/index.mak'
_template_uri = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/index.mak'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<html lang="en">\n\n    <head>\n        <title>Jminee - Notifications Simplified</title>\n\n        <meta charset="utf-8">\n        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\t\n\t\t<link type="text/css" rel="stylesheet" href="/css/styles.css">\n        <link type="text/css" rel="stylesheet" href="/bootstrap/css/bootstrap-responsive.min.css">\n        <link type="text/css" rel="stylesheet" href="/bootstrap/css/bootstrap.css">\n        \n\n        <script type="text/javascript" src="/javascript/jquery-1.7.2.js"></script>\n        <script type="text/javascript" src="/javascript/handlebars-1.0.rc.1.js"></script>\n        <script type="text/javascript" src="/javascript/ember-1.0.pre.js"></script>\n        \n     \n        \n        <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script>\n        \n\n        <link type="text/css" rel="stylesheet" href="/css/styles.css">\n        <script src="/javascript/creation.js" type="text/javascript"></script>\n        <script src="/javascript/login.js" type="text/javascript"></script>\n        <script src="/javascript/controllers.js" type="text/javascript"></script>\n        <script src="/javascript/textareacontrollers.js" type="text/javascript"></script>\n        <script src="/javascript/messageviews.js" type="text/javascript"></script>\n        <script src="/javascript/topicviews.js" type="text/javascript"></script>\n        <script src="/javascript/topicnavviews.js" type="text/javascript"></script>\n        <script src="/javascript/subjectnavviews.js" type="text/javascript"></script>\n        <script src="/javascript/subjectviews.js" type="text/javascript"></script>\n        <script src="/javascript/composeviews.js" type="text/javascript"></script>\n        <script src="/javascript/views.js" type="text/javascript"></script>        \n                \n    </head>\n\n    <body>\n        <!-- navbar -->\n        <div class="navbar navbar-fixed-top navbar-inverse">\n            <div class="navbar-inner">\n                <div class="container">\n                    <a class="brand pull-left" href="#">\n                        Jminee\n                    </a>\n                </div>\n            </div>\n        </div>\n        <!-- /navbar -->\n        <div class="container" id="main_container">\n        </div>\n    </body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


