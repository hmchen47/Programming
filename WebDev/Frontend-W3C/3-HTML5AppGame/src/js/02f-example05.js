var SPRITESHEET_URL = "http://i.imgur.com/3VesWqx.png";
var SPRITE_WIDTH = 48;
var SPRITE_HEIGHT = 92;
var NB_POSTURES=8;
var NB_FRAMES_PER_POSTURE = 13;


var canvas, ctx;
var spritesheet;
var woman;

window.onload = function() {	  
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
  
    // load the spritesheet
    spritesheet = new Image();
    spritesheet.src = SPRITESHEET_URL;      
    
    // Called when the spritesheet has been loaded
    spritesheet.onload = function() {
      
      // Resize small canvas to the size of the spritesheet image
      canvas.width = SPRITE_WIDTH;
      canvas.height = SPRITE_HEIGHT;
       
      // get the sprite array
      woman = new Sprite();
      
      woman.extractSprites(spritesheet, NB_POSTURES, 1, 
                               NB_FRAMES_PER_POSTURE, 
                               SPRITE_WIDTH, SPRITE_HEIGHT);
      woman.setNbImagesPerSecond(20);
      
      requestAnimationFrame(mainloop);
    }; // onload
};

function mainloop() {
  // clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // draw sprite at 0, 0 in the small canvas
  woman.draw(ctx, 0, 0, 1);
  
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

