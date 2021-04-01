<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Dashboard extends CI_Controller {

		function __construct(){
	 			parent::__construct();
				$this->load->helper('url');
				$this->load->library('session');
				$this->load->model('dashboard_model');
				//$this->load->library('Pdf');
				//$this->load->library('unit_test');

	 	}
	 	
	 	//this is the login and signup page of the admin
	 	public function index(){

	 		$this->load->view('templates/header');
	 		$this->load->view('dashboard/login');
	 		$this->load->view('templates/footer');

	 	}
	 	//this is the page for recovering account
	 	public function recover(){

	 		$this->load->view('templates/header');
	 		$this->load->view('dashboard/recover_account');
	 		$this->load->view('templates/footer');

	 	}
	 	/*main page of the admin panel*/
	 	public function dashboard(){

	 		if($this->session->userdata('admin')){

	 		  $this->load->view('templates/header');
	 		  $this->load->view('dashboard/dashboard');
	 		  $this->load->view('templates/footer');

	 		}else{

	 			redirect('/');
	 		}
	 		
	 	}
	 	//this is the page for recovering account
	 	public function recoverAccount(){

	 		$data['username'] = $_POST['name'];
			$data['hint'] = $_POST['hint'];
			
			$return = $this->dashboard_model->adminLogin($data);

			if ($return != false) {
				
				$ret = $this->dashboard_model->accountRecovery($data);

				if ($ret != false) {
					
					$msg['msg'] = "True";
					$msg['id'] = $ret['id'];


				}else{

					$msg['msg']  = "Incorrect hint!";
				}

			}else{

				$msg['msg']  =  "Username not found!";
			}
	 		
	 		echo json_encode($msg);

	 	}
	 	/*getting the info of the admin to be displayed */
	 	public function adminInfo(){

	 		$info = $this->session->userdata('admin');
	 		extract($info);

	 		$ret = $this->dashboard_model->setAdminInfo($id);
	 		if($ret === false){

	 			echo "No active user!";
	 		}else{

	 			echo json_encode($ret);
	 		}

	 	}

	 	/*page for the list of admins*/
	 	public function admins(){

	 		if($this->session->userdata('admin')){
	 		
	 		
	 		  $this->load->view('templates/header');
	 		  $this->load->view('dashboard/admins');
	 		  $this->load->view('templates/footer');

	 		}else{

	 			redirect('/');
	 		}
	 		
	 	}
	 	//page for the management of the districts
	 	public function district(){

	 		if($this->session->userdata('admin')){

	 		 $this->load->view('templates/header');
	 		 $this->load->view('dashboard/district');
	 		 $this->load->view('templates/footer');

	 		}else{

	 			redirect('/');
	 		}
	 		
	 	}
	 	//page for the settings of the admin user
	 	public function settings(){

	 		if($this->session->userdata('admin')){

	 		 $this->load->view('templates/header');
	 		 $this->load->view('dashboard/settings');
	 		 $this->load->view('templates/footer');

	 		}else{

	 			redirect('/');
	 		}
	 		
	 	}
	 	//page for managing municipalities
	 	public function municipality(){

	 		if($this->session->userdata('admin')){
		 		$this->load->view('templates/header');
		 		$this->load->view('dashboard/municipality');
		 		$this->load->view('templates/footer');

	 		}else{

	 			redirect('/');
	 		}
	 	}
	 	//page for managing tourist spots
	 	public function touristSpots(){
	 		if($this->session->userdata('admin')){
		 		$this->load->view('templates/header');
		 		$this->load->view('dashboard/tourist_spots');
		 		$this->load->view('templates/footer');
	 		}else{

	 			redirect('/');
	 		}		
	 	}
	 	//page for managing establioshment/hotels
	 	public function establishment(){

	 		if($this->session->userdata('admin')){
		 		$this->load->view('templates/header');
		 		$this->load->view('dashboard/establishment');
		 		$this->load->view('templates/footer');
	 		}else{

	 			redirect('/');
	 		}		
	 	}
	 	//page for managing the categories of the tourist spots
	 	public function spotCategory(){
	 		if($this->session->userdata('admin')){

		 		$this->load->view('templates/header');
		 		$this->load->view('dashboard/spot_category');
		 		$this->load->view('templates/footer');

	 		}else{

	 			redirect('/');
	 		}	
	 	}
	 	//inserting new to spot to the database
	 	public function addSpot(){

	    $output = array('error' => false);
	    //check if the filename is not empty
        if(!empty($_FILES['file']['name'])){

        	//upload path of the file
            $config['upload_path'] = 'assets/images/';
            $config['file_name'] = $_FILES['file']['name'];
            //allwoed MIME type of the file
            $config['allowed_types'] = 'gif|jpg|png|jpeg';
            

            $this->load->library('upload', $config);
            $this->upload->initialize($config);
            
            //check if true uploading the file to the path
            if($this->upload->do_upload('file')){
                $uploadData = $this->upload->data();
                $filename = $uploadData['file_name'];

				$file['filename'] = $filename;
                //get the data from the users input
				$data['name'] = $_POST['name'];
				$data['municipality'] = $_POST['municipality'];
				$data['district'] = $_POST['district'];
				$data['category'] = $_POST['category'];
				$data['photo'] = $file['filename'];
				
				//call the add function in the model	
				$query = $this->dashboard_model->Add($data,'spots');
				//check if the return of query is not empty
				if($query != ""){
					
					$output['error'] = false;
					$output['message'] = 'Spot added successfully';

				}
				else{
					$output['error'] = true;
					$output['message'] = 'File uploaded but not inserted to database';
				}

            }else{

            	$output['error'] = true;
				$output['message'] = 'Cannot upload file';
				//$output['message'] = $_FILES['file']['name'];
            }

        }else{

        	$output['error'] = true;
			$output['message'] = 'Cannot upload empty file';
        }

        echo json_encode($output);

	 	}
	 	public function count(){
	 		 $tables = array(
	 		   'name' => array('spots',
			   'municipality',
			   'establishment',
			   'admin'
				)
	 		 );
	 		 $ret = "";
	 		
	 		 foreach($tables['name'] as $key => $value){

		 		$ret =$this->dashboard_model->counter($tables['name'][$key]) . " " . $ret;
	 		 	
	 		 }

	 		 echo $ret;
	 	}
	 	//signup admin
	 	public function signup(){

	    $output = array('error' => false);
	    //check if the filename is not empty
        if(!empty($_FILES['file']['name'])){

        	//upload path of the file
            $config['upload_path'] = 'assets/images/';
            $config['file_name'] = $_FILES['file']['name'];
            //allwoed MIME type of the file
            $config['allowed_types'] = 'gif|jpg|png|jpeg';
            

            $this->load->library('upload', $config);
            $this->upload->initialize($config);
            
            //check if true uploading the file to the path
            if($this->upload->do_upload('file')){
                $uploadData = $this->upload->data();
                $filename = $uploadData['file_name'];

				$file['filename'] = $filename;
                //get the data from the users input
				$data['name'] = $_POST['name'];
				$data['password'] = password_hash($_POST['password'], PASSWORD_DEFAULT);
				$data['hint'] = $_POST['hint'];
				$data['photo'] = $file['filename'];
				
				//call the add function in the model	
				$query = $this->dashboard_model->Add($data,'admin');
				//check if the return of query is not empty
				if($query != ""){
					
					$output['error'] = false;
					$output['message'] = $query;

				}
				else{
					$output['error'] = true;
					$output['message'] = 'Photo uploaded but not inserted to database';
				}

            }else{

            	$output['error'] = true;
				$output['message'] = 'Cannot upload photo';
				//$output['message'] = $_FILES['file']['name'];
            }

        }else{

        	$output['error'] = true;
			$output['message'] = 'Cannot upload empty photo';
        }

        echo json_encode($output);

	 	}

	 	public function login(){
	 			//$response = array('msg' => array());
			$data['username'] = $_POST['name'];
			$data['password'] = $_POST['password'];

			$return = $this->dashboard_model->adminLogin($data);
			

			if($_POST['name'] == ""){

				$ret['msg'] = "Username must not be empty!";

			}else if($_POST['password'] == ""){

				$ret['msg'] = "Password must not be empty!";

			}else{

				if($return != false){
					
					if(password_verify($_POST['password'], $return['password'])){
					
						$this->session->set_userdata('admin', $return);
						$ret['msg'] = 'Logging in...';
						$ret['login'] = 'True';


					}else{
							
						$ret['msg'] = "Password is incorrect!";
					}

				}else{

					$ret['msg'] = "Username not found!";
				}

			}

			echo json_encode($ret);
	 	}
	 	//inserting new category of tourist spots to the database
	 	public function addCategory(){
        
	 		if($_POST['category'] != ""){

	 			$data['name'] = $_POST['category'];
	 			$ret = $this->dashboard_model->Add($data,'spot_category');

	 		}else{

	 			$ret = "Category name must not be empty!";
	 		}
	 		

	 		echo $ret;

	 	}
	 	//inserting new district  to the database
	 	public function addDistrict(){

	 		if($_POST['name'] != ""){

	 			$data['name'] = $_POST['name'];
	 			$ret = $this->dashboard_model->Add($data,'district');

	 		}else{

	 			$ret = "District name must not be empty!";
	 		}
	 		
	 		echo $ret;

	 	}
	 	//inserting new establishment to the database
	 	public function addEstablishment(){

	 		if($_POST['name'] != "" && $_POST['location'] != "" && $_POST['rates'] != "" && $_POST['contact'] != ""){

	 			$data['name'] = $_POST['name'];
	 			$data['location'] = $_POST['location'];
	 			$data['rates'] = $_POST['rates'];
	 			$data['contact'] = $_POST['contact'];
	 			$ret = $this->dashboard_model->Add($data,'establishment');

	 		}else{

	 			$ret = "All fields must be filled up!";
	 		}
	 		
	 		echo $ret;

	 	}
	 	//inserting new muncipality to the database
	 	public function addMunicipality(){

	 		if($_POST['name'] != "" && $_POST['dist_id'] != ""){

	 			$data['name'] = $_POST['name'];
	 			$data['district_id'] = $_POST['dist_id'];
	 			$ret = $this->dashboard_model->Add($data,'municipality');

	 		}else{

	 			$ret = "All fields should be filled up!";
	 		}
	 		

	 		echo $ret;

	 	}

	 	//controller for the deleting of category of tourist spots
	 	function deleteCategory(){

	 		$ret = $this->dashboard_model->Delete($_POST['id'], 'spot_category');

	 		echo json_encode($ret);

	 	}
	 	//controller for the deleting of districts
	 	function deleteDistrict(){

	 		$ret = $this->dashboard_model->Delete($_POST['id'], 'district');

	 		echo json_encode($ret);

	 	}
	 	//controller for the deleting of establishment
	 	function deleteEstablishment(){

	 		$ret = $this->dashboard_model->Delete($_POST['id'], 'establishment');

	 		echo json_encode($ret);
	 	}
	 	//controller for the deleting of municipality
	 	function deleteMunicipality(){

	 		$ret = $this->dashboard_model->Delete($_POST['id'], 'municipality');

	 		echo json_encode($ret);

	 	}
	 	//controller for the deleting of tourist spots
	 	function deleteSpot(){

	 		$ret = $this->dashboard_model->Delete($_POST['id'], 'spots');

	 		echo json_encode($ret);
	 	}
	 	//controller for the editing the  category of tourist spots
	 	public function editCategory(){
	 		$data['name'] = $_POST['category'];
	 		$id = $_POST['id'];
	 		$ret = $this->dashboard_model->Edit($data,$id,'spot_category');

	 		echo $ret;

	 	}
	 	//controller for the editing the  districts
	 	public function editDistrict(){
	 		$data['name'] = $_POST['name'];
	 		$id = $_POST['id'];
	 		$ret = $this->dashboard_model->Edit($data,$id,'district');

	 		echo $ret;

	 	}
	 	//controller for the editing the name of the user
	 	public function editName(){
	 		$data['name'] = $_POST['name'];
	 		$id = $_POST['id'];
	 		$ret = $this->dashboard_model->Edit($data,$id,'admin');

	 		echo $ret;

	 	}
	 	//controller for the editing the  security like password and hint of the user
	 	public function editSecurity(){
	 		$data['password'] = password_hash($_POST['password'], PASSWORD_DEFAULT) ;
	 		$id = $_POST['id'];
	 		$ret = $this->dashboard_model->EditInfo($data,$id,'admin');

	 		echo $ret;

	 	}
	 	//controller for the editing the  profile
	 	public function editDp(){
	 		
	    $output = array('error' => false);
	    //check if the filename is not empty
        if(!empty($_FILES['file']['name'])){

        	//upload path of the file
            $config['upload_path'] = 'assets/images/';
            $config['file_name'] = $_FILES['file']['name'];
            //allwoed MIME type of the file
            $config['allowed_types'] = 'gif|jpg|png|jpeg';
            

            $this->load->library('upload', $config);
            $this->upload->initialize($config);
            
            //check if true uploading the file to the path
            if($this->upload->do_upload('file')){
                $uploadData = $this->upload->data();
                $filename = $uploadData['file_name'];

				$file['filename'] = $filename;
                //get the data from the users input
				$id = $_POST['id'];
				$data['photo'] = $file['filename'];
				
				//call the add function in the model	
				$query = $this->dashboard_model->EditInfo($data,$id,'admin');
				//check if the return of query is not empty
				if($query != ""){
					
					$output['error'] = false;
					$output['message'] = $query;

				}
				else{
					$output['error'] = true;
					$output['message'] = 'Photo uploaded but not inserted to database';
				}

            }else{

            	$output['error'] = true;
				$output['message'] = 'Cannot upload photo';
				//$output['message'] = $_FILES['file']['name'];
            }

        }else{

        	$output['error'] = true;
			$output['message'] = 'Cannot upload empty photo';
        }

        echo json_encode($output);
	 	}
	 	//controller for the editing establishment
	 	public function editEstablishment(){
	 		$data['name'] = $_POST['name'];
	 		$data['location'] = $_POST['location'];
	 		$data['rates'] = $_POST['rates'];
	 		$data['contact'] = $_POST['contact'];
	 		$id = $_POST['id'];
	 		$ret = $this->dashboard_model->Edit($data,$id,'establishment');

	 		echo $ret;

	 	}
	 	//controller for the editing the municipalities
	 	public function editMunicipality(){
	 		$data['name'] = $_POST['name'];
	 		$data['district_id'] = $_POST['dist_id'];
	 		$id = $_POST['id'];
	 		$ret = $this->dashboard_model->Edit($data,$id,'municipality');

	 		echo $ret;

	 	}
	 	//controller for the creating the new password of the user in  for recovering its account
	 	public function changePass(){
	 		$data['password'] = password_hash($_POST['password'], PASSWORD_DEFAULT);
	 		$id = $_POST['id'];

	 		if ($_POST['password'] == "") {
	 		     
	 		     $ret = "Password must not be empty";

	 		}else if ($_POST['password'] != $_POST['pass2']) {

	 			 $ret = "Password didn't matched!";

	 		}else{

	 			 $ret = $this->dashboard_model->newPassword($data,$id,'admin');
	 		}

	 		echo $ret;

	 	}
	 	//controller for the editing the  tourist spots
	 	public function editSpots(){
	
	 	$output = array('error' => false);
        //check if the filename is not empty
        if(!empty($_FILES['file']['name'])){

        	//upload path of the file
            $config['upload_path'] = 'assets/images/';
            $config['file_name'] = $_FILES['file']['name'];
            //allwoed MIME type of the file
            $config['allowed_types'] = 'gif|jpg|png|jpeg';
            

            $this->load->library('upload', $config);
            $this->upload->initialize($config);
            
            //check if true uploading the file to the path
            if($this->upload->do_upload('file')){
                $uploadData = $this->upload->data();
                $filename = $uploadData['file_name'];

				$file['filename'] = $filename;

				$data['name'] = $_POST['name'];
				$data['municipality'] = $_POST['municipality'];
				$data['district'] = $_POST['district'];
				$data['category'] = $_POST['category'];
				$data['photo'] = $file['filename'];
				$id = $_POST['id'];

				//call the function for editing
				$query = $this->dashboard_model->Edit($data,$id,'spots');
				if($query != ""){
					
					$output['error'] = false;
					$output['message'] = 'Spot changed successfully';

				}
				else{
					$output['error'] = true;
					$output['message'] = 'File uploaded but not inserted to database';
				}

            }else{
            	$output['error'] = true;
				$output['message'] = 'Cannot upload file';
				//$output['message'] = $_FILES['file']['name'];
            }
        }else{
        	$output['error'] = true;
			$output['message'] = 'Cannot upload empty file';
        }

        echo json_encode($output);

	 	}
	 	//getting the districts to be displayed in view
	 	public function getAdmin(){
	 		
	 		$ret = $this->dashboard_model->get('admin');

	 		echo json_encode($ret);
	 	}
	 	//getting the districts to be displayed in view
	 	public function getDistrict(){
	 		
	 		$ret = $this->dashboard_model->get('district');

	 		echo json_encode($ret);
	 	}
	 	//getting the category of tourist spots to be displayed in view
	 	public function getCategory(){

	 		$ret = $this->dashboard_model->get('spot_category');

	 		echo json_encode($ret);

	 	}
	 	//getting the establishment to be displayed in view
	 	public function getHotels(){

	 		$ret = $this->dashboard_model->get('establishment');

	 		echo json_encode($ret);

	 	}
	 	//getting the municipalities to be displayed in view
	 	public function getMunicipalities(){
	 		
	 		$ret = $this->dashboard_model->municipalities();

	 		echo json_encode($ret);
	 	}
	 	//getting the tourist spots to be displayed in view
	 	public function getSpot(){
	 		
	 		$ret = $this->dashboard_model->get('spots');

	 		echo json_encode($ret);
	 	}

	 	function logout(){
	 		$this->session->unset_userdata('admin');
			redirect('/dashboard');
	 	}

}