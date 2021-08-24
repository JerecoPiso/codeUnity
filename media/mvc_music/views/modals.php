 <?php require "templates/crud_modal.php";?>
 <!-- modal for see album -->
 <div class="modal" id="see">
		<div class="modal-dialog">
			<div class="modal-content modal-see-album">
                <div class="modal-header p-2">
                    <button data-dismiss="modal" class="close close-album-modal">&times;</button>
                </div>
				<div class="modal-body">
					 <h2 class="text-center" id="title-album">KAMIKAZEE</h2>
					 <p class="text-center" id="album-artists"></p>
					 <div class="songs" style="margin-left: 15%;">
					 	<h3>Songs:</h3>
					 	
					 
					 </div>
				</div>
			</div>
		</div>
	</div>
    <!-- modal for delete -->
    <div class="modal" id="del">
    	<div class="modal-dialog">
    		<div class="modal-content delete-modal">
    			<div class="modal-body">
    				<h6 class="text-center">Are you sure you want to delete this record?</h6>
                    <button type="button" class="no" data-dismiss="modal">No</button>
    				<button type="button" class="yes-delete">Yes</button>
    			</div>
    			
    		</div>
    		
    	</div>
    	
    </div>
  
  <!-- modal for getting artists -->
  <div class="modal" id="artist-search">
    <div class="modal-dialog">
        <div class="modal-content artist-search">
            <div class="modal-header p-2">
                <button class="close" data-dismiss="modal">&times;</button>
            </div>
            <div class="modal-body p-2">
                 <h3 class="text-center song-artist"></h3>
                 <p class="text-center album-artist" id=""></p>
                <div class="row mt-2 ">
                    <h4 class="pl-4 s">Songs</h4>
                    <ul class="list-group songs-of-artist pr-4 pl-4" style="min-width: 100%;">
                        
                    </ul>
                    
                </div>
            </div>
        </div>
        
    </div>
       
  </div>

  <!--modal for update -->
  <div class="modal" id="update-music">
    <div class="modal-dialog">
        <div class="modal-content" style="background-color:     #1E90FF; width: 70%;margin-left: 20%;">
            <div class="modal-body">
                <span class="pull-right mb-3" data-dismiss="modal">&times;</span>
                <form class="">
                        <label>Song Title</label>
                        <input type="text" id="edit-song-title" class="form-control">
                        <label>Artist</label>
                        <select class="custom-select" id="edit-song-artist">
                              <?php foreach ($artists as $key => $value): ?>

                                <option value="<?=$value['id']?>"><?=$value['name']?></option>

                              <?php endforeach ?>
                        </select>
                        <label>Genre</label>
                        <select class="custom-select" id="edit-song-genre">
                            <?php foreach ($genre as $key => $value): ?>

                                <option value="<?=$value['id']?>"><?=$value['genre']?></option>

                              <?php endforeach ?>
                        </select>
                        <label>Album</label>
                        <select class="custom-select" id="edit-song-album">
                            <?php foreach ($album as $key => $value): ?>

                                <option value="<?=$value['id']?>"><?=$value['title']?></option>

                              <?php endforeach ?>
                        </select>
                      
                        <button type="button" class="add" id="update-song"> Update </button>
                    </form>
            </div>
        </div>
    </div> 
  </div>
  <!-- no result found -->
  <div class="modal" id="no-result">
    <div class="modal-dialog">
        <div class="modal-content no-result">
            <div class="modal-body">
                <h6>No result found</h6>
            </div>
            
        </div>
        
    </div>
      
  </div>