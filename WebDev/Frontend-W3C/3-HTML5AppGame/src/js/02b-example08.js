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
        
        // draw the monster
        drawMyMonster(10+Math.random()*10, 10+Math.random()*10);
      
        // call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };

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

        // start the animation
        requestAnimationFrame(mainLoop);
    };

    //our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};

