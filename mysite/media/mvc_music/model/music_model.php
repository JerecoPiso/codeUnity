<?php

	require_once 'config.php';

	class Music extends Connection{
		
		public function getMusic(){

			  $sql = "SELECT music.id AS music_id,  music.title AS music_title,  artists.name, genre.genre, album.title as album, album.id FROM music INNER JOIN artists ON music.artist_id=artists.id INNER JOIN genre ON music.genre=genre.id INNER JOIN album ON music.album_id=album.id";
			
		      $stmt = $this->conn->prepare($sql);
		      $stmt->execute();

		      $result = $stmt->fetchALL(PDO::FETCH_ASSOC);
		       $this->close();
		      return $result;
		}
		public function addMusic($data){
			  $stmt = $this->conn->prepare("INSERT INTO music (title,album_id,artist_id,duration,ratings,genre) VALUES (:title, :album,:artist,:duration,:ratings,:genre)");
			      $stmt->bindParam(':title', $data['title']);
			      $stmt->bindParam(':album', $data['album']);
			      $stmt->bindParam(':artist', $data['artist']);
			      $stmt->bindParam(':duration', $data['duration']);
			      $stmt->bindParam(':ratings', $data['rating']);
			      $stmt->bindParam(':genre', $data['genre']);

			      if($stmt->execute()){
			      	return "added";
			      }
	      
		}
		public function deleteMusic($id){
			
			$stmt = $this->conn->prepare("DELETE FROM music WHERE id=:id");
			   $stmt->bindParam(':id', $id);
		      
		      if($stmt->execute()){
		      	return "DEleted";
		      }else{
		      	return "Error";
		      }	
		}
		public function editMusic($data){
			  $stmt = $this->conn->prepare("UPDATE music SET title=:title, album_id=:a_id, artist_id=:s_id, genre=:genre WHERE id=:id");
			      $stmt->bindParam(':title', $data['title']);	    
			      $stmt->bindParam(':a_id', $data['album']);	  
			      $stmt->bindParam(':s_id', $data['artist']);	  
			      $stmt->bindParam(':genre', $data['genre']);	  
			      $stmt->bindParam(':id', $data['id']);	 

			      if($stmt->execute()){
			      	return "updated";
			      }
		}
		//function of getting the artist, album and  genre links
		public function getter($get,$id){
			  if($get == 'artist'){
			  	$sql = "SELECT music.title, album.title as album_title FROM music INNER JOIN album ON music.album_id=album.id WHERE music.artist_id=$id";

			  }else if($get == 'album'){
			  	  $sql = "SELECT  music.title, album.title  as album_title, artists.name as artist FROM album INNER JOIN music ON album.id=music.album_id INNER JOIN artists ON album.artist_id=artists.id WHERE album.id=$id";

			  }else{
			  	 $sql = "SELECT  genre.genre, music.title , artists.name as artist FROM genre INNER JOIN music ON genre.id=music.genre INNER JOIN artists ON music.artist_id=artists.id WHERE genre.id=$id";

			  }
			 $stmt= $this->conn->prepare($sql);
			 $stmt->execute();
			 $result = $stmt->fetchALL(PDO::FETCH_ASSOC);

		     return $result;

		}
		
	}