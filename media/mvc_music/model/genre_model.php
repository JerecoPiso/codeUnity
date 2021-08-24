<?php

	require_once 'config.php';

	class Genre extends Connection{
		
		public function getGenres(){

			  $sql = "SELECT *  FROM genre";
			
		      $stmt = $this->conn->prepare($sql);
		      $stmt->execute();

		      $result = $stmt->fetchALL(PDO::FETCH_ASSOC);
		       $this->close();
		      return $result;
		}
	

        public function addGenre($data){
			 $stmt= $this->conn->prepare("INSERT INTO genre (genre) VALUES (:genre)");
			   $stmt->bindParam(':genre', $data['genre']);
			 if($stmt->execute()){
			 	return "Added";
			 }else{
			 	return "Error";
			 }
			
		}
		public function deleteGenre($id){
			 $stmt= $this->conn->prepare("DELETE FROM genre WHERE id=:id");
			   $stmt->bindParam(':id', $id);
			 if($stmt->execute()){
			 	return "Deleted";
			 }else{
			 	return "Error";
			 }
			
		}
         
        public function editGenre($id,$genre){
			 $stmt= $this->conn->prepare("UPDATE genre SET genre=:genre WHERE id=:id");
			  $stmt->bindParam(':genre', $genre);
			  $stmt->bindParam(':id', $id);
			 if($stmt->execute()){
			 	return "EDited";
			 }else{
			 	return "Error";
			 }
			
		}
          
     

	}