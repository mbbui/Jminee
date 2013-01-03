$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	Jminee.AlertView = Ember.View.extend({
		classNameBindings: ['alert', 'type', 'pull'],
		alert: true,
		pull: 'pull-left',
		show: function(relatedView, text, type){
			if (type)
				this.set('type', type);
			if (this.isVisible)
				this.removeFromParent();
			this.relatedView=relatedView;		
			this.set('text',text);			
			this.parent.get('childViews').pushObject(this);						
		},
		template: Ember.Handlebars.compile(
			'{{view.text}}'
		),		
	});
	
	Jminee.viewWithAlert = Ember.Mixin.create({
		focusOut: function(event){
			if (this.value.match(/^\s*$/)){
				this.alertView.show(this, this.alertText, this.alertType);
			}
		},
		focusIn: function(event){
			if (this.alertView.isVisible && this.alertView.relatedView==this){
				this.alertView.removeFromParent();
			}
			this.set('active', true);
		}
	});
	
	Jminee.subjectAlertView = Jminee.AlertView.create();
	Jminee.createTopicAlertView = Jminee.AlertView.create();
});
