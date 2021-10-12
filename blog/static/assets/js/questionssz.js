var skills = {
    delimiters: ['[', ']'],
    props:{
        
        tags: String,
        // dev_skills: String,
    
        
        
        
    },
    data: function(){

        return{
            tags: this.skills,
            question_tags: String,
        }

    },
    created: function(){
        this.question_tags = this.getTags(this.tags)
    
        // alert(this.dev_skills)
    },
    methods:{
        getTags: function(tag){
            var str = tag
        
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
            //
        }
    },
    template: '<div id="tags" style="margin: 10px 5px 5px 0;font-size: 10px" v-html="question_tags"></div>'
}
var datePosted = {
    delimiters: ['[', ']'],
        props:{
            // date: String,
            posted: String
        },
        data: function(){
            return {
                date: '',
                post: this.posted,
                
            }
        },
        mounted: function(){

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
        template: "<span>( [date] )</span>"

    }
var a  = new Vue({
    delimiters: ['[', ']'],
    el:"#ques",
    data:{
        
        category: '',
        searchValue: '',
    
    },
    components: {
    
    'my-component': skills,
    'date-posted': datePosted
    

    },
    mounted: function(){
    // console.log(my_component.props.dev_skills.type)
        
    },
    methods: {
        searchQuestion: function(){
            let data = new FormData()
            data.append('search', this.searchValue)
            // axios.post('/projects/'+this.searchValue, data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
                
            // })
        
            if(this.searchValue != ""){
                window.location.href="/questions/"+this.searchValue
            }
        
        },
        getCategory: function(){
            window.location.href = '/questions/category/'+ this.category
        }
    }
})
new Vue({
    delimiters: ['[', ']'],
    el:"#searchQuestion",
    data:{
        
        filter: '',
        searchValue: '',
    
    },
    mounted: function(){
    // console.log(my_component.props.dev_skills.type)
        // alert($("#totalComments").text())
    },
    methods: {
        searchQuestion: function(){
            let data = new FormData()
            data.append('search', this.searchValue)
            // axios.post('/projects/'+this.searchValue, data, {headers: {'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val()}}).then(function(response){
                
            // })
        
            if(this.searchValue != ""){
                window.location.href="/questions/search/"+this.searchValue
            }
        
        },
        getFilter: function(){
            window.location.href = '/questions/filter/'+ this.filter
        }
    }
})
