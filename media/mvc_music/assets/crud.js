$(document).on('click', '#del-genre' ,function(){
		$('.delete').modal('show');
        $('.delete-btn').val($(this).val());

        $('.delete-btn').click(function(){
            $.ajax({
            	url: "../controller/genre_controller.php?page=delete",
            	type: "POST",
            	data: {
            		id: $(this).val()
            	},
            	success: function(res){
            		alert(res)
                     $('.delete').modal('hide');
            	}
            });
        });
        
	});
$(document).on('click', '#delete-album' ,function(){
		$('.delete').modal('show');
        $('.delete-btn').val($(this).val());

        $('.delete-btn').click(function(){
            $.ajax({
            	url: "../controller/album_controller.php?page=delete",
            	type: "POST",
            	data: {
            		id: $(this).val()
            	},
            	success: function(res){
            		alert(res)
                     $('.delete').modal('hide');
            	}
            });
        });
        
});
$(document).on('click', '#delete-artist' ,function(){
        $('.delete').modal('show');
        $('.delete-btn').val($(this).val());

        $('.delete-btn').click(function(){
            $.ajax({
                url: "../controller/artist_controller.php?page=delete",
                type: "POST",
                data: {
                    id: $(this).val()
                },
                success: function(res){
                    alert(res)
                     $('.delete').modal('hide');
                }
            });
        });
        
});
$(document).on('click', '#edit-genre' ,function(){
		$('#edit-genre-modal').modal('show');
        $('.update-btn').val($(this).val());
        var id = $(this).val();
        var old_genre = $('#genre-title'+id).text()
        $('#genre-up').val(old_genre)
        $('.update-btn').click(function(){
            $.ajax({
            	url: "../controller/genre_controller.php?page=edit",
            	type: "POST",
            	data: {
            		id: $(this).val(),
            		genre: $('#genre-up').val()
            	},
            	success: function(res){
            		alert(res)
                    $('#edit-genre-modal').modal('hide');
            	}
            });
        });
        
});
// ON MONDAY CONTINUE THE EDIT FUNCTION OF ALBUM
$(document).on('click', '#edit-album' ,function(){
		$('#edit-album-modal').modal('show');
        $('#update-album').val($(this).val());
        var id = $(this).val();
       
        $('#ab-artist').val($('#album-artist'+id).text())
        $('#ab-title').val($('#album-title'+id).text())
        $('#ab-year').val($('#album-year'+id).text())
        $('#ab-songs').val($('#album-songs'+id).text())
        $('#ab-sold').val($('#album-sold'+id).text())
        $('#update-album').click(function(){
            $.ajax({
            	url: "../controller/album_controller.php?page=edit",
            	type: "POST",
            	data: {
            		id: $(this).val(),
            		artist:  $('#ab-artist').val(),
                    title:  $('#ab-title').val(),
                    year: $('#ab-year').val(),
                    no_of_songs: $('#ab-songs').val(),
                    sold:   $('#ab-sold').val()
            	},
            	success: function(res){
            		alert(res)
                    $('#edit-album-modal').modal('hide');
            	}
            });
        });
        
});

$(document).on('click', '#edit-artist' ,function(){
        $('#edit-artist-modal').modal('show');
        $('#update-artist').val($(this).val());
        var id = $(this).val();
        $('#artist-album').val($('#artist'+id).text());
        $('#bday').val($('#birthday'+id).text());
        $('#total-of-album').val($('#num_albums'+id).text());
 
        $('#update-artist').click(function(){
            $.ajax({
                url: "../controller/artist_controller.php?page=edit",
                type: "POST",
                data: {
                    id: $(this).val(),
                    artist: $('#artist-album').val(),
                    bdate:   $('#bday').val(),
                    num_albums:  $('#total-of-album').val()

                },
                success: function(res){
                    alert(res)
                    $('#edit-artist-modal').modal('hide');
                }
            });
        });
        
});
