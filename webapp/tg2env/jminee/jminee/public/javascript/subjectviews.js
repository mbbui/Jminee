$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		subject views
	/*********************************************/
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
		commentView: Jminee.MessageReviewView.create({textSpan: 'span8', composeControllerName: 'Jminee.commentController', tableBinding: 'Jminee.commentController.table' }),
		childViews:['contentView', 'commentView']
	});
});
