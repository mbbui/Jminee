<html>

    <head>
        <title>Jminee - Notifications Simplified</title>
        <meta charset="utf-8">
		<script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
        <script type="text/javascript" src="javascript/ember-0.9.8.1.min.js"></script>
        <link type="text/css" rel="stylesheet" href="/css/styles.css">
    </head>

    <body>
    	<div id="registration_complete">
    <h1>Registration completed</h1>
    <p>
        <h4>Congratulations, your registration has been completed.</h4>
        <strong>An email</strong> has been sent to <strong>${email}</strong> to activate the account,
        please proceed by clicking on the provided link to be able
        to login.
    </p>
</div>
    </body>

</html>

<%doc>
<%inherit file="local:templates.master"/>

<%def name="title()">Complete registration</%def>

<div id="registration_complete">
    <h1>Registration completed</h1>
    <p>
        <h4>Congratulations, your registration has been completed.</h4>
        <strong>An email</strong> has been sent to <strong>${email}</strong> to activate the account,
        please proceed by clicking on the provided link to be able
        to login.
    </p>
</div>
</%doc>