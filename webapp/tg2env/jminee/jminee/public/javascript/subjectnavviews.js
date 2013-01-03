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
		click: function(event){
		  	if (Jminee.subjectAlertView.isVisible)
		  		Jminee.subjectAlertView.removeFromParent();
		  	this.set('active', true);
		},
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
	
	
	
	Jminee.AddSubjectTitleView = Ember.TextField.extend(Jminee.viewWithAlert, {
//		classNameBindings: ['active'],
		placeholder:"Create a subject...",
		alertView: Jminee.subjectAlertView,
		alertText: 'Subject musts have a title!',
		alertType: 'alert-error'
	});
	
	
	Jminee.subjectNavView = Ember.View.create({
		  tagName: 'ul',
		  classNames: ['nav', 'nav-pills', 'nav-stacked'],
		  template: Ember.Handlebars.compile(
				  '{{#each Jminee.subjectListController}}\
				  		{{#unless addSubject}}\
				  			{{view Jminee.SubjectNavItemView activeBinding="active"}}\
				  		{{else}}\
				  			{{view Jminee.AddSubjectTitleView activeBinding="active"\
				  				valueBinding="title"}}\
				  		{{/unless}}\
				  {{/each}}')				  	
	});
	
	Jminee.subjectNavContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span3'],
		childViews: [Jminee.subjectNavView]
	});
	
	Jminee.subjectAlertView.reopen({parent: Jminee.subjectNavContainer, type: 'alert-error'});
});