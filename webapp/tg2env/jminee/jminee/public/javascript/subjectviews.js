$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		subject views
	/*********************************************/
//	Jminee.subjectCommentView = Jminee.MessageReviewView.create({tableBinding: 'Jminee.commentController.table',
//		inputView: Jminee.MessageInputView.create({textSpan: 'span8', controller: Jminee.commentController})});
    
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
		commentView: Jminee.MessageReviewView.create({tableBinding: 'Jminee.commentController.table',
			inputView: Jminee.MessageInputView.create({textSpan: 'span8', controller: Jminee.commentController})}),
		childViews:['contentView', 'commentView']
	});
});
