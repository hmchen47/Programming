  //-----------------------------------------------------------------------------
  // vars for counting frames/s, used by the measureFPS function
    var frameCount = 0;
    var lastTime;
    var fpsContainer;
    var fps;

    var initFPSCounter = function() {
        // adds a div for displaying the fps value
        fpsContainer = document.createElement('div');
        document.body.appendChild(fpsContainer);
    }
    
    var measureFPS = function (newTime) {

        // test for the very first invocation
        if (lastTime === undefined) {
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
     //   fpsContainer.innerHTML = 'FPS: ' + fps;
        frameCount++;
    };
    //------------------------------------------------------------------------------------
    //timeBaseAnimation
    var delta, oldTime = 0;

    function timer(currentTime) {
        var delta = currentTime - oldTime;
        oldTime = currentTime;
        return delta;
    }

    var calcDistanceToMove = function (delta, speed) {
        //console.log("#delta = " + delta + " speed = " + speed);
        return (speed * delta) / 1000;
     };
    //-------------------------------------------------------------------------------------
    //listeners
    function addListeners(inputStates, canvas) {
        //add the listener to the main, window object, and update the states
        window.addEventListener('keydown', function (event) {
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
            } else if (event.keyCode === 13) {
                inputStates.enter = true;
            }
        }, false);

        //if the key will be released, change the states object 
        window.addEventListener('keyup', function (event) {
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
            }else if (event.keyCode === 13) {
                inputStates.enter = false;
            }
        }, false);

        // Mouse event listeners
        canvas.addEventListener('mousemove', function (evt) {
            inputStates.mousePos = getMousePos(evt, canvas);
        }, false);

        canvas.addEventListener('mousedown', function (evt) {
            inputStates.mousedown = true;
            inputStates.mouseButton = evt.button;
        }, false);

        canvas.addEventListener('mouseup', function (evt) {
            inputStates.mousedown = false;
        }, false);
}

function getMousePos(evt, canvas) {
    // necessary to take into account CSS boudaries
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}
//------------------------------------------------------------------------------
// We can add the other collision functions seen in the
   // course here...
   
   // Collisions between rectangle and circle
    function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {
        var testX = cx;
        var testY = cy;

        if (testX < x0)
            testX = x0;
        if (testX > (x0 + w0))
            testX = (x0 + w0);
        if (testY < y0)
            testY = y0;
        if (testY > (y0 + h0))
            testY = (y0 + h0);

        return (((cx - testX) * (cx - testX) + (cy - testY) * (cy - testY)) < r * r);
    }
// Collisions between aligned rectangles
function rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2) {
 
  if ((x1 > (x2 + w2)) || ((x1 + w1) < x2))
     return false; // No horizontal axis projection overlap
  if ((y1 > (y2 + h2)) || ((y1 + h1) < y2))
     return false; // No vertical axis projection overlap
   // console.log("x1="+x1+"  y1="+y1+"  w1="+w1+"  h1="+h1);
   // console.log("x2="+x2+"  y2="+y2+"  w2="+w2+"  h2="+h2);
  return true; // If previous tests failed, then both axis projections
               // overlap and the rectangles intersect
}

    function testCollisionWithWalls(ball, w, h) {
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
            ball.angle = -ball.angle;
        }
    }
    //-----------------------------------------------------------------------------
    // Sprite utility functions
    // ------------------------
