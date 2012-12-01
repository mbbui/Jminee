$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
//	Jminee.MainView = Ember.ContainerView.extend({
//		tagName: 'div',
//		classNames: ['row'],
//		changeChildView: function(childView){
//			this.childView=childView; 
//		}
//	});
	
	
//	Jminee.TopicListView = Ember.View.extend({
//		tagName: 'ul',
//		classNames: ['thumbnails'],
//		template: Ember.Handlebars.compile('{{#each Jminee.topicListController}}\
//											{{#view Jminee.topicView}}\
//													{{view.content}}\
//											{{/view}}\
//											{{/each}}')
//	});
	
	Jminee.SubjectView = Ember.View.extend({
		tagName: 'li',
		layout: Ember.Handlebars.compile('<a href="#">{{yield}}</a>'),
		classNameBindings: ['active'],
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  	view.set('active', true);
			  }
		}),
		
		content: function(){
			var str=this.title;
			if (this.including & Jminee.MSG){
				str+='<i class="icon-comment  pull-right"></i>';
			}
			if (this.including & Jminee.TBL){
				str+='<i class="icon-list-alt  pull-right"></i>';
			}
			return new Handlebars.SafeString(str);
		}.property()
	});

	Jminee.SubjectContentView = Ember.View.extend({
		tagName: 'div',
		classNames: ['well  well-small'],
		template: Ember.Handlebars.compile(
			'{{#if sender}}<a href="#">{{sender}} </a>:{{/if}}\
				{{#if message}}{{message}}{{/if}}'),
	});

	Jminee.SubjectTblContentView = Jminee.SubjectContentView.extend({
		template: Ember.Handlebars.compile(
			'{{#if sender}}<a href="#">{{sender}} </a>:{{/if}}\
			{{#if view.message}}{{view.message}}{{/if}}\
			{{#if view.table.title}}<h4>{{view.table.title}}</h4>{{/if}}\
			<table class="table table-bordered">\
			<thead><tr>\
			{{#each header in view.table.header}}\
				<td><h5>{{header}}</h5></td>\
			{{/each}}\
			</tr></thead>\
			<tbody>\
			{{#each row in view.table.data}}\
				<tr>\
					{{#each col in row}}\
						<td>{{col}}</td>\
					{{/each}}\
				</tr>\
			{{/each}}\
			</tbody></table>'
		)
	});

	Jminee.SubjectEditView = Jminee.SubjectContentView.extend({
		template: Ember.Handlebars.compile(
			'<form class="form-horizontal">\
		 		<div class="control-group">\
		 			<div class="control">\
						{{view Jminee.TextArea spanBinding="view.textSpan" valueBinding="view.textController"}}\
					</div>\
			  	</div>\
			  	<div class="control-group">\
		 			<div class="control">\
			  			<button  class="control" type="submit" class="btn">Submit</button>\
			  		</div>\
			  	</div>\
			</form>'),
	});

	Jminee.subjectListView = Ember.View.create({
		  tagName: 'ul',
		  classNames: ['nav', 'nav-pills', 'nav-stacked'],
		  template: Ember.Handlebars.compile(
				  '{{#each Jminee.subjectListController}}\
				  	{{#view Jminee.SubjectView titleBinding="title" activeBinding="active"\
				  			includingBinding="including"}}\
				  		{{view.content}}\
				  	{{/view}}\
				  {{/each}}')	
	});
	
	//subject view
	Jminee.subjectListContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span3'],
		childViews: [Jminee.subjectListView]
	});
	
	Jminee.ComposeReviewView = Ember.ContainerView.extend({
		reviewHidden: true,
		changeReviewView: function(){
			if (this.table){
				if (this.reviewHidden){
					this.get('childViews').insertAt(0,this.get('reviewView'));
					this.reviewHidden = false;
				}
			}
			else if (!this.reviewHidden){
				this.get('childViews').removeAt(0,1);
				this.reviewHidden = true;				
			}
		}.observes('table'),
		reviewView: function(){
			return Jminee.SubjectTblContentView.create({tableBinding: this.composeControllerName+".table", message: 'Review'});
		}.property(),
		editView: function(){
			return Jminee.SubjectEditView.create({textSpan: this.textSpan, textControllerBinding: this.composeControllerName+".text"});
		}.property(),
		childViews: ['editView']
	});
	
	Jminee.subjectContentContainer = Ember.ContainerView.create({
		classNames: ['span9'],
		contentView: Ember.View.create({
			template: Ember.Handlebars.compile('{{#each Jminee.subjectContentListController}}\
													{{#if table}}\
														{{view Jminee.SubjectTblContentView tableBinding="table"}}\
													{{else}}\
														{{view Jminee.SubjectContentView}}\
													{{/if}}\
												{{/each}}')
		}),
		commentView: Jminee.ComposeReviewView.create({textSpan: 'span8', composeControllerName: 'Jminee.commentController', tableBinding: 'Jminee.commentController.table' }),
		childViews:['contentView', 'commentView'],
	});
	
	
	/*********************************************	
	/*		topic nav view
	/*********************************************/
	Jminee.TopicNavItemView = Ember.View.extend({
		tagName: 'li',
		layout: Ember.Handlebars.compile('<a href="#">{{yield}}</a><span class="divider">></span>'),
		content: function(){
			var str=this.title;
			return new Handlebars.SafeString(str);
		}.property(),
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  	view.set('active', true);
			  }
		}),
	});
	Jminee.topicNavView = Ember.View.create({
		tagName: 'ul',
		classNames: ['breadcrumb'],
		template: Ember.Handlebars.compile(
				  '{{#each Jminee.topicNavController}}\
					  	{{#view Jminee.TopicNavItemView title=title activeBinding="active"\
								viewList=viewList}}\
							{{view.content}}\
						{{/view}}\
				  {{/each}}'
				)
	});

	Jminee.topicNavContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span8'],
		childViews: [Jminee.topicNavView]
	});
	
	Jminee.composeButtonView = Ember.View.create({
		tagName: 'button',
		classNames: ['toolbox', 'btn', 'btn-small'],
		template: Ember.Handlebars.compile('<img src="/images/icons/edit.png">'),
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  Jminee.composeView.$().modal('show');
			  }
		}),
	});
	
	Jminee.searchBoxView = Ember.View.create({
		tagName: 'form',
		classNames: ['toolbox', 'pull-right'],
		layout: Ember.Handlebars.compile('<input type="text" class="input-large search-query" placeholder="Search...">')		
	});
	
	Jminee.composeButtonContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span4', 'whitesmoke' ],
		childViews: [Jminee.composeButtonView, Jminee.searchBoxView],
	});
	
	Jminee.contentNavContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['row'],
		childViews: [Jminee.topicNavContainer, Jminee.composeButtonContainer]
	});
	
	Jminee.contentNavContainer.appendTo("#main_container");
		
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
	
	Jminee.mainView = Ember.ContainerView.create({
			tagName: 'div',
			classNames: ['row'],
			mainViewsDict:{'topic':[Jminee.topicListContainer], 'subject':[Jminee.subjectListContainer,Jminee.subjectContentContainer]},
			changeChildView: function(){
				while(this.get('childViews').popObject());
				this.get('childViews').pushObjects(this.mainViewsDict[Jminee.topicNavController.mainViewName]); 
			}.observes('Jminee.topicNavController.mainViewName')
	});
	
	Jminee.mainView.appendTo("#main_container");
		
});
