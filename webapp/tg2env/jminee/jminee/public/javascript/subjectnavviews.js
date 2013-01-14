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
		alertType: 'alert-error',
		focusIn: function(){
			this.set('active',true);
			this._super();
		}
	});
	
	
	Jminee.subjectNavView = Ember.View.create({
		  tagName: 'ul',
		  classNames: ['nav', 'nav-pills', 'nav-stacked'],
		  template: Ember.Handlebars.compile(
				  '{{#each Jminee.subjectListController}}\
				  		{{#if addSubject}}\
				  			{{view Jminee.AddSubjectTitleView activeBinding="active"\
	  							valueBinding="title"}}\
				  		{{else}}\
				  			{{view Jminee.SubjectNavItemView activeBinding="active"}}\
				  		{{/if}}\
				  {{/each}}')				  	
	});
	
	Jminee.subjectNavContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span3'],
		childViews: [Jminee.subjectNavView],
		
		isVisible: function(){
			return (Jminee.topicNavController.contentType=='subject');
		}.property('Jminee.topicNavController.contentType'),
		
		didInsertElement: function(){
			this.get('childViews').removeObject(Jminee.subjectAlertView);
		}
	});
	
	Jminee.subjectAlertView.reopen({parent: Jminee.subjectNavContainer});
});