// useful to have them as global variables
var canvas, ctx, w, h; 
var ball1 = {
  x: 100,
  y:100,
  radius: 30,
  color:'blue',
  speedX:2,
  speedY:1
}

var ball2 = {
  x: 60,
  y:130,
  radius: 55, 
  color:'purple',
  speedX:3,
  speedY:1
}

var ball3 = {
  x: 200,
  y:250,
  radius: 15,
  color:'green',
  speedX:3,
  speedY:5
}

var player = {
  x:10,
  y:10,
  width:20,
  height:20,
  color:'red'
}

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
  // 1 - clear the canvas
  ctx.clearRect(0, 0, w, h);
  
  // draw the ball and the player
  drawFilledRectangle(player);
  drawFilledCircle(ball1);
  drawFilledCircle(ball2);
  drawFilledCircle(ball3);

  // animate the ball that is bouncing all over the walls
  moveBall(ball1);
  moveBall(ball2);
  moveBall(ball3);
  
  // ask for a new animation frame
  requestAnimationFrame(mainLoop);
}

function moveBall(b) {
  b.x += b.speedX;
  b.y += b.speedY;
  
  testCollisionBallWithWalls(b);
}

function testCollisionBallWithWalls(b) {
    // COLLISION WITH VERTICAL WALLS ?
    if((b.x + b.radius) > w) {
    // the ball hit the right wall
    // change horizontal direction
    b.speedX = -b.speedX;
    
    // put the ball at the collision point
    b.x = w - b.radius;
  } else if((b.x -b.radius) < 0) {
    // the ball hit the left wall
    // change horizontal direction
    b.speedX = -b.speedX;
    
    // put the ball at the collision point
    b.x = b.radius;
  }
  
  // COLLISIONS WTH HORIZONTAL WALLS ?
  // Not in the else as the ball can touch both
  // vertical and horizontal walls in corners
  if((b.y + b.radius) > h) {
    // the ball hit the right wall
    // change horizontal direction
    b.speedY = -b.speedY;
    
    // put the ball at the collision point
    b.y = h - b.radius;
  } else if((b.y -b.radius) < 0) {
    // the ball hit the left wall
    // change horizontal direction
    b.speedY = -b.speedY;
    
    // put the ball at the collision point
    b.Y = b.radius;
  }  
}

function drawFilledRectangle(r) {
    // GOOD practice: save the context, use 2D trasnformations
    ctx.save();
  
    // translate the coordinate system, draw relative to it
    ctx.translate(r.x, r.y);
  
    ctx.fillStyle = r.color;
    // (0, 0) is the top left corner of the monster.
    ctx.fillRect(0, 0, r.width, r.height);
  
    // GOOD practice: restore the context
    ctx.restore();
}

function drawFilledCircle(c) {
    // GOOD practice: save the context, use 2D trasnformations
    ctx.save();
  
    // translate the coordinate system, draw relative to it
    ctx.translate(c.x, c.y);
  
    ctx.fillStyle = c.color;
    // (0, 0) is the top left corner of the monster.
    ctx.beginPath();
    ctx.arc(0, 0, c.radius, 0, 2*Math.PI);
    ctx.fill();
 
    // GOOD practice: restore the context
    ctx.restore();
}
