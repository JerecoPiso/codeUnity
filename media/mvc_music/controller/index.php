<?php
    
     require_once '../model/music_model.php';
     require_once '../model/artist_model.php';
     require_once '../model/album_model.php';
     require_once '../model/genre_model.php';
     new Home();

     class Home{
        private $music, $artist, $album, $genre;
        
        function __construct(){
            $this->music = new Music();
        	$this->artist = new Artist();
            $this->album = new Album();
            $this->genre = new Genre();
        	if(isset($_GET['page'])){
        		$this->{$_GET['page']}();

        	}else{
        		$this->index();
        	}
        }
        
        public function index(){

            $ret = $this->music->getMusic();
            $artists = $this->artist->getArtists();
            $genre = $this->genre->getGenres();
            $album = $this->album->getAlbums();


            include '../views/templates/header.php';
            include '../views/templates/navbar.php';
            include '../views/music_view.php';
            include '../views/modals.php';
            include '../views/templates/footer.php';    	
        }

        public function genre(){
            $genre = $this->genre->getGenres();
            $ret = $this->music->getMusic();
            $artists = $this->artist->getArtists();
           
            $album = $this->album->getAlbums();

            include '../views/templates/header.php';
            include '../views/templates/navbar.php';
            include '../views/genre_view.php';
            include '../views/modals.php';
            include '../views/templates/footer.php';      


        }
         public function artist(){
            $genre = $this->genre->getGenres();
            $ret = $this->music->getMusic();
            $artists = $this->artist->getArtists();
           
            $album = $this->album->getAlbums();

            include '../views/templates/header.php';
            include '../views/templates/navbar.php';
            include '../views/artist_view.php';
            include '../views/modals.php';
            include '../views/templates/footer.php';      


        }
        public function album(){
            $genre = $this->genre->getGenres();
            $ret = $this->music->getMusic();
            $artists = $this->artist->getArtists();
            $album = $this->album->getAlbums();
            $album_artist = $this->album->getAlbumArtist();

            include '../views/templates/header.php';
            include '../views/templates/navbar.php';
            include '../views/album_view.php';
            include '../views/modals.php';
            include '../views/templates/footer.php';      

        }

        public function response(){
            $ret = $this->music->getMusic();

             include '../views/response.php';

        }
        
        
     }