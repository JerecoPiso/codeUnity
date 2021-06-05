<?php
     
     require_once '../model/music_model.php';
     new Musics();

     class Musics{
        private $music;

        function __construct(){
        	$this->music = new Music();
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
        	   
            $data['title'] = $_POST['title'];
            $data['artist'] = $_POST['artist'];
            $data['genre']= $_POST['genre'];
            $data['album'] = $_POST['album'];
            $data['duration'] = $_POST['duration'];
            $data['rating'] = $_POST['rating'];

    			  $ret = $this->music->addMusic($data);
    			  echo $ret;
	      
	   	}

      public function delete(){
            $id = $_POST['id'];
            $ret = $this->music->deleteMusic($id);
            echo $ret;

      }
       public function edit(){
            $data['id'] = $_POST['id'];
            $data['title'] = $_POST['title'];
            $data['artist'] = $_POST['artist'];
            $data['genre']= $_POST['genre'];
            $data['album'] = $_POST['album'];
             $ret = $this->music->editMusic($data);
             echo $ret;

      }

      public function getInfo(){

        $id= $_GET['id'];

        if($_GET['get'] == 'artist'){
          $get = 'artist';
        
          $ret = $this->music->getter($get,$id);
          $result = array(
                'title' => array(),
                'album_title' => array()
          );

          foreach ($ret as  $value) {
            array_push($result["title"], $value["title"]);
            array_push($result["album_title"], $value["album_title"]);
          }

        
        }else if($_GET['get'] == 'album'){

           $get = 'album';
        
          $ret = $this->music->getter($get,$id);
          $result = array(
                'title' => array(),
                'album_title' => array(),
                'artist' => array()
          );

          foreach ($ret as  $value) {
            array_push($result["title"], $value["title"]);
            array_push($result["album_title"], $value["album_title"]);
            array_push($result["artist"], $value["artist"]);
          }

          
        }else{
          $get = 'genre';
        
          $ret = $this->music->getter($get,$id);
          $result = array(
                'genre' => array(),
                'title' => array(),
                'artist' => array()
          );

          foreach ($ret as  $value) {
            array_push($result["genre"], $value["genre"]);
            array_push($result["title"], $value["title"]);
            array_push($result["artist"], $value["artist"]);
          }

         

        }

           echo json_encode($result);

      }
     }