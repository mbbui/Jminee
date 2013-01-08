
<!DOCTYPE html>
<html>
<body >
	<div style="*position: relative; *z-index: 2; margin-bottom: 20px; overflow: visible;
  			color: #999999;">
  		<div style="min-height: 40px;
			  padding-right: 20px;
			  padding-left: 20px;
			  background-color: #fafafa;
			  background-image: -moz-linear-gradient(top, #ffffff, #f2f2f2);
			  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#ffffff), to(#f2f2f2));
			  background-image: -webkit-linear-gradient(top, #ffffff, #f2f2f2);
			  background-image: -o-linear-gradient(top, #ffffff, #f2f2f2);
			  background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);
			  background-repeat: repeat-x;
			  border: 1px solid #d4d4d4;
			  -webkit-border-radius: 4px;
			     -moz-border-radius: 4px;
			          border-radius: 4px;
			  filter: progid:dximagetransform.microsoft.gradient(startColorstr='#ffffffff', endColorstr='#fff2f2f2', GradientType=0);
			  *zoom: 1;
			  -webkit-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.065);
			     -moz-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.065);
			          box-shadow: 0 1px 4px rgba(0, 0, 0, 0.065);
			   background-color: #1b1b1b;
				  background-image: -moz-linear-gradient(top, #222222, #111111);
				  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#222222), to(#111111));
				  background-image: -webkit-linear-gradient(top, #222222, #111111);
				  background-image: -o-linear-gradient(top, #222222, #111111);
				  background-image: linear-gradient(to bottom, #222222, #111111);
				  background-repeat: repeat-x;
				  border-color: #252525;
				  filter: progid:dximagetransform.microsoft.gradient(startColorstr='#ff222222', endColorstr='#ff111111', GradientType=0);">
          	<div style="width: auto;">
          		<a style="display: block;
					  float: left;
					  padding: 10px 20px 10px;
					  margin-left: -20px;
					  font-size: 20px;
					  font-weight: 200;
					  color: #777777;
					  text-shadow: 0 1px 0 #ffffff; color: #999999;
					  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
					  text-decoration: none;"
					  href="#">
  					Jminee
  				</a>
          	</div>
          </div>
  	</div>	
	<p style="font-family:helvetica, arial, sans-serif;font-size:14px;line-height:24px;color:#666666; text-decoration: none">
		${user_name | n} invited you to join a topic on <a href="http://www.jminee.com" style="text-decoration: none">Jminee</a>
	</p>	
	<ul style="padding: 10px 15px; margin: 0 0 20px; list-style: none; background-color: #f5f5f5;
  				-webkit-border-radius: 4px 0px 0px 4px; -moz-border-radius: 4px 0px 0px 4px; 
  				border-radius: 4px 0px 0px 4px;">
		<li style="display: inline-block; *display: inline; text-shadow: 0 1px 0 #ffffff;
  					*zoom: 1;"> 
			<a href="#" style="text-decoration: none">Topic</a>
			<span style="padding: 0 5px; color: #ccc;">></span>		
		</li>
		<li style="display: inline-block; *display: inline; text-shadow: 0 1px 0 #ffffff;
  					*zoom: 1;">
			<a href="#" style="text-decoration: none">${topic | n} </a>
			<span style="padding: 0 5px; color: #ccc;">></span>	
		</li>
	</ul>
</body>
</html>

