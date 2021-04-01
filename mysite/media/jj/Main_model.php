<?php
	
	class Main_model extends CI_Model{

		function __construct(){
			parent::__construct();
			$this->load->database();		
		}
		

		function select($table,$spot){

			$this->db->where($table.'.category', $spot);
			$ret = $this->db->get($table);

			
			if($ret->num_rows() > 0){

				return $ret->result();

			}else{

				return false;
			}

		}

		public function searchResult($search){


			$this->db->like('spots.name', $search, 'both');

			$this->db->or_like('spots.municipality', $search, 'both');
			$this->db->or_like('spots.district', $search, 'both');
			$this->db->or_like('spots.category', $search, 'both');
			
			$ret = $this->db->get('spots');

			if($ret->num_rows() > 0){

				return $ret->result();

			}else{

				return false;
			}


		}
	}