# Module 2: Game programming with HTML5 section


## 2.5 Animating multiple objects, collision detection

### 2.5.1 Animating multiple objects

#### Live coding video: animating multiple objects

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2SRKvzF)

In this section, we will see how we can animate and control not only the player but also other objects on the screen.

Let's study a simple example: animating a few balls and detecting collisions with the surrounding walls. For the sake of simplicity, we will not use time-based animation in the first examples.


#### Wall collisions with multiple balls

__Animating multiple balls which bounce off horizontal and vertical walls__

[Online example](https://jsbin.com/fikomik/edit?js,output) at JSBin:

[Local Demo](src/02e-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3cYKbWP')"
    src    = "https://bit.ly/35EjWAV"
    alt    = "Some circular balls that bounce agains vertical and horizontal borders of the canvas"
    title  = "Some circular balls that bounce agains vertical and horizontal borders of the canvas"
  />
</figure>

In this example, we define a constructor function for creating balls. This is a way to design JavaScript "pseudo classes" as found in other object-oriented languages like Java, C# etc. It's useful when you plan to create many objects of the same class. Using this we could animate hundreds of balls on the screen.

Each ball has an x and y position, and in this example, instead of working with angles, we defined two "speeds" - horizontal and vertical speeds - in the form of the increments we will add to the x and y positions at each frame of animation. We also added a variable for adjusting the size of the balls: the radius.

Here is the constructor function for building balls:

<div><ol>
<li value="1">// Constructor function for balls</li>
<li>function Ball(x, y, vx, vy, diameter) {</li>
<li>&nbsp; // property of each ball: a x and y position, speeds, radius</li>
<li>&nbsp;&nbsp;this.x = x;</li>
<li>&nbsp;&nbsp;this.y = y;</li>
<li>&nbsp;&nbsp;this.vx = vx;</li>
<li>&nbsp;&nbsp;this.vy = vy;</li>
<li>&nbsp;&nbsp;this.radius = diameter/2;</li>
<li> </li>
<li>&nbsp; // methods</li>
<li>&nbsp;&nbsp;this.draw = function() {</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li>&nbsp; &nbsp; ctx.arc(this.x, this.y, this.radius, 0, 2*Math.PI);</li>
<li>&nbsp; &nbsp; ctx.fill();</li>
<li>&nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp;&nbsp;this.move = function() {</li>
<li>&nbsp; &nbsp;&nbsp;// add horizontal increment to the x pos</li>
<li>&nbsp; &nbsp;&nbsp;// add vertical increment to the y pos</li>
<li>&nbsp; &nbsp;&nbsp;this.x += this.vx;</li>
<li>&nbsp; &nbsp;&nbsp;this.y += this.vy;</li>
<li>&nbsp;};</li>
<li>}</li>
</ol></div><br>

Using a constructor function makes it easy to build new balls as follows:

<div><ol>
<li value="1">var b1 = new Ball(10, 10,&nbsp;2, 2,&nbsp;5); // x, y, vx, vy, radius</li>
<li>var b1 = new Ball(100, 130,&nbsp;4, 5,&nbsp;5);&nbsp;</li>
<li>etc...</li>
</ol></div><br>

We defined two methods in the constructor function for moving the ball and for drawing the ball as a black filled circle. Here is the syntax for moving and drawing a ball:

<div><ol>
<li value="1">b1.draw();</li>
<li>b1.move();</li>
</ol></div><br>

We will call these methods from inside the mainLoop, and as you'll see, we will create many balls. This object-oriented design makes it easier to handle large quantities.

Here is the rest of the code from this example:

<div><ol>
<li value="1">var canvas, ctx, width, height;</li>
<li> </li>
<li><strong style="color: red;">// array of balls to animate</strong></li>
<li><strong style="color: red;">var ballArray = [];</strong></li>
<li> </li>
<li>function init() {</li>
<li>&nbsp; canvas = document.querySelector("#myCanvas");</li>
<li>&nbsp; ctx = canvas.getContext('2d');</li>
<li>&nbsp; width = canvas.width;</li>
<li>&nbsp; height = canvas.height;</li>
<li> </li>
<li>&nbsp;&nbsp;<strong style="color: red;">// try to change this number</strong></li>
<li><strong style="color: red;">&nbsp; createBalls(16);</strong> </li>
<li> </li>
<li>&nbsp; requestAnimationFrame(mainLoop);</li>
<li>}</li>
<li> </li>
<li>function createBalls(numberOfBalls) {</li>
<li>&nbsp;&nbsp;for(var i=0; i &lt; numberOfBalls; i++) {</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">// Create a ball with random position and speed. </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// You can change the radius</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;var ball = new Ball(width*Math.random(),</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; height*Math.random(),</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;(10*Math.random())-5,</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;(10*Math.random())-5,</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;30);</strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;//&nbsp;add the ball to the array</strong></li>
<li>&nbsp; &nbsp; <strong style="color: red;">ballArray</strong><strong style="color: red;">[i] = ball;</strong></li>
<li>&nbsp; &nbsp;}</li>
<li>} </li>
<li> </li>
<li>function mainLoop() {</li>
<li>&nbsp;&nbsp;// clear the canvas</li>
<li>&nbsp; ctx.clearRect(0, 0, width, height);</li>
<li> </li>
<li>&nbsp;&nbsp;<strong style="color: red;">// for each ball in the array</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;for(var i=0; i &lt; ballArray.length; i++) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;var ball = ballArray[i];&nbsp;</strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// 1) move the ball</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; ball.move(); </strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// 2) test if the ball collides with a wall</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;testCollisionWithWalls(ball);</strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// 3) draw the ball</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; ball.draw();</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;}</strong></li>
<li>&nbsp;&nbsp;// ask for a new frame of animation at 60f/s</li>
<li>&nbsp; window.requestAnimationFrame(mainLoop);</li>
<li>}</li>
<li> </li>
<li>function testCollisionWithWalls(ball) {</li>
<li>&nbsp;&nbsp;// left</li>
<li>&nbsp;&nbsp;if (ball.x &lt; ball.radius) { // x and y of the ball are at the center of the circle</li>
<li>&nbsp; &nbsp; ball.x = ball.radius; &nbsp; &nbsp; // if collision, we replace the ball at a position</li>
<li>&nbsp; &nbsp; ball.vx *= -1; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// where it's exactly in contact with the left border</li>
<li>&nbsp;&nbsp;} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // and we reverse the horizontal speed</li>
<li>&nbsp;&nbsp;// right</li>
<li>&nbsp;&nbsp;if (ball.x &gt; width - (ball.radius)) {</li>
<li>&nbsp; &nbsp; ball.x = width - (ball.radius);</li>
<li>&nbsp; &nbsp; ball.vx *= -1;</li>
<li>&nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;// up</li>
<li>&nbsp;&nbsp;if (ball.y &lt; ball.radius) {</li>
<li>&nbsp; &nbsp; ball.y = ball.radius;</li>
<li>&nbsp; &nbsp; ball.vy *= -1;</li>
<li>&nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;// down</li>
<li>&nbsp; if (ball.y &gt; height - (ball.radius)) {</li>
<li>&nbsp; &nbsp; ball.y = height - (ball.radius);</li>
<li>&nbsp; &nbsp; ball.vy *= -1;</li>
<li>&nbsp;&nbsp;} </li>
<li>}</li>
</ol></div><br>

Notice that:

+ All the balls are stored in an array (_line 4_),
+ We wrote a `createBalls(nb)` function that creates a given number of balls (and stores them in the array) with random values for position and speed (_lines 18-32_)
+ In the mainLoop, we iterate on the array of balls and for each ball we: 1) move it, 2) test if it collides with the boundaries of the canvas (in the function `testCollisionWithWalls`), and 3) we draw the balls (_lines 38-50_). The order of these steps is not critical and may be changed.
+ The function that tests collisions is straightforward (_lines 55-76_).  We did not use "if... else if" since a ball may sometimes touch two walls at once (in the corners). In that rare case, we need to invert both the horizontal and vertical speeds. When a ball collides with a wall, we need to replace it in a position where it is no longer against the wall (otherwise it will collide again during the next animation loop execution).


#### Direction and velocity with wall collisions

__Similar example but with the ball direction as an angle, and a single velocity variable__

Try this [example at JSBin](https://jsbin.com/begaci/edit): it behaves in the same way as the previous example.

[Local Demo](src/02e-example02.html)

Note that we just changed the way we designed the balls and computed the angles after they rebound from the walls. The changes are highlighted in bold:

<div><ol>
<li value="1">var canvas, ctx, width, height;</li>
<li> </li>
<li>// Array of balls to animate</li>
<li>var ballArray = [];</li>
<li> </li>
<li>function init() {</li>
<li>&nbsp; ...</li>
<li>}</li>
<li> </li>
<li>function createBalls(numberOfBalls) {</li>
<li>&nbsp;&nbsp;for(var i=0; i &lt; numberOfBalls; i++) {</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// Create a ball with random position and speed. </li>
<li>&nbsp; &nbsp;&nbsp;// You can change the radius</li>
<li>&nbsp; &nbsp;&nbsp;var ball = new Ball(width*Math.random(),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; height*Math.random(),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong style="color: red;">(2*Math.PI)*Math.random(), // angle</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong style="color: red;">(10*Math.random())-5, &nbsp; &nbsp; &nbsp;// speed</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;30);</li>
<li> </li>
<li>&nbsp; &nbsp;// We add it in an array<br></li>
<li>&nbsp; &nbsp;ballArray[i] = ball;</li>
<li>&nbsp;&nbsp;}</li>
<li>} </li>
<li> </li>
<li>function mainLoop() {</li>
<li>&nbsp;&nbsp;...</li>
<li>} </li>
<li> </li>
<li>function testCollisionWithWalls(ball) {</li>
<li>&nbsp;&nbsp;// left</li>
<li>&nbsp;&nbsp;if (ball.x &lt; ball.radius) {</li>
<li>&nbsp; &nbsp; &nbsp;ball.x = ball.radius;</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">ball</strong><strong style="color: red;">.angle = -ball.angle + Math.PI;</strong></li>
<li>&nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;// right</li>
<li>&nbsp;&nbsp;if (ball.x &gt; width - (ball.radius)) {</li>
<li>&nbsp; &nbsp; ball.x = width - (ball.radius);</li>
<li>&nbsp; &nbsp; <strong style="color: red;">ball</strong><strong style="color: red;">.angle = -ball.angle + Math.PI;</strong> </li>
<li>&nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;// up</li>
<li>&nbsp;&nbsp;if (ball.y &lt; ball.radius) {</li>
<li>&nbsp; &nbsp; ball.y = ball.radius;</li>
<li>&nbsp; &nbsp; <strong style="color: red;">ball</strong><strong style="color: red;">.angle = -ball.angle;</strong> </li>
<li>&nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;// down</li>
<li>&nbsp;&nbsp;if (ball.y &gt; height - (ball.radius)) {</li>
<li>&nbsp; &nbsp; ball.y = height - (ball.radius);</li>
<li>&nbsp; &nbsp;<strong style="color: red;"> ball</strong><strong style="color: red;">.angle =-ball.angle;</strong> </li>
<li>&nbsp;&nbsp;} </li>
<li>}</li>
<li> </li>
<li>// constructor function for balls</li>
<li>function Ball(x, y, angle, v, diameter) {</li>
<li>&nbsp;&nbsp;this.x = x;</li>
<li>&nbsp;&nbsp;this.y = y;</li>
<li>&nbsp;&nbsp;<strong style="color: red;">this.angle = angle;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;this.v = v;</strong></li>
<li>&nbsp;&nbsp;this.radius = diameter/2;</li>
<li> </li>
<li>&nbsp;&nbsp;this.draw = function() {</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp;&nbsp;this.move = function() {</li>
<li>&nbsp; &nbsp;// add horizontal increment to the x pos</li>
<li>&nbsp; &nbsp;// add vertical increment to the y pos</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">this.x += this.v * Math.cos(this.angle);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;this.y += this.v * Math.sin(this.angle);</strong></li>
<li>&nbsp;&nbsp;};</li>
<li>}</li>
</ol></div><br>

Using angles or horizontal and vertical increments is equivalent. However, one method might be preferable to the other: for example, to control an object that follows the mouse, or that tracks another object in order to attack it, angles would be more practical input to the computations required.


#### Notes for 2.5.1 Animating multiple objects

+ Pseudo class
  + define a constructor function for creating objects
  + found in other object-oriented languages, such as Java, C#, etc.
  + useful to create many objects of the same classes

+ Example: multiple balls
  + constructor function for balls w/ x & y velocity<a name="ballXY"></a>: `function Ball(x, y, vx, vy, diameter) {...}`
    + declare ball properties: `this.x = x; this.y = y; this.vx = vx; this.vy = vy; this.radius = diameters/2;`
    + draw ball: `this.draw = function() { ctx.beginPath(); ctx.arc(this.x, this.y, this.radius, 0.2*Math.PI); ctx.fill(); };`
    + move ball: `this.move = function() { this.x += this.x; this.y += this.y; };`
  + declare variables<a name="vars"></a>: `var canvas, ctx, width, height;`
  + declare array of balls<a name="ballArray"></a>: `var ballArray = [];`
  + init page after DOM ready<a name="init"></a>: `function init() {...}`
    + access canvas and set context: `var canvas = document.querySelector("#myCanvas"); var ctx = canvas.getContext("2d");`
    + set varables: `width = canvas.width; height = canvas.height;`
    + call to create balls: `createBalls(16);`
    + start animation loop: `requestAnimationFrame(mainLoop);`
  + create balls w/ x, y velocity: `function createBalls(numberOfBalls) {...}`
    + iterate to create balls: `for (var i-0; i<numberOfBalls; i++) {...}`
    + create ball: `var ball = new Ball(width*Math.random(), height*Math.random(), (10*Math.random())-5, (10*Math.random())-5, 30);`
    + add ball to array: `ballArray[i] = ball;`
  + create animation loop<a name="animationLoop"></a>: `function mainLoop() {...}`
    + empty canvas: `ctx.clearRect(0, 0, width, height);`
    + draw balls through loop: `for (var i=0; i<ballArray.length; i++) {...}`
      + get the ball: `var ball = ballArray[i];`
      + move the ball: `ball.move();`
      + call to test collision: `textCollisionWithWalls(ball);`
      + draw the ball: `ball.draw();`
    + request for next frame: `window.requestAnimationFrame(mainLoop);`
  + test collision w/ x, y velocity: `function testCollisionWithWalls(ball) {...}`
    + (x, y): center of the circle
    + collision: replace the ball at position where it's exactly in contact w/ the border
    + test collision independently, `if...else if` not suitable
    + left collision: `if (ball.x < (ball.radius)) { ball.x = ball.radius; ball.vx *= -1; }`
    + right collision: `if (ball.x > width - ball.radius) { ball.x = width - ball.radius; ball.vx *= -1; }`
    + up collision: `if (ball.y < (ball.radius)) { ball.y = ball.radius; ball.vy *= -1; }`
    + down collision: `if (ball.y > width - ball.radius) { ball.y = height - ball.radius; ball.vy *= -1; }`

+ Example: direction and velocity with wall collisions
  + [declare variables](#vars)
  + declare [array of balls](#ballArray)
  + [init page after DOM ready](#init)
  + create balls w/ angle & speed: `function createBalls(numberOfBalls) {...}`
    + iterate to create balls: `for (var i-0; i<numberOfBalls; i++) {...}`
    + create ball: `var ball = new Ball(width*Math.random(), height*Math.random(), (2*Math.PI)*Math.random(), (10*Math.random())-5, 30);`
    + add ball to array: `ballArray[i] = ball;`
  + create [animation loop](#animationLoop)
  + test collision w/ angle & speed: `function testCollisionWithWalls(ball) {...}`
    + test collision independently, `if...else if` not suitable
    + left collision: `if (ball.x < (ball.radius)) {ball.x = ball.radius; ball.angle = -ball.angle + Math.PI;}`
    + right collision: `if (ball.x > width - ball.radius) {ball.x = width - ball.radius; ball.angle = -ball.angle + Math.PI;}`
    + up collision: `if (ball.y < (ball.radius)) {ball.y = ball.radius; ball.angle = -ball.angle;}`
    + right collision: `if (ball.y > width - ball.radius) {ball.y = width - ball.radius; ball.angle = -ball.angle;}`
  + constructor function for balls w/ speed and angle<a name="ballSA"></a>: `function Ball(x, y, angle, v, diameter) {...}`
    + declare ball properties: `this.x = x; this.y = y; this.angle = angle; this.v = v; this.radius = diameters/2;`
    + draw ball: `this.draw = function() { ctx.beginPath(); ctx.arc(this.x, this.y, this.radius, 0.2*Math.PI); ctx.fill(); };`
    + move ball: `this.move = function() { this.x += this.v * Math.cos(this.angle); this.y += this.v * Math.sin(this.angle); };`


### 2.5.2 Adding balls to the game framework

This time, let's extract the source code used to create the balls, and include it in our game framework. We are also going to use time-based animation. The distance that the player and each ball should move is computed and may vary between animation frames, depending  on the time-delta since the previous frame.

[Online example](https://jsbin.com/tehuve/edit) at JSBin.

[Local Demo](src/02e-example03.html)

Try to move the monster with arrow keys and use the mouse button while moving to change the monster's speed. Look at the source code and change the parameters controlling the creation of the balls: number, speed, radius, etc. Also, try changing the monster's default speed. See the results.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3xEXEuO')"
    src    = "https://bit.ly/3gPYw8Y"
    alt    = "Monster + balls in the game framework. On the screen we see the monster + a bunch of balls"
    title  = "Monster + balls in the game framework. On the screen we see the monster + a bunch of balls"
  />
</figure>

For this version, we copied and pasted some code from the previous example and we also modified the mainLoop to make it more readable. In a next lesson, we will split the game engine into different files and clean the code-base to make it more manageable. But for the moment, jsbin.com is a good playground to try-out and test things...

The new mainLoop:

<div><ol>
<li value="1">var mainLoop = function(time){</li>
<li>&nbsp;&nbsp;//main function, called each frame </li>
<li>&nbsp; measureFPS(time);</li>
<li> </li>
<li>&nbsp;&nbsp;// number of ms since last frame draw</li>
<li>&nbsp; delta = timer(time);</li>
<li> </li>
<li>&nbsp;&nbsp;// Clear the canvas</li>
<li>&nbsp; clearCanvas();</li>
<li> </li>
<li>&nbsp;&nbsp;// Draw the monster</li>
<li>&nbsp; drawMyMonster(monster.x, monster.y);</li>
<li> </li>
<li>&nbsp;&nbsp;// Check inputs and move the monster</li>
<li>&nbsp; updateMonsterPosition(delta);</li>
<li> </li>
<li>&nbsp;&nbsp;// Update and draw balls</li>
<li>&nbsp; updateBalls(delta);</li>
<li> </li>
<li>&nbsp;&nbsp;// Call the animation loop every 1/60th of second</li>
<li>&nbsp; requestAnimationFrame(mainLoop);</li>
<li> };</li>
</ol></div><br>

As you can see, we draw the player/monster, we update its position; and we call an `updateBalls` function to do the same  for the balls: draw and update their position.

<div><ol>
<li value="1">function updateMonsterPosition(delta) {</li>
<li>&nbsp; monster.speedX = monster.speedY = 0;</li>
<li>&nbsp;&nbsp;// check inputStates</li>
<li>&nbsp;&nbsp;if (inputStates.left) {</li>
<li>&nbsp; &nbsp; monster.speedX = -monster.speed;</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;if (inputStates.up) {</li>
<li>&nbsp; &nbsp; monster.speedY = -monster.speed;</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp; ...</li>
<li> </li>
<li>&nbsp;&nbsp;// Compute the incX and incY in pixels depending</li>
<li>&nbsp;&nbsp;// on the time elapsed since last redraw</li>
<li>&nbsp; monster.x += calcDistanceToMove(delta, monster.speedX);</li>
<li>&nbsp; monster.y += calcDistanceToMove(delta, monster.speedY);</li>
<li>}</li>
<li> </li>
<li>function updateBalls(delta) {</li>
<li>&nbsp;&nbsp;// for each ball in the array</li>
<li>&nbsp;&nbsp;for(var i=0; i &lt; ballArray.length; i++) {</li>
<li>&nbsp; &nbsp;var ball = ballArray[i];</li>
<li> </li>
<li>&nbsp; &nbsp;// 1) move the ball</li>
<li>&nbsp; &nbsp;ball.move(); </li>
<li> </li>
<li>&nbsp; &nbsp;// 2) test if the ball collides with a wall</li>
<li>&nbsp; &nbsp;testCollisionWithWalls(ball);</li>
<li> </li>
<li>&nbsp; &nbsp;// 3) draw the ball</li>
<li>&nbsp; &nbsp;ball.draw();</li>
<li> }</li>
<li>} </li>
</ol></div><br>

Now, in order to turn this into a game, we need to create some interactions between the player (the monster) and the obstacles/enemies (balls, walls)... It's time to take a look at collision detection.


#### Notes for 2.5.2 Adding balls to the game framework

+ Example: game framework w/ bouncing balls
  + tasks:
    + move the moster w/ arrow keys
    + accelerate monster w/ mouse button
    + animate bouncing balls
  + generate animation loop<a name="mainLoop"></a>: `var mainLoop = function(time) {...}`
    + call to measure FPS: `measureFPS(time);`
    + clear canvas: `clearCanvas();`
    + call to draw monster: `drawMyMonster(monster.x, monster.y);`
    + call to move monster: `updateMonsterPosition(delta);`
    + call to draw balls: `updateBalls(delta);`
    + call for next frame: `requestAnimationFrame(mainLoop);`
  + calculate the new position of monster: `function updateMonsterPosition(delta) {...}`
    + init speed: `monster.speedX = monster.speedY = 0;`
    + set left arrow key: `if (inputStates.left) { monster.speedX = -monster.speed; }`
    + set up arrow key: `if (inputStates.up) { monster.speedY = -monster.speed; }`
    + ...
    + compute the position: `monster.x += calcDistanceToMove(delta, monster.speedX); monster.y += calcDistanceToMove(delta, monster.speedY);`
  + draw balls w/ new position: `function updateBalls(delta) {...}`
    + iterate all balls: `for (var i=0; i<ballArray.length; i++) {...}`
    + call to move ball: `ball.move();`
    + call to test wall collision: `testCollisionWithWalls(ball);`
    + call to draw ball: `ball.draw();`


### 2.5.3 Collision detection

In this chapter, we explore some techniques for detecting collisions between objects. This includes moving and static objects. We first present three "classic" collision tests, and follow them with brief sketches of more complex algorithms.

#### Circle collision test

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3vJxHZv')"
    src    = "https://bit.ly/3cZ1O8K"
    alt    = "two circles with distances between the centers drawn"
    title  = "two circles with distances between the centers drawn"
  />
</figure>


Collision between circles is easy. Imagine there are two circles:

1. Circle `c1` with center `(x1,y1)` and radius `r1`;
1. Circle `c2` with center `(x2,y2)` and radius `r2`.

Imagine there is a line running between those two center points. The distances from the center points to the edge of each circle is, by definition, equal to their respective radii. So:

+ if the edges of the circles touch, the distance between the centers is `r1+r2;`
+ any greater distance and the circles don't touch or collide; whereas
+ any less and they do collide or overlay.

<font style="color: red;">In other words: if the distance between the center points is less than the sum of the radii, then the circles collide.</font>

<div><ol>
<li value="1">function circleCollideNonOptimised(x1, y1, r1, x2, y2, r2) {</li>
<li>&nbsp;&nbsp;var dx = x1 - x2;</li>
<li>&nbsp;&nbsp;var dy = y1 - y2;</li>
<li>&nbsp;&nbsp;<strong style="color: red;">var distance = Math.sqrt(dx * dx + dy * dy);</strong></li>
<li> </li>
<li>&nbsp;&nbsp;return (distance &lt; r1 + r2); </li>
<li>}</li>
</ol></div><br>

This could be optimized a little averting the need to compute a square root:

<div><ol>
<li value="1">(x2-x1)^2 + (y1-y2)^2 &lt;= (r1+r2)^2</li>
</ol></div><br>

Which yields:

<div><ol>
<li value="1">function circleCollide(x1, y1, r1, x2, y2, r2) {</li>
<li> var dx = x1 - x2;</li>
<li> var dy = y1 - y2;</li>
<li> return ((dx * dx + dy * dy) &lt; (r1 + r2)*(r1+r2)); </li>
<li>}</li>
</ol></div><br>

This technique is attractive because a "bounding circle" can often be used with graphic objects of other shapes, providing they are not too elongated horizontally or vertically.

#### Test the idea

Try [this example at JSBin](https://jsbin.com/ciyiko/edit): move the monster with the arrow keys and use the mouse to move "the player": a small circle. Try to make collisions between the monster and the circle you control.

[Local Demo](src/02e-example04.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3vJxHZv')"
    src    = "https://bit.ly/3h8CCy7"
    alt    = "monster and small circle: collision, they are drawn in red and a 'collision' message appears"
    title  = "monster and small circle: collision, they are drawn in red and a 'collision' message appears"
  />
</figure>

This online example uses the game framework (without time-based animation in this one). We just added a "player" (for the moment, a circle that follows the mouse cursor), and a "monster". We created two JavaScript objects for describing the monster and the player, and these objects both have a `boundingCircleRadius` property:

Let's implement this as a JavaScript function step-by-step:

<div><ol>
<li value="1">// The monster!</li>
<li>var monster = {</li>
<li>&nbsp; x:80,</li>
<li>&nbsp; y:80,</li>
<li>&nbsp; width: 100,</li>
<li>&nbsp; height : 100,</li>
<li>&nbsp; speed:1,</li>
<li>&nbsp;<strong style="color: red;"> boundingCircleRadius</strong><strong style="color: red;">: 70</strong> </li>
<li> };</li>
<li> </li>
<li>var player = {</li>
<li>&nbsp; x:0,</li>
<li>&nbsp; y:0,</li>
<li>&nbsp; <strong style="color: red;">boundingCircleRadius</strong><strong style="color: red;">: 20</strong> </li>
<li>};</li>
</ol></div><br>

The collision test occurs in the main loop:

<div><ol>
<li value="1">var mainLoop = function(time){</li>
<li>&nbsp;&nbsp;//main function, called each frame </li>
<li>&nbsp; measureFPS(time);</li>
<li> </li>
<li>&nbsp;&nbsp;// Clear the canvas</li>
<li>&nbsp; clearCanvas();</li>
<li> </li>
<li>&nbsp;&nbsp;// Draw the monster</li>
<li>&nbsp; drawMyMonster();</li>
<li> </li>
<li>&nbsp;&nbsp;// Check inputs and move the monster</li>
<li>&nbsp; updateMonsterPosition();</li>
<li> </li>
<li>&nbsp; updatePlayer();</li>
<li> </li>
<li>&nbsp; <strong style="color: red;">checkCollisions</strong><strong style="color: red;">();</strong></li>
<li> </li>
<li>&nbsp;&nbsp;// Call the animation loop every 1/60th of second</li>
<li>&nbsp; requestAnimationFrame(mainLoop);</li>
<li> };</li>
<li> </li>
<li>function updatePlayer() {</li>
<li>&nbsp;&nbsp;// The player is just a circle drawn at the mouse position</li>
<li>&nbsp;&nbsp;// Just to test circle/circle collision.</li>
<li> </li>
<li>&nbsp;&nbsp;if(inputStates.mousePos) { &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Move the player and draw it as a circle</li>
<li>&nbsp; &nbsp; player.x = inputStates.mousePos.x; &nbsp;// when the mouse moves</li>
<li>&nbsp; &nbsp; player.y = inputStates.mousePos.y;</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li>&nbsp; &nbsp; ctx.arc(player.x, player.y, player.boundingCircleRadius, 0, 2*Math.PI);</li>
<li>&nbsp; &nbsp; ctx.stroke();</li>
<li>&nbsp;&nbsp;}</li>
<li> }</li>
<li> </li>
<li>function checkCollisions() {</li>
<li>&nbsp;<strong style="color: red;">&nbsp;</strong><strong style="color: red;">if(circleCollide(player.x, player.y, player.boundingCircleRadius, </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monster.x, monster.y, monster.boundingCircleRadius))</strong> {<br>&nbsp; &nbsp; // Draw everything in red</li>
<li>&nbsp; &nbsp; ctx.fillText("Collision", 150, 20);</li>
<li>&nbsp; &nbsp; ctx.strokeStyle = ctx.fillStyle = 'red';</li>
<li>&nbsp;&nbsp;} else {<br>&nbsp; &nbsp; // Draw in black</li>
<li>&nbsp; &nbsp; ctx.fillText("No collision", 150, 20);</li>
<li>&nbsp; &nbsp; ctx.strokeStyle = ctx.fillStyle = 'black';</li>
<li>&nbsp;&nbsp;}</li>
<li> }</li>
<li> </li>
<li><strong style="color: red;">function circleCollide(x1, y1, r1, x2, y2, r2) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;var dx = x1 - x2;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;var dy = y1 - y2;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;return ((dx * dx + dy * dy) &lt; (r1 + r2)*(r1+r2)); </strong></li>
<li><strong style="color: red;">}</strong></li>
</ol></div><br>


#### [Advanced technique] Collision detection with complex shapes

__[Advanced technique] Use several bounding circles for complex shapes, recompute bounding circles when the shape changes over time (animated objects)__

This is an advanced technique: you can use a list of bounding circles or better still, a hierarchy of bounding circles in order to reduce the number of tests. The image below of an "arm" can be associated with a hierarchy of bounding circles. First, test against the "big one" on the left that contains the whole arm, then if there is a collision, test for the two sub-circles, etc... this recursive algorithm will not be covered in this course, but it's a classic optimization. (left diagram)

In 3D, you can use spheres instead of circles: (right diagram)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="url" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3gKp2lm"
      alt   = "mage of an arm with a hierarchy of bounding circles: one for the whole arm, and two smaller for the forearm and the other part"
      title = "mage of an arm with a hierarchy of bounding circles: one for the whole arm, and two smaller for the forearm and the other part"
    >
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3cZ5FTa"
      alt   = "a 3D object (a lamp) with bounding spheres"
      title = "a 3D object (a lamp) with bounding spheres"
    >
  </a>
</div>

The famous game Gran Turismo 4 on the PlayStation 2 uses bounding spheres for detecting collisions between cars:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3vJxHZv')"
    src    = "https://bit.ly/3zNYIy2"
    alt    = "Grand turismo used collisions between bounding spheres: image of the game (a car on a road track)"
    title  = "Grand turismo used collisions between bounding spheres: image of the game (a car on a road track)"
  />
</figure>


#### Rectangle detection test

__Rectangle (aligned along X and Y axis) detection test__

Let's look at a simple illustration:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3vJxHZv')"
    src    = "https://bit.ly/3wPCRo9"
    alt    = "two pictures: one with non intersected rectangles: the projection of horizontal sides of rectangles to the X axis do not intersect (then rectangles do not intersect), the other with both projections intersect (rectangles intersect)"
    title  = "two pictures: one with non intersected rectangles: the projection of horizontal sides of rectangles to the X axis do not intersect (then rectangles do not intersect), the other with both projections intersect (rectangles intersect)"
  />
</figure>


From this:

To detect a collision between two aligned rectangles, we project the horizontal and vertical axis of the rectangles over the X and Y axis. If both projections overlap, there is a collision!

Try this online demonstration of rectangle - [rectangle detection](https://silentmatt.com/rectangle-intersection/)

1 - Only horizontal axis projections overlap: no collision between rectangles (left diagram)

2 - Only vertical axis projections overlap: no collision between rectangles (middle diagram)

3 - Horizontal and vertical axis projections overlap: collision detected! (right diagram)


<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="url" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3wPDaiN"
      alt   = "Only horizontal axis overlap: no collision"
      title = "Only horizontal axis overlap: no collision"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3vH53IF"
      alt   = "Only vertical axis projections overlap: no collision"
      title = "Only vertical axis projections overlap: no collision"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3d2oO6L"
      alt   = "the projections of axis overlap: collision detected"
      title = "the projections of axis overlap: collision detected"
    >
  </a>
</div>

Here is a JavaScript implementation of a rectangle - rectangle (aligned) collision test:

<div><ol>
<li value="1">// Collisions between aligned rectangles</li>
<li>function rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2) {</li>
<li>&nbsp;&nbsp;</li>
<li>&nbsp;&nbsp;if ((x1&nbsp;&gt; (x2 + w2)) || ((x1&nbsp;+ w1) &lt; x2))</li>
<li>&nbsp; &nbsp;&nbsp;return false; // No horizontal axis projection overlap</li>
<li> </li>
<li>&nbsp;&nbsp;if ((y1&nbsp;&gt; (y2 + h2)) || ((y1&nbsp;+ h1) &lt; y2))</li>
<li>&nbsp; &nbsp;&nbsp;return false;&nbsp;<span style="line-height: 25.6px;">// No vertical&nbsp;axis projection overlap</li>
<li> </li>
<li>&nbsp;&nbsp;return true; &nbsp; &nbsp;// If previous tests failed, then both axis projections</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // overlap and the rectangles intersect</li>
<li> }</li>
</ol></div>


#### Test the method

Try [this example](https://jsbin.com/fubima/edit) at JSBin: move the monster with the arrow keys and use the mouse to move "the player": this time a small rectangle. Try to make collisions between the monster and the circle you control. Notice that this time the collision detection is more accurate and can work with elongated shapes.

[Local Demo](src/02e-example05.html)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3vJxHZv" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3iXktpr"
      alt   = "Player as a square is inside the monster bounding circle but not inside the bounding rectangle, as we use rect rect collision test: no collision detected"
      title = "Player as a square is inside the monster bounding circle but not inside the bounding rectangle, as we use rect rect collision test: no collision detected"
    >
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3jgHdB1"
      alt   = "Same as previous picture but this time the player square is inside the monster bounding rectangle: collision detected"
      title = "Same as previous picture but this time the player square is inside the monster bounding rectangle: collision detected"
    >
  </a>
</div>


Here is what we modified (in bold) in the code:

<div><ol>
<li value="1">...</li>
<li value="1">// The monster!</li>
<li>var monster = {</li>
<li>&nbsp; x: 80,</li>
<li>&nbsp; y: 80,</li>
<li>&nbsp; width: 100,</li>
<li>&nbsp; height: 100,</li>
<li>&nbsp; speed: 1,</li>
<li>&nbsp; boundingCircleRadius: 70</li>
<li>};</li>
<li>&nbsp;</li>
<li>var player = {</li>
<li>&nbsp; x: 0,</li>
<li>&nbsp; y: 0,</li>
<li>&nbsp; boundingCircleRadius: 20</li>
<li>};</li>
<li>...</li>
<li>&nbsp;</li>
<li>function updatePlayer() {</li>
<li>&nbsp; // The player is just a square drawn at the mouse position</li>
<li>&nbsp; // Just to test rectangle/rectangle collisions.</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;if (inputStates.mousePos) {</li>
<li>&nbsp; &nbsp; player.x = inputStates.mousePos.x;</li>
<li>&nbsp; &nbsp; player.y = inputStates.mousePos.y;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; <strong style="color: red;">// draws a rectangle centered on the mouse position</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; // we draw it as a square.</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; // We remove size/2 to the x and y position at drawing time in</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; // order to recenter the rectangle on the mouse pos (normally </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; // the 0, 0 of a rectangle is at its top left corner)</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;var size = player.boundingCircleRadius;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; ctx.fillRect(player.x - size / 2, player.y - size / 2, size, size);</strong></li>
<li>&nbsp;&nbsp;}</li>
<li>}</li>
<li>&nbsp;</li>
<li>function checkCollisions() {</li>
<li>&nbsp; <strong style="color: red;">// Bounding rect position and size for the player. We need to translate</strong></li>
<li><strong style="color: red;">&nbsp; // it to half the player's size</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;var playerSize = player.boundingCircleRadius;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;var playerXBoundingRect = player.x - playerSize / 2;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;var playerYBoundingRect = player.y - playerSize / 2;</strong></li>
<li><strong style="color: red;">&nbsp; // Same with the monster bounding rect</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;var monsterXBoundingRect = monster.x - monster.width / 2;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;var monsterYBoundingRect = monster.y - monster.height / 2;</strong></li>
<li><strong style="color: red;">&nbsp;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;if (rectsOverlap(playerXBoundingRect, playerYBoundingRect, </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;playerSize, playerSize, </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monsterXBoundingRect, monsterYBoundingRect, </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monster.width, monster.height)) {</strong></li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("Collision", 150, 20);</li>
<li>&nbsp; &nbsp; &nbsp;ctx.strokeStyle = ctx.fillStyle = 'red';</li>
<li>&nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("No collision", 150, 20);</li>
<li>&nbsp; &nbsp; &nbsp;ctx.strokeStyle = ctx.fillStyle = 'black';</li>
<li>&nbsp;&nbsp;}</li>
<li>}</li>
<li>&nbsp;</li>
<li><strong style="color: red;">// Collisions between aligned rectangles</strong></li>
<li><strong style="color: red;">function rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2) {</strong></li>
<li><strong style="color: red;">&nbsp;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;if ((x1 &gt; (x2 + w2)) || ((x1 + w1) &lt; x2))</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;return false; // No horizontal axis projection overlap</strong></li>
<li><strong style="color: red;"></strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;if ((y1 &gt; (y2 + h2)) || ((y1 + h1) &lt; y2))</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;return false; // No vertical axis projection overlap</strong></li>
<li><strong style="color: red;"></strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;return true; // If previous tests failed, then both axis projections</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// overlap and the rectangles intersect</strong></li>
<li><strong style="color: red;">}</strong></li>
</ol></div><br>


#### Many real games use aligned rectangle collision tests

Testing "circle-circle" or "rectangle-rectangle collisions is cheap in terms of computation. "Rectangle-rectangle" collisions are used in many 2D games, such as [Dodonpachi](https://www.youtube.com/watch?v=cgcWY0nOuCI) (one of the most famous and enjoyable shoot'em'ups ever made - you can play it using the MAME arcade game emulator):

You could also try the free Genetos shoot'em up game (Windows only) that retraces the history of the genre over its different levels ([download here](https://tatsuya-koyama.com//works/games/genetos/)). Press the G key to see the bounding rectangles used for collision test. Here is a screenshot:

These games run at 60 fps and can have hundreds of bullets moving at the same time. Collisions have to be tested: did the player's bullets hit an enemy, AND did an enemy bullet (for one of the many enemies) hit the player? These examples demonstrate the efficiency of such collision test techniques.


#### Other collision tests

In this section, we only give sketches and examples of more sophisticated collision tests. For further explanation, please follow the links provided.


__Aligned rectangle-circle__

There are only two cases when a circle intersects with a rectangle:

+ Either the circle's center lies inside the rectangle, or
+ One of the edges of the rectangle intersects the circle.

We propose this function (implemented after reading [this Thread at StackOverflow](https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection)):

<div><ol>
<li value="1">// Collisions between rectangle and circle</li>
<li>function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {</li>
<li>&nbsp; &nbsp;var testX=cx; </li>
<li>&nbsp; &nbsp;var testY=cy; </li>
<li> </li>
<li>&nbsp; &nbsp;if (testX &lt; x0) testX=x0; </li>
<li>&nbsp; &nbsp;if (testX &gt; (x0+w0)) testX=(x0+w0); </li>
<li>&nbsp; &nbsp;if (testY &lt; y0) testY=y0; </li>
<li>&nbsp; &nbsp;if (testY &gt; (y0+h0)) testY=(y0+h0); </li>
<li> </li>
<li>&nbsp; &nbsp;return (((cx-testX)*(cx-testX)+(cy-testY)*(cy-testY))&lt;&nbsp;r*r); </li>
<li> }</li>
</ol></div><br>

Try this function in [this example](https://jsbin.com/acohiv/845/edit?html,output) on JSBin.

[Local Demo](src/02e-example06.html)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3vJxHZv" ismap target="_blank">
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3gWvF2Y"
      alt   = "Circle and rectangle not in collisioncircle collides a rectangle"
      title = "Circle and rectangle not in collisioncircle collides a rectangle"
    >
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3zNm5bd"
      alt   = "Circle and rectangle not in collisioncircle collides a rectangle"
      title = "Circle and rectangle not in collisioncircle collides a rectangle"
    >
  </a>
</div>


#### [ADVANCED] Collision between balls (pool like)


+ Math and physics: please read this external resource (for math), a [great article](https://web.archive.org/web/20181231090226/http://archive.ncsa.illinois.edu/Classes/MATH198/townsend/math.html) that explains the physics of a pool game.
+ [Example of colliding balls](https://jsbin.com/juzefa/edit) at JSBin (author: M.Buffa), and also try [this example](https://jsbin.com/nopefe/edit) that does the same with a blurring effect

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3vJxHZv')"
    src    = "https://bit.ly/3wPpOmM"
    alt    = "ball ball collision example"
    title  = "ball ball collision example"
  />
</figure>


The principle behind collision resolution for pool balls is as follows. You have a situation where two balls are colliding, and you know their velocities (step 1 in the diagram below). You separate out each ball's velocity (the solid blue and green arrows in step 1, below) into two perpendicular components: the "normal" component heading towards the other ball (the dotted blue and green arrows in step 2) and the "tangential" component that is perpendicular to the other ball (the dashed blue and green arrows in step 2). We use "normal" for the first component as its direction is along the line that links the centers of the balls, and this line is perpendicular to the collision plane (the plane that is tangent to the two balls at collision point).

The solution for computing the resulting velocities is to swap the components between the two balls (as we move from step 2 to step 3), then finally recombine the velocities for each ball to achieve the result (step 4):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3vJxHZv')"
    src    = "https://bit.ly/35G82qa"
    alt    = "diagram with two balls, velocities, tengeantial and normal planes"
    title  = "diagram with two balls, velocities, tengeantial and normal planes"
  />
</figure>


The above picture has been borrowed from [this interesting article](https://sinepost.wordpress.com/2012/09/05/making-your-balls-bounce/) about how to implement in C# pool like collision detection.

Of course, we will only compute these steps if the balls collide, and for that test we will have used the basic circle collision test outlined earlier.

To illustrate the algorithm, [here is an example at JSBin](https://jsbin.com/vuqeti/6/edit) that displays the different vectors in real time, with only two balls. The math for the collision test have also been expanded in the source code to make computations clearer. Note that this is not for beginners: advanced math and physics are involved!

[Local Demo](src/02e-example07.html)


#### To go further... video game physics!


For the ones who are not afraid by some math and physics and would like to learn how to do collision detection in a more realistic way (using physics modeling), we recommend [this tutorial](https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics), that is the first of a three-part series about video game physics.


#### Notes for 2.5.3 Collision detection

+ Circle collision test
  + objects: (left diagram)
    + circle `c1` w/ center `(x1, y1)` and radius `r1`
    + circle `c2` w/ center `(x2, y2)` and radius `r2`
  + imaging a line running btw two center points
  + scenarios btw distance and radii of circles
    + $\overline{c_1 c_2} = r_1 + r_2$: the edges of the circles touch
    + $\overline{c_1 c_2} > r_1 + r_2$: the circles neither touched nor collided
    + $\overline{c_1 c_2} < r_1 + r_2$: the circles collided or overlaid
  + Javascript snippet: `function circleCollideNonOptimised(x1, y1, r1, x2, y2, r2) {...}`
    + declare variables: `var dx = x1 - x2; dy = y1 - y2;`
    + compute distance: `var distance = Math.sqrt(dx * dx + dy * dy);`
    + return boolean value: `return (distance < r1 + r2);`
  + complex shapes (right diagrams)
    + using a list of bounding circles or a hierarchy of bounding circles
    + a hierarchy of bounding circles (middle diagram)
      + test against the "big one" on the left containing the whole arm
      + collision $\implies$ test for two-sub-circles
      + ...

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/3vJxHZv" ismap target="_blank">
      <img style="margin: 0.1em;" height=150
        src   = "https://bit.ly/3cZ1O8K"
        alt   = "two circles with distances between the centers drawn"
        title = "two circles with distances between the centers drawn"
      >
      <img style="margin: 0.1em;" height=150
        src   = "https://bit.ly/3gKp2lm"
        alt   = "mage of an arm with a hierarchy of bounding circles: one for the whole arm, and two smaller for the forearm and the other part"
        title = "mage of an arm with a hierarchy of bounding circles: one for the whole arm, and two smaller for the forearm and the other part"
      >
    </a>
  </div>

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
</div>

+ Example: circle collision test
  + declare monster object<a name="monsterObj"></a>: `var monster = {x:80, y:80, width:100, heigh:100, speed:1, boundingCircleRadius:70};`
  + declare player object<a name="playerObj"></a>: `var player = {x:0, y:0, boundingCircleRadius:20}`
  + generate [animation loop](#mainLoop) adding  player and collision after moster position
    + call to get player position: `updatePlayer();`
    + call to check collision: `checkCollisions();`
  + calculate player position: `function updatePlayer() {...}`
    + player just a circle drawn at the mouse position
    + check mouse position to move the player and draw circle: `if (inputStates.mousePos) {...}`
      + player position: `player.x = inputStates.mousePos.x; player.y = inputStates.mouseStates.mousePos.y;`
      + draw circle: `ctx.beginPath(); ctx.arc(player.x, player.y, player.boundingCircleRadius, 0, 2*Math.PI); x=ctx.stroke();`
  + check collision: `function testCollisions() {...}`
    + call to check collision: `if (circleCollide(player.x, player.y, player.boundingCircleRadius, monster.x monster.y, monster.boundingCircleRadius)) { //red } else { // black }`
    + collide to draw red: `ctx.fillText("Collision", 150, 20); ctx.strokeStyle = ctx.fillStyle = 'red';`
    + non-collide to draw black: `ctx.fillText("No collision", 150, 20); ctx.strokeStyle = ctx.fillStyle = 'black';`
  + check circle collision: `function circleCollide(x1, y1, r1, x2, y2, r2) {...}`
    + compute differences: `var dx = x1 - x2; dy = y1 - y2;`
    + check collision or not: `return ((dx * dx + dy * dy) < (r1 + r2)*(r1 + r2));`

+ Rectangle detection test
  + projecting the horizontal and vertical axis of the rectangles over the X and Y asix
  + scenarios:
    + only horizontal axis projection overlapped: no collision
    + only vertical axis projection overlapped: no collision
    + both horizontal and vertical projectsions overlapped: collision detected
  + JavaScript snippet: `function rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2) {...}`
    + only horizontal overlap: `if ((x1 > (x2+w2)) || ((x1 + w1) < x2)) return false;`
    + only vertical overlap: `if ((y1 > (y2+h2)) || ((y1+h1) < y2)) return false;`
    + both axes overlap: `return true;`

+ Example: rectangle collision test
  + declare [monster object](#monsterObj)
  + declare [player object](#playerObj)
  + calculate player position: `function updatePlayer() {...}`
    + draw a rectangle centered on the mouse position
    + check mouse position to move the player and draw circle: `if (inputStates.mousePos) {...}`
      + player position: `player.x = inputStates.mousePos.x; player.y = inputStates.mouseStates.mousePos.y;`
      + draw circle: `var size = player.boundingCircleRadius; ctx.fillRect(player.x - size/2, player.y - size/2, size, size);`
  + check collision: `function testCollisions() {...}`
    + get player boundaries: `var playerSize = player.boundingCircleRadius; var playerXBoundingRect = player.x - playerSize/2; var playerYBoundingRect = player.y - playerSize/2;`
    + get mouse boundaries: `var monsterXBondingRect = monster.x - monster.width/2; var monsterYBondingRect = monster.y - monster.height/2;`
    + call to check collision: `if (rectsOverlap(playerXBondingRect, playerYBonsingRect, playerSize, playerSize, monsterXBondingRect, monsterYBondingRect, monster.width, monster.height)) { //red } else { // black }`
      + collide to draw red: `ctx.fillText("Collision", 150, 20); ctx.strokeStyle = ctx.fillStyle = 'red';`
      + non-collide to draw black: `ctx.fillText("No collision", 150, 20); ctx.strokeStyle = ctx.fillStyle = 'black';`
    + check rectangle collision: `function rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2) {...}`
      + no horizontal overlap: `if ((x1 > (x2 + w2)) || ((x1 + w1) < x2)) return false;`
      + no vertical overlap: `if ((y1 > (y2+h2)) || ((y1+h1) < y2)) return false;`
      + both overlap: `return true;`

+ Rectangle-circle collision
  + [scenarios](https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection)
    + circle's center lying inside the rectangle
    + one of the edges of the rectngle interacting the circle
  + JavaScript snippet: `function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {...}`
    + declare and set circle center: `var testX = cx; var testY = cy;`
    + left collision: `if (testX < x0) testX = x0;`
    + right collision: `if (testX > (x0+w0)) testX = (x0+w0);`
    + top collision: `if (testY < y0) testY = y0;`
    + buttom collision: `if (testY > (y0+h0)) testY = (y0+h0);`
    + return collision check: `return (((cx-testX)*(cx-testX) - (cy-testY)*(cy-testY)) < r*r);`

+ Ball collision - pool like
  + two balls collide and know their velocities (step 1)
  + separate each ball's velocity into perpenduclar componnets (step 2)
    + "normal" component: heading twoward the other ball
    + "tangential" component: perpendicular to the other ball
    + using "normal" for the first component as its direction along the line linking the centers of the balls
    + line perpendicular to the collision plane, tangent to the two balls at collision point
  + swap the components btw two balls (step 3)
  + recombine the velocities for each ball (step 4)

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://sinepost.wordpress.com/2012/09/05/making-your-balls-bounce/')"
      src    = "https://bit.ly/35G82qa"
      alt    = "diagram with two balls, velocities, tengeantial and normal planes"
      title  = "diagram with two balls, velocities, tengeantial and normal planes"
    />
  </figure>

  + Ref: [Video Game Physics Tutorial - Part I: An Introduction to Rigid Body Dynamics](https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics)



### 2.5.4 Adding collision detection to the game framework

Our previous lesson enabled us to animate balls in the game framework (this example).

Now we can add the functionality presented in the last lesson, to perform collision tests between a circle and a rectangle. It will be called 60 times/s when we update the position of the balls. If there is a collision between a ball (circle) and the monster (rectangle), we set the ball color to red.

Try [the example](https://jsbin.com/bohebe/edit?js,output) at JsBin!

[Local Demo](src/02e-example08.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3d7dir0')"
    src    = "https://bit.ly/3xISQEx"
    alt    = "Collision between balls and the monster"
    title  = "Collision between balls and the monster"
  />
</figure>


Source code extract:

<div><ol>
<li value="1">function updateBalls(delta) {</li>
<li>&nbsp; &nbsp;// for each ball in the array</li>
<li>&nbsp; &nbsp;for(var i=0; i &lt; ballArray.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;var ball = ballArray[i];</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// 1) move the ball</li>
<li>&nbsp; &nbsp; &nbsp;ball.move(); </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// 2) test if the ball collides with a wall</li>
<li>&nbsp; &nbsp; &nbsp;testCollisionWithWalls(ball);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">// 3) Test if the monster collides</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;if(circRectsOverlap(monster.x, monster.y, </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monster.width, monster.height, </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ball.x, ball.y, ball.radius)) {</strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;//change the color of the ball</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; ball.color = 'red';</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;}</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// 3) draw the ball</li>
<li>&nbsp; &nbsp; &nbsp;ball.draw();</li>
<li>&nbsp;&nbsp;}</li>
<li>} </li>
</ol></div><br>

The only additions are: _lines 13-19_ in the updateBalls function, and the `circRectsOverlap` function!


#### Notes for 2.5.4 Adding collision detection to the game framework

+ Example: game framework w/ collision detection
  + calculate ball positions: `function updateBalls(delta) {...}`
  + iterate through all balls: `for (var i=0; i<ballArray.length; i++) {...}`
  + get current ball: `var ball = ballArray[i];`
  + call self to move ball: `ball.move();`
  + call to test wall collision: `testCollisionWithWalls(ball);`
  + test collision: `if (circRectsOverlap(monster.x, monster.y, monster.width, monster.height, ball.x, ball.y, ball.radius)) { ball.color = 'red'; }`
  + call self to draw ball: `ball.draw();`


### 2.5.5 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics of discussion:

+ Have you found any good external resources about collision detection? Please share!
+ Why didn't we use non-oriented rectangle collision tests? Try to find explanations on the web. Why does it cost too much in terms of computation?
+ What would you like to see added to this part of the course?


#### Optional projects:

+ How would you animate different balls with different sizes, colors, etc?
+ How would you animate other sorts of objects: asteroids, different monsters, spaceships, etc?
+ How would you model intelligent behaviors for the enemies: go in the direction of the player, escape the player, etc?
+ Try to find a polygon-point collision test and use it with some polygon-shaped objects.
+ Here is an impressive example of ball to ball collisions, written by a student who followed this course:
  + [Original Demo](https://codepen.io/w3devcampus/pen/LYNxgzg)
  + [Local Demo](src/02e-example09.html)


