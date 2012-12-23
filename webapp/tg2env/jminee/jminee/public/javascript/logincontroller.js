$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    
    Jminee.inputValidateController = Ember.Object.create({
    	validate: function(view){
    		if (view.type=='email') return this.email(view);
    		else if (view.type=='password') return this.password(view);
    	},
    	email: function(view){
    		email = $.trim(view.value);
//    		return true;
    		if (email==null || email.match('^[^@]+@[^@\.]+\.[^@\.]+$')==null){
    			if (this.alertView)
    				this.alertView.show(view,'Wrong email format!');
    			return false;
    		}
    		return true;
    	},
    	password: function(view){
    		password = $.trim(view.value);
    		if (password==null || password==''){
    			if (this.alertView)
    				this.alertView.show(view,'Password cannot be blank!');
    			return false;
    		}    			    		
    		return true;
    	}
    });
    
    Jminee.loginController = Ember.Controller.create({
    	keepLogIn: false,
//    	isEmailValid: false,
//    	isPasswordValid: false,
    	login: function(){
    		if (!this.isEmailValid || !this.isPasswordValid){
    			console.log('Not valid inputs');
    			return;
    		}
    		$.ajax({
		     	url: '/login_handler',
		     	data: {login: this.email, password: this.password, remember: this.keepLogIn},
    			dataType: 'json',
    			success: function(resp){
    				return resp.data;
    			},
    			error: function(resp){
    				Jminee.loginAlertView.show('Error connecting server!');
    			} 
		    });
    	}
    });
    
   
});