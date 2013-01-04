$(window).load(function() {
	if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    };
	
    Jminee.FunctionStr = Ember.Object.create({
    	formTypes: {table: {matchStr:'#table', preForm:['#','Members']}},
    	match: function(str){
    		for(type in this.formTypes){
    			if (str.match(this.formTypes[type]['matchStr'])){
    				return type;
    			}
    		}
    		return false;
    	},
    	getHeader: function(type, str){
    		var formType = this.formTypes[type];
    		var tmpStr = str.replace(formType['matchStr']+'(', '');
    		var matchArray = tmpStr.match('[^,)]*(?=[,)]){1}');
    		var fields = formType['preForm'].slice();
    		var matchStr;
    		while (matchArray){
    			 matchStr = matchArray[0];
    			 fields.push(matchStr);
    			 tmpStr = tmpStr.replace(matchStr, '');
    			 if (tmpStr[0]==')'){
    				 return fields;
    			 }
    			 tmpStr = tmpStr.replace(',', '');
    			 matchArray = tmpStr.match('[^,)]*(?=[,)]){1}');
    		}
    		return fields;
    	}
    });
    
    /*********************************************	
	/*		text area controller
	/*********************************************/ 
    Jminee.CreateSubjectController = Ember.Controller.extend({
    	textChanged: function(){
			var str = $.trim(this.text);
			var type = Jminee.FunctionStr.match(str);
			if (type){
//				this.reviewController.set('table', {header: Jminee.FunctionStr.getHeader(type, str)});
				this.set('table', {header: Jminee.FunctionStr.getHeader(type, str)});
			}
			else{
//				this.reviewController.set('table', null);
				this.set('table', null);
			}
		}.observes('text'),
		
		focusIn: function(){
			
		},
		
		submit: function(){
			var data = {topic_id: Jminee.topicInfo.uid};
			if (this.subject.addSubject){
				if (Jminee.empty(this.subject.title)){
					Jminee.subjectAlertView.show(this, 'Subject musts have a title!');
					return;
				}
				data.title=this.subject.title;
				if (!Jminee.empty(this.text)){
					data.content = this.text;
				}
			}
			else {
				if (Jminee.empty(this.text)){
					return;
				}
				data.content = this.text;
				data.subject_id = this.subject.uid;
			}
						
			if (this.subject.addSubject){
				$.ajax({
			     	url: '/topic/create_subject',
			     	data: data,
	    			dataType: 'json',
	    			success: function(resp){
	    				if (!resp.success)
	    					//TODO: change error message
	    					//TODO: create subjectAlertView
	    					Jminee.subjectAlertView.show(null, 'Error code '+resp.error_code);
	    				else {
	    					Jminee.subjectListController.reload();	    					
	    				}
	    				
	    				return resp;
	    			},
	    			error: function(resp){
	    				Jminee.subjectAlertView.show(null, 'Error connecting server!');
	    			} 
			    });
			}
			else{
				$.ajax({
			     	url: '/topic/create_comment',
			     	data: data,
	    			dataType: 'json',
	    			success: function(resp){
	    				if (!resp.success)
	    					//TODO: change error message
	    					//TODO: create subjectAlertView
	    					Jminee.subjectAlertView.show(null, 'Error code '+resp.error_code);
	    				else {
	    					Jminee.commentController.set('text', '');
	    					Jminee.subjectListController.loadComments();
	    				}
	    				
	    				return resp;
	    			},
	    			error: function(resp){
	    				Jminee.subjectAlertView.show(null, 'Error connecting server!');
	    			} 
			    });
			}	
		}
	});
    
    Jminee.commentController = Jminee.CreateSubjectController.create();
    Jminee.composeController = Jminee.CreateSubjectController.create();
  
    
});