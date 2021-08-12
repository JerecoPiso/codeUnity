
var ctx = document.getElementById('myChart').getContext('2d');
var ctx2 = document.getElementById('comments').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Project # of Downloads',
            data: [],
            backgroundColor: [
                
               
            ],
            borderColor: [
             
                
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: false
                }
            }]
        },
       
    }
});
var myChart2 = new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: [],
        datasets: [{
            label: 'Project # of Downloads',
            data: [],
            backgroundColor: [
               
               
            ],
            borderColor: [
            
                
            ],
            borderWidth: 1
        }]
    },
   
});
var userChartForProjects = new Vue({
    el: ".charts",
    data:{
        projectName: [],
        downloads: []
    },
    created: function(){
        this.getProjects()
        this.getQuestions()
        // console.log(myChart.data.labels)
      
      
    },
    methods:{
        getProjects: function(){
            axios.get("getProjects").then(function(response){
            
                for(var i = 0; i < response.data.length; i++){
                 
                    myChart.data.labels.push(response.data[i].project_name)
               
                    myChart.data.datasets[0].data.push(response.data[i].downloads)
                    myChart.data.datasets[0].backgroundColor.push('rgba('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+0.5+')')
                    myChart.data.datasets[0].borderColor.push('rgba('+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*255)+','+0.8+')')
                    
                  
                    myChart.update()

               
                }
           
              
            })
        },
        getQuestions: function(){
            axios.get("getQuestions").then(function(response){
            
                for(var i = 0; i < response.data.length; i++){
                 
                  
                    
                    myChart2.data.labels.push(response.data[i].question)
                    myChart2.data.datasets[0].data.push(response.data[i].views)
                    myChart2.data.datasets[0].backgroundColor.push('rgba('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+0.5+')')
                    myChart2.data.datasets[0].borderColor.push('rgba('+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*255)+','+0.8+')')
       
                    myChart2.update()
               
                }
           
              
            })
        }
    }
})
var notifications = new Vue({
    delimiters: ['[', ']'],
    el: ".notifications-div",
    data:{
       noti: [],
      
    },
    mounted: function(){
    
      this.getNotifications()
      
    },
    methods:{
        getNotifications(){
            axios.get("/user/getNotifications").then(function(response){
               
                notifications.noti = response.data
                // console.log(notifications.noti)
            }).catch(function(err){
                console.log(err)
            })
        }
        
    }
})

