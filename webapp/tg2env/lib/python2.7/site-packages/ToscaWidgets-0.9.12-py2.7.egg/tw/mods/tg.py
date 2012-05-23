from pkg_resources import require, VersionConflict

import logging

# TurboGears 1.0, 1.1 use CherryPy 2.x while TurboGears 1.5 uses CherryPy 3.x.
# CherryPy 2.x uses Filters while CherryPy 3.x uses Tools. We put the CherryPy
# specific code in separate files which makes it possible for CherryPy users
# who are not using TurboGears to use them directly.
try:
    require("TurboGears>=1.0, <1.5dev")
    import cp2 as cp
    default_view = 'kid'
except VersionConflict:
    require("TurboGears>=1.5dev, <2.0dev")
    import cp3 as cp
    default_view = 'genshi'

import turbogears
from turbogears.i18n.tg_gettext import gettext
from turbogears.view import stdvars

import cherrypy

from tw.core import view
from tw.core.util import install_framework
from tw.mods.base import HostFramework

install_framework()

log = logging.getLogger(__name__)


class TurboGears(HostFramework):

    @property
    def request_local(self):
        try:
            rl = cherrypy.request.tw_request_local
        except AttributeError:
            rl = self.request_local_class(cherrypy.request.wsgi_environ)
            cherrypy.request.tw_request_local = rl
        return rl

    def start_request(self, environ):
        self.request_local.default_view = self._default_view

    def url(self, url):
        """Return the absolute path for the given url."""
        prefix = self.request_local.environ['toscawidgets.prefix']

        return '/' + turbogears.url(prefix + url).lstrip('/')


def start_extension():
    if not cherrypy.config.get('toscawidgets.on', False):
        return

    engines = view.EngineManager()
    engines.load_all(cp._extract_config(), stdvars)

    host_framework = TurboGears(
        engines=engines,
        default_view=cherrypy.config.get('tg.defaultview', default_view),
        translator=gettext)
    prefix = cherrypy.config.get('toscawidgets.prefix', '/toscawidgets')
    host_framework.prefix = prefix
    host_framework.webpath = cherrypy.config.get('server.webpath', '')

    log.info("Loaded TW TurboGears HostFramework")
    filter_args = dict(
        prefix = prefix,
        serve_files = cherrypy.config.get('toscawidgets.serve_files', True))

    cp.start_extension(host_framework, **filter_args)
