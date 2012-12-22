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
	
	/*********************************************	
	/*		login/signin views
	/*********************************************/
	Jminee.loginView = Ember.View.create({
		tagName: 'form',
		classNames: ['well', 'span4', 'offset6', 'form-horizontal'],
		template: Ember.Handlebars.compile(
		'<div class="control-group">\
				<input type="text" placeholder="Email">\
		 </div>\
		 <div class="control-group">\
		    <input type="password" placeholder="Password">\
		</div>\
		<div class="control-group">\
		      <label class="checkbox">\
		        <input type="checkbox"> Keep me log in\
		      </label>\
		      <div class="row">\
		      <button type="submit" class="btn span2">Log in / Sign up</button> <a class="span2" href="#" >Forget password</a>\
		      </div>\
		</div>')
	});
	
	Jminee.mainView = Ember.ContainerView.create({
		childViews: [Jminee.composeView, Jminee.contentNavContainer, Jminee.contentView]
	});
	
//	Jminee.composeView.appendTo("#main_container");	
//	Jminee.contentNavContainer.appendTo("#main_container");
//	Jminee.contentView.appendTo("#main_container");
	Jminee.loginView.appendTo("#main_container")
//	Jminee.mainView.appendTo("#main_container");
});
