$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    
    Jminee.createTopicController = Ember.Controller.create({
    	submit: function(content){
    		$.ajax({
		     	url: '/topic/create_topic',
		     	data: content,
    			dataType: 'json',
    			success: function(resp){
    				if (!resp.success)
    					//TODO: having the right message
    					Jminee.createTopicAlertView.show(null, 'Error code '+resp.error_code);
    				else {
    					//reload topic list
    					Jminee.topicNavController.showTopicContent(resp.topic);    					
    					Jminee.composeView.$().modal('hide');    					
    				}	
    				return resp;
    			},
    			error: function(resp){
    				Jminee.createTopicAlertView.show(null, 'Error connecting server!');
    			} 
		    });    		
    	}    	
    });
        
});

