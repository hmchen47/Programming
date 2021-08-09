var SPRITESHEET_URL = "http://i.imgur.com/3VesWqx.png";
var SPRITE_WIDTH = 48;
var SPRITE_HEIGHT = 92;
var NB_POSTURES=8;
var NB_FRAMES_PER_POSTURE = 13;


var canvas, ctx;
var spritesheet;
var woman = [];
var inputStates = {};
var currentDirection = 0;
// postures number corresponds to directions
var DIR_LEFT = 2;
var DIR_RIGHT = 6;
var speedX = 0;
var posX = 100;

window.onload = function() {	  
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
  
    // load the spritesheet
    spritesheet = new Image();
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
        woman[i] = sprite;
      }

      requestAnimationFrame(mainloop);
      
   // Add the listener to the main, window object, and update the states
    window.addEventListener('keydown', function(event){
      if (event.keyCode === 37) {
        inputStates.left = true;
      } else if (event.keyCode === 38) {
        inputStates.up = true;
      } else if (event.keyCode === 39) {
        inputStates.right = true;
      } else if (event.keyCode === 40) {
        inputStates.down = true;
      } else if (event.keyCode === 32) {
        inputStates.space = true;
      }
    }, false);
    // If the key is released, change the states object
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

    }; // onload
};

function mainloop() {
  // clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
   // check inputStates
   speedX = 0;
    if (inputStates.left) {
      speedX = -1;
      currentDirection = DIR_LEFT;
    }
   
   if (inputStates.right) {
     speedX = 1;
     currentDirection = DIR_RIGHT;
   }

    if(speedX === 0)
      woman[currentDirection].drawStopped(ctx, posX, 100, 1);
    else 
      woman[currentDirection].draw(ctx, posX, 100, 1);
  
    posX+= speedX;
  
  requestAnimationFrame(mainloop);
}

// ------------------------
// Sprite utility functions
// ------------------------
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

