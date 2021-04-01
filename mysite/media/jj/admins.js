var url = "http://localhost/LTIPC/";
	
	var admin = new Vue({
		el: "#admin",
		data: {
			admins: []
		},
		mounted: function(){

			this.getAdmin();
		},
		methods: {
			getAdmin: function(){

				axios.post(url+"index.php/dashboard/getAdmin").then(function(response){
					
				     dashboardHomePage.admins = response.data;
				    

				});

			},
			
		}

	});