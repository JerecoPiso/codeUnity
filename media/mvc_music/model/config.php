<?php
 class Connection{
  private $server = "mysql:host=localhost;dbname=music";
  private $username = "root";
  private $password = "";

  private $options  = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);

  protected $conn;
    //function for connection
  public function __construct(){
    $this->open();
  }
  public function open(){
    try{

      $this->conn = new PDO($this->server, $this->username, $this->password);
      return $this->conn;
    }
    catch (PDOException $e){
      echo "There is some problem in connection: " . $e->getMessage();
    }
 
    }
    protected function close(){
      $this->conn = null;
    }
  }
?>