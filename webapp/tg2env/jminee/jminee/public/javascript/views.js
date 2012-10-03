if (typeof window.Jminee === 'undefined') {
    window.Jminee = Ember.Application.create();
}

Jminee.SubjectView = Ember.View.extend({
	templateName: 'subject_item',
	tagName: 'li',
	title: 'blah',
	date: 'goog',
	template: Ember.Handlebars.compile('{{title}} {{date}}')	
});

Jminee.SubjectList = Ember.View.extend({
	  tagName: 'div',
	  classNames: ['span3'],
	  layout: Ember.Handlebars.compile('<ul class="nav nav-pills nav-stacked"> {{yield}} </ul>'),
	  template: Ember.Handlebars.compile('{{#each subjects}}\
			  								{{#view Jminee.SubjectView}} {{view.title}} {{viwe.date}} {{/view}}\
			  							  {{/each}}')	  
});

var subjects = [];
subjects.push(Jminee.SubjectView.create({title: 'blah1', date:'01'}));
subjects.push(Jminee.SubjectView.create({title: 'blah2', date:'02'}));

var subjectList = Jminee.SubjectList.create({subjects: subjects});

subjectList.appendTo("#subject_list");

//if (typeof Jminee.Views === 'undefined') {
//    Jminee.Views = {};
//    Jminee.Views.
//    
//    subject = []
//    
//    	
//    subjectList = Jminee.Views.SubjectList.create({
//    	subjects: 
//    })
//}