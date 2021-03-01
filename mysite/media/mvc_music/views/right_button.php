                <button class="btn-add add-song-btn">Add Song</button>
		   	  		<form class="form-add-song">
		   	  			<label>Song Title</label>
		   	  			<input type="text" id="song-title" class="form-control">
		   	  			<label>Artist</label>
		   	  			<select class="custom-select" id="song-artist">
		   	  				  <?php foreach ($artists as $key => $value): ?>

				       	  	  	<option value="<?=$value['id']?>"><?=$value['name']?></option>

				       	  	  <?php endforeach ?>
		   	  			</select>
		   	  			<label>Genre</label>
		   	  			<select class="custom-select" id="song-genre">
		   	  				<?php foreach ($genre as $key => $value): ?>

				       	  	  	<option value="<?=$value['id']?>"><?=$value['genre']?></option>

				       	  	  <?php endforeach ?>
		   	  			</select>
		   	  			<label>Album</label>
		   	  			<select class="custom-select" id="song-album">
		   	  				<?php foreach ($album as $key => $value): ?>

				       	  	  	<option value="<?=$value['id']?>"><?=$value['title']?></option>

				       	  	  <?php endforeach ?>
		   	  			</select>
		   	  			<label>Duration</label>
		   	  			<input type="text" placeholder="1:00 mins" id="duration" class="form-control">
		   	  			<label>Rating</label>
		   	  			<input type="number" placeholder="1-10" id="rating" class="form-control">
		   	  			<button type="button" class="add" id="add-song"> Add </button>
		   	  		</form>
	   	  		<button class="btn-add add-artist-btn">Add Artist</button>
		   	  		   <form class="form-add-artist">
			   	  			
			   	  			<label>Artist</label>
			   	  			<input type="text" class="form-control" id="artist-name" name="">
			   	  			<label>Birthday</label>
			   	  			<input type="date" class="form-control" id="bdate" name="">
			   	  			<label>No. of Album</label>
			   	  			<input type="number" id="total-album" class="form-control">
			   	  			<button type="button" class="add" id="add-artist"> Add </button>
			   	  		</form>
	   	  		<button class="btn-add add-album-btn">Add Album</button>
	   	  		       <form class="form-add-album">
			   	  			
			   	  			<label>Artist</label>
			   	  			<select class="custom-select" id="album-artist">
			   	  				 <?php foreach ($artists as $key => $value): ?>

				       	  	  	<option value="<?=$value['id']?>"><?=$value['name']?></option>

				       	  	  <?php endforeach ?>
			   	  			</select>
			   	  			<label>Title</label>
			   	  			<input type="text" class="form-control" name="" id="album-title">
			   	  			<label>Year</label>
			   	  			<input type="number" class="form-control" name="" id="album-year">

			   	  			<label>No. of Songs</label>
			   	  			<input type="number" class="form-control" id="album-songs">
			   	  			<label>No. of Sold</label>
			   	  			<input type="number" class="form-control" id="album-sold">
			   	  			<button type="button" class="add" id="add-album"> Add </button>
			   	  		</form>
	   	  		      <button class="btn-add add-genre-btn">Add Genre</button>
	   	  		       <form class="form-add-genre">
			   	  			
			   	  			<label>Genre</label>
			   	  			<input type="text" class="form-control" id="genre-input" name="">
			   	  			
			   	  			<button type="button" class="add" id="add-genre"> Add </button>
			   	  		</form>
			   	  	  <button class="btn-add tables-dropdown">Tables</button>
		   	  		      <ul class="list-group dropdown-table">
		   	  		      	<li class="list-group-item"><a href="../controller/index.php?page=artist">Artist</a> </li>
		   	  		      	<li class="list-group-item"><a href="../controller/index.php?page=album">Album</a> </li>
		   	  		        <li class="list-group-item"><a href="../controller/index.php?page=genre">Genre</a> </li>
		   	  		      </ul>