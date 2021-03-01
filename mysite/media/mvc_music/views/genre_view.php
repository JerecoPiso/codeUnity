<div class="body row mr-1 ml-1">
	   	  	<div class="col-lg-9">
	   	  		 <h4 class="pull-left mt-2 ml-3">Song Lists</h4>
	   	  		 <input type="text" id="myInput" class="pull-right mt-2 mb-2" placeholder="Filter table...">
	   	  		 <table class="table  table-striped" style="overflow: auto;">
       	  
				       	  <thead>
					       	  <tr>
					       	  	<th>No.</th>
					       	  	<th>Genre</th>
					       	  	<th>Action</th>
					       	 
					       	  </tr>
				       	  </thead>
				       	  <tbody id="myTable">
				       	  	  <?php $counter=1; foreach ($genre as  $value): ?>

				       	  	  	 <tr>
				       	  	  	 	<td><?= $counter; ?></td>
					       	  	  	<td id="genre-title<?= $value['id']?>"><?= $value["genre"]?></td>
					       	  	
					       	  	  
					       	  	  	<td>
					       	  	  		<button class="btn btn-warning" id="edit-genre" value="<?= $value['id']?>"><span class="fa fa-edit"></span> Edit</button>
					       	  	  		<button class="btn btn-danger" id="del-genre" value="<?= $value['id']?>"><span class="fa fa-trash mr-2"></span>Delete</button>
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
