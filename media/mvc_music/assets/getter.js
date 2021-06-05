$(document).on('click','.dropdown-item', function(e){
	
	var display = $(this).attr('id');
	$('.song-artist').text($(this).text());
      
	 $.ajax({

	 	type: "GET",
	 	url: $(this).attr('href'),
	 	
	 	success:function(res){
	 		
	 		//check if the link click is artist
	 		var data = JSON.parse(res)
            if (display == "artist-link") {
              
              if(data.title.length === 0){
                 //alert for no result
              	 $('#no-result').modal('show');
              	 setInterval(function(){
              	 	 $('#no-result').modal('hide');
              	 }, 1500);

              }else{

              	  for (var i = 0; i < data.title.length; i++) {
   
            	 //$('.songs-of-artist').append("<p class='song' style='margin-left: 1%%;'>"+data.title[i]+"</p>");
            	  $('.list-group').append("<li class='list-group-item' >"+data.title[i]+"( "+data.album_title[i]+" )</li>")   	
            	  $('#album-artist').text($(this).text())
                
            	  $('#artist-search').modal('show')
                 }

              }
           
            }else if(display == "album-link"){

            	 //var data = JSON.parse(res)
            	 if(data.title.length === 0){
            	 	 //alert for no result
            	 	 $('#no-result').modal('show');
	              	     setInterval(function(){
	              	 	 $('#no-result').modal('hide');
	              	 }, 1500);

            	 }else{
            	 	 for (var i = 0; i < data.title.length; i++) {
		   					$('.album-artist').text("( "+data.artist[i]+" )")
		            	  $('.list-group').append("<li class='list-group-item' >"+data.title[i]+"</li>")   	
		            	
		                
		                 
		            	 $('#artist-search').modal('show')
		              }
            	 }
                	 		 
	    	}else{
	    		 //var data = JSON.parse(res)
	    		  if(data.title.length === 0){
	    		  	 //alert for no result
            	 	 $('#no-result').modal('show');
	              	 setInterval(function(){
	              	 	 $('#no-result').modal('hide');
	              	 }, 1500);

            	 }else{

	                 for (var i = 0; i < data.title.length; i++) {

	   					$('.album-artist').text("( Genre )")
	            	    $('.list-group').append("<li class='list-group-item' >"+data.title[i]+"( " +data.artist[i]+" )</li>")   		            	
	               	                
	            	 $('#artist-search').modal('show')
	            	}
	    		//alert(res)
	    	}
         }
       }
	 });
	 e.preventDefault();
});
$('.close').click(function(){
  $('.list-group > .list-group-item').remove();
  	$('.album-artist').text('');
});