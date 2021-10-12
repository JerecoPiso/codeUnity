

var files = new Vue({
    delimiters: ['[', ']'],
    el: ".folders-files",
    data:{
        path: '',
        filename: '',
        code: '',
        lang: 'html',
        filePath: '',
        media: '/media/',
        responseMsg: '',
        modalLogo: ''
    },
    mounted: function(){
        // alert("skjfsjhdfgjhg")
        this.lang = $("#language").val()
        
    },
    methods: {
        highlighter: function(code) {
        // alert(comments.code)
        // var inp = code.replace(/<(style|script|iframe)[^>]*?>[\s\S]+?<\/\1\s*>/gi,'').replace(/<[^>]+?>/g,'').replace(/\s+/g,' ').replace(/ /g,' ').replace(/>/g,' '); 
        return Prism.highlight(code, Prism.languages.js, this.lang);
    },
        getFile: function(){
            if(files.filename.search(".png") < 0 && files.filename.search(".jpg") < 0){
                let fd = new FormData();
            
                fd.append('path', files.path)
                fd.append('fname', files.filename)


            axios.post('/user/readFile', fd,{headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){

                if(response.data != ""){
                    files.code = response.data.code
                    files.filePath = response.data.filename
                    $(".modalEditor").show()
                }
            
                
            }).catch(function(err){
                files.modalLogo = "err"
                files.responseMsg = "Unable to open file!"
                $(".promptModal").show()
                
            })
            }else{
                $(".imgModal").show()
            
        }

            
        },
        editCode: function(){
            let data = new FormData()
            
            data.append("filePath", files.filePath)
            data.append("code", files.code)
            axios.post("/user/editCode", data,{headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                files.modalLogo = "success"
                files.responseMsg = response.data
                $(".modalEditor").hide()
                $(".promptModal").show()
            }).catch(function(err){
                console.log(err)
            })

        },
        closeEditor(){
            $(".modalEditor").hide()
        },
        closeImageViewer: function(){
            $(".imgModal").hide()
        },
        closeResponseModal(){
            $(".promptModal").hide()
        },
        deleteFile(){
            if(confirm("Are you sure you want to delete this file "+"' "+files.filename+" ' ?") == true){
                let data = new FormData()
                data.append("filename", files.path.replace(/%/g, "\\"))
                
                axios.post('/user/deleteFile', data,{headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                    
                    if(response.data == "Success"){
                    
                        files.modalLogo = "success"
                        files.responseMsg = "Deleted file successfully"
                        
                        $(".promptModal").show()
                        $(".imgModal").hide()
                        
                        window.location.href = window.location.pathname
                    }else{
                        files.modalLogo = "err"
                        files.responseMsg = response.data
                        $(".promptModal").show()
                    }
                })
            }
        }
            

    }
})