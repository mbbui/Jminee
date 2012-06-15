<!DOCTYPE html>
<html>

    <head>
        <title>Jminee - Notifications Simplified</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1"> 
        <link rel="stylesheet" href="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.css" />
        <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
        <script src="http://code.jquery.com/mobile/1.1.0/jquery.mobile-1.1.0.min.js"></script>
        <script type="text/javascript" src="javascript/ember-0.9.8.1.min.js"></script>
        <link type="text/css" rel="stylesheet" href="/css/styles.css">
    </head>

    <body>
        <!-- login page -->
        <div id="loginPage" data-role="page" data-theme="b">
            <div data-role="header">
                <h1>Jminee</h1>
            </div>
            <div data-role="content">
                <div data-role="fieldcontain">
                    <label for="login_userName">Username:</label>
                    <input type="text" name="name" id="login_userName" value="" />
                    <label for="login_password">Password:</label>
                    <input type="password" name="password" id="login_password" value="" />
                    <input type="submit" id="loginSubmit" value="Login" />
                </div>
                <input type="button" id="loginRegister" value="Register" />
            </div>
            <div data-role="footer">
                <h4>Login</h4>
            </div>
        </div>
        <!-- /login page -->
    </body>

</html>
