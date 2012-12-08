$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
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
											{{/each}}')
	});
	
	Jminee.topicListContainer = Ember.ContainerView.create({
		tagName: 'div',
		classNames: ['span12'],
		childViews: [Jminee.topicListView]
	});
})