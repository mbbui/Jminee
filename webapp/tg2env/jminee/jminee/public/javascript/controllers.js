$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    
    Jminee.MSG = 0x01;
    Jminee.TBL = 0x02;
    
    Jminee.SubjectController = Ember.Controller.extend({
    	selected: function(){
    		if (this!=this.parent.get('activeSubject')){
    			this.parent.setActive(this);
    		}
    	}.observes('active')
    });

    Jminee.SubjectListController = Ember.ArrayController.extend({
    	setActive: function(subject){
    		if (this.activeSubject){
    			this.activeSubject.set('active', false);
    		}
//    		subject.set('active', true);
    		this.set('activeSubject', subject);
    		Jminee.subjectContentListController.set('content', subject.get('content'));
    	},
    	activeSubject: null
    });
    
    Jminee.SubjectContentController = Ember.Controller.extend({
    });

    Jminee.SubjectTblContentController = Ember.Controller.extend({
    });
      
    var content1=[Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'hello'}),
              Jminee.SubjectContentController.create({sender: 'Giang', createdDate:'01', message: 'bye'}),
              Jminee.SubjectContentController.create({sender: 'Alex', createdDate:'01', message: 'hello'}),
              Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'bye'}),
              Jminee.SubjectTblContentController.create({sender: 'Bach', createdDate:'01', message: 'hello',
           	   table: {title: 'Registration', header: ['#','Name','Will join'], data: [['1','Bach','Y'],['2','Alex','N']]
           	   		}})];
    
    var content3=[Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'12/01/02', message: 'Please register for this tournament'}),
                  Jminee.SubjectTblContentController.create({sender: 'Bach', createdDate:'01', message: '',
                	  table: {title: 'Registration', header: ['#','Name','Will join'], data: [['1','Bach','Y'],['2','Alex','N']]}
                  })];
    
    Jminee.subjectListController = Jminee.SubjectListController.create();
    Jminee.subjectListController.set('content',[Jminee.SubjectController.create({title: 'Practice', createdDate:'01', including: Jminee.MSG,
    																			active: true, parent: Jminee.subjectListController, content: content1}),
                                                Jminee.SubjectController.create({title: 'Goalkeeper gloves', createdDate:'02', including: Jminee.MSG, 
                    															active: false, parent: Jminee.subjectListController}),
                                                Jminee.SubjectController.create({title: 'Registration', createdDate:'02', including: Jminee.MSG|Jminee.TBL, 
                                                								active: false, parent: Jminee.subjectListController, content: content3}),
                                                Jminee.SubjectController.create({title: 'Expense', createdDate:'02', including: Jminee.MSG, 
                    															active: false, parent: Jminee.subjectListController})]);
    
    Jminee.subjectContentListController = Ember.ArrayController.create();
    
    Jminee.subjectListController.setActive(Jminee.subjectListController.get('content')[0]);
    
    /*********************************************	
	/*		topic list controller
	/*********************************************/ 
    Jminee.TopicController = Ember.Controller.extend({
    	selected: function(){
    		Jminee.topicNavController.addCrumb(Jminee.TopicItemNavController.create({title: this.title, mainViewName: 'subject'}));
    	}
    }); 
    Jminee.topicListController = Ember.ArrayController.create({content:[Jminee.TopicController.create({title: 'Soccer Tournament'}),
                                                                        Jminee.TopicController.create({title: 'CS431'}),
                                                                        Jminee.TopicController.create({title: 'Drafts'})]});
    
    /*********************************************	
	/*		topic nav controller
	/*********************************************/ 
    Jminee.topicNavController = Ember.ArrayController.create({
    	mainViewNameBinding: 'currentCrumb.mainViewName',
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
    
//    Jminee.topicNavController.set('content',[Jminee.TopicItemNavController.create({title: 'Main', mainViewName: 'topic'}),
//                                             Jminee.TopicItemNavController.create({title: 'Soccer Tournament', mainViewName: 'subject'})]);
    Jminee.topicNavController.addCrumb(Jminee.TopicItemNavController.create({title: 'Main', mainViewName: 'topic'}));
//    Jminee.topicNavController.addCrumb(Jminee.TopicItemNavController.create({title: 'Soccer Tournament', mainViewName: 'subject'}));
    
    
});

