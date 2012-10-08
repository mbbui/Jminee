if (typeof window.Jminee === 'undefined') {
    window.Jminee = Ember.Application.create();
}

Jminee.SubjectView = Ember.View.extend({
	tagName: 'li',
	layout: Ember.Handlebars.compile('<a href="#">{{yield}}</a>'),
	content: function(){
		var str=this.title;
		if (this.including & Jminee.MSG){
			str+='<i class="icon-comment  pull-right"></i>';
		}
		if (this.including & Jminee.TBL){
			str+='<i class="icon-list-alt  pull-right"></i>';
		}
		return new Handlebars.SafeString(str);
	}.property()
});

Jminee.SubjectListView = Ember.View.extend({
	  tagName: 'div',
	  classNames: ['span3'],
	  layout: Ember.Handlebars.compile('<ul class="nav nav-pills nav-stacked"> {{yield}} </ul>'),
	  template: Ember.Handlebars.compile('{{#each Jminee.subjectListController}}\
			  								{{#view Jminee.SubjectView title=title createdDate=createdDate\
			  											status=status including=including}}\
			  									{{view.content}}\
			  								{{/view}}\
			  								{{/each}}')	  
});

Jminee.SubjectContentView = Ember.View.extend({
	tagName: 'div',
	classNames: ['well  well-small'],
	content: function(){
		if (!this.viewed){
			this.classNames = ['well  well-small'];
		}
		var str='';
		str+='<a href="#">'+this.sender+'</a>: '+this.message;
		if (this.table){
			str+=this.tblView();
		}
		
		return new Handlebars.SafeString(str);
	}.property()
});

Jminee.SubjectTblContentView = Jminee.SubjectContentView.extend({
	tblView: function(){
		var str='<h4>'+this.table.title+'</h4>';
		str+='<table class="table table-bordered">';
		str+='<thead><tr>';
		var header = this.table.header;
		for (i=0; i<header.length; i++){
			str+='<td><h5>'+header[i]+'</h5></td>';			
		}
		str+='</tr></thead>';
		str+='<tbody>';
		var data = this.table.data
		for (i=0; i<data.length; i++){
			str+='<tr>';
			row = data[i];
			for (j=0; j<row.length; j++){
				str+='<td>'+row[j]+'</td>';
			}
			str+='</tr>';
		}
		str+='</tbody></table>';
		return str;
	}
});

Jminee.SubjectEditView = Jminee.SubjectContentView.extend({
	content: function(){
		var str='\
		<form class="form-horizontal">\
	 		<div class="control-group">\
	 			<div class="control">\
	 				<textarea class="span8" rows="3" placeholder="Type your message"></textarea> \
				</div>\
		  	</div>\
		  	<div class="control-group">\
	 			<div class="control">\
		  			<button  class="control" type="submit" class="btn">Submit</button>\
		  		</div>\
		  	</div>\
		</form>'
		return new Handlebars.SafeString(str);
	}.property()
})

Jminee.SubjectContentListView = Ember.View.extend({
	tageName: 'div',
	classNames: ['span9'],
	template: Ember.Handlebars.compile('{{#each Jminee.subjectContentListController}}\
										{{#if table}}\
											{{#view Jminee.SubjectTblContentView sender=sender\
													createdDate=createdDate message=message table=table viewed=viewed}}\
												{{view.content}}\
											{{/view}}\
										{{else}}\
											{{#view Jminee.SubjectContentView sender=sender\
													createdDate=createdDate message=message viewed=viewed}}\
												{{view.content}}\
											{{/view}}\
										{{/if}}\
										{{/each}}\
										{{#view Jminee.SubjectEditView}}\
											{{view.content}}\
										{{/view}}')
});

Jminee.subjectListView = Jminee.SubjectListView.create();
Jminee.subjectListView.appendTo("#topic_view");

Jminee.subjectContentListView = Jminee.SubjectContentListView.create();
Jminee.subjectContentListView.appendTo("#topic_view");


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