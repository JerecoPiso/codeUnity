var signup = new Vue({
	delimiters: ['[', ']'],
	el: "#signup",
	data:{
		signupInfo: {username: '',email: '', password: '', password2: ''},
		error: '',
		success: '',
		status: 'Signup'
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
					axios.post("register", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}}).then(function(response){
						
							if(response.data != "Success"){
								signup.error = response.data;
								setTimeout(function(){
									signup.error = "";
												
								}, 2000)
							}else{
								$("#btn-signup").css({'opacity': '0.6'})
								signup.status = 'Redirecting...'
								setTimeout(function(){
									window.location.href = "verify"
								}, 2000)
								
							}
						
					})
				}	
				
			}else{
			 		signup.error =	"All fields must be filled up!";
			}
			
			

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
	var verify = new Vue({
		el: "#verify",
		data:{
			verifyInfo: {code: ''}
		},
		methods:{
			verify: function(){
				let data = verify.toFormData(verify.verifyInfo)
				axios.post('verified', data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}}).then(function(resp){
					// if(resp.data == "Correct"){
					// 	window.location.href = "/user"
					// }else{
					// 	alert(resp.data)
					// }
					alert(resp.data)
				})
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

var login = new Vue({
		delimiters: ['[', ']'],
		el: "#login",
		data: {
			loginInfo: {email: '', password: ''},
			error: '',
			success: ''
		},
		methods:{
			loginUser: function(){
				var fd = login.toFormData(login.loginInfo)
				axios.post('userLogin', fd , {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}}).then(function(response){
					
					if(response.data == "Success"){
						login.success = "Redirecting . . ."
						window.location.href = '/user'
					}else{
						login.error = response.data
					}
				})
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