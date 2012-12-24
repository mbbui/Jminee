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
//    		return true;
    		email = $.trim(view.value);
    		if (email==null || email.match('^[^@]+@[^@\.]+\.[^@\.]+$')==null){
    			if (this.alertView)
    				this.alertView.show(view,'Wrong email format!');
    			return false;
    		}
    		return true;
    	},
    	password: function(view){
//    		return true;
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
    	isEmailValid: false,
    	isPasswordValid: false,
    	login: function(){
    		if (!this.isEmailValid || !this.isPasswordValid) return;
    		if (Jminee.loginAlertView.relatedView==Jminee.loginView)
				  Jminee.loginAlertView.removeFromParent();
    		$.ajax({
		     	url: '/login_handler',
//		     	data: {login: Jminee.loginController.email, password: Jminee.loginController.password, 
//		     			remember: Jminee.loginController.keepLogIn},
		     	data: {login: 'testuser', password: 'testuser'},
    			dataType: 'json',
    			success: function(resp){
    				if (!resp.success)
    					//TODO: change error message
    					Jminee.loginAlertView.show(Jminee.loginView, 'Error code '+resp.error_code);
    				else {
    					//TODO: update account info
    					Jminee.userInfo.setInfo(Jminee.loginController);
    					Jminee.loginController.set('email', null);
    					Jminee.loginController.set('password', null);    					
    					Jminee.set('isLogin',true);
//    					Jminee.topicListController.reload();    					
    				}	
    				return resp;
    			},
    			error: function(resp){
    				Jminee.loginAlertView.show(Jminee.loginView, 'Error connecting server!');
    			} 
		    });
    	},
	    logout: function(){
			//TODO: check if use already login
			$.ajax({
		     	url: '/logout_handler',
				dataType: 'json',
				success: function(resp){
					if (!resp.success)
						//TODO: change error message
						Jminee.loginAlertView.show(Jminee.loginView, 'Error code '+resp.error_code);
					else {
						Jminee.userInfo.clearInfo();
						Jminee.set('isLogin',false);
					}	
					return resp;
				},
				error: function(resp){
					Jminee.loginAlertView.show(Jminee.loginView, 'Error connecting server!');
				} 
		    });
		}
    });
    
   
});