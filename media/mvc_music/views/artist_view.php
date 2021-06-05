<div class="body row mr-1 ml-1">
	   	  	<div class="col-lg-9">
	   	  		 <h4 class="pull-left mt-2 ml-3">Song Lists</h4>
	   	  		 <input type="text" id="myInput" class="pull-right mt-2 mb-2" placeholder="Filter table...">
	   	  		 <table class="table  table-striped" style="overflow: auto;">
       	  
				       	  <thead>
					       	  <tr>
					       	  	<th>No.</th>
					       	  	<th>Name</th>
					       	  	<th>Bithday</th>
					       	  	<th>No. of Albums</th>
					       	  	<th>Action</th>
					       	 
					       	  </tr>
				       	  </thead>
				       	  <tbody id="myTable">
				       	  	  <?php $counter=1; foreach ($artists as $key => $value): ?>

				       	  	  	 <tr>
				       	  	  	 	<td><?= $counter; ?></td>
					       	  	  	<td id="artist<?= $value['id']?>"><?= $value["name"]?></td>
					       	  	  	<td id="birthday<?= $value['id']?>"><?= $value["b_date"]?></td>
					       	  	  	<td id="num_albums<?= $value['id']?>"><?= $value["no_of_albums"]?></td>
					       	  	 
					       	  	  
					       	  	  	<td>
					       	  	  		<button class="btn btn-warning" id="edit-artist" value="<?= $value['id']?>"><span class="fa fa-edit"></span> Edit</button>
					       	  	  		<button class="btn btn-danger" id="delete-artist" value="<?= $value['id']?>"><span class="fa fa-trash mr-2"></span>Delete</button>
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
