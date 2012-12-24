$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }

    if (typeof Jminee.Models === 'undefined') {
        Jminee.Models = {};
    }

    Jminee.UserInfo = Ember.Object.extend({
    	clearInfo: function(){
    		this.set('email', null);
    	},
    	setInfo: function(info){
    		this.set('email', info.email);
    	}
    });
    Jminee.userInfo = Jminee.UserInfo.create();
    
    Jminee.Models.message = Ember.Object.extend({
        'msgID'   : '1234ABCD',
        'isRead'  : false,
        'subject' : 'sample subject',
        'content' : 'Some sample text.'
    });

    Jminee.Models.topic = Ember.Object.extend({
        'title'       : 'sample title',
        'msgIDs'      : [],
        'topicID'     : '123',
        'numMessages' : 0,
        'addMessages' : function(msgIDs) {
            var i;
            for (i = 0; i < msgIDs.length; i+=1) {
                this.get('msgIDs')[numMessages + i] = msgIDs[i];
            }
            this.set('numMessages', this.get('numMessages') + msgIDs.length);
        }
    });
});
