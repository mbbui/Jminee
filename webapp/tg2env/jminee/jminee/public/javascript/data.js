$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }

    if (typeof Jminee.Models === 'undefined') {
        Jminee.Models = {};
    }

    Jminee.UserInfo = Ember.Object.extend({
    	clearInfo: function(){
    		this.set('id', null);
    		this.set('name', null);
    		this.set('email', null);
    	},
    	setInfo: function(info){
    		this.set('id', info.id);
    		this.set('name', info.name);
    		this.set('email', info.email);
    	}
    });
    Jminee.userInfo = Jminee.UserInfo.create();
    Jminee.topicInfo = Ember.Object.create();
    
    Jminee.Models.message = Ember.Object.extend({
        'msgID'   : '1234ABCD',
        'isRead'  : false,
        'subject' : 'sample subject',
        'content' : 'Some sample text.'
    });

    Jminee.Topic = Ember.Object.extend();
});