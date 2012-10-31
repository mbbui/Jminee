$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }

    if (typeof Jminee.Models === 'undefined') {
        Jminee.Models = {};
    }

    Jminee.Models.User = Ember.Object.extend({
        'pic'       : 'http://www.sampleurl.com/sampleimage.jpg',
        'userID'    : 'default',
        'lastName'  : 'Shmoe',
        'fullName'  : function() {
            return this.get('firstName') + ' ' + this.get('lastName');
        }.property(),
        'firstName' : 'Joe'
    });
    Jminee.user = Jminee.Models.User.create({'lastName': 'Bui', 'firstName': 'Bach'});
    
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
