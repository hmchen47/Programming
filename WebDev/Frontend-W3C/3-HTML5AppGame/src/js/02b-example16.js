var gamepad;
var buttonStatusDiv;
var analogicValueProgressBar;
var directionDiv, angleDiv;
var inputStates = {};

window.onload = function() {
  buttonStatusDiv = document.querySelector("#buttonStatus");
   analogicValueProgressBar = document.querySelector("#buttonValue");
   directionDiv = document.querySelector("#direction");
   angleDiv = document.querySelector("#angle");
  requestAnimationFrame(mainloop);
  };

function mainloop() {
  // clear, draw objects, etc...
  scangamepads();
  // Check gamepad button states
  checkButtons(gamepad);
  // Check joysticks
  checkAxes(gamepad);
  
  // Move the player, taking into account
  // the gamepad left joystick state
  updatePlayerPosition();
  
  // We could use the same technique in
  // order to react when buttons are pressed
  //...
  
  // animate at 60 frames/s
  requestAnimationFrame(mainloop);
}

function updatePlayerPosition() {
  directionDiv.innerHTML += "";
  if(inputStates.left) {
    directionDiv.innerHTML = "Moving left";
  } 
  if(inputStates.right) {
    directionDiv.innerHTML = "Moving right";
  } 
  if(inputStates.up) {
    directionDiv.innerHTML = "Moving up";
  } 
  if(inputStates.down) {
    directionDiv.innerHTML = "Moving down";
  } 
  angleDiv.innerHTML = Math.round((inputStates.angle*180/Math.PI));
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

// detect axis (joystick states)
function checkAxes(gamepad) {
  if(gamepad === undefined) return;
  if(!gamepad.connected) return;
 
  var axisValueProgressBars = document.querySelectorAll(".axe");
  
    // update progress bar values
    for (var i=0; i<gamepad.axes.length; i++) {
      var progressBar = axisValueProgressBars[i];
      progressBar.innerHTML = i + ": " + gamepad.axes[i].toFixed(4);
      progressBar.setAttribute("value", gamepad.axes[i] + 1);
    }
  
  // Set inputStates.left, right, up, down
  inputStates.left = inputStates.right = inputStates.up = inputStates.down = false;
  
  // all values between [-1 and 1]
  // Horizontal detection
  if(gamepad.axes[0] > 0.5) {
    inputStates.right=true;
    inputStates.left=false;
  } else if(gamepad.axes[0] < -0.5) {
    inputStates.left=true;
    inputStates.right=false;
  } 
 
  // vertical detection
  if(gamepad.axes[1] > 0.5) {
    inputStates.down=true;
    inputStates.up=false;
  } else if(gamepad.axes[1] < -0.5) {
    inputStates.up=true;
    inputStates.down=false;
  } 

  // compute the angle. gamepad.axes[1] is the 
  // sin of the angle (values between [-1, 1]),
  // gamepad.axes[0] is the cos of the angle
  // we display the value in degree as in a regular
  // trigonometric circle, with the x axis to the right
  // and the y axis that goes up
  // The angle = arcTan(sin/cos); We inverse the sign of
  // the sin in order to have the angle in standard
  // x and y axis (y going up)
  inputStates.angle = Math.atan2(-gamepad.axes[1], gamepad.axes[0]);
  
}
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
