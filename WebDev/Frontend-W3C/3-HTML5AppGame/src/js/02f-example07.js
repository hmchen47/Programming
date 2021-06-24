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
      speed:100 // pixels/s this time !
    };
    // Woman object and sprites
    // sprite index corresponding to posture
    var WOMAN_DIR_RIGHT = 6;
    var WOMAN_DIR_LEFT = 2;
    var woman = {
      x:100,
      y:200,
      width:48,
      speed:100, // pixels/s this time !
      direction: WOMAN_DIR_RIGHT 
    };

    var womanSprites = [];
  
      // We want the object to move at speed pixels/s (there are 60 frames in a second)
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
      
        // Draw a woman moving left and right
        womanSprites[woman.direction].draw(ctx, woman.x, woman.y);
        updateWomanPosition(delta);
        // call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };
  
    function updateWomanPosition(delta) {
      
       // check collision on left or right
       if(((woman.x+woman.width) > canvas.width) || (woman.x < 0)) {
       // inverse speed
       woman.speed = -woman.speed;
     }
      
      // change sprite direction
      if(woman.speed >= 0) {
        woman.direction = WOMAN_DIR_RIGHT;
      } else {
         woman.direction = WOMAN_DIR_LEFT;
      }
       woman.x += calcDistanceToMove(delta, woman.speed);
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
      
        // Compute the incX and inY in pixels depending
        // on the time elasped since the last redraw
        monster.x += calcDistanceToMove(delta, monster.speedX);
        monster.y += calcDistanceToMove(delta, monster.speedY);
   }
  
  
    function getMousePos(evt) {
        // necessary to take into account CSS boudaries
        var rect = canvas.getBoundingClientRect();
        return {
            x: evt.clientX - rect.left,
            y: evt.clientY - rect.top
        };
    }
    /*---------------------------------------*/
    /* SPRITE UTILITY FUNCTIONS              */
    /*---------------------------------------*/
  function SpriteImage(img, x, y, width, height) {
   this.img = img;  // the whole image that contains all sprites
   this.x = x;      // x, y position of the sprite image in the whole image
   this.y = y;
   this.width = width;   // width and height of the sprite image
   this.height = height;
   // xPos and yPos = position where the sprite should be drawn,
   // scale = rescaling factor between 0 and 1
   this.draw = function(ctx, xPos, yPos, scale) {
      ctx.drawImage(this.img,
                    this.x, this.y, // x, y, width and height of img to extract
                    this.width, this.height,
                    xPos, yPos,     // x, y, width and height of img to draw
                    this.width*scale, this.height*scale);
   };
}

function Sprite() {
  this.spriteArray = [];
  this.currentFrame = 0;
  this.delayBetweenFrames = 10;
  
  this.extractSprites = function(spritesheet, nbPostures, postureToExtract, nbFramesPerPosture, 
                         spriteWidth, spriteHeight) {
      // number of sprites per row in the spritesheet
      var nbSpritesPerRow = Math.floor(spritesheet.width / spriteWidth);
  
      // Extract each sprite
    var startIndex = (postureToExtract-1) * nbFramesPerPosture;
    var endIndex = startIndex + nbFramesPerPosture;
      for(var index = startIndex; index < endIndex; index++) {
          // Computation of the x and y position that corresponds to the sprite
          // index
          // x is the rest of index/nbSpritesPerRow * width of a sprite
          var x = (index % nbSpritesPerRow) * spriteWidth;
          // y is the divisor of index by nbSpritesPerRow * height of a sprite
          var y = Math.floor(index / nbSpritesPerRow) * spriteHeight;
    
          // build a spriteImage object
          var s = new SpriteImage(spritesheet, x, y, spriteWidth, spriteHeight);
    
          this.spriteArray.push(s);
      }
  };
  
  this.then = performance.now();
  this.totalTimeSinceLastRedraw = 0;
  
  this.drawStopped = function(ctx, x, y) {
    var currentSpriteImage = this.spriteArray[this.currentFrame];
     currentSpriteImage.draw(ctx, x, y, 1);
    
  };
  
  this.draw = function(ctx, x, y) {
    // Use time based animation to draw only a few images per second
    var now = performance.now();
    var delta = now - this.then;
    
    // draw currentSpriteImage
    var currentSpriteImage = this.spriteArray[this.currentFrame];
    // x, y, scale. 1 = size unchanged
    currentSpriteImage.draw(ctx, x, y, 1);
    
    // if the delay between images is elapsed, go to the next one
    if (this.totalTimeSinceLastRedraw > this.delayBetweenFrames) {
       // Go to the next sprite image
      this.currentFrame++; 
      this.currentFrame %=  this.spriteArray.length;
      
      // reset the total time since last image has been drawn
      this.totalTimeSinceLastRedraw = 0;
    } else {
      // sum the total time since last redraw
     this. totalTimeSinceLastRedraw += delta;
    }
    
    this.then = now;
  };
  
  this.setNbImagesPerSecond = function(nb) {
    // elay in ms between images
    this.delayBetweenFrames = 1000 / nb;
  };
}
    /*---------------------------------------*/
    /* EN OF SPRITE UTILITY FUNCTIONS        */
    /*---------------------------------------*/
  
   
    var loadAssets = function(callback) {
      var SPRITESHEET_URL = "http://i.imgur.com/3VesWqx.png";
      var SPRITE_WIDTH = 48;
      var SPRITE_HEIGHT = 92;
      var NB_POSTURES=8;
      var NB_FRAMES_PER_POSTURE = 13;
      
      // load the spritesheet
      var spritesheet = new Image();
      spritesheet.src = SPRITESHEET_URL;      
    
      // Called when the spritesheet has been loaded
      spritesheet.onload = function() {
             
         // Create woman sprites
         for(var i = 0; i < NB_POSTURES; i++) {
            var sprite = new Sprite();
      
            sprite.extractSprites(spritesheet, NB_POSTURES, (i+1), 
                                  NB_FRAMES_PER_POSTURE, 
                                  SPRITE_WIDTH, SPRITE_HEIGHT);
            sprite.setNbImagesPerSecond(20);
            womanSprites[i] = sprite;
         }
         // call the callback function passed as a parameter, 
         // we're done with loading assets and building the sprites
         callback();
      };
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

      // Load sounds and images, then when this is done, start the mainLoop
      loadAssets(function() {
        // when enter here only when all assets have been loaded
        requestAnimationFrame(mainLoop);
      });
    };

    //our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};

