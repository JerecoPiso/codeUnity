<?php

	require_once 'config.php';

	class Artist extends Connection{
		
		public function getArtists(){

			  $sql = "SELECT * FROM artists";
			
		      $stmt = $this->conn->prepare($sql);
		      $stmt->execute();

		      $result = $stmt->fetchALL(PDO::FETCH_ASSOC);
		       $this->close();
		      return $result;
		}
		public function addArtist($data){
			  $stmt = $this->conn->prepare("INSERT INTO artists (name,b_date,no_of_albums) VALUES (:title, :bdate,:t_album)");
			      $stmt->bindParam(':title', $data['artist']);
			      $stmt->bindParam(':bdate',  $data['bdate']);
			      $stmt->bindParam(':t_album',  $data['total_album']);
			  

			      if($stmt->execute()){
			      	return "added";
			      }	
	      
		}
		public function deleteArtist($id){
			$stmt = $this->conn->prepare("DELETE FROM artists WHERE id=:id");
			$stmt->bindParam(':id', $id);
			if($stmt->execute()){
			      	return "deleted";
			 }else{
			 	return "error";
			 }
		}
		public function editArtist($data){
			$stmt = $this->conn->prepare("UPDATE artists SET name=:name, b_date=:bdate, no_of_albums=:num_albums WHERE id=:id");
			$stmt->bindParam(':name', $data['artist']);
			$stmt->bindParam(':bdate', $data['bdate']);
			$stmt->bindParam(':num_albums', $data['num_albums']);
			$stmt->bindParam(':id', $data['id']);
			if($stmt->execute()){
			      	return "edited";
			 }else{
			 	return "error";
			 }
		}


	}