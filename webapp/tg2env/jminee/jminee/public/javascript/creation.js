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
    Jminee.Creation.checkFieldsValid = function(email, pass) {
        return ((email.indexOf("@") != -1) && (email.indexOf(".") != -1) && (email.length > 6 && pass.length > 5));
    };

    Jminee.Creation.checkPasswordsMatch = function(pass, verifyPass) {
        return (pass === verifyPass);
    };

    // modal state-mutating functions
    Jminee.Creation.setModalFieldsInvalid = function() {
        $("div.modal-body p")[0].innerHTML = "We have determined that you have entered a non-valid email or password. Please re-enter your email and password.";
        $("h3.modal-titles")[0].innerHTML = "Invalid Email or Password";
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
        $("div.modal-body p")[0].innerHTML = "Welcome to Jminee! A confirmation email has been sent to the address you supplied us. Please check your inbox and follow the instructions in the email we sent you to complete your registration.";
        $("h3.modal-titles")[0].innerHTML = "Registration Successful!";
    };

    Jminee.Creation.setModalEmailAlreadyTakenError = function(email) {
        $("div.modal-body p")[0].innerHTML = "Sorry, but it appears the email \'"+email+"\' has already been taken.";
        $("h3.modal-titles")[0].innerHTML = "Email Already in Use";
    };

    Jminee.Creation.setModalEmailInvalidError = function(email) {
        $("div.modal-body p")[0].innerHTML = "Sorry, but it appears the email \'"+email+"\' is invalid.";
        $("h3.modal-titles")[0].innerHTML = "Email is Invalid";
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

        // handle non-ajax errors
        if (!Jminee.Creation.checkFieldsValid(email, pass)) {
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
        $.getJSON("/registration?email_address="+email+"&password="+pass, function(json) {
            if (json.success) {
                Jminee.Creation.setModalRegistrationSuccessful();
                return;
            }

            if (json.errors.email_address === 'Email address has already been taken') {
                Jminee.Creation.setModalEmailAlreadyTakenError(email);
            } else {
                Jminee.Creation.setModalEmailInvalidError(email);
            }
        })
        .error(function() { Jminee.Creation.setModalConnectionError(); });
    };

    $("#registerButton").click(function() {
        Jminee.Creation.register();
    });
});
