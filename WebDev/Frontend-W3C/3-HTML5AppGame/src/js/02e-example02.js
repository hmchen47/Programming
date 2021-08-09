var canvas, ctx, width, height;

// array of balls to animate
var ballArray = [];

function init() {
  canvas = document.querySelector("#myCanvas");
  ctx = canvas.getContext('2d');
  width = canvas.width;
  height = canvas.height;
  
  // try to change this number
  createBalls(16); 
  
  requestAnimationFrame(mainLoop);
}
                                
function createBalls(numberOfBalls) {
  for(var i=0; i < numberOfBalls; i++) {
    
    // Create a ball with random position and speed. 
    // You can change the radius
    var ball =  new Ball(width*Math.random(),
                          height*Math.random(),
                          (2*Math.PI)*Math.random(),        
                          (10*Math.random())-5,
                          30);
    
    // On la rajoute au tableau
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
    if (ball.x < ball.radius) {
        ball.x = ball.radius;
        ball.angle = -ball.angle + Math.PI;
    } 
    // right
    if (ball.x > width - (ball.radius)) {
        ball.x = width - (ball.radius);
        ball.angle = -ball.angle + Math.PI; 
    }     
    // up
    if (ball.y < ball.radius) {
        ball.y = ball.radius;
        ball.angle = -ball.angle;     
    }     
    // down
    if (ball.y > height - (ball.radius)) {
        ball.y = height - (ball.radius);
        ball.angle =-ball.angle; 
    } 
}

// constructor function for balls
function Ball(x, y, angle, v, diameter) {
  this.x = x;
  this.y = y;
  this.angle = angle;
  this.v = v;
  this.radius = diameter/2;
  
  this.draw = function() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, 2*Math.PI);
      ctx.fill();
  };
  
  this.move = function() {
    // add horizontal increment to the x pos
    // add vertical increment to the y pos
    
    this.x += this.v * Math.cos(this.angle);
    this.y += this.v * Math.sin(this.angle);
  };
}

