$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	/*********************************************	
	/*		message views
	/*********************************************/
	Jminee.MessageView = Ember.View.extend({
		classNames: ['well  well-small'],
		template: Ember.Handlebars.compile(
				'{{#if creator_name}}<a href="#">{{creator_name}} </a>:{{/if}}\
					{{#if content}}{{content}}{{/if}}'),
	});

	Jminee.TableMessageView = Jminee.MessageView.extend({
		template: Ember.Handlebars.compile(
			'{{#if creator_name}}<a href="#">{{creator_name}} </a>:{{/if}}\
			{{#if view.content}}{{view.content}}{{/if}}\
			{{#if view.table.title}}<h4>{{view.table.title}}</h4>{{/if}}\
			<table class="table table-bordered">\
			<thead><tr>\
			{{#each header in view.table.header}}\
				<td><h5>{{header}}</h5></td>\
			{{/each}}\
			</tr></thead>\
			<tbody>\
			{{#each row in view.table.data}}\
				<tr>\
					{{#each col in row}}\
						<td>{{col}}</td>\
					{{/each}}\
				</tr>\
			{{/each}}\
			</tbody></table>'
		)
	});

	Jminee.MessageInputView = Jminee.MessageView.extend({
		template: Ember.Handlebars.compile(
			'<form class="form-horizontal">\
				{{#with controller}}\
					<div class="control-group">\
			 			<div class="control">\
							{{view Jminee.TextArea spanBinding="view.textSpan" controller=this}}\
						</div>\
				  	</div>\
				  	<div class="control-group">\
			 			<div class="control">\
				  			<button  class="control btn" type="submit" {{action "submit" target="controller"}}>Submit</button>\
				  		</div>\
				  	</div>\
				{{/with}}\
			</form>')
	});
			
	Jminee.MessageReviewView = Ember.ContainerView.extend({
		reviewHidden: true,
		changeReviewView: function(){
			if (this.table){
				if (this.reviewHidden){
					this.get('childViews').insertAt(0,this.get('reviewView'));
					this.reviewHidden = false;
				}
			}
			else if (!this.reviewHidden){
				this.get('childViews').removeAt(0,1);
				this.reviewHidden = true;				
			}
		}.observes('table'),
//		setInfo: function(info){
//			this.inputView.set('controller', info.inputController);
////			this.inputView.set('textSpan', info.inputSpan);
//		},
		reviewView: Jminee.TableMessageView.create(),
//		inputView: Jminee.MessageInputView.create(),
		childViews: ['inputView']
	});
	
	Jminee.AlertView = Ember.View.extend({
		show: function(relatedView, text){
			if (this.isVisible)
				this.removeFromParent();
			this.relatedView=relatedView;		
			this.set('text',text);
			this.parent.get('childViews').pushObject(this);						
		},
		template: Ember.Handlebars.compile(
			'<div type"input" class="alert alert-error">\
				{{view.text}}\
			</div>'
		),		
	});
	
	Jminee.subjectAlertView = Jminee.AlertView.create({});
});
