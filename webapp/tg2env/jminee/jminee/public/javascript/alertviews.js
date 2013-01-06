$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	Jminee.AlertView = Ember.View.extend({
		classNameBindings: ['alert', 'type', 'pull'],
		alert: true,
		pull: 'pull-left',
		type: 'alert-error',
		
		show: function(relatedView, text, type){
			if (type)
				newType = type;
			if (this.isVisible)
				this.removeFromParent();
			this.relatedView=relatedView;		
			this.set('text',text);			
			this.parent.get('childViews').pushObject(this);						
		},
		template: Ember.Handlebars.compile(
			'{{{view.text}}}'
		),		
		didInsertElement: function(){
			this.set('type', newType);
		}
	});
	
	Jminee.viewWithAlert = Ember.Mixin.create({
		//default validatFunction
		isValid: function(value){
			return !Jminee.empty(value);
		},
		focusOut: function(event){
			if (!this.isValid(this.value)){
				this.alertView.show(this, this.alertText, this.alertType);
			}			
		},
		focusIn: function(event){
			if (this.alertView.isVisible && (this.alertView.relatedView==this
					||this.alertView.relatedView==null)){
				this.alertView.removeFromParent();
			}
		}
	});
	
	Jminee.subjectAlertView = Jminee.AlertView.create();
	Jminee.createTopicAlertView = Jminee.AlertView.create();
	Jminee.loginAlertView = Jminee.AlertView.create();
});
