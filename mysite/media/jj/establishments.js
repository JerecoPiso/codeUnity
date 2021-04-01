var url = "http://localhost/LTIPC/";

	var establishment = new Vue({
		el: "#establishment",
		data: {
			modal: false,
			modalDelete: false,
			modalEdit: false,
			message: '',
			establishmentInfo: {id: '',name: '', location: '', rates: '', contact: ''},
			hotels: [],
			photo: '',
			file: ''
		},
		mounted: function(){

			this.getHotels();
		},	
		methods: {

			FileUpload(){
		        this.photo = this.$refs.filess.files[0];
			},
			EditFileUpload(){
		        this.file = this.$refs.file.files[0];
			},
			     
			 addEstablishment: function(){

				
				let formData = new FormData();
	            formData.append('file', this.photo);
	            formData.append('name', establishment.establishmentInfo.name);
	            formData.append('location', establishment.establishmentInfo.location);
	            formData.append('rates', establishment.establishmentInfo.rates);
	            formData.append('contact', establishment.establishmentInfo.contact);
	        

				axios.post(url+"index.php/uploader/addEstablishment",formData).then(function(response){

					
					establishment.message = response.data.message;
					establishment.getHotels();
					establishment.clear();
				});

			},

			deleteEstablishment: function(){

				var id = district.toFormData(establishment.establishmentInfo);

				axios.post(url+"index.php/dashboard/deleteEstablishment", id).then(function(response){

					establishment.message = response.data;
					establishment.getHotels();

				});

			},

			editEstablishment: function(){
				

				let formData = new FormData();
	            formData.append('file', this.file);
	            formData.append('name', establishment.establishmentInfo.name);
	            formData.append('location', establishment.establishmentInfo.location);
	            formData.append('rates', establishment.establishmentInfo.rates);
	            formData.append('contact', establishment.establishmentInfo.contact);
	            formData.append('id', establishment.establishmentInfo.id);
	        

				axios.post(url+"index.php/uploader/editEstablishment",formData).then(function(response){

					
					establishment.message = response.data.message;
					establishment.getHotels();

				});


			},

	
			getHotels: function(){

				axios.get(url+"index.php/dashboard/getHotels").then(function(response){

					establishment.hotels = response.data;

				});
			},

			clear: function(){

					establishment.establishmentInfo.name = "";
					establishment.establishmentInfo.location = "";
					establishment.establishmentInfo.rates = "";
					establishment.establishmentInfo.contact = "";
			}

		}

	});
