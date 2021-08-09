# Module 2: Game programming with HTML5 section


## 2.7 Game states


### 2.7.1 Menus, high score tables, etc.


#### Properties of player and enemy objects

With our game framework handling the basics, we can make things more exciting by causing something to happen when a collision occurs - maybe the player 'dies', balls are removed, or we should add to your score? Usually, we add extra properties to the player and enemy objects. For example, a boolean `dead` property that will record if an object is dead or alive: if a ball is marked "dead", do not draw it! If all balls are dead: go to the next level with more balls, faster balls, etc.

Let's try adding a `dead` property to balls and consult it before drawing them. We could also test to see if all the balls are dead, in which case we recreate them and add one more ball. Let's update the score whenever the monster eats a ball. And finally, we should add a test in the `createBalls` function to ensure that no balls are created on top of the monster.

[Try this jsBin!](https://jsbin.com/jixolu/edit?js,console,output)

[Local Demo](src/02g-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick= "window.open('https://bit.ly/3xRoIXS')"
    src    = "https://bit.ly/3j69VV0"
    alt    = "Eat the ball game"
    title  = "Eat the ball game"
  />
</figure>


Source code extract:

<div><ol>
<li value="1">function updateBalls(delta) {</li>
<li>&nbsp; &nbsp;<strong style="color: red;">// for each ball in the array</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;var allBallDead = true;</strong></li>
<li> </li>
<li>&nbsp; &nbsp;for(var i=0; i &lt; ballArray.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;var ball = ballArray[i];</li>
<li> </li>
<li>&nbsp; &nbsp; <strong style="color: red;">&nbsp;</strong><strong style="color: red;">if(ball.dead) continue; // do nothing if the ball is dead</strong></li>
<li> </li>
<li>&nbsp; &nbsp; <strong style="color: red;">&nbsp;</strong><strong style="color: red;">// if we are here: the ball is not dead</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;allBallDead = false;</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// 1) move the ball</li>
<li>&nbsp; &nbsp; &nbsp;ball.move(); </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// 2) test if the ball collides with a wall</li>
<li>&nbsp; &nbsp; &nbsp;testCollisionWithWalls(ball);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;// Test if the monster collides</li>
<li>&nbsp; &nbsp; &nbsp;if(circRectsOverlap(monster.x, monster.y, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monster.width, monster.height, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ball.x, ball.y, ball.radius)) {</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;//change the color of the ball</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ball.color = 'red';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong style="color: red;">ball</strong><strong style="color: red;">.dead = true;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Here, a sound effect would greatly improve</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// the experience!</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;"> currentScore</strong><strong style="color: red;">+= 1;</strong></li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// 3) draw the ball</li>
<li>&nbsp; &nbsp; &nbsp;ball.draw();</li>
<li>&nbsp;&nbsp;}</li>
<li value="1">&nbsp;<strong style="color: red;"> if</strong><strong style="color: red;">(allBallDead) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;// reset all balls, create more balls each time</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;//&nbsp;as a way&nbsp;of increasing the difficulty</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;// in a real game: change the level, play nice music!</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;nbBalls++;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;createBalls(nbBalls);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;}</strong></li>
<li>}</li>
</ol></div><br>


#### Game states: menus, high score tables, etc.

In this example, let's make use of a global `gameState` variable for managing the life-cycle of the game. Usually, there is a main menu with a "start new game" option, then we play the game, and if we 'die' we suffer a game-over screen, etc...

Ah!... you think that the game has been too easy? Let's reverse the game: now you must survive without being touched by a ball!!!

Also, every five seconds a next level will start: the set of balls is re-created, and each level has two more than before. How long can you survive?

Try this JsBin, then look at the source code. Start from the `mainloop`!

`currentGameState = gameStates.gameOver` & `currentGameState = gameStates.gamerunning`:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3xRoIXS" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/35WQ2aV"
      alt   = "Game Over Screen, asking to press space to start again"
      title = "Game Over Screen, asking to press space to start again"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3gRbkxa"
      alt   = "game running, showing score, time, level"
      title = "game running, showing score, time, level"
    >
  </a>
</div>


Game state management in the JavaScript code:

<div><ol>
<li value="1"> ...</li>
<li> // game states</li>
<li> var gameStates = {</li>
<li>&nbsp; &nbsp;mainMenu: 0,</li>
<li>&nbsp; &nbsp;gameRunning: 1,</li>
<li>&nbsp; &nbsp;gameOver: 2</li>
<li> };</li>
<li>&nbsp;</li>
<li> var currentGameState = gameStates.gameRunning;</li>
<li> var currentLevel = 1;</li>
<li> var TIME_BETWEEN_LEVELS = 5000; // 5 seconds</li>
<li> var currentLevelTime = TIME_BETWEEN_LEVELS;</li>
<li>...</li>
<li> var mainLoop = function (time) {</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;// number of ms since last frame draw</li>
<li>&nbsp; &nbsp;delta = timer(time);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// Clear the canvas</li>
<li>&nbsp; &nbsp;clearCanvas();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// monster.dead is set to true in updateBalls when there</li>
<li>&nbsp; &nbsp;// is a collision</li>
<li>&nbsp; &nbsp;<strong style="color: red;">if (monster.dead) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; currentGameState = gameStates.gameOver;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;}</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;<strong style="color: red;">switch (currentGameState) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;case gameStates.gameRunning:</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// draw the monster</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; drawMyMonster(monster.x, monster.y);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Check inputs and move the monster</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; updateMonsterPosition(delta);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// update and draw balls</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; updateBalls(delta);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// display Score</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; displayScore();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// decrease currentLevelTime. Survive 5s per level</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// When &lt; 0 go to next level</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;currentLevelTime -= delta;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if (currentLevelTime &lt; 0) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; goToNextLevel();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;break;</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">case gameStates.mainMenu:</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// TO DO! We could have a main menu with high scores etc.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;break;</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">case gameStates.gameOver:</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx.fillText("GAME OVER", 50, 100);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx.fillText("Press SPACE to start again", 50, 150);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx.fillText("Move with arrow keys", 50, 200);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx.fillText("Survive 5 seconds for next level", 50, 250);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if (inputStates.space) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; startNewGame();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;break;</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;};</li>
<li>...&nbsp;</li>
</ol></div><br>

And below are the functions for starting a new level, starting a new game, and the `updateBalls` function that determines when a player loses and changes the current game-state to GameOver:

<div><ol>
<li value="1"> function startNewGame() {</li>
<li>&nbsp; &nbsp; monster.dead = false;</li>
<li>&nbsp; &nbsp; currentLevelTime = 5000;</li>
<li>&nbsp; &nbsp; currentLevel = 1;</li>
<li>&nbsp; &nbsp; nbBalls = 5;</li>
<li>&nbsp; &nbsp; createBalls(nbBalls);</li>
<li>&nbsp; &nbsp; <strong style="color: red;">currentGameState </strong><strong style="color: red;">= gameStates.gameRunning;</strong></li>
<li> }</li>
<li>&nbsp;</li>
<li> function goToNextLevel() {</li>
<li>&nbsp; &nbsp;&nbsp;// reset time available for next level</li>
<li>&nbsp; &nbsp;&nbsp;// 5 seconds in this example</li>
<li>&nbsp; &nbsp;currentLevelTime = 5000;</li>
<li>&nbsp; &nbsp;currentLevel++;</li>
<li>&nbsp; &nbsp;// Add two balls per level</li>
<li>&nbsp; &nbsp;nbBalls += 2;</li>
<li>&nbsp; &nbsp;createBalls(nbBalls);</li>
<li> }</li>
<li>&nbsp;</li>
<li> function updateBalls(delta) {</li>
<li>&nbsp; &nbsp;&nbsp;// Move and draw each ball, test collisions, </li>
<li>&nbsp; &nbsp;&nbsp;for (var i = 0; i &lt; ballArray.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Test if the monster collides</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if (circRectsOverlap(monster.x, monster.y,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; monster.width, monster.height,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ball.x, ball.y, ball.radius)) {</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;//change the color of the ball</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ball.color = 'red';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong style="color: red;">&nbsp;monster</strong><strong style="color: red;">.dead = true;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Here, a sound effect greatly improves</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// the experience!</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;plopSound.play();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// 3) draw the ball</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ball.draw();</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li> }</li>
</ol></div>


#### Notes for 2.7.1 Menus, high score tables, etc.

+ Example: properties for balls
  + tasks:
    + adding a `dead` property to balls and check before drawing
    + display score and update it as monster eats ball
    + add a test to ensure no balls created on top of monster
  + update ball position: `function updateBalls(delta) {...}`
    + declare variable: `var allBallDead = true;`
    + iterate through all balls: `for (var i=0; i<ballArray.length; i++) {...}`
      + declare ball: `var ball = ballArray[i];`
      + check existence of ball: `if (ball.dead) continue;`
      + set ball existed: `allBallDead = false;`
      + set ball position: `ball.move();`
      + test collision w/ walls: `textCollisionWithWalls(ball);`
      + test collision w/ monster: `if (circRectOverlap(monster.x, monster.y, monster.with, monster.height, ball.x, ball.y)) { ball.color = 'red'; ball.dead = true; currentScore += 1; }`
      + draw ball: `ball.draw();`
    + reset to create balls: `if (allBallDead) { nbBalls++; createBalls(nbBalls); }`

+ Example: game states
  + tasks
    + using a global `gameState` variable for managing the life cycle of the game
    + start next level game for 5 seconds
  + declare game state: `var gameStates = { mainMenu: 0, gameRunning: 1, gameOver: 2 };`
  + init variable values: `var currentGameState = gameStates.gameRunning; var currentLevel = 1; var TIME_BETWEEN_LEVELS = 5000; var currentLevelTime = TIME_BETWEEN_LEVELS;`
  + generate animation loop: `var mainLoop = function (time) {...};`
    + ...
    + get time difference btw frames: `delta = timer(time);`
    + clear the canvas: `clearCanvas();`
    + check monster existence: `if (monster.dead) { currentGameState = gameStates.gameOver; }`
    + select current game state: `switch (currentGameState) {...}`
      + case for game running: `case gameStates.gameRunning:`
        + draw monster: `drawMyMonster(monster.x, monster.y);`
        + call to update monster position: `updateMonsterPosition(delta);`
        + call to update ball positions: `updateBalls(delta);`
        + call to display score: `displayScore();`
        + decrease current level time remain: `currentLevelTime -= delta;`
        + check next level: `if (currentLevelTime < 0) { goToNextLevel(); }`
        + exit case: `break;`
      + case for displaying main menu: `case gameState.mainMenu:`
        + display menu for game
        + exit case: `break;`
      + case for game over: `case gameStates.gameOver:`
        + display game instruction: `ctx.fillText("GAME OVER", 50, 100); ctx.fillText("Press SPACE to start again", 50, 150); ctx.fillText("Move with arrow keys", 50, 200); ctx.fillText("Survive 5 seconds for next level", 50, 250);`
        + check to start new game: `if (inputStates.space) { startNewGame(); }`
        + exit case: `break;`
  + start new game: `function startNewGame() {...}`
    + set values for variables: `monster.dead = false; currentLevelTime = 5000; currentLevel = 1; nbBalls = 5;`
    + call to create balls: `createBalls(nbBalls);`
    + set game state: `currentGameState = gameStates.gameRunning;`
  + move to next level: `function goToNextLevel() {...}`
    + set values for variables: `currentLevelTime = 5000; currentLevel++; nbBalls += 2;`
    + call to create balls: `createBalls(nbBalls);`
  + update balls in game: `function updateBalls(delta) {...}`
    + iterate to move all balls: `for (var i=0; i<ballArray.length; i++) {...}`
    + ...
    + test collision w/ monster: `if (circRectOverlap(monster.x, monster.y, monster.width, monster.height, ball.x, ball.y, ball.radius)) { ball.color = 'red'; monster.dead = true; plopSound.play(); }`
    + draw ball: `ball.draw;`


### 2.7.2 Splitting the game into several JS files

JSBin is a great tool for sharing code, for experimenting, etc. But as soon as the size of your project increases, you'll find that the tool is not suited for developing large systems. 

In order to keep working on this game framework, we recommend that you modularize the project and split the JavaScript code into several JavaScript files:

+ Review the different functions and isolate those that have no dependence on the framework. Obviously, the sprite utility functions, the collision detection functions, and the ball constructor function can be separated from the game framework, and could easily be reused in other projects. Key and mouse listeners also can be isolated, gamepad code too...
+ Look at what you could change to reduce dependencies: add a parameter in order to make a function independent from global variables, for example.
+ In the end, try to limit the `game.js` file to the core of the game framework (`init` function, `mainloop`, game states, score, levels), and separate the rest into functional groupings, eg `utils.js`, `sprites.js`, `collision.js`, `listeners.js`, etc.

Let's do this together!


#### Start with a simple structure

First, create a `game.html` file that contains the actual HTML code:

`game.html`:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Nearly a real game&lt;/title&gt;</li>
<li>&nbsp;<strong style="color: red;">&lt;!-- External JS libs --&gt;</strong></li>
<li> &lt;script src="https://cdnjs.cloudflare.com/ajax/libs/howler/1.1.25/howler.min.js"&gt;&lt;/script&gt;</li>
<li><span style="color: #008888;" color="#008888">&nbsp;<strong style="color: red;">&lt;!-- CSS files for your game --&gt;</strong></span></li>
<li><span style="color: #008888;" color="#008888">&nbsp;&lt;link rel="stylesheet" href="css/game.css"&gt;</span></li>
<li><strong style="color: red;"> &lt;!-- Include here all game JS files--&gt;</strong></li>
<li><strong style="color: red;">&nbsp;&lt;script src="js/game.js"&gt;&lt;/script&gt;</strong></li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;canvas id="myCanvas" width="400" height="400"&gt;&lt;/canvas&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

Here is the `game.css` file (very simple):

<div><ol>
<li value="1">canvas {</li>
<li>&nbsp; &nbsp;border: 1px solid black;</li>
<li>}</li>
</ol></div><br>

Let's take the JavaScript code from the last JSBin example, save it to a file called `game.js`, and locate it in a subdirectory `js` under the directory where the `game.html` file is located. Similarly, we'll keep the CSS file in a `css` subdirectory:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3vTlXUn"
    alt    = "first game structure"
    title  = "first game structure"
  />
</figure>


Try the game: open the `game.html` file in your browser. If the game does not work, open devtools, look at the console, fix the errors, try again, etc. You may have to do this several times when you split your files and encounter errors.


#### Isolate the ball function constructor

Put the Ball constructor function in a js/ball.js file, include it in the `game.html` file, and try the game: oops, it doesn't work! Let's open the console:

`Ball.js`:

<div><ol>
<li value="1">// constructor function for balls</li>
<li> function Ball(x, y, angle, v, diameter) {</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;this.draw = function () {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">ctx</strong>.save();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp; };</li>
<li>&nbsp; &nbsp;&nbsp;this.move = function () {</li>
<li>&nbsp; &nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;this.x +=<strong style="color: red;"> calcDistanceToMove</strong>(delta, incX);</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;this.y +=<strong style="color: red;"> calcDistanceToMove</strong>(delta, incY);</li>
<li>&nbsp; &nbsp;&nbsp;};</li>
<li> }</li>
</ol></div><br>


#### Isolate the time based animation functions into a separate file

Hmmm... the `calcDistanceToMove` function is used here, but is defined in the `game.js` file, inside the `GF` object and will certainly raise an error... Also, the `ctx` variable should be added as a parameter to the `draw` method, otherwise it won't be recognized... 

Just for fun, let's try the game without fixing this, and look at the devtools console:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3xSIsdC"
    alt    = "error the function calcDistToMove not found in ball.js"
    title  = "error the function calcDistToMove not found in ball.js"
  />
</figure>


Aha! The `calcDistanceToMove` function is indeed used by the Ball constructor in `ball.js` at _line 27_ (it moves the ball using time-based animation). If you look carefully, you will see that it's also used for moving the monster, etc. In fact, there are parts in the game framework related to time-based animation. Let's move them all into a `timeBasedAnim.js` file!!

Fix: extract the utility functions related to time-based animation and add a _ctx_ parameter to the draw method of `ball.js`. Don't forget to add it in `game.js` where `ball.draw()` is called. The call should be now `ball.draw(ctx);` instead of `ball.draw()` without any parameter.

`timeBasedAnim.js`:

<div><ol>
<li value="1">var delta, oldTime = 0;</li>
<li>&nbsp;</li>
<li>function timer(currentTime) {</li>
<li>&nbsp; &nbsp;var delta = currentTime - oldTime;</li>
<li>&nbsp; &nbsp;oldTime = currentTime;</li>
<li>&nbsp; &nbsp;return delta;</li>
<li>}</li>
<li>&nbsp;</li>
<li>var calcDistanceToMove = function (delta, speed) {</li>
<li>&nbsp; &nbsp;//console.log("#delta = " + delta + " speed = " + speed);</li>
<li>&nbsp; &nbsp;return (speed * delta) / 1000;</li>
<li> };</li>
</ol></div><br>


#### Isolate the part that counts the number of frames per second

We need to add a small `initFPS` function for creating the `<div>` that displays the FPS value... this function will be called from the `GF.start()` method. There was code in this `start` method that has been moved into the `initFPS` function we created and added into the `fps.js` file.

`fps.js`:

<div><ol>
<li value="1"> // vars for counting frames/s, used by the measureFPS function</li>
<li> var frameCount = 0;</li>
<li> var lastTime;</li>
<li> var fpsContainer;</li>
<li> var fps;</li>
<li>&nbsp;</li>
<li> var initFPSCounter = function() {</li>
<li>&nbsp; &nbsp;// adds a div for displaying the fps value</li>
<li>&nbsp; &nbsp;fpsContainer = document.createElement('div');</li>
<li>&nbsp; &nbsp;document.body.appendChild(fpsContainer);</li>
<li> }</li>
<li> </li>
<li> var measureFPS = function (newTime) {</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// test for the very first invocation</li>
<li>&nbsp; &nbsp;if (lastTime === undefined) {</li>
<li>&nbsp; &nbsp; &nbsp; lastTime = newTime;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;return;</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;//calculate the difference between last &amp; current frame</li>
<li>&nbsp; &nbsp;var diffTime = newTime - lastTime;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;if (diffTime &gt;= 1000) {</li>
<li>&nbsp; &nbsp; &nbsp; fps = frameCount;</li>
<li>&nbsp; &nbsp; &nbsp; frameCount = 0;</li>
<li>&nbsp; &nbsp; &nbsp; lastTime = newTime;</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;//and display it in an element we appended to the </li>
<li>&nbsp; &nbsp;// document in the start() function</li>
<li>&nbsp; &nbsp;fpsContainer.innerHTML = 'FPS: ' + fps;</li>
<li>&nbsp; &nbsp;frameCount++;</li>
<li> };</li>
</ol></div><br>

At this stage, the structure looks like this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3jcRPAM"
    alt    = "Game structure"
    title  = "Game structure"
  />
</figure>



#### Let's continue and isolate the event listeners

Now, consider the code that creates the listeners, can we move it from the `GF.start()` method into a `listeners.js` file? We'll have to pass the canvas as an extra parameter (to resolve a dependency) and we also move the `getMousePos` method into there. 

`listeners.js`:

<div><ol>
<li value="1">function addListeners(inputStates,<strong style="color: red;"> canvas</strong>) {</li>
<li>&nbsp; &nbsp;//add the listener to the main, window object, and update the states</li>
<li>&nbsp; &nbsp;window.addEventListener('keydown', function (event) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if (event.keyCode === 37) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;inputStates.left = true;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 38) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;inputStates.up = true;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}&nbsp;...</li>
<li>&nbsp; &nbsp;}, false);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;//if the key&nbsp;is released, change the states object </li>
<li>&nbsp; &nbsp;window.addEventListener('keyup', function (event) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;}, false);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// Mouse event listeners</li>
<li>&nbsp; &nbsp;canvas.addEventListener('mousemove', function (evt) {</li>
<li>&nbsp; &nbsp; &nbsp; inputStates.mousePos =<strong style="color: red;"> getMousePos(evt, canvas);</strong></li>
<li>&nbsp; &nbsp;}, false);</li>
<li>...</li>
<li>}</li>
<li>&nbsp;</li>
<li>function getMousePos(evt,<strong style="color: red;"> canvas</strong>) {</li>
<li>&nbsp; &nbsp;...</li>
<li>}</li>
</ol></div><br>


#### Isolate the collision tests

Following the same idea, let's put these into a `collisions.js` file:

<div><ol>
<li value="1"> // We can add the other collision functions seen in the</li>
<li> // course here...</li>
<li> </li>
<li> // Collisions between rectangle and circle</li>
<li> function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {</li>
<li>&nbsp; &nbsp;...</li>
<li> }</li>
<li>&nbsp;</li>
<li> function testCollisionWithWalls(ball,<strong style="color: red;"> w, h</strong>) {</li>
<li>&nbsp; &nbsp;...</li>
<li> }</li>
</ol></div><br>

We added the width and height of the canvas as parameters to the testCollisionWithWalls function to resolve dependencies. The other collision functions (circle-circle and rectangle-rectangle) presented during the course, could be put into this file as well.


#### Final downloadable version and conclusion

After all that, we reach this tidy structure:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3h7oqVI')"
    src    = "https://bit.ly/3x8fK8k"
    alt    = "final game structure in files"
    title  = "final game structure in files"
  />
</figure>


Final `game.html` file:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Nearly a real game&lt;/title&gt;</li>
<li> <strong style="color: red;">&lt;link rel="stylesheet" href="css/game.css"&gt;</strong></li>
<li> &lt;script src="https://cdnjs.cloudflare.com/ajax/libs/howler/1.1.25/howler.min.js"&gt;&lt;/script&gt;</li>
<li> &lt;!-- Include here all JS files --&gt;</li>
<li> <strong style="color: red;">&lt;script src="js/game.js"&gt;&lt;/script&gt;</strong></li>
<li><strong style="color: red;"> &lt;script src="js/ball.js"&gt;&lt;/script&gt;</strong></li>
<li><strong style="color: red;"> &lt;script src="js/timeBasedAnim.js"&gt;&lt;/script&gt;</strong></li>
<li><strong style="color: red;"> &lt;script src="js/fps.js"&gt;&lt;/script&gt;</strong></li>
<li><strong style="color: red;"> &lt;script src="js/listeners.js"&gt;&lt;/script&gt;</strong></li>
<li><strong style="color: red;"> &lt;script src="js/collisions.js"&gt;&lt;/script&gt;</strong></li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;canvas id="myCanvas" width="400" height="400"&gt;&lt;/canvas&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

We could go further by defining a `monster.js` file, turning all the code related to the monster/player into a well-formed object, with draw and move methods, etc. There are many potential improvements you could make. JavaScript experts are welcome to make a much fancier version of this little game :-)

[Download the zip](https://bit.ly/3xIZGKm) for this version, just open the game.html file in your browser!

[Local Demo](src/02f-gameForMooc/game.html)

Our intent this week was to show you the primary techniques/approaches for dealing with animation, interactions, collisions, managing with game states, etc. 

The quizzes for this week are not so important. _We're keen to see you write your own game!_ You are welcome to freely re-use the examples presented in the lessons and modify them, improve the code structure, playability, add sounds, better graphics, more levels, etc. We like to give points for style and flair, but most especially because we've been (pleasantly) surprised!


#### Notes for 2.7.2 Splitting the game into several JS files

+ Modulizing game project
  + review and isolate functions
    + grouping functions w/o dependence on the framework
    + typical functions reused in other project
      + sprite utility functions
      + collision detection functions
      + ball constructor functions
    + typical interactive functions
      + key and mouse listeners
      + gamepad code
      + ...
  + reduce dependencies:
    + change code to reduce dependencies
    + example: add a parameter to make a function independent from global variables
  + limit main JavaScript to certain function
    + `game.js` as the core of the game framework: `init` function, `mainloop` function, game states, score, levels
    + other functional groupings: `utils.js`, `sprites.js`, `collisions.js`, `listeners.js`

+ Possible procedure of game development
  + start w/ a simple structure: `game.html` and `game.css`
  + isolate ball function constructor: `ball.js`
  + isolate time-based animation functions in a separate file: `timeBaseAnim.js`
  + isolate the part counting the number of frames per second: `fps.js`
  + isolate the event listeners: `listeners.js`
  + isolate the collision tests: `collisions.js`

+ A simple structure
  + HTML snippet `game.html`<a name="simpleGame"></a>:
    + head part: `<head> ... </head>`
      + sound script: `<script src="https://cdnjs.cloudflare.com/.../howler.min.js"></script>`
      + css style: `<link rel="stylesheet" href="css/game.css">`
      + game script: `<script src="js/game.js"></script>`
    + body part: `<canvas id="myCanvas" width=200 height=200></canvas>`
  + CSS style `game.css`: `canvas { border: 1px solid black; }`

+ Ball function constructor, `ball.js`
  + ball constructor: `function Ball(x, y, angle, v, diameter) {...}`
    + ...
    + draw method: `this.draw = function() { ctx.save; ... };`
    + move method: `this.move = function() { ... this.x += calDistanceToMove(delta, incX); this.y += calcDistanceToMove(delta, incY); };`
  + `calcDistanceToMove` used here but declared in `game.js` within `GF` object
  + `ctx` variable missing $\to$ added as a parameter to the `draw` method

+ Time-based animation, `timeBasedAnim,js`
  + `calcDistanceToMove` function used by the Ball constructor and moving the monster etc.
  + extract the utility functions related to time-based animation
  + add `ctx` parameter to the `draw` method of `ball.js`
  + delcare variables: `var delta, oldTime = 0;`
  + calculate time difference btw frames: `function timer(currentTime) {...}`
    + set time difference: `var delta = currentTime - oldTime;`
    + update old time: `oldTime = currentTime;`
    + return the time difference: `return delta;`
  + calculate distance: `var calcDistanceToMove = function (delta, speed) { return (speed*delta) / 1000; };`

+ Count the number of frames per second, `fps.js`
  + add a small `initFPS` function for creating the `<div>` to display the FPS value
  + call `initFPS` from `GF.start()` method
  + code in `start` method moved into the `initFPS` function and added into the `fps.js`
  + declare variables: `var fameCount = 0; var lastTime; var fpsContainer; var fps;`
  + init PFS count: `var initFPSCount = function() {...}`
    + create fps container: `fpsContainer = document.createElement('div');`
    + add container into page: `document.body.appendChild(fpsContainer);`
  + measure FPS: `var measureFPS = function(newTime) {...}`
    + test for the first invocation: `if (lastTime === undefined) { lastTime = newTime; return; }`
    + calculate time difference btw the last and current frames: `var diffTime = newTime - lastTime;`
    + check time difference greater than 1 second: `if (diffTime < 1000) { fps = frameCount; frameCount = 0; lastTime = newTime; }`
  + display fps info: `fpsContainer.innerHTML = 'FPS: ' + fps; frameCount++;`

+ Handling event listeners, `listeners.js`
  + add listenters for input states: `function addListeners(inputStates, canvas) {...}`
    + add key down listeners: `window.addEventListener('keydown', function(event) {...}, false);`
      + check left arrow key down: `if (event.keyCode === 37) { inputStates.left = true; }`
      + check right arrow key up: `else if (event.keyCode === 38) { inputStates.up = true; }`
      + ...
    + add key up listeners: `window.addEventListener('keyup', function(event) {...}, false);`
    + add mouse event listener: `canvas.addEventListener('mouseover', function(evt) {inputStates.mousePos = getMousePos(evt, canvas)}; false);`
    + ...
  + calculate mouse position: `function getMousePos(evt, canvas) {...}`

+ Collision detection, `collisions.js`
  + detection collision btw rectangle and circle: `function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {...}`
  + detection collision w/ walls: `function testCollisionWithWalls(ball, w, h) {...}`

+ Final version of game fraework
  + HTML [simple structure](#simpleGame)
  + additional links for JS files
    + link JS file for ball function constructor: `<script src="js/ball.js"></script>`
    + link JS file for time-based animation functions in a separate file: `<script src="js/timeBaseAnim.js"></script>`
    + link JS file for the part counting the number of frames per second: `<script src="js/fps.js"></script>`
    + link JS file for the event listeners: `<script src="js/listeners.js"></script>`
    + link JS file for the collision tests: `<script src="js/collisions.js"></script>`


### 2.7.3 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Suggested topics of discussion:

+ What additional content would you like to see in this part of the course?
+ Did you notice we gave you (without saying) a small particle engine during Week 1? This is very useful for simulating explosions or bullet impacts...


#### Optional projects: create your own game!

Try to make your own game, either by modifying/completing the given example (change the scenario, add levels, colors, sound effects, sprites, shots, etc.) or by writing your own using the methods explained in the course.

To inspire you, here are some examples written by Michel's students. Some of them are based on the framework presented in the course.

+ [The Wanted](https://output.jsbin.com/cuwuso/): escape the Police and steal as many gold coins as you can! This game did not really follow the game framework presented in the course, but the final game is fun and is an interesting variation on examples presented in the course.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/3dgiYPo" ismap target="_blank">
      <img style="margin: 0.1em;" height=150
        src   = "https://bit.ly/3wZZjuO"
        alt   = "Main screen of the game called Wanted"
        title = "Main screen of the game called Wanted"
      >
      <img style="margin: 0.1em;" height=150
        src   = "https://bit.ly/3dgC0oS"
        alt   = "The game running, monster with black bombs and gold coins"
        title = "The game running, monster with black bombs and gold coins"
      >
    </a>
  </div>

+ Duck Hunt (by Benjamin Reale and Anthony Caron). Get [the whole game](https://github.com/Ben06/ASCI-CARON-REALE-Duck-Hunt/) at this GitHub link + just grab the sprite sheet and sounds in this [archive](https://bit.ly/3xPI4MI) and try to make the game yourself (500k). This one started with the game framework presented in the course.

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://bit.ly/3dgiYPo')"
      src    = "https://bit.ly/3vWYyS3"
      alt    = "Screenshot of the Duck hunt game"
      title  = "Screenshot of the Duck hunt game"
    />
  </figure>

+ Shoot em up (by Max Chazarra) ([sources](https://bit.ly/3gYbqTS) on the GitHub site). This one started with the game framework presented in the course:

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://bit.ly/3dgiYPo')"
      src    = "https://bit.ly/3jh7b75"
      alt    = "Screenshot of the shoot em up game"
      title  = "Screenshot of the shoot em up game"
    />
  </figure>

+ Gameboy Tetris (written starting from the game framework presented in the course). [Download the sources](https://bit.ly/3dfiqJM) (author Maxime Demetrio)

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://bit.ly/3dgiYPo')"
      src    = "https://bit.ly/2U62vXq"
      alt    = "gameboy tetris in html5"
      title  = "gameboy tetris in html5"
    />
  </figure>

+ A small "kill the ninjas" game (by Tristan Poilvet). This game used the game framework presented in the course as a starting point. [Sources](https://bit.ly/3w7cSHT) available here.

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick= "window.open('https://bit.ly/3dgiYPo')"
      src    = "https://bit.ly/3jh7per"
      alt    = "a 'kill the ninja game'"
      title  = "a 'kill the ninja game'"
    />
  </figure>





