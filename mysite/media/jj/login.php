<div id="loginSignup" >

	<div class="signup-form" v-if="signup">
		
	   <div class="form">
	   <h4 class="signup-label">Admin Sign Up</h4>
	     <h6 class="text-center error" v-if="message">{{message}}</h6>
	     <h6 class="text-center success" v-if="registered">{{registered}}</h6>
		 <label>Username</label><br>
		 <input type="text" class="form-input" @keyup="nameMonitor()" v-model="signupDetails.name" placeholder="Username...">
		 <i class="error" v-if="errors.name">{{errors.name}}</i><br>

		 <label class="mt-2">Password</label><br>
		 <input type="password" class="form-input" @keyup="pass1Monitor()"  v-model="signupDetails.password" placeholder="Password...">
		  <i class="error" v-if="errors.pass">{{errors.pass}}</i><br>

		 <label class="mt-2">Re-type Password</label><br>
		 <input type="password" class="form-input" @keyup="pass2Monitor()" v-model="signupDetails.pass2" placeholder="Re-type Password...">
		 <i class="error" v-if="errors.pass2">{{errors.pass2}}</i>
		 <i class="success" v-if="success">{{success}}</i><br>

		 <label class="mt-2">Hint</label><br>
		 <input type="text" class="form-input" @keyup="hintMonitor()" v-model="signupDetails.hint" placeholder="Hint...">
		 <i class="error" v-if="errors.hint">{{errors.hint}}</i><br>
		 
		 <label class="mt-2">Photo</label><br>
		 <input type="file" class="photo" id="file"  ref="file" v-on:change="handleFileUpload()" class="form-control-file border">

		 <button class="signup" @click="register()" >Sign Up <span class="fa fa-sign-out"></span></button>

		 <button class="already-have"  @click="signup = false;login = true;"  v-b-tooltip.hover title="Login">Already have an account?</button>

	  </div>
	 
	</div>

	<div class="login-form" v-if="login">
		
	 <div class="form">
	   <h4 class="signup-label">Admin Login</h4>
	     <h6 class="text-center error" v-if="message">{{message}}</h6>
		 <label>Username</label><br>
		 <input type="text" v-model="loginDetails.name" @keyup="loginMonitor()" class="form-input" placeholder="Username...">

		 <label class="mt-2">Password</label><br>
		 <input type="password" class="form-input" @keyup="loginMonitor()" v-model="loginDetails.password" placeholder="Password...">

		 <button class="login" @click="loginAdmin()">{{login_text}}<span class="fa fa-sign-out"></span></button>

		 <button class="already-have" @click="login = false; signup = true;"  v-b-tooltip.hover title="Sign Up">Don't have an account?</button>

		 <a href="<?php echo base_url();?>index.php/dashboard/recover" class="forgot"  v-b-tooltip.hover title="Recover Password">Forgot Password?</a>
	  </div>
	 
	</div>

</div>