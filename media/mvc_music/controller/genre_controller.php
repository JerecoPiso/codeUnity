<?php
     
     require_once '../model/genre_model.php';
     new Genres();

     class Genres{
        private $genre;

        function __construct(){
        	$this->genre = new Genre();
        	if(isset($_GET['page'])){
        		$this->{$_GET['page']}();

        	}else{
        		$this->index();
        	}
        }
        
        public function index(){
              
        	include '../views/header.php';
            include '../views/navbar.php';
            include '../views/body.php';
            include '../views/modals.php';
            include '../views/footer.php';

        }
        public function save(){
        	    $data['genre'] = $_POST['genre'];
           
			        $ret = $this->genre->addGenre($data);
			        echo $ret;
	      
		}
        public function delete(){
                $id = $_POST['id'];
           
                $ret = $this->genre->deleteGenre($id);
                echo $ret;
        }
        public function edit(){
                $id = $_POST['id'];
                $genre = $_POST['genre'];
           
                $ret = $this->genre->editGenre($id,$genre);
                echo $ret;
        }

     }