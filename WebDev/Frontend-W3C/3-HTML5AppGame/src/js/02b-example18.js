// Inits
window.onload = function init() {
  var game = new GF();
  game.start();
};


// GAME FRAMEWORK STARTS HERE
var GF = function(){
    // Vars relative to the canvas
    var canvas, ctx, w, h; 
    var gamepad;
  
    // vars for counting frames/s, used by the measureFPS function
    var frameCount = 0;
    var lastTime;
    var fpsContainer;
    var fps; 
  
    // vars for handling inputs
    var inputStates = {};
  
    // The monster !
    var monster = {
      x:10,
      y:10,
      speed:1
    };
  
    var measureFPS = function(newTime){
      
         // test for the very first invocation
         if(lastTime === undefined) {
           lastTime = newTime; 
           return;
         }
      
        //calculate the difference between last & current frame
        var diffTime = newTime - lastTime; 

        if (diffTime >= 1000) {
            fps = frameCount;    
            frameCount = 0;
            lastTime = newTime;
        }

        //and display it in an element we appended to the 
        // document in the start() function
       fpsContainer.innerHTML = 'FPS: ' + fps; 
       frameCount++;
    };
  
     // clears the canvas content
     function clearCanvas() {
       ctx.clearRect(0, 0, w, h);
     }
  
     // Functions for drawing the monster and maybe other objects
     function drawMyMonster(x, y) {
       // draw a big monster !
       // head
   
       // save the context
       ctx.save();
  
       // translate the coordinate system, draw relative to it
       ctx.translate(x, y);
  
       // (0, 0) is the top left corner of the monster.
       ctx.strokeRect(0, 0, 100, 100);
  
       // eyes
       ctx.fillRect(20, 20, 10, 10);
       ctx.fillRect(65, 20, 10, 10);
  
       // nose
       ctx.strokeRect(45, 40, 10, 40);
  
       // mouth
       ctx.strokeRect(35, 84, 30, 10);
  
       // teeth
       ctx.fillRect(38, 84, 10, 10);
       ctx.fillRect(52, 84, 10, 10);
  
      // restore the context
      ctx.restore(); 
    }
  
    var mainLoop = function(time){
        //main function, called each frame 
        measureFPS(time);
      
        // Clear the canvas
        clearCanvas();
        
        // gamepad
        updateGamePadStatus();
      
        // draw the monster
        drawMyMonster(monster.x, monster.y);
      
        // Check inputs and move the monster
        updateMonsterPosition();
 
        // call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };
  
    
    function updateMonsterPosition() {
      monster.speedX = monster.speedY = 0;
        // check inputStates
        if (inputStates.left) {
            ctx.fillText("left", 150, 20);
            monster.speedX = -monster.speed;
        }
        if (inputStates.up) {
            ctx.fillText("up", 150, 40);
           monster.speedY = -monster.speed;
        }
       if (inputStates.right) {
            ctx.fillText("right", 150, 60);
            monster.speedX = monster.speed;
        }
        if (inputStates.down) {
            ctx.fillText("down", 150, 80);
            monster.speedY = monster.speed;
        } 
        if (inputStates.space) {
            ctx.fillText("space bar", 140, 100);
        }
        if (inputStates.mousePos) { 
            ctx.fillText("x = " + inputStates.mousePos.x + " y = " + inputStates.mousePos.y, 5, 150);
        }
       if (inputStates.mousedown) { 
            ctx.fillText("mousedown b" + inputStates.mouseButton, 5, 180);
            monster.speed = 5;
        } else {
          // mouse up
          monster.speed = 1;
        }
      
        monster.x += monster.speedX;
        monster.y += monster.speedY;
      
    }
  
  
    function getMousePos(evt) {
        // necessary to take into account CSS boudaries
        var rect = canvas.getBoundingClientRect();
        return {
            x: evt.clientX - rect.left,
            y: evt.clientY - rect.top
        };
    }
  
  //----------------------------------
  // gamepad utility code
  //----------------------------------
  
  function updateGamePadStatus() {
    // get new snapshot of the gamepad properties
    scangamepads();
  // Check gamepad button states
  checkButtons(gamepad);
  // Check joysticks
  checkAxes(gamepad);
  }
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
  
  // Set inputStates.left, right, up, down
  inputStates.left = inputStates.right = inputStates.up =   inputStates.down = false;
  
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
  // in this function we should add properties to the
  // inputStates object in order to use gamepad buttons
  if(gamepad === undefined) return;
  if(!gamepad.connected) return;
  
 for (var i = 0; i < gamepad.buttons.length; i++) {  
   var b = gamepad.buttons[i];
 
   if(b.pressed) {
     // do something
     console.log("button pressed");
     if(b.value !== undefined)
      // do something
       console.log("analog button pressed");
   }
 }
}

function scangamepads() {
  var gamepads = navigator.getGamepads();
  
  for (var i = 0; i < gamepads.length; i++) {
    if(gamepads[i])
        gamepad = gamepads[i]; 
  }
}
      
    var start = function(){
        // adds a div for displaying the fps value
        fpsContainer = document.createElement('div');
        document.body.appendChild(fpsContainer);
      
        // Canvas, context etc.
        canvas = document.querySelector("#myCanvas");
  
        // often useful
        w = canvas.width; 
        h = canvas.height;  
  
        // important, we will draw with this object
        ctx = canvas.getContext('2d');
        // default police for text
        ctx.font="20px Arial";
      
       //add the listener to the main, window object, and update the states
      window.addEventListener('keydown', function(event){
          if (event.keyCode === 37) {
             inputStates.left = true;
          } else if (event.keyCode === 38) {
             inputStates.up = true;
          } else if (event.keyCode === 39) {
             inputStates.right = true;
          } else if (event.keyCode === 40) {
             inputStates.down = true;
          }  else if (event.keyCode === 32) {
             inputStates.space = true;
          }
      }, false);

      //if the key will be released, change the states object 
      window.addEventListener('keyup', function(event){
          if (event.keyCode === 37) {
             inputStates.left = false;
          } else if (event.keyCode === 38) {
             inputStates.up = false;
          } else if (event.keyCode === 39) {
             inputStates.right = false;
          } else if (event.keyCode === 40) {
             inputStates.down = false;
          } else if (event.keyCode === 32) {
             inputStates.space = false;
          }
      }, false);
      
      // Mouse event listeners
      canvas.addEventListener('mousemove', function (evt) {
          inputStates.mousePos = getMousePos(evt);
      }, false);

      canvas.addEventListener('mousedown', function (evt) {
            inputStates.mousedown = true;
            inputStates.mouseButton = evt.button;
      }, false);

      canvas.addEventListener('mouseup', function (evt) {
          inputStates.mousedown = false;
      }, false);      


        // start the animation
        requestAnimationFrame(mainLoop);
    };

    //our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};


