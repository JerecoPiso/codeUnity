var questions = new Vue({
    delimiters: ['[', ']'],
    el: "#my-questions",
    data: {
        questionInfo: {language: '', id: '', question: '', category: ''},
        languages: [],
        myquestions: [],
        question_cat: [],
        total_ques: '',
        frameworks: [],
        toShowLang: true,
        txt: 'Switch to Frameworks',
        tags: [],
        newTag: '',
        toDelete: 0
    },
    mounted: function(){
        this.getLanguages()
        this.getQuestionCat()
        this.getQuestions()
        this.getFrameworks()
    },
    methods:{
        deleteTag: function(index){
            // this.tags.pop(index)
            questions.tags.splice(index,1)
            
        },
        monitor: function(event){
            if(event.key == "Enter"){
                if (this.newTag != "") {
                    this.tags.push(this.newTag)
                    this.newTag = ""
                }
                
            }
            // alert(this.tags.toString())
            // alert($('.tags').html())
            
                
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
        askQuestion: function(){
            let data = new FormData()
            
            var code = $("#summernote").summernote('code')
        
                if((questions.questionInfo.question && questions.questionInfo.language && questions.questionInfo.category) != ""){
                    
                    data.append('question', questions.questionInfo.question)
                    data.append('code', code)
                    data.append('language', questions.questionInfo.language)
                    data.append('category', questions.questionInfo.category)
                    if(questions.tags.length == 0){
                        data.append("tags", "")
                    }else{
                        data.append("tags", questions.tags.toString())
                    }
                    
                    // alert(questions.tags.toString())
                    axios.post("askQuestion", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                        alert(response.data)
                        questions.getQuestions()
                    
                    })

                }else{
                    alert("All fields must be filled up except the field of code!")
                }
                
        
            
        },
        deleteQuestion: function(){
            if (confirm("Are you sure you want to delete this data?") == true) {
                let data = new FormData()
                data.append("id", questions.questionInfo.id)
                axios.post("deleteQuestion", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                    alert(response.data)
                    questions.getQuestions()
                    
                })

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
        getQuestions: function(){
            axios.get("getQuestions").then(function(response){
                    
            if(response.data == "Failed"){
                alert("Unable to retrieve Questions!")
            }else{
            
                questions.myquestions = response.data
                questions.total_ques = response.data.length
            }
            
          })
        }
    }
})