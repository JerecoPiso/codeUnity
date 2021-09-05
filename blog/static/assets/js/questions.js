var my_component = {
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
new Vue({
    delimiters: ['[', ']'],
    el:"#ques",
    data:{
        
        category: '',
        searchValue: '',
    
    },
    components: {
    
    'my-component': my_component,
    

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
