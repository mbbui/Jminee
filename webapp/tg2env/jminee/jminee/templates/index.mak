<!DOCTYPE html>
<html lang="en">

    <head>
        <title>Jminee - Notifications Simplified</title>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link type="text/css" rel="stylesheet" href="/bootstrap/css/bootstrap-responsive.min.css">
        <link type="text/css" rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">

        <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
        <script type="text/javascript" src="/javascript/ember-0.9.8.1.min.js"></script>
        <script type="text/javascript" src="/bootstrap/js/bootstrap-modal.js"></script>
        <script type="text/javascript" src="/bootstrap/js/bootstrap-transition.js"></script>

        <link type="text/css" rel="stylesheet" href="/css/styles.css">
        <script src="/javascript/creation.js" type="text/javascript"></script>
    </head>

    <body>
        <!-- navbar -->
        <div class="navbar navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container">
                    <a class="brand pull-left" href="#">
                        Jminee
                    </a>
                    <form class="navbar-form pull-right form-inline">
                        <input type="text" placeholder="Email" class="input-small">
                        <input type="password" placeholder="Password" class="input-small">
                        <label class="checkbox">
                            <input type="checkbox"> Remember Me
                        </label>
                        <button type="submit" class="btn">Login</button>
                    </form>
                </div>
            </div>
        </div>
        <!-- /navbar -->

        <!-- login page -->
        <div class="container">
            <section>
                <div class="page-header">
                    <h2>
                        Why Jminee?
                        <small>Let's make a stance. Let's revolutionize notifications.</small>
                    </h2>
                </div>
                <div class="row">
                    <div class="span4">
                        <h3>Email is Working Overtime</h3>
                        <p>Email wasn't invented with the notion of our current, fast-paced society in mind. It does its job well, but it just wasn't meant for the micro-conversations we have with people over the internet every day. There was no Facebook. No Twitter. The internet was a cyber wild west, and had much fewer people using it. Since email has been such a fundamental part of communicating over the internet, its uses have been dragged far and stretched thin. Busy people with many tasks use their email as a means of reminding them of their current todos. We think this is wrong. These todos end up cluttering your inbox and reduce your productivity and peace-of-mind.</p>
                    </div>
                    <div class="span4">
                        <h3>Organization and Granularity</h3>
                        <p>Currently, people organize their life into two sections: work and play. Their social life notifications get relayed to them through Facebook and their professional life notifications through email. This is a very cut-and-dry way to split up one's life, considering work and play often intertwine. We believe there needs to be a better way to organize your notifications in the same place. With Jminee's topic-based notification system, you can receive notifications from professors for a certain class you may be taking, from employees within your team at work, from friends you regularly grab lunch with, etcetera. Subtopics make it easy to granulate the broad spectrums of your life and better model how you should really be receiving your notifications.</p>
                    </div>
                    <div class="span4">
                        <h3>Pushing Notifications</h3>
                        <p>You probably push notifications to people more often than you realize. You may email a coworker, asking that they complete a mandatory task. If you are a student, you may text everyone in your study group that the meeting place or time of your next study session has changed. These aren't involved conversations, but they are notifications that you probably want people to receive as soon as they are sent out. We believe it's time these notifications are available immediately in a safe, organized location.</p>
                    </div>
                </div>
            </section>

            <section>
                <div class="page-header">
                    <h2>
                        Give it a Test Drive
                        <small>Registration is as easy as an email and password.</small>
                    </h2>
                </div>
                <div class="container">
                    <form class="form-vertical">
                        <label>Email:</label>
                        <input type="text" placeholder="Email" id="emailRegisterField">
                        <label>Username:</label>
                        <input type="text" placeholder="Username" id="userRegisterField">
                        <label>Password:</label>
                        <input type="password" placeholder="Password" id="passRegisterField">
                        <label>Verify it:</label>
                        <input type="password" placeholder="Again! Again!" id="passVerifyRegisterField">
                        <br/>
                        <button class="btn btn-large btn-primary" data-toggle="modal" data-target="#registrationModal" id="registerButton">Sign Me Up!</button>
                    </form>
                </div>
            </section>
        </div>
        <!-- /login page -->

        <!-- registration modal -->
        <div class="modal hide fade" id="registrationModal" data="backdrop keyboard show">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">x</button>
                <h3 class="modal-titles">Registration Successful!</h3>
            </div>
            <div class="modal-body">
                <p>Welcome to Jminee! A confirmation email has been sent to the address you supplied us. Please check your inbox and follow the instructions in the email we sent you to complete your registration.</p>
            </div>
            <div class="modal-footer">
                <a href="#" class="btn" data-dismiss="modal">Close</a>
            </div>
        </div>
        <!-- /registration modal -->
    </body>

</html>
