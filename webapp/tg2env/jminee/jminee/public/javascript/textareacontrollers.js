$(window).load(function() {
	if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    };
	
    Jminee.FunctionStr = Ember.Object.create({
    	formTypes: {table: {matchStr:'#table', preForm:['#','Members']}},
    	match: function(str){
    		for(type in this.formTypes){
    			if (str.match(this.formTypes[type]['matchStr'])){
    				return type;
    			}
    		}
    		return false;
    	},
    	getHeader: function(type, str){
    		var formType = this.formTypes[type];
    		var tmpStr = str.replace(formType['matchStr']+'(', '');
    		var matchArray = tmpStr.match('[^,)]*(?=[,)]){1}');
    		var fields = formType['preForm'].slice();
    		var matchStr;
    		while (matchArray){
    			 matchStr = matchArray[0];
    			 fields.push(matchStr);
    			 tmpStr = tmpStr.replace(matchStr, '');
    			 if (tmpStr[0]==')'){
    				 return fields;
    			 }
    			 tmpStr = tmpStr.replace(',', '');
    			 matchArray = tmpStr.match('[^,)]*(?=[,)]){1}');
    		}
    		return fields;
    	}
    });
    
    /*********************************************	
	/*		text area controller
	/*********************************************/ 
    Jminee.textAreaController = Ember.Controller.create({
		textChanged: function(){
			var str = $.trim(this.text);
			var type = Jminee.FunctionStr.match(str);
			if (type){
				if (!Jminee.reviewController.visibility)
					Jminee.reviewController.set('visibility',true);
				Jminee.reviewController.set('table', {header: Jminee.FunctionStr.getHeader(type, str)});
			}
			else{
				
			}
		}.observes('text'), 
	});
  
    Jminee.reviewController = Ember.Controller.create({
		message: 'Review',
    });
});