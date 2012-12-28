$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    
    Jminee.MSG = 0x01;
    Jminee.TBL = 0x02;
    
    Jminee.SubjectItemController = Ember.Controller.extend({
    	selected: function(){
    		if (this.get('active')==true){
    			this.parent.setActive(this);
    		}
    	}.observes('active')
    });
    
    Jminee.subjectListController = Ember.ArrayController.create({
    	content: [],
    	
    	initContentInfo: function(){
    		Jminee.subjectContentListController.set('content', []);
    		Jminee.commentController.set('text', '');
			Jminee.commentController.set('subject', this.activeSubject);
    	},
    	
    	setActive: function(subject){
    		if (this.activeSubject && this.activeSubject!=subject){
    			this.activeSubject.set('active', false);
    		}
    		this.set('activeSubject', subject);
    		this.initContentInfo();
			//if subject is creating it has no comment to be loaded
    		this.loadComments();  
    	},
    	
    	//load comments for a subject
    	//comments is loaded from the server
    	loadComments: function(){
    		var subject=this.activeSubject;
    		if (!subject.newSubject)
	    		$.ajax({
			     	url: '/topic/get_comments',
			     	data: {topic_id: Jminee.topicInfo.uid, subject_id: subject.uid},
	    			dataType: 'json',
	    			success: function(resp){
	    				var commentList=[];
	    				if (!resp.success)
	    					//TODO: change error message
	    					//TODO: create subjectAlertView
	    					Jminee.subjectAlertView.show(null, 'Error code '+resp.error_code);
	    				else {
	    					//TODO: check if res.topics always an array
	    					var comments = resp.comments;    					
	    					for (var i=0; i<comments.length; i++){
	    						commentList.push(Jminee.SubjectContentController.create(comments[i]));    						
	    					}    			
//	    					var item=Jminee.SubjectContentController.create({input: true, subject: subject});
//	    					commentList.push(item);
	    					Jminee.subjectContentListController.set('content', commentList);
//	    					Jminee.reviewView.reopen({subject: subject});
	    				}	
	    				return resp;
	    			},
	    			error: function(resp){
	    				Jminee.subjectAlertView.show(null, 'Error connecting server!');
	    			} 
			    });       		
    		else{
//    			var item = Jminee.SubjectContentController.create({input: true, subject: subject});
//    	    	Jminee.subjectContentListController.set('content', [item]);
//    			Jminee.reviewView.reopen({subject: subject});
    		}    		
    	},
    	//reload the subject list
    	reload: function(){
    		$.ajax({
		     	url: '/topic/get_subjects',
		     	data: {topic_id: Jminee.topicInfo.uid},
    			dataType: 'json',
    			success: function(resp){
    				var subjectList=[];
    				Jminee.subjectAlertView.reopen({parent: Jminee.subjectNavContainer});
    				if (!resp.success)
    					//TODO: change error message
    					//TODO: create subjectAlertView
    					Jminee.subjectAlertView.show(null, 'Error code '+resp.error_code);
    				else {
    					//TODO: check if res.topics always an array
    					var subjects = resp.subjects;
    					var item;
    					//add creating subject title controller
    					item = Jminee.SubjectItemController.create({parent: Jminee.subjectListController, newSubject: true});
						subjectList.push(item);
    					
						for (var i=0; i<subjects.length; i++){
    						item=Jminee.SubjectItemController.create(subjects[i]);
    						item.set('parent', Jminee.subjectListController);
    						subjectList.push(item);       						
    					}
    					       					
						
    					Jminee.subjectListController.set('content', subjectList);
    					if (subjects.length>0)
    						subjectList[1].set('active',true);
    					else
    						subjectList[0].set('active',true);
    					//reset content to empty to remove old content
    					//Jminee.subjectContentListController.set('content', []);
    					
    				}	
    				return resp;
    			},
    			error: function(resp){
    				Jminee.subjectAlertView.show(null, 'Error connecting server!');
    			} 
		    });
    	},
    	activeSubject: null
    });
    
    Jminee.SubjectContentController = Ember.Controller.extend({
    });

    Jminee.SubjectTblContentController = Ember.Controller.extend({
    });
//      
//    var content1=[Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'hello'}),
//              Jminee.SubjectContentController.create({sender: 'Giang', createdDate:'01', message: 'bye'}),
//              Jminee.SubjectContentController.create({sender: 'Alex', createdDate:'01', message: 'hello'}),
//              Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'bye'}),
//              Jminee.SubjectTblContentController.create({sender: 'Bach', createdDate:'01', message: 'hello',
//           	   table: {title: 'Registration', header: ['#','Name','Will join'], data: [['1','Bach','Y'],['2','Alex','N']]
//           	   		}})];
//    
//    var content3=[Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'12/01/02', message: 'Please register for this tournament'}),
//                  Jminee.SubjectTblContentController.create({sender: 'Bach', createdDate:'01', message: '',
//                	  table: {title: 'Registration', header: ['#','Name','Will join'], data: [['1','Bach','Y'],['2','Alex','N']]}
//                  })];
    
//    Jminee.subjectListController = Jminee.SubjectController.create();
//    Jminee.subjectListController.set('content',[Jminee.SubjectItemController.create({title: 'Practice', createdDate:'01', withMsg:true,
//    																			active: true, parent: Jminee.subjectListController, content: content1}),
//                                                Jminee.SubjectItemController.create({title: 'Goalkeeper gloves', createdDate:'02', withMsg:true, 
//                    															active: false, parent: Jminee.subjectListController}),
//                                                Jminee.SubjectItemController.create({title: 'Registration', createdDate:'02', withMsg:true, withTbl:true, 
//                                                								active: false, parent: Jminee.subjectListController, content: content3}),
//                                                Jminee.SubjectItemController.create({title: 'Expense', createdDate:'02', withMsg:true, 
//                    															active: false, parent: Jminee.subjectListController})]);
    
    Jminee.subjectContentListController = Ember.ArrayController.create();
    
    
        
});

