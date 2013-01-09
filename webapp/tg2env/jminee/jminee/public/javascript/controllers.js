jQuery.ajaxSettings.traditional = true;

$(window).load(function() {
    if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    }
    
    
    
    $.ajax({
     	url: '/post_login/',
     	data: {__logins: 0},
		dataType: 'json',
		success: function(resp){
			if (resp.success){
				Jminee.userInfo.setInfo(resp.userInfo);
				Jminee.set('isLogin',true);
			}
			else 
				Jminee.set('isLogin',false);
			return resp;
		},
		error: function(resp){
			Jminee.mainAlertView.show(null, 'Error connecting server!');
		} 
    });
    
    Jminee.reopen({
    	logInOut: function(){
			if (Jminee.isLogin){
				Jminee.topicNavController.pushCrumb(Jminee.TopicItemNavController.create(
			    		{title: 'Topics', contentType: 'topic', contentController: Jminee.topicListController}));
				Jminee.loginView.removeFromParent();
				Jminee.mainView.appendTo("#main_container");
				Jminee.accountView.appendTo("#navbar_container");
			}			
			else{
				//TODO: clear all info
				Jminee.mainView.removeFromParent();
				Jminee.accountView.removeFromParent();
				Jminee.loginView.appendTo("#main_container");
			};
		}.observes('isLogin'),
    });
});

