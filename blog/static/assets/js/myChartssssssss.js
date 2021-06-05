
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
                // 'rgba(255, 99, 132, 0.2)',
                // 'rgba(54, 162, 235, 0.2)',
                // 'rgba(255, 206, 86, 0.2)',
                // 'rgba(75, 192, 192, 0.2)',
                // 'rgba(153, 102, 255, 0.2)',
                // 'rgba(255, 159, 64, 0.9)',
               
            ],
            borderColor: [
                // 'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(153, 102, 255, 1)',
                
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
                // 'rgba(255, 99, 132, 0.2)',
                // 'rgba(54, 162, 235, 0.2)',
                // 'rgba(255, 206, 86, 0.2)',
                // 'rgba(75, 192, 192, 0.2)',
                // 'rgba(153, 102, 255, 0.2)',
                // 'rgba(255, 159, 64, 0.9)',
               
            ],
            borderColor: [
                // 'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(153, 102, 255, 1)',
                
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
       
    }
});
var userChartForProjects = new Vue({
    el: ".charts",
    data:{
        projectName: [],
        downloads: []
    },
    created: function(){
        this.getProjects()
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
                    
                    myChart2.data.labels.push(response.data[i].project_name)
               
                    myChart2.data.datasets[0].data.push(response.data[i].downloads)
                    myChart2.data.datasets[0].backgroundColor.push('rgba('+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+Math.floor(Math.random()*255)+','+0.5+')')
                    myChart2.data.datasets[0].borderColor.push('rgba('+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*100)+','+Math.floor(Math.random()*255)+','+0.8+')')
                    myChart.update()
                    myChart2.update()
               
                }
           
              
            })
        }
    }
})
