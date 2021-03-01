
	   	  		 <table class="table  table-striped" >
       	  
				       	  <thead>
					       	  <tr>
					       	  	<th>No.</th>
					       	  	<th>Title</th>
					       	  	<th>Artist</th>
					       	  	<th>Genre</th>
					       	  	<th>Album</th>
					       	  </tr>
				       	  </thead>
				       	  <tbody>
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
	   	  