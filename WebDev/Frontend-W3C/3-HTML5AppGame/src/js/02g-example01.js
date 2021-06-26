// Inits
window.onload = function init() {
  var game = new GF();
  game.start();
};


// GAME FRAMEWORK STARTS HERE
var GF = function(){
    // Vars relative to the canvas
    var canvas, ctx, w, h; 

    // vars for counting frames/s, used by the measureFPS function
    var frameCount = 0;
    var lastTime;
    var fpsContainer;
    var fps; 
    // for time based animation
    var delta, oldTime = 0;
  
    // vars for handling inputs
    var inputStates = {};
  
    // The monster !
    var monster = {
      x:10,
      y:10,
      width:100,
      height:100,
      speed:100, // pixels/s this time !
    };
  
    // array of balls to animate
    var ballArray = [];
    var nbBalls = 5;
    var currentScore = 0;
  
      // We want the rectangle to move at speed pixels/s (there are 60 frames in a second)
    // If we are really running at 60 frames/s, the delay between frames should be 1/60
    // = 16.66 ms, so the number of pixels to move = (speed * del)/1000. If the delay is twice
    // longer, the formula works : let's move the rectangle twice longer!
  var calcDistanceToMove = function(delta, speed) {
    //console.log("#delta = " + delta + " speed = " + speed);
    return (speed * delta) / 1000; 
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
  
  function timer(currentTime) {
    var delta = currentTime - oldTime;
    oldTime = currentTime;
    return delta;
    
  }
    var mainLoop = function(time){
        //main function, called each frame 
        measureFPS(time);
      
        // number of ms since last frame draw
        delta = timer(time);
      
        // Clear the canvas
        clearCanvas();
       
        // draw the monster
        drawMyMonster(monster.x, monster.y);
      
        // Check inputs and move the monster
        updateMonsterPosition(delta);
 
        // update and draw balls
        updateBalls(delta);
      
        // display Score
        displayScore();

      
        // call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };
  
    function displayScore() {
      ctx.save();
      ctx.fillStyle = 'Green';
       ctx.fillText("Score: " + currentScore, 300, 30);
      ctx.restore();
    }
    function updateMonsterPosition(delta) {
      monster.speedX = monster.speedY = 0;
        // check inputStates
        if (inputStates.left) {
            monster.speedX = -monster.speed;
        }
        if (inputStates.up) {
           monster.speedY = -monster.speed;
        }
       if (inputStates.right) {
            monster.speedX = monster.speed;
        }
        if (inputStates.down) {
            monster.speedY = monster.speed;
        } 
        if (inputStates.space) {
        }
        if (inputStates.mousePos) { 
        }
       if (inputStates.mousedown) { 
            monster.speed = 500;
        } else {
          // mouse up
          monster.speed = 100;
        }
      
        // COmpute the incX and inY in pixels depending
        // on the time elasped since last redraw
        monster.x += calcDistanceToMove(delta, monster.speedX);
        monster.y += calcDistanceToMove(delta, monster.speedY);
   }
  
 function updateBalls(delta) {
      // for each ball in the array
   var allBallDead = true;
   
    for(var i=0; i < ballArray.length; i++) {
      var ball = ballArray[i];
      
      if(ball.dead) continue;
      
      // The ball is not dead
      allBallDead = false;
      
      // 1) move the ball
      ball.move();   
  
      // 2) test if the ball collides with a wall
      testCollisionWithWalls(ball);

      // Test if the monster collides
      if(circRectsOverlap(monster.x, monster.y, 
                          monster.width, monster.height, 
                          ball.x, ball.y, ball.radius)) {
                            
        //change the color of the ball
        ball.color = 'red';
        ball.dead = true;
        // Here, a sound effect would greatly improve
        // the experience!
        
        currentScore+= 1;
      }
  
      // 3) draw the ball
      ball.draw();
  }
   
   if(allBallDead) {
     // reset all balls, create more balls each time
     // sort of increasing the difficulty
     nbBalls++;
      createBalls(nbBalls);
   }
} 
  
      // Collisions between rectangle and circle
      function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {
          var testX=cx; 
          var testY=cy; 
          
          if (testX < x0) testX=x0; 
          if (testX > (x0+w0)) testX=(x0+w0); 
          if (testY < y0) testY=y0; 
          if (testY > (y0+h0)) testY=(y0+h0); 
 
          return (((cx-testX)*(cx-testX)+(cy-testY)*(cy-testY))<r*r); 
      }

  
  function testCollisionWithWalls(ball) {
    // left
    if (ball.x < ball.radius) {
        ball.x = ball.radius;
        ball.angle = -ball.angle + Math.PI;
    } 
    // right
    if (ball.x > w - (ball.radius)) {
        ball.x = w - (ball.radius);
        ball.angle = -ball.angle + Math.PI; 
    }     
    // up
    if (ball.y < ball.radius) {
        ball.y = ball.radius;
        ball.angle = -ball.angle;     
    }     
    // down
    if (ball.y > h - (ball.radius)) {
        ball.y = h - (ball.radius);
        ball.angle =-ball.angle; 
    } 
}
  
    function getMousePos(evt) {
        // necessary to take into account CSS boudaries
        var rect = canvas.getBoundingClientRect();
        return {
            x: evt.clientX - rect.left,
            y: evt.clientY - rect.top
        };
    }
      
  function createBalls(numberOfBalls) {
      for(var i=0; i < numberOfBalls; i++) {
        // Create a ball with random position and speed. 
        // You can change the radius
        var ball =  new Ball(w*Math.random(),
                          h*Math.random(),
                          (2*Math.PI)*Math.random(),        
                          (80*Math.random()),
                          30);
        
        // Do not create a ball on the player
        if(!circRectsOverlap(monster.x, monster.y, 
                          monster.width, monster.height, 
                          ball.x, ball.y, ball.radius)) {
          // Add it to the array
        ballArray[i] = ball;
        } else {
          i--;
        }
    
        
      }
   }                                
// constructor function for balls
function Ball(x, y, angle, v, diameter) {
  this.x = x;
  this.y = y;
  this.angle = angle;
  this.v = v;
  this.radius = diameter/2;
  this.color = 'black';
  this.dead = false;
  
  this.draw = function() {    
      ctx.save();
      ctx.beginPath();
      ctx.fillStyle = this.color;
      ctx.arc(this.x, this.y, this.radius, 0, 2*Math.PI);
      ctx.fill();
    ctx.restore();
    this.color = 'black';
  };
  
  this.move = function() {    
    // add horizontal increment to the x pos
    // add vertical increment to the y pos
    
    var incX = this.v * Math.cos(this.angle);
    var incY = this.v * Math.sin(this.angle);
    
    this.x += calcDistanceToMove(delta, incX);
    this.y += calcDistanceToMove(delta, incY);
  };
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

        // We create tge balls: try to change the parameter
        createBalls(nbBalls); 

        // start the animation
        requestAnimationFrame(mainLoop);
    };

    //our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};


