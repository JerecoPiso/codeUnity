  <div class="body row mr-1 ml-1">
	   	  	<div class="col-lg-9">
	   	  		 <h4 class="pull-left mt-2 ml-3">Song Lists</h4>
	   	  		 <input type="text" id="myInput" class="pull-right mt-2 mb-2" placeholder="Filter table...">
	   	  		 <table class="table table-responsive table-striped" style="overflow: auto;">
       	  
				       	  <thead>
					       	  <tr>
					       	  	<th>No.</th>
					       	  	<th>Title</th>
					       	  	<th>Artist</th>
					       	  	<th>Genre</th>
					       	  	<th>Album</th>
					       	  	<th>See Album</th>
					       	  	<th>Action</th>
					       	 
					       	  </tr>
				       	  </thead>
				       	  <tbody id="myTable">
				       	  	  <?php $counter=1; foreach ($ret as $key => $value): ?>

				       	  	  	 <tr>
				       	  	  	 	<td><?= $counter; ?></td>
					       	  	  	<td id="song-title<?= $value['music_id']?>"><?= $value["music_title"]?></td>
					       	  	  	<td id="song-artist<?= $value['music_id']?>"><?= $value["name"]?></td>
					       	  	  	<td id="song-genre<?= $value['music_id']?>"><?= $value["genre"]?></td>
					       	  	  	<td id="song-album<?= $value['music_id']?>"><?= $value["album"]?></td>
					       	  	  	<td>
					       	  	  		<button class="pull-right see-album" value="<?= $value["id"]?>"><span class="	fa fa-eye"></span> See Album</button>
					       	  	  	</td>
					       	  	  	<td>
					       	  	  		<button class="btn btn-warning" id="edit" value="<?= $value['music_id']?>"><span class="fa fa-edit"></span> Edit</button>
					       	  	  		<button class="btn btn-danger" id="delete" value="<?= $value['music_id']?>"><span class="fa fa-trash mr-2"></span>Delete</button>
					       	  	  	</td>
					       	  	  
					       	  	  	
				       	  	    </tr>
				       	  	  <?php $counter++; endforeach ?>
				       	  	 
				       	  </tbody>
      			  </table>
	   	  	</div>
	   	  	<div class="col-lg-3">
	   	  		
	   	  		<?php require 'right_button.php'; ?>
	   	  		
	   	  	</div>
	   	  </div>

