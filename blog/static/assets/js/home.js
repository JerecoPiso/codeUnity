var signup = new Vue({
	delimiters: ['[', ']'],
	el: "#signup",
	data:{
		signupInfo: {username: '', email: '', password: '', password2: ''},
		error: '',
		// success: '',
		// status: 'Signup'
		btnDisable: '',
		stringOnly: /^[a-zA-Z ]+$/,
		numbersOnly: /^[0-9]+$/
	},
	mounted: function(){
		this.btnDisable = true
		$('.btn-signup').css({'opacity': '0.7'})
	},
	methods: {
		disable: function(){
			this.btnDisable = true
			$('.btn-signup').css({'opacity': '0.7'})
		
		},
		usernameMonitor: function(event){
			const key = event.key
			
			if(!key.toString().match(signup.stringOnly)){
				newname = this.signupInfo.username
				this.signupInfo.username = newname.substr(0,newname.length-1)
			}else{
				this.finalChecker()
			}
			

		},
		emailMonitor: function(event){
			
			this.finalChecker()
			

		},
		passwordMonitor: function(event){
			
			if(signup.signupInfo.password.length < 8){
				
				this.error = "Password must contain at least 8 characters!"
				$(".error").show()
				this.disable()
				
			}else if((this.signupInfo.password.match(signup.numbersOnly) || this.signupInfo.password.match(signup.stringOnly))){
		
				this.error = "Password must contain letters and numbers!"
				$(".error").show()
				this.disable()

			}else{
				this.error = ""
				$(".error").hide()
				if(!this.signupInfo.password2 == "" && this.signupInfo.password2.length >= 8){

					if((signup.signupInfo.email && signup.signupInfo.username && signup.signupInfo.password2) != ""){			
						
						this.btnDisable = false
						$(".btn-signup").css({'opacity': '1'})
					}
						this.error = ""
						$(".error").hide()
						
				}
				
			}
			if(event.key == " "){
				newpass = this.signupInfo.password
				this.signupInfo.password = newpass.substr(0,newpass.length-1)
				this.error = "Password must not contain a whitespace!"
				$(".error").show()
			
			}
		},
		password2Monitor: function(event){
				if(this.signupInfo.password != ""){
					

						if(this.signupInfo.password2 == ""){
							this.error = "Password didn't matched!"
							$(".error").show()
							this.disable()

							

						}else if(this.signupInfo.password2.length < 8){
							this.error = "Password didn't matched!"
							$(".error").show()
							this.disable()
							

						
						}else{
						
							if((this.signupInfo.password.length < 8)){
									this.error = "Password must contain at least 8 characters!"
									$(".error").show()
									this.disable()
									
							}else if((this.signupInfo.password.match(this.numbersOnly) || this.signupInfo.password.match(this.stringOnly))){
								
									this.error = "Password must contain letters and numbers!"
									$(".error").show()
									this.disable()

							}else{
								$(".error").hide()
								this.finalChecker()
							}
						}	
						
					// }
				

				}
				
		
				
		},
		finalChecker: function(){
			if(this.signupInfo.password == this.signupInfo.password2){
							if((signup.signupInfo.email && signup.signupInfo.password && signup.signupInfo.username && signup.signupInfo.password2) != ""){			
								this.btnDisable = false
								$(".btn-signup").css({'opacity': '1'})
								this.error = ""
								$(".error").hide()
							}else{
								this.disable()
							}
							
						}else{
							this.error = "Pasword didn't matched!"
							$(".error").show()
							this.disable()
						}
		}
	
	

	}
})
