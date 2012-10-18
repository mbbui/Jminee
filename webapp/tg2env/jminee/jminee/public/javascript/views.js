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
		content: function(){
			if (!this.viewed){
				this.classNames = ['well  well-small'];
			}
			var str='';
			str+='<a href="#">'+this.sender+'</a>: '+this.message;
			if (this.table){
				str+=this.tblView();
			}
			
			return new Handlebars.SafeString(str);
		}.property()
	});

	Jminee.SubjectTblContentView = Jminee.SubjectContentView.extend({
		tblView: function(){
			var str='<h4>'+this.table.title+'</h4>';
			str+='<table class="table table-bordered">';
			str+='<thead><tr>';
			var header = this.table.header;
			for (i=0; i<header.length; i++){
				str+='<td><h5>'+header[i]+'</h5></td>';			
			}
			str+='</tr></thead>';
			str+='<tbody>';
			var data = this.table.data
			for (i=0; i<data.length; i++){
				str+='<tr>';
				row = data[i];
				for (j=0; j<row.length; j++){
					str+='<td>'+row[j]+'</td>';
				}
				str+='</tr>';
			}
			str+='</tbody></table>';
			return str;
		}
	});

	Jminee.SubjectEditView = Jminee.SubjectContentView.extend({
		content: function(){
			var str='\
			<form class="form-horizontal">\
		 		<div class="control-group">\
		 			<div class="control">\
		 				<textarea class="span8" rows="3" placeholder="Type your message"></textarea> \
					</div>\
			  	</div>\
			  	<div class="control-group">\
		 			<div class="control">\
			  			<button  class="control" type="submit" class="btn">Submit</button>\
			  		</div>\
			  	</div>\
			</form>'
			return new Handlebars.SafeString(str);
		}.property()
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
	
	Jminee.subjectContentListView = Ember.View.create({
		tagName: 'div',
		classNames: ['span9'],
		template: Ember.Handlebars.compile('{{#each Jminee.subjectContentListController}}\
											{{#if table}}\
												{{#view Jminee.SubjectTblContentView sender=sender\
														createdDate=createdDate message=message table=table viewed=viewed}}\
													{{view.content}}\
												{{/view}}\
											{{else}}\
												{{#view Jminee.SubjectContentView sender=sender\
														createdDate=createdDate message=message viewed=viewed}}\
													{{view.content}}\
												{{/view}}\
											{{/if}}\
											{{/each}}\
											{{#view Jminee.SubjectEditView}}\
												{{view.content}}\
											{{/view}}')
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
		template: Ember.Handlebars.compile('<img src="/images/icons/edit.png" alt="">')
	});
	
	Jminee.searchBoxView = Ember.View.create({
		tagName: 'form',
		classNames: ['toolbox', 'pull-right'],
		layout: Ember.Handlebars.compile('<input type="text" class="input-large search-query" placeholder="Search...">')		
	});
	
	Jminee.composeButtonContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span4', 'whitesmoke' ],
		childViews: [Jminee.composeButtonView, Jminee.searchBoxView]	
	});
	
	Jminee.contentNavContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['row'],
		childViews: [Jminee.topicNavContainer, Jminee.composeButtonContainer]
	});
	
	Jminee.contentNavContainer.appendTo("#main_container");
	
	/*********************************************	
	/*		edit view
	/*********************************************/	
	Jminee.editView = Ember.View.create({
		tagName: 'div',
		classNames: ['modal', 'hide', 'fade'],
		layout:  Ember.Handlebars.compile('<div class="modal-header">\
						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
						<h3>Modal header</h3>\
					</div>\
					<div class="modal-body">\
						<p>One fine body…</p>\
					</div>\
					<div class="modal-footer">\
						<a href="#" class="btn">Close</a>\
						<a href="#" class="btn btn-primary">Save changes</a>\
					</div>') 
	});
	
	 
	
	
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
	
})