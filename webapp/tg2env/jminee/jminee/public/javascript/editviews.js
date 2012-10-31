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
	Jminee.editView = Ember.View.create({
		tagName: 'div',
		classNames: ['editmodal', 'hide'],
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){
				  view.$('input')[0].focus();				  
			  },
		}),
		childViewData: [{iconUrl:"/images/icons/folder.png", placeholder:"Topics", value: this.topic},
		                {iconUrl:"/images/icons/group.png", placeholder:"Members", value: this.members},
		                {iconUrl:"/images/icons/conversation.png", placeholder:"Subject", value: this.subject}],
		template: Ember.Handlebars.compile('\
				<div class="editmodal-header">\
					<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
					<h5>Compose: </h5>\
					<div class="input-prepend">\
						{{#each childViewData}}\
							<span class="add-on"><img width=20px height=15px {{bindAttr src="iconUrl"}}></span>\
							{{view Jminee.TextField size="input-mini" placeholderBinding="placeholder" valueBinding="value"}}\
						{{/each}}\
					</div>\
				</div>\
				<div class="editmodal-body">\
					<form>\
						<br>\
						<div>\
							{{view Jminee.TextArea span="span12" valueBinding="Jminee.textAreaController.text"}}\
						</div>\
						<br>\
						<div>\
							<a href="#" class="btn">Submit</a>\
						</div>\
					</form>\
				</div>'
			)
	});
	Jminee.editView.appendTo("#main_container");	
});
