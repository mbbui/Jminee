$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		subject views
	/*********************************************/
//	Jminee.subjectCommentView = Jminee.CommentReviewView.create({tableBinding: 'Jminee.commentController.table',
//		inputView: Jminee.CommentInputView.create({textSpan: 'span8', controller: Jminee.commentController})});
    
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
		commentView: Jminee.CommentReviewView.create({tableBinding: 'Jminee.commentController.table',
			inputView: Jminee.CommentInputView.create({textSpan: 'span8', controller: Jminee.commentController})}),
		childViews:['contentView', 'commentView']
	});
});
