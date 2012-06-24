/*
* This javascript submodule takes care of all registration
* logic. It does not implement ember.js view binding due to
* its inherent simplicity of view-dependency.
*/

$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }

    if (typeof Jminee.Creation === 'undefined') {
        Jminee.Creation = {};
    }

    // registration non-ajax verification functions
    Jminee.Creation.checkFieldsValid = function(email, pass, user) {
        return (email.length > 0 && pass.length > 0 && user.length > 0);
    };

    Jminee.Creation.checkPasswordsMatch = function(pass, verifyPass) {
        return (pass === verifyPass);
    };

    // modal state-mutating functions
    Jminee.Creation.setModalFieldsInvalid = function() {
        $("div.modal-body p")[0].innerHTML = "We have determined that you have entered a non-valid email, username or password. Please re-enter your email, username and password.";
        $("h3.modal-titles")[0].innerHTML = "Invalid Username, Email or Password";
    };

    Jminee.Creation.setModalPasswordMismatch = function() {
        $("div.modal-body p")[0].innerHTML = "We have determined that the password you entered and the verification password do not match. Please re-enter your password and verification password.";
        $("h3.modal-titles")[0].innerHTML = "Password Mismatch";
    };

    Jminee.Creation.setModalConnectionError = function() {
        $("div.modal-body p")[0].innerHTML = "We are having problems connecting to the server. Please ensure that your internet connection is still working. If it is, this is our fault and we have been notified of this mishap.";
        $("h3.modal-titles")[0].innerHTML = "Connection Error";
    };

    Jminee.Creation.setModalRegistrationSuccessful = function() {
        $("div.modal-body p")[0].innerHTML = "Welcome to Jminee! A confirmation email has been sent to the address you supplied us. Please check your inbox and follow the instructions in the email we sent you to com plete your registration.";
        $("h3.modal-titles")[0].innerHTML = "Registration Successful!";
    };

    Jminee.Creation.setModalRegistrationPending = function() {
        $("div.modal-body p")[0].innerHTML = "We are attempting to register you on our servers.";
        $("h3.modal-titles")[0].innerHTML = "Registering...";
    };

    // the main registration controller
    Jminee.Creation.register = function() {
        var email      = $("#emailRegisterField").val();
        var pass       = $("#passRegisterField").val();
        var verifyPass = $("#passVerifyRegisterField").val();
        var user       = $("#userRegisterField").val();

        // handle non-ajax errors
        if (!Jminee.Creation.checkFieldsValid(email, pass, user)) {
            Jminee.Creation.setModalFieldsInvalid();
            return;
        }

        if (!Jminee.Creation.checkPasswordsMatch(pass, verifyPass)) {
            Jminee.Creation.setModalPasswordMismatch();
            return;
        }

        // there may be some delay due to the ajax call, so tell
        // the user that we're attempting to register them
        Jminee.Creation.setModalRegistrationPending();

        // make a registration ajax call
        $.getJSON("/registration?email_address="+email+"&password="+pass+"&user_name="+user+"&password_confirm="+verifyPass, function(json) {
            if (!json.success) {
                // handle error throwbacks here, including:
                // 1.) username/email already used
                // 2.) password not being long enough/not having the proper character conditions
                return;
            }
            Jminee.Creation.setModalRegistrationSuccessful();
        })
        .error(function() { Jminee.Creation.setModalConnectionError(); });
    };

    $("#registerButton").click(function() {
        Jminee.Creation.register();
    });
});
