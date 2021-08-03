// $('#work-experience').summernote({
//     tabSize: 1,
//     maxHeight: 500,
//     placeholder: 'e.g works/links, work experience, years of experience, and your personal profile',

// });
var sideNav  = new Vue({
    delimiters: ['[', ']'],
    el: ".sideNav",
    data:{
    username: '',
    mydp: null,
    src: '/media/'
    },
    mounted: function(){
    this.getUser()
    // alert("hahahah")
    },
    methods:{
    
    getUser: function(){
         axios.get("/user/getUserInfo").then(function(response){
            sideNav.mydp = response.data[0].photo
            sideNav.username = response.data[0].uname
         })
    }
    }
    })
var changeDp = new Vue({
        delimiters: ['[', ']'],
        el: "#user-dp",
        data:{

        photo: '',
        mydp: null,
        src: '/media/',
        responseMsg: '',
        modalLogo: ''
        },
        mounted: function(){
        this.getUser()
        },
        methods:{
        haha(){
            alert("Dfdf")
        },
        closePromptModal(){
            $("#promptModal").hide()
        },
        changeDpModal: function(toDo){
            if(toDo == "show"){
                $(".dpModal").show()
            }else{
                $(".dpModal").hide()
            }
        },
        dp: function(){
            changeDp.photo  = this.$refs.photo.files[0]
        },
        changeDp: function(){
            let data = new FormData()
            data.append("photo", changeDp.photo)
            axios.post('/user/changeDp', data,{headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value}} ).then(function(response){
                // projects.getProjects()

                if(response.data == "Saved"){
                    changeDp.responseMsg = "Profile updated successfully"
                
                }else{
                    changeDp.modalLogo = "err"
                    changeDp.responseMsg = "Unable to change profile!"
                
                }
                $(".dpModal").hide()
                changeDp.getUser()
                sideNav.getUser()
                $("#promptModal").show()
            
            }).catch(function(err){
                
                changeDp.modalLogo = "err"
                changeDp.responseMsg = "Unable to change profile!"
                $("#promptModal").show()
            

            })
        },
        getUser: function(){
            axios.get("/user/getUserInfo").then(function(response){
                changeDp.mydp = response.data[0].photo
            })
        }
    }
})


var settings = new Vue({
delimiters: ['[', ']'],
el: "#security-info",
data:{
editPassDisable: true,
editUnameDisable: true,
password_save: false,
uname_save: false,
disabled: false,
skills: [],
newSkill: '',
userInfo: {email: '', password: '', verifyPass: '', username: ''},
showPass: false,
stringOnly: /^[a-zA-Z ]+$/,
numbersOnly: /^[0-9]+$/
},
mounted: function(){
this.getUserData()
},
methods:{

changeUsername: function(){
    let data = new FormData()
    data.append("username", settings.userInfo.username)
    axios.post("/user/editUsername", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
       
        if(response.data == "Username updated successfully"){
            changeDp.responseMsg = response.data
            
        }else{
            changeDp.modalLogo = "err"
            changeDp.responseMsg = "Unable to change username!"
          
        }
        $("#promptModal").show()
        settings.getUserData()
        settings.editUnameDisable = true
        settings.uname_save = false
        sideNav.getUser()
    }).catch(function(err){
        changeDp.modalLogo = "err"
        changeDp.responseMsg = "Unable to change username!"
        $("#promptModal").show()
    })
},
changePassword: function(){
    if(settings.userInfo.password.length < 8){
    
    alert("Password must contain at least 8 characters!")

    
}else if( settings.userInfo.password.match(settings.numbersOnly) || settings.userInfo.password.match(settings.stringOnly) ){

    alert("Password must contain letters and numbers!")

}else{
    
    if(settings.userInfo.password != "" && settings.userInfo.verifyPass != ""){

            if(settings.userInfo.password == settings.userInfo.verifyPass){
                
                // axios for updating password
                let data = new FormData()
                data.append("password", settings.userInfo.password)
                axios.post("/user/editPassword", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
                 
                    if(response.data == "Password updated successfully"){
                        changeDp.responseMsg = response.data
                        $("#promptModal").show()
                    }else{
                        changeDp.modalLogo = "err"
                        changeDp.responseMsg = "Unable to change password!"
                      
                    }
                 
                    settings.getUserData()
                    settings.editPassDisable = true
                    settings.password_save = false
                    settings.userInfo.password = ""
                    $(".passwordModal").hide()
                    $("#promptModal").show()
                }).catch(function(err){
                    changeDp.modalLogo = "err"
                    changeDp.responseMsg = "Unable to change password!"
                    $("#promptModal").show()
                })

            }else{
                alert("Password didn't matched!")
            }
    
            
    }
    
}

},
getUserData: function(){

    axios.get("/user/getUserInfo").then(function(response){
        settings.userInfo.username = response.data[0].uname
        // settings.userInfo.password = response.data[0].password
        settings.userInfo.email = response.data[0].email
    }).catch(function(err){
        console.log(err)
    })

},
viewHidePass: function(){

    if(this.$refs.pass.type == "password"){
        settings.showPass = true
        this.$refs.pass.type = "text"
    }else{
        settings.showPass = false
        this.$refs.pass.type = "password"
    }

},
deleteTag: function(index){
    // this.tags.pop(index)
    settings.skills.splice(index,1)
    
},
monitor: function(event){

    if(event.key == "Enter"){
        if (this.newSkill != "") {
            this.skills.push(this.newSkill)
            this.newSkill = ""
        }
        
    }
    // alert(this.tags.toString())
    // alert($('.tags').html())
    
        
},

editPassword: function(){
    
    if(settings.password_save){
        if(settings.userInfo.password != ""){
            $(".passwordModal").show()
        }else{
            alert("Password must not be empty!")
        }
        
    }else{
        settings.password_save = true
    }
},
closeVerifyPass: function(){
    $(".passwordModal").hide()
},
editUname: function(){
    if(settings.uname_save){
        // edit code
    }else{
        settings.uname_save = true
    }
}
}
})
var my_component = {
delimiters: ['[', ']'],
props:{

skills: String,
// dev_skills: String,




},
data: function(){

return{
    tag: this.skills,
    dev_skills: String,
}

},
created: function(){
this.dev_skills = this.getTags(this.tag)

// alert(this.dev_skills)
},
methods:{
getTags: function(skill){
    var str = skill

    var n = null;
    var tags = ""
    // var num = str.search(",");
    while(str.length != 0){
        var ctr = str.search(",");
        if(ctr != -1){
            n = str.slice(0,ctr)
            str = str.slice(ctr+1,str.length)
        
            tags = tags+"<a href='/questions/tags/"+n+"' class='tag-link'>"+n+"</a>";
            
        }else{
            str = str.slice(0,str.length)
            tags = tags+"<a href='/questions/tags/"+str+"' class='tag-link'>"+str+"</a>";
        
            str = ""
            
            
        
        }
        
    }

    return tags
}
},
template: '<div id="tags" style="margin: 10px 5px 5px 0;font-size: 10px" v-html="dev_skills"></div>'
}

