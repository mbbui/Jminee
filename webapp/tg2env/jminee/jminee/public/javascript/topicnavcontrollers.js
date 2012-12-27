$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    

    /*********************************************	
	/*		topic nav controller
	/*********************************************/ 
    Jminee.topicNavController = Ember.ArrayController.create({
    	contentTypeBinding: 'topCrumb.contentType',
    	content: [],
    	delCrumbUntil: function(crumb){
    		this.topCrumb.set('active', false);
    		while(crumb!=this.content[this.content.length-1]){
    			this.content.popObject();
    		}
    		this.set('topCrumb', this.content[this.content.length-1]);    		
    		this.topCrumb.set('active', true);
    		this.topCrumb.contentController.reload();
    	},
    
	    pushCrumb: function(crumb){
			if (this.topCrumb){
				this.topCrumb.set('active', false);
			}
			this.content.pushObject(crumb);
			this.set('topCrumb', this.content[this.content.length-1]);
			this.topCrumb.set('active', true);
			this.topCrumb.contentController.reload();
		}
    });
    
    Jminee.TopicItemNavController = Ember.Controller.extend({
    	selected: function(){
    		if (this!=this.parent.topCrumb){
    			this.parent.delCrumbUntil(this);
    		}
    	}.observes('active'),
    	parent: Jminee.topicNavController
    });
    
    Jminee.topicNavController.pushCrumb(Jminee.TopicItemNavController.create(
    		{title: 'Topics', contentType: 'topic', contentController: Jminee.topicListController}));
    
});

