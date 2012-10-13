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
    		subject.set('active', true);
    		this.activeSubject=subject;
    	}
    });
    
    Jminee.SubjectContentController = Ember.Controller.extend({
    });

    Jminee.SubjectTblContentController = Ember.Controller.extend({
    });


    Jminee.subjectContentListController = Ember.ArrayController.create();
    Jminee.subjectContentListController.set('content');
    
    var content1=[Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'hello'}),
              Jminee.SubjectContentController.create({sender: 'Giang', createdDate:'01', message: 'bye'}),
              Jminee.SubjectContentController.create({sender: 'Alex', createdDate:'01', message: 'hello'}),
              Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'bye'}),
              Jminee.SubjectTblContentController.create({sender: 'Bach', createdDate:'01', message: 'hello',
           	   table: {title: 'Registration', header: ['#','Name','Will join'], 
           		   		data: [['1','Bach','Y'],['2','Alex','N']]
           	   		}})];
    
    Jminee.subjectListController = Jminee.SubjectListController.create();
    Jminee.subjectListController.set('content',[Jminee.SubjectController.create({title: 'Practice', createdDate:'01', including: Jminee.MSG,
    																			active: true, parent: Jminee.subjectListController,
    																			content: content1}),
                                                Jminee.SubjectController.create({title: 'Goalkeeper gloves', createdDate:'02', including: Jminee.MSG, 
                    															active: false, parent: Jminee.subjectListController}),
                                                Jminee.SubjectController.create({title: 'Registration', createdDate:'02', including: Jminee.MSG|Jminee.TBL, 
                                                								active: false, parent: Jminee.subjectListController}),
                                                Jminee.SubjectController.create({title: 'Expense', createdDate:'02', including: Jminee.MSG, 
                    															active: false, parent: Jminee.subjectListController})]);
    Jminee.subjectListController.setActive(Jminee.subjectListController.get('content')[0]);

});

