var gamepad;
var buttonStatusDiv;
var analogicValueProgressBar;

window.onload = function() {
  buttonStatusDiv = document.querySelector("#buttonStatus");
   analogicValueProgressBar = document.querySelector("#buttonValue");
  requestAnimationFrame(mainloop);
  
  setInterval(scangamepads, 500);
};

function mainloop() {
  // clear, draw objects, etc...
  scangamepads();
  // Check gamepad button states
  checkButtons(gamepad);
  
  // animate at 60 frames/s
  requestAnimationFrame(mainloop);
}


//----------------------------------
// gamepad utility code
//----------------------------------
window.addEventListener("gamepadconnected", function(e) {
   // now as a global var
   gamepad = e.gamepad;
   var index = gamepad.index;
   var id = gamepad.id;
   var nbButtons = gamepad.buttons.length;
   var nbAxes = gamepad.axes.length;
   console.log("Gamepad No " + index +
               ", with id " + id + " is connected. It has " +
               nbButtons + " buttons and " +
               nbAxes + " axes");
});

window.addEventListener("gamepaddisconnected", function(e) {
   var gamepad = e.gamepad;
   var index = gamepad.index;
   console.log("Gamepad No " + index + " has been disconnected");
});


// Detect button states
function checkButtons(gamepad) {
  if(gamepad === undefined) return;
  if(!gamepad.connected) return;
  
  //console.log("t");
  var atLeastOneButtonPressed = false;
 for (var i = 0; i < gamepad.buttons.length; i++) {  
   var b = gamepad.buttons[i];
 
   if(b.pressed) {
     atLeastOneButtonPressed = true;
     buttonStatusDiv.innerHTML = 
      "Button " + i + " is pressed<br>";
     if(b.value !== undefined)
      analogicValueProgressBar.value = b.value;
   }
 }
  
  if(!atLeastOneButtonPressed) {
    buttonStatusDiv.innerHTML = "";
    analogicValueProgressBar.value = 0;
  }
}

function scangamepads() {
  var gamepads = navigator.getGamepads();
  
  for (var i = 0; i < gamepads.length; i++) {
    if(gamepads[i])
        gamepad = gamepads[i]; 
  }
}
