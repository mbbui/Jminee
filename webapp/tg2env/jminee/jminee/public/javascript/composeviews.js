$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
		
	/*********************************************	
	/*		input views
	/*********************************************/	
	Jminee.TextField = Ember.TextField.extend({
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){
//				  view.set('size', 'input-xxlarge');				  
			  },
			  focusOut: function(event, view){
//				  view.set('size', 'input-mini');
			  }
		})
	});
	Jminee.TextArea = Ember.TextArea.extend({
		classNameBindings: ['span'],
		attributeBindings: ['placeholder', 'rows'],
		valueBinding: 'controller.text',
		rows: '6',
		placeholder: 'Type your message',
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){	
				  view.controller.focusIn(event, view);
			  } 
		})
	});
	
	/*********************************************	
	/*		compose views
	/*********************************************/
	Jminee.ComposeAddSubjectBtn = Ember.View.extend({
		subjectOnOff: false,
		click: function(event){
			if (this.subjectOnOff==false){
				this.$('a')[0].innerHTML='<i class="icon-minus-sign"></i> Add subject';
				this.set('subjectOnOff', true);				
			}
			else{
				this.$('a')[0].innerHTML='<i class="icon-plus-sign"></i> Add subject';
				this.set('subjectOnOff', false);
			}
		},
		template: Ember.Handlebars.compile(
				'{{#with view}}\
				<ul class="nav nav-pills">\
					<li>\
				<a html="#" style="cursor:pointer"><i class="icon-plus-sign"></i>Add subject</a>\
					</li>\
				</ul>{{/with}}')
	});
	Jminee.ComposeTextView = Ember.View.extend({
		template: Ember.Handlebars.compile(
				'<form class="form-horizontal">\
					{{#with controller}}\
						<div class="control-group">\
				 			<div class="control">\
								<div class="input-prepend">\
									<span class="add-on"><img width=20px height=15px src="/images/icons/conversation.png"></span>\
									{{view Jminee.TextField class="input-xxlarge" placeholder="Subject" valueBinding="view.subject"}}\
								</div>\
							</div>\
					  	</div>\
						<div class="control-group">\
				 			<div class="control">\
								{{view Jminee.TextArea spanBinding="view.textSpan" controller=this}}\
							</div>\
					  	</div>\
					{{/with}}\
				</form>')
	});
	
	Jminee.composeView = Ember.ContainerView.create({
		classNames: ['composemodal', 'hide'],
		eventManager: Ember.Object.create({
			  focusIn: function(event, view){
//				  view.$('input')[0].focus();				  
			  }
		}),
		headerView: Ember.View.create({
			classNames: ['composemodal-header'],
			headerData: [{iconUrl:"/images/icons/folder.png", placeholder:"Title", value: this.topic},
			                {iconUrl:"/images/icons/group.png", placeholder:"Members", value: this.members}],
			template: Ember.Handlebars.compile('\
						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
						<h5>Create a topic: </h5>\
						{{#each view.headerData}}\
							<div class="input-prepend">\
								<span class="add-on"><img width=20px height=15px {{bindAttr src="iconUrl"}}></span>\
								{{view Jminee.TextField class="input-xxlarge" placeholderBinding="placeholder" valueBinding="value"}}\
							</div>\
						{{/each}}')
		}),
		footerView: Ember.View.create({
			classNames: ['modal-footer'],
			template: Ember.Handlebars.compile('\
						<button  class="btn" type="submit" {{action "submit" target="controller"}}>Submit</button>')
		}),
		bodyView: Ember.ContainerView.create({
			classNames: ['composemodal-body'],
			subjectOnOffBinding: 'this.addSubjectBtn.subjectOnOff',
			changeInput: function(event){
				if(this.subjectOnOff){
					this.get('childViews').pushObject(this.commentView);
				}
				else{
					this.commentView.removeFromParent();
				}
			}.observes('subjectOnOff'), 
			addSubjectBtn: Jminee.ComposeAddSubjectBtn.create(),
			commentView: Jminee.MessageReviewView.create({tableBinding: 'Jminee.commentController.table',
				inputView: Jminee.ComposeTextView.create({textSpan: 'span10', controller: Jminee.commentController})}),
			childViews: ['addSubjectBtn']
		}),
		childViews: ['headerView', 'bodyView', 'footerView'],
	});
	
});
