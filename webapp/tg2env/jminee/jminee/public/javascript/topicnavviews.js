$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
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
})