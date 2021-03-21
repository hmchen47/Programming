# Module 4: Structuring data


## 4.4 Improving the game with classes


### 4.4.1 Class and constructor

First, let's look how we were handling balls previously in our game!

We have built balls in order to fill the array of balls.

#### OLD VERSION

<div><ol>
<li value="1">function createBalls(n) {</li>
<li>&nbsp; &nbsp; // empty array</li>
<li>&nbsp; &nbsp; let ballArray = [];</li>
<li> </li>
<li>&nbsp; &nbsp; // create n balls</li>
<li>&nbsp; &nbsp; for(let i=0; i &lt; n; i++) {&nbsp;<strong>// let's build multiple times a singleton object</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>let</strong><strong> b = {&nbsp;</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x:w/2,</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; y:h/2,</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; radius: 5 + 30 * Math.random(), // between 5 and 35</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedX: -5 + 10 * Math.random(), // between -5 and + 5</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedY: -5 + 10 * Math.random(), // between -5 and + 5</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; color:getARandomColor(),</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; }</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // add ball b to the array</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ballArray.push(b);</li>
<li>&nbsp; &nbsp; } // end of for loop</li>
<li></li>
<li>&nbsp; &nbsp; // returns the array full of randomly created balls</li>
<li>&nbsp; &nbsp; return ballArray;</li>
<li>}</li>
</ol></div>

In the code above, in order to build `n` balls, we created a singleton ball object multiple times. This worked, but if we have misspelled a property name within the code, or forgot one of the properties that had to be initialized, we would have received no warnings. We will replace these lines with something like `let b = new Ball(...);`

#### NEW VERSION

Using the `new` keyword and an ES6 class

<div><ol>
<li value="1">function createBalls2(n) {</li>
<li>&nbsp; &nbsp; // empty array</li>
<li>&nbsp; &nbsp; let ballArray = [];</li>
<li> </li>
<li>&nbsp; &nbsp; // create n balls</li>
<li>&nbsp; &nbsp; for(let i=0; i &lt; n; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // Create some random values...</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; let x = w/2;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; let y = h/2;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; let radius = 5 + 30 * Math.random(); // between 5 and 35</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; let speedX = -5 + 10 * Math.random(); // between -5 and + 5</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; let speedY = -5 + 10 * Math.random(); // between -5 and + 5</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; let color = getARandomColor();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>// Create the new ball b</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; let b = new Ball(x, y, radius, color, speedX, speedY);</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // add ball b to the array</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ballArray.push(b);</li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; // returns the array full of randomly created balls</li>
<li>&nbsp; &nbsp; return ballArray;</li>
<li>}</li>
</ol></div>


Ok, not a very big change here, except that we are no longer manipulating the property names one by one, and we use the `new` keyword. 

And here is the (so far, incomplete) ES6 class for Ball (continued in the next page of this course):

<div><ol>
<li value="1"><strong>class Ball {</strong></li>
<li>&nbsp; &nbsp; <strong>constructor</strong><strong>(x, y, radius, color, speedX, speedY) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.x = x; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// properties</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.y = y;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.radius = radius;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.color = color;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.speedX = speedX;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.speedY = speedY;</li>
<li>&nbsp; &nbsp; }</li>
<li> ... // code to come for methods</li>
<li>}</li>
</ol></div>


#### Notes for 4.4.1 Class and constructor

+ Example: comparisons of constructor function and class
  + constructor function: `function createBalls1(n) {...}`
    + declare an empty array: `let ballArray = [];`
    + create `n` balls w/ properties by singleton object and add into array

      ```js
      for (let i=0; i < n; i++) { // let's build multiple times a singleton object
          let b = { 
            x: w/2, y: h/2,
            radius: 5 + 30 * Math.random(), // between 5 and 35
            speedX: -5 + 10 * Math.random(), // between -5 and + 5
            speedY: -5 + 10 * Math.random(), // between -5 and + 5
            color:getARandomColor(),
          }

        ballArray.push(b);
      }
      ```

    + return the array w/ randomly created balls: `return ballArray;`
  + constructor function w/ `new` keyword: `function createBalls2(n) {...}`
    + declare an empty array: `let ballArray = [];`
    + create `n` balls w/ properties by `new` keyword and add into array

      ```js
      for(let i=0; i < n; i++) {
        let x = w/2; let y = h/2;
        let radius = 5 + 30 * Math.random(); // between 5 and 35
        let speedX = -5 + 10 * Math.random(); // between -5 and + 5
        let speedY = -5 + 10 * Math.random(); // between -5 and + 5
        let color = getARandomColor();
 
        // Create the new ball b
        let b = new Ball(x, y, radius, color, speedX, speedY);

        ballArray.push(b);
      }
      ```

    + return the array w/ randomly created balls: `return ballArray;`
  + ES5 class: `class Ball() {...}`
    + declare constructor: `constructor(x, y, radius, color, speedX, speedY) {...}`
    + declare properties in constructor:

      ```js
      this.x = x;            // properties
      this.y = y;
      this.radius = radius;
      this.color = color;
      this.speedX = speedX;
      this.speedY = speedY;
      ```

    + declare methods: `// code for methods`


