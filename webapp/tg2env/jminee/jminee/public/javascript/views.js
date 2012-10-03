if (typeof window.Jminee === 'undefined') {
    window.Jminee = Ember.Application.create();
}

SubjectList = Ember.View.extend({
	  templateName: 'subject_list',
	  tagName: 'div',
	  classNames: ['span3'],
	  template: Ember.Handlebars.compile('{{#each subjects}} {{excitedGreeting}}')	  
});

if (typeof Jminee.Views === 'undefined') {
    Jminee.Views = {};
    Jminee.Views.
    
    subject = []
    
    	
    subjectList = Jminee.Views.SubjectList.create({
    	subjects: 
    })
}