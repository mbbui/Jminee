$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		review view
	/*********************************************/
	Jminee.reviewView = ember.View.create({
		
	})
	
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
//		textChanged: function(){
//			  var str = $.trim(this.value);
//			  if (str.match('#[tT]able().*$')){
//				  console.log(str);  
//			  }
//		  }.observes('value'), 
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
	

	
	
	/*********************************************	
	/*		topic view
	/*********************************************/	
	Jminee.TopicView = Ember.View.extend({
		tagName: 'li',
		layout: Ember.Handlebars.compile('<a href="#" class="thumbnail">\
				<img src="http://placehold.it/160x120" alt="">\
				<p>{{yield}}</p></a>'),
		classNames: ['span2'],
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  	view.get('controller').selected();
			  }
		}),
		
		content: function(){
			var str=this.title;
			return new Handlebars.SafeString(str); 
		}.property()
	});
	
	Jminee.topicListView = Ember.View.create({
		tagName: 'ul',
		classNames: ['thumbnails'],
		template: Ember.Handlebars.compile('{{#each Jminee.topicListController}}\
												{{#view Jminee.TopicView title=title controller=this}}\
													{{view.content}}\
												{{/view}}\
											{{/each}}'),
	});
	
	Jminee.topicListContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span12'],
		childViews: [Jminee.topicListView]
	});


	/*********************************************	
	/*		main view
	/*********************************************/	
	Jminee.currentMainViewName = 'topic';
	Jminee.mainView = Ember.ContainerView.create({
			tagName: 'div',
			classNames: ['row'],
			mainViewsDict:{'topic':[Jminee.topicListContainer], 'subject':[Jminee.subjectListContainer,Jminee.subjectContentListView]},
			changeChildView: function(){
				while(this.get('childViews').popObject());
				this.get('childViews').pushObjects(this.mainViewsDict[Jminee.topicNavController.mainViewName]); 
			}.observes('Jminee.topicNavController.mainViewName')
	});
	Jminee.mainView.appendTo("#main_container");
//	Jminee.mainView.changeChildView([Jminee.subjectListContainer,Jminee.subjectContentListView]);
//	Jminee.mainView.changeChildView([Jminee.topicListContainer]);
	
	
});

function showModal(elem){
	elem.$("input")[0].focus();
};

//$(window).ready(function(){
//	window.Jminee.editView.$().on('show', function(){
//		window.Jminee.editView.$('input')[0].focus();
//	});
//	window.Jminee.editView.$().modal('show');
//});

