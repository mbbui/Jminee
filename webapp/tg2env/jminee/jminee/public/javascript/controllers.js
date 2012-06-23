$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }

    if (typeof Jminee.Controllers === 'undefined') {
        Jminee.Controllers = {};
    }

    Jminee.Controllers.topicsController = Ember.ArrayProxy.create({
        elems       : [],
        createTopic : function(title) {
            var topic = Jminee.Models.topic.create({ title: title });
        }
    });
});
