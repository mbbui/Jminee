$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		subject nav view
	/*********************************************/
	Jminee.SubjectNavItemView = Ember.View.extend({
		tagName: 'li',
		layout: Ember.Handlebars.compile('<a href="#">{{yield}}</a>'),
		classNameBindings: ['active'],
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  	view.set('active', true);
			  }
		}),
		template: Ember.Handlebars.compile(
			'{{title}}\
				{{#if withMsg}}\
					<i class="icon-comment  pull-right"></i>\
				{{/if}}\
				{{#if withTbl}}\
					<i class="icon-list-alt  pull-right"></i>\
				{{/if}}'
		)
	});

	Jminee.subjectNavView = Ember.View.create({
		  tagName: 'ul',
		  classNames: ['nav', 'nav-pills', 'nav-stacked'],
		  template: Ember.Handlebars.compile(
				  '{{#each Jminee.subjectListController}}\
				  	{{view Jminee.SubjectNavItemView activeBinding="active"}}\
				  {{/each}}')	
	});
	
	Jminee.subjectNavContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span3'],
		childViews: [Jminee.subjectNavView]
	});
})