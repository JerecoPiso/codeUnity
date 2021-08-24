   <!-- modal for delete -->
    <div class="modal delete">
    	<div class="modal-dialog">
    		<div class="modal-content delete-modal">
    			<div class="modal-body">
    				<h6 class="text-center">Are you sure you want to delete this genre?</h6>
                    <button type="button" class="no" data-dismiss="modal">No</button>
    				<button type="button" class="yes-delete delete-btn">Yes</button>
    			</div>
    			
    		</div>    
    		
    	</div>
    	
    </div>

    <div class="modal" id="edit-genre-modal">
        <div class="modal-dialog">
            <div class="modal-content modal-genre">
                <div class="modal-body">
                     <form>                        
                          <label>Genre</label>
                            <input type="text" class="form-control" id="genre-up" name="">
                            
                            <button type="button" class="btn btn-primary pull-right update-btn" > Update </button>
                        </form>
                </div>
            </div>
            
        </div>
        
    </div>
    <div class="modal" id="edit-album-modal">
        <div class="modal-dialog">
            <div class="modal-content modal-genre">
                <div class="modal-body">
                     <form>
                            
                            <label>Artist</label>
                            <select class="custom-select" id="ab-artist">
                                 <?php foreach ($artists as $key => $value): ?>

                                <option value="<?=$value['id']?>"><?=$value['name']?></option>

                              <?php endforeach ?>
                            </select>
                            <label>Title</label>
                            <input type="text" class="form-control" name="" id="ab-title">
                            <label>Year</label>
                            <input type="number" class="form-control" name="" id="ab-year">

                            <label>No. of Songs</label>
                            <input type="number" class="form-control" id="ab-songs">
                            <label>No. of Sold</label>
                            <input type="number" class="form-control" id="ab-sold">
                            <button type="button" class="add" id="update-album"> Update </button>
                        </form>
                </div>
            </div>
            
        </div>
        
    </div>

     <div class="modal" id="edit-artist-modal">
        <div class="modal-dialog">
            <div class="modal-content modal-genre">
                <div class="modal-body">
                    <form>
                            
                            <label>Artist</label>
                            <input type="text" class="form-control" id="artist-album" name="">
                            <label>Birthday</label>
                            <input type="date" class="form-control" id="bday" name="">
                            <label>No. of Album</label>
                            <input type="number" id="total-of-album" class="form-control">
                            <button type="button" class="add" id="update-artist"> Update </button>
                    </form>
                </div>
            </div>
            
        </div>
        
    </div>