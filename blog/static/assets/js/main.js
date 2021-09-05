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
 
  function setUserDevice(){
    
    var screenSize = document.body.clientWidth
    var deviceName = ''
    let data = new FormData()
    if(screenSize < 768){
        deviceName = "Mobile"
    }else if(screenSize >= 768 && screenSize < 992){
        deviceName = "Tablets"
    }else if(screenSize > 992 ){
         deviceName = "Laptop/Desktop"
    }
    data.append("deviceName", deviceName)
    axios.post("/dashboard/setDevice", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}}).then(function(response){

    }).catch(function(err){
        console.log(err.statusText)
    })
}
 
$(document).ready(function(){
	setUserDevice()

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
    Vue.component('date-posted',{
        delimiters: ['[', ']'],
            props:{
                date: String,
                posted: String
            },
            data: function(){
                return {
                    post: this.posted,
                    
                }
            },
            mounted: function(){
    
                this.date = this.getDate(this.post)
        
    
            },
            methods: {
                getDate: function(val){
                    var now = moment().year()+"-"+(moment().month()+1)+"-"+moment().date()+" "+moment().hour()+":"+moment().minutes()+":"+moment().seconds() 
                    var currDate = moment(now)
                    var dateToTest = moment(val);				 
                    var years = currDate.diff(dateToTest, 'years')
                    var months = currDate.diff(dateToTest, 'months')
                    var weeks = currDate.diff(dateToTest, 'weeks')
                    var days = currDate.diff(dateToTest, 'days')
                    var hours = currDate.diff(dateToTest, 'hours')
                     var minutes = currDate.diff(dateToTest, 'minutes')
                       // check year if less than or equal to 1
                       if(years <= 1){
                             // check months if less than 1
                             if (months < 12) {
                                     // check if months is less than or equal to 1
                                   if(months <= 1){
                                       // check if weeks
                                       if (weeks > 4) {
                                           return(months+" month ago")
                                       // check if weeks is greater than 1 and less than 5
                                       }else if (weeks > 1 && weeks < 5){
    
                                           return(weeks+" weeks ago")
    
                                       }else{
                                           // check if weeks is equal to 1 and days is equal to 7
                                           if (weeks == 1 && days == 7) {
    
                                               return(weeks+" week ago")
    
                                           }else{
                                               // check if days is greater than 1 and days is less than 7
                                               if (days > 1 && days < 7) {
                                                   return(days+" days ago")
                                               }else{
                                                   // check if days is equal to 1 and hours is equal to 24
                                                   if(days == 1){
                                                   
                                                       return(days+" day ago")
                                                       
                                                   }else{
    
                                                       if(hours > 1 && hours < 24){
                                                           return(hours+" hours ago")
                                                       }else if(hours >= 24){
                                                         var day = hours/24
    
                                                               if(Math.floor(day) > 1){
                                                                   return(Math.floor(day)+" days ago")
                                                               }else{
                                                                   return(Math.floor(day)+" day ago")
                                                               }
    
                                                       }else{
    
                                                           if(minutes == 60 && hours == 1){
                                                               return(hours+" hour ago")
                                                           }else if(minutes >= 60){
                                                               var hour = minutes/60
    
                                                               if(Math.floor(hour) > 1){
                                                                   return(Math.floor(hour)+" hours ago")
                                                               }else{
                                                                   return(Math.floor(hour)+" hour ago")
                                                               }
    
                                                           }else{
                                                               if (minutes > 1 && minutes == 60) {
                                                                   return(minutes+" minutes ago")
                                                               }else{
                                                                   if(minutes == 1){
                                                                    return(minutes+" minute ago")
                                                                   }else if(minutes == 0){
                                                                    return("now")
                                                                   }else{
                                                                    return(minutes+" minutes ago")
                                                                   }
                                                                   
                                                               }
                                                           }
                                                       }
                                                       
                                                   }
                                               
                                               }
                                           }
                                           
                                       }
    
                                   }else{
                                       return(months+" months ago")
                                   }
                               }else{
                                   return(years+" year ago")
                               }
                       }else{
                               return(years + " years ago")
                       }
                       
                }
            },
            template: "<span>( [date] )</span>"
    
        });
        new Vue({
            delimiters: ['[', ']'],
            el: ".time-counter",
            data:{
                
            }
        
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