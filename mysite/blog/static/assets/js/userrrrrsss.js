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
       		$('.flex-item1').show().css({'width': '30%'})     		
       	
       	}else{
       		$('.flex-item1').css({'width': '50%'})     					
       	}
   	});
	$('#show').click(function(){
		$('.flex-item1').show().css({'width': '50%'})
	})
	$('#bars').click(function(){
		$('.flex-item1').hide()
	})
})