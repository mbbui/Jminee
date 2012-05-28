# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1338221670.791062
_enable_loop = True
_template_filename = u'/Users/vhiremath4/Desktop/Code/GitHub/Jminee/webapp/tg2env/jminee/jminee/templates/master.mak'
_template_uri = u'/Users/vhiremath4/Desktop/Code/GitHub/Jminee/webapp/tg2env/jminee/jminee/templates/master.mak'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['footer', 'sidebar_top', 'title', 'body_class', 'header', 'meta', 'sidebar_bottom', 'main_menu', 'content_wrapper']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n                      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n<head>\n    ')
        # SOURCE LINE 5
        __M_writer(escape(self.meta()))
        __M_writer(u'\n    <title>')
        # SOURCE LINE 6
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        # SOURCE LINE 7
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer(u'" />\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        # SOURCE LINE 8
        __M_writer(escape(tg.url('/css/admin.css')))
        __M_writer(u'" />\n</head>\n<body class="')
        # SOURCE LINE 10
        __M_writer(escape(self.body_class()))
        __M_writer(u'">\n  ')
        # SOURCE LINE 11
        __M_writer(escape(self.header()))
        __M_writer(u'\n  ')
        # SOURCE LINE 12
        __M_writer(escape(self.main_menu()))
        __M_writer(u'\n  ')
        # SOURCE LINE 13
        __M_writer(escape(self.content_wrapper()))
        __M_writer(u'\n  ')
        # SOURCE LINE 14
        __M_writer(escape(self.footer()))
        __M_writer(u'\n</body>\n\n')
        # SOURCE LINE 33
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(u'\n')
        # SOURCE LINE 39
        __M_writer(u'\n\n')
        # SOURCE LINE 41
        __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(u'\n\n')
        # SOURCE LINE 72
        __M_writer(u'\n\n')
        # SOURCE LINE 81
        __M_writer(u'\n')
        # SOURCE LINE 93
        __M_writer(u'\n')
        # SOURCE LINE 116
        __M_writer(u'\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 82
        __M_writer(u'\n  <div class="flogo">\n    <img src="')
        # SOURCE LINE 84
        __M_writer(escape(tg.url('/images/under_the_hood_blue.png')))
        __M_writer(u'" alt="TurboGears" />\n    <p><a href="http://www.turbogears.org/">Powered by TurboGears 2</a></p>\n  </div>\n  <div class="foottext">\n    <p>TurboGears is a open source front-to-back web development\n      framework written in Python. Copyright (c) 2005-2009 </p>\n  </div>\n  <div class="clearingdiv"></div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_top(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 42
        __M_writer(u'\n  <div id="sb_top" class="sidebar">\n      <h2>Get Started with TG2</h2>\n      <ul class="links">\n        <li>\n')
        # SOURCE LINE 47
        if page == 'index':
            # SOURCE LINE 48
            __M_writer(u'              <span><a href="')
            __M_writer(escape(tg.url('/about')))
            __M_writer(u'">About this page</a> A quick guide to this TG2 site </span>\n')
            # SOURCE LINE 49
        else:
            # SOURCE LINE 50
            __M_writer(u'              <span><a href="')
            __M_writer(escape(tg.url('/')))
            __M_writer(u'">Home</a> Back to your Quickstart Home page </span>\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'        </li>\n        <li><a href="http://www.turbogears.org/2.1/docs/">TG2 Documents</a> - Read everything in the Getting Started section</li>\n        <li><a href="http://docs.turbogears.org/1.0">TG1 docs</a> (still useful, although a lot has changed for TG2) </li>\n        <li><a href="http://groups.google.com/group/turbogears"> Join the TG Mail List</a> for general TG use/topics  </li>\n      </ul>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 74
        __M_writer(u'\n  <div id="header">\n  \t<h1>\n  \t\tWelcome to TurboGears 2\n\t\t<span class="subtitle">The Python web metaframework</span>\n\t</h1>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 37
        __M_writer(u'\n  <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_bottom(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 60
        __M_writer(u'\n  <div id="sb_bottom" class="sidebar">\n      <h2>Developing TG2</h2>\n      <ul class="links">\n        <li><a href="http://trac.turbogears.org/query?status=new&amp;status=assigned&amp;status=reopened&amp;group=type&amp;milestone=2.1&amp;order=priority">TG2 Trac tickets</a> What\'s happening now in TG2 development</li>\n        <li><a href="http://trac.turbogears.org/timeline">TG Dev timeline</a> (recent ticket updates, svn checkins, wiki changes)</li>\n        <li><a href="http://svn.turbogears.org/trunk">TG2 SVN repository</a> For checking out a copy</li>\n        <li><a href="http://turbogears.org/2.1/docs/main/Contributing.html#installing-the-development-version-of-turbogears-2-from-source">Follow these instructions</a> For installing your copy</li>\n        <li><a href="http://trac.turbogears.org/browser/trunk">TG2 Trac\'s svn view</a> In case you need a quick look</li>\n        <li><a href="http://groups.google.com/group/turbogears-trunk"> Join the TG-Trunk Mail List</a> for TG2 discuss/dev </li>\n      </ul>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        request = context.get('request', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 94
        __M_writer(u'\n  <ul id="mainmenu">\n    <li class="first"><a href="')
        # SOURCE LINE 96
        __M_writer(escape(tg.url('/')))
        __M_writer(u'" class="')
        __M_writer(escape(('', 'active')[page=='index']))
        __M_writer(u'">Welcome</a></li>\n        <li><a href="')
        # SOURCE LINE 97
        __M_writer(escape(tg.url('/about')))
        __M_writer(u'" class="')
        __M_writer(escape(('', 'active')[page=='about']))
        __M_writer(u'">About</a></li>\n        <li><a href="')
        # SOURCE LINE 98
        __M_writer(escape(tg.url('/environ')))
        __M_writer(u'" class="')
        __M_writer(escape(('', 'active')[page=='environ']))
        __M_writer(u'">WSGI Environment</a></li>\n        <li><a href="')
        # SOURCE LINE 99
        __M_writer(escape(tg.url('/data')))
        __M_writer(u'" class="')
        __M_writer(escape(('', 'active')[page=='data']))
        __M_writer(u'">Content-Types</a></li>\n\n')
        # SOURCE LINE 101
        if tg.auth_stack_enabled:
            # SOURCE LINE 102
            __M_writer(u'        <li><a href="')
            __M_writer(escape(tg.url('/auth')))
            __M_writer(u'" class="')
            __M_writer(escape(('', 'active')[page=='auth']))
            __M_writer(u'">Authentication</a></li>\n')
            pass
        # SOURCE LINE 104
        __M_writer(u'        <li><a href="http://groups.google.com/group/turbogears">Contact</a></li>\n')
        # SOURCE LINE 105
        if tg.auth_stack_enabled:
            # SOURCE LINE 106
            __M_writer(u'      <span>\n')
            # SOURCE LINE 107
            if not request.identity:
                # SOURCE LINE 108
                __M_writer(u'            <li id="login" class="loginlogout"><a href="')
                __M_writer(escape(tg.url('/login')))
                __M_writer(u'">Login</a></li>\n')
                # SOURCE LINE 109
            else:
                # SOURCE LINE 110
                __M_writer(u'            <li id="login" class="loginlogout"><a href="')
                __M_writer(escape(tg.url('/logout_handler')))
                __M_writer(u'">Logout</a></li>\n            <li id="admin" class="loginlogout"><a href="')
                # SOURCE LINE 111
                __M_writer(escape(tg.url('/admin')))
                __M_writer(u'">Admin</a></li>\n')
                pass
            # SOURCE LINE 113
            __M_writer(u'      </span>\n')
            pass
        # SOURCE LINE 115
        __M_writer(u'  </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n    <div id="content">\n    <div>\n')
        # SOURCE LINE 20
        if page:
            # SOURCE LINE 21
            __M_writer(u'      <div class="currentpage">\n       Now Viewing: <span>')
            # SOURCE LINE 22
            __M_writer(escape(page))
            __M_writer(u'</page>\n      </div>\n')
            pass
        # SOURCE LINE 25
        __M_writer(u'      ')

        flash=tg.flash_obj.render('flash', use_js=False)
        
        
        # SOURCE LINE 27
        __M_writer(u'\n')
        # SOURCE LINE 28
        if flash:
            # SOURCE LINE 29
            __M_writer(u'        ')
            __M_writer(flash )
            __M_writer(u'\n')
            pass
        # SOURCE LINE 31
        __M_writer(u'      ')
        __M_writer(escape(self.body()))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


