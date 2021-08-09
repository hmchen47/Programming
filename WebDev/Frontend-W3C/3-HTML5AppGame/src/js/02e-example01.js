var canvas, ctx, width, height;

// array of balls to animate
var ballArray = [];

function init() {
  canvas = document.querySelector("#myCanvas");
  ctx = canvas.getContext('2d');
  width = canvas.width;
  height = canvas.height;
  
  // try to change this number
  createBalls(10); 
  
  requestAnimationFrame(mainLoop);
}
                                
function createBalls(numberOfBalls) {
  for(var i=0; i < numberOfBalls; i++) {
    // Create a ball with random position and speed.
    // You can change the radius
    var ball = new Ball(width*Math.random(),
                        height*Math.random(),
                        (10*Math.random())-5,
                        (10*Math.random())-5,
                        30);
    // add the ball to the array
    ballArray[i] = ball;
   }
}

function mainLoop() {
    // clear the canvas
    ctx.clearRect(0, 0, width, height);
  
    // for each ball in the array
    for(var i=0; i < ballArray.length; i++) {
      var ball = ballArray[i];
      
      // 1) move the ball
      ball.move();   
  
      // 2) test if the ball collides with a wall
      testCollisionWithWalls(ball);
  
      // 3) draw the ball
      ball.draw();
  }
    // ask for a new frame of animation at 60f/s
     window.requestAnimationFrame(mainLoop);
}  
 
function testCollisionWithWalls(ball) {
  // left
  if (ball.x < ball.radius) { // x and y of the ball are at the center of the circle
    ball.x = ball.radius;     // if collision, we replace the ball at a position
    ball.vx *= -1;            // where it's exactly in contact with the left border
  }                           // and we reverse the horizontal speed
  // right
  if (ball.x > width - (ball.radius)) {
    ball.x = width - (ball.radius);
    ball.vx *= -1;
  }
  // up
  if (ball.y < ball.radius) {
    ball.y = ball.radius;
    ball.vy *= -1;
  }
  // down
  if (ball.y > height - (ball.radius)) {
    ball.y = height - (ball.radius);
    ball.vy *= -1;
  }
}

// Constructor function for balls
function Ball(x, y, vx, vy, diameter) {
  // property of each ball: a x and y position, speeds, radius
  this.x = x;
  this.y = y;
  this.vx = vx;
  this.vy = vy;
  this.radius = diameter/2;
  // methods
  this.draw = function() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, 2*Math.PI);
    ctx.fill();
  };
  this.move = function() {
    // add horizontal increment to the x pos
    // add vertical increment to the y pos
    this.x += this.vx;
    this.y += this.vy;
 };
}

