$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		review view
	/*********************************************/
//	Jminee.ReviewView = Jminee.SubjectTblContentView.extend({
//		table: {header: ['#','Name']},
//	});
	
	/*********************************************	
	/*		edit view
	/*********************************************/	
	Jminee.TextField = Ember.TextField.extend({
		classNameBindings: ['size'],
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){
				  view.set('size', 'input-xxlarge');				  
			  },
			  focusOut: function(event, view){
				  view.set('size', 'input-mini');
			  },
		}),
	});
	Jminee.TextArea = Ember.TextArea.extend({
		classNameBindings: ['span'],
		attributeBindings: ['placeholder', 'rows'],
		rows: '12',
		placeholder: 'Type your message',
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){				
			  }, 
		}),
	});
	Jminee.composeView = Ember.ContainerView.create({
		classNames: ['editmodal', 'hide'],
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){
				  view.$('input')[0].focus();
				  
			  },
		}),
		headerView: Ember.View.create({
			tagName: 'div',
			classNames: ['editmodal-header'],
			headerData: [{iconUrl:"/images/icons/folder.png", placeholder:"Topics", value: this.topic},
			                {iconUrl:"/images/icons/group.png", placeholder:"Members", value: this.members},
			                {iconUrl:"/images/icons/conversation.png", placeholder:"Subject", value: this.subject}],
			template: Ember.Handlebars.compile('\
						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
						<h5>Compose: </h5>\
						<div class="input-prepend">\
							{{#each headerView.headerData}}\
								<span class="add-on"><img width=20px height=15px {{bindAttr src="iconUrl"}}></span>\
								{{view Jminee.TextField size="input-mini" placeholderBinding="placeholder" valueBinding="value"}}\
							{{/each}}\
						</div>')
		}),
		
		bodyView: Ember.ContainerView.create({
			classNames: ['editmodal-body'],
			commentView: Jminee.ComposeReviewView.create({textSpan: 'span12', composeControllerName: 'Jminee.composeController', tableBinding: 'Jminee.composeController.table' }),
//			editView: Jminee.EditReviewView.create({textSpan: "span12"}),
			childViews: ['commentView']
		}),
		childViews: ['headerView', 'bodyView'],
	});
	Jminee.composeView.appendTo("#main_container");	
});