### 4.4.2 Adding methods classes

Ok, we've seen how to define the Ball class: properties and constructor. Properties are the DNA for balls: they all have an x and y position, a radius, a color, a horizontal and a vertical speed.

It is time to add some behaviors: a `draw` and a `move` method. Indeed, all balls will be able to draw and move themselves.

Here's how we were drawing a ball in the previous version of the game:

<div><ol>
<li value="1">function drawFilledCircle(<strong>c</strong>) {</li>
<li>&nbsp; &nbsp; // GOOD practice: save the context, use 2D trasnformations</li>
<li>&nbsp; &nbsp; ctx.save();</li>
<li> </li>
<li>&nbsp; &nbsp; // translate the coordinate system, draw relative to it</li>
<li>&nbsp; &nbsp; ctx.translate(<strong>c.x, c.y</strong>);</li>
<li> </li>
<li>&nbsp; &nbsp; ctx.fillStyle =<strong> c.color;</strong></li>
<li>&nbsp; &nbsp; // (0, 0) is the top left corner of the monster.</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li>&nbsp; &nbsp; ctx.arc(0, 0,<strong> c.radius</strong>, 0, 2*Math.PI);</li>
<li>&nbsp; &nbsp; ctx.fill();</li>
<li> </li>
<li> // GOOD practice: restore the context</li>
<li> ctx.restore();</li>
<li>}</li>
</ol></div>

And this how we were drawing and moving all the balls:

<div><ol>
<li value="1">function drawAllBalls(ballArray) {</li>
<li>&nbsp; &nbsp; ballArray.forEach(function(b) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; drawFilledCircle(b);</li>
<li>&nbsp; &nbsp; });</li>
<li>}</li>
<li>&nbsp;</li>
<li>function moveAllBalls(ballArray) {</li>
<li>&nbsp; &nbsp; // iterate on all balls in array</li>
<li>&nbsp; &nbsp; balls.forEach(function(b, index) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // b is the current ball in the array</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; b.x += (b.speedX * globalSpeedMutiplier);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; b.y += (b.speedY * globalSpeedMutiplier);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; testCollisionBallWithWalls(b); </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; testCollisionWithPlayer(b, index);</li>
<li> });</li>
<li>}</li>
</ol></div>


#### Adding a draw and a move method to the ES6 ball class

Instead of having these behaviors as separate functions that take a ball reference as a parameter, it is always better to put this as a method inside the class. Indeed, each ball can move, can draw itself, and the content of these methods does not bring any external dependencies.

For example, if we decide to put a method named testCollisionWithWalls inside the Ball class, it would be bad, in terms of reusability, for its content to rely on external, global variables, such as the canvas size. You could have passed the canvas as a parameter, but then you create more specialization: you have a Ball class for balls that can move inside a rectangular area that is a canvas. It's better to just pass the width and the height of the zone.

Anyway, if you plan to use your balls in another game, it is recommended that you keep the class as simple as possible. It will be more reusable in other projects.

__New version__ of the ES6 Ball class with draw and move methods:

<div><ol>
<li value="1">class Ball {</li>
<li>&nbsp; &nbsp; constructor(x, y, radius, color, speedX, speedY) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // see previous section for the code</li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; draw(<strong>ctx</strong>) { // Nearly the same as the old drawFilledCircle function</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // BEST practice: save the context, use 2D transformations</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.save();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // translate the coordinate system, draw relative to it</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.translate(<strong>this.x, this.y</strong>);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.fillStyle = <strong>this.color;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // (0, 0) is the top left corner of the monster.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.beginPath();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.arc(0, 0, <strong>this.radius</strong>, 0, 2*Math.PI);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.fill();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // BEST practice: restore the context</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.restore(); </li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; move() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.x += this.speedX;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; this.y += this.speedY; </li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
</ol></div>

Explanations:

+ _Line 6_: the `draw` function's content is nearly the same as the `drawFilledCircle` function we previously used. We replaced all `c.x`, `c.y` etc. by `this.x`, `this.y`, to use the properties of the current object. This means that when we create a ball with `var b = new Ball(...);` and when we draw it using `b.draw(ctx)`, then `this.x` will be the value of the x property of the ball b, etc.
+ _Line 23_: the move function takes no parameter as it will add the value of the speedX/speedY properties to the current `x` and `y` value of the current ball.

<span style="color: brown;">Notice that we did not take into account the <code>globalSpeedMultiplier</code> we had in the old moveAllBalls function, as this is not something that is individually relevant to each ball: it is more something that affect ALL balls. <b>This should raise an alert: use an ES6 class property for that!</b>

In other words, even if zero ball has been created, this `globalSpeedMultiplier` is set and can be modified using a slider in the graphic user interface. Consequently, it is not a ball property, __more a property of the Ball class itself.__

This setting could be created using a class property, as seen in a previous section of this course.


#### Example: draw and move balls

And here is how we can now move and draw ALL balls

<div><ol>
<li value="1">function drawAllBalls2(ballArray) {</li>
<li>&nbsp; &nbsp; ballArray.forEach(function(b) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong> b</strong><strong>.draw(ctx);</strong></li>
<li>&nbsp; &nbsp; });</li>
<li>}</li>
<li>&nbsp;</li>
<li>function moveAllBalls2(ballArray) {</li>
<li>&nbsp; &nbsp; // iterate on all balls in array</li>
<li>&nbsp; &nbsp; balls.forEach(function(b, index) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // b is the current ball in the array</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong> b</strong><strong>.move();</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; testCollisionBallWithWalls(b); </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; testCollisionWithPlayer(b, index);</li>
<li> });</li>
<li>}</li>
</ol></div>


