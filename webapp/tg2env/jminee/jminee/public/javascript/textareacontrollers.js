$(window).load(function() {
	if (typeof window.Jminee === 'undefined') {
        window.Jminee = Ember.Application.create();
    };
	
    Jminee.FunctionStr = Ember.Object.create({
    	functionKey: '#',
    	functionStrs: ['[tT]able.*$'],
    	match: function(str){
    		for(var i=0; i<this.functionStrs.length; i++){
    			if (str.match(this.functionKey+this.functionStrs[i])){
    				return true;
    			}
    		}
    		return false;
    	},    	
    });
    
    /*********************************************	
	/*		text area controller
	/*********************************************/ 
    Jminee.textAreaController = Ember.Controller.create({
		textChanged: function(){
			var str = $.trim(this.text);
			if (Jminee.FunctionStr.match(str)){
				console.log(str);  
			}
		}.observes('text'), 
	});
    
});