$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
			
	/*********************************************	
	/*		main view
	/*********************************************/	
	
	Jminee.mainView = Ember.ContainerView.create({
			tagName: 'div',
			classNames: ['row'],
			mainViewsDict:{'topic':[Jminee.topicListContainer], 'subject':[Jminee.subjectNavContainer,Jminee.subjectContentContainer]},
			changeChildView: function(){
				while(this.get('childViews').popObject());
				this.get('childViews').pushObjects(this.mainViewsDict[Jminee.topicNavController.mainViewName]); 
			}.observes('Jminee.topicNavController.mainViewName')
	});
	
	Jminee.composeView.appendTo("#main_container");	
	Jminee.contentNavContainer.appendTo("#main_container");
	Jminee.mainView.appendTo("#main_container");
		
});
