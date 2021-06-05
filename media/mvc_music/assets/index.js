$(document).ready(function(){
   //slideToggle for add song
   $('.add-song-btn').click(function(){
     
     $('.form-add-song').slideToggle();

   });
 
   $('.add-artist-btn').click(function(){
     
     $('.form-add-artist').slideToggle();

   });
   $('.add-album-btn').click(function(){
     
     $('.form-add-album').slideToggle();

   });
   $('.add-genre-btn').click(function(){
     
     $('.form-add-genre').slideToggle();

   });
    $('.tables-dropdown').click(function(){
     
     $('.dropdown-table').slideToggle();

   });
  
   $('.close-album-modal').click(function(){
     
     $('.songs > p').remove();

   });
  //filtering the data on the table
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
   
});
//adding new song
$(document).on('click', '#add-song', function(){
     
     $.ajax({
         
         url: "../controller/music_controller.php?page=save",
         type: "POST",
         data: {

            title: $('#song-title').val(),
            artist: $('#song-artist').val(),
            genre: $('#song-genre').val(),
            album: $('#song-album').val(),
            duration: $('#duration').val(),
            rating: $('#rating').val()
         },
 			
 			success:function(res){
       // alert(res)
 				$('input').val('');
 				response();
 			}

     });
   //   event.preventDefault();
});
//adding new genre
$(document).on('click', '#add-genre', function(){
     
     $.ajax({
         
         url: "../controller/genre_controller.php?page=save",
         type: "POST",
         data: {

            genre: $('#genre-input').val(),
           
         },
      
      success:function(res){
        alert(res)
        $('input').val('');

      }

     });
   //   event.preventDefault();
});
//adding new artist
$(document).on('click', '#add-artist', function(){
     
     $.ajax({
         
         url: "../controller/artist_controller.php?page=save",
         type: "POST",
         data: {

          
            artist: $('#artist-name').val(),
            bdate: $('#bdate').val(),
            total_album: $('#total-album').val(),
          
         },
 			
 			success:function(res){
 				$('input').val('');
        alert(res)
 			
 			}

     });
   //   event.preventDefault();
});
//adding new album
$(document).on('click', '#add-album', function(){
     
     $.ajax({
         
         url: "../controller/album_controller.php?page=save",
         type: "POST",
         data: {

          
            artist: $('#album-artist').val(),
            title: $('#album-title').val(),
            year: $('#album-year').val(),
            song: $('#album-songs').val(),
            sold: $('#album-sold').val(),
          
         },
 			
 			success:function(res){
        alert(res)
 				$('input').val('');
 				//response();
 			}

     });
   //   event.preventDefault();
});
//function for response
function response(){

        $.get("../controller/home.php?page=response", function(data){
        
           $('#myTable').html(data);
        });
}
$(document).on('click', '#haha', function(){

        $.get("../controller/home.php?page=response", function(data){
         
           //$('.col-lg-9').html(data);
        });
})
//see album
$(document).on('click', '.see-album', function(){
     
  $.ajax({
         
         url: "../controller/album_controller.php?page=see",
         type: "POST",
         data: {

            album: $(this).val()
           
         },
 			
 			success:function(res){
			  var data = JSON.parse(res)
              for (var i = 0; i < data.title.length; i++) {
            	 $('#title-album').text(data.title[i]);
            	 $('#album-artists').text(data.name[i]+"( "+data.year[i]+" )");    
            	 $('.songs').append("<p class='song' style='margin-left: 15%;'>"+data.music_title[i]+"</p>")   	
            	 $('#see').modal('show')
              }
           
         	   
 			}

     });
   //   event.preventDefault();
});
//deleting the music
$(document).on('click', '#delete', function(){
	   $('#del').modal('show')
       $('.yes-delete').val($(this).val());
       $('.yes-delete').click(function(){
       	//$(this).val()
	       $.ajax({
	       		url: "../controller/music_controller.php?page=delete",
	       		type: "POST",
	       		data:{
                   id: $(this).val()
	       		},
	       		success:function(res){
	       			 $('#del').modal('hide')
	       		  	//alert(res)
               // alert(res)
               response();
	       		}
	       });
       });
});
//editing the music
$(document).on('click', '#edit', function(){
     var id = $(this).val();
    // alert($("#song-genre"+id).text())
     $('#edit-song-title').val($("#song-title"+id).text());
     $('#edit-song-artist').val($("#song-artist"+id).text());
     $('#edit-song-genre').val($("#song-genre"+id).text());
     $('#edit-song-album').val($("#song-album"+id).text());
     $('#update-music').modal('show');

     $('#update-song').click(function(){
       $.ajax({
         
         url: "../controller/music_controller.php?page=edit",
         type: "POST",
         data: {
            id: id,
            title: $('#edit-song-title').val(),
            artist: $('#edit-song-artist').val(),
            genre: $('#edit-song-genre').val(),
            album: $('#edit-song-album').val(),
         },
         success:function(res){
            //alert(res)
             $('#update-music').modal('hide')
             response();
         }
  
        });


     });
    
});
