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
				'<ul class="nav nav-pills">\
					<li>\
						<a html="#" style="cursor:pointer"><i class="icon-plus-sign"></i> Add subject</a>\
					</li>\
				</ul>')
	});
	
	Jminee.AddTopicTitleView = Ember.TextField.extend(Jminee.viewWithAlert, {
		placeholder:"Topic...",
		alertView: Jminee.createTopicAlertView,
		alertText: 'Untitled topic will be placed in a folder named after all member\'s email address.',
		alertType: 'alert-info'
	});
	
	Jminee.AddMembersView = Ember.TextField.extend(Jminee.viewWithAlert, {
		placeholder:"Members...",
		alertView: Jminee.createTopicAlertView,
		alertText: 'You are the only member of this topic.',
		alertType: 'alert-info'
	});
	
	Jminee.AddSubjectComposeView = Jminee.AddSubjectTitleView.extend(Jminee.viewWithAlert, {
		alertView: Jminee.createTopicAlertView,
		alertText: 'If subject\'s title is empty, only topic will be created.', 
		alertType: 'alert-info',
	});
	
	Jminee.SubjectContentTextArea = Ember.TextArea.extend({
		classNameBindings: ['span'],
		attributeBindings: ['placeholder', 'rows'],
		placeholder: 'Type your message...',
	});
	
	Jminee.ComposeTextView = Ember.View.extend({
		alertView: Jminee.createTopicAlertView,
		template: Ember.Handlebars.compile(
				'<form class="form-horizontal">\
					<div class="control-group">\
			 			<div class="control">\
							<div class="input-prepend">\
								<span class="add-on"><img width=20px height=15px src="/images/icons/conversation.png"></span>\
								{{view "Jminee.AddSubjectComposeView" class="input-xxlarge" valueBinding="Jminee.composeView.subject"}}\
							</div>\
						</div>\
				  	</div>\
					<div class="control-group">\
			 			<div class="control">\
							{{view "Jminee.SubjectContentTextArea" spanBinding="view.textSpan"\
								valueBinding="Jminee.composeView.message" rows="6"}}\
						</div>\
				  	</div>\
				</form>')
	});
	
	Jminee.composeView = Ember.ContainerView.create({
		classNames: ['composemodal', 'hide'],
		controller: Jminee.createTopicController,
		headerView: Ember.View.create({
			classNames: ['composemodal-header'],
			template: Ember.Handlebars.compile('\
						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
						<h5>Create a topic: </h5>\
						<div class="input-prepend">\
							<span class="add-on"><img width=20px height=15px src="/images/icons/folder.png"></span>\
							{{view Jminee.AddTopicTitleView class="input-xxlarge" valueBinding="Jminee.composeView.topic"}}\
						</div>\
						<div class="input-prepend">\
							<span class="add-on"><img width=20px height=15px src="/images/icons/folder.png"></span>\
							{{view Jminee.AddMembersView class="input-xxlarge" valueBinding="Jminee.composeView.members"}}\
						</div>\
						<div class="input-prepend">\
							<span class="add-on"><img width=20px height=15px src="/images/icons/folder.png"></span>\
							{{view Ember.TextField class="input-xxlarge" placeholder="Logo URL..."\
								valueBinding="Jminee.composeView.logourl"}}\
						</div>')
		}),
		footerView: Ember.ContainerView.create({
			classNames: ['modal-footer'],
			alertView: Ember.ContainerView.create({
				classNames: ['span8']
			}),
			button: Ember.View.create({
				template: Ember.Handlebars.compile('\
							<button  class="btn" type="submit" {{action "submit" target="Jminee.composeView"}}>Submit</button>')
			}),
			childViews:['alertView', 'button'],
			
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
			commentView: Jminee.CommentReviewView.create({
				inputView: Jminee.ComposeTextView.create({textSpan: 'span10'})
			}),				
			childViews: ['addSubjectBtn']
		}),
		
		childViews: ['headerView', 'bodyView', 'footerView'],
		
		submit: function(event){
			this.controller.submit({title: this.topic, members: this.members, 
				logourl: this.logourl, subject: this.subject, message: this.message});
//			if (this.message && this.subject && 
//					!this.message.match(/^\s*$/) && 
//					!this.subject.match(/^\s*$/)){
//				this.controller.submit({topic: this.topic, subject: this.subject, 
//					members: this.members, content: this.content});
//			}
		}
	});
	
	Jminee.createTopicAlertView.reopen({parent: Jminee.composeView.footerView.alertView});
});
