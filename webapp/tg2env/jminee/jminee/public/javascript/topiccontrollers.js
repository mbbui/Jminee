$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    
    /*********************************************	
	/*		topic list controller
	/*********************************************/ 
    Jminee.TopicItemController = Ember.Controller.extend({
    	selected: function(){
    		Jminee.topicInfo.reopen(this.topicInfo);
    		Jminee.topicNavController.pushCrumb(Jminee.TopicItemNavController.create(
    				{title: this.topicInfo.title, contentType: 'subject',
    					contentController: Jminee.subjectListController}));
    	},
    }); 

    Jminee.topicListController = Ember.ArrayController.create({
    	reload: function(){
    		$.ajax({
		     	url: '/topic/get_topics',
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
    						topicList.push(Jminee.TopicItemController.create({topicInfo: topics[i]}));    						
    					}    					    					    					
    					Jminee.topicListController.set('content', topicList);
    				}	
    				return resp;
    			},
    			error: function(resp){
    				Jminee.topicAlertView.show(null, 'Error connecting server!');
    			} 
		    });    		
    	},
//    	afterLogin: function(){
//    		if (Jminee.isLogin){
//    			this.reload();
//    			Jminee.topicNavController.pushCrumb(Jminee.TopicItemNavController.create(
//    		    		{title: 'Topics', contentType: 'topic', contentController: Jminee.topicListController}));
//    		}
//    			
//    	}.observes('Jminee.isLogin')
    });
        
});

