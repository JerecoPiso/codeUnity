
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
		template: "<span> [date] </span>"

	}
var questions = new Vue({
    delimiters: ['[', ']'],
    el: "#my-questions",
    components: {
        "date-posted": my_component
    },
    data(){
        return {      
            myquestions: [],        
            questionInfo: {language: '', id: '', question: '', category: ''},
            questionEditInfo:  {language: '', id: '', question: '', category: ''},
            languages: [],              
            question_cat: [],
            total_ques_answered: 0,
            total_ques_unanswered: 0,
            frameworks: [],
            tags: [],
            newTag: '',
            toDelete: 0,
            url: '/question/',
            responseMsg: '',
            modalLogo: ''
              
        }
       
    },
    mounted: function(){
        this.getLanguages()
        this.getQuestionCat()
                    
        this.getFrameworks()
        this.getQuestions()
    },
    methods:{
        closePromptModal: function(){
            $("#promptModal").hide()
        },  
        viewQuestion: function(id){
            window.location.href= questions.url+id
        },
        updateQuestion: function(){
            let data = new FormData()
            data.append("id", questions.questionEditInfo.id)
            data.append("question", questions.questionEditInfo.question)
            data.append("language", questions.questionEditInfo.language)
            data.append("category", questions.questionEditInfo.category)
            axios.post("updateQuestion", data ,{headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
              
                $("#editQuestionModal").hide()
              
                if(response.data == "Success"){
                    questions.responseMsg = "Question updated successfully"
                    
                }else{
                    questions.modalLogo = "err"
                    questions.responseMsg = "Unable to update question!"
                    
                }
                $("#promptModal").show()
                questions.getQuestions()

            }).catch(function(err){  
                questions.modalLogo = "err"
                questions.responseMsg = "Unable to update question!"
                $("#promptModal").show()
            })
        },
        putDatasToBeEdit(){
            var con = false
            for(var i = 0; i<questions.languages.length; i++){
                if(questions.languages[i].language == questions.questionEditInfo.language){
                    con = true
                    break;
                }else{
                    con = false
                }
              
            }
           
          
            $("#editQuestionModal").show()
         
        },
        editModalMethod: function(method){
            // alert(questions.questionEditInfo.language)
            if(method == "show"){
                questions.putDatasToBeEdit()
            }else{
                $("#editQuestionModal").hide()
            }

        },
        change: function(){
            this.questionInfo.language = null
            if(this.toShowLang == true){
                this.txt = "Switch to Languages"
                this.toShowLang = false
            }else{
                this.txt = "Switch to Frameworks"
                this.toShowLang = true
            }

        },
        deleteTag: function(index){
            // this.tags.pop(index)
            asked.tags.splice(index,1)
            
        },
        monitor: function(event){
            if(event.key == "Enter"){
                if (this.newTag != "") {
                    this.tags.push(this.newTag)
                    this.newTag = ""
                }
                
            }
         
        },
      
        askQuestion: function(){
            let data = new FormData()
            
            var code = $("#questionCode").summernote('code')
            var now = moment().year()+"-"+(moment().month()+1)+"-"+moment().date()+" "+moment().hour()+":"+moment().minutes()+":"+moment().seconds() 
              
            if((questions.questionInfo.question && questions.questionInfo.language && questions.questionInfo.category) != ""){
                    
                    data.append('question', questions.questionInfo.question)
                    data.append('code', code)
                    data.append('language', questions.questionInfo.language)
                    data.append('category', questions.questionInfo.category)
                    data.append('date', now)
                    if(questions.tags.length == 0){
                        data.append("tags", "")
                    }else{
                        data.append("tags", questions.tags.toString())
                    }
                    
                 
                    axios.post("askQuestion", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                       
                        if(response.data == "Asked successfully"){
                            questions.total_ques_answered = 0
                            questions.total_ques_unanswered = 0
                            questions.getQuestions()
                            questions.questionInfo.question = ''
                            questions.tags = []
                            $("#questionCode").summernote("code", " ")
                            questions.responseMsg = "Question asked successfully"
                        }else{
                            questions.modalLogo = "err"
                            questions.responseMsg = "Unable to asked question!"
                            
                        }
                        $("#promptModal").show()
                     
                    
                    }).catch(function(err){
                      
                            questions.modalLogo = "err"
                            questions.responseMsg = "Unable to asked question!"
                            $("#promptModal").show()
                       
                    })

                }else{
                   
                    questions.modalLogo = "err"
                    questions.responseMsg = "All fields must be filled up except the field of code!"
                    $("#promptModal").show()
                }
                
        
            
        },
        getLanguages: function(){
            axios.get("/dashboard/getLanguages").then(function(response){
                if(response.data == "Failed"){
                alert("Unable to retrieve Languages!")
            }else{
            
               
                questions.languages = response.data
            }
          })
        },
        getFrameworks: function(){
            axios.get("/dashboard/getFrameworks").then(function(response){
                
              
                questions.frameworks = response.data
          })
        },
        
        getQuestionCat: function(){
            axios.get("/dashboard/getCategory").then(function(response){
                if(response.data == "Failed"){
                alert("Unable to retrieve Question Category!")
            }else{
                
                questions.question_cat = response.data
            }
          })
        },
    
        showHideDelModal: function(method){
            if(method == "show"){
                $("#deleteModalForQuestion").show()
            }else{
                $("#deleteModalForQuestion").hide()
            }

        },
        deleteQuestion: function(){
            
                let data = new FormData()
                data.append("id", questions.questionInfo.id)
                axios.post("deleteQuestion", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                  
                    if(response.data == "Deleted successfully"){
                        questions.total_ques_answered = 0
                        questions.total_ques_unanswered = 0
                        questions.getQuestions()
                        $("#deleteModalForQuestion").hide()
                        questions.responseMsg = response.data
                   
                    }else{
                        questions.modalLogo = "err"
                        questions.responseMsg = "Unable to delete question!"
                    }
                    $("#promptModal").show()
                }).catch(function(err){
                    questions.modalLogo = "err"
                    questions.responseMsg = "Unable to delete question!"
                    $("#promptModal").show()
                })

        },

        getQuestions: function(){
            axios.get("getQuestions").then(function(response){
                    
            if(response.data == "Failed"){
                alert("Unable to retrieve Questions!")
            }else{
            
                questions.myquestions = response.data
                for(var i = 0; i < response.data.length; i++){
                    if(questions.myquestions[i].status == "Answered"){
                       questions.total_ques_answered++;
                      
                    }else{
                        questions.total_ques_unanswered++;
                      
                    }
                   
                }
                
               
            }
            
          })
        }
    }
})