function SpriteImage(img, x, y, width, height,scale) {
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
                                            //кол-во поз,     поза для выделения, кол-во кадров на позу
  this.extractSprites = function(spritesheet, /*nbPostures,*/ postureToExtract, nbFramesPerPosture, 
                      //кол-во колонок в листе,кол-во строк в листе
                          nb_column_sheet,nb_string_sheet) {
      // number of sprites per row in the spritesheet

       spriteHeight=Math.floor(spritesheet.height/ nb_string_sheet); //высота фрейма
       spriteWidth =Math.floor(spritesheet.width / nb_column_sheet);
      var nbSpritesPerRow = Math.floor(spritesheet.width / spriteWidth); //кол-во фреймов в строке
    /* 
      console.log("spritesheet.width="+spritesheet.width);
      console.log("spritesheet.height="+spritesheet.height);

      console.log("spriteWidth="+spriteWidth);

      console.log("spriteHeight="+spriteHeight);

      console.log("nbSpritesPerRow="+nbSpritesPerRow);
      */
      // Extract each sprite
    var startIndex = (postureToExtract-1); // * nbFramesPerPosture;
 
    var endIndex = startIndex + nbFramesPerPosture;
      for(var index = startIndex; index < endIndex; index++) {
          // Computation of the x and y position that corresponds to the sprite
          // index
          // x is the rest of index/nbSpritesPerRow * width of a sprite
          var x = (index % nbSpritesPerRow) * spriteWidth;
          // y is the divisor of index by nbSpritesPerRow * height of a sprite
          var y = Math.floor(index / nbSpritesPerRow) * spriteHeight;
     //  console.log("x="+x);
     //  console.log("y="+y);
          // build a spriteImage object
          var s = new SpriteImage(spritesheet, x, y, spriteWidth, spriteHeight);
    
          this.spriteArray.push(s);
      }
  };
  
  this.then = performance.now();
  this.totalTimeSinceLastRedraw = 0;
  
  this.drawStopped = function(ctx, x, y,scale) {
    var currentSpriteImage = this.spriteArray[this.currentFrame];
     currentSpriteImage.draw(ctx, x, y, scale);
  };
  
  this.draw = function(ctx, x, y,scale) {
    // Use time based animation to draw only a few images per second
    var now = performance.now();
    var delta = now - this.then;
    
    // draw currentSpriteImage
    var currentSpriteImage = this.spriteArray[this.currentFrame];
    // x, y, scale. 1 = size unchanged
    currentSpriteImage.draw(ctx, x, y, scale);
 /*   console.log("x="+x);
    console.log("y="+y);*/
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
//--------------------------------------------------------------
// game objects


        function Rocket(x,y,width,height,img,img2,speed){
       this.x=x;
       this.y=y;
       this.width=width;
       this.height=height;
       this.picture = img;
       this.picture2 = img2;
       this.speed = speed;
       this.crash = false;
       this.maxHitpoint = 3;
       this.hitpoint = 3;
       this.hitRocket = false;
       this.timeAfterHit = 500;

        this.decreaseHit = function(){
        this.hitpoint --;
        return this.hitpoint;
      };

       this.draw = function(ctx,w,h){
   
    if (this.x < -20) { this.x = -20;}
    if (this.x > w - this.width +20) {this.x = w- this.width+20;}
    
    if (this.y > h - this.height) {this.y =h- this.height;}
    if (this.y < 0) {this.y = 0;}

                if(this.hitRocket === true)  {this.picture2.draw(ctx,this.x,this.y,1);}
                                     else    {this.picture.draw(ctx, this.x, this.y,1);}
       // this.picture.draw(ctx, this.x, this.y,1);
    };
}

  function drawFire(fires,ctx) {
    if (fires.length) {
      for (var i = 0; i < fires.length; i++) {
        ctx.save();
       // ctx.translate(0, -32);
        ctx.lineWidth = 3;
        ctx.lineCap = "round";
        ctx.strokeStyle = "rgba(255, 255, 255, 0.7)";
        ctx.shadowBlur = 10;
        ctx.shadowColor = "rgba(255, 255, 255, 0.6)";
        ctx.beginPath();
        ctx.moveTo(fires[i][0], fires[i][1]);
        ctx.lineTo(fires[i][0], fires[i][1] - 10);
        ctx.stroke();
        ctx.restore();
      }
    }
  }
  
  function moveFire(fires,hit,yTarget) {
  //  console.log("kill="+kill+" yTarget="+yTarget);
  //for
    if(hit!==true) 
    for (var i = 0; i < fires.length; i++) {
          if (fires[i][1] >= 32) {  //если коор-та "y" огня >=32,то двигать огонь по 5 пикселей вверх 
          fires[i][1] -= 5;
          } else 
          fires.splice(i, 1); //с i удалить 1 эл-т           
    }
    else { fires.splice(i, 1);}       
 }// moveFire(fires)

   function Bomb(x,y,r,speed,dx,dy){
    this.x=x+40;
    this.y=y+80;
    this.r=r;
    this.speed=speed;
    this.dx=dx;
    this.dy=dy;
    this.remove = false;

    this.draw = function(ctx){
   // for (var i = 0; i < 5; i++) {   
    ctx.save();
    ctx.beginPath(); 
    ctx.strokeStyle="rgb(255,145,110)";
    ctx.fillStyle="rgb(243,91,61)";
    ctx.arc(this.x,this.y,this.r,0,2*Math.PI);
    ctx.stroke();
    ctx.fill();
    ctx.restore();
   //  }//for
    }//draw bomb

    this.move = function (h) {

    this.y += this.dy*calcDistanceToMove(delta, this.speed);
    this.x += this.dx*calcDistanceToMove(delta, this.speed/10);
    if(this.y > h){
      return this.remove = true;
    }
            };//move
   }//bomb

   function Bullet(index,x,y,r,speed,dx,dy,time){
    this.index = index;
    this.x=x;
    this.y=y;
    this.r=r;
    this.speed=speed;
    this.dx=dx;
    this.dy=dy;
    this.time = time;
    this.remove = false;

    this.draw = function(ctx){  
    ctx.save();
    ctx.beginPath(); 
    ctx.strokeStyle="rgb(245,142,255)";
    ctx.fillStyle="rgb(155,0,166)";
    ctx.arc(this.x,this.y,this.r,0,2*Math.PI);
    ctx.stroke();
    ctx.fill();
    ctx.restore();
    }//draw bomb

    this.move = function (h,delta) {

    this.y += calcDistanceToMove(delta, this.speed);
    this.x += this.dx*calcDistanceToMove(delta, this.speed/10);
    if(this.y > h){
      return this.remove = true;
    }
            };//move
   }//bomb


   function Stranger(x,y,rectW,rectH,img,img2,speed){
    this.x=x;
    this.y=y;
    this.speed=speed;
    this.width=rectW;
    this.height=rectH;
    this.picture = img; //new SpriteImage(img,0,80,74,80);//img;
    this.picture2= img2;
    this.speed = speed;
    this.crash = false;
    this.hitpoint = 3;
    this.hitStranger = false; 
    this.timeAfterHit = 100;

    this.draw = function(ctx){
                if(this.hitStranger === true){this.picture2.draw(ctx,this.x,this.y,1);}
                                     else    {this.picture.draw(ctx, this.x, this.y,1);}
              };

    this.move = function (rocketX,rocketW) {
        var centerRocket=rocketX+ rocketW/2;
        if(centerRocket+5 < this.x+rectW/2){
            this.x -= calcDistanceToMove(delta, this.speed);
            } else if(centerRocket-5 > this.x+rectW/2){
               this.x += calcDistanceToMove(delta, this.speed);
            }

      };//move
      this.decreaseHit = function(){
        this.hitpoint --;
        return this.hitpoint;
      };
   } 
  function CrashStranger(begined,x,y,img,time){
    this.begined = begined;
    this.x=x;
    this.y=y;
    this.picture = img; //new SpriteImage(img,0,80,74,80);//img;
    this.time = time;
     
    this.draw = function(ctx){
                this.picture.draw(ctx, this.x, this.y,1);
              }
   }

   function CrashBlock(begined,x,y,img,time){
    this.begined = begined;
    this.x=x;
    this.y=y;
    this.picture = img; //new SpriteImage(img,0,80,74,80);//img;
    this.time = time;
     
    this.draw = function(ctx){
                this.picture.draw(ctx, this.x, this.y,1);
              }
   }

    function Block(x,y,speed,rectW,rectH,opt,worked,sheet,gun){

    this.blockX=x;
    this.blockY=y;
    this.rectW=rectW;
    this.rectH=rectH;
    this.speed=speed;
    this.optName = opt;
    this.opt={};
    this.worked=worked;
    this.crashColor = false;
    this.gun = gun;
    


    this.setHit = function(){
    if(this.optName == "optNormal"){
       this.hitpoint = 1;
    } else if(this.optName == "optYellow"){
      this.hitpoint = 2;
    } else if (this.optName == "optRed") {
      this.hitpoint = 2;
    } 

    return this.hitpoint;
  }
  this.countHit = function(){   
      this.hitpoint --;    
    return this.hitpoint;
  }

 
    this.draw = function (ctx){
     if (this.optName === "optNormal") {
      this.opt = {
    "colorFill":"rgb(50, 120, 225)",
    "colorShadow":"rgb(70, 60, 225)",
    "colorStroke":"rgb(120, 190, 225)",
    "colorStrokeShadow":"rgb(152, 123, 225)",
    "hitpoint":1
      }
    } else if(this.optName === "optYellow"){
       this.opt = {    
    "colorFill":"rgb(30, 233, 159)",
    "colorShadow":"rgb(5, 146, 90)",
    "colorStroke":"rgb(100, 250, 222)",
    "colorStrokeShadow":"rgb(9, 190, 160)",
    "hitpoint":2
      }
    }  else if(this.optName === "optRed"){
      this.opt = {
       "colorFill":"rgb(239, 105, 158)",
    "colorShadow":"rgb(210, 25, 85)",
    "colorStroke":"rgb(250, 135, 200)",
    "colorStrokeShadow":"rgb(250, 84, 120)",
    "hitpoint":2
      }
    }  
    ctx.lineWidth = 5;
    ctx.lineJoin = "round";
    ctx.strokeStyle = this.opt.colorStrokeShadow;
    ctx.fillStyle = this.opt.colorShadow;

    ctx.beginPath();
    
    ctx.moveTo(this.blockX,this.blockY + rectH);
    ctx.lineTo(this.blockX + 5, this.blockY + rectH + 5);
    ctx.lineTo(this.blockX + rectW + 5, this.blockY + rectH + 5);
    ctx.lineTo(this.blockX + rectW + 5, this.blockY + 5);
    ctx.lineTo(this.blockX + rectW, this.blockY);
    ctx.lineTo(this.blockX, this.blockY + rectH);
    ctx.stroke();
    ctx.fill();
    ctx.closePath();

    ctx.strokeStyle = this.opt.colorStroke;
    //ctx.lineWidth = 5;
    //ctx.lineJoin = "round";
    ctx.fillStyle = this.opt.colorFill;
    ctx.beginPath();
    ctx.rect(this.blockX, this.blockY, rectW, rectH);
    ctx.stroke();
    ctx.fill();
    ctx.closePath();

  
   if(this.crashColor){
        ctx.fillStyle = "rgba(255,255,255,0.4)";
        ctx.beginPath();
        ctx.moveTo(this.blockX,this.blockY);
        ctx.lineTo(this.blockX,this.blockY+rectH);
        ctx.lineTo(this.blockX + 5, this.blockY + rectH + 5);
        ctx.lineTo(this.blockX + rectW + 5, this.blockY + rectH + 5);
        ctx.lineTo(this.blockX + rectW + 5, this.blockY + 5);
        ctx.lineTo(this.blockX + rectW, this.blockY);
        //ctx.rect(this.blockX, this.blockY, rectW, rectH);
        ctx.closePath();
        ctx.fill();
       
      }
       if(this.gun){
        ctx.beginPath();
        ctx.strokeStyle = this.opt.colorShadow;
        ctx.fillStyle = this.opt.colorStrokeShadow;
        ctx.arc(this.blockX + rectW/2, this.blockY + rectH/2, 10, 0, 2 * Math.PI);       
        ctx.rect(this.blockX + rectW/2 - 3, this.blockY + rectH/2, 5, 15);        
        ctx.stroke();
        ctx.fill();
        ctx.closePath();
        ctx.beginPath();
        ctx.fillStyle = this.opt.colorStroke;
        ctx.arc(this.blockX + rectW/2, this.blockY + rectH/2, 4, 0, 2 * Math.PI); 
        ctx.stroke();         
        ctx.fill();
        ctx.closePath();
      }
    };//draw

      this.move = function () {
            this.blockY +=calcDistanceToMove(delta, this.speed);
            
      };//move   
  
}

//-------------------------------------------------------------
// Inits
window.onload = function init() {
    var game = new GF();
    game.start();
};

// GAME FRAMEWORK STARTS HERE
var GF = function () {

      var assetsToLoadURLs = {
         spritesheet    :{url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/Ships_2.svg", type:"image"},
         spriteBlock    :{url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/block-crash.svg",  type:"image"},
         mainBackground :{url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/Cosmo-background.jpg",  type:"image"},
         helperSound    : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6MFBDb3JsVFRxN1E.mp3", buffer: false, loop: false, volume: 1.0,  type:"sound"},
         bombsFly       : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6OEFZYzZ3ajNEUVk.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         clickCosmos    : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6MDFPaFkwdjJSY3M.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         clickMenu      : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6WTltOXBVaE5vb1E.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         littleClick    : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6TVROZWxfenIzMUE.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         strangerHit    : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6WDBhMzJrM29fYXc.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         tuk            : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6Y0ZYbHZYeU1CNnM.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         tukLouder      : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6TTRmQ2c0QjBEb1E.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         fire           : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6blZhMV9FSTl4UHM.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         soundCrash     : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6X1RLSE9qTGxwYWM.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"},
         rocketHit      : {url: "https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/0B_E4HKbPQZo6SGpyMDlRYzhydnM.mp3", buffer: false, loop: false, volume: 1.0, type:"sound"}        
};
      // the assets variable holds the assets once loaded
    var assets = {};
    // Vars relative to the canvas
    var canvas, ctx, w, h;

    // vars for handling inputs
    var inputStates = {};

    // game states
    var gameStates = {
        mainMenu: 0,
        gameRunning: 1,
        gameOver: 2
    };
    var currentGameState = gameStates.mainMenu;
    var currentLevel = 1;
    var TIME_BETWEEN_LEVELS = 20000; // 20 seconds
    var currentLevelTime = TIME_BETWEEN_LEVELS;
   // var helperSound; 

    var TIME_ROCKET_CRASH = 1500;
    var currTimeRocketCrash;
    var rocket;
    var rocketCrash;
    var strangerCrash;

    var fires = [];  
    var firesTotal = 3;
    var enemy=[];
    var bombs=[];
    var guns=[];
    var crashEnemy=[];
    var crashBlock = [];

     var strangerPicture;
     var rocketPicture;

    var gridLength = 16;
    var line = []; 
    var randBin=[];
 
    var rectW = 47;
    var rectH = 37;
    var allBlocks = [];
    var nbOfBlocks = 10;//20;
    var grid = [];
 //  var numStrGrid = 0;
    var Y_START = -rectH-3;
    var Y_FINISH = h;
    var SPEED_START = 40;
    var indexNewLine;
    var flagRemoveLine = false; 
    var score=0;
    var maxScore=0;
    var finish=false;

            var BLOCK_CRASH_BEGIN   = 1 ;
            var BLOCK_CRASH_NB      = 6  ;
            var BLOCK_NB_STRING     =  1 ;
            var BLOCK_NB_COLUMN     =  6 ; 

            var STRANGER_CRASH_BEGIN   = 11+3;
            var STRANGER_CRASH_NB      = 9; 

            var SHEET_NB_STRING     =   2 ;
            var SHEET_NB_COLUMN     =  11 ; 

   
    // clears the canvas content
    function clearCanvas() {
        ctx.clearRect(0, 0, w, h);
    }

    
    var mainLoop = function (time) {
        //main function, called each frame 
        measureFPS(time);

        // number of ms since last frame draw
        delta = timer(time);

        // Clear the canvas
        clearCanvas();

        switch (currentGameState) {
            case gameStates.gameRunning:
                
                  
              if (!rocket.crash) {console.log("rocket.crash="+rocket.crash);
                   if (!testRocketBlocks() && !testRocketStranger() && !testBulletRocket() &&
                       !testBombRocket()){
                                           rocket.draw(ctx,w,h,1);
                      if (rocket.hitRocket) {
                                            assets.rocketHit.play();
                                             rocket.timeAfterHit -= delta;
                                             if (rocket.timeAfterHit<=0){rocket.hitRocket=false;
                                                                         rocket.timeAfterHit=500;
                                                                         } 
                                            }// if (rocket.hitRocket)
                                    }
                                     else{ 
                                           console.log("ракета разбита !!!!!"); 
                                           rocket.crash=true;
                                           assets.soundCrash.play();
                                           currTimeRocketCrash = TIME_ROCKET_CRASH;
                                           break;
                                          }
                                  }//if (!rocket.crash)
                            else {   rocketCrash.draw(ctx,rocket.x,rocket.y,1);
                                     currTimeRocketCrash -= delta;               
                                     if (currTimeRocketCrash < 0) {
                                      currentGameState=gameStates.gameOver;
                                      break;
                                     }
                                  }       
                                       drawFire(fires,ctx);                                       updateRocketPosition(delta);                 
                 updateBlock();
                 
                 if(guns.length){
                    updateBullets();
                    if(guns.length){
                       for(var i=0; i< guns.length; i++)
                       { 
                        var lastBullet = guns[i][guns[i].length - 1];
                    //    console.log("i="+i+" time ="+lastBullet.time +" index="+lastBullet.index+
                    //                 " y="+lastBullet.y);
                        if(allBlocks[lastBullet.index].gun){
                      if(lastBullet.time>0) lastBullet.time -= delta;
                      if(lastBullet.time <= 0){guns[i].push(new Bullet(lastBullet.index,
                                                            allBlocks[lastBullet.index].blockX+allBlocks[lastBullet.index].rectW/2,
                                                          allBlocks[lastBullet.index].blockY+allBlocks[lastBullet.index].rectH,
                                                          3,100,0,1,3000));  
                                               assets.tuk.play();
                                              }  
                        }                                                     
                    }//for
                    }//  if(guns.length)  
                 }//if guns.length
                   /*  for (var i = 0; i < guns.length; i++) {
                        console.log("i="+i);
                        for (var ii = 0; ii < guns[i].length; ii++) {
                          console.log("index="+guns[i][ii].index+" time="+guns[i][ii].time);
                        }                          
                       }  */
                 updateEnemy();
                 if(enemy.length>0) 
                     if (testFireEnemy() >= 0){// console.log("it's time update bombs");
                                                moveFire(fires,true);              
                                               } 
                 if(bombs.length>0)updateBombs();
                 //---------------------------------------------------------------------
                 if(crashEnemy.length)
                     for (var i = 0; i < crashEnemy.length; i++) {
                       crashEnemy[i].draw(ctx);
                       crashEnemy[i].time -= delta;               
                       if ( crashEnemy[i].time< 0) crashEnemy.splice(i,1);
                     }//for
                 //----------------------------------------------------------------------
                  if(crashBlock.length)
                     for (var i = 0; i < crashBlock.length; i++) {
                       crashBlock[i].draw(ctx);
                       crashBlock[i].time -= delta;               
                       if ( crashBlock[i].time< 0) crashBlock.splice(i,1);
                     }//for    
                 //------------------------------------------------------------------------
                 var yTarget = testFireBlocks(fires);
                // есть попадание - закончить вывод огня на цели,
                // иначе - двигать до верха экрана
                   switch (yTarget){
                    case -1:
                    moveFire(fires,false);
                    break;
                    case -2:
                    moveFire(fires, true);
                    break;
                    default:                                
                    moveFire(fires, true, yTarget);
                       }                                 
                // display Score
                displayScore();

                // decrease currentLevelTime. 
                // When < 0 go to next level
                
                currentLevelTime -= delta;
               
                if (currentLevelTime < 0) {
                                            goToNextLevel();
                }
                /*
                if(finish===true) currentGameState= gameStates.gameOver;
                */
                break;
            case gameStates.mainMenu:
                // TO DO !               
                ctx.save();
                ctx.fillStyle = "rgb(0,168,203)";
                ctx.font = "26px Arial";
                ctx.fillText("Press ENTER to start", 450, 190);
                ctx.font = "20px Arial";
                ctx.fillText("Created by Inga Berezhna", 25, 400);
                ctx.fillText("and Katerina Berezhna", 135, 430);
                ctx.restore();
                ctx.save();
                ctx.lineWidth = 7;
                ctx.lineCap = "round";
                ctx.strokeStyle = "rgba(255,255,255,0.8)";
                ctx.shadowBlur = 10;
                ctx.shadowColor = "rgba(255, 255, 255, 0.7)";
                ctx.rotate(-50 * Math.PI / 180);
                rocketPicture.draw(ctx, -200, 500, 7);
                ctx.strokeStyle = "rgba(255,255,255,1)";     
                ctx.beginPath();
                ctx.moveTo(80,450);
                ctx.lineTo(80,350);
                ctx.stroke();
                ctx.closePath();
                ctx.restore();

                ctx.save();
                ctx.rotate(-35 * Math.PI / 180);
                strangerPicture.draw(ctx,-120,20,4);
                ctx.restore();
                ctx.save();
                ctx.fillStyle = "rgb(217,103,255)";
                ctx.font = "76px Arial";
                ctx.fillText("Star Warriors", 300, 120);
                 
                ctx.font = "12px Arial";
                ctx.fillText("Music from AstroMenace Artwork ver 1.2 Copyright (c) 2006-2007 Michael Kurinnoy, Viewizard", 20, 480);
                ctx.restore();
                if(inputStates.enter){
                    currentGameState = gameStates.gameRunning;
                   //  assets.spaceMusic.stop();
                }
                break;
            case gameStates.gameOver:
            
                ctx.font = "40px Arial";
                ctx.fillStyle = "rgb(217,103,255)";
                
                if (finish===true){console.log("finish="+finish);
                                   ctx.fillText("You have finished your mission", 200, 200);
                                  }
                            else   ctx.fillText("GAME OVER", 250, 150);    
                ctx.font = "25px Arial";
                ctx.fillText("High Score : "+  maxScore,290, 250);
                ctx.fillText("Your Score : " + score,   290, 290);
                ctx.fillText("Your Time  : " + (((currentLevel-1)*TIME_BETWEEN_LEVELS+
                                             (TIME_BETWEEN_LEVELS-currentLevelTime))/1000).toFixed(0), 290, 330);

                ctx.font = "20px Arial";
                ctx.fillText("Press ENTER to start again", 260, 450);
                if (inputStates.enter) {
                    startNewGame();
                    currentGameState = gameStates.gameRunning;
                }
                break;
        }

        // call the animation loop every 1/60th of second
        requestAnimationFrame(mainLoop);
    };
    function startMenu(){
        currentGameState = gameStates.mainMenu;
    }

    function startNewGame() {
       
       if(score > maxScore) maxScore=score;
       score=0;
       enemy=[];
       bombs=[];
       guns=[];
       grid=[];
       crashEnemy=[];
       crashBlock = [];
       allBlocks = [];
       nbOfBlocks=10;
        currentLevelTime = TIME_BETWEEN_LEVELS;
        currentLevel =1;
        finish=false;
           //иниц-ция массива блоков
          for(var i=0;i<nbOfBlocks;i++)
          {
            allBlocks[i]=new Block(0,Y_START,SPEED_START,rectW,rectH,"optNormal",false,
                              assets.spritesheet,false);
          }
          for(var i=0;i<gridLength;i++) line[i]=0;
            setNewLine();

       rocket.crash = false;
       rocket.maxHitpoint = 3;
       rocket.hitpoint = 3;
       rocket.hitRocket = false;
       rocket.timeAfterHit = 500;
       
       rocket = new Rocket(w/2-15,h-60,80,80,rocketPicture,rocketPictureSecond,20); 
       // currentGameState = gameStates.gameRunning;
    }

    function goToNextLevel() {
        
        // reset time available for next level
        // 5 seconds in this example
        currentLevelTime = TIME_BETWEEN_LEVELS;
        currentLevel++;
        allBlocks.push(new Block(0,Y_START,SPEED_START,rectW,rectH,"optNormal",false,
                              assets.spritesheet,false));
        nbOfBlocks++;
   
    }

    function displayScore() {
        ctx.save(); 
        ctx.fillStyle = "rgb(0,168,203)";
        ctx.font = "22px Arial";
        ctx.fillText("Level: " + currentLevel, 640, 460);
        ctx.fillText("Time: " + (currentLevelTime / 1000).toFixed(0), 640, 490);
       //  ctx.fillText("Time: " + currentLevelTime / 1000, 640, 490);
        ctx.fillText("Score:" + score,10, 490);
      //  ctx.fillText("max Score:" + maxScore,640, 490);
        ctx.restore();
    }


    function updateRocketPosition(delta) {
        rocket.speedX = rocket.speedY = 0;
        // check inputStates
        if (inputStates.left) {
            rocket.speedX = -rocket.speed;
        }
        if (inputStates.up) {
            rocket.speedY = -rocket.speed;
        }
        if (inputStates.right) {
            rocket.speedX = rocket.speed;
           
        }
        if (inputStates.down) {
            rocket.speedY = rocket.speed;
        }
        if (inputStates.space && fires.length < firesTotal) {
         /* console.log("fires.push="+rocket.y);  
         fires.push([rocket.x+rocket.width/2, rocket.y]);*/
         //если это начало огня, просто добавить коорд-ты
        if(fires[0]===undefined) { fires.push([rocket.x+rocket.width/2, rocket.y]);
                                    assets.fire.play();}
                         else // иначе следующий выстрел писать,когда предыд.прошел 40 пикселей
                             if(fires[fires.length-1][1]+40<rocket.y){ fires.push([rocket.x+rocket.width/2, rocket.y]);
                             assets.fire.play();}
              }
       /* if (inputStates.mousePos) {
        }
        if (inputStates.mousedown) {
            rocket.speed = 500;
        } else {
            // mouse up
        }*/
            rocket.speed = 100;
        
        
        // Compute the incX and inY in pixels depending
        // on the time elasped since last redraw
        rocket.x += calcDistanceToMove(delta, rocket.speedX);
        rocket.y += calcDistanceToMove(delta, rocket.speedY);
       
    }
    function updateBlock(){ 
         var flagRemoveLine = false; 

         //------------------------------------------
         // подсчитать кол-во рабочих блоков в allBlocks
         var sum=0;
         for (var i = 0; i < allBlocks.length; i++) {
         if(allBlocks[i].worked===true) {sum++;}
         }//sum
         //если рабочих блоков нет,то экран пуст и надо создавать новую линию и записать ее в grid
         if(sum===0){setNewLine();
                     console.log("создаем линию после пустого экрана");
                     } 
        //-----------------------------------------------------------------------------------------
         //дать приращение  координате y блокам на экране
         for (var i = 0; i < allBlocks.length; i++) {
         var block = allBlocks[i];
         if(block.worked){
                           block.move();
                         }
      
         //если y блока больше экранного,сделать его нерабочим и установить его "y" на старт
         // а также установить флаг flagRemoveLine - признак,что пора формировать новую линию
        // for (var i = 0; i < allBlocks.length; i++) {                           
         if(allBlocks[i].blockY >= 500){
                                  flagRemoveLine = true;
                                  allBlocks[i].worked=false;  
                                  allBlocks[i].blockY=Y_START; 
                                  allBlocks[i].gun=false;                                                                 
                                  }
         }// for i allBlocks.length
         //--------------------------------------------------------------------------               
         //если блоки выползли с экрана вниз
         if (flagRemoveLine) {// setNewLine();
                                grid.shift();
                             }
             // indexNewLine - индекс блока в последней созданной линии,
         // как только коорд-та у такого блока станет > 0,т.е.появится на экране,
         // можно создавать новую линию
       //  if(currentLevelTime>1000){
         if(indexNewLine!==undefined){
             if(isFreeBlock()){
                               //console.log("indexNewLine ="+indexNewLine+"  создаем линию");
                               if (allBlocks[indexNewLine].blockY>=0) setNewLine();
                               }
         } //  if(indexNewLine!==undefined)  
       //                           }
         //--------------------------------------------
         
         //выод grid на экран
         if(grid.length !== undefined){
         //вывести на экран все рабочие блоки 
         for(var kol=grid.length-1; kol>=0; kol--)        
         
             for (var i = 0; i < grid[kol].length; i++) 
             {  var ind=grid[kol][i];
                if(allBlocks[ind].worked === true) allBlocks[ind].draw(ctx);
             }
         }//if(grid.length !== undefined)

      }//  function updateBlock() 
    //-----------------------enemy--------------------

    function updateEnemy(){
        for (var i = 0; i < enemy.length; i++) {
            enemy[i].draw(ctx,enemy[i].x,enemy[i].y,1);
            enemy[i].move(rocket.x,rocket.width);
            if (enemy[i].hitStranger) {
                  enemy[i].timeAfterHit -= delta;
                  if (enemy[i].timeAfterHit<=0){enemy[i].hitStranger=false;
                                                enemy[i].timeAfterHit=100;
                                                } 
                  }
        }
    }
   //-----------------------------------------------------------------------
      function testFireEnemy(){
         var rez=-1;
         var arr=[];
         var indexDel=[];
      if (fires.length>0){
         for (var i = 0; i < enemy.length; i++) {

        // for(var j=0; j< fires.length; j++){                 
             if(circRectsOverlap(enemy[i].x, enemy[i].y,enemy[i].width,enemy[i].height,
                                 fires[0][0],fires[0][1],2)){
                if(enemy[i].hitpoint >1){  assets.strangerHit.play();
                    enemy[i].decreaseHit();
                    //изменить вид stranger на strangerPictureSecond 
                    enemy[i].hitStranger = true;
                    score+=2;
                    return rez = 0;
                }else{assets.bombsFly.play();
               // попадание в enemy,через промежуток времени создать массив бомб
               enemy[i].crash=true;
               score+=4;
               for(k=0;k<5;k++)
               {arr.push(new Bomb(enemy[i].x, enemy[i].y,5,30,-20+k*10,1+Math.random()*4));}
               //в crashEnemy добавить объект для вывода crashStranger 
            var strangerCrash = new Sprite();             
            strangerCrash.extractSprites(assets.spritesheet,STRANGER_CRASH_BEGIN,
                                STRANGER_CRASH_NB, 
                                SHEET_NB_COLUMN,SHEET_NB_STRING );            
            strangerCrash.setNbImagesPerSecond(8);
               crashEnemy.push(new CrashStranger(false,enemy[i].x,enemy[i].y,strangerCrash,1125));
            rez=1;
            indexDel.push(i);//записать индекс enemy,в который попали,чтобы удалить его из массива enemy
            // console.log("enemy kill !!!!!!!");   
            }//if hitpoint        
           }//if (circRectsOverlap
           if(arr.length !==0){ bombs.push(arr);
                               // console.log("i="+i);
                               // console.log("bombs="+bombs[i][0].x+" rez="+rez);
                              }
                                
         }//for  i
         //убрать enemy[i] из массива
         if(rez===1){for (var i = 0; i < indexDel.length; i++) {                       
                       enemy.splice(indexDel[i],1);
                      } 
                 }
      }//if (fires.length>0)
     return rez;

     }  
     //----------------------------------------------------------------------------
    function updateBombs(){
       // console.log("выводим бомбы");
        for (var i=0;i<bombs.length;i++){
            for(var ii=0;ii<bombs[i].length;ii++){
          //  console.log("bombs.x="+bombs[i][ii].x);
            bombs[i][ii].draw(ctx);
            bombs[i][ii].move (h);
            if(bombs[i][ii].remove) bombs[i].splice(ii,1);
            }
          if(bombs[i].length === 0){bombs.splice(i,1);} 
        }
    }
    function updateBullets(){
        for (var i = 0; i < guns.length; i++) {
            for (var ii = 0; ii < guns[i].length; ii++) {
                guns[i][ii].draw(ctx);
                 guns[i][ii].move(h,delta);
                 if(guns[i][ii].remove) guns[i].splice(ii,1);
            }
            if(guns[i].length === 0){guns.splice(i,1);} 
        }
    }
    //-------------------------------------------------------------------------------------
    function testBulletRocket(){
        
        for (var i = 0; i < guns.length; i++) {
            for (var ii = 0; ii < guns[i].length; ii++) {
              if( circRectsOverlap(rocket.x+20, rocket.y+10,rocket.width-40,rocket.height-20,
                                      guns[i][ii].x,guns[i][ii].y,guns[i][ii].r)){
                //удалить из массива guns пулю,которая поразила цель
                  guns[i][ii].remove = true;
                if(rocket.hitpoint >1){
                                       rocket.decreaseHit();
                                       //изменить вид rocket на rocketPictureSecond  
                                       rocket.hitRocket = true;
                                       return false;
                                      }                                 
                return true;
              }//if( circRectsOverlap
            }//for ii            
        }//for i
        return false;
    } 
    //-------------------------------------------------------------------------------
     function testBombRocket(){
        
        for (var i = 0; i < bombs.length; i++) {
            for (var ii = 0; ii < bombs[i].length; ii++) {
              if( circRectsOverlap(rocket.x+20, rocket.y+10,rocket.width-40,rocket.height-20,
                                      bombs[i][ii].x,bombs[i][ii].y,bombs[i][ii].r)){

                //удалить из массива guns пулю,которая поразила цель
                  bombs[i][ii].remove = true;
                if(rocket.hitpoint >1){ console.log("бомба попала в ракету");
                                       rocket.decreaseHit();
                                       //изменить вид rocket на rocketPictureSecond  
                                       rocket.hitRocket = true;
                                       return false;
                                      }                                 
                return true;
              }//if( circRectsOverlap
            }//for ii            
        }//for i
        return false;
    }                              
    //------------------- тест collision блоков с ракетой-----------------------------
     function testRocketBlocks(){
         var rez=false;
         for (var i = 0; i < allBlocks.length; i++) {
         if( rectsOverlap(rocket.x, rocket.y,rocket.width,rocket.height,
                       allBlocks[i].blockX+10, allBlocks[i].blockY+5,
                       allBlocks[i].rectW-20, allBlocks[i].rectH-5)){
            
            allBlocks[i].worked=false;
            rez=true;
            break;
           }//if  
        }//for
     return rez;
     } //   function testRocketBlocks()
    //---------------------------------------------------------------------------------
      function testRocketStranger(){
         var rez=false;
         for (var i = 0; i < enemy.length; i++) {
         if( rectsOverlap(rocket.x, rocket.y,rocket.width,rocket.height,
                       enemy[i].x+10, enemy[i].y+5,
                       enemy[i].width-20, enemy[i].height-5)){
            //allBlocks[i].worked=false;
            rez=true;
            break;
           }//if  
        }//for
     return rez;
     } 
    //------------------- тест collision блоков с выстрелом ---------------------------------------
    function testFireBlocks(fires){
         var y=-1;
         if (fires.length>0)
      {
          for (var i = 0; i < allBlocks.length; i++) {

                //   console.log(" индекс "+i+ " x="+allBlocks[i].blockX+" y="+allBlocks[i].blockY);  
                if(allBlocks[i].worked){
                    for(var ii=0; ii < fires.length; ii++){
                    if (circRectsOverlap(allBlocks[i].blockX, allBlocks[i].blockY,
                        allBlocks[i].rectW, allBlocks[i].rectH,
                        fires[ii][0], fires[ii][1], 2))
                     {  //было попадание   
                        score+=2;
                      if(allBlocks[i].hitpoint > 1){ assets.littleClick.play();                     
                        allBlocks[i].countHit();
                        allBlocks[i].crashColor = true;
                     //   console.log("hitpoint = " + allBlocks[i].hitpoint);
                      //  console.log(y);
                        return y = -2;
                     } else {  //блок можно убирать  
                     score+=4;            
                     //запомнить у блока,в который попал выстрел
                     y=allBlocks[i].blockY;
                     //исчезает - сделать блок нерабочим 
                    allBlocks[i].worked=false;
                    allBlocks[i].gun=false;
                    //подготовить спрайт для вывода разбившегося блока
                     var pic = new Sprite();             
                     pic.extractSprites(assets.spriteBlock,BLOCK_CRASH_BEGIN,
                                      BLOCK_CRASH_NB, 
                                      BLOCK_NB_COLUMN,BLOCK_NB_STRING );            
                     pic.setNbImagesPerSecond(10);

                    crashBlock.push(new CrashBlock(false,allBlocks[i].blockX,allBlocks[i].blockY,pic,600));
                    //если блок красный,то строить массив enemy,создавая новый stranger
                    if(allBlocks[i].optName ==="optRed"){score+=2;
                    enemy.push(new Stranger (allBlocks[i].blockX+rectW/2-40,allBlocks[i].blockY,80,80,
                                            strangerPicture,strangerPictureSecond,40));                        
                                            }
                    allBlocks[i].blockY=Y_START;                             
                                          
                    //---------- удалить из grid индекс,соотв.удаленному блоку --------
                        for(var k=0; k<grid.length; k++) {  
                          var st=grid[k];              
                        for (var j = 0; j < grid[k].length; j++) 
                         { 
                            if (st[j]===i) {st.splice(j,1);/*console.log("st="+st);*/}                
                         }//for j
                         if(st.length===0) {grid.splice(k,1); 
                                           // console.log("grid="+grid);
                                        } 
                        }//for k                   
                    //--------------- конец удаления из grid ------------------------ 
                       assets.helperSound.play();
                     }//else if hitpoint
                  }//if (circRectsOverlap 
                }//for ii
              }//if(allBlocks[i].worked)
        }//for
    }//if (fires.length)
    return y;
    }//function testFireBlocks()  
    
    function isFreeBlock(){
   for(var i=0; i < nbOfBlocks; i++){
          if (allBlocks[i].worked === false) return true;
           } //for
          //  console.log("нельзя больше создать блоков");
            return -1;
    } //function 

       function countFreeBlock(){
    var sum=0;
   for(var i=0; i < nbOfBlocks; i++){
          if (allBlocks[i].worked === false) sum++;
           } //for
     return sum;
    } //function  
        
    //найти в allBlocks элемент с worked=false
        
    //этот блок записать в текущий эл-т allBlocks,изменив пар-ры:x,opt,worked
    function findNoWorkedBlock(){
       // for(var i=0; i < nbOfBlocks; i++) console.log("i="+i+" allBlocks[i].worked="+allBlocks[i].worked);

         for(var i=0; i < nbOfBlocks; i++){
            if (allBlocks[i].worked === false){
                    //изменить пар-р worked
                     allBlocks[i].worked = true ;
                   //  console.log("i="+i);
                     return i;
                 }//if - true
            } //for
          //  console.log("нельзя больше создать блоков");
            return -1;
    } //function   

     function createLine(){

       var arr=[];
       var bullArr=[];
     
        var sum=0;
        for(var i=0; i < gridLength; i++){
            if(Math.random() < randBin[i]){ line[i] = 1; sum++;}
                                     else 
                                           line[i] = 0;
            }
       //   console.log("line="+line+" sum="+sum);
   
         if (countFreeBlock()>=sum)
          for(var i=0; i < gridLength; i++){
          if(line[i]===1) { 
            
            var cBlock="optNormal";
                if (Math.random() <= 0.4)  {cBlock="optYellow";  }
                    else if (Math.random() <=0.2){cBlock="optRed";}              
              
                var index = findNoWorkedBlock();
               // console.log("index="+index);
                                 allBlocks[index].blockX= i*(rectW+3);
                                 allBlocks[index].optName=cBlock;
                                 allBlocks[index].setHit();
                                 allBlocks[index].crashColor = false;
                                 allBlocks[index].gun = false;
                                 
                                 if(Math.random() < 0.2){
                                    allBlocks[index].gun = true;
                                   bullArr=[]; 
                                   bullArr.push( new Bullet(index,
                                                           allBlocks[index].blockX+allBlocks[index].rectW/2,
                                                          allBlocks[index].blockY+allBlocks[index].rectH,
                                                          3,100,0,1,3000));
                               
                                    guns.push(bullArr);
                                } 

                                 indexNewLine=index;
                                 arr.push(index);
                                } //if(line[i]===1)  
                } //for i         
          return arr;  
        }


function setNewLine(){
    var arr=[];

    for(var i=0; i < gridLength; i++){
        if (line[i] === 1 || line[i+1] === 1){
            randBin[i] = 0.5;
        }else{
            randBin[i] = 0.1;
        }
    }
 //  сформировать новую линию блоков line 
        arr=createLine();
 //если строка пустая, то в grid дописывать ее не надо
        if (arr.length === 0) {//console.log("сформирована пустая строка ");
                               return;}
 // либо пишем в конец grid, либо в начало grid
                   else  
                        { 
                            grid.push(arr);
                               // console.log("grid " + numStrGrid + "  = "+grid.lenght); 
                         // numStrGrid ++;      
                              /*   for (var n=0;n<grid.length;n++)      
                                 console.log("grid"+n+" = " + grid[n]);
                                 console.log("line="+line);
                                 for(var i=0;i<allBlocks.length;i++){
                                 if(allBlocks[i].worked === false)
                                  //  console.log("i="+i+" block.worked="+allBlocks[i].worked);
                                 }
                               */  
                        }
}//setNewLine


    var start = function () {
        initFPSCounter();

        canvas = document.getElementById("shooter");
          // often useful
        w = canvas.width;
        h = canvas.height;
        ctx = canvas.getContext('2d');
        console.log("ctx="+ctx);
        // default police for text
        ctx.font = "20px Arial";
        
        // Create the different key and mouse listeners
        addListeners(inputStates, canvas);
         for(var i=0; i < gridLength; i++)
           randBin.push(0.1);
        //иниц-ция массива блоков
          for(var i=0;i<nbOfBlocks;i++)
          {
            allBlocks[i]=new Block(0,Y_START,SPEED_START,rectW,rectH,"optNormal",false,
                              assets.spritesheet,false);
   
          }
          for(var i=0;i<gridLength;i++) line[i]=0;
           // createLine();
            setNewLine();
        //createSquare();
             loadAssets(assetsToLoadURLs, function(assetsLoaded) {
            assets = assetsLoaded;
            console.log("all images and sounds loaded and decoded");
                   // all assets (images, sounds) loaded, we can start the animation
         //   rocket = new Rocket(w/2-15,h-60,100,160,assets.rocket,20); 
            canvas.style.backgroundImage = "url('https://mainline.i3s.unice.fr/mooc/StarWarriors/assets/Cosmo-background.jpg')"; 
            currentLevelTime = TIME_BETWEEN_LEVELS; 

         //   var ROCKET_SPRITE_WIDTH  = 80; 
         //   var ROCKET_SPRITE_HEIGHT = 80;
            var ROCKET_CRASH_BEGIN   = 3;
            var ROCKET_CRASH_NB      = 9; 

            var STRANGER_CRASH_BEGIN   = 11+3;
            var STRANGER_CRASH_NB      = 9; 

            var SHEET_NB_STRING     =   2 ;
            var SHEET_NB_COLUMN     =  11 ; 
        //=======================================================================   
            rocketPicture         = new SpriteImage(assets.spritesheet,0,0,80,80); 
            rocketPictureSecond   = new SpriteImage(assets.spritesheet,80,0,80,80);
            rocketCrash = new Sprite();             
            rocketCrash.extractSprites(assets.spritesheet,ROCKET_CRASH_BEGIN,
                                ROCKET_CRASH_NB, 
                                SHEET_NB_COLUMN,SHEET_NB_STRING );           
            rocketCrash.setNbImagesPerSecond(6);

            rocket = new Rocket(w/2-15,h-60,80,80,rocketPicture,rocketPictureSecond,20); 
        //------------------------------------------------------------------------
            strangerPicture       = new SpriteImage(assets.spritesheet,0,80,80,80);
            strangerPictureSecond = new SpriteImage(assets.spritesheet,80,80,80,80);
            strangerCrash = new Sprite();             
            strangerCrash.extractSprites(assets.spritesheet,STRANGER_CRASH_BEGIN,
                                STRANGER_CRASH_NB, 
                                SHEET_NB_COLUMN,SHEET_NB_STRING );            
            strangerCrash.setNbImagesPerSecond(10);
         //========================================================================   
           // assets.spaceMusic.play();
            requestAnimationFrame(mainLoop);
        });
    };

    //our GameFramework returns a public API visible from outside its scope
    return {
        start: start
    };
};


function isImage(url) {
    return (url.match(/\.(jpeg|jpg|gif|png|svg)$/) != null);
}

function isAudio(url) {
    return (url.match(/\.(mp3|ogg|wav)$/) != null);
}

function loadAssets(assetsToBeLoaded, callback) {
    var assetsLoaded = {};
    var loadedAssets = 0;
    var numberOfAssetsToLoad = 0;

    // define ifLoad function
    var ifLoad = function () {
        if (++loadedAssets >= numberOfAssetsToLoad) {
            callback(assetsLoaded);
        }
        console.log("Loaded asset" + loadedAssets);
    };
    // get num of assets to load
    for (var name in assetsToBeLoaded) {
        numberOfAssetsToLoad++;
        console.log(name);
    }

    console.log("Nb assets to load: " + numberOfAssetsToLoad);

    for (name in assetsToBeLoaded) {
        var url = assetsToBeLoaded[name].url;
        var type = assetsToBeLoaded[name].type;
        console.log("Loading " + url);
        if (type === "image") {
            assetsLoaded[name] = new Image();

            assetsLoaded[name].onload = ifLoad;
            // will start async loading. 
            assetsLoaded[name].src = url;
        } else {
            // We assume the asset is an audio file
            console.log("loading " + name + " buffer : " + assetsToBeLoaded[name].loop);
            assetsLoaded[name] = new Howl({
                urls: [url],
                format: 'mp3',
                buffer: assetsToBeLoaded[name].buffer,
                loop: assetsToBeLoaded[name].loop,
                autoplay: false,
                
                volume: assetsToBeLoaded[name].volume,
                onload: function () {
                    if (++loadedAssets >= numberOfAssetsToLoad) {
                        callback(assetsLoaded);
                    }
                    console.log("Loaded asset " + loadedAssets);
                }
            }); // End of howler.js callback
            
        } // if

    } // for
} // function

