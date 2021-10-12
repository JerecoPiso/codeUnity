
  var marginLeft = 0
  var click = 0
  var devicesScreens = ['xs','s','m','l','xl']
  var currentDeviceScreen = ''
  window.onload = function(){
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    if(width <= 568){
      click = 4
      currentDeviceScreen = devicesScreens[0]
    }else if(width >= 569 && width <= 768){
      click = 4
      currentDeviceScreen = devicesScreens[1]
    }else if(width >= 769 && width <= 992){
      click = 3
      currentDeviceScreen = devicesScreens[2]
    }else if(width >= 993 && width <= 1999){
      click = 1
      currentDeviceScreen = devicesScreens[3]
    }else{
      click = 1
      currentDeviceScreen = devicesScreens[4]
    }

  }
  window.onresize = function(){
      var animation = document.getElementById('first')
      animation.style.marginLeft = "0%"
    marginLeft = 0
    var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;
    if(width <= 568){
      click = 4
      currentDeviceScreen = devicesScreens[0]
    }else if(width >= 569 && width <= 768){
      click = 4
      currentDeviceScreen = devicesScreens[1]
    }else if(width >= 769 && width <= 992){
      click = 3
      currentDeviceScreen = devicesScreens[2]
    }else if(width >= 993 && width <= 1999){
      click = 1
      currentDeviceScreen = devicesScreens[3]
    }else{
      click = 1
      currentDeviceScreen = devicesScreens[4]
    }
  }

  function prevNext(event){
    var animation = document.getElementById('first')

    if(event == "prev"){
      if(click != 0){
          click--;
          if(currentDeviceScreen == 'xs'){
                marginLeft = marginLeft + 50.5
          }else if(currentDeviceScreen == 's'){
                marginLeft = marginLeft + 50.3
          }else if(currentDeviceScreen == 'm'){
                marginLeft = marginLeft + 33.5
          }else{
            // alert(currentDeviceScreen)
              marginLeft = marginLeft + 20.5
          }
          // marginLeft = marginLeft + 20.5
          
        animation.style.marginLeft = "-" + marginLeft.toString() +"%"

        animation.style.transition = "1s"

      }
    }else{
      if(click != 4){
          click++;
          if(currentDeviceScreen == 'xs'){
                marginLeft = marginLeft - 50.5
          }else if(currentDeviceScreen == 's'){
                marginLeft = marginLeft - 50.3
          }else if(currentDeviceScreen == 'm'){
                marginLeft = marginLeft - 33.5
          }else{
            // alert(currentDeviceScreen)
              marginLeft = marginLeft - 20.5
          }
        animation.style.marginLeft = "-" + marginLeft.toString() +"%"
        animation.style.transition = "1s"

      }

    }

  }
