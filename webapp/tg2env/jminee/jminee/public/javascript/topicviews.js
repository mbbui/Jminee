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
		eventManager: Ember.Object.create({
			  click: function(event, view){
				  	view.get('controller').selected();
			  }
		}),
		template: Ember.Handlebars.compile(
				'<a href="#" class="thumbnail">\
				<img src="http://placehold.it/160x120" alt="">\
				<p>{{title}}</p></a>'),
	});
	
	Jminee.topicListContainer = Ember.View.create({
		tagName: 'div',
		classNames: ['span12'],
		template: Ember.Handlebars.compile(
				'<ul class="thumbnails">\
					{{#each Jminee.topicListController}}\
						{{view Jminee.TopicView title=title controller=this}}\
					{{/each}}\
				</ul>'
				)
	});
	
});