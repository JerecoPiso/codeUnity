   <nav class="navbar navbar-expand-md bg-dark navbar-dark" >
				
		<!-- Toggler/collapsibe Button -->
		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
			 <span class="navbar-toggler-icon "></span>
		 </button>

		 <!-- Navbar links -->
		 <div class="collapse navbar-collapse" id="collapsibleNavbar">
			<ul class="navbar-nav">
				<li class="nav-item dropdown">
				       
				   <a class="nav-link dropdown-toggle link-artists" href="#" id="navbardrop" data-toggle="dropdown">
					  <span class="fa fa-users mr-2"></span>Artists
				    </a>
					   <div class="dropdown-menu">
					      	<?php foreach ($artists as  $value): ?>

					      		 <a class="dropdown-item" id="artist-link" href="../controller/music_controller.php?page=getInfo&get=artist&id=<?=$value['id']?>"><?=$value['name']?></a>

					      	<?php endforeach ?>					     				      
					   </div>
			    </li>
				     
				<li class="nav-item dropdown">
				    
				      <a class="nav-link dropdown-toggle " href="#" id="navbardrop" data-toggle="dropdown">
					     <span class="fa fa-book mr-2"></span>Albums
					 </a>
					  <div class="dropdown-menu" style="">
					      	<?php foreach ($album as  $value): ?>

					      		 <a class="dropdown-item" id="album-link" href="../controller/music_controller.php?page=getInfo&get=album&id=<?=$value['id']?>"><?=$value['title']?></a>

					      	<?php endforeach ?>
					    					       
					 </div>
			   </li>
			    <li class="nav-item dropdown">
				   
				    <a class="nav-link dropdown-toggle " href="" id="navbardrop" data-toggle="dropdown">
					    <span class="fa fa-microphone"></span> Genre
					</a>
					<div class="dropdown-menu" >
					      	<?php foreach ($genre as  $value): ?>

					      		 <a class="dropdown-item" href="../controller/music_controller.php?page=getInfo&get=genre&id=<?=$value['id']?>"><?=$value['genre']?></a>

					      	<?php endforeach ?>					    
					       
					</div>

				</li>
			
				
		     </ul>

		</div>
				   
	</nav>