And here is the CodePen version of the game that includes these improvements:

[CodePen Demo](https://codepen.io/w3devcampus/pen/EWzgpr)

[Local Demo](src/04d-example01.html)


#### Notes for 4.4.2 Adding methods classes

+ Example: draw and move balls w/ functions
  + drawing balls: `function drawFilledCircle(c) {...}`
    + store context: `ctx.save();`
    + translate the coordinate system: `ctx.translate(c.x, c.y);`
    + context property setting: `ctx.fillStyle = c.color;`
    + lift pen to start a new path: `ctx.beginPath();`
    + draw a circle; `ctx.arc(0, 0, c.radius, 0, 2+Math.PI); ctx.fill();`
    + restore the context: `ctx.restore();`
  + drawing all balls in an array: `function drawAllBalls(ballArray) { ballArray.forEach(function(b) { drawFilledCircle(b); }); }`
  + moving balls: `function moveAllBalls(ballArray) {...}`
    + iterate all balls in the array: `balls.forEach(function(b, index) {...});`
    + set new position of current balls: `b.x += (b.speedX * globalSpeedMultiplier); b.y += (b.speedY * globalSpeedMultiplier);`
    + detect collisions: `testCollisionBallWithWalls(b); testCollisionWithPlayer(b, index);`
  
+ Example: [draw and move balls w/ methods](src/04d-example01.html)
  + keep class as simple as possible
  + reusability: prevent the class contents to rely on external, global variables
  + declare ball class: `class Ball { constructor(x, y, radius, color, speedX, speedY) { // refer to class Ball() properties } ... }`
  + draw ball in class w/ `this` keyword: `draw(ctx) {...}`
    + save context: `ctx.save();`
    + translate context: `ctx.translate(this.x, this.y);`
    + set context property: `ctx.fillStyle = this.color;`
    + lift pen to start new draw path: `ctx.beginPath();`
    + draw a circle: `ctx.arc(0, 0, this.radius, 0, 2*Math.PI); ctx.fill();`
    + restore context: `ctx.restore();`
  + move ball method: `move() { this.x += this.speedX; this.y += this.speedY; }`
  + missing `globalSpeedMultiplier`: not relevant to each ball but all $\to$ existed event w/o ball $\to$ not a ball property
  + draw all balls: `function drawAllBalls2(ballArray) { ballArray.forEach(function(b) { b.draw(ctx); }); }`
  + move all balls: `function moveAllBalls2(ballArray) {...});`
    + iterate through all balls: `balls.forEach(function(b, index) {...}`
    + move the current ball: `b.move();`
    + detect collision: `testCollisionBallWithWalls(b); testCollisionWithPlayer(b, index);`


### 4.4.3 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Suggested topic

Did you register to [W3C HTML5 Apps and Games MOOC](https://www.edx.org/course/html5-apps-and-games)? There is module about video game programming, and with the knowledge acquired from this JS intro MOOC, you should have no problem following it.

It uses JavaScript object oriented programming and shows many examples that share the concepts seen during the first 4 modules of this course.


#### Optional projects

+ Try to use ES6 classes as much as you can.
+ Split the project into files!
  + Try to make a local version on your hard disk and try to split the game into files such as main.js, listeners.js, balls.js, player.js, sound.js, score.js, etc.
  + Did you manage to use the multiple image loader from Module 2? Try again, ask for help in the discussion forum proposed below!<br> Try to replace the balls by images, use nice graphics, etc.





