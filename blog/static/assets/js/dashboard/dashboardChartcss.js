var ctx = document.getElementById('top-projects').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Project # of Downloads',
            data: [],
            backgroundColor: [
                // 'rgb(255, 99, 132)',
                // 'rgb(54, 162, 235)',
                // 'rgb(255, 206, 86)',
                // 'rgb(75, 192, 192)',
                // 'rgb(153, 102, 255)',
                // 'rgb(255, 159, 64)',
                // 'rgb(255, 159, 64)',
                // 'rgb(153, 102, 255)',
                // 'rgb(255, 159, 64)',
                // 'rgb(255, 159, 64)',
               
            ],
            borderColor: [
                // 'rgb(255, 99, 132)',
                // 'rgb(54, 162, 235)',
                // 'rgb(255, 206, 86)',
                // 'rgb(75, 192, 192)',
                // 'rgb(153, 102, 255)',
                // 'rgb(153, 102, 255)',
                // 'rgb(255, 206, 86)',
                // 'rgb(75, 192, 192)',
                // 'rgb(153, 102, 255)',
                // 'rgb(153, 102, 255)',
                
            ],
            borderWidth: 1
        }]
    },
   
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        title: {
            // display: true,
            text: 'Most Downloaded Projects',
            fontSize: 23,
            fontColor: '#527a7a',
         
           
        },
      
     
    }
});
var ctx2 = document.getElementById('yearly').getContext('2d');
var myChart2 = new Chart(ctx2, {
    type: 'line',
    data :{
        labels: [
            // 'Mobile',
            // 'Laptop',
            // 'Tablet'
        ],
        datasets: [
            {   
                label: "No. of Visitors Yearly",
                data: [],
                backgroundColor: [
                    // 'rgba(0,128,128,0.7)',
                    // 'rgba(0,255,128,0.7)',
                    // 'rgba(0,128,255,0.7)'
                ]
            },
           
        ],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
      
    },
  
    options: {
      
        // title: {
        //     display: true,
        //     text: "Yearly Visitors",
        //     fontSize: 20,
        //     fontColor: '#527a7a',
            
        
        // },
        
        legend: {
            display: true,
           
        }
    }
   
});
var ctx3 = document.getElementById('devices').getContext('2d');
var myChart3 = new Chart(ctx3, {
    type: 'pie',
    data :{
        labels: [
            // 'Mobile',
            // 'Laptop',
            // 'Tablet'
        ],
        datasets: [
            {   
                label: "User's Devices",
                data: [],
                backgroundColor: [
                    // 'rgba(0,128,128,0.7)',
                    // 'rgba(0,255,128,0.7)',
                    // 'rgba(0,128,255,0.7)'
                ]
            },
           
        ],
    
       
      
    },
  
    options: {
      
        // title: {
        //     display: true,
        //     text: "User's Devices",
        //     fontSize: 20,
        //     fontColor: '#527a7a',
            
        
        // },
        
        legend: {
            display: true,
           
        }
    }
   
});
var home = new Vue({
    delimiters: ['[', ']'],
    el: "#mostViewed",
    data:{
        viewedQuestions: [],
        haha: 'sdfdf'
    },
    mounted: function(){
        this.getYearlyVisitors()
        this.getMostDownloadedApp()
        this.getMostViewedQuestions()
       
    },
    methods:{
        getYearlyVisitors: function(){
            axios.get("yearlyVisitors").then(function(response){
                // alert(response.data)
                 for(var i = 0; i < response.data.length; i++){
                 
                  
                    myChart2.data.labels.push(response.data[i].year)
                    myChart2.data.datasets[0].data.push(response.data[i].total_visitors)
                    // alert(response.data[i].year)
                    // myChart2.data.datasets[0].backgroundColor.push('rgba('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+0.8+')')
                    // myChart2.data.datasets[0].borderColor.push('rgba('+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*255)+','+0.8+')')
                  
                    myChart2.update()
               
                }
            }).catch(function(err){
                console.log(err)
            })
        },
        getMostDownloadedApp: function(){
            axios.get("getMostDownloadedApp").then(function(response){
                for(var i = 0; i < response.data.length; i++){
                 
                    myChart.data.labels.push(response.data[i].project_name)
                    myChart.data.datasets[0].data.push(response.data[i].downloads)
                    myChart.data.datasets[0].backgroundColor.push('rgba('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+0.8+')')
                    myChart.data.datasets[0].borderColor.push('rgba('+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*255)+','+0.8+')')               
                    myChart.update()

               
                }
            }).catch(function(err){
                console.log(err)
            })
        },
        getMostViewedQuestions: function(){
            axios.get("getMostViewedQuestions").then(function(response){
                home.viewedQuestions = response.data
              
                // for(var i = 0; i < response.data.length; i++){
                 
                  
                //     myChart2.data.labels.push(response.data[i].question)
                //     myChart2.data.datasets[0].data.push(response.data[i].views)
                //     myChart2.data.datasets[0].backgroundColor.push('rgba('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+0.8+')')
                //     myChart2.data.datasets[0].borderColor.push('rgba('+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*255)+','+0.8+')')
                  
                //     myChart2.update()
               
                // }
            }).catch(function(err){
                console.log(err)
            })
        }
    }
})
var devices = new Vue({
    delimiters: ['[', ']'],
    el: "#device-form",
    data:{
     
      
    }, 
    mounted: function(){
        this.getDevices()
    },
    methods:{
       
        getDevices: function(){
            axios.get("/dashboard/getDevices").then(function(response){
                var totalUsers = 0
                for(var i = 0; i < response.data.length; i++){
                    totalUsers = totalUsers + response.data[i].total_users
                }
                for(var i = 0; i < response.data.length; i++){
                    
                    myChart3.data.labels.push(response.data[i].device_name)
                    var percent = (response.data[i].total_users/totalUsers) * 100
                 
                    myChart3.data.datasets[0].data.push(Math.round(percent))
                    // alert(response.data[i].year)
                    myChart3.data.datasets[0].backgroundColor.push('rgba('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+0.8+')')
                    // myChart3.data.datasets[0].borderColor.push('rgba('+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*255)+','+0.8+')')
                  
                    myChart3.update()
               
                }
               
            }).catch(function(err){
                console.log(err.statustext)
            })
        },
      
    }
})
