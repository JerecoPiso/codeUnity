const express = require("express");
var validators = require("./input-validators.js");
const app = express.Router();
const conn = require("./conn.js");
app.post("/login", (req, res) => {


	if(req.method == "POST"){
		var uname = req.body.name;
		var pass = req.body.password;

		if(pass != ""  && uname != ""){

			conn.query("SELECT * FROM users WHERE username = ?", [uname], function(err, results, fields){
			
				if(results.length > 0){
					
					for(var i in results){
						if(pass == results[i].password){
						 	req.session.loggin = true;
						 	req.session.name = uname;
						 	req.session.user_id = results[i].users_id;
						 	req.session.photo =  results[i].photo;
						 	var sql = "UPDATE users SET status = ? WHERE users_id = ?";
						 	var status = "active";
						 	var id = results[i].users_id;

						 	conn.query(sql,[status, id], function(error, results){

						 		if(err) throw err;


						 	})
						 	res.redirect("/chatroom");
						 }else{

						 	req.session.err = "Incorrect password!";
						 	res.redirect("/");
						 }
					}

				}else{
					req.session.err = "No username found!";
					res.redirect("/");
				}
			});
		}else{
			req.session.err = "All fields must be filled up!";
			res.redirect("/");
		}
		
	}

});
app.post("/signup", (req, response) => {
	var date = new Date();
	var months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"];
    var month = months[date.getMonth()];
    var date_send = month+" "+date.getDate()+" "+date.getFullYear();

	var name = req.body.username;
	var pass = req.body.signup_password;
	var pass2 = req.body.password_two;
	if (req.method == "POST") {

		 if (!req.files){

		 		req.session.err_signup = "No files were uploaded!";
			 	req.session.to_show = false;
			 	response.redirect('/')
		 } 

			
		var file = req.files.uploaded_image;
	
		var position = file.name.lastIndexOf(".");
		var extension = file.name.substring(position, file.name.length);
		//var 
        
         var img_name = file.md5+extension;
      

	  	 if(file.mimetype == "image/jpeg" ||file.mimetype == "image/png"||file.mimetype == "image/gif" ){
             
             //validate name
       		 var ret = validators.nameChecker(name);
    		 if(ret === true){
    		 	//validate password
    		 	var pass_valid = validators.passwordChecker(pass);
    		 	if(pass_valid === true){
    			if(name != "" && pass != "" && pass2 != ""){
    				
					var sqll = "SELECT COUNT(username) FROM users WHERE username = '"+name+"'";
				 	var query = conn.query(sqll, function(error, rows, fiels){

				 		if (error) throw error;
						
						if(rows[0]['COUNT(username)'] > 0){

							 req.session.err_signup = "Username already exist!";
							 req.session.to_show = false;
							 response.redirect('/')

						}else{

		 				if(pass == pass2){

							var sql = "INSERT INTO users (username, password, photo) VALUES (?,?,?)";
							conn.query(sql, [name, pass, img_name],function(err, res, fields){

								if (err) {

									 req.session.err_signup = "An error occurred!";
							      	 req.session.to_show = false;
								     response.redirect('/')

				 			     }else{
				 			     	//save image
				 			     	 file.mv('public/images/'+img_name, function(err) {
                             
							              if (err){
							              	 req.session.err_signup = "An error has occured!";
								 			 req.session.to_show = false;
								 			 response.redirect('/')

							              }

		             				 });

				 			      	 req.session.success = "Signup successfully";
							      	 req.session.to_show = false;
									 response.redirect('/')

								}

							})

						}else{

					 		     req.session.err_signup = "Password didn't matched!"
				 				 req.session.to_show = false;
								 response.redirect('/')
								
								}
								
							}///

					 	})

				////////////
					 }else{	
						    req.session.err_signup = "All fields must be filled up!"
						    req.session.to_show = false;
							response.redirect('/')				
					}


					}else{
							  req.session.err_signup = "Password is too short!"
						    req.session.to_show = false;
							response.redirect('/')				
					}


					}else if(ret === false){

						  req.session.err_signup = "Name must contain only letters!"
						  req.session.to_show = false;
						  response.redirect('/')		

					}else{

						  req.session.err_signup = "Name is too short!"
						  req.session.to_show = false;
						  response.redirect('/')		
					}
			
          } else {
          	           
            	req.session.err_signup =  "This format is not allowed , please upload file with '.png','.gif','.jpg'";
		 	    req.session.to_show = false;
		 		response.redirect('/')
      
          }
		
	}
						
});

module.exports = app;