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
        modalErr: false,
        toShowLang: true,
        text: "Switch to Framework"
    },
    mounted: function(){
        this.getLanguages()
        this.getFrameworks()
    },
    methods:{
        change: function(){
            this.language = null
            if(this.toShowLang == true){
                this.toShowLang = false
                this.text = "Switch to Language"
            }else{
                this.toShowLang = true
                this.text = "Switch to Framework"
            }

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
        
            
        },
        photo: function(){
            folderUpload.appPhoto  = this.$refs.photo.files[0]
        },
        file: function(){
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
                //  alert(folderUpload.language)
                axios.post('uploadProject', fd,{headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                    projects.getProjects()
                    alert(response.data)
                    $('#more').summernote('reset');
                    $('#about').summernote('reset');
                    
                    folderUpload.language = null
                    
                })


            }else{
                folderUpload.modalErr = true
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
        modalDel: false
    },
    mounted: function(){
        this.getProjects();

    },
    methods:{
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
                    alert(response.data)
                    projects.modalDel = false
                    projects.getProjects()
                    
                })

        }
    }
})