 
var folderUpload = new Vue({
    el: "#files",
    delimiters: ['[', ']'],
    data:{
        folder: '',
        about: '',
        language: '',
        languages: [],
        frameworks: [],
        framework: [],
        appPhoto: '',
        fileLimit: false,
        placeHolder: 'Select folder to upload',
        editProjectInfo: {project_name: '', lang: '', more: '', about: ''},
        appPhotoName: 'Select Photo',
        bar: 0
    },
    mounted: function(){
        this.getLanguages()
        this.getFrameworks()
    },
    methods:{
        editProject: function(){
            let data = new FormData()
            data.append("project_name", folderUpload.editProjectInfo.project_name)
            data.append("language", folderUpload.editProjectInfo.lang)
            data.append("id", folderUpload.editProjectInfo.id)
            data.append("more", $("#more-update").summernote('code'))
            data.append("about", $("#about-update").summernote('code'))
            axios.post("/user/editProjectInfo", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}}).then(function(response){
             
                if(response.data == "Success"){
                  
                    $(".updateModal").hide()
                    projects.getProjects()
                    projects.responseMsg = "Updated successfully"
					$("#promptModal").show()
                }else{
                    projects.modalLogo = "err"
					projects.responseMsg = "Unable to delete project!"
					$("#promptModal").show()
                }
            }).catch(function(err){
                // console.log(err)
                
                    projects.modalLogo = "err"
					projects.responseMsg = "Unable to delete project!"
					$("#promptModal").show()
             

            })
        },
        closeSizeLimit: function(){
            $("#size-limit").hide()
        },
        getLanguages: function(){
            axios.get("/dashboard/getLanguages").then(function(response){
                if(response.data == "Failed"){
                alert("Unable to retrieve Languages!")
            }else{
            
                folderUpload.languages = response.data
            }
          })
        },
        getFrameworks: function(){
            axios.get("/dashboard/getFrameworks").then(function(response){
                
                folderUpload.frameworks = response.data
                
          })
        },
        handleFileUpload: function(){

            folderUpload.folder = this.$refs.file.files
            
            var max_size = 0
            for (i = 0; i < folderUpload.folder.length; i++) {
                max_size = folderUpload.folder[i].size + max_size
                
            }
            if(max_size > 10457600){
                folderUpload.fileLimit = true
                folderUpload.modalErr = true
            }else{
                folderUpload.fileLimit = false
            }
            var pos = folderUpload.folder[0]['webkitRelativePath'].indexOf("/");
            // let fd = new FormData();
         
            folderUpload.placeHolder = folderUpload.folder[0]['webkitRelativePath'].slice(0, pos)
            
        },
        photo: function(){
            folderUpload.appPhoto  = this.$refs.photo.files[0]
            folderUpload.appPhotoName = folderUpload.appPhoto.name

        },
        closeEditModal: function(){
          
            $(".updateModal").hide()
        },
        uploadProject: function(){
            var now = moment().year()+"-"+(moment().month()+1)+"-"+moment().date()+" "+moment().hour()+":"+moment().minutes()+":"+moment().seconds() 
            
            if(folderUpload.fileLimit != true){

                // var about = new nicEditors.findEditor('about');
                var about = $("#about").summernote('code')
                var more = $("#more").summernote('code')
                // var more = new nicEditors.findEditor('more')
                var pos = folderUpload.folder[0]['webkitRelativePath'].indexOf("/");
                let fd = new FormData();
                for(var i = 0; i < folderUpload.folder.length; i++){
                    fd.append('files', folderUpload.folder[i])
                    fd.append('paths', folderUpload.folder[i]['webkitRelativePath'])
                }
                
                fd.append("project_name", folderUpload.folder[0]['webkitRelativePath'].slice(0, pos))
                fd.append('about', about)
                fd.append('more', more)
                fd.append("language", folderUpload.language)
                fd.append("photo", folderUpload.appPhoto)
                fd.append("date", now)
                //  alert(folderUpload.language)
            
                axios.post('uploadProject', fd,
                {
                    headers: { 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value },  
                    progress:( progressEvent ) => {
                        folderUpload.bar = Math.round( (progressEvent.loaded * 100) / progressEvent.total )
                  }
                }
                 ).then(function(response){
                   
                 
                   
                    if(response.data != "Folder name aldready exists." || response.data != "An error has occurred!" ){
                        $('#more').summernote('reset');
                        $('#about').summernote('reset');
                        folderUpload.language = null     
                        projects.responseMsg = response.data
                        $("#promptModal").show()
                    }else{
                        projects.modalLogo = "err"
                        projects.responseMsg = response.data
                        $("#promptModal").show()
                    }
                    projects.getProjects()
                    
                }).catch(function(err){
                    console.log(err)
                })
            }else{
                
                $("#size-limit").show()
            }
            
        
        }

    }
})
var projects = new Vue({
    delimiters: ['[', ']'],
    el: "#projects",
    data:{
        project: [],
        url: "project_files/",
        id: '',
        count: '',
        responseMsg: '',
        modalLogo: ''
        
      
    },
    mounted: function(){
        this.getProjects();

    },
    methods:{
        // to show the modal for editing
        updateProject: function(project_name, language, id, more, about){
            folderUpload.editProjectInfo.project_name = project_name
            folderUpload.editProjectInfo.lang = language
            folderUpload.editProjectInfo.id = id
            $("#about-update").summernote('code', about)
            $("#more-update").summernote('code', more)
            $(".updateModal").show()
        },
       
        getProjects: function(){
            
            axios.get("getProjects").then(function(response){
                projects.project = response.data
                projects.count = response.data.length
            })
        },
        deleteProject: function(){
            
                let data = new FormData()
                data.append("id", projects.id)
            
                axios.post("deleteProject", data, {headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                   
                    projects.modalDel = false
                    projects.getProjects()
                    $("#deleteProjectModal").hide()
                    projects.responseMsg = response.data
					$("#promptModal").show()
                    
                }).catch(function(err){
                    projects.modalLogo = "err"
                    projects.responseMsg = "Unable to delete project!"
                    $("#deleteProjectModal").hide()
					$("#promptModal").show()
                })

        },
        closePromptModal: function(){
            $("#promptModal").hide()
        },
        showDeleteModal: function(toDo){
            if(toDo == "show"){
                $("#deleteProjectModal").show()
            }else{
                $("#deleteProjectModal").hide()
            }
           
        }
    }
})