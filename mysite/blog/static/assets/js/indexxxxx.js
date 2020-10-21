var signup = new Vue({
	delimiters: ['[', ']'],
	el: "#signup",
	data:{
		signupInfo: {email: '', password: '', password2: ''},
		error: '',
		success: ''
	},
	mounted: function(){
		// alert($('input[name=csrfmiddlewaretoken]').val())
	},
	methods: {
		register: function(){

			if((signup.signupInfo.email && signup.signupInfo.password && signup.signupInfo.password2) != ""){
				if(signup.signupInfo.password.length < 7){
					signup.error = "Password must contain at least 8 characters!";
				}else if(signup.signupInfo.password != signup.signupInfo.password2){
					signup.error = "Password didn't matched!";
				}else{

					 var data = signup.toFormData(signup.signupInfo);
					axios.post("register", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
						if(response.data != "Registered successfully"){
							signup.error = response.data;
						}else{
							signup.success = response.data

							setTimeout(function(){							
								signup.success = "";
								signup.signupInfo.email = ''
								signup.signupInfo.password2 = ''
								signup.signupInfo.password = ''
							}, 5000)

						}
						
					})
				}	
				
			}else{
			 		signup.error =	"All fields must be filled up!";
			}
			
			setTimeout(function(){
							signup.error = "";
							
						}, 5000)

		},

		 toFormData: function(obj){
            var form_data = new FormData();
            for(var key in obj){
                form_data.append(key, obj[key]);
            }
            return form_data;
      },
	}
})