var chatApp = new Vue({
    delimiters: ['[', ']'],
    el: "#chatApp",
    data:{
        receiver: "",
        image: "/assets/images/",
        haha: "LAPTOP.jpg",
        messageInfo: {message: '', sender: getId(), receiver_id: '' , last_id: null},
        users: [],
        messages: [],
        show: false,
        ctr: 0,
        userDp: ''
    },
    mounted: function(){
                 
        this.$nextTick(function () {    

             this.getUsers();

        })
        setInterval(function(){
          //update the list of online users every 1.5 seconds
            chatApp.getUsers();                                         

         }, 1500)

    },
    updated: function(){

      if(chatApp.ctr == 1){

        scroll()

      }
         
    },
    methods:{
        
          send: function(){
     
                chatApp.ctr++;
                 setInterval(function(){
                   chatApp.ctr = 0;
                   chatApp.getNewMessages();
                }, 1000)
        },
        fastSend: function(){

            if(event.key == "Enter"){
                chatApp.sendMessage();
            }
            
        },
        getUsers: function(){
       
            axios.get("getUsers").then(function(res){
              if(res.data != "No users"){

                       chatApp.users = res.data;
             }else{
                chatApp.users = null;
             }
            

            })
         
        },
        getMessages: function(){
   
             if(chatApp.messageInfo.receiver_id != null){

                     chatApp.messages = null  
                     axios.post("getMessages",chatApp.messageInfo).then(function(res){

                        if(res.data == false){

                            chatApp.show = true;
                            chatApp.send();
                        }else{

                             chatApp.messages = res.data
                             chatApp.send();
                             chatApp.show = true;
                        
                        }   
                    })

             }
        },
        getNewMessages: function(){


             if(chatApp.messageInfo.last_id != null){
             
                 axios.post("getNewMessages",chatApp.messageInfo).then(function(res){
                   

                      if(res.data == "None" || res.data == false){
                     
                      }else{

                         chatApp.messages = null; 
                         chatApp.messages = res.data
                         scroll()
                      }

                
                })

         }

        },
        sendMessage: function(){
            if(chatApp.messageInfo.receiver_id != null){

                    axios.post("/sendMessage", chatApp.messageInfo).then(function(res){                
                        chatApp.messageInfo.message = "";
                        chatApp.getMessages();

                    });

            }
        },
      
    }
       
})

 function scroll(){
    var element = document.getElementById('msg');
    element.scrollTop = element.scrollHeight;  
     
}
           
function getId(){
   return document.getElementById("id").value;
}