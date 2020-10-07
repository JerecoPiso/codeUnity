  var to_show;
	  function toShow(){
	  	to_show =  document.getElementById("to-show").innerHTML;
	  	if(to_show == "true"){
	  		to_show = true;
	  	}else{
	  		to_show = false;
	  	}
	  	return to_show;
	  }
     
		new Vue({
			el: "#forms",
			data:{
				formToShow: toShow(),
				
			}
		})