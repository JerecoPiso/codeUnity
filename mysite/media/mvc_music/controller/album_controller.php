<?php
     
     require_once '../model/album_model.php';
     new Albums();

     class Albums{
        private $album;

        function __construct(){
        	$this->album = new Albu
        	}m();
            if(isset($_GET['page'])){
                $this->{$_GET['page']}();

            }else{
                $this->index();
        }
        
        public function index(){
              
        	include '../views/templates/header.php';
            include '../views/templates/navbar.php';
            include '../views/body.php';
            include '../views/modals.php';
            include '../views/templates/footer.php';

        }
        public function save(){
        	    $data['artist'] = $_POST['artist'];
              $data['title'] = $_POST['title'];
              $data['year'] = $_POST['year'];
              $data['song'] = $_POST['song'];
              $data['sold'] = $_POST['sold'];
      			  $ret = $this->album->addAlbum($data);
      			  echo $ret;
	      
    		}

        public function see(){
            $album = $_POST['album'];
            $ret = $this->album->seeAlbum($album);
             $result = array(
               'title' => array(),
               'year' => array(),
               'no_of_songs' => array(),
               'name' => array(),
               'music_title' => array()

             );
 
        
             foreach ($ret as  $fetch) {
                array_push($result['title'], $fetch['title']);
                array_push($result['year'], $fetch['year']);
                array_push($result['no_of_songs'], $fetch['no_of_songs']);
                array_push($result['name'], $fetch['name']);
                array_push($result['music_title'], $fetch['music_title']);
             }
            
        
            echo  json_encode($result);

        }
         public function delete(){
                $id = $_POST['id'];
           
                $ret = $this->album->deleteAlbum($id);
                echo $ret;
        }

        public function edit(){
                $data['artist'] = $_POST['artist'];
                $data['title'] =  $_POST['title'];
                $data['year'] = $_POST['year'];
                $data['no_of_songs'] = $_POST['no_of_songs'];
                $data['sold'] = $_POST['sold'];
                $data['id'] = $_POST['id'];
                $ret = $this->album->editAlbum($data);
                echo $ret;
        }
     }