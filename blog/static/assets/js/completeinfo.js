var completeinfo = new Vue({
    delimiters: ['[',']'],
    el: '#completeinfo',
    data:{
        countries: [],
        expertise: '',
        rate: '',
        arrIndex: '',
        skills: [],
        more: '',
        termsAndCondition: false,
        addedSkills: [],
        newSkills: [],
        newSkill: '',
        showLanguages: false,
        showFrameworks: false,
        showLangBtnTxt: 'Show Languages',
        showFwBtnTxt: 'Show Frameworks',
        ifLangEmpty: '',
        ifFwEmpty: '',
        languages: [],
        frameworks: [],
        responseModal: false,
        responseMsg: ''
    },
    mounted: function(){
        for(var i = 0; i < countryList.length; i++){
            this.countries.push({
                name: countryList[i].name,
                countryAbbr: countryList[i].code.toLowerCase()
            })
        }
        
    },
    methods:{
        selectToShow: function(toShown){
            if(toShown == "language"){
                if(completeinfo.showLanguages == true){
            
                    completeinfo.showLangBtnTxt = "Show Languages"
                    completeinfo.showLanguages = false
                    completeinfo.ifLangEmpty = ""
                    
                }else{
                    completeinfo.showLangBtnTxt = "Hide Languages"
                    // settingsOtherInfo.languages = settingsOtherInfo.languages
                    completeinfo.showLanguages = true
                    completeinfo.languages = []
                    completeinfo.ifLangEmpty = ""
                }
                completeinfo.showFwBtnTxt = "Show Frameworks"
                completeinfo.showFrameworks = false
            }else{

                if(completeinfo.showFrameworks){
                    completeinfo.toShow = completeinfo.frameworks
                    completeinfo.showFwBtnTxt = "Show Frameworks"
                    completeinfo.showFrameworks = false
                }else{
                    completeinfo.showFwBtnTxt = "Hide Frameworks"
            
                    completeinfo.showFrameworks = true
                    completeinfo.frameworks = []
                
                }
                completeinfo.showLangBtnTxt = "Show Languages"
                completeinfo.showLanguages = false

        
            
            }
        
        },
        addSkillFromSuggestions: function(index,val,arrayName){
  
            if(arrayName == "languages"){
                this.languages.splice(index,1)
            }else{
                this.frameworks.splice(index,1)
            }
            
            var list = []
            for(var i = 0; i< completeinfo.addedSkills.length; i++){
                list.push(completeinfo.addedSkills[i].value.toLowerCase())
                
            }
            // alert(list.concat(settingsOtherInfo.newSkills).length)
            if(list.concat(completeinfo.newSkills).length != 0){
                    for(var i = 0; i < list.concat(completeinfo.newSkills).length; i++){
                    
                        if(list.concat(completeinfo.newSkills).indexOf(val.toLowerCase()) < 0){
                            this.addedSkills.push({
                                value: val,
                                origin: arrayName
                            })
                            break;
                    }
                }
            }else{
                this.addedSkills.push({
                    origin: arrayName,
                    value: val
                })
            }
            if(arrayName == "languages"){
                if(completeinfo.languages.length == 0){
                    completeinfo.showLangBtnTxt = "Show Languages"
                    // settingsOtherInfo.ifLangEmpty = "You have already added all the languages in your skills."
                    completeinfo.showLanguages = false
            
                    
                }
            }else{
                if(completeinfo.frameworks.length == 0){
                    completeinfo.showFwBtnTxt = "Show Frameworks"
                    completeinfo.showFrameworks = false
            
                    
                }
            }
            
 
 

          },
        getLanguages: function(){
            completeinfo.languages = []
                axios.get("/dashboard/getLanguages").then(function(response){
                    
                    var list = []
                    // for (a = 0; a < completeinfo.mySkills.length; a++){
                    //     list.push(completeinfo.mySkills[a].toLowerCase())
                    // }
                    var join = completeinfo.addedSkills
                    var finalJoin = []
                    if(completeinfo.newSkills.length != 0){
                        for(var i = 0; i < completeinfo.newSkills.length; i++){
                        
                        
                        
                                finalJoin.push(completeinfo.newSkills[i].toLowerCase())
                        
                        }
                    }
                    if(join.length != 0){
                        for(var i = 0; i < join.length; i++){
                        
                        
                                finalJoin.push(join[i].value.toLowerCase())
                        
                        
                        
                        }
                        list = list.concat(finalJoin)
                    }
                
                    // check if the language is already added to new skill
                    for(var x = 0; x < response.data.length;x++){
                        
                        if(list.indexOf(response.data[x].language.toLowerCase()) < 0){
                            completeinfo.languages.push({
                                    
                                value: response.data[x].language
                            })
                        
                        }

                    }
                    if(completeinfo.languages.length === 0){
                        completeinfo.ifLangEmpty = "You have already used all the languages."
                    }else{
                        completeinfo.ifLangEmpty = ""
                    }

                }).catch(function(err){
                    console.log(err)
                })
        },
        getFrameworks: function(){
                completeinfo.frameworks = []
                axios.get("/dashboard/getFrameworks").then(function(response){
                
                    var list = []
                    // for (a = 0; a < settingsOtherInfo.mySkills.length; a++){
                    //     list.push(settingsOtherInfo.mySkills[a].toLowerCase())
                    // }
                    var join = completeinfo.addedSkills
                    var finalJoin = []
                    if(completeinfo.newSkills.length != 0){
                        for(var i = 0; i < completeinfo.newSkills.length; i++){
                        
                        
                        
                                finalJoin.push(completeinfo.newSkills[i].toLowerCase())
                        
                        }
                    }
                    if(join.length != 0){
                        for(var i = 0; i < join.length; i++){
                            finalJoin.push(join[i].value.toLowerCase())
                        
                        }
                        list = list.concat(finalJoin)
                    }
                    for(var x = 0; x < response.data.length;x++){
                    
                        if(list.indexOf(response.data[x].framework.toLowerCase()) < 0){
                            completeinfo.frameworks.push({
                                    
                                value: response.data[x].framework
                            })
                        
                        }

                    }
                
                    if(completeinfo.frameworks.length === 0){
                        completeinfo.ifFwEmpty = "You have already used all the frameworks."
                    }else{
                        completeinfo.ifFwEmpty = ""
                    }

                }).catch(function(err){
                    console.log(err)
                })
        },
        submit: function(){
            let data = new FormData()
            var addedSkillsClean = []
            var summerNoteContent = $("#more-aboutme").summernote('code')
            if(completeinfo.expertise == ""){
                completeinfo.responseMsg = "Expertise must not be empty!"
                completeinfo.responseModal = true
                // alert("Expertise must be fillep up!")
            }else if(completeinfo.arrIndex == ""){
                completeinfo.responseMsg = "You must select a country!"
                completeinfo.responseModal = true
            
            }else if(completeinfo.rate == ""){
                completeinfo.responseMsg = "Rate must be empty!"
                completeinfo.responseModal = true
        
            }else if(completeinfo.newSkills.concat(addedSkillsClean).length == 0){
                completeinfo.responseMsg = "You should put a least one skill!"
                completeinfo.responseModal = true


            }else if(completeinfo.termsAndCondition != true){
                completeinfo.responseMsg = "It's important to agree to our terms and conditions before completing the form."
                completeinfo.responseModal = true


            }else{
                
                data.append("expertise", completeinfo.expertise)
                data.append("rate", completeinfo.rate)
                data.append("country", completeinfo.countries[completeinfo.arrIndex].name)
                data.append("countryAbbr", completeinfo.countries[completeinfo.arrIndex].countryAbbr)
                data.append("more", summerNoteContent)
                for(var i = 0; i < completeinfo.addedSkills.length; i++){
                    addedSkillsClean.push(completeinfo.addedSkillsClean[i].value)
                }
                
                data.append("skills", completeinfo.newSkills.concat(addedSkillsClean))
                axios.post("/setmoreinfo", data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
                    if(response.data === "Success"){
                        window.location.href="/verify"
                    }else{
                        completeinfo.responseMsg = "An error has occured!"
                        completeinfo.responseModal = true
                    }
                
                }).catch(function(err){
                    console.log(err)
                })
            }
            
            
            
        },
        deleteSkill: function(index){
                // this.tags.pop(index)
                this.newSkills.splice(index,1)
        
        },
        undoAddedSkill: function(index,skill,origin){
            this.addedSkills.splice(index, 1)
            if(origin == "languages"){
                this.languages.unshift({
                    value: skill
                })
            }else{
                this.frameworks.unshift({
                    value: skill
                })
            }
        
        },
        monitor: function(event){
       
            if(event.key == "Enter"){
                if (this.newSkill != "") {
                    var list = []
                    if(completeinfo.addedSkills.length != 0){
                        for(var i = 0; i < completeinfo.addedSkills.length; i++){
                            list.push(completeinfo.addedSkills[i].value.toLowerCase())
                            
                        }
                    }
                    
                    
                    if(list.concat(completeinfo.newSkills).length != 0){
                        for(var i = 0; i < list.concat(completeinfo.newSkills).length; i++){
                            if(list.concat(completeinfo.newSkills).indexOf(this.newSkill.toLowerCase()) < 0){
                                this.newSkills.push(
                                    this.newSkill
                                )
        
                        }
                    }
                    }else{
                        this.newSkills.push(
                                this.newSkill
                        )
                    }
                    
                    this.newSkill = ""
                }
                
            }
           }
     }
    })
    $("#more-aboutme").summernote('code', '')