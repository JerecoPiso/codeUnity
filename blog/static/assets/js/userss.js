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
var months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'];
var day = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']

function time(){
	var date = new Date();
	var dateNow = months[date.getMonth()] +' '+ date.getDate() + ' '+date.getFullYear() + " ("+ day[date.getDay()]+")";
    document.getElementById("time").innerHTML = date.toLocaleTimeString();
    document.getElementById('date').innerHTML = dateNow.toString();

}
$(document).ready(function(){

	var set = setInterval(time, 1000)	

	$(window).resize(function(){
       	if(document.body.clientWidth > 992){
       		$('.flex-item1').show().css({'width': '20%'})     				
		}else if(document.body.clientWidth > 600 && document.body.clientWidth < 992){
       		$('.flex-item1').css({'width': '40%'})     		
       	
		}else{
			   $('.flex-item1').css({'width': '40%'}).hide() 
			
       	}
   	});

	$('#bars').click(function(){
		$('.flex-item1').hide()
	})
})



$(document).ready(function(){
	
	$('#questionCode').summernote({
		tabSize: 1,
		maxHeight: 500,
	});
	$('#about').summernote({
			tabSize: 1,
			maxHeight: 500,
			
		
	});
	$('#more').summernote({
		tabSize: 1,
		maxHeight: 500,
		placeholder: 'e.g features, how to run, technologies used',  
	});

	

	$("#about").summernote('code', '')
	$("#more").summernote('code', '')
	
	$("#about-update").summernote('code', '')
	$("#more-update").summernote('code', '')
	
	$("#questionCode").summernote('code', '')
	
		$('#show').click(function(){
			$('.flex-item1').show().css({'width': '50%'})
		})
		$('#bars').click(function(){
			$('.flex-item1').hide()
		})
		$("#uploadErr").click(function(){
			$(".uploadErr").fadeOut()
		})
	})

