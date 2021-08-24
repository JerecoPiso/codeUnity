<?php
     
     require '../model/artist_model.php';
     new Artists();

     class Artists{
        private $artist;

        function __construct(){
        	$this->artist = new Artist();
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
        	 $data['artist'] = $_POST['artist'];
			 $bdate['bdate'] = $_POST['bdate'];
			 $data['total_album'] = $_POST['total_album'];
		
			 $ret = $this->artist->addArtist($data);
			 echo $ret;
	      
		}
         public function delete(){
             $id = $_POST['id'];
        
             $ret = $this->artist->deleteArtist($id);
             echo $ret;
          
         }

         public function edit(){
            $data['artist'] = $_POST['artist'];
            $data['bdate'] =  $_POST['bdate'];
            $data['num_albums'] =  $_POST['num_albums'];
             $data['id'] =  $_POST['id'];
            $ret = $this->artist->editArtist($data);
            echo $ret;
         }
     }