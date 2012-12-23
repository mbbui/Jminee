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
	
//	Jminee.composeView.appendTo("#main_container");	
//	Jminee.contentNavContainer.appendTo("#main_container");
//	Jminee.contentView.appendTo("#main_container");
	Jminee.loginView.appendTo("#main_container");
	
//	Jminee.mainView.appendTo("#main_container");
});
