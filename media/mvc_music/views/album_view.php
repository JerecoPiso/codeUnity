<div class="body row mr-1 ml-1">
	   	  	<div class="col-lg-9">
	   	  		 <h4 class="pull-left mt-2 ml-3">Song Lists</h4>
	   	  		 <input type="text" id="myInput" class="pull-right mt-2 mb-2" placeholder="Filter table...">
	   	  		 <table class="table  table-striped" style="overflow: auto;">
       	  
				       	  <thead>
					       	  <tr>
					       	  	<th>No.</th>
					       	  	<th>Name</th>
					       	  	<th>Title</th>
					       	  	<th>Year</th>
					       	  	<th>No. of Songs</th>
					       	  	<th>Sold</th>
					       	  	<th>Action</th>
					       	 
					       	  </tr>
				       	  </thead>
				       	  <tbody id="myTable">
				       	  	  <?php $counter=1; 
				       	  	  foreach ($album_artist as $key => $value): ?>

				       	  	  	 <tr>
				       	  	  	 	<td><?= $counter; ?></td>
				       	  	  	 	<td id="album-artist<?= $value['id']?>"><?= $value["name"]?></td>
					       	  	  	<td id="album-title<?= $value['id']?>"><?= $value["title"]?></td>
					       	  	  	<td id="album-year<?= $value['id']?>"><?= $value["year"]?></td>
					       	  	  	<td id="album-songs<?= $value['id']?>"><?= $value["no_of_songs"]?></td>
					       	  	  	<td id="album-sold<?= $value['id']?>"><?= $value["sold"]?></td>
					       	  	 
					       	  	  
					       	  	  	<td>
					       	  	  		<button class="btn btn-warning" id="edit-album" value="<?= $value['id']?>"><span class="fa fa-edit"></span> Edit</button>
					       	  	  		<button class="btn btn-danger" id="delete-album" value="<?= $value['id']?>"><span class="fa fa-trash mr-2"></span>Delete</button>
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
