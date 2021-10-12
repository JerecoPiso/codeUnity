new Vue({
    el: ".search-section",
    data:{
        searchValue: "",
        toSearch: 'Search by:'
    },
    methods:{
        search: function(){
            if(this.toSearch == "Projects"){
                window.location.href="/projects/search/"+this.searchValue
            }else if(this.toSearch == "Questions"){
                window.location.href="/questions/search/"+this.searchValue
            }else if(this.toSearch == "Developers"){
                window.location.href="/developers/search/"+this.searchValue
            }else{
                alert("Please select a category on what to search")
            }
        }
    }
})
 
//   function setUserDevice(){
    
//     var screenSize = document.body.clientWidth
//     var deviceName = ''
//     let data = new FormData()
//     if(screenSize < 768){
//         deviceName = "Mobile"
//     }else if(screenSize >= 768 && screenSize < 992){
//         deviceName = "Tablets"
//     }else if(screenSize > 992 ){
//          deviceName = "Laptop/Desktop"
//     }
//     data.append("deviceName", deviceName)
//     axios.post("/dashboard/setDevice", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}}).then(function(response){
//         alert("haha")
//     }).catch(function(err){
//         console.log(err.statusText)
//     })
// }
 
$(document).ready(function(){
	// setUserDevice()

	$(window).resize(function(){
       	if(document.body.clientWidth > 651){
       		$('#top-nav').css({'width': '100%'})
       		$('#open').hide() 	
       	}else{
       		$('#top-nav').css({'width': '0'})
       		$('#open').show() 	
       	}

       	if(document.body.clientWidth > 600 && document.body.clientWidth > 800){
			$('.languages-box').show()
       	}else{
			$('.languages-box').hide()
       	}
   	});

	$('#open').click(function(){
	
		   $('#top-nav').css({'width': '250px'})
		   $('#top-nav').show()
	 	$(this).hide()
	 	
	})
	$('.showSearch').click(function(){
	 		
			 $('.search-section').slideDown()
			 
			 
		})
		$('.x').click(function(){
	 		
			 $('.search-section').slideUp()
			 
			 
		})
	$('#close').click(function(){
	 		
	 	$('#top-nav').css({'width': '0'})
	 	$('#open').show() 	
	 	
	})
  	$('#btn-languages').click(function(){
	 		
	 	$('.languages-box').show()
	 	
	 	
	})
	$('#close-show').click(function(){
	 		
		$('.languages-box').hide()
	 	
	})
	
	})

    document.onreadystatechange = function() {
	
        if (document.readyState !== "complete") {
            document.querySelector(
              "body").style.display = "none";
            document.querySelector(
              ".spinner1").style.display = "block";
        
        } else {
            document.querySelector(
              ".spinner1").style.display = "none";
            document.querySelector(
              "body").style.display = "block";
        }
    };
     