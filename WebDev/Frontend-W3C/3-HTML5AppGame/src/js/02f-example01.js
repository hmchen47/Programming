var spritesWoman = {
	// As many sprites as direction
	// Each element in this array contains n images
	sprites : []
};




DIR_S= 0;
DIR_SW = 1;
DIR_W= 2;
DIR_NW = 3;
DIR_N = 4;
DIR_NE  = 5;
DIR_E = 6;
DIR_SE = 7;

var dir = DIR_S;

var moving = false;
var x = 0;
var y = 0;

var scale = 1;

function mainLoop(timestamp) {

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    if (moving) {
		switch(dir) {
		case DIR_E:
		    x += 6;
		    break;
		case DIR_W:
		    x -= 6;
		    break;
		case DIR_N:
		    y -= 6;
		    break;
		case DIR_S:
		    y += 6;
		}

		scale = 1 + 2 * (y / canvas.height);
    }

    if(!moving) {
        spritesWoman[dir].render(x, y, scale);
	} else {
		spritesWoman[dir].renderMoving(x, y, scale);
	}

	// recall mainLoop every 1/60th of second
    requestAnimationFrame(mainLoop);
}


window.onload = function() {	  
    canvas = document.getElementById("canvas");
    ctx = document.getElementById("canvas").getContext("2d");
  
    // load the spritesheet
    spritesheet = new Image();
    spritesheet.src="https://i.imgur.com/3VesWqx.png";
  
    spritesheet.onload = function() {
      
    // info about spritesheet
	var SPRITE_WIDTH = 48;
	var SPRITE_HEIGHT = 92;
	var NB_DIRECTIONS = 8;
	var NB_FRAMES_PER_POSTURE = 13;

    initSprites(spritesheet, SPRITE_WIDTH, SPRITE_HEIGHT, 
    			NB_DIRECTIONS, NB_FRAMES_PER_POSTURE);
      
      requestAnimationFrame(mainLoop);
    };
    
};

document.onkeydown = function(e) {
    e = e || window.event;

    switch (e.keyCode) {
    case 38:	
	dir = DIR_N;
	moving = true;
	break;
    case 37:
	dir = DIR_W;
	moving = true;
	break;	
    case 39:	
	dir = DIR_E;
	moving = true;
	break;
    case 40:
	dir = DIR_S;
	moving = true;
	break;
    }

};

document.onkeyup = function(e) {
    e = e || window.event;

	moving = false;
};

function SpriteImage(img, x, y, width, height) {
	this.img = img;
	this.x = x;
	this.y = y;
	this.width = width;
	this.height = height;
  
    // xPos and yPos = position where the sprite should be drawn,
    // scale = rescaling factor between 0 and 1
    this.render = function(xPos, yPos, scale) {
          ctx.drawImage(this.img, 
		  this.x, this.y, 
		  this.width, this.height, 
		  xPos, yPos, 
		  this.width*scale, this.height*scale);
    };
}

function Sprite(spritesheet, x, y, width, height, nbImages, nbFramesOfAnimationBetweenRedraws) {
	this.spriteImages = [];
    this.currentFrame = 0;
    this.nbFrames = nbImages;
    this.nbTicksBetweenRedraws = nbFramesOfAnimationBetweenRedraws;
    this.nbCurrentTicks=0;

    // let's process the row in the big image, and extract all sprites for a given posture
    // of animation
	for(var i = 0; i < nbImages; i++) {
		// we extract the subimage
		this.spriteImages[i] = new SpriteImage(spritesheet, x+i*width, y, width, height);
	}

	this.renderMoving = function(x, y, scale) {
		// renders animated sprite, changed every nbTicksBetweenRedraws
		// the frame number
		
		// draw the sprite with the current image
		this.spriteImages[this.currentFrame].render(x, y, scale);

		// increment the number of ticks of animation 
		this.nbCurrentTicks++;

		if(this.nbCurrentTicks > this.nbTicksBetweenRedraws) {
			// enough time elapsed, let's go to the next image
			this.currentFrame++;
			if(this.currentFrame == this.nbFrames) {
				this.currentFrame=0;
			}
			this.nbCurrentTicks = 0;
		}
	};
	this.render = function(x, y, scale) {
		// draws always frame 0, static position
		this.spriteImages[0].render(x, y, scale);
	};
}
function initSprites(spritesheet, spriteWidth, spriteHeight, nbLinesOfSprites, 
						  nbSpritesPerLine) { 	
   
    // sprite extraction
   	for(var i= 0; i < nbLinesOfSprites; i++) {
   		var yLineForCurrentDir = i*spriteHeight;

   		var sprite = new Sprite(spritesheet, 0, yLineForCurrentDir, 
   								spriteWidth, spriteHeight, 
   								nbSpritesPerLine,
   								3); // draw every 1s
   		spritesWoman[i] = sprite;
   	}
}

