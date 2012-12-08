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
				'{{#if sender}}<a href="#">{{sender}} </a>:{{/if}}\
					{{#if message}}{{message}}{{/if}}'),
	});

	Jminee.TableMessageView = Jminee.MessageView.extend({
		template: Ember.Handlebars.compile(
			'{{#if sender}}<a href="#">{{sender}} </a>:{{/if}}\
			{{#if view.message}}{{view.message}}{{/if}}\
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
		 		<div class="control-group">\
		 			<div class="control">\
						{{view Jminee.TextArea spanBinding="view.textSpan" valueBinding="view.textController"}}\
					</div>\
			  	</div>\
			  	<div class="control-group">\
		 			<div class="control">\
			  			<button  class="control" type="submit" class="btn">Submit</button>\
			  		</div>\
			  	</div>\
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
		reviewView: function(){
			return Jminee.TableMessageView.create({tableBinding: this.composeControllerName+".table", message: 'Review'});
		}.property(),
		editView: function(){
			return Jminee.MessageInputView.create({textSpan: this.textSpan, textControllerBinding: this.composeControllerName+".text"});
		}.property(),
		childViews: ['editView']
	});
	
});
