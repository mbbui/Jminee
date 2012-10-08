Jminee.MSG = 0x01;
Jminee.TBL = 0x02;

//$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
//});

Jminee.SubjectController = Ember.Controller.extend({
});

Jminee.SubjectContentController = Ember.Controller.extend({
});

Jminee.SubjectTblContentController = Ember.Controller.extend({
});

Jminee.subjectListController = Ember.ArrayController.create();
Jminee.subjectListController.set('content',[Jminee.SubjectController.create({title: 'Practice', createdDate:'01', status: 'active', including: Jminee.MSG}),
                                            Jminee.SubjectController.create({title: 'Goalkeeper gloves', createdDate:'02', including: Jminee.MSG}),
                                            Jminee.SubjectController.create({title: 'Registration', createdDate:'02', including: Jminee.MSG|Jminee.TBL}),
                                            Jminee.SubjectController.create({title: 'Expense', createdDate:'02', including: Jminee.MSG})]);

Jminee.subjectContentListController = Ember.ArrayController.create();
Jminee.subjectContentListController.set('content',[Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'hello'}),
                                                   Jminee.SubjectContentController.create({sender: 'Giang', createdDate:'01', message: 'bye'}),
                                                   Jminee.SubjectContentController.create({sender: 'Alex', createdDate:'01', message: 'hello'}),
                                                   Jminee.SubjectContentController.create({sender: 'Bach', createdDate:'01', message: 'bye'}),
                                                   Jminee.SubjectTblContentController.create({sender: 'Bach', createdDate:'01', message: 'hello',
                                                	   table: {title: 'Registration', header: ['#','Name','Will join'], 
                                                		   		data: [['1','Bach','Y'],['2','Alex','N']]
                                                	   		}})]);
