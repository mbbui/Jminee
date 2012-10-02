# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1349060999.384273
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
        __M_writer(u'<!DOCTYPE html>\n<html lang="en">\n\n    <head>\n        <title>Jminee - Notifications Simplified</title>\n\n        <meta charset="utf-8">\n        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n\n        <link type="text/css" rel="stylesheet" href="/bootstrap/css/bootstrap-responsive.min.css">\n        <link type="text/css" rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">\n\n        <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>\n        <script type="text/javascript" src="/javascript/ember-0.9.8.1.min.js"></script>\n        <script type="text/javascript" src="/bootstrap/js/bootstrap.min.js"></script>\n        \n\n        <link type="text/css" rel="stylesheet" href="/css/styles.css">\n        <script src="/javascript/creation.js" type="text/javascript"></script>\n        <script src="/javascript/login.js" type="text/javascript"></script>\n<!--        <script>-->\n<!--\t\t\t$(function() {-->\n<!--\t\t\t\t$( "#accordion" ).accordion();-->\n<!--\t\t});-->\n<!--\t\t</script>-->\n    </head>\n\n    <body>\n        <!-- navbar -->\n        <div class="navbar navbar-fixed-top navbar-inverse">\n            <div class="navbar-inner">\n                <div class="container">\n                    <a class="brand pull-left" href="#">\n                        Jminee\n                    </a>\n                    <form class="navbar-search pull-right">\n\t\t\t\t\t\t<input type="text" class="input-medium search-query" placeholder="Search...">\n\t\t\t\t\t</form>\n                </div>\n            </div>\n        </div>\n        <!-- /navbar -->\n\n        <!-- topic page -->\n        <div class="container">\n        \t<section>\n        \t \t<div class="row ">\n        \t\t\t<div class="span12">        \t\t\t\t\n       \t\t\t\t\t<ul class="breadcrumb">\n      \t\t\t\t\t\t<li><a href="#">Main</a> <span class="divider">></span></li>\n  \t\t\t\t\t\t\t<li class="active"><a href="#">Soccer Tournament</a> </li>\n\t\t\t\t\t\t</ul>\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\t\n        \t\t</div>\n        \t\t\n                <div class="row">\n                    <div class="span3">\n                        <div class="accordion" id="accordion2">\n\t\t\t\t\t\t  <div class="accordion-group">\n\t\t\t\t\t\t    <div class="accordion-heading">\n\t\t\t\t\t\t      <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseOne">\n\t\t\t\t\t\t       <i class="icon-comment"></i>\n\t\t\t\t\t\t      </a>\n\t\t\t\t\t\t    </div>\n\t\t\t\t\t\t    <div id="collapseOne" class="accordion-body collapse in">\n\t\t\t\t\t\t      <div class="accordion-inner">\n\t\t\t\t\t\t\t      <ul class="nav nav-pills nav-stacked">\n\t\t\t\t\t\t\t        <li class="active"> <a href="#">Practice</a> </li>\n\t\t\t\t\t\t\t        <li> <a href="#">Goalkeeper gloves</a> </li>\n\t\t\t\t\t\t\t      </ul>\n\t\t\t\t\t\t      </div>\n\t\t\t\t\t\t    </div>\n\t\t\t\t\t\t  </div>\n\t\t\t\t\t\t  <div class="accordion-group">\n\t\t\t\t\t\t    <div class="accordion-heading">\n\t\t\t\t\t\t      <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion2" href="#collapseTwo">\n\t\t\t\t\t\t        <i class="icon-list-alt"></i>\t\t\t\t\t\t        \n\t\t\t\t\t\t      </a>\n\t\t\t\t\t\t    </div>\n\t\t\t\t\t\t    <div id="collapseTwo" class="accordion-body collapse">\n\t\t\t\t\t\t      <div class="accordion-inner">\n\t\t\t\t\t\t      \t<ul class="nav nav-pills nav-stacked">\n\t\t\t\t\t\t\t      \t<li> <a href="#">Registration</a></li>\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t    \t<li> <a href="#">Expense</a></li>\n\t\t\t\t\t\t    \t</ul>\n\t\t\t\t\t\t      </div>\n\t\t\t\t\t\t    </div>\n\t\t\t\t\t\t  </div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\n                    </div>\n                    <div class="span9">\n                    \t<div class="well  well-small">\n                    \t BRING WATER. there\'s no water fountain as far as we know.\n\nreminder: practice starts 10am\n\nNOT at turf fields\n\nbut at COMPLEX fields\n\nbring balls if you have them\n                    \t</div>\n                    \t<div class="well  well-small">\n                    \t i just talked to campus rec, they said the turf fields are open from 3pm - 5pm\n\t\t\n\nSO we will practice\n\nSTART 3pm (be at the field by 3pm)\n\nat OUTDOOR TURF fields (1st & stadium, champaign)\n                    \t</div>\n                    \t<div class="well  well-small">\n                    \t \t<form class="form-horizontal">\n                    \t \t\t<div class="control-group">\n                    \t \t\t\t<div class="control">\n                    \t \t\t\t\t<textarea class="span8" rows="3" placeholder="Type your message\u2026"></textarea>                    \t \t\t\t\t\n                    \t \t\t\t</div>\n\t\t\t\t\t\t\t  \t</div>\n\t\t\t\t\t\t\t  \t<div class="control-group">\n                    \t \t\t\t<div class="control">\n\t\t\t\t\t\t\t  \t\t\t<button  class="control" type="submit" class="btn">Submit</button>\n\t\t\t\t\t\t\t  \t\t</div>\n\t\t\t\t\t\t\t  \t</div>\n\t\t\t\t\t\t\t</form>\n                    \t</div>                       \n                    </div>\n                </div>\n            </section>\n        </div>\n        <!-- topic page -->\n    </body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


