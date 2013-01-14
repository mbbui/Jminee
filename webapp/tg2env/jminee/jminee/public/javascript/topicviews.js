window.closeOnOutClick = [];

$(window).click(function() {
	if (window.activeTopicTool && !window.disable){
		window.activeTopicTool.close();
		window.activeTopicTool=null;
	}	
});

$(window).load(function() { 
	if (typeof window.Jminee === 'undefined') {
	    window.Jminee = Ember.Application.create();
	}
	
	Jminee.waitingView = Ember.View.create({
		classNames: ['waiting']
	});
	
	Jminee.globalDisable = function(){
		window.disable = true;
		Jminee.waitingView.appendTo("body");
	};
	Jminee.globalEnable = function(){
		window.disable = false;
		Jminee.waitingView.removeFromParent();
	};
	/*********************************************	
	/*		topic view
	/*********************************************/	
	Jminee.ToolboxButton = Ember.View.extend({
		tagName: 'li',
		active: false,
		layout: Ember.Handlebars.compile(
			'<a class="toolbox_icon thumbnail" href="#">{{yield}}</a>'
		),
		click: function(event){
			if (this.get('active'))
				event.stopPropagation();
			else 
				this.get('parentView').clickedTool=this;
		},		
		close: function(){
			this.set('active', false);
			this.set('isVisible', false);
		},				
	});
	
	Jminee.TopicToolMenu = Ember.View.extend({
		tagName: 'li',
		classNameBindings: ['inputcss', 'textcss'],
		inputcss: false,
		textcss: true,
		alert: false,
		
		changeTextClass: function(){ 
			this.set('textcss', !this.inputcss); 
		}.observes('inputcss'),
		
		click: function(){
			if(!this.get('inputcss')){
//				this.controller.reload();
				this.set('inputcss', true);				
			}
		},	
		
		keyUp: function(event){
			if (event.keyCode==Jminee.ENTERKEY){
				this.get("controller").submit(this.inputView);
				this.get("inputView").setState('submit');									
			} 
			else if (event.keyCode==Jminee.ESCAPEKEY){
				this.set('inputcss', false);
				this.get('inputView').set('value','');
				this.set('alert', false);
			}
		},
		
		InputView: Ember.TextField.extend({
			isVisibleBinding: 'parentView.inputcss',
			viewState: null,
			
			focusOut: function(){
				if (this.viewState!='submit')
					this.set('isVisible', false);	
				this.get('parentView').set('alert', false);
			},
			becameVisible: function(){
				this.set('placeholder', this.get("defaultPlaceholder"));
				this.$().focus();
			},			
			setState: function(state){
				this.viewState = state;
				if (state=='submit'){
					this.tmpValue = this.value;
					this.set('value', '');
					this.set('placeholder', 'Submitting...');
					Jminee.globalDisable();
				}
				else if (state=='fail'){
					this.set('value', this.tmpValue);
					this.set('placeholder', this.get("defaultPlaceholder"));
					Jminee.globalEnable();
				}
				else if (state=='success'){
					this.set('placeholder', "Done!");
					window.timeoutElement = this;
//					this.set('isVisible', false);
//					this.set('placeholder', this.get("defaultPlaceholder"));
					Jminee.globalEnable();
					setTimeout(function(){
						window.timeoutElement.set('isVisible', false);
					},1000);
				}
			},
			submitDone: function(resp){
				if (resp.success)
					this.setState('success');
				else{
					this.setState('fail');
					this.get('parentView').set('alert', true);
				}					
			},
			keyPress: function(){
				this.get('parentView').set('alert', false);
			},
			click : function(){
				this.get('parentView').set('alert', false);
			}
		}),
		template: Ember.Handlebars.compile(
				'{{#if view.changemember}}\
					{{view view.InputView viewName="inputView" placeholder="Member emails..."\
						defaultPlaceholder="Member emails..."\
						valueBinding="Jminee.changeMemberController.value"\
						}}\
					{{#view Ember.View viewName="textView"\
						isVisibleBinding="view.textcss"\
						textBinding="view.text"}}\
						Change members\
					{{/view}}\
				{{/if}}\
				{{#if view.changelogo}}\
					{{view view.InputView viewName="inputView"  placeholder="Logo URL..."\
						defaultPlaceholder="Logo URL..."\
						valueBinding="Jminee.changeLogoController.value"}}\
					{{#view Ember.View viewName="textView"\
						isVisibleBinding="view.textcss"\
						textBinding="view.text"}}\
						Change logo\
					{{/view}}\
				{{/if}}\
				{{#view viewName="alertView" isVisibleBinding="view.alert"}}\
					<div class="alert alert-error">Error connecting to the server</div>\
				{{/view}}'
		),
	});
	
	Jminee.QvPopover = Ember.View.extend({
		classNames: ['popover', 'right', 'qv-popover'],
		template: Ember.Handlebars.compile(
				'<div class="arrow"></div>\
				<h3 class="popover-title">Quickview</h3>\
				<div class="popover-content"><p>Subject: comments</p></div>')
	});
	
	Jminee.ConfigPopover = Ember.View.extend({
		classNames: ['config-popover', 'popover', 'bottom'],
		text: "Change",
		template: Ember.Handlebars.compile(
				'<div class="arrow"></div>\
				<div class="popover-content">\
					<ul class="popover-nav">\
				  		{{view Jminee.TopicToolMenu changemember=true controllerBinding="Jminee.changeMemberController"}}\
						{{view Jminee.TopicToolMenu changelogo=true controllerBinding="Jminee.changeLogoController"}}\
				  	</ul>\
				</div>')
	});
	
	Jminee.TopicToolView = Ember.View.extend({
		tagName: 'ul',
		classNames: ['topic_toolbox', 'thumbnails'],
		isVisible: false,
		
		template: Ember.Handlebars.compile('\
				{{#view Jminee.ToolboxButton viewName="config"\
					class="config_thumbnail"\
					isVisibleBinding="view.isVisible"\
					}}\
					<img src="images/icons/config.png" alt="">\
					{{view Jminee.ConfigPopover viewName="configPopover"\
					isVisibleBinding="view.active"}}\
				{{/view}}\
				{{#view Jminee.ToolboxButton viewName="quickview"\
					class="quickview_thumbnail"\
					isVisibleBinding="view.isVisible"\
					}}\
					<img src="images/icons/quickview.png" alt="">\
					{{view Jminee.QvPopover viewName="quickviewPopover"\
					isVisibleBinding="view.active"}}\
				{{/view}}\
				'),
		click: function(event){
			event.stopPropagation();
			if (this.activeTool){
				this.get('activeTool').set('active',false);
			}
			this.clickedTool.set('active',true);
			this.activeTool = this.clickedTool;
			this.clickedTool = null;
			if (window.activeTopicTool && window.activeTopicTool!=this){
				window.activeTopicTool.close();				
			}						
			window.activeTopicTool=this;
		},
		close: function(){
			this.activeTool.close();
			this.activeTool = null;
		},
		show: function(){
			if (!window.activeTopicTool)
				this.set('isVisible', true);
		},
		hide: function(){
			if (!this.config.get('active')&&!this.quickview.get('active'))
				this.set('isVisible', false);
		}		
	});
	
	Jminee.TopicView = Ember.View.extend({
		tagName: 'li',
		classNames: ['span2', 'topic_box'],
		showTool: false,
		template: Ember.Handlebars.compile(
				'<a href="#" class="thumbnail" {{action "selected" target="controller"}}>\
				<img class="topic_img" {{bindAttr src="topicInfo.logourl"}} alt="">\
				<p class="topic_title">{{topicInfo.title}}</p></a>\
				{{view Jminee.TopicToolView viewName="toolView"}}\
				'),
		mouseEnter: function(){
			this.toolView.show();
		},
		mouseLeave: function(){
			this.toolView.hide();
		}
	});
	
	Jminee.topicListContainer = Ember.View.create({
		tagName: 'div',
		classNames: ['span12'],
		template: Ember.Handlebars.compile(
				'<ul class="thumbnails">\
					{{#each Jminee.topicListController}}\
						{{view Jminee.TopicView topicInfo=topicInfo controller=this}}\
					{{/each}}\
				</ul>'
		),
		isVisible: function(){
			return (Jminee.topicNavController.contentType=='topic');
		}.property('Jminee.topicNavController.contentType'),				
	});
	
});