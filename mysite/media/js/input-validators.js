const stringOnly = /^[a-zA-Z ]+$/;

exports.nameChecker = (name) => 
			{

				if(name.match(stringOnly)){
					return true;
				}else if(name.length <= 7){
					return "Name must contain at least 8 letters!";
				}else{
					 return false;
				}

			}
exports.passwordChecker = (password) => {
			if(password.length >= 8){
				return true;
			}else{
				return false;
			}

}