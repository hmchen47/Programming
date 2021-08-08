# Module 2: Game programming with HTML5 section


## 2.3 A simple game framework


### 2.3.1 A game framework skeleton

We are going to develop a game - not all at once, let's divide the whole job into a series of smaller tasks. The first step is to create a foundation or basic structure.

Let's start by building the skeleton of a small game framework, based on [the Black Box Driven Development in JavaScript](https://hacks.mozilla.org/2014/08/black-box-driven-development-in-javascript/) methodology. In other words: a game framework skeleton is a simple object-based model that uses encapsulation to expose only useful methods and properties.

We will evolve this framework throughout the lessons in this course, and cut it in different files once it becomes too large to fit within one single file.

Here is the starting point:

<div><ol>
<li value="1">var GF = function(){</li>
<li> </li>
<li>&nbsp;&nbsp;var mainLoop = function(time){</li>
<li>&nbsp; &nbsp;&nbsp;//Main function, called each frame</li>
<li>&nbsp; &nbsp; requestAnimationFrame(mainLoop);</li>
<li>&nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp;&nbsp;var start = function(){</li>
<li>&nbsp; &nbsp; requestAnimationFrame(mainLoop);</li>
<li>&nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp;&nbsp;// Our GameFramework returns a public API visible from outside its scope</li>
<li>&nbsp; // Here we only expose the start method, under the "start" property name.</li>
<li>&nbsp;&nbsp;<strong style="color: red;">return {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; start: start</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;};</strong></li>
<li>};</li>
</ol></div><br>

With this skeleton, it's very easy to create a new game instance:

<div><ol>
<li value="1">var game = new GF();</li>
<li> </li>
<li>// Launch the game, start the animation loop, etc.</li>
<li><strong style="color: red;">game.start();</strong></li>
</ol></div>


#### Examples

__Let's put something into the mainLoop function, and check if it works__

Try this [online example at JSBin](https://jsbin.com/tatowa/edit), with a new `mainloop`:  (check the JavaScript and output tabs). This page should display a different random number every 1/60 second. We don't have a real game yet, but we're improving our game engine :-)

[Local Demo](src/02b-example04.html)

Source code extract:

<div><ol>
<li value="1">var mainLoop = function(time){</li>
<li>&nbsp;&nbsp;// main function, called each frame</li>
<li>&nbsp; document.body.innerHTML = Math.random();</li>
<li> </li>
<li>&nbsp;&nbsp;// call the animation loop every 1/60th of second</li>
<li>&nbsp; requestAnimationFrame(mainLoop);</li>
<li>};</li>
</ol></div><br>


__Let's measure that animation's frame rate__

Every game needs to have a function which measures the actual frame rate achieved by the code.

The principle is simple:

1. Count the time elapsed by adding deltas in the `mainloop`.
2. If the sum of the deltas is greater or equal to 1000, then 1s has elapsed since we started counting.
3. If at the same time, we count the number of _frames_ that have been drawn, then we have the _frame rate_ - measured in number of frames per second. Remember, it should be around 60 fps!

__Quick glossary:__ the word delta is the name of a Greek letter (uppercase Δ, lowercase δ or 𝛿). The upper-case version is used in mathematics as an abbreviation for measuring the change in some object, over time - in our case, how quickly the mainloop is running. This dictates the maximum speed at which the game display will be updated. This maximum speed could be referred to as the _rate of change_. We call what is displayed at a single point-in-time, a frame. Thus the _rate of change_  can be measured in frames per second (fps). Accordingly, our game's delta, determines the achievable frame rate - the __shorter__ the delta (measured in mS), the __faster__ the possible _rate of change_ (in _fps_).

Here is a screenshot of an example and the code we added to our game engine, for measuring FPS (try it [online at JSBin](https://jsbin.com/noqibu/edit)):

[Local Demo](src/02b-example05.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xuD14p')"
    src    = "https://bit.ly/3q2qd2v"
    alt    = "screenshot of the example that displays 60 frames/s"
    title  = "screenshot of the example that displays 60 frames/s"
  />
</figure>


Source code extract:

<div><ol>
<li value="1">&nbsp;&nbsp; // vars for counting frames/s, used by the measureFPS function</li>
<li> var frameCount = 0;</li>
<li> var lastTime;</li>
<li> var fpsContainer;</li>
<li> var fps; </li>
<li> </li>
<li> var measureFPS = function(newTime){</li>
<li> </li>
<li>&nbsp; &nbsp;// test for the very first invocation</li>
<li>&nbsp; &nbsp;if(lastTime === undefined) {</li>
<li>&nbsp; &nbsp; &nbsp;lastTime = newTime; </li>
<li>&nbsp; &nbsp; &nbsp;return;</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;// calculate the delta&nbsp;between last &amp; current frame</li>
<li>&nbsp; &nbsp;var diffTime = newTime - lastTime; </li>
<li> </li>
<li>&nbsp; &nbsp;if (diffTime &gt;= 1000) {</li>
<li>&nbsp; &nbsp; &nbsp;fps = frameCount; </li>
<li>&nbsp; &nbsp; &nbsp;frameCount = 0;</li>
<li>&nbsp; &nbsp; &nbsp;lastTime = newTime;</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;// and display it in an element we appended to the </li>
<li>&nbsp; &nbsp;// document in the start() function</li>
<li>&nbsp; &nbsp;fpsContainer.innerHTML = 'FPS: ' + fps; </li>
<li>&nbsp; &nbsp;frameCount++;</li>
<li> };</li>
</ol></div><br>

Now we can call the `measureFPS` function from inside the animation loop, passing it the current time, given by the high resolution timer that comes with the `requestAnimationFrame` API:

<div><ol>
<li value="1">var mainLoop = function(<strong style="color: red;">time</strong>){</li>
<li>&nbsp;&nbsp;//&nbsp;compute FPS,&nbsp;called each frame, uses the high resolution time parameter&nbsp;</li>
<li>&nbsp; //&nbsp;given&nbsp;by the browser that implements the requestAnimationFrame API</li>
<li>&nbsp; <strong style="color: red;">measureFPS</strong><strong style="color: red;">(time);</strong></li>
<li> </li>
<li>&nbsp; // call the animation loop every 1/60th of second</li>
<li>&nbsp; requestAnimationFrame(mainLoop);</li>
<li>};</li>
</ol></div><br>

And the `<div>` element used to display FPS on the screen is created in this example by the `start()` function:

<div><ol>
<li value="1">var start = function(){</li>
<li>&nbsp;&nbsp;<strong style="color: red;">// adds a div for displaying the fps value</strong></li>
<li><strong style="color: red;">&nbsp; fpsContainer = document.createElement('div');</strong></li>
<li><strong style="color: red;">&nbsp; document.body.appendChild(fpsContainer);</strong></li>
<li> </li>
<li>&nbsp; requestAnimationFrame(mainLoop);</li>
<li>};</li>
</ol></div>


__Hack:  achieving more than 60 fPS? It's possible but to be avoided except in hackers' circles!__

We also know methods of implementing loops in JavaScript which achieve even more than 60fps (this is the limit using `requestAnimationFrame`).

My favorite hack uses the onerror callback on an `<img>` element like this:

<div><ol>
<li value="1">function&nbsp;mainloop(){</li>
<li>&nbsp;&nbsp;var img = new Image;</li>
<li></li>
<li>&nbsp; img.onerror =&nbsp;<span style="line-height: 23.2727px;">mainloop;</li>
<li>&nbsp; img.src = 'data:image/png,' + Math.random();</li>
<li>}</li>
</ol></div><br>

What we are doing here, is creating a new image on each frame and providing invalid data as a source of the image. The image cannot be displayed properly, so the browser calls the onerror event handler that is the mainloop function itself, and so on.

Funny right? Please try this and check the number of FPS displayed with this [JSBin example](https://jsbin.com/notupe/edit).

[Local Demo](src/02b-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xuD14p')"
    src    = "https://bit.ly/3wtWW3n"
    alt    = "Screenshot of example with 4441 FPS displayed"
    title  = "Screenshot of example with 4441 FPS displayed"
  />
</figure>


Source code extract of this example:

<div><ol>
<li value="1">var mainLoop = function(){</li>
<li>&nbsp;&nbsp;// main function, called each frame </li>
<li> </li>
<li>&nbsp; measureFPS(+(new Date()));</li>
<li> </li>
<li>&nbsp;&nbsp;// call the animation loop every LOTS of seconds using previous hack method</li>
<li>&nbsp;&nbsp;var img = new Image();</li>
<li>&nbsp; img.onerror = mainLoop;</li>
<li>&nbsp; img.src = 'data:image/png,' + Math.random();</li>
<li> };</li>
</ol></div><br>


#### Notes for 2.3.1 A game framework skeleton

+ Game framework skeleton
  + based on the [Black Box Driven Development](https://hacks.mozilla.org/2014/08/black-box-driven-development-in-javascript/)
    + principle 1: modularize everything
    + principle 2: expose only public methods
    + principle 3: use composition over inheritance
  + a simple objected-based model using encapsulation to expose only useful methods and properties
  + cut into several files once becoming too large to fit into one single file
  + game:
    + a state machine
    + states changed depending on user interaction, collisions, or game conditions
    + animation loop referring to current states to make the game respond accordingly

+ Example: game framework starting point
  + generate game framework <a name="gf"></a>: `var GF = function() {...}`
    + create animation loop: `var mainloop = function() { requestAnimationFrame(mainloop); };`
    + init game loop: `var star = function() { requestAnimationFrame(mainloop); };`
    + return a public API<a name="publicAPI"></a>: `return { start: start };`
  + create a new game instance
    + declare game instance: `var game = new GF();`
    + launch game: `game.start();`

+ Example: animation loop of game framework
  + create animation loop: `var mainloop = function(time) {...};`
  + call animation function to display random number in page: `document.body.innerHTML = Math.random();`
  + call animation loop: `requestAnimationFrame(mainloop);`

+ Measuring animation's frame rate
  + every game requiring a function to measure the actual frame rate achieved by the code
  + principle:
    + count the time elapsed by adding deltas in the `mainloop`
    + sum of the deltas $\ge 1000 \implies$ 1s elapsed since starting point
    + meanwhile, count the number of frames drawn $\implies$ meansure frame rate, should be 60 fps
  + delta ($\Delta, \delta$)
    + $\Delta$:
      + used in mathematics as an abbreviation for measuring the change in some object
      + how quickly the mainloop running
      + the maximum speed, rate of change, at which the game display will be updated
      + rate of change able to be measured in frames per second (fps)
    + $\delta$
      + determine the achievable frame rate
      + the shorter the delta (in ms), the faster the possible rate of change (in fps)

+ Example: counting frames/s
  + delcare variables: `var frameCount = 0; var lastTime; var fpsContainer; var fps;`
  + measure FPS<a name="measureFPS"></a>: `var measureFPS = function(newTime) {...}`
    + test and process first invocation: `if (lastTime === undefined) { lastTime = newTime; return; }`
    + calculate the delta btw last & current frame: `var diffTime = newTime - lastTime;`
    + check delta and assign values: `if (diffTime >= 1000) { fps = frameCount; frameCount = 0; lastTime = newTime; }`
    + display info: `fpsContainer.innerHTML = 'FPS: ' + fps;`
    + increase frame count: `frameCount++;`

+ Example: compute FPS in animation loop
  + create animation loop: `var mainloop = function(time) {...}`
  + compute FPS: `measureFPS(time);`
  + call animation loop: `requestAnimationFrame(mainloop);`

+ Example: display FPS
  + initialize the game framework<a name="initGF"></a>: `var start = function() {...}`
  + add div container: `fpsContainer = document.createElement('div');`
  + add div contain to page: `document.body.appendChild(fpsContainer);`
  + init the animation loop: `requestAnimationFrame(mainloop);`

+ Example: image element w/ error callback
  + create animation loop: `function mainloop() {...}`
  + delcare variable: `var img = new image;`
  + assign error callback: `img.onerror = mainloop;`
  + assign image source: `img.src = 'data:image/png,' + Math.random();`

+ Example: check the number of FPS
  + create animation loop: `var mainloop = function() {...}`
  + measure FPS w/ current time: `measureFPS(+(new Date()));`
  + generate new image: `var img = new Image();`
  + handle error: `img.error = mainloop;`
  + assign image source: `img.src = 'data:image/png' + Math.random();`


#### Knowledge check 2.3.1

1. How do we measure the time between two consecutive animations?

  a. We use the parameter passed by the browser to the animation loop. This is a `requestAnimationFrame` API feature.<br>
  a. We use the Date() JavaScript object, that returns the current time.<br>

  Ans: <span style="color: magenta;">a, xb<br/>
  Explanation: When we ask the browser to call the `mainloop` function using `requestAnimationFrame(mainloop)`, a time parameter is passed to the `mainloop` function. It's a high resolution time in ms, that we use to compute deltas. By computing the difference between the current time and the previous time measured during the previous execution of `mainloop`, we can get the elapsed time, with a sub millisecond accuracy.


### 2.3.2 Introducing graphics

[Note: drawing within a canvas is studied in detail during the [W3C HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) course, in module 3.]

Is this really a course about games? Where are the graphics?

Good news! We will add graphics to our game engine in this lesson!  To-date we have talked of "basic concepts"; so without further ado, let's draw something, animate it, and move shapes around the screen :-)

Let's do this by including into our framework the same "monster" we used during the [W3C HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) course.


#### HTML5 canvas basic usage: drawing a monster

How to draw a monster in a canvas: you can try it [online at JSBin](https://jsbin.com/ponaki/edit).

[Local Demo](src/02b-example07.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/2UeN679')"
    src    = "https://bit.ly/3xrMtFt"
    alt    = "Small monster drawn in a canvas"
    title  = "Small monster drawn in a canvas"
  />
</figure>


HTML code (declaration of the canvas):

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp;&lt;title&gt;Draw a monster in a canvas&lt;/title&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &nbsp;<strong style="color: red;">&lt;canvas id="myCanvas" width="200" height="200"&gt;&lt;/canvas&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

The canvas declaration is at _line 8_. Use attributes to give it a `width` and a `height`, but unless you add some CSS properties, you will not see it on the screen because it's transparent!

Let's use CSS to reveal the canvas, for example, add a 1px black border around it:

<div><ol>
<li value="1">canvas {</li>
<li>&nbsp; &nbsp;border: 1px solid black;</li>
<li>}</li>
</ol></div><br>

And here is a reminder of best practices when using the canvas, as described in the HTML5 Part 1 course:

1. Use a function that is called AFTER the page is fully loaded (and the DOM is ready), set a pointer to the canvas node in the DOM.
1. Then, get a 2D graphic context for this canvas (the `context` is an object we will use to draw on the canvas, to set global properties such as color, gradients, patterns and line width).
1. Only then can you can draw something,
1. Do not forget to use global variables for the canvas and context objects. I also recommend keeping the width and height of the canvas somewhere. These might be useful later.
1. For each function that will change the context (color, line width, coordinate system, etc.), start by saving the context, and end by restoring it.

Here is JavaScript code which implements those best practices:

<div><ol>
<li value="1">// useful to have them as global variables</li>
<li>var canvas, <g id="126" data-gr-id="126">ctx</g>, w, h; </li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li>window.onload = function init() {</li>
<li>&nbsp;&nbsp;// Called AFTER the page has been loaded</li>
<li>&nbsp; canvas = document.querySelector("#myCanvas");</li>
<li> </li>
<li>&nbsp;&nbsp;// Often useful</li>
<li>&nbsp; w = canvas.width; </li>
<li>&nbsp; h = canvas.height; </li>
<li> </li>
<li>&nbsp;&nbsp;// Important, we will draw with this object</li>
<li>&nbsp; ctx = canvas.getContext('2d');</li>
<li> </li>
<li>&nbsp;&nbsp;// Ready to go!</li>
<li>&nbsp;&nbsp;// Try to change the parameter values to move</li>
<li>&nbsp;&nbsp;// the monster</li>
<li>&nbsp; drawMyMonster(10, 10);</li>
<li>};</li>
<li>&nbsp;</li>
<li>function drawMyMonster(x, y) {</li>
<li>&nbsp;&nbsp;// Draw a big monster!</li>
<li>&nbsp;&nbsp;// Head</li>
<li> </li>
<li>&nbsp;&nbsp;// BEST practice: save the context, use 2D transformations</li>
<li>&nbsp; ctx.save();</li>
<li> </li>
<li>&nbsp;&nbsp;// Translate the coordinate system, draw relative to it</li>
<li>&nbsp; ctx.translate(x, y);</li>
<li> </li>
<li>&nbsp;&nbsp;// (0, 0) is the top left corner of the monster.</li>
<li>&nbsp; ctx.strokeRect(0, 0, 100, 100);</li>
<li> </li>
<li>&nbsp;&nbsp;// Eyes</li>
<li>&nbsp; ctx.fillRect(20, 20, 10, 10);</li>
<li>&nbsp; ctx.fillRect(65, 20, 10, 10);</li>
<li> </li>
<li>&nbsp;&nbsp;// Nose</li>
<li>&nbsp; ctx.strokeRect(45, 40, 10, 40);</li>
<li> </li>
<li>&nbsp;&nbsp;// Mouth</li>
<li>&nbsp; ctx.strokeRect(35, 84, 30, 10);</li>
<li> </li>
<li>&nbsp;&nbsp;// Teeth</li>
<li>&nbsp; ctx.fillRect(38, 84, 10, 10);</li>
<li>&nbsp; ctx.fillRect(52, 84, 10, 10);</li>
<li> </li>
<li>&nbsp;&nbsp;// BEST practice: restore the context</li>
<li>&nbsp; ctx.restore();</li>
<li>}</li>
</ol></div><br>

In this small example, we used the `context` object to draw a monster using the default color (black) and wireframe and filled modes:

+ `ctx.fillRect(x, y, width, height)`: draws a rectangle whose top left corner is at (x, y) and whose size is specified by the `width` and `height` parameters; and both outlined by, and filled with, the default color.
+ `ctx.strokeRect(x, y, width, height)`: same but in wireframe mode.
+ Note that we use (_line 30_) `ctx.translate(x, y)` to make it easier to move the monster around. So, all the drawing instructions are coded as if the monster was in (0, 0), at the top left corner of the canvas (look at line 33). We draw the body outline with a rectangle starting from (0, 0). Calling `context.translate` "changes the coordinate system" by moving the "old (0, 0)" to (x, y) and keeping other coordinates in the same position relative to the origin.
+ _Line 19_: we call the `drawMonster` function with (10, 10) as parameters, which will cause the original coordinate system to be translated by (10, 10).
+ And if we change the coordinate system (this is what the call to `ctx.translate(...)` does) in a function, it is a best practice to always save the previous context  at the beginning of the function and restore it at the end of the function (_lines 27 and 50_).


#### Including Animation to Game Engine

__Animating the monster and including it in our game engine__

Ok, now that we know how to move the monster, let's integrate it into our game engine:

1. add the canvas to the HTML page,
2. add the content of the `init()` function to the `start()` function of the game engine,
3. add a few global variables (`canvas`, `ctx`, etc.),
4. call the `drawMonster(...)` function from the mainLoop,
5. add a random displacement to the x, y position of the monster to see it moving,
6. in the main loop, do not forget to clear the canvas before drawing again; this is done using the `ctx.clearRect(x, y, width, height)` function.

You can try [this version online at JSBin](https://jsbin.com/xuruja/edit).

[Local Demo](src/02b-example08.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/2UeN679')"
    src    = "https://bit.ly/35v4GpW"
    alt    = "Screenshot of a trembling monster in a 60 f/s animation"
    title  = "Screenshot of a trembling monster in a 60 f/s animation"
  />
</figure>


HTML code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Trembling monster in the Game Framework&lt;/title&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> <strong style="color: red;">&lt;canvas id="myCanvas" width="200" height="200"&gt;&lt;/canvas&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

JavaScript complete code:

<div><ol>
<li value="1">// Inits</li>
<li>window.onload = function init() {</li>
<li>&nbsp;&nbsp;var game = new GF();</li>
<li>&nbsp; game.start();</li>
<li>};</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li>// GAME FRAMEWORK STARTS HERE</li>
<li>var GF = function(){</li>
<li>&nbsp;&nbsp;<strong style="color: red;">// Vars relative to the canvas</strong></li>
<li>&nbsp;&nbsp;<strong style="color: red;">var canvas, <g id="121" data-gr-id="121">ctx</g>, w, h;</strong> </li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;...</li>
<li> </li>
<li>&nbsp;&nbsp;var measureFPS = function(newTime){</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li> };</li>
<li> </li>
<li> // Clears the canvas content</li>
<li> function clearCanvas() {</li>
<li>&nbsp; &nbsp;ctx.clearRect(0, 0, w, h);</li>
<li> }</li>
<li> </li>
<li> // Functions for drawing the monster and perhaps other objects</li>
<li> function drawMyMonster(x, y) {</li>
<li>&nbsp; &nbsp;...</li>
<li> }</li>
<li> </li>
<li> var mainLoop = function(time){</li>
<li>&nbsp; &nbsp;&nbsp;// Main function, called each frame </li>
<li>&nbsp; &nbsp; measureFPS(time);</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">&nbsp;</strong><strong style="color: red;">// Clear the canvas</strong></li>
<li>&nbsp; &nbsp; <strong style="color: red;">clearCanvas</strong><strong style="color: red;">();</strong></li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">// Draw the monster</strong></li>
<li>&nbsp; &nbsp; <strong style="color: red;">drawMyMonster</strong><strong style="color: red;">(10+Math.random()*10, 10+Math.random()*10);</strong></li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// Call the animation loop every 1/60th of second</li>
<li>&nbsp; &nbsp; requestAnimationFrame(mainLoop);</li>
<li> };</li>
<li>&nbsp;</li>
<li> var start = function(){</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">// Canvas, context etc.</strong></li>
<li>&nbsp; &nbsp; <strong style="color: red;">canvas </strong><strong style="color: red;">= document.querySelector("#myCanvas");</strong></li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">// often useful</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; w = canvas.width; </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; h = canvas.height; </strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// important, we will draw with this object</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; ctx = canvas.getContext('2d');</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// Start the animation</li>
<li>&nbsp; &nbsp; requestAnimationFrame(mainLoop);</li>
<li> };</li>
<li>&nbsp;</li>
<li> //our GameFramework returns a public API visible from outside its scope</li>
<li> return {</li>
<li>&nbsp; &nbsp;start: start</li>
<li> };</li>
<li>};</li>
</ol></div><br>

__Explanations:__

+ Note that we now start the game engine in a `window.onload` callback (_line 2_), so only after the page has been loaded.
+ We also moved 99% of the `init()` method from the previous example into the `start()` method of the game engine, and added the canvas, `ctx`, `w`, `h` variables as global variables to the game framework object.
+ Finally, in the main loop we added a call to the `drawMonster()` function, injecting randomicity through the parameters:  the monster is drawn with an x,y offset of between 0 and 10, in successive frames of the animation.
+ And we clear the previous canvas content before drawing the current frame (_line 35_).

If you try the example, you will see a trembling monster. The canvas is cleared and the monster drawn in random positions, at around 60 times per second!

Next, let's see how to interact with it using the mouse or the keyboard.


#### Notes for 2.3.2 Introducing graphics

+ Best practices for canvas
  1. use a function called AFTER the page is fully loaded (and the DOM is ready), set a pointer to the canvas node in the DOM
  2. get a 2D graphic context for this canvas; the `context` object used to
      + draw on the canvas
      + set global properties, such as color, gradient, patterns and line width
  3. then able to draw something
  4. do not forget to use global variables for the canvas and context object, in particular, the width and height of the cnavas
  5. for each function that will change the context, start by saving context and end by restoring it

+ Example: draw a monster in a canvas
  + canvas element <a name="canvasElm"></a>: `<canvas id="myCanvas" width=200 height=200></canvas>`
  + canvas style <a name="canvasStyle"></a>: `canvas { border: 1px solid black; }`
  + JavaScript snippet
    + declare global variable: `var canvas, ctx, w, h;`
    + init page after DOM ready<a name="initCanvas"></a>: `window.onload = function init() {...}`
      + access canvas element: `canvas = document.querySelector("#myCanvas");`
      + set useful values: `w = canvas.width; h = canvas.height;`
      + set 2D graphic for canvas: `ctx = canvas.getContext("2d");`
      + call to draw monster: `drawMyMonster(10, 10);`
    + draw monster<a name="drawMonster"></a>: `function drawMyMonster(x, y) {...}`
      + save the context: `ctx.save();`
      + translate the coordinate: `ctx.translate(x, y);`
      + draw the frame:  `ctx.strokeRect(0, 0, 100, 100);`
      + draw eyes: `ctx.fillRect(20, 20, 10, 10); ctx.fillRect(65, 20, 10, 10);`
      + draw nose: `ctx.strokeRect(45, 40, 10, 40);`
      + draw mouth: `ctx.strokeRect(35, 84, 30, 10);`
      + draw teeth: `ctx.fillRect(38, 84, 10, 10); ctx.fillRect(52, 84, 10, 10);`
      + restore the context: `ctx.restore();`

+ Adding animaton into canvas
  1. add the canvas to the HTML page
  2. add tne content of the `init()` function to the `start()` function of the game engine
  3. add a few global variables, such as `canvas`, `ctx`, etc.
  4. call the `drawMonster(...)` function from the mainloop
  5. add a random displacement to the x, y position of the monster to see it moving
  6. before drawing again in main loop, clear the canvas by `ctx.clearRect(x, y, width, height)` fucntion

+ Example: add animation to game engine
  + create [canvas element](#canvasElm)
  + JavaScript snippet:
    + init page after DOM ready<a name="newGF"></a>: `window.onload = function init() { var game = new GF(); game.start(); };`
    + generate game framework<a name="genGF"></a>: `var GF = function() {...};`
      + declare variables: `var canvas, ctx, x, y;`
      + [measure FPS](#measureFPS)
      + clear canvas<a name="clearCanvas"></a>: `function clearCanvas() { ctx.clearRect(0, 0, w, h); }`
      + [draw monster](#drawMonster)
      + generate animation loop: `var mainloop = function(time) {...}`
        + call to measure FPS: `measureFPS(time);`
        + call to clear the canvas: `clearCanvas();`
        + call to draw monster: `drawMyMonster(10+Math.random()*10, 10+Math.random()*10);`
        + call to animate: `requestAnimateFrame(mainloop);`
      + start the GF: `var start = function() {...}`
        + ...
        + access canvas: `canvas = document.querySelector("#myCanvas");`
        + set variables: `w = canvas.width; h = canvas.height;`
        + set context: `ctx.canvas.getContext('2d');`
        + start the animation: `requestAnimationFrame(mainloop);`
      + return public API: `return {start: start };`


### 2.3.3 User interaction and event handling

#### Input & output: how do events work in Web apps & games?

__HTML5 events__

There is no input or output in JavaScript. We treat events caused by user actions as inputs, and we manipulate the DOM structure as output. Usually in games, we will maintain state variables representing moving objects like the position and speed of an alien ship, and the animation loop will refer to these variables in determining the movement of such objects.

In any case, the events are called DOM events, and we use the DOM APIs to create _event handlers_.

__How to listen to events__

There are three ways to manage events in the DOM structure. You could attach an event inline in your HTML code like this:

__Method #1: declare an event handler in the HTML code__

<div><ol>
<li value="1">&lt;div id="someDiv" <strong style="color: red;">onclick</strong>="alert('clicked!')"&gt; content of the div &lt;/div&gt;</li>
</ol></div><br>

This method is very easy to use, but it is not the recommended way to handle events. Indeed, It works today but is _deprecated_ (will probably be abandoned in the future). Mixing 'visual layer' (HTML) and 'logic layer' (JavaScript) in one place is really bad practice and causes a host of problems during development.

__Method #2: attach an event handler to an HTML element in JavaScript__

<div><ol>
<li value="1">document.getElementById('someDiv').<strong style="color: red;">onclick </strong>= function() {</li>
<li>&nbsp; &nbsp;alert(<g id="54" data-gr-id="54">'clicked</g>!');</li>
<li>}</li>
</ol></div><br>

This method is fine, but  you will not be able to attach multiple _listener_ functions. If you need to do this, use the version shown below.

__Method #3: register a callback to the event listener with the `addEventListener` method (preferred  method)__

<div><ol>
<li value="1">document.getElementById('someDiv').<strong style="color: red;">addEventListener</strong>('click', function() {</li>
<li>&nbsp; &nbsp;alert('clicked!');</li>
<li>}, false);</li>
</ol></div><br>

Note that the third parameter describes whether the _callback_ has to be called during the captured phase. This is not important for now, just set it to false.


#### Details of the DOM event are passed to the event listener function

When you create an event listener and attach it to an element, the listener will create an `event` object to describe what happened. This object is provided as a parameter of the callback function:

<div><ol>
<li value="1">element.addEventListener(<g id="64" data-gr-id="64">'click</g>', function(<strong style="color: red;">event</strong>) {</li>
<li>&nbsp; &nbsp;<strong style="color: red;">// now you can use event object inside the callback</strong></li>
<li>}, false);</li>
</ol></div><br>

Depending on the type of event you are listening to, you will consult different properties from the `event` object in order to obtain useful information such as: "which keys are pressed down?", "what is the location of the mouse cursor?", "which mouse button has been clicked?", etc.

In the following lessons, we will remind you now how to deal with the keyboard and the mouse (previously covered during the HTML5 Part 1 course) in the context of a game engine (in particular, how to manage multiple events at the same time), and also demonstrate how you can accept input from a game pad using the new Gamepad API.


#### Further reading

In the method #1 above, we mentioned that "Mixing 'visual layer' (HTML) and 'logic layer' (JavaScript) ... bad practice", and this is similarly reflected in many style features being deprecated in HTML5 and moved into CSS3. The management philosophy at play here is called "the separation of concerns" and applies in several ways to software development - at the code level, through to the management of staff. It's not part of the course, but professionals may find the following references useful:

+ [Separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) - Wikipedia, the free encyclopedia


#### Notes for 2.3.3 User interaction and event handling

+ HTML5 events
  + JavaScript w/o input and output
    + treating event caused by user actions as inputs
    + manipulating the DOM structure as output
  + games
    + maintaining state variables respenting moving objects like the position and speed of an alien ship
    + the animation loop refers to the variables in determining the movement of such objects
  + listening the event
    + declare an event handler in the HTML code
      + example: `<div id="someDiv" onclick="alert('clicked!');"> content of the div</div>`
      + easy to use but not recommended $\to$ deprecated
      + bad practice ([separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns): mixing 'visual layer' (HTML) and 'logical layer' (JavaScript)
    + attach an event handler to an HTML element in JavaScript
      + example: `document.getElementById('someDiv').onclick = function() { alert('clicked!'); }`
      + not able to attach multiple listener functions
    + register a callback to the event listener w/ the `addEventListener` method (preferred method)
      + example: `document.getElementById('someDiv').addEventListener('click', function() { alert('clicked!'); }, false );`
      + parameter `false` describes whether the callback has to be called during the captured phase

+ DOM event passed to the event listener function
  + the listener creating an `event` object to describe what happened
  + example: `element.addEventListener('click', function(evt) { // use evt object inside he callback }, false);`
  + different types of event $\to$ different properties of the `event` object


### 2.3.4 Adding key listeners


#### A few reminders

This has been something of a nightmare for years, as different browsers had different ways of handling key events and key codes (read this if you are [fond of JavaScript archaeology](https://unixpapa.com/js/key.html)). Fortunately, it's much improved today and we can rely on methods that should work in any browser less than four years old.

After a keyboard-related event (eg `keydown` or `keyup`), the code of the key that fired the event will be passed to the listener function. It is possible to test which key has been pressed or released, like this:

<div><ol>
<li value="1">window.addEventListener(<g id="84" data-gr-id="84">'keydown</g>', function(event) {</li>
<li>&nbsp; &nbsp;if (event.keyCode === 37) {</li>
<li>&nbsp; &nbsp; &nbsp;// Left arrow was pressed</li>
<li>&nbsp; &nbsp;}</li>
<li>}, false);</li>
</ol></div><br>

At line 2, the key code of 37 corresponds to the left arrow key.

You can try key codes with this [interactive example](http://www.asquare.net/javascript/tests/KeyCode.html), and here is a list of keyCodes (from [CSS Tricks](https://css-tricks.com/snippets/javascript/javascript-keycodes/)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2SH2BEt')"
    src    = "https://bit.ly/35LX8zj"
    alt    = "JavaScript key codes"
    title  = "JavaScript key codes"
  />
</figure>


#### Multiple Keyboard-related Events

__Game requirements: managing multiple `keypress` / `keyrelease` events__

In a game, we often need to check which keys are being used, at a very high frequency - typically from inside the game loop that is looping at up to 60 times per second.

If a spaceship is moving left, chances are you are keeping the left arrow down, and if it's firing missiles at the same time you must also be pressing the space bar like a maniac, and maybe pressing the shift key to release smart bombs.

Sometimes these three keys might be down at the same time, and the game loop will have to take these three keys into account: move the ship left, release a new missile if the previous one is out of the screen or if it reached a target, launch a smart bomb if conditions are met, etc.


#### Keep the list of pertinent keys in a JavaScript object

The typical method used is: store the list of the keys (or mouse button or whatever game pad button...) that are up or down at a given time in a JavaScript object. For our small game engine we will call this object "`inputStates`".

We will update its content inside the different input event listeners, and later check its values inside the game loop to make the game react accordingly.

__Add this to our game framework:__

So, these are the changes to our small game engine prototype (which is far from finished yet):

1. We add an empty `inputStates` object as a global property of the game engine,
2. In the `start()` method, we add event listeners for each keydown and keyup event which controls the game.
3. In each listener, we test if an arrow key or the space bar has been pressed or released, and we set the properties of the `inputStates` object accordingly. For example, if the space bar is pressed, we set `inputStates.space=true;` but if it's released, we reset to `inputStates.space=false`.
4. In the main loop (to prove everything is working), we add tests to check which keys are down; and if a key is down, we print its name on the canvas.

Here is the [online example](https://jsbin.com/razeya/edit) you can try at JSBin

[Local Demo](src/02b-example09.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/2SH2BEt')"
    src    = "https://bit.ly/3q6zPJI"
    alt    = "trembling monster with multiple key press management."
    title  = "trembling monster with multiple key press management."
  />
</figure>


And here is the complete source code:

<div><ol>
<li value="1">// Inits</li>
<li>window.onload = function init() {</li>
<li>&nbsp;&nbsp;var game = new GF();</li>
<li>&nbsp; game.start();</li>
<li>};</li>
<li> </li>
<li> </li>
<li>// GAME FRAMEWORK STARTS HERE</li>
<li>var GF = function(){</li>
<li>&nbsp; &nbsp;...&nbsp;</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">// vars for handling inputs</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;var inputStates = {};</strong></li>
<li> </li>
<li>&nbsp; &nbsp;var measureFPS = function(newTime){</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;};</li>
<li> </li>
<li>&nbsp; &nbsp;// Clears the canvas content</li>
<li>&nbsp; &nbsp;function clearCanvas() {</li>
<li>&nbsp; &nbsp; &nbsp;ctx.clearRect(0, 0, w, h);</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;// Functions for drawing the monster and perhaps other objects</li>
<li>&nbsp; &nbsp;function drawMyMonster(x, y) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;var mainLoop = function(time){</li>
<li>&nbsp; &nbsp; &nbsp;// Main function, called each frame </li>
<li>&nbsp; &nbsp; &nbsp;measureFPS(time);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// Clears the canvas</li>
<li>&nbsp; &nbsp; &nbsp;clearCanvas();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// Draws the monster</li>
<li>&nbsp; &nbsp; &nbsp;drawMyMonster(10+Math.random()*10, 10+Math.random()*10);</li>
<li>&nbsp;</li>
<li>&nbsp;<strong style="color: red;"> &nbsp;&nbsp;</strong><strong style="color: red;">// check inputStates</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;if (inputStates.left) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; ctx.fillText("left", 150, 20);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;}</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;if (inputStates.up) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; ctx.fillText("up", 150, 50);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;}</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;if (inputStates.right) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; ctx.fillText("right", 150, 80);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;}</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;if (inputStates.down) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;ctx.fillText("down", 150, 120);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;} </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;if (inputStates.space) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;ctx.fillText("space bar", 140, 150);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;}</strong> </li>
<li> </li>
<li>&nbsp; &nbsp;// Calls the animation loop every 1/60th of second</li>
<li>&nbsp; &nbsp;requestAnimationFrame(mainLoop);</li>
<li> };</li>
<li> </li>
<li> var start = function(){</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;// Important, we will draw with this object</li>
<li>&nbsp; &nbsp; ctx = canvas.getContext('2d');</li>
<li>&nbsp; &nbsp;&nbsp;// Default police for text</li>
<li>&nbsp; &nbsp; ctx.font="20px Arial";</li>
<li> </li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// Add the listener to the main, window object, and update the states</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; window.addEventListener('keydown', function(event){</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; if (event.keyCode === 37) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.left = true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 38) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.up = true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 39) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.right = true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; } else if (event.keyCode === 40) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.down = true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 32) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.space = true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;}</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;}, false);</strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// If the key&nbsp;is released, change the states object </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; window.addEventListener('keyup', function(event){</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;if (event.keyCode === 37) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.left = false;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 38) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.up = false;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 39) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.right = false;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 40) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.down = false;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 32) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; inputStates.space = false;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;&nbsp;}</strong></li>
<li>&nbsp; &nbsp;&nbsp;}, false);</li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp;// Starts the animation</li>
<li>&nbsp; &nbsp;requestAnimationFrame(mainLoop);</li>
<li>&nbsp;};</li>
<li> </li>
<li> // our GameFramework returns a public API visible from outside its scope</li>
<li> return {</li>
<li>&nbsp; &nbsp;start: start</li>
<li> };</li>
<li>};</li>
</ol></div><br>

You may notice that on some computers / operating systems, it is not possible to simultaneously press the up and down arrow keys, or left and right arrow keys, because they are mutually exclusive. However space + up + right should work in combination.


#### Notes for 2.3.4 Adding key listeners

+ Keyboard related events
  + the code of the key passed tot he listener function once key-board event fired
  + example: `window.addEventListener('keydown', function(evt) { if (event.keyCode === 37) { // left arrow pressed } }, false);`
  + online interactive [event keycode test page](http://www.asquare.net/javascript/tests/KeyCode.html)

+ Multiple keyboard related events
  + game requirements:
    + check keys pressed at a very high frequency
    + typically from inside the game loop that is looping at up to 60 times per second
    + possible pressed down multiple keys
  + keep the list if pertinent keys in a JavaScript object
    + typical methods: store the list of the keys up or down at a given time in a JavaScript object
    + object `inputStates`
      + update content inside the different input event listener
      + check values inside the game loop to make the game react accordingly
  + add changes to game framework
    + add empty `inputState` object as a global property of the game engine
    + add event listeners for each keydown and keyup event to control game within `start()` method
    + test if an arrow key or the space bar pressed or released $\to$ set the properties of the `inputState` object accordingly, e.g., space bar pressed w/ setting `inputState.space=true;` but released w/ resetting `inputState.space=false;`
    + add tests to check which keys are down within main loop

+ Example: handling multiple keyboard-related events
  + [init page](#newGF) after DOM ready
  + [generate game framework](#genGF)
    + declare dictionary to handle inputs<a name="input"></a>: `var inputStates = {};`
    + [measure FPS](#measureFPS)
    + [clear canvas](#clearCanvas)
    + [draw monster](#drawMonster)
    + check input states<a name="chkInput"></a>:
      + left arrow key: `if (inputStates.left) { ctx.fillText("left", 150, 20); }`
      + up arrow key: `if (inputStates.up) { ctx.fillText("up", 150, 50); }`
      + right arrow key: `if (inputStates.right) { ctx.fillText("right", 150, 80); }`
      + down arrow key: `if (inputStates.down) { ctx.fillText("down", 150, 120); }`
      + space bar: `if (inputStates.space) { ctx.fillText("space bar", 150, 150); }`
    + call animation loop: `requestAnimationFrame(mainloop);`
  + [init game framework](#initGF) w/ input handling
    + set 2d context: `ctx = canvas.getContext('2d');`
    + set font: `ctx.font = "20px Arial";`
    + add event listener for key pressed<a name="keyDownCode"></a>: `window.addEventListener('keydown', function(evt) {...}, flase);`
      + left arrow key: `if (evt.keyCode === 37) { inputStates.left = true; }`
      + up arrow key: `else if (evt.keyCode === 38) { inputStates.up = true; }`
      + right arrow key: `else if (evt.keyCode === 39) { inputStates.right = true; }`
      + down arrow key: `else if (evt.keyCode === 40) { inputStates.down = true; }`
      + space bar: `else if (evt.keyCode === 32) {inputStates.space = true; }`
    + add event listener for key released<a name="keyUpCode"></a>: `window.addEventListener('keyup', function(evt) {...}, flase);`
      + left arrow key: `if (evt.keyCode === 37) { inputStates.left = false; }`
      + up arrow key: `else if (evt.keyCode === 38) { inputStates.up = false; }`
      + right arrow key: `else if (evt.keyCode === 39) { inputStates.right = false; }`
      + down arrow key: `else if (evt.keyCode === 40) { inputStates.down = false; }`
      + space bar: `else if (evt.keyCode === 32) { inputStates.space = false; }`
    + start amimation: `requestAnimationFrame(mainloop);`
    + return [public API](#publicAPI)


### 2.3.5 Adding mouse listeners


#### A few reminders

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/35zjZh9')"
    src    = "https://bit.ly/3iRXVGv"
    alt    = "A few reminder sa schema of mouse internals"
    title  = "A few reminder sa schema of mouse internals"
  />
</figure>

Working with mouse events requires detecting whether a mouse button is up or down, identifying that button, keeping track of mouse movement, getting the x and y coordinates of the cursor, etc.

Special care must be taken when acquiring mouse coordinates because the HTML5 canvas has default (or directed) CSS properties which could produce false coordinates. The trick to get the right x and y mouse cursor coordinates is to use this method from the canvas API:

<div><ol>
<li value="1">// necessary to take into account CSS boudaries</li>
<li> var rect = canvas.getBoundingClientRect();</li>
</ol></div><br>

The width and height of the `rect` object must be taken into account. These dimensions correspond to the padding / margins / borders of the canvas. See how we deal with them in the `getMousePos()` function in the next example.

Here is an [online example at JSBin](https://jsbin.com/metavu/edit) that covers all cases correctly.

[Local Demo](src/02b-example10.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/35zjZh9')"
    src    = "https://bit.ly/3wGu1sL"
    alt    = "screenshot of a JsBin example that shows the mouse position + button pressed"
    title  = "screenshot of a JsBin example that shows the mouse position + button pressed"
  />
</figure>


Move the mouse over the canvas and press or release mouse buttons. Notice that we keep the state of the mouse (position, buttons up or down) as part of the `inputStates` object, just as we do with the keyboard (per previous lesson).

Below is the JavaScript source code for this small example:

<div><ol>
<li value="1">var canvas, ctx;</li>
<li><strong style="color: red;">var inputStates = {};</strong></li>
<li> </li>
<li>window.onload = function init() {</li>
<li>&nbsp; &nbsp;canvas = document.getElementById('myCanvas');</li>
<li>&nbsp; &nbsp;ctx = canvas.getContext('2d');</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">canvas</strong><strong style="color: red;">.addEventListener('mousemove', function (evt) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: red;">inputStates</strong><strong style="color: red;">.mousePos = getMousePos(canvas, evt);</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var message = 'Mouse position: ' + inputStates.mousePos.x + ',' +&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inputStates.mousePos.y;</li>
<li>&nbsp; &nbsp; &nbsp; writeMessage(canvas, message);</li>
<li>&nbsp; &nbsp;}, false);</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">canvas</strong><strong style="color: red;">.addEventListener('mousedown', function (evt) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: red;">inputStates</strong><strong style="color: red;">.mousedown = true;</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: red;">inputStates</strong><strong style="color: red;">.mouseButton = evt.button;</strong></li>
<li>&nbsp; &nbsp; &nbsp; var message = "Mouse button " + evt.button + " down at position: " +&nbsp; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inputStates.mousePos.x + ',' + inputStates.mousePos.y;</li>
<li>&nbsp; &nbsp; &nbsp; writeMessage(canvas, message);</li>
<li>&nbsp; &nbsp;}, false);</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">canvas</strong><strong style="color: red;">.addEventListener('mouseup', function (evt) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong style="color: red;">inputStates</strong><strong style="color: red;">.mousedown = false;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var message = "Mouse up at position: " + inputStates.mousePos.x + ',' +&nbsp; &nbsp; &nbsp; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inputStates.mousePos.y;</li>
<li>&nbsp; &nbsp; &nbsp; writeMessage(canvas, message);</li>
<li>&nbsp; &nbsp;}, false);</li>
<li>};</li>
<li> </li>
<li>function writeMessage(canvas, message) {</li>
<li>&nbsp;&nbsp;var ctx = canvas.getContext('2d');</li>
<li>&nbsp; ctx.save();</li>
<li>&nbsp; ctx.clearRect(0, 0, canvas.width, canvas.height);</li>
<li>&nbsp; ctx.font = '18pt Calibri';</li>
<li>&nbsp; ctx.fillStyle = 'black';</li>
<li>&nbsp; ctx.fillText(message, 10, 25);</li>
<li>&nbsp; ctx.restore();</li>
<li>}</li>
<li> </li>
<li><strong style="color: red;">function getMousePos(canvas, evt) {</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;// necessary to take into account CSS boudaries</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;var rect = canvas.getBoundingClientRect();</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;return {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;x: evt.clientX - rect.left,</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;y: evt.clientY - rect.top</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;};</strong></li>
<li><strong style="color: red;">}</strong></li>
</ol></div>


#### Making an object follow the mouse cursor

Try this [example at JsBin](https://jsbin.com/soduko/edit?js,output)

[Local Demo](src/02b-example11.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/35zjZh9')"
    src    = "https://bit.ly/2TEFgmZ"
    alt    = "A rectangle that follows the mouse cursor"
    title  = "A rectangle that follows the mouse cursor"
  />
</figure>

Source code:

<div><ol>
<li value="1">var canvas, ctx, width, height;</li>
<li>var rect = {x:40, y:40, rayon: 30, width:80, height:80, v:1};</li>
<li>var mousepos = {x:0, y:0};</li>
<li>&nbsp;</li>
<li>function init() {</li>
<li>&nbsp; &nbsp; canvas = document.querySelector("#myCanvas");</li>
<li>&nbsp; &nbsp; ctx = canvas.getContext('2d');</li>
<li>&nbsp; &nbsp; width = canvas.width;</li>
<li>&nbsp; &nbsp; height = canvas.height; </li>
<li> </li>
<li>&nbsp; &nbsp; canvas.addEventListener('mousemove', function (evt) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;mousepos = getMousePos(canvas, evt);</li>
<li>&nbsp; &nbsp; }, false); </li>
<li> </li>
<li>&nbsp; &nbsp; mainloop();</li>
<li>}</li>
<li>&nbsp;</li>
<li>function mainloop() {</li>
<li>&nbsp; &nbsp;// 1) clear screen</li>
<li>&nbsp; &nbsp;ctx.clearRect(0, 0, canvas.width, canvas.height);</li>
<li> </li>
<li>&nbsp; &nbsp;// 2) move object</li>
<li>&nbsp; &nbsp;&nbsp;var dx = rect.x - mousepos.x;</li>
<li>&nbsp; &nbsp;&nbsp;var dy = rect.y - mousepos.y;</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">var angle = Math.atan2(dy, dx);</strong></li>
<li> </li>
<li>&nbsp; &nbsp; <strong style="color: red;">rect</strong><strong style="color: red;">.x -= rect.v*Math.cos(angle); </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; rect.y -= rect.v*Math.sin(angle);</strong> </li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// 3) draw object</li>
<li>&nbsp; &nbsp; drawRectangle(angle);</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;//&nbsp;request new frame</li>
<li>&nbsp; &nbsp; window.requestAnimationFrame(mainloop);</li>
<li>}</li>
<li> </li>
<li>function drawRectangle(angle) {</li>
<li>&nbsp; &nbsp;ctx.save();</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">// These two lines move the coordinate system</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;ctx.translate(rect.x, rect.y);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;ctx.rotate(angle);</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;// recenter the coordinate system in the middle</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;// the rectangle. Like that it will rotate around</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;// this point instead of top left corner</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;ctx.translate(-rect.width/2, -rect.height/2);</strong></li>
<li> </li>
<li>&nbsp; &nbsp;ctx.fillRect(0, 0, rect.width, rect.height);</li>
<li>&nbsp; &nbsp;ctx.restore();</li>
<li>}</li>
<li>&nbsp;</li>
<li>function getMousePos(canvas, evt) {</li>
<li>&nbsp; &nbsp;// necessary to take into account CSS boudaries</li>
<li>&nbsp; &nbsp;var rect = canvas.getBoundingClientRect();</li>
<li>&nbsp; &nbsp;return {</li>
<li>&nbsp; &nbsp; &nbsp; x: evt.clientX - rect.left,</li>
<li>&nbsp; &nbsp; &nbsp; y: evt.clientY - rect.top</li>
<li>&nbsp; &nbsp;};</li>
<li>}</li>
</ol></div><br>

__Explanations:__

+ _Line 25_ calculates the angle between mouse cursor and the rectangle,
+ _Lines 27-28_ move the rectangle v pixels along a line between the rectangle's current position and the mouse cursor,
+ _Lines 41-46_ translate the rectangle, rotate it, and recenter the _rotational point_ to the center of the rectangle (in its new position).


#### Adding mouse listeners to the game framework

Now we will include these listeners into our game framework. Notice that we changed some parameters (no need to pass the canvas as a parameter of the `getMousePos()` function, for example).

The [new online version of the game engine](https://jsbin.com/rizuyah/edit) can be tried at JSBin:

[Local Demo](src/02b-example12.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/35zjZh9')"
    src    = "https://bit.ly/3q6HaZP"
    alt    = "Screenshot of a JsBin example that shows message on mouse events"
    title  = "Screenshot of a JsBin example that shows message on mouse events"
  />
</figure>


Try pressing arrows and space keys, moving the mouse, and pressing the buttons, all at the same time. You'll see that the game framework handles all these events simultaneously because the global variable named `inputStates` is updated by keyboard and mouse events, and consulted to direct movements every 1/60th second.

JavaScript source code:

<div><ol>
<li value="1">// Inits</li>
<li>window.onload = function init() {</li>
<li>&nbsp;&nbsp;var game = new GF();</li>
<li>&nbsp; game.start();</li>
<li>};</li>
<li> </li>
<li> </li>
<li>// GAME FRAMEWORK STARTS HERE</li>
<li>var GF = function(){</li>
<li>&nbsp;&nbsp;...</li>
<li> </li>
<li>&nbsp;&nbsp;// Vars for handling inputs</li>
<li>&nbsp;&nbsp;var inputStates = {};</li>
<li> </li>
<li>&nbsp;&nbsp;var measureFPS = function(newTime){</li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li><span style="color: #000000;" color="#000000">&nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp;&nbsp;// Clears the canvas content</li>
<li>&nbsp;&nbsp;function clearCanvas() {</li>
<li>&nbsp; &nbsp; ctx.clearRect(0, 0, w, h);</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp;&nbsp;// Functions for drawing the monster and perhaps other objects</li>
<li>&nbsp;&nbsp;function drawMyMonster(x, y) {</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp;&nbsp;var mainLoop = function(time){</li>
<li>&nbsp; &nbsp;// Main function, called each frame </li>
<li>&nbsp; &nbsp;measureFPS(time);</li>
<li> </li>
<li>&nbsp; &nbsp;// Clears the canvas</li>
<li>&nbsp; &nbsp;clearCanvas();</li>
<li> </li>
<li>&nbsp; &nbsp;// Draws the monster</li>
<li>&nbsp; &nbsp;drawMyMonster(10+Math.random()*10, 10+Math.random()*10);</li>
<li>&nbsp; &nbsp;// Checks inputStates</li>
<li>&nbsp; &nbsp;if (inputStates.left) {</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("left", 150, 20);</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;if (inputStates.up) {</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("up", 150, 40);</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;if (inputStates.right) {</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("right", 150, 60);</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;if (inputStates.down) {</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("down", 150, 80);</li>
<li>&nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp;if (inputStates.space) {</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("space bar", 140, 100);</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;if (inputStates.mousePos) { </li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("x = " + inputStates.mousePos.x + " y = " + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;inputStates.mousePos.y, 5, 150);</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;if (inputStates.mousedown) { </li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillText("mousedown b" + inputStates.mouseButton, 5, 180);</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;// Calls the animation loop every 1/60th of second</li>
<li>&nbsp; &nbsp;requestAnimationFrame(mainLoop);</li>
<li>&nbsp;&nbsp;};</li>
<li> </li>
<li> </li>
<li>&nbsp;&nbsp;function getMousePos(evt) {</li>
<li>&nbsp; &nbsp;&nbsp;// Necessary to take into account CSS boudaries</li>
<li>&nbsp; &nbsp;&nbsp;var rect = canvas.getBoundingClientRect();</li>
<li>&nbsp; &nbsp;&nbsp;return {</li>
<li>&nbsp; &nbsp; &nbsp; x: evt.clientX - rect.left,</li>
<li>&nbsp; &nbsp; &nbsp; y: evt.clientY - rect.top</li>
<li>&nbsp; &nbsp;&nbsp;};</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp;&nbsp;var start = function(){</li>
<li>&nbsp; &nbsp;&nbsp;... </li>
<li>&nbsp; &nbsp;&nbsp;// Adds the listener to the main window object, and updates the states</li>
<li>&nbsp; &nbsp; window.addEventListener('keydown', function(event){</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if (event.keyCode === 37) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; inputStates.left = true;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 38) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; inputStates.up = true;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 39) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; inputStates.right = true;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 40) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; inputStates.down = true;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 32) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; inputStates.space = true;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;&nbsp;}, false);</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// If the key&nbsp;is released, changes the states object </li>
<li>&nbsp; &nbsp;window.addEventListener('keyup', function(event){</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if (event.keyCode === 37) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; inputStates.left = false;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 38) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;inputStates.up = false;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 39) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;inputStates.right = false;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 40) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;inputStates.down = false;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else if (event.keyCode === 32) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; inputStates.space = false;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;}, false);</li>
<li> </li>
<li>&nbsp; &nbsp;// Mouse event listeners</li>
<li>&nbsp; &nbsp;canvas.addEventListener('mousemove', function (evt) {</li>
<li>&nbsp; &nbsp; &nbsp;inputStates.mousePos = getMousePos(evt);</li>
<li>&nbsp; &nbsp;}, false);</li>
<li> </li>
<li>&nbsp; &nbsp;canvas.addEventListener('mousedown', function (evt) {</li>
<li>&nbsp; &nbsp; &nbsp;inputStates.mousedown = true;</li>
<li>&nbsp; &nbsp; &nbsp;inputStates.mouseButton = evt.button;</li>
<li>&nbsp; &nbsp;}, false);</li>
<li> </li>
<li>&nbsp; &nbsp;canvas.addEventListener('mouseup', function (evt) {</li>
<li>&nbsp; &nbsp; &nbsp;inputStates.mousedown = false;</li>
<li>&nbsp; &nbsp;}, false); </li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp;// Starts the animation</li>
<li>&nbsp; &nbsp;requestAnimationFrame(mainLoop);</li>
<li>&nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp;&nbsp;// Our GameFramework returns a public API visible from outside its scope</li>
<li>&nbsp;&nbsp;return {</li>
<li>&nbsp; &nbsp; start: start</li>
<li>&nbsp;&nbsp;};</li>
<li>};</li>
</ol></div>


#### Notes for 2.3.5 Adding mouse listeners

+ Mouse corrdinate
  + HTML canvas w/ default (or directed) CSS properties producing false corrdinate
  + using `var rect = canvas.getBoundingClientRect();` to get exact mouse cursor corrdinates
    + considering the width and height of the `rect` object
    + dimensions corresponding to the padding / margins / borders of the canvas
  + `getMousePos()` to retrieve the mouse position within page

+ Example: mouse position in canvas
  + delcare variables; `var canvas, ctx; var inputStates = {};`
  + init page after DOM ready: `window.onload = function init() {...}`
    + access canvas element: `canvas = document.getElementById('myCanvas');`
    + set 2d graphic: `ctx = canvas.getContext('2d');`
    + add mouse move listener<a name="mousemove"></a>: `canvas.addEventListener('mousemove', function(evt) {...}, false);`
      + get mouse position: `inputStates.mousePos = getMousePos(canvas, evt);`
      + display position msg: `var message = 'Mouse position: ' + inputStates.mousePos.x + inputStates.mousePos.y; writeMessage(canvas, message);`
    + add mouse button down listener<a name="mousedown"></a>: `canvas.addEventListener('mousedown', function(evt) {...}, false);`
      + set mouse status: `inputStates.mousedown = true; inputStates.mouseButton = evt.button;`
      + display position msg: `var message = "Mouse button: " + evt.button + " down at position: " + inputStates.mousePos.x + "," + inputStates.mousePos.y; writeMessage(canvas, message);`
    + add mouse button up listener<a name="mouseup"></a>: `canvas.addEventListener('mousedown', function(evt) {...}, false);`
      + set mouse status: `inputStates.mousedown = false;`
      + display position msg: `var message = "Mouse up at position: " + inputStates.mousePos.x + "," +  inputStates.mousePos.y; writeMessage(canvas, message);`
    + display message: `function writeMessage(canvas, message) {...}`
      + set 2d context: `var ctx = canvas.getContext('2d');`
      + save context: `ctx.save();`
      + empty canvas: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
      + set style and draw message: `ctx.font = '18pt Calibri'; ctx.fillStyle = 'black'; ctx.fillText(message, 10, 25);`
      + restore context: `ctx.restore();`
    + get mouse position<a name="mousePos"></a>: `function getMousePos(canvas, evt) {...}`
      + get CSS boundaries: `var rect = canvas.getBoundingClientRect();`
      + return the relative position: `return {x: evt.clientX - rect.left, y: evt.clientY - rect.top};`

+ Example: object following mouse cursor
  + declare variables: `var canvas, ctx, width, height; var rect = {x: 40, y: 40, rayon: 30, width: 80, height: 80, v: 1}; var mmousePos = {x: 0, y: 0};`
  + init page after DOM ready: `function init() {...}`
    + access canvas element and get 2d context: `canvas = document.querySelector("#myCanvas"); ctx = canvas.getContext{'2d');`
    + get canvas dimensions: `width = canvas.width; height = canvas.height;`
    + add mouse move event listener: `canvas.addEventListener('mousemove', function (evt) { mousePos = getMousePos(canvas, evt); }, false);`
    + call animation loop: `mainloop();`
  + generate animation loop: `function mainloop() {...}`
    + clear screen: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
    + move object: `var dx = rect.x - mousePos.x; var dy = rect.y - mousePos.y; var angle =  Math.anta(dy, dx); rect.x -= rect.v*Math.cos(angle); rect.y -= rect.v*Math.sin(angle);`
    + draw object: `drawRectangle(angle);`
    + request new frame: `window.requestAnimationFrame(mainloop);`
  + draw object: `function drawRectangle(angle) {...}`
    + save context: `ctx.save();`
    + move the coordinate system: `ctx.translate(rect.x, rect.y); ctx.rotate(angle);`
    + recenter the coordinate system to object center: `ctx.translate(-rect.width/2, -rect.height/2);`
    + draw the rectangle: `ctx.fillRect(0, 0, rect.width, rect.height);`
    + restore context: `ctx.resore();`
  + get [mouse position](#mousePos)
  
+ Example: adding mouse listeners to the game framework
  + [init page](#newGF) after DOM ready
  + [generate game framework](#genGF)
    + ...
    + declare dictionary to [handle inputs](#input)
    + [measure FPS](#measureFPS)
    + ...
  + [clear canvas](#clearCanvas)
  + [draw monster](#drawMonster)
  + generate main loop: `var mainloop = function(time) {...}`
    + call to measure FPS: `measureFPS(time);`
    + clear the canvas: `clearCanvas();`
    + call to draw monster: `drawMyMonster(10+Math.random()*10, 10+Math.random()*10);`
    + [check input](#chkInput)
    + display mouse psotion: `if (inputStates.mousePos) { ctx.fillText("x = " + inputStates.mousePos.x + " y = " + inputStates.mousePos.y, 5, 150); }`
    + display mouse button: `if (inputStates.mousedown) { ctx.fillText("mousedown b" + inputStates.mouseButton, 5, 180); }`
    + call to animate: `requestAnimateFrame(mainloop);`
  + get [mouse position](#mousePos)
  + register event listeners: `var start = function() {...}`
    + add event listener for [key pressed](#keyDownCode)
    + add event listener for [key released](#keyUpCode)
    + add event listener for [mouse move](#mousemove)
    + add event listener for [mouse button down](#mousedown)
    + add event listener for [mouse button up](#mouseup)
    + call to animate: `requestAnimationFrame(mainloop);`
  + return a [public API](#publicAPI)


### 2.3.6 Gamepad events


#### Live coding video: gamepad management

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/35CmbEQ)


Some games, mainly arcade/action games, are designed to be used with a gamepad:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/2TLYJ5c"
    alt    = "a xbox 360 gamepad"
    title  = "a xbox 360 gamepad"
  />
</figure>


#### The Gamepad API


The [Gamepad API](https://w3c.github.io/gamepad/) is currently supported by all major browsers (including Microsoft Edge), except Internet Explorer - see the up to date version of this [feature's compatbility table](https://caniuse.com/#feat=gamepad). Note that the API is still a draft and may change in the future. We recommend using a Wired Xbox 360 Controller or a PS2 controller, both of which should work out of the box on Windows XP, Windows Vista, Windows, and Linux desktop distributions. Wireless controllers are supposed to work too, but we haven't tested the API with them. You may find someone who has managed but they've probably needed to install an operating system driver to make it work.


#### Detecting gamepads

__Events triggered when the gamepad is plugged in or unplugged__

Let's start with a 'discovery' script to check that the GamePad is connected, and to see the range of facilities it can offer to JavaScript.

If the user interacts with a controller (presses a button, moves a stick) a [`gamepadconnected`](https://w3c.github.io/gamepad/#event-gamepadconnected) event will be sent to the page. NB the page must be visible! The event object passed to the `gamepadconnected` listener has a `gamepad` property which describes the connected device.

[Example on JSBin](https://jsbin.com/kiduwu/edit?console,output)

[Local Demo](src/02b-example013.html)

<div><ol>
<li value="1">window.addEventListener("gamepadconnected", function(e) {</li>
<li>&nbsp; &nbsp;var gamepad = e.gamepad;</li>
<li>&nbsp; &nbsp;var index = gamepad.index;</li>
<li>&nbsp; &nbsp;var id = gamepad.id;</li>
<li>&nbsp; &nbsp;var nbButtons = gamepad.buttons.length;</li>
<li>&nbsp; &nbsp;var nbAxes = gamepad.axes.length;</li>
<li> </li>
<li>&nbsp; &nbsp;console.log("Gamepad No " + index + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;", with id " + id + " is connected. It has " + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;nbButtons + " buttons and " +</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;nbAxes + " axes");</li>
<li>});</li>
</ol></div><br>


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/2Udwwo5"
    alt    = "a xbox 360 gamepad"
    title  = "a xbox 360 gamepad"
  />
</figure>

If a gamepad is disconnected (you unplug it), a [`gamepaddisconnected`](https://w3c.github.io/gamepad/#event-gamepaddisconnected) event is fired. Any references to the gamepad object will have their `connected` property set to false.

<div><ol>
<li value="1">window.addEventListener("<g id="186" data-gr-id="186">gamepaddisconnected</g>", function(e) {</li>
<li>&nbsp; &nbsp;var gamepad = e.gamepad;</li>
<li>&nbsp; &nbsp;var index = gamepad.index;</li>
<li> </li>
<li>&nbsp; &nbsp;console.log("Gamepad No " + index +&nbsp;" has been disconnected");</li>
<li>});</li>
</ol></div>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/3wIDRdH"
    alt    = "gamepad disconnected, screenshot from jsbin console"
    title  = "gamepad disconnected, screenshot from jsbin console"
  />
</figure>


__Scanning for gamepads__

If you reload the page, and if the gamepad has already been detected by the browser, it will not fire the gamepadconnected event again. This can be problematic if you use a global variable for managing the gamepad, or an array of gamepads in your code. As the event is not fired, these variables will stay undefined...

So, you need to regularly scan for gamepads available on the system. You should still use that event listener if you want to do something special when the system detects that a gamepad has been unplugged.

Here is the code to use to scan for a gamepad:

<div><ol>
<li value="1">var gamepad;</li>
<li>&nbsp;</li>
<li>function mainloop() {</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;scangamepads();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// test gamepad status: buttons, joysticks etc.</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;requestAnimationFrame(mainloop);</li>
<li>}</li>
<li>&nbsp;</li>
<li>function scangamepads() {</li>
<li>&nbsp;&nbsp;// function called 60 times/s</li>
<li>&nbsp;<strong style="color: red;">&nbsp;</strong><strong style="color: red;">// the gamepad is a "snapshot", so we need to set it </strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;// 60 times / second in order to have an updated status</strong></li>
<li>&nbsp;&nbsp;var gamepads = navigator.getGamepads();</li>
<li> </li>
<li>&nbsp;&nbsp;for (var i = 0; i &lt; gamepads.length; i++) {</li>
<li>&nbsp; &nbsp;&nbsp;// current gamepad is not necessarily the first</li>
<li>&nbsp; &nbsp;&nbsp;if(gamepads[i] !== undefined)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;gamepad = gamepads[i];</li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
</ol></div><br>

In this code, we check every 1/60 second for newly or re-connected gamepads, and we update the gamepad global var with the first gamepad object returned by the browser. We need to do this so that we have an accurate "snapshot" of the gamepad state, with fixed values for the buttons, axes, etc. If we want to check the current button and joystick statuses, we must poll the browser at a high frequency  and call for an updated snapshot.

From the specification: "_`getGamepads` retrieves a snapshot of the data for the currently connected and interacted with gamepads._"

This code will be integrated (as well as the event listeners presented earlier) in the next JSBin examples.

To keep things simple, the above code works with a single gamepad - here's a good [example of managing multiple gamepads](https://github.com/luser/gamepadtest).


#### Detecting button status and axes values (joysticks)

__Properties of the gamepad object__

The gamepad object returned in the event listener has [different properties](https://w3c.github.io/gamepad/#gamepad-interface):

+ `id`: a string indicating the id of the gamepad. Useful with the `mapping` property below.
+ `index`: an integer used to distinguish multiple controllers (gamepad 1, gamepad 2, etc.).
+ `connected`: true if the controller is still connected, false if it has been disconnected.
+ `mapping`: not implemented yet by most browsers. It will allow the controllers of the gamepad to be remapped. A layout map is associated with the id of the gamepad. By default, and before they implement support for different mapping, all connected gamepads use a [standard default layout](https://w3c.github.io/gamepad/#remapping).


  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
      onclick= "window.open('https://bit.ly/3gGGF5m')"
      src    = "https://bit.ly/3gGGF5m"
      alt    = "standard gamepad layout"
      title  = "standard gamepad layout"
    />
    <figcaption> Click the above image to open a large view in another window/tab. </figcaption>
  </figure>

+ `axes`: an array of floating point values containing the state of each axis on the device. Usually these represent the analog sticks, with a pair of axes giving the position of the stick in its X and Y axes. Each axis is normalized to the range of -1.0...1.0, with -1.0 representing the up or left-most position of the axis, and 1.0 representing the down or right-most position of the axis.
+ `buttons`: an array of [GamepadButton](https://w3c.github.io/gamepad/#idl-def-GamepadButton) objects containing the state of each button on the device. Each GamepadButton has a `pressed` and a `value` property.
+ The `pressed` property is a Boolean property indicating whether the button is currently pressed (`true`) or unpressed (`false`).
+ The `value` property is a floating point value used to enable representing analog buttons, such as the triggers, on many modern gamepads. The values are normalized to the range 0.0...1.0, with 0.0 representing a button that is not pressed, and 1.0 representing a button that is fully depressed.


__Detecting whether a button is pressed__

Digital, on/off buttons evaluate to either one or zero (respectively). Whereas analog buttons will return a floating-point value between zero and one.

[Example on JSBin](https://jsbin.com/heriqej/edit). You might also give a look at at [this demo](https://github.com/luser/gamepadtest) that does the same thing but with multiple gamepads.

[Local Demo](src/02b-example14.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/3vJEpia"
    alt    = "button status detected, example on jsbin"
    title  = "button status detected, example on jsbin"
  />
</figure>


Code for checking if a button is pressed:

<div><ol>
<li value="1">function checkButtons(gamepad) {</li>
<li>&nbsp; &nbsp;for (var i = 0; i &lt; gamepad.buttons.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; // do nothing is the gamepad is not ok</li>
<li>&nbsp; &nbsp; &nbsp; if(gamepad === undefined) return;</li>
<li>&nbsp; &nbsp; &nbsp; if(!gamepad.connected) return;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var b = gamepad.buttons[i];</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if(b.pressed) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log("Button " + i + " is pressed.");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(b.value !== undefined)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// analog trigger L2 or R2, value is a float in [0, 1]</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log("Its value:" + b.val);</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;}</li>
<li>}</li>
</ol></div><br>

Next, we'll integrate it into the `mainloop` code. Note that we also need to call the `scangamepads` function from the loop, to generate fresh "snapshots" of the gamepad with updated properties. Without this call, the `gamepad.buttons` will return the same  states every time.

<div><ol>
<li value="1">function <g id="192" data-gr-id="192">mainloop</g>() {</li>
<li>&nbsp; &nbsp;// clear, draw objects, etc...</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;scangamepads();</li>
<li>&nbsp; &nbsp;// Check gamepad button states</li>
<li>&nbsp; &nbsp;checkButtons(gamepad);</li>
<li> </li>
<li>&nbsp; &nbsp;// animate at 60 frames/s</li>
<li>&nbsp; &nbsp;requestAnimationFrame(mainloop);</li>
<li>}</li>
</ol></div><br>


__Detecting axes (joystick) values__

[Example on JSBin](https://jsbin.com/yaxika/edit)

[Local Demo](src/02b-example15.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/3wFhxSp"
    alt    = "axes detection in JsBin"
    title  = "axes detection in JsBin"
  />
</figure>


Code for detecting the axes' values:

<div><ol>
<li value="1">// detect axis (joystick states)</li>
<li>function checkAxes(gamepad) {</li>
<li>&nbsp; &nbsp;if(gamepad === undefined) return;</li>
<li>&nbsp; &nbsp;if(!gamepad.connected) return;</li>
<li> </li>
<li>&nbsp; &nbsp;for (var i=0; i&lt;gamepad.axes.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;var axisValue = gamepad.axes[i];</li>
<li>&nbsp; &nbsp; &nbsp;// do something with the value</li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;}</li>
<li>}</li>
</ol></div><br>

__Detecting the direction (left, right, up, down, diagonals) and angle of the left joystick__

We could add an inputStates object similar to the one we used in the game framework, and check its values in the mainloop to decide whether to move the player up/down/left/right, including diagonals - or maybe we'd prefer to use the current angle of the joystick. Here is how we manage this:

[JSBin example](https://jsbin.com/vuxoqo/edit?js,output):

[Local Demo](src/02b-example16.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/3q9LfMD"
    alt    = "direction and angle detection for joystick"
    title  = "direction and angle detection for joystick"
  />
</figure>


Source code extract:

<div><ol>
<li value="1"><strong style="color: red;">var inputStates = {};</strong></li>
<li>...</li>
<li>function <g id="189" data-gr-id="189">mainloop</g>() {</li>
<li>&nbsp; &nbsp;// clear, draw objects, etc...</li>
<li>&nbsp; &nbsp;// update gamepad status</li>
<li>&nbsp; &nbsp;scangamepads();</li>
<li>&nbsp;&nbsp;// Check gamepad button states</li>
<li>&nbsp; checkButtons(gamepad);</li>
<li>&nbsp;&nbsp;// Check joysticks states</li>
<li>&nbsp; checkAxes(gamepad);</li>
<li> </li>
<li>&nbsp;&nbsp;<strong style="color: red;">// Move the player, taking into account</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;// the gamepad left joystick state</strong></li>
<li><strong style="color: red;">&nbsp; updatePlayerPosition();</strong></li>
<li> </li>
<li>&nbsp;&nbsp;// We could use the same technique in</li>
<li>&nbsp;&nbsp;// order to react when buttons are pressed</li>
<li>&nbsp;&nbsp;//...</li>
<li> </li>
<li>&nbsp;&nbsp;// animate at 60 frames/s</li>
<li>&nbsp; requestAnimationFrame(mainloop);</li>
<li>}</li>
<li>&nbsp;</li>
<li>function updatePlayerPosition() {</li>
<li>&nbsp; &nbsp;directionDiv.innerHTML += "";</li>
<li>&nbsp; <strong style="color: red;">&nbsp;</strong><strong style="color: red;">if(inputStates.left)</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; directionDiv.innerHTML = "Moving left";</li>
<li>&nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp;<strong style="color: red;">if(inputStates.right)</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; directionDiv.innerHTML = "Moving right";</li>
<li>&nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp;<strong style="color: red;">if(inputStates.up)</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; directionDiv.innerHTML = "Moving up";</li>
<li>&nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp;<strong style="color: red;">if(inputStates.down)</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; directionDiv.innerHTML = "Moving down";</li>
<li>&nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp;// Display the angle in degrees, in the HTML page</li>
<li>&nbsp; &nbsp;angleDiv.innerHTML = Math.round((<strong style="color: red;">inputStates.angle</strong>*180/Math.PI));</li>
<li>}</li>
<li>&nbsp;</li>
<li>// gamepad code below</li>
<li>// -------------------------</li>
<li>// detect axis (joystick states)</li>
<li>function checkAxes(gamepad) {</li>
<li>&nbsp; if(gamepad === undefined) return;</li>
<li>&nbsp;&nbsp;if(!gamepad.connected) return;</li>
<li> </li>
<li>&nbsp;&nbsp;...</li>
<li> </li>
<li>&nbsp;<strong style="color: red;">&nbsp;</strong><strong style="color: red;">// Set inputStates.left, right, up, down</strong></li>
<li><strong style="color: red;">&nbsp; inputStates.left = inputStates.right = inputStates.up = inputStates.down = false;</strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;// all values between [-1 and 1]</strong></li>
<li>&nbsp;<strong style="color: red;">&nbsp;</strong><strong style="color: red;">// Horizontal detection</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;if(gamepad.axes[0] &gt; 0.5) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;inputStates.right=true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;inputStates.left=false;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;} else if(gamepad.axes[0] &lt; -0.5) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;inputStates.left=true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;inputStates.right=false;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;} </strong></li>
<li><strong style="color: red;"> </strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;// vertical detection</strong></li>
<li><strong style="color: red;">&nbsp; if(gamepad.axes[1] &gt; 0.5) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; inputStates.down=true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; inputStates.up=false;</strong></li>
<li><strong style="color: red;">&nbsp; } else if(gamepad.axes[1] &lt; -0.5) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; inputStates.up=true;</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; inputStates.down=false;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;}</strong> </li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;// compute the angle. gamepad.axes[1] is the </li>
<li>&nbsp;&nbsp;// sinus of the angle (values between [-1, 1]),</li>
<li>&nbsp;&nbsp;// gamepad.axes[0] is the cosinus of the angle.</li>
<li>&nbsp;&nbsp;// we display the value in degree as in a regular</li>
<li>&nbsp;&nbsp;// trigonometric circle, with the x axis to the right</li>
<li>&nbsp;&nbsp;// and the y axis that goes up.</li>
<li>&nbsp;&nbsp;// The angle = arcTan(sin/cos); We inverse the sign of</li>
<li>&nbsp;&nbsp;// the sinus in order to have the angle in standard</li>
<li>&nbsp;&nbsp;// x and y axis (y going up)</li>
<li>&nbsp; <strong style="color: red;">inputStates</strong><strong style="color: red;">.angle = Math.atan2(-gamepad.axes[1], gamepad.axes[0]);</strong></li>
<li>}</li>
</ol></div>


#### Other gamepads and joysticks tested

__Logitech Attack 3 Joystick on Linux__

> _Hi (=dn reports)_: Have successfully installed a Logitech Attack 3 joy-stick on my Thinkpad running Linux Mint 17.1. It runs all of the code presented here correctly, reporting 11 buttons and 3 axes (the knurled rotating knob (closest to my pen) is described as a 'throttle' or 'accelerator')).

> Traditionally Linux has been described as 'for work only' or 'no games', so it was a pleasant surprise to see how easy things were - no "driver" to install (it seems important to uninstall any existing connection between a device and the x-server), installed "joystick" testing and calibration tool, and the "jstest-gtk" configuration and testing tool; and that was 'it' - no actual configuration was necessary!

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/3xAOQWu"
    alt    = "saitek joystick"
    title  = "saitek joystick"
  />
</figure>


__Wireless Microsoft gamepad__

> Hi! (Michel Buffa reports) I managed to test a wireless Microsoft gamepad on a PC windows 8.1 and it worked with Chrome/FF. I did not try with a console version of the wireless gamepad, I tried with a version for PC, that comes with a wireless receiver (see pictures and video)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3iW8jNo')"
    src    = "https://bit.ly/3wHAYKi"
    alt    = "wireless padwureless pad"
    title  = "wireless padwureless pad"
  />
</figure>


[Video of this gamepad with Windows 8.1 + FireFox](https://goo.gl/photos/rfNc36W8v9ZKRyjH8)


#### External resources

+ THE BEST resource: [this paper](https://www.smashingmagazine.com/2015/11/gamepad-api-in-web-games/) from smashingmagazine.com tells you everything about the GamePad API. Very complete, explains how to set a dead zone, a keyboard fallback, etc.
+ Good [article](https://hacks.mozilla.org/2013/12/the-gamepad-api/) about using the gamepad API on the Mozilla Developer Network site
+ An [interesting article](https://www.html5rocks.com/en/tutorials/doodles/gamepad/) on the gamepad support, published on the HTML5 Rocks Web site
+ [gamepad.js](https://github.com/neogeek/gamepad.js) is a Javascript library to enable the use of gamepads and joysticks in the browser. It smoothes over the differences between browsers, platforms, APIs, and a wide variety of gamepad/joystick devices.
+ [Another library](https://github.com/kallaspriit/HTML5-JavaScript-Gamepad-Controller-Library) we used in our team for controlling a mobile robot (good support from the authors)
+ [Gamepad Controls for HTML5 Games](https://blog.teamtreehouse.com/gamepad-controls-html5-games)


#### Notes for 2.3.6 Gamepad events

+ Gamepad API
  + a [W3C draft](https://w3c.github.io/gamepad/)
  + supported by all browsers, except IE
  + recommendation: Wired Xbox 360 Controller or a PS2 controller
  + wireless controllers supported but not tested yet
  + some controllers probably require to install drivers

+ Detecting gamepad
  + event triggered when plugged in or unplugged
  + `gamepadconnected` event trigered as user interacting (press a button or move a stick)
  + `gamepad` property along w/ event listener to describe the connected device
  + issue: gamepad already detected by the browser
    + using a global variable for managing the gamepad or an array of gampads in code
    + reload page $\to$ no event fired $\to$ variables undefined
  + solution: regular scanning gamepap availability
  + `getGamepads`: retrieving a snapshot of the data for the current connected nad interacted w/ gamepads
  + [luser/gamepadtest in GitHub](https://github.com/luser/gamepadtest): good example of managing multiple gamepads

+ Attributes of [Gamepad interface](https://w3c.github.io/gamepad/#gamepad-interface)
  + `id`: identification string for the gamepad, brand or style of connected gamepad, useful w/ `mapping` property
  + `index`: index of the gamepad in the Naviagtor, used for multiple gamepads
  + `connected`: whether the physical device represented still connected to the system
  + `timestamp`: last time the data updated
  + `mapping`:
    + setting a property to a known mapping name
    + not implemented yet by most browsers
    + a layout map associated w/ the `id` of the gamepad
    + default: all connected gamepads using a [standard default layout](https://w3c.github.io/gamepad/#remapping)
  + `axes`:
    + array of values for all axes of gamepad, ranging [-1.0, 1.0]
    + usually representing the analog sticks
    + a pair of axes given the position on the stick in its X and Y axis
    + -1.0 representing the up or left-most position of the axis while 1.0 representing the down or right-most position of the axis
    + compute the angle via axes values w/ `angle = arcTan(sin/cos);`
  + `buttons`: array of button states of `GamepadButton` objects for all buttons of the gamepad
    + `pressed`: a Boolean property indicating whether the button is currently pressed (`true`) or unpressed (`false`)
    + `value`: a floating-point value used to enable representing analog buttons, normalized to [0.0, 1.0]

+ Example: detecting gamepad
  + add gamepad connected evenet listener<a name="gamepadconnected"></a>: `windows.addEventlistener("gandpadconnected", function(e) {...});`
    + access gamepad attributes: `var gamepad = e.gamepad; var index = gamepad.index; var id = gamepad.id; var nbButtons = gampad.buttons.length; var nbAxes = gampad.axes.length;`
    + log msg: `console.log("Gamepad No " + index + ", with id " + id + " is connected. It has " + nbButtons + " buttons and " + nbAxes + " axes");`
  + add gamepad disconcted event listener<a name="gamepaddisconnected"></a>: `windows.addEventListener("gamepaddisconnected", function(e) {...});`
    + access gamepad attribute: `var gampad = e.gamepad; var index = gamepad.index;`
    + log msg: `console.log("Gamepad No " + index + " has been disconnected");`

+ Example: scanning the gamepad
  + scan gamepad availability every 1/60 second
  + declare variable: `var gamepad;`
  + create animation loop w/ gampad scan: `function mainloop() {...}`
    + call to scan gamepads: `... scangamepads(); // test gampad status: buttons, joysticks etc.`
    + call for next frame: `... requestAnimationFrame(mainloop);`
  + scan gamepads<a name="scangamepad"></a>: `function scangampads() {...}`
    + get list of gamepads: `var gamepads = navigator.getGamepads();`
    + iterate on all gamepad ports: `for (var i=0; i<gamepads.length; i++>) {...}`
      + chk availability: `if (gamepads[i] !== undefined) { gamepad = gamepads[i]; }`

+ Example: detecting button status
  + scan buttons<a name="chkButtons"></a>: `function checkButtons(gamepad) {...}`
  + iterate through all buttons: `for (var i=0; i<gamepad.buttons.length; i++) {...}`
  + pass through if gamepad not available: `if (gamepad === undefined) return; if (!gamepad.connected) return;`
  + declare variable for buttons: `var b = gamepad.button[i];`
  + check button pressing: `if (b.pressed) {...}`
    + log msg: `console.log("Button " + i + " is pressed.");`
    + chk axes values and log msg: `if (b.value !== undefined) {console.log("It's value: " + b.value);}`

+ Example: detecting axes values
  + check axes w/ values<a name="chkAxesVal"></a>: `function checkAxes(gamepad) {...}`
  + check availability of gamepad: `if (gamepad === undefined) return; if (!gamepad.connected) return;`
  + iterate through all axes: `for (var i=0; i<gamepad.axes.length; i++) {...}`
    + access axis: `var axisValue = gamepad.axes[i];`
    + action: `// do something w/ the value`

+ Example: detecting the direction
  + check axes w/ direction<a name="chkAxesDir"></a>: `function checkAxes(gamepad) {...}`
  + reset direction w/ inputStates: `inputStates.left = inputStates.right = inputStates.top = inputStates.down = false;`
  + read value for left direction: `if (gamepad.axes[0] > 0.5) { inputStates.right = true; inputStates.left = false; }`
  + read value for right direction: `else if (gamepad.axes[0] < -0.5) { inputStates.right = false; inputStates.left = true; }`
  + read value for down direction: `if (gamepad.axes[1] > 0.5) { inputStates.down = true; inputStates.up = false; }`
  + read value for up direction: `else if (gamepad.axes[1] < -0.5) { inputStates.down = false; inputStates.up = true; }`
  + compute the angle: `inputStates.angle = Math.atan2(-gamepad.axes[1], gamepad.axes[0]);`


### 2.3.7 Move the monster!


#### Live coding video: game framework and user interactions

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2SEYqcs)

#### Moving object with arrow keys

__Make the monster move using the arrow keys, and to increase its speed by pressing a mouse button__

To conclude this topic about events, we will use the arrow keys to move our favorite monster up/down/left/right, and make it accelerate when we press a mouse button while it is moving. Notice that pressing two keys at the same time will make it move diagonally.

Check this [online example at JSBin](https://jsbin.com/yebufu/edit): we've changed very few lines of code from the previous evolution!

[Local Demo](src/02b-example17.html)


#### Add a JavaScript object to describe the monster

<div><ol>
<li value="1">// The monster!</li>
<li>var monster = {</li>
<li>&nbsp; x:10,</li>
<li>&nbsp; y:10,</li>
<li>&nbsp; speed:1</li>
<li> };</li>
</ol></div><br>

Where `monster.x` and `monster.y` define the monster's current position and `monster.speed` corresponds to the number of pixels the monster will move between animation frames.

Note: this is not the best way to animate objects in a game; we will look at a far better solution - "_time based animation_" - in another lesson.

__We modified the game loop as follows:__

<div><ol>
<li value="1">var mainLoop = function(time){</li>
<li>&nbsp;&nbsp;// Main function, called each frame </li>
<li>&nbsp; measureFPS(time);</li>
<li> </li>
<li>&nbsp;&nbsp;// Clears the canvas</li>
<li>&nbsp; clearCanvas();</li>
<li> </li>
<li>&nbsp;&nbsp;<strong style="color: red;">// Draws the monster</strong></li>
<li><strong style="color: red;">&nbsp; drawMyMonster(monster.x, monster.y);</strong></li>
<li> </li>
<li>&nbsp;&nbsp;<strong style="color: red;">// Checks inputs and moves the monster</strong></li>
<li><strong style="color: red;">&nbsp; updateMonsterPosition();</strong></li>
<li> </li>
<li>&nbsp;&nbsp;// Calls the animation loop every 1/60th of second</li>
<li>&nbsp; requestAnimationFrame(mainLoop);</li>
<li> };</li>
</ol></div><br>

We moved all the parts that check the input states in the `updateMonsterPosition()` function:

<div><ol>
<li value="1">function updateMonsterPosition() {</li>
<li>&nbsp; monster.speedX = monster.speedY = 0;</li>
<li></li>
<li>&nbsp;&nbsp;// Checks inputStates</li>
<li>&nbsp;&nbsp;if (inputStates.left) {</li>
<li>&nbsp; &nbsp; ctx.fillText("left", 150, 20);</li>
<li>&nbsp; &nbsp; monster.speedX = -monster.speed;</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;if (inputStates.up) {</li>
<li>&nbsp; &nbsp; ctx.fillText("up", 150, 40);</li>
<li>&nbsp; &nbsp; monster.speedY = -monster.speed;</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;if (inputStates.right) {</li>
<li>&nbsp; &nbsp; ctx.fillText("right", 150, 60);</li>
<li>&nbsp; &nbsp; monster.speedX = monster.speed;</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;if (inputStates.down) {</li>
<li>&nbsp; &nbsp; ctx.fillText("down", 150, 80);</li>
<li>&nbsp; &nbsp; monster.speedY = monster.speed;</li>
<li>&nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;if (inputStates.space) {</li>
<li>&nbsp; &nbsp; ctx.fillText("space bar", 140, 100);</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;if (inputStates.mousePos) { </li>
<li>&nbsp; &nbsp; ctx.fillText("x = " + inputStates.mousePos.x + " y = " + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inputStates.mousePos.y, 5, 150);</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;if (inputStates.mousedown) { </li>
<li>&nbsp; &nbsp; ctx.fillText("mousedown b" + inputStates.mouseButton, 5, 180);</li>
<li>&nbsp; &nbsp; monster.speed = 5;</li>
<li>&nbsp;&nbsp;} else {</li>
<li>&nbsp;&nbsp;// Mouse up</li>
<li>&nbsp; monster.speed = 1;</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; monster.x += monster.speedX;</li>
<li>&nbsp; monster.y += monster.speedY;</li>
<li>}</li>
</ol></div><br>

__Explanations:__

+ In this function, we added two properties to the `monster` object: `speedX` and `speedY` which will correspond to the number of pixels we will add to the `x` and `y` position of the monster at each new frame of animation.
+ We first set these to zero (_line 2_), then depending on the keyboard input states, we set them to a value equal to `monster.speed` or `-monster.speed` modified by the keys that are being pressed at the time (_lines 4-20_).
+ Finally, we add `speedX` and `speedY` pixels to the `x` and/or `y` position of the monster (_lines 36 and 37_).
+ When the function is called by the game loop, if `speedX` and/or `speedY` are non-zero they will change the `x` and `y` position of the monster in successive frames, making it move smoothly.
+ If a mouse button is pressed or released we set the `monster.speed` value to `+5` or to `+1`. This will make the monster move faster when a mouse button is down, and return to its normal speed when no button is down.

Notice that two arrow keys and a mouse button can be pressed down at the same time. In this situation, the monster will take a diagonal direction and accelerate. This is why it is important to keep all the input states up-to-date, and not to handle single events individually.


#### Gamepad enhancements

Let's add the gamepad utility functions from the previous lesson (we tidied them a bit too, removing the code for displaying the progress bars, buttons, etc.), added a gamepad property to the game framework, and added one new call in the game loop for updating the gamepad status:

[Check the result](https://jsbin.com/yidohe/edit) on JSBin:

[Local Demo](src/02b-example18.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3wKXUrX')"
    src    = "https://bit.ly/3gIdqzg"
    alt    = "move the monster with the gamepad, jsbin screenshot"
    title  = "move the monster with the gamepad, jsbin screenshot"
  />
</figure>


The new updated `mainloop`:

<div><ol>
<li value="1">var mainLoop = function(time){</li>
<li>&nbsp; &nbsp;//main function, called each frame </li>
<li>&nbsp; &nbsp;measureFPS(time);</li>
<li> </li>
<li>&nbsp; &nbsp;// Clear the canvas</li>
<li>&nbsp; &nbsp;clearCanvas();</li>
<li> </li>
<li>&nbsp; <strong style="color: red;">&nbsp;</strong><strong style="color: red;">// gamepad</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;updateGamePadStatus();</strong></li>
<li> </li>
<li>&nbsp; &nbsp;// draw the monster</li>
<li>&nbsp; &nbsp;drawMyMonster(monster.x, monster.y);</li>
<li> </li>
<li>&nbsp; &nbsp;// Check inputs and move the monster</li>
<li>&nbsp; &nbsp;updateMonsterPosition();</li>
<li> </li>
<li>&nbsp; &nbsp;// Call the animation loop every 1/60th of second</li>
<li>&nbsp; &nbsp;requestAnimationFrame(mainLoop);</li>
<li> };</li>
</ol></div><br>

And here is the updateGamePadStatus function (the inner function calls are to gamepad utility functions detailed in the previous lesson):

<div><ol>
<li value="1">function updateGamePadStatus() {</li>
<li>&nbsp;&nbsp;// get new snapshot of the gamepad properties</li>
<li>&nbsp; scangamepads();</li>
<li>&nbsp;&nbsp;// Check gamepad button states</li>
<li>&nbsp; checkButtons(gamepad);</li>
<li>&nbsp;&nbsp;// Check joysticks</li>
<li>&nbsp; checkAxes(gamepad);</li>
<li> }</li>
</ol></div><br>

The `checkAxes` function updates the `left`, `right`, `up`, `down` properties of the `inputStates` object we previously used with key events. Therefore, without changing any code in the `updatePlayerPosition` function, the monster moves by joystick command!


#### Notes for 2.3.7 Move the monster!

+ Example: moving and accelerating object
  + tasks:
    + arrow keys to move object up/down/left/right
    + mouse button to accelerate
  + set object position and speed: `var monster = {x: 10, y: 10, speed: 1};`
  + generate animation loop: `var mainloop = function(time) {...}`
    + call to measure FPS: `measureFPS(time);`
    + call to empty canvas: `clearCanvas();`
    + call to draw monster: `drawMyMonster(monster.x, monster.y);`
    + call to check position: `updateMonsterPosition();`
    + call next animation frame: `requestAnimationFrame(mainloop);`
  + update the position of monster: `function updateMonsterPosition() {...}`
    + init monster speed: `monster.speedX = monster.speedY = 0;`
    + display left arrow key and set speed: `if (inputStates.left) { ctx.fillText("left", 150, 20); monster.speedX = -monster.speed; }`
    + display up arrow key and set speed: `if (inputStates.up) { ctx.fillText("up", 150, 40); monster.speedY = -monster.speed; }`
    + display right arrow key and set speed: `if (inputStates.right) { ctx.fillText("right", 150, 60); monster.speedX = monster.speed; }`
    + display down arrow key and set speed: `if (inputStates.down) { ctx.fillText("down", 150, 80); monster.speedY = monster.speed; }`
    + display space bar: `if (inputStates.space) { ctx.fillText("space bar", 150, 100); }`
    + display mouse position: `if (inputStates.mousePos) {ctx.fillText("x = " + inputStates.mousePos.x + " y = " + inputStates.mousePos.y, 5, 150); }`
    + display mouse buttom down: `if (inputStates.mousedown) {ctx.fillText("mousedown b " + inputStates.mouseButton, 5, 180); monster.speed = 5; }`
    + display mouse button up: `else { monster.speed = 1; }`
    + accelerate speed: `monster.x += monster.speedX; monster.y += monster.speedY;`

+ Example: gamepad enhancements
  + generate animation loop: `var mainloop = function(time) {...}`
    + call to measure FPS: `measureFPS(time);`
    + call to empty canvas: `clearCanvas();`
    + call to update gamepad status: `updateGameStatus();`
    + call to draw object: `drawMyMonster(monster.x, monster.y);`
    + call to check position: `updateMonsterPosition();`
    + call next animation frame: `requestAnimationFrame(mainloop);`
  + update gamepad status: `function updateGameStatus() {...}`
    + call to get new snapshot to the gamepad properties: `scangamepad();`
    + call to check gamepad button states: `checkButtons(gamepad);`
    + call to check joystick: `checkAxes(gamepad);`


### 2.3.8 Discussion and project

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics of discussion:

+ The gamepad API can also be used for serious applications. In our laboratory we remote control a mobile robot with a gamepad and a P2P connection using the WebRTC API. Do you know other applications or demos on the web that use the gamepad API?
+ If you write a nice demo or find any interesting tools relating to the gamepad API, please share in the forum!


#### Optional project:

Have a go at improving the last example:

+ Add gamepad support if you have a gamepad or joystick
+ Make the canvas bigger, add a background if you like (remember you can do this using CSS, or draw something on the whole canvas area instead of clearing it),
+ Improve the appearance of the monster, try animating parts of it,
+ Try to make it "follow" the mouse,
+ Start adding sound effects using skills you learned in Week 1...
etc.

Feel free to experiment and be creative. When attempting more complex ideas, consider collaborating with friends you've made in the discussion forum.


