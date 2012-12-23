$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		login/signin views
	/*********************************************/
	Jminee.LogInField = Ember.TextField.extend({
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){
				  if (Jminee.loginAlertView.relatedView==view)
					  Jminee.loginAlertView.removeFromParent();				  
			  },
			  focusOut: function(event, view){
				  view.set('isValid',Jminee.inputValidateController.validate(view));
			  }
		})
	});
	
	Jminee.loginAlertView = Ember.View.create({
		classNames: ['span4', 'offset6'],
		show: function(relatedView, text){
			if (this.isVisible)
				this.removeFromParent();
			this.relatedView=relatedView;		
			this.set('text',text);
			this.appendTo("#main_container");			
		},
		template: Ember.Handlebars.compile(
			'<div type"input" class="alert alert-error">\
				{{text}}\
			</div>'
		),		
	});
	
	Jminee.loginView = Ember.View.create({
		tagName: 'form',
		classNames: ['well', 'span4', 'offset6', 'form-horizontal'],	
		template: Ember.Handlebars.compile(
			'{{#with Jminee.loginController}} <div class="control-group">\
				{{view Jminee.LogInField placeholder="Email" type="email" valueBinding="email" isValidBinding="isEmailValid"}}\
			</div>\
			<div class="control-group">\
				{{view Jminee.LogInField type="password" placeholder="Password" valueBinding="password" isValidBinding="isPasswordValid"}}\
			</div>\
			<div class="control-group">\
			    <label class="checkbox">\
					{{view Ember.Checkbox checkedBinding="keepLogIn"}} Keep me log in\
				</label>\
			    <div class="row">\
			    <button {{action "login" target="Jminee.loginController"}} class="btn span2">Log in / Sign up</button> <a class="span2" href="#" >Forget password</a>\
			    </div>\
			</div>{{/with}}'
		),
	});
	
	Jminee.inputValidateController.reopen({alertView: Jminee.loginAlertView});
		
});
