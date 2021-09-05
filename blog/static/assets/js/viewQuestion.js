
var my_component = {
	delimiters: ['[', ']'],
	props:{
		
		posted: String
	},
	data: function(){
		return {
			post: this.posted,
			date: ''
		}
	},
	created: function(){

		this.date = this.getDate(this.post)


	},
	methods: {
		getDate: function(val){
			var now = moment().year()+"-"+(moment().month()+1)+"-"+moment().date()+" "+moment().hour()+":"+moment().minutes()+":"+moment().seconds() 
			var currDate = moment(now)
			var dateToTest = moment(val);				 
			var years = currDate.diff(dateToTest, 'years')
			var months = currDate.diff(dateToTest, 'months')
			var weeks = currDate.diff(dateToTest, 'weeks')
			var days = currDate.diff(dateToTest, 'days')
			var hours = currDate.diff(dateToTest, 'hours')
			 var minutes = currDate.diff(dateToTest, 'minutes')
			   // check year if less than or equal to 1
			   if(years <= 1){
					 // check months if less than 1
					 if (months < 12) {
							 // check if months is less than or equal to 1
						   if(months <= 1){
							   // check if weeks
							   if (weeks > 4) {
								   return(months+" month ago")
							   // check if weeks is greater than 1 and less than 5
							   }else if (weeks > 1 && weeks < 5){

								   return(weeks+" weeks ago")

							   }else{
								   // check if weeks is equal to 1 and days is equal to 7
								   if (weeks == 1 && days == 7) {

									   return(weeks+" week ago")

								   }else{
									   // check if days is greater than 1 and days is less than 7
									   if (days > 1 && days < 7) {
										   return(days+" days ago")
									   }else{
										   // check if days is equal to 1 and hours is equal to 24
										   if(days == 1){
										   
											   return(days+" day ago")
											   
										   }else{

											   if(hours > 1 && hours < 24){
												   return(hours+" hours ago")
											   }else if(hours >= 24){
												 var day = hours/24

													   if(Math.floor(day) > 1){
														   return(Math.floor(day)+" days ago")
													   }else{
														   return(Math.floor(day)+" day ago")
													   }

											   }else{

												   if(minutes == 60 && hours == 1){
													   return(hours+" hour ago")
												   }else if(minutes >= 60){
													   var hour = minutes/60

													   if(Math.floor(hour) > 1){
														   return(Math.floor(hour)+" hours ago")
													   }else{
														   return(Math.floor(hour)+" hour ago")
													   }

												   }else{
													   if (minutes > 1 && minutes == 60) {
														   return(minutes+" minutes ago")
													   }else{
														   if(minutes == 1){
															return(minutes+" minute ago")
														   }else if(minutes == 0){
															return("now")
														   }else{
															return(minutes+" minutes ago")
														   }
														   
													   }
												   }
											   }
											   
										   }
									   
									   }
								   }
								   
							   }

						   }else{
							   return(months+" months ago")
						   }
					   }else{
						   return(years+" year ago")
					   }
			   }else{
					   return(years + " years ago")
			   }
			   
		}
	},
	template: "<span> ( [date] )  </span>"

}
	var comments = new Vue({
	  delimiters: ['[', ']'],
	  el: "#comment-section",
	  components: {
        "date-posted": my_component
    },
	  data(){
		  return{
			code: String,
			commentInfo: [],
			commentTotal: 0,
			// comment
			comment: '',
			// text area for the code
			editor: false,
			
			replies: [],
			// comment id
			comId: '',
			// post id
			srcImg: '/media/',
			flashMsg: '',
			// used to hide and show the reply popup box
			// replyModal: false,
			replyInfo: {question_id: '', comment_id: '', commentor_id: '', reply: ''},
			setAnswerInfo: {question_id: '',category: '', id: ''},
			// reply id
			replyId: '',
			// question id
			qID: '',
			// the modal 
			// popUpAlert: false,
			// what action to perform in the modal 
			actionToPerform: '',
			// extension for the message in the modal content on which data will be deleted
			promptMsgExtension: '',
			btnDisable: true,
			questionId: '',
		
			lang: String,
			commentIndex: 0,
			replyClass: "haha",
			viewQuestion: '',
			// limit the shown reply
			lim: [],
			showCheckMark: []
		
	}

	  },
	  mounted: function(){
		//   console.log(this.lim[0])
		this.qID = $("#post-id").val()
		// alert($("#post-id").val())
		this.getComments($("#post-id").val())
		this.getReplies($("#post-id").val())
		
		this.lang = $("#lang").val()
	  },
	
	  methods:{
		  setAnswer: function(index){
			//   alert(comments.setAnswerInfo.category)
			
			let data = new FormData()

			data.append("id", comments.setAnswerInfo.id)
			data.append("category", comments.setAnswerInfo.category)
			data.append("question_id", comments.setAnswerInfo.question_id)
			axios.post("/setAnswered", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}} ).then(function(response){
				
				if(response.data === "Done"){
					
					comments.flashMsg = "The commented code has been set as answer to the question."
					
				}else{
					comments.flashMsg = "Something went wrong!"
				}
				$(".flash-msg").show()

				
				if(comments.showCheckMark[index] == 'false'){
					Vue.set(comments.showCheckMark,index,'true')
				}else{
					Vue.set(comments.showCheckMark,index,'false')
				}
				setTimeout(function(){
					comments.flashMsg = ""
					$(".flash-msg").hide()
				}, 5000)
			}).catch(function(err){
				console.log(err)
			})
		  },
		  setUnanswered: function(index){
			//   alert(comments.setAnswerInfo.category)
			let data = new FormData()

			data.append("id", comments.setAnswerInfo.id)
			data.append("category", comments.setAnswerInfo.category)
			data.append("question_id", comments.setAnswerInfo.question_id)
			axios.post("/setUnanswered", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}} ).then(function(response){
					
			
				if(comments.showCheckMark[index] == 'true'){
					Vue.set(comments.showCheckMark,index,'false')
				}else{
					Vue.set(comments.showCheckMark,index,'true')
				}
		
			}).catch(function(err){
				console.log(err)
			})
				
		  },
		  showHideDeleteModal(status){
			if(status == "show"){
				$("#deleteModall").show()
			}else{
				$("#deleteModall").hide()
			}
		  },
		  showHideReplyModal(status){
			if(status == "show"){
				$("#replyModall").show()
			}else{
				$("#replyModall").hide()
			}
			
			
		  },
		  limitShownReply(index){
			if(this.lim[index] == 'false'){
				Vue.set(this.lim,index,'true')
			}else{
				Vue.set(this.lim,index,'false')
			}
			
		  },
		 
		  reply(com,id){
			  let newReplies = []
					for(var i = 0; i < com.length; i++){
						if(com[i].comment_id == id){
							newReplies.push(com[i])
						}
					
					}
				
			  	return newReplies
				

		  },
		highlighter: function(code) {
			// alert(comments.code)
			// var inp = code.replace(/<(style|script|iframe)[^>]*?>[\s\S]+?<\/\1\s*>/gi,'').replace(/<[^>]+?>/g,'').replace(/\s+/g,' ').replace(/ /g,' ').replace(/>/g,' '); 
		 	 return Prism.highlight(code, Prism.languages.js, this.lang);
		},
		  	// adding reply
		  secComment: function(){
			 let data = new FormData()
			 var now = moment().year()+"-"+(moment().month()+1)+"-"+moment().date()+" "+moment().hour()+":"+moment().minutes()+":"+moment().seconds() 
			 data.append("post_id", comments.replyInfo.question_id)
			 data.append('comment_id', comments.replyInfo.comment_id)
			 data.append('commentor_id', comments.replyInfo.commentor_id)
			 data.append('reply', comments.replyInfo.reply)
			 data.append('date', now)
			 axios.post("/reply", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
				comments.flashMsg = response.data
				$(".flash-msg").show()
				comments.replyInfo.reply = ""
				comments.replyModal = false
				comments.getComments(comments.qID)
				comments.getReplies(comments.qID)
				setTimeout(function(){
					comments.flashMsg = ""
					$(".flash-msg").hide()
				}, 5000)
				comments.showHideReplyModal('hide');
				var getTotalComment = $("#totalComments").text()
			 	 $("#totalComments").text(Number(getTotalComment)+1)
			 })
		
		  },
		  	// adding comment
		  addComment: function(post_id){
			//   console.log(app.$options)
			  var code = $("#summernote").summernote('code')
			  var now = moment().year()+"-"+(moment().month()+1)+"-"+moment().date()+" "+moment().hour()+":"+moment().minutes()+":"+moment().seconds() 
				
			    let data = new FormData()
				data.append("comment", comments.comment)
				// alert(code)
				// var dom = new DOMParser()
				// var doc = dom.parseFromString(code, 'html')
				data.append("date", now) 
				data.append("post_id", post_id) 
				
			  if(code != "<p><br></p>"){
				
				data.append("answer", code)
			  }else{
				data.append("answer", "")
			  }

			  axios.post("/addComment", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
				$("#summernote").summernote('reset')
				comments.comment = ""
				comments.flashMsg = response.data
				$(".flash-msg").show()
				comments.getComments(post_id)
				comments.getReplies(comments.qID)
				setTimeout(function(){
					comments.flashMsg = ""
					$(".flash-msg").hide()
				}, 5000)
				
			  })
			  var getTotalComment = $("#totalComments").text()
			  $("#totalComments").text(Number(getTotalComment)+1)
		  },
		  	// deleting comment
		  deleteComment: function(post_id){
			var toDeleteReplyCtr = 0
			let data = new FormData()
	
			data.append("id", comments.comId)
		
			data.append("post_id", comments.questionId)
			
		
			axios.post("/deleteComment", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
				comments.flashMsg = response.data
				$(".flash-msg").show()
				comments.commentInfo.splice(comments.commentIndex,1)
				comments.getReplies(comments.qID)
				setTimeout(function(){
					comments.flashMsg = ""
					$(".flash-msg").hide()
				}, 5000)
		
				for(var i = 0; i < comments.replies.length; i++){
					if(comments.replies[i].comment_id == comments.comId){
						toDeleteReplyCtr++;
					}
					
				}
				comments.showHideDeleteModal('hide');
				var getTotalComment = $("#totalComments").text()
			 	$("#totalComments").text(Number(getTotalComment)-(1+toDeleteReplyCtr))
			  })
		  },
		  	// deleting reply
		  deleteReply: function(){
			let data = new FormData()
			
			data.append("id", comments.replyId)
			
			data.append("post_id", comments.questionId)
			axios.post("/deleteReply", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
				
				comments.flashMsg = response.data
				$(".flash-msg").show()
				comments.getComments(comments.qID)
				comments.replies.splice(comments.commentIndex,1)
				// comments.getReplies(comments.qID)
				setTimeout(function(){
					comments.flashMsg = ""
					$(".flash-msg").hide()
				}, 5000)
				comments.showHideDeleteModal('hide');
				var getTotalComment = $("#totalComments").text()
			 	 $("#totalComments").text(Number(getTotalComment)-1)
			   })
		  },
		  	// getting comments
		  getComments: function(id){
			  let data = new FormData()
			  data.append("question_id", id)
			  
			axios.post("/getComment", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
				
				comments.commentInfo = response.data
				comments.showCheckMark = []
				comments.commentTotal = comments.commentInfo.length
				for(var i=0;i < comments.commentInfo.length;i++){
					
				
					if(comments.commentInfo[i].status == ""){
						comments.showCheckMark.push('false')
					}else{
						comments.showCheckMark.push('true')
					}
					comments.lim.push('false')
					
				}
			
			  })
		  },
		  	// getting replies
		  getReplies: function(id){
			  let data = new FormData()
			  data.append("question_id", id)
			  
			axios.post("/getReply", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
			
				 comments.replies = response.data
			
			
			  })
		  },
		  	// what delete function will be executed
		  toDelete: function(){
				if(comments.actionToPerform == "deleteComment"){
					comments.deleteComment(comments.questionId)
					
				}else{
					comments.deleteReply()
				}
				setTimeout(function(){
					comments.popUpAlert = false
				}, 800)
		  },
		 
	  }
  })
  var app = new Vue({
    delimiters: ['[', ']'],
    el: "#app",
    data: function(){
        return{
            ques_code: '',
            lang: '',
            
            
        }
        
    
    },
    
    mounted: function(){
        this.ques_code = $("#cd").val()
        this.lang = $("#lang").val()
        // this.commentTotal = comments.commentTotal
        // alert(this.commentTotal)
        // alert(comments.commentTotal)
    },
    methods: {
    
        highlighter(code) {
      
              return Prism.highlight(code, Prism.languages.js, this.lang)
        },
        
    }
    
})



	

	

	
$('.btn-put-code').click(function(){
	if($(this).text() != "Close"){
	  $('.summernote').slideToggle()
	  $(this).text("Close")
	}else{
	  $('.summernote').slideToggle()
	  $(this).text("Put Code")
	}
   
})
$('#summernote').summernote({
	  tabsize: 1,
	  maxHeight: 120,
	  
	 
});