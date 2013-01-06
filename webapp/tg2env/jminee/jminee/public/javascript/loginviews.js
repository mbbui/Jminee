$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		login/signin views
	/*********************************************/
	Jminee.LogInField = Ember.TextField.extend(Jminee.viewWithAlert, {
		attributeBindings: ['autofocus'],	
		alertView: Jminee.loginAlertView,
		alertType: "alert-error",
	});
		
	Jminee.EmailField = Jminee.LogInField.extend({
		placeholder: "Email...",
		type: "email",
		alertText: Jminee.Message2User.WRONGEMAILFORMAT,
		isValid: function(email){
			return (email!=null && email.match('^[^@]+@[^@\.]+\.[^@\.]+$')!=null);
		},
		
		focusIn: function(){
			this.set('existingUser', null);
			this._super();
		},
		
		focusOut: function(){
			if (this.isValid(this.value))
				this.checkEmailExist();
			else
				this._super();
		},
		
		afterCheckEmailExist: function(){
			if (this.get('existingUser')!=null){
				if (this.get('existingUser')){
					
				}
				else
					Jminee.loginAlertView.show(this, Jminee.Message2User.NEWUSER, 'alert-warning');
			}
		}.observes('existingUser'),
		
		checkEmailExist: function(){
			$.ajax({
		     	url: '/registration/email_exist',
		     	data: {email: this.value},
    			dataType: 'json',
    			success: function(resp){
    				if (!resp.success)
    					//TODO: change error message
    					Jminee.loginAlertView.show(Jminee.loginView, 'Error code '+resp.error_code);
    				else {
    					//TODO: update account info
    					Jminee.loginView.mainLogin.set('existingUser',resp.email_exist);    					    					    				
    				}	
    				return resp;
    			},
    			error: function(resp){
    				Jminee.loginAlertView.show(Jminee.loginView, 'Error connecting server!');
    			} 
		    });
		}
	});
	
	Jminee.SignupLoginButton = Ember.View.extend({
		tag:'button',
		classNameBindings: ['btn', 'span'],
		btn: true,
		span: 'span1',
		
		changeStatus: function(){
			if (this.get('existingUser'))
				this.$()[0].innerHTML = 'Log in';
			else if(this.get('existingUser')==false)
				this.$()[0].innerHTML = 'Sign up';			
		}.observes('existingUser'),
		
		template: Ember.Handlebars.compile(
			'Submit'
		),
		click: function(){
			if (this.get('existingUser')!=null && !Jminee.empty(this.controller.password)){
				if (this.get('existingUser')==false)
					this.controller.signin();
				else
					this.controller.login();
			}
		},
//		handleKeyEvent: function(event) {
//            switch (event.type) {
//                case "keydown": console.log('keypress'); break;
//                case "keypress": emberEvent = 'keyPress'; break;
//            }
//		}
	});
	
	//make this container so we can insert the alertView
	Jminee.loginView = Ember.ContainerView.create({
		classNames: ['span5', 'offset6'],
		mainLogin: Ember.View.create({
			classNames: ['well', 'form-horizontal'],
			tagName: 'form',
			existingUser: null,
			template: Ember.Handlebars.compile(
					'<div class="control-group">You can both <strong>sign up</strong>\
						or <strong>log in</strong> here</div>\
					{{#with Jminee.loginController}}\
					<div class="control-group">\
						{{view Jminee.EmailField autofocus="autofocus" valueBinding="email"\
							existingUserBinding="view.existingUser"}}\
					</div>\
					<div class="control-group">\
						{{view Jminee.LogInField type="password" placeholder="Password..."\
							valueBinding="password" alertText="Password cannot be blank!"}}\
					</div>\
					<div class="control-group">\
					    <label class="checkbox">\
							{{view Ember.Checkbox checkedBinding="keepLogIn"}} Keep me log in\
						</label>\
					    <div class="row">\
							{{view Jminee.SignupLoginButton existingUserBinding="view.existingUser"\
								controller=this}}\
							<a class="span2" href="#">Forget password</a>\
					    </div>\
					</div>{{/with}}'
				),
		}),
		childViews: ['mainLogin'],
	});
	
//	Jminee.inputValidateController.reopen({alertView: Jminee.loginAlertView});
	Jminee.loginAlertView.reopen({parent: Jminee.loginView});	
});
