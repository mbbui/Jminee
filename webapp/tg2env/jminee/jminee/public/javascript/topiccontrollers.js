$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    
    /*********************************************	
	/*		topic list controller
	/*********************************************/ 
    Jminee.TopicController = Ember.Controller.extend({
    	selected: function(){
    		Jminee.topicNavController.addCrumb(Jminee.TopicItemNavController.create({title: this.title, contentType: 'subject'}));
    	},
    	setInfo: function(topic){
    		this.title = topic.title;
    	}
    }); 

    Jminee.topicListController = Ember.ArrayController.create({
    	reload: function(){
    		$.ajax({
		     	url: '/message/get_topics',
		     	data: {},
    			dataType: 'json',
    			success: function(resp){
    				var topicList=[];
    				if (!resp.success)
    					//TODO: change error message
    					//TODO: create topicAlertView
    					Jminee.topicAlertView.show(null, 'Error code '+resp.error_code);
    				else {
    					//TODO: check if res.topics always an array
    					var topics = resp.topics;
    					for (var i=0; i<topics.length; i++){
    						topicList.push(Jminee.TopicController.create(topics[i]));    						
    					}    					    					    					
    					Jminee.topicListController.set('content', topicList);
    				}	
    				return resp;
    			},
    			error: function(resp){
    				Jminee.loginAlertView.show(Jminee.loginView, 'Error connecting server!');
    			} 
		    });
//    		this.set('content', topicList);    		
    	},
    	afterLogin: function(){
    		if (Jminee.isLogin)
    			this.reload();
    	}.observes('Jminee.isLogin')
    });
    
    /*********************************************	
	/*		topic nav controller
	/*********************************************/ 
    Jminee.topicNavController = Ember.ArrayController.create({
    	contentTypeBinding: 'currentCrumb.contentType',
    	content: [],
    	delCrumbUntil: function(crumb){
    		if (this.currentCrumb){
    			this.currentCrumb.set('active', false);
    		}
    		while(crumb!=this.content[this.content.length-1]){
    			this.content.popObject();
    		}
    		this.set('currentCrumb', this.content[this.content.length-1]);
    	},
    
	    addCrumb: function(crumb){
			if (this.currentCrumb){
				this.currentCrumb.set('active', false);
			}
			this.content.pushObject(crumb);
			this.set('currentCrumb', this.content[this.content.length-1]);
			this.currentCrumb.set('active', true);
		}
    });
    
    Jminee.TopicItemNavController = Ember.Controller.extend({
    	selected: function(){
    		if (this!=this.parent.get('currentCrumb')){
    			this.parent.delCrumbUntil(this);
    		}
    	}.observes('active'),
    	parent: Jminee.topicNavController
    });
    
//    Jminee.topicNavController.set('content',[Jminee.TopicItemNavController.create({title: 'Main', contentType: 'topic'}),
//                                             Jminee.TopicItemNavController.create({title: 'Soccer Tournament', contentType: 'subject'})]);
    Jminee.topicNavController.addCrumb(Jminee.TopicItemNavController.create({title: 'Topics', contentType: 'topic'}));
//    Jminee.topicNavController.addCrumb(Jminee.TopicItemNavController.create({title: 'Soccer Tournament', contentType: 'subject'}));
    
    
});

