import os
from urllib import quote, unquote
from logging import getLogger

try:
    import json
except ImportError:
    # Python < 2.6
    import simplejson as json

__all__ = ["Flash"]

IS_DEBUG = 'WEBFLASH_DEBUG' in os.environ
log = getLogger(__name__)

class Flash(object):
    """
    A flash message creator.

    *Parameters (all optional):*

        `cookie_name`
            The name of the cookie that will be used as transport

        `default_status`
            The CSS class that will be added to the flash container when it
            is not passed explicitly when calling the Flash instance.

        `get_response`
            A callable that will provide the response object of the framework
            if no explicit response is passed when calling the Flash instance.

        `js_path`
            Shall you want to override the JS code that will display the flash
            message then pass the path to where the file lives. Note that this
            is a path within the file-system, not a URL

        `debug`
            Should the JS code be provided in an uncompressed form (provided that
            js_path has not been overriden) and reloaded every time a page is
            rendered?


    Flash needs a Reponse object with a `set_cookie` method, like WebOb's
    :class:`webob.Response`. We'll mock one for demonstration purposes::

        >>> class MyResponse(object):
        ...     def set_cookie(self, name, value):
        ...         pass

    The :class:`Flash` object could be instantiated once for the lifetime
    of an application and be kept at module scope (or a request-local object
    if the framework provides one). A :meth:`get_response` callable is useful
    in this case if the framework provides a global response to avoid passing
    the response object around on every call to the :class:`Flash` instance::
    
        >>> flash = Flash(get_response=lambda: MyResponse())


    Displaying the flash message is done by calling the Flash instance from
    your controller/view code::

        >>> flash("All your data has been erased and your identity destroyed")
        >>> flash("Stuff broke", status="error")

    To insert the JavaScript code needed for Flash to work you need to insert
    the result of the :meth:`render` method on every page you might want to
    display flash messages (normally all of them, so you might want to include
    the call in a base template)::

        >>> _ = flash.render("flash-container")
    """
    template = '<div id="%(container_id)s">'\
               '<script type="text/javascript">'\
               '//<![CDATA[\n'\
               '%(js_code)s'\
               '%(js_call)s'\
               '\n//]]>'\
               '</script>'\
               '</div>'
    static_template = '<div id="%(container_id)s">'\
                      '<div class="%(status)s">%(message)s</div>'\
                      '</div>'
    _js_code = None
    def __init__(self, cookie_name="webflash", default_status="ok",
                 get_response=None, get_request=None, js_path=None,
                 debug=IS_DEBUG):
        self.default_status = default_status
        self.get_response = get_response or (lambda: None)
        self.get_request = get_request or (lambda: None)
        self.cookie_name = cookie_name
        self.js_path = js_path or _get_js_path(debug)
        if not debug:
            # Preload js_code so we don't need to read the file on every request
            self.js_code = open(self.js_path).read()

    def _get_js_code(self):
        return self._js_code or open(self.js_path).read()
    def _set_js_code(self, value):
        self._js_code = value
    js_code = property(_get_js_code, _set_js_code)

        
    def __call__(self, message, status=None, response=None, request=None,
                 **extra_payload):
        response = response or self.get_response()
        if response is None:
            raise ValueError(
                "Must provide a response object or configure a callable that "
                "provides one"
                )
        payload = self.prepare_payload(
            message = message,
            status = status or self.default_status,
            **extra_payload
            )
        request = request or self.get_request()
        if request is not None:
            # Save the payload in environ too in case JavaScript is not being
            # used and the message is being displayed in the same request.
            request.environ['webflash.payload'] = payload
            log.debug("Setting payload in environ %d", id(request.environ))
        log.debug("Setting payload in cookie")
        response.set_cookie(self.cookie_name, payload)

    def prepare_payload(self, **data):
        return quote(json.dumps(data))

    def js_call(self, container_id):
        return 'webflash(%(options)s).render();' % {
            'options': json.dumps({
                'id': container_id,
                'name': self.cookie_name
                })
            }

    def render(self, container_id, use_js=True, request=None, response=None):
        if use_js:
            return self._render_js_version(container_id)
        else:
            return self._render_static_version(container_id, request, response)

    def _render_static_version(self, container_id, request, response):
        payload = self.pop_payload(request, response)
        if not payload:
            return ''
        payload['message'] = html_escape(payload.get('message',''))
        payload['container_id'] = container_id
        return self.static_template % payload

    def _render_js_version(self, container_id):
        return self.template % {
            'container_id': container_id,
            'js_code': self.js_code,
            'js_call': self.js_call(container_id)
            }

    def pop_payload(self, request=None, response=None):
        """
        Fetches and decodes the flash payload from the request and sets the
        required Set-Cookie header in the response so the browser deletes the
        flash cookie.

        This method is intended to manage the flash payload without using
        JavaScript and requires webob compatible request/response
        objects.
        """
        # First try fetching it from the request
        request = request or self.get_request()
        response = response or self.get_response()
        if request is None or response is None:
            raise ValueError("Need to provide a request and reponse objects")
        payload = request.environ.get('webflash.payload', {})
        if not payload:
            payload = request.str_cookies.get(self.cookie_name, {})
            if payload:
                log.debug("Got payload from cookie")
        else:
            log.debug("Got payload for environ %d, %r",
                      id(request.environ), payload)
        if payload:
            payload = json.loads(unquote(payload))
            if 'webflash.deleted_cookie' not in request.environ:
                log.debug("Deleting flash payload")
                response.delete_cookie(self.cookie_name)
                request.environ['webflash.delete_cookie'] = True
        return payload or {}


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&#39;",
    ">": "&gt;",
    "<": "&lt;",
    }

# From http://wiki.python.org/moin/EscapingHtml
def html_escape(text):
    """Produce entities within text."""
    L=[]
    for c in text:
        L.append(html_escape_table.get(c,c))
    return "".join(L)


def _get_js_path(debug):
    filename = debug and 'webflash.js' or 'webflash.min.js'
    try:
        import pkg_resources
        return pkg_resources.resource_filename('webflash', filename)
    except ImportError:
        # Be compatible with pkg_resources haters
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), filename)
            )
