# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1337988133.060216
_enable_loop = True
_template_filename = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/authentication.mak'
_template_uri = '/projects/Jminee/webapp/tg2env/jminee/jminee/templates/authentication.mak'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['title']


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
        tg = context.get('tg', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(escape(parent.sidebar_top()))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(escape(parent.sidebar_bottom()))
        __M_writer(u'\n  <div id="getting_started">\n    <h2>Authentication &amp; Authorization in a TG2 site.</h2>\n    <p>If you have access to this page, this means you have enabled authentication and authorization\n    in the quickstart to create your project.</p>\n    <p>\n    The paster command will have created a few specific controllers for you. But before you\n    go to play with those controllers you\'ll need to make sure your application has been\n    properly bootstapped.\n    This is dead easy, here is how to do this:\n    </p>\n\n    <span class="code">\n    paster setup-app development.ini\n    </span>\n\n    <p>\n    inside your application\'s folder and you\'ll get a database setup (using the preferences you have\n    set in your development.ini file). This database will also have been prepopulated with some\n    default logins/passwords so that you can test the secured controllers and methods.\n    </p>\n    <p>\n    To change the comportement of this setup-app command you just need to edit the <span class="code">websetup.py</span> file.\n    </p>\n    <p>\n    Now try to visiting the <a href="')
        # SOURCE LINE 30
        __M_writer(escape(tg.url('/manage_permission_only')))
        __M_writer(u'">manage_permission_only</a> URL. You will be challenged with a login/password form.\n    </p>\n    <p>\n    Only managers are authorized to visit this method. You will need to log-in using:\n        <p>\n        <span class="code">\n        login: manager\n        </span>\n        </p>\n        <p>\n        <span class="code">\n        password: managepass\n        </span>\n        </p>\n    </p>\n    <p>\n    Another protected resource is <a href="')
        # SOURCE LINE 46
        __M_writer(escape(tg.url('/editor_user_only')))
        __M_writer(u'">editor_user_only</a>. This one is protected by a different set of permissions.\n    You will need to be <span class="code">editor</span> with a password of <span class="code">editpass</span> to be able to access it.\n    </p>\n    <p>\n    The last kind of protected resource in this quickstarted app is a full so called <a href="')
        # SOURCE LINE 50
        __M_writer(escape(tg.url('/secc')))
        __M_writer(u'">secure controller</a>. This controller is protected globally.\n    Instead of having a @require decorator on each method, we have set an allow_only attribute at the class level. All the methods in this controller will\n    require the same level of access. You need to be manager to access <a href="')
        # SOURCE LINE 52
        __M_writer(escape(tg.url('/secc')))
        __M_writer(u'">secc</a> or <a href="')
        __M_writer(escape(tg.url('/secc/some_where')))
        __M_writer(u'">secc/some_where</a>.\n    </p>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'Learning TurboGears 2.1: Quick guide to authentication.')
        return ''
    finally:
        context.caller_stack._pop_frame()


