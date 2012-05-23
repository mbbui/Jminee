/* webflash.js *
 * Copyright (c) 2009 Alberto Valverde González
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *

 * USAGE:
 * var wf = webflash(options);
 *
 * Available options:
 *     id              -> The id of the DOM node that acts as a container of
 *                        the flash message. This element must exist in the DOM.
 *                        Will default to "webflash" if missing from hash.
 *
 *     name            -> The name of the cookie that carries the payload.
 *                        Will default to "webflash" if missing from hash.
 *
 *     on_display       -> (optional) Callback to execute after the flash message
 *                        has been displayed. It is called with the payload
 *                        and the container DOM node as first and second
 *                        arguments.
 *                        If this option is a string it is expected to be the
 *                        name of a function attached to the window object
 *     create_node      -> (optional) A function that should return the DOM node
 *                        that will be appended to the container.
 *                        If this option is a string it is expected to be the
 *                        name of a function attached to the window object
 *     
 * Available methods:
 *      
 *     wf.render()     -> Renders the flash message stored in the flash cookie.
 *                        This function must be called before the window has
 *                        finisihed loading.
 *                        If the cookie was not set by the server this is a noop.
 *
 *     wf.payload()    -> Returns an object with the payload stored in the cookie
 *                        If no cookie  was set returns null.
 * 
 * Payload structure:
 * 
 *     The payload is expected to be an escaped JSON string which deserializes
 *     into an object with the following keys:
 *
 *     message (string) -> The text to insert into the container. By default this
 *                         text will be apended as a text node so HTML will be
 *                         escaped. Initialize webflash with a custom
 *                         'create_node' function to override this.
 *     status (string)  -> If present this will be the class of the div that
 *                         holds the flash message inside the container.
 *     delay (int)      -> If present, the flash container will be hidden after
 *                         this amount of milliseconds.
 *
 *     Extra arguments may be passed in th payload and interpreted by a custom
 *     create_node or on_display function.
 *   
 */

if (!window.webflash) {
    webflash = (function() {
        var doc = document; // Alias to aid name-mangling
        var allCookies = doc.cookie;
        var cookie_name = null;
        var flash_shown = false;
        var container_id = null;
        var isIE = /msie|MSIE/.test(navigator.userAgent);

        // This function creates the node that will hold the flash message inside
        // the flash container. It can be overrided with the options.create_node
        // option passed to webflash()
        var create_node = function (payload) {
            return doc.createTextNode(payload.message);
        }

        var on_display = function(payload, node) {};

        var lookup_method = function(name_or_func, _default) {
            var ret = _default;
            if (typeof(name_or_func) == "string") {
                ret =  window[name_or_func];
            } else if (name_or_func) {
                ret = name_or_func;
            }
            return ret
        }

        var get_payload = function() {
            var pos = allCookies.indexOf(cookie_name + '=');
            if (pos<0) {
                return null;
            }
            var start = pos + cookie_name.length + 1;
            var end = allCookies.indexOf(';', start);
            if (end == -1) {
                end = allCookies.length;
            }
            var cookie = allCookies.substring(start, end);
            // remove cookie
            doc.cookie = cookie_name + '=; expires=Fri, 02-Jan-1970 00:00:00 GMT; path=/';
            return webflash.lj(unescape(cookie));
        }

        var display_flash = function() {
            if (flash_shown) return;
            flash_shown = true;
            var payload = get_payload();
            if (payload !== null) {
                var container = doc.getElementById(container_id);
                var flash_div = doc.createElement('div');
                if (payload.status) {
                    flash_div.setAttribute(isIE?'className':'class', payload.status);
                }
                var messageNode = create_node(payload);
                flash_div.appendChild(messageNode);
                container.style.display = 'block';
                if (payload.delay) {
                    setTimeout(function() {
                        container.style.display = 'none';
                    }, payload.delay);
                }
                container.appendChild(flash_div);
                on_display(payload, container);
            }
        }

        // Adds a display_flash for when the DOM is ready. It also adds a
        // callback for the window "onload" event since the domready event does
        // not always work.
        // This code is heavily inspired by jquery's ready() function.
        var attachLoadEvent = function() {
            if (!isIE) {
                // DOM 2 Event model
                var domloaded = "DOMContentLoaded";
                doc.addEventListener(domloaded, function() {
                    doc.removeEventListener(domloaded, arguments.callee, false);
                    display_flash();
                }, false);
                // A fallback to window.onload that will always work
                window.addEventListener("load", display_flash, false);
            } else if (isIE) {
                // IE event model
                var domloaded = "onreadystatechange";
                // ensure firing before onload,
                // maybe late but safe also for iframes
                doc.attachEvent(domloaded, function() {
                    doc.detachEvent(domloaded, arguments.callee);
                    display_flash();
                });
                // If IE and not an iframe
                // continually check to see if the document is ready
                if (doc.documentElement.doScroll && !frameElement ) (function(){
                    if (flash_shown) return;
                    try {
                        // If IE is used, use the trick by Diego Perini
                        // http://javascript.nwbox.com/IEContentLoaded/
                        doc.documentElement.doScroll("left");
                    } catch( error ) {
                        setTimeout( arguments.callee, 0 );
                        return;
                    }
                    display_flash()
                })();
                // A fallback to window.onload that will always work
                window.attachEvent("load", display_flash);
            }
        }

        return function(opts) {
            cookie_name = opts.name || "webflash";
            container_id = opts.id || "webflash";
            on_display = lookup_method(opts.on_display, on_display);
            create_node = lookup_method(opts.create_node, create_node);

            return {
                payload: get_payload,
                render: attachLoadEvent
            }
        }
    })();

    // This function needs to live outside the anonymous function's closure for
    // YUICompressor to be able to mangle the private symbols because it uses
    // eval
    webflash.lj = function(s) {
        // Loads a JSON string
        var r;
        eval("r="+s);
        return r;
    };
};