var settingsOtherInfo = new Vue({
delimiters: ['[', ']'],
el: "#other-info",
data:{
newSkills: [],
newSkill: '',
expertise: '',
mySkills: [],
rmSkills: [],
summerNote: ''



},
components:{
'my-skills': my_component
},	
mounted: function(){

this.getOtherInfo()

},
methods:{
getAboutMe(c){
    this.summerNote = c
},
deleteSkill: function(index){
    // this.tags.pop(index)
    this.newSkills.splice(index,1)
    
},
deleteMySkills: function(index,skill){
    this.mySkills.splice(index,1)
    this.rmSkills.push({
        id: index,
        value: skill 
    })
    // console.log(this.rmSkills)
},
undoDeleteSkills: function(index,skill){

    this.mySkills.splice(index, 0, skill)
    this.rmSkills.splice(index, 1)
    // alert(this.rmSkills[index])

},
getSkills: function(skill){
    var str = skill

    var n = null;
    var tags = []
    // var num = str.search(",");
    while(str.length != 0){
        var ctr = str.search(",");
        if(ctr != -1){
            n = str.slice(0,ctr)
            str = str.slice(ctr+1,str.length)
        
            tags.push(n)
            
        }else{
            str = str.slice(0,str.length)
            // tags = tags+"<a href='/questions/tags/"+str+"' class='tag-link'>"+str+"</a>";
            tags.push(str)
            str = ""
            
            
        
        }
        
    }
    // console.log(tags)
    return tags
},
monitor: function(event){

    if(event.key == "Enter"){
        if (this.newSkill != "") {
            this.newSkills.push(this.newSkill)
            this.newSkill = ""
        }
        
    }
},
getOtherInfo: function(){
    axios.get("/user/getUserInfo").then(function(response){
        // console.log(response.data)
        
        settingsOtherInfo.mySkills = settingsOtherInfo.getSkills(response.data[0].skills)
        settingsOtherInfo.expertise = response.data[0].expertise
        settingsOtherInfo.summerNote = response.data[0].aboutme
        $("#work-experience").summernote('code', response.data[0].aboutme)
        // console.log(skill)
    })
},
updateInfo: function(){
    let data = new FormData()
    data.append("skills", this.mySkills.concat(this.newSkills))
    data.append("expertise", this.expertise)
    var summerNoteContent = $("#work-experience").summernote('code')
    data.append("aboutme", summerNoteContent)
    // alert(this.newSkills.toString())
    // alert(this.mySkills.concat(this.newSkills))
    axios.post("/user/updateInfo", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
     
        if(response.data == "Success"){
            changeDp.responseMsg = "Updated successfully"
        }else{
            changeDp.modalLogo = "err"
            changeDp.responseMsg = "Unable to update infos!"
          
        }
        $("#promptModal").show()
        settingsOtherInfo.newSkills = []
        settingsOtherInfo.rmSkills = []
        settingsOtherInfo.getOtherInfo()
    }).catch(function(err){
        changeDp.modalLogo = "err"
            changeDp.responseMsg = "Unable to update infos!"
            $("#promptModal").show()
    })
}


}
})
$('#work-experience').on('summernote.change', function(we, contents, $editable) {
// console.log(contents);
settingsOtherInfo.getAboutMe(contents)
});


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