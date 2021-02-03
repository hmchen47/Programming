// useful to have them as global variables
var canvas, ctx, w, h; 
var xMonster = 10;
var yMonster = 10;
var monsterSpeed = 1;

window.onload = function init() {
    // called AFTER the page has been loaded
    canvas = document.querySelector("#myCanvas");
  
    // often useful
    w = canvas.width; 
    h = canvas.height;  
  
    // important, we will draw with this object
    ctx = canvas.getContext('2d');
  
    // ready to go !
    mainLoop();
};

function mainLoop() {
  // 1 - clear the canvas. We told you that w, and h will be useful!
  ctx.clearRect(0, 0, w, h);
  
  // 2 - draw the monster
  drawMyMonster(xMonster, yMonster);
  
  // 3 - move the monster
  xMonster += monsterSpeed;
  
  // 4 - test collisions with vertical boundaries
   if (((xMonster + 100)> w) || (xMonster < 0))  {
     // collision with left or right wall
    // change the direction of movement
    monsterSpeed = -monsterSpeed;
  }
  
  // 5 - request a new frame of animation in 1/60s
  requestAnimationFrame(mainLoop);
}

function drawMyMonster(x, y) {
    // draw a big monster !
    // head
  
    // GOOD practice: save the context, use 2D trasnformations
    ctx.save();
  
    // translate the coordinate system, draw relative to it
    ctx.translate(x, y);
  
    // (0, 0) is the top left corner of the monster.
    ctx.strokeRect(0, 0, 100, 100);
  
    // eyes, x=20, y=20 is relative to the top left corner
    // of the previous rectangle
    ctx.fillRect(20, 20, 10, 10);
    ctx.fillRect(65, 20, 10, 10);
  
    // nose
    ctx.strokeRect(45, 40, 10, 40);
  
    // mouth
    ctx.strokeRect(35, 84, 30, 10);
  
    // teeth
    ctx.fillRect(38, 84, 10, 10);
    ctx.fillRect(52, 84, 10, 10);
  
   // GOOD practice: restore the context
   ctx.restore();
}
