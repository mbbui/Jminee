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
    		crumb.contentController.reload();
    		while(crumb!=this.content[this.content.length-1]){
    			this.content.popObject();
    		}
    		this.set('topCrumb', this.content[this.content.length-1]);    		
    	},
    
	    pushCrumb: function(crumb){
	    	crumb.contentController.reload();
			this.content.pushObject(crumb);
			this.set('topCrumb', this.content[this.content.length-1]);
		},
    	
    	showTopicContent: function(topicInfo){
    		while (this.content.length>1)
    			this.content.popObject();
    		
    		Jminee.topicInfo.reopen(topicInfo);
    		this.pushCrumb(Jminee.TopicItemNavController.create(
    				{title: topicInfo.title, contentType: 'subject',
    					contentController: Jminee.subjectListController}));
    	}
    });
    
    Jminee.TopicItemNavController = Ember.Controller.extend({
    	selected: function(){
    		if (this!=this.parent.topCrumb){
    			this.parent.delCrumbUntil(this);
    		}
    	},
    	parent: Jminee.topicNavController
    });
    
    
    
});

