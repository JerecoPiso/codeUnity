const express = require("express");
const router = express.Router();
const conn = require("./conn.js");
router.get("/", (req, res) => {
	var show;
	if(req.session.to_show == null){
		show = true;
	}else{
		show = false;
	}
    res.render("index",{ success: req.session.success,
    					 err: req.session.err,
    					 form_condition: show,
    					 err_signup: req.session.err_signup


    					}
    		   );
    //set this sessions values to null
    req.session.err = null;
    req.session.err_signup = null;
    req.session.to_show = null;
    req.session.success = null;

});
//router for the chatroom
router.get("/chatroom", (req, res) => {

	if(req.session.loggin == true){

		res.render("chatroom",{
			name: req.session.name,
    		id: req.session.user_id,
    		photo: req.session.photo
		});

	}else{
		res.redirect("/");
	}
	
});
router.get("/getUsers", (req, res) => {
	  var sql = "SELECT * FROM users WHERE users_id != ? AND status = ?";
	  var id = req.session.user_id;
	  var status = "active";
     conn.query(sql, [id, status], (err,results) => {
                     
       if(err) throw err;
                     

        if(results.length <= 0){

             res.send("No users");

        }else{
        	 var query = "SELECT COUNT(*) FROM messages WHERE sender_id = ? AND receiver_id = ? AND status = ?";
        	 var receiver = req.session.user_id;
        	 var status = "unseen";
        	 var ctr = 0;
        	// var haha;
        	 for(var i in results){
			
        	 	conn.query(query, [results[i].users_id, receiver, status], function(err, rows, fields){
        	 		
        	 	
        	 				 results[ctr++].msg_ctr = rows[0]['COUNT(*)'].toString();
        	 				 if(ctr === results.length){
        	 				 		//console.log(results)
       			 					 res.send(results);
        	 				 }

        	 	});
        	
        	 }
        	 	
          
        }

    });
});
router.post("/getMessages", (req, res) => {
	var sender = req.body.sender;
	var receiver = req.body.receiver_id;
	var sql = "SELECT * FROM messages WHERE sender_id = ? AND receiver_id = ? OR sender_id = ? AND receiver_id = ?";

	conn.query(sql,[sender, receiver, receiver, sender], function(err, results){
		if(err) throw err;
		if(results.length <= 0){
			res.send(false);
		}else{
			 var status = "seen";
			var query = "UPDATE messages SET status = ? WHERE sender_id = ? AND receiver_id = ?";
			 conn.query(query, [status, receiver, sender], function(err, results){

				if(err) throw err;			

			})

			res.send(results);
		}
	})

});

router.post("/getNewMessages", (req, res) => {
	var sender = req.body.sender;
	var receiver = req.body.receiver_id;
	var last_id = req.body.last_id;
	 var check_last_id = "SELECT message_id  FROM messages WHERE  sender_id='"+sender+"'AND receiver_id='"+receiver+"' OR receiver_id='"+sender+"'AND sender_id='"+receiver+"' ORDER BY message_id DESC LIMIT 1";
       var last;
       conn.query(check_last_id, (error, results) => {
           
           if (error) throw error;

           for(var i in results){
            last = results[i].message_id;
           }
           
           if(last == req.body.last_id){
              
              res.send("None");

           }else{

           		var sql = "SELECT * FROM messages WHERE sender_id = ? AND receiver_id = ? OR sender_id = ? AND receiver_id = ?";

					conn.query(sql,[sender, receiver, receiver, sender], function(err, results){
						if(err) throw err;
						if(results.length <= 0){
							res.send(false);
						}else{
							 var status = "seen";
							var query = "UPDATE messages SET status = ? WHERE sender_id = ? AND receiver_id = ?";
							 conn.query(query, [status, receiver, sender], function(err, results){

								if(err) throw err;			

							})

							res.send(results);
						}
					})

           }

	});
});
router.post("/sendMessage", (req, res) => {
	var msg = req.body.message;
	var sender = req.body.sender;
	var receiver = req.body.receiver_id;
	var status = "unseen";
	var sql = "INSERT INTO messages (message, sender_id, receiver_id, status) VALUES (?,?,?,?)";
	conn.query(sql, [msg, sender, receiver, status], function(err, results){
		if(err) throw err;

		if (results.affectedRows == 1) {
			res.send("Sended");
		}else{
			res.send("Unable to send!");
		}
	});
});

//logout
router.get("/logout", (req, res) => {
	
	  var sql = "UPDATE users SET status = ? WHERE users_id = ?";
	  var id = req.session.user_id;
	  var status = "";
	conn.query(sql, [status, id], (error, results) => {

		if (error) throw err;

	})
	req.session.loggin = false;
	res.redirect("/");
});
module.exports = router;