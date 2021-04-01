<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Main extends CI_Controller {

		function __construct(){
	 			parent::__construct();
				$this->load->helper('url');
				$this->load->library('session');
				$this->load->model('dashboard_model');
				$this->load->model('main_model');
			
	 	}
	 	/*index page of the web app*/
	 	function index(){}
	 		$this->load->view('templates/main_header');
	 		$this->load->view('index');
	 		$this->load->view('templates/main_footer');
	 	}
	 	function spotCategories(){
	 		$cat['cat'] = $_GET['cat'];
	 		$this->load->view('templates/main_header');

	 		$this->load->view('spot_categories', $cat);
	 		$this->load->view('templates/main_footer');
	 	}

	 	function searchResult(){

	 		$search['search'] = $_GET['search'];
	 		$this->load->view('templates/main_header');
	 		$this->load->view('search_result', $search);
	 		$this->load->view('templates/main_footer');
	 		
	 	}
	 	function touristSpots(){

	 		$this->load->view('templates/main_header');
	 		$this->load->view('tourist_spots');
	 		$this->load->view('templates/main_footer');

	 	}
	 	function hotels(){
	 		
	 		$this->load->view('templates/main_header');
	 		$this->load->view('hotels');
	 		$this->load->view('templates/main_footer');

	 	}
	 	function search(){
	 		$search = $_POST['search'];
	 		$ret = $this->main_model->searchResult($search);

	 		if($ret != false){

	 			echo json_encode($ret);

	 		}else{

	 			echo "False";
	 		}
	 	}




}