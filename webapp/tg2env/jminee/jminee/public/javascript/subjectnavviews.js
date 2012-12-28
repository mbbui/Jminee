$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		subject nav view
	/*********************************************/
	Jminee.SubjectNavItemView = Ember.View.extend({
		tagName: 'li',
		classNameBindings: ['active'],
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  	view.set('active', true);
				  	if (Jminee.subjectAlertView.isVisible)
				  		Jminee.subjectAlertView.removeFromParent();
			  }
		}),
		template: Ember.Handlebars.compile(
			'<a href="#">{{title}}\
			{{#if withMsg}}\
				<i class="icon-comment  pull-right"></i>\
			{{/if}}\
			{{#if withTbl}}\
				<i class="icon-list-alt  pull-right"></i>\
			{{/if}}</a>'
		)
	});
	
	Jminee.AddSubjectTitleView = Ember.TextField.extend({
		classNameBindings: ['active'],
		placeholder:"Create a subject...",
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  	view.set('active', true);
				  	if (Jminee.subjectAlertView.isVisible)
				  		Jminee.subjectAlertView.removeFromParent();
			  }
		})
	});
	
	
	Jminee.subjectNavView = Ember.View.create({
		  tagName: 'ul',
		  classNames: ['nav', 'nav-pills', 'nav-stacked'],
		  template: Ember.Handlebars.compile(
				  '{{#each Jminee.subjectListController}}\
				  		{{#unless newSubject}}\
				  			{{view Jminee.SubjectNavItemView activeBinding="active"}}\
				  		{{else}}\
				  			{{view Jminee.AddSubjectTitleView activeBinding="active" valueBinding="title"}}\
				  		{{/unless}}\
				  {{/each}}')				  	
	});
	
	Jminee.subjectNavContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span3'],
		childViews: [Jminee.subjectNavView]
	});
});