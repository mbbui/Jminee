$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
			
	/*********************************************	
	/*		content view
	/*********************************************/	
	Jminee.contentView = Ember.ContainerView.create({
			classNames: ['row'],
			contentViewsDict:{'topic':[Jminee.topicListContainer], 'subject':[Jminee.subjectNavContainer,Jminee.subjectContentContainer]},
			contentTypeBinding: 'Jminee.topicNavController.contentType',
			changeChildView: function(){
				while(this.get('childViews').popObject());
				this.get('childViews').pushObjects(this.contentViewsDict[this.contentType]); 
			}.observes('contentType')
	});
	
	Jminee.mainView = Ember.ContainerView.create({
		childViews: [Jminee.composeView, Jminee.contentNavContainer, Jminee.contentView]
	});
	
	Jminee.accountView = Ember.View.create({
		tagName: 'ul',
		classNames: ['nav', 'pull-right'],
		template: Ember.Handlebars.compile(
				'<li class="dropdown pull-right">\
					<a href="#" class="dropdown-toggle" data-toggle="dropdown">\
						{{Jminee.userInfo.email}} <b class="caret"></b>\
					</a>\
					<ul class="dropdown-menu">\
						<li><a {{action "showAccount"}} href="#">Account</a></li>\
						<li class="divider"></li>\
						<li><a {{action "logout" target="Jminee.loginController"}} href="#">\
							Log out</a>\
						</li>\
					</ul>\
				</li>')
	});  
	
	Jminee.reopen({changeView: function(){
		if (!Jminee.isLogin){
			Jminee.mainView.removeFromParent();
			Jminee.accountView.removeFromParent();
			Jminee.loginView.appendTo("#main_container");
		}
		else{
			Jminee.loginView.removeFromParent();
			Jminee.mainView.appendTo("#main_container");
			Jminee.accountView.appendTo("#navbar_container");
		}			
	}.observes('isLogin')});
	
	Jminee.set('isLogin',false);
	
});
