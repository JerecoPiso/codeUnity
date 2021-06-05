<?php

	require_once 'config.php';

	class Album extends Connection{
		
		public function getAlbums(){

			  $sql = "SELECT * FROM album";
			
		      $stmt = $this->conn->prepare($sql);
		      $stmt->execute();

		      $result = $stmt->fetchALL(PDO::FETCH_ASSOC);
            
		      return $result;
		}

		 public function addAlbum($data){
              $stmt = $this->conn->prepare("INSERT INTO album (artist_id,title,year,no_of_songs,sold) VALUES (:artist_id, :title,:year,:no_of_songs,:sold)");
                  $stmt->bindParam(':artist_id',   $data['artist']);
                  $stmt->bindParam(':title', $data['title']);
                  $stmt->bindParam(':year',$data['year']);
                  $stmt->bindParam(':no_of_songs', $data['song'] );
                  $stmt->bindParam(':sold',  $data['sold']);
            

                  if($stmt->execute()){
                    return "added";
                  }
          
        }
        public function seeAlbum($album){
			
			$query = $this->conn->prepare("SELECT album.title, album.year, album.no_of_songs, artists.name, music.title  AS music_title FROM album INNER JOIN artists ON album.artist_id=artists.id INNER JOIN music ON album.id=music.album_id WHERE album.id=$album");
			  
		      $query->execute();

		      $result = $query->fetchALL(PDO::FETCH_ASSOC);

		      return $result;
		}

		public function getAlbumArtist(){
			$query = $this->conn->prepare("SELECT album.id, album.title, album.year, album.no_of_songs, album.sold, artists.name FROM album INNER JOIN artists ON album.artist_id=artists.id");

		      $query->execute();

		      $result = $query->fetchALL(PDO::FETCH_ASSOC);
		       $this->close();
		      return $result;
		}
		public function deleteAlbum($id){
			 $stmt= $this->conn->prepare("DELETE FROM album WHERE id=:id");
			   $stmt->bindParam(':id', $id);
			 if($stmt->execute()){
			 	return "Deleted";
			 }else{
			 	return "Error";
			 }
			
		}
		public function editAlbum($data){
			 $stmt= $this->conn->prepare("UPDATE album SET artist_id=:a_id, title=:title, year=:year, no_of_songs=:no_songs, sold=:sold WHERE id=:id");
			 $stmt->bindParam(':a_id', $data['artist']);
			 $stmt->bindParam(':title',  $data['title']);
			 $stmt->bindParam(':year',  $data['year']);
			 $stmt->bindParam(':no_songs',  $data['no_of_songs']);
			 $stmt->bindParam(':sold',  $data['sold']);
			 $stmt->bindParam(':id',  $data['id']);
			 if($stmt->execute()){
			 	return "edited";
			 }else{
			 	return "Error";
			 }
			
		}




	}