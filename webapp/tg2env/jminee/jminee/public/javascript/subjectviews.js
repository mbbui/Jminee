$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		subject views
	/*********************************************/
	Jminee.reviewView = Jminee.MessageReviewView.create({tableBinding: 'Jminee.commentController.table', 
														controller: Jminee.commentController}),
														
	Jminee.subjectContentContainer = Ember.ContainerView.create({
		classNames: ['span9'],
		contentView: Ember.View.create({
			template: Ember.Handlebars.compile('{{#each Jminee.subjectContentListController}}\
													{{#if table}}\
														{{view Jminee.TableMessageView table=table}}\
													{{else}}\
														{{view Jminee.MessageView}}\
													{{/if}}\
												{{/each}}')
		}),
		reviewView: Jminee.reviewView,
		childViews:['contentView', 'reviewView']
	});
});
