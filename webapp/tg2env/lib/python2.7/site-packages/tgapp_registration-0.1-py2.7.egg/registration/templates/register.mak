<html>

    <head>
        <title>Jminee - Notifications Simplified</title>
        <meta charset="utf-8">
		<script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
        <script type="text/javascript" src="javascript/ember-0.9.8.1.min.js"></script>
        <link type="text/css" rel="stylesheet" href="/css/styles.css">
    </head>

    <body>
    	<div id="registration_new">
    		${form(value=value, action=action) |n}
		</div>
    </body>

</html>

<%doc>
  <%inherit file="local:templates.master"/>

<%def name="title()">Register New User</%def>


<div id="registration_new">
    ${form(value=value, action=action) |n}
</div>
</%doc>