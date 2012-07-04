/*
 * This javascript submodule takes care of all registration
 * logic. It does not implement ember.js view binding due to
 * its inherent simplicity of view-dependency.
*/

$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }

    if (typeof Jminee.Login === 'undefined') {
        Jminee.Login = {};
    }

    // the main login controller
    Jminee.Login.login = function() {
        var email = $("#emailLogin").val();
        var pass  = $("#passLogin").val();

        if (email.length == 0 || pass.length == 0) {
            return;
        }

        $.getJSON("/login_handler?login="+email+"&password="+pass, function(json) {
            if (!json.success) {
                // handle error throwbacks here
                return;
            }
            alert("success!");
        })
        .error(function() {          });
    };

    // the main logout controller
    Jminee.Login.logout = function() {

    };

    $("#loginButton").click(function() {
        Jminee.Login.login();
    });
});
