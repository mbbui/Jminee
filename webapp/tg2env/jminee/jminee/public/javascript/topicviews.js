$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		topic view
	/*********************************************/	
	Jminee.TopicView = Ember.View.extend({
		tagName: 'li',
		classNames: ['span2'],
		template: Ember.Handlebars.compile(
				'<a href="#" class="thumbnail" {{action "selected" target="controller"}}>\
				<img {{bindAttr src="topicInfo.logourl"}} alt="">\
				<p>{{topicInfo.title}}</p></a>'),
	});
	
	Jminee.topicListContainer = Ember.View.create({
		tagName: 'div',
		classNames: ['span12'],
		template: Ember.Handlebars.compile(
				'<ul class="thumbnails">\
					{{#each Jminee.topicListController}}\
						{{view Jminee.TopicView topicInfo=topicInfo controller=this}}\
					{{/each}}\
				</ul>'
				)
	});
	
});