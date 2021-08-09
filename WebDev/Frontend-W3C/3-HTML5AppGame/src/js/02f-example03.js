var SPRITESHEET_URL = "https://i.imgur.com/PABuFc6.png";
var SPRITE_WIDTH = 275;
var SPRITE_HEIGHT = 275;
var NB_POSTURES=1;
var NB_FRAMES_PER_POSTURE = 16;

var xField, yField, wField, hField, spriteSelect, spriteNumber;

var canvas, canvasSpriteSheet, ctx1, ctx2;


window.onload = function() {	  
    canvas = document.getElementById("canvas");
    ctx1 = canvas.getContext("2d");
  canvasSpriteSheet = document.getElementById("spritesheet");
    ctx2 = canvasSpriteSheet.getContext("2d");
  
  
    xField = document.querySelector("#x");
    yField = document.querySelector("#y");
    wField = document.querySelector("#width");
    hField = document.querySelector("#height");
    spriteSelect = document.querySelector("#spriteSelect");
    spriteNumber = document.querySelector("#spriteNumber");
  
    wField.value = SPRITE_WIDTH;
    hField.value = SPRITE_HEIGHT;
    xField.value = 0;
    yField.value = 0;
  
    spriteSelect.min = 0;
    spriteSelect.max=NB_POSTURES*NB_FRAMES_PER_POSTURE - 1;
  
    spriteSelect.disabled = true;
    spriteNumber.innerHTML=0;
  
    // load the spritesheet
    spritesheet = new Image();
    spritesheet.src = SPRITESHEET_URL;      
    
  // Called when the spritesheet has been loaded
    spritesheet.onload = function() {
      // enable slider
      spriteSelect.disabled = false;
      
      // Resize big canvas to the size of the spritesheet image
      canvasSpriteSheet.width = spritesheet.width;
       canvasSpriteSheet.height = spritesheet.height;
       // Resize small canvas to the size of the spritesheet image
      canvas.width = SPRITE_WIDTH;
       canvas.height = SPRITE_HEIGHT;
      
      
      // Draw the whole spritesheet
      ctx2.drawImage(spritesheet, 0, 0);
      // Draw the first sprite in the small canvas, corresponding to sprite 0
      // wireframe rectangle in the sprite sheet
      drawWireFrameRect(ctx2, 0 , 0, SPRITE_WIDTH, SPRITE_HEIGHT, 'red', 3);
      // small canvas, draw subimage corresponding to sprite 0
      ctx1.drawImage(spritesheet, 0, 0, SPRITE_WIDTH, SPRITE_HEIGHT, 0, 0, SPRITE_WIDTH, SPRITE_HEIGHT);
    };
  
     // input listener on the 
      spriteSelect.oninput = function(evt) {
          // Current sprite number from 0 to NB_FRAMES_PER_POSTURE * NB_ROWS
          var index = spriteSelect.value;
    
          var nbSpritesPerRow = Math.floor(spritesheet.width / SPRITE_WIDTH);
        
        
          // Computation of the x and y position that corresponds to the sprite
          // number index
          // x is the rest of index/nbSpritesPerRow * width of a sprite
          var x = (index % nbSpritesPerRow) * SPRITE_WIDTH;
          // y is the divisor of index by nbSpritesPerRow * height of a sprite
          var y = Math.floor(index / nbSpritesPerRow) * SPRITE_HEIGHT;
                
          // update fields
          xField.value = x;
          yField.value = y;
      
          // Clear big canvas, draw wireframe rect at x, y, redraw stylesheet
          ctx2.clearRect(0, 0, canvasSpriteSheet.width, canvasSpriteSheet.height);
          ctx2.drawImage(spritesheet, 0, 0);
          drawWireFrameRect(ctx2, x , y, SPRITE_WIDTH, SPRITE_HEIGHT, 'red', 3);

          // Draw current sprite in the small canvas
          ctx1.clearRect(0, 0, SPRITE_WIDTH, SPRITE_HEIGHT);
          ctx1.drawImage(spritesheet, x, y, SPRITE_WIDTH, SPRITE_HEIGHT,
                    0, 0, SPRITE_WIDTH, SPRITE_HEIGHT);

          // Update output elem on the right of the slider
          spriteNumber.innerHTML = index;
    };
};

function drawWireFrameRect(ctx, x, y, w, h, color, lineWidth) {
    ctx.save();
    ctx.strokeStyle = 'red';
    ctx.lineWidth = lineWidth;
    ctx.strokeRect(x , y, w, h);
    ctx.restore();
}

