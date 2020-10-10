# Week 4: HTML5 Animations


## 4.2 Basic animation techniques


### 4.2.0 Lecture Notes

+ [Animation techniques](421-animation-techniques)
  + basic steps to perform an animation
    + clear the content of the canvas w/ `ctx.clearRect(0, 0, canvasWidth, canvasHeight)` method
    + draw some shapes by using any drawing methods
    + move the shapes by modifying the positions and/or orientation, size, and color
    + repeat the first step
  + perform in a canvas
  + principle: __clear-draw-move-repeat__
  + possible ignore the first step if redrawing the whole canvas content
  
+ [Animations before HTML5](#before-html5)
  + using CSS backgrounds inside `<div>` elements
  + change the CSS top, left, width, and height properties of the divs
  + only solutions:
    + `setInterval(function, ms)`: run every $n$ milliseconds
    + `setTimeout(function, ms)`: run only once  after $n$ milliseconds (the last step above)

+ [Animation after HTML5](#after-html5)
  + the `<canvas>` element introduced
  + `requestAnimationFrame` API
    + tell the browser to perform an animation
    + request the browser calling a specified function to update an animation before the next repaint
    + take a callback as an argument to be invoked before the repaint

+ [`setInterval` method](#423-animating-using-setinterval)
  + syntax: `setInterval(function, ms);`
  + not the recommended way to do 60 frames/second canvas animation
  + still popular on the Web
  + call another function or evaluates an expression at specified intervals of time (in milliseconds)
  + return the unique `id` of the action
  + always stop it by calling the `clearInterval(id)` function w/ the interval identifier as an argument
  + example: animate a DIV using the DOM API
    + before the `<canvas>` element introduced, made games using `<div>` elements
    + animate characters in games by changing their background color, top and left CSS positions
    + using the JavaScript setInterval or setTimeout functions to call repeatedly a function that did the drawing
    + define a `<div>` element to call the custom-defined `render()` method to draw shape every 10ms
    + `render()` method: increment the position of the element by changing its left CSS property
    + call `setInterval` and return an id when click on start button
    + call `clearInterval` to stop the animation as stop button clicked
  + example: animate in a canvas using `setInterval`
    + start the animation loop, change 20 for bigger values by clicking start button: `requestId = setInterval(animationLoop, 20);`
    + draw the animated character: `function drawMonster(x, y, angle, headColor, eyeColor) {...}` w/ `ctx.save()` and `ctx.restore()` at the beginning and end of the function
    + the basic animation steps: clear-draw-move-repeat w/ `function animationLoop() {...}`
      + using state variables for the position and angle of the character
      + clear the canvas: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
      + draw the character using variables for pos, angle, etc.:  `drawMonster(monsterX, monsterY, monsterAngle, 'green', 'yellow');`
      + move the character by changing pos, angle, size, etc.: `monsterX += 10; monsterX %= canvas.width; monsterAngle += 0.01;`
  + issues
    + running several animations simultaneously
      + hard to debug
      + two intervals w/ very different time frame, the longer one difficult to debug
    + probably interrupted by itself to become two simultaneous animations
      + execute the function passed as first parameter every n milliseconds regardless of when the function was last called or how long the function takes to execute
      + the function taking longer than the interval $\to$ queue too many function executions back to back $\to$ unpredictable results
      + e.g., call game loop function every $n$ ms, even if the previous one is not yet finished
  + __best practice__: avoid using `setInterval` for animation in a canvas, except for trivial cases

+ [`setTimeout` method](#424-animating-using-settimeout)
  + syntax: `setTimeout(function, delay);`
  + call function ONCE and AFTER a given amount of time
  + run the function passed as the first parameter only once
  + call at the end of the loop
  + more suitable for doing graphic animation
  + never interrupt an ongoing animation, even if the instructions inside the animation loop take too long
  + not "wait" during the timeout period, the rest of the JavaScript code runs
  + schedule a new call to the function passed as the first parameter w/ a timer running in the background
  + issues w/ `setInterval()` and `setTimeout()`
    + `setTimeout()`: probably take slightly longer than the expected timeout period to start executing
    + `setInterval`: the timing not "very" reliable
    + designed long time ago while high precision timers and 60 frames per second animation were not an option
  + __best practice__: avoid using setTimeout for animating in a canvas, except for trivial cases
  + __best practice__: using `requestAnimationFrame` for 60 frames/second animation

+ [`requestAnimationFrame` method](#425-the-requestanimationframe-api)
  + syntax: `id = requestAnimationFrame(animationLoop)`
  + `cancelAnimationFrame(id)` for stopping an animation
  + similar to `setTimeout`
    + call the function passed as a parameter ONCE
    + fixed target delay, 16.6ms
  + target 60 frames/s
    + browser scheduling a call to the `animationLoop` function
    + scheduling at 1/60th of a second = 16.6ms
    + most monitors unable to display more than 60 frames/sec (FPS)
    + most games acceptable above 30 PFS
    + virtual reality probably reaching 75 PFS to achieve a natural feel
    + some gaming monitors go up to 144 FPS
  + call only once: call again to play a continuous animation
  + advantages
    + much more accurate scheduling: much smaller average error btw the schedule time and the real time if the execution time inside the function smaller than 16.6ms
    + high resolution timer: smaller average time error $\to$ higher resolution $\to$ time-based animation
    + merged multiple animations: bundle animations happening at the same time into a single paint redraw
    + GPU/CPU optimization, battery saved on mobile:
      + js executed but not drawn if not visible
      + animationLoop still executed
  + typical use:
    + `init()` function called after the page loaded
      + get the canvas: `canvas = document.getElementById('myCanvas')`
      + get the context: `ctx = canvas.getContext('2d')`
      + start the animation: `startAnimation()`
    + `startAnimation()` function: `id = requestAnimationFrame(animationLoop);`
    + `animationLoop` function: `function animationLoop(timeStamp)`
      + clear: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
      + draw: `drawShapes(...);`
      + move: `moveShapes(...);`
      + call mainloop again after 16.6 ms (60 frames/s): `id = requestAnimationFrame(animationLoop);`
    + stop animation: `cancelAnimationFrame(requestId);`
  + the 16.6ms delay really accurate?
    + hard to reach
      + animation loop content too complex
      + lower end phone or computer
      + scheduler not at the point
    + solution: time-based animation
  + time-based animation:
    + a technique that comprises measuring the amount of time elapsed between two frames
    + computing the distance in pixels to move objects on screen
    + the visible speed for a human eye remaining constant, even if the frame rate is not
    + independent to the GPU/CPU of the computer or mobile device
    + `timeStamp` parameter in `function animationLoop(timeStamp)`
      + giving a high resolution time
      + measuring deltas btw two consecutive calls of the `animationLoop`
      + knowing exactly, with a sub-millisecond accuracy, the elapsed time btw two frames




### 4.2.1 Animation techniques

In order to perform an animation, we need to:

1. Clear the content of the canvas: this can be done using the `ctx.clearRect(0, 0, canvasWidth, canvasHeight)` method;
2. Draw some shapes: use any of the drawing methods we have seen so far;
3. Move the shapes: modify the position and/or orientation, size and color of the shapes;
4. Repeat (go to step 1).

These are the basic steps for animating objects in a canvas. The order of the steps can be changed (i.e. you can move the shapes before drawing them), but, the principle is the same: __clear-draw-move-repeat__.

Step 1 could be avoided if you redraw the whole canvas content during step 2.


#### Before HTML5

Even before HTML5 and the introduction of the canvas element, people created HTML games. They used CSS backgrounds inside `<div>` elements, and used to change the CSS top, left, width and height properties of the divs to animate graphic images on the screen.

During the late 1990s and early 2000s, JavaScript became increasingly popular. The community created a first 'umbrella term' describing a collection of technologies used together to create interactive and animated Web sites - [DHTML (Dynamic HTML)](https://en.wikipedia.org/wiki/Dhtml). For example, check the [games developed at this time by Brent Silby](https://def-logic.com/) (they all use DHTML).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2wdoc4h')"
    src    ="https://tinyurl.com/yyfoxenr"
    alt    ="A mario like DHTML game"
    title  ="A mario like DHTML game"
  />
</figure>


For animation, the `setInterval(function, ms)` and `setTimeout(function, ms)` methods were the only solutions. Both methods take a function as the first parameter, and a number of milliseconds as the second parameter.

The only difference is that the code provided to `setInterval` will run every n milliseconds whereas the code in `setTimeout` will run only once after n milliseconds (meaning that we will have to repeat a call to `setTimeout` at step 4 above).


#### After HTML5

The methods described above are now completed by a new method that comes with multiple advantages: the `requestAnimationFrame` API.

We will compare the old methods with the new one, and implement the same  example with each of them to highlight the differences.


#### Knowledge check 4.2.1

1. Before HTML5, how did people write games?

  a. It was not possible.<br/>
  b. They used JavaScript for animating + the top, left, etc. CSS properties of HTML elements in the page. This set of tricks was called 'DHTML'.<br/>
  c. They used Flash, as it was not possible to draw graphics or perform an animation using Web standards such as HTML, CSS and JavaScript.<br/>

  Ans: b<br/>
  Explanation: Indeed, before HTML5, and with the arrival of JavaScript, it became possible, using functions such as `setInterval` or `setTimeout`, to modify CSS properties of HTML objects in real time, and in a repeated manner. Animation loops could be implemented using this technique. Now, the HTML5 canvas and the new requestAnimationFrame API make drawing and animating easier, with better performance.


### 4.2.2 Basic animation techniques


<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V001700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/>

[Transcript](https://tinyurl.com/y2vunzbl)


See the [online example](https://jsbin.com/nikimovuza/1/edit?html,output) shown in the video, with source code. ([Local Example - Basic Animations](src/4.2.2-example1.html))

Errata: in the video, we use `speed +=1;` in order to increment the speed of the rectangle each time it bounces (in the `changeColor()` function). This is not correct as `speed` can be negative. The online example fixes this by using `speed += Math.sign(speed) * 1;` instead this will add +1 or -1 depending on the sign of `speed`.


### 4.2.3 Animating using setInterval()

The `setInterval(...)` function is still popular on the Web, and even though this is not the recommended way to do 60 frames/second canvas animation, it is worth understanding how it works.

+ Syntax: `setInterval(function, ms);`

The `setInterval(...)` function calls another function or evaluates an expression at specified intervals of time (in milliseconds), and returns the unique id of the action. You can always stop it by calling the `clearInterval(id)` function with the interval identifier as an argument.


#### Basic example that shows how to animate a DIV using the DOM API

This is how pre-HTML5 games were written. Before the introduction of the canvas element, developers made games using div elements. By changing their background color, top and left CSS positions, it was possible to animate characters in games. The animation was created by calling repeatedly a function that did the drawing, using the JavaScript `setInterval` or `setTimeout` functions.

Please try this [online example](https://jsbin.com/zeqare/1/edit?html,output) (open the html, JavaScript and output tabs) that moves/animates a div using `setInterval`: ([Local Example - DIV w/ DOM API](src/4.2.3-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yxlx8rtj')"
    src    ="https://tinyurl.com/y3hmn3aq"
    alt    ="animate a div using setInterval"
    title  ="animate a div using setInterval"
  />
</figure>


Extract from the source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"animatedDIV"</span><span class="tag">&gt;</span><span class="pln">Animated DIV :-)</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">start</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Start animation</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">stop</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Stop animation</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> elm </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"animatedDIV"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> requestId</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> render</span><span class="pun">(</span><span class="pln">time</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;elm</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">left </span><span class="pun">=</span><span class="pln"> x</span><span class="pun">++</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"px"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> start</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>requestId </strong></span><strong><span class="pun">=</span><span class="pln"> setInterval</span><span class="pun">(</span><span class="pln">render</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> stop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">requestId</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>clearInterval</strong></span><strong><span class="pun">(</span><span class="pln">requestId</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

Here, we define a `<div>` element, (see the online source code for the CSS properties involved), and we use the `setInterval` method (line 17) to call every 10ms the `render()` method that will just increment the position of this element. Notice that since we're using the DOM, the horizontal position of the div is modified by changing its left CSS property.

The call to `setInterval` returns an id we can use to stop the animation, by calling `clearInterval` (line 22).


#### Animate the monster in a canvas, using setInterval

This example is available [online](https://jsbin.com/mimenol/1/edit?html,output). ([Local Example - Canvas w/ SetInterval](src/4.2.3-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yxlx8rtj')"
    src    ="https://tinyurl.com/y2exmper"
    alt    ="animate a monster in a canvas using setInterval"
    title  ="animate a monster in a canvas using setInterval"
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"400"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; Your browser does not support the canvas tag.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;/canvas&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">start</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Start animation</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">stop</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Stop animation</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> monsterX</span><span class="pun">=</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">=</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// 1 - Get the canvas</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// 2 - Get the context</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// 1 - Clear the canvas</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// 2 Draw the monster using variables for pos, angle, etc.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;drawMonster</span><span class="pun">(</span><span class="pln">monsterX</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// 3 Move the monster (change pos, angle, size, etc.)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monsterX </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monsterX </span><span class="pun">%=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;monsterAngle</span><span class="pun">+=</span><span class="pln"> </span><span class="lit">0.01</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> drawMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">,</span><span class="pln"> headColor</span><span class="pun">,</span><span class="pln"> eyeColor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// BEST PRACTICE: SAVE CONTEXT AND RESTORE IT AT THE END</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Moves the coordinate system so that the monster is drawn</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><span class="com">// at position (x, y)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// head</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">headColor</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; ...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// BEST PRACTICE!</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> start</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Start the animation loop, change 20 for bigger values</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;<span style="color: #880000;" color="#880000">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span></span><strong><span class="pln">requestId </span><span class="pun">=</span><span class="pln"> setInterval</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun"><span style="color: #000000;" color="#000000">&nbsp; &nbsp; &nbsp;</span>}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> stop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">requestId</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>clearInterval</strong></span><strong><span class="pun">(</span><span class="pln">requestId</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>


Explanations:

+ _Lines 52-61_: The code for launching and stopping the animation is similar to that from the previous example.
+ _Lines 34-50_: The code that draws the monster is that which we saw earlier when we presented the 2D transformations. Best practice is to save and restore the context at the beginning and end of each function that changes the context.
+ _Lines 21-32_: __The most interesting part is the animation loop__ that implements the basic animation steps: clear-draw-move. In order to make a shape "movable", we use some "state variables" for its position and angle, and we modify them at each iteration (lines 29-32). We will see later on how to modify the value of these variables on user interactions (keyboard, mouse, etc.).


#### Problems with setInterval

While the above example works, there are several reasons not to use `setInterval` for doing smooth animations.


__Running several animations simultaneously__

The `setInterval` function may become hard to debug, particularly if you run several animations simultaneously. For example, if you have two intervals, one running every 100 milliseconds, the other every second, and if you want to debug the second one, the first one will constantly be run at regular intervals, making step by step debugging really difficult.


__A single animation may be interrupted by itself to become two simultaneous animations__

`setInterval` will execute the function passed as first parameter every n milliseconds regardless of when the function was last called or how long the function takes to execute. If the function takes longer than the interval, then `setInterval` might queue too many function executions back to back when the interval is too short, leading to unpredictable results. 

<div style="border: 1px solid red; margin: 10px; padding: 10px;">
<p style="text-align: center;"><em><strong>BEST&nbsp;PRACTICE</strong>: AVOID using <span style="font-family: 'courier new', courier;">setInterval</span></em><em><span style="font-family: 'courier new', courier;"><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">&nbsp;for animating in a canvas, <br>except for trivial cases&nbsp; (change a color every second).</span></span></em></p>
</div>


#### Knowledge check 4.2.3

1. What is the correct syntax for setInterval?

  a. setInterval(function, milliseconds)<br/>
  b. setInterval(milliseconds, function)<br/>

  Ans: a<br/>
  Explanation: The first answer is correct. The second parameter is the length of the interval of time, in millisonds, between consecutive calls to the function passed as first parameter. setInterval can be useful for simple animations, where timing and performance are not critical. Example: display a clock that is updated every second, etc.



### 4.2.4 Animating using `setTimeout()`

One thing you should always remember about using `setInterval`: if we set number of milliseconds at - let’s say 20ms - it will call our game loop function EACH 20ms, <i>even if the previous one is not yet finished</i>. This may lead to many problems (incomplete rendering, etc.).

That's where we can use another function: 

+ `setTimeout(function, ms);`

This function works like `setInterval(...)` with one difference: it calls your function ONCE and _AFTER a given amount of time_.


#### Example of the monster animated in a canvas with setTimeout

Example of the animated monster is [online](https://jsbin.com/gogafu/1/edit?html,output) (open the JavaScript, console and output tabs): ([Local Example - Animation w/ setTimeout](src/4.2.4-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y3kp455a')"
    src    ="https://tinyurl.com/y2ja2xsb"
    alt    ="monster animated with setTimeout"
    title  ="monster animated with setTimeout"
  />
</figure>


This is similar to the previous example except that we called `setTimeout(function, delay)` instead of setInterval(function, period). <strong>As setTimeout runs the function passed as the first parameter only once, <span style="color: magenta;">we also have to call it at the end of the loop</span>.</strong>

Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - Clear</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2 Draw</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;drawMonster</span><span class="pun">(</span><span class="pln">monsterX</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 3 Move</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;monsterX </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;monsterX </span><span class="pun">%=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;monsterAngle</span><span class="pun">+=</span><span class="pln"> </span><span class="lit">0.01</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// call mainloop again after 20ms</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>requestId </strong></span><strong><span class="pun">=</span><span class="pln"> setTimeout</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> start</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Start the animation loop, change 20 for bigger</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// values</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>requestId </strong></span><strong><span class="pun">=</span><span class="pln"> setTimeout</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> stop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">requestId</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>clearTimeout</strong></span><strong><span class="pun">(</span><span class="pln">requestId</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>


This function is certainly more suitable for doing graphic animation, such as for writing an HTML5 game. It will never interrupt an ongoing animation, even if the instructions inside the animation loop take too long.


#### Problems with `setInterval()` and `setTimeout()`

`setTimeout` does not "wait"  during the timeout period. It lets the rest of the JavaScript code run. It schedules a new call to the function passed as first parameter with a timer running in the background. This might cause it to take slightly longer than the expected timeout period to start executing. 

This problem also occurs with `setInterval`, the timing is not "very" reliable. If you plan to run a function every 20ms, and if you measure precisely the real timing, sometimes you will discover big differences between what is scheduled and what is performed. This is because these methods were designed a long time ago, when high precision timers and 60 frames per second animation were not an option.

Here comes [the requestAnimationFrame API](https://www.w3.org/TR/animation-timing/), a very good companion to the canvas API!

<div style="border: 1px solid red; margin: 10px; padding: 10px;">
<p style="text-align: center;"><em><strong>BEST&nbsp;PRACTICE</strong>: AVOID using <span style="font-family: 'courier new', courier;">setTimeout<span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;"> for animating in a canvas, except for trivial cases. </span></span></em></p>
<p style="text-align: center;"><span style="color: #ff0000;"><strong><em><span style="font-family: 'courier new', courier;"><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">For 60 frames/second animation, use <span style="font-family: 'courier new', courier;">requestAnimationFrame</span>!</span></span></em></strong></span></p>
</div>


#### Knowledge check 4.2.4

`setInterval(function, milliseconds);`

`setTimeout(function, milliseconds);`

1. Regarding the two lines of code above, which statement is true?

  a. `setTimeout` will call the function only once, after a delay corresponding to the value passed as second parameter.<br/>
  b. They will produce the same result: call the function passed as first parameter every interval of time passed as the second parameter (in milliseconds)<br/>

  Ans: a<br/>
  Explanation: `setTimeout` will call the function only once, after a delay passed as second parameter. As `setTimeout` runs the function passed as the first parameter only once, in order to implement an animation loop, we have to call it again at the end of the loop.



### 4.2.5 The requestAnimationFrame API

The `requestAnimationFrame(animationLoop)` is very similar to `setTimeout`:

+ __It targets 60 frames/s__: `requestAnimationFrame` asks the browser to schedule a call to the `animationLoop` function passed as parameter in 1/60th of a second (equivalent to 16.6ms). Keep in mind that most monitors cannot display more than 60 frames per second (FPS). Note that whether humans can tell the difference among high frame rates depends on the application, most games are acceptable above 30 FPS, and virtual reality might require 75 FPS to achieve a natural feel. Some gaming monitors go up to 144 FPS (pro players in e-sport train themselves at Counter Strike with a 150 frames/s rate).
+ __It calls the function only ONCE__, so if you want a continuous animation, like with `setTimeout`, you need to call again `requestAnimationFrame` at the end of the `animationLoop` function.

It has, however, several advantages over `setInterval` and `setTimeout`:

+ __The scheduling is much more accurate:__ if the code inside the function can be executed in less than 16.6ms, then the average error between the scheduled time and the real time will be much smaller than with the old functions.
+ __High resolution timer:__ even if this difference is small, the function that is called after 16.6ms has an extra parameter that is a high resolution time, very useful for writing games that do [time-based animation](https://blog.sklambert.com/using-time-based-animation-implement/). Time-based animation will be studied in detail in the HTML5 Part 2 course at W3Cx. It is a technique that comprises measuring the amount of time elapsed between two frames, then computing the distance in pixels to move objects on screen so that the visible speed for a human eye remains constant, even if the frame rate is not.
+ __Multiple animations are merged:__ browsers can bundle animations happening at the same time into a single paint redraw (thus happening faster/with less CPU cycles), solving the problems that can occur with simultaneous `setInterval` calls.
+ __CPU/GPU optimization, battery saved on mobiles:__  if the JavaScript execution is occurring in a tab/window which is not visible, it doesn’t have to be drawn. However the animation loop is still executed (objects will be moved, not drawn). This is the same when a mobile phone or tablet screen is black or if the application is put in background.


#### Typical use

You will note that `requestAnimationFrame(function)` is used like `setTimeout(function, delay)`. A call to `requestAnimationFrame` just asks the browser to call the function passed as a parameter ONCE, __and the target delay is fixed__, and corresponds to a 60 frames/s frame rate (16.6ms). Notice that an id is used for stopping an animation with `cancelAnimationFrame(id)`.

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - Get the canvas</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2 - Get the context</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 3 - start the animation</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;startAnimation</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">&nbsp;<strong>var</strong></span><strong><span class="pln"> id</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">&nbsp;function</span><span class="pln"> animationLoop</span><span class="pun">(<span style="line-height: 25.6000003814697px;">timeStamp</span>)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - Clear</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2 Draw</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;drawShapes</span><span class="pun">(...);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 3 Move</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;moveShapes</span><span class="pun">(...);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// call mainloop&nbsp; again after 16.6ms (corresponds to 60 frames/second)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>id </strong></span><strong><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">&nbsp;function</span><span class="pln"> startAnimation</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>id </strong></span><strong><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="kwd">function</span><span class="pln"> stopAnimation</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">id</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>cancelAnimationFrame</strong></span><strong><span class="pun">(</span><span class="pln">id</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>


#### Example: animate the monster with requestAnimationFrame

[Online example at JsBin](https://jsbin.com/jukoniz/1/edit?html,output) ([Local Example - requestAnimationFrame](src/4.2.5-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y2l9blgo')"
    src    ="https://tinyurl.com/y5pq67hz"
    alt    ="monster animated using requestAnimationFrame"
    title  ="monster animated using requestAnimationFrame"
  />
</figure>


Extract from source code, compare to the previous example that used setInterval()

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">(timeStamp)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 1 - Clear</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 2 - Draw</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawMonster</span><span class="pun">(</span><span class="pln">monsterX</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 3 - Move</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; monsterX </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; monsterX </span><span class="pun">%=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; monsterAngle</span><span class="pun">+=</span><span class="pln"> </span><span class="lit">0.01</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// call mainloop again after 16.6 ms (60 frames/s)</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>requestId </strong></span><strong><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> start</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// Start the animation loop, targets 60 frames/s, this </span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="com">&nbsp; &nbsp; // calls animationLoop only ONCE!</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>requestId </strong></span><strong><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> stop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">requestId</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>cancelAnimationFrame</strong></span><strong><span class="pun">(</span><span class="pln">requestId</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Notice that calling `requestAnimationFrame(animationLoop)` at line 19, and after that from within the loop at line 14, asks the browser to call the `animationLoop` function so that the delta between calls will be <strong>as close as possible to 16.6ms  (this corresponds to 1/60th of a second)</strong>.


#### Is the 16.6ms delay really accurate? Can we trust it?

This target may be hard to reach if:

+ The animation loop content is too complex,
+ The target device that runs the animation is a low end phone or an old computer,
+ The scheduler may be a bit late or a bit in advance (even if this kind of error is much smaller with `requestAnimationFrame` than with `setInterval` or `setTimeout`).

Many HTML5 games perform what we call a "time-based animation". For this, we need an accurate timer that will tell us the elapsed time between each animation frame.

Depending on this time, we can compute the distances that must be achieved by each object on the screen in order to move at a constant speed (for a human eye), independently of the CPU or GPU of the computer or mobile device that is running the game.

The `timeStamp` parameter of the `animationLoop` function (line 1 in the above code) is useful for exactly that: it gives a high resolution time. By measuring deltas between two consecutive calls of the `animationLoop`, we will know exactly, with a sub-millisecond accuracy, the elapsed time between two frames.

Using time-based animation, and more generally, using the canvas element for writing HTML5 games, is part of the W3Cx HTML5 Apps and Games course.

Current [support](https://caniuse.com/#feat=requestanimationframe) is really good and all modern browsers support this API.


#### Knowledge check 4.2.5

1. `requestAnimationFrame(function);`

  `requestAnimationFrame` asks the browser to call the function passed as a parameter only once, and tries to call it after 16.6ms:

  a. Yes, this is true<br/>
  b. No, it will call the function automatically every 16.6ms, resulting in a 60 frames/second smooth animation. It works like setInterval, but is more efficient.<br/>

  Ans: a<br/>
  Explanation: A call to `requestAnimationFrame` just asks the browser to call the function passed as a parameter ONCE, and the target delay is fixed, and corresponds to a 60 frames/s frame rate (16.6ms). In an animation loop, it is necessary to call again `requestAnimationFrame` at the end of the loop to ask for another frame of animation. Similarly to `setTimeout`...



### 4.2.6 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ Why do we always mention "smooth animation" with 60 frames/s (note that in Europe, it was 50 frames/s for a long time)?
+ When should we use setTimeout or setInterval instead of the brand new super duper requestAnimationFrame? Please take a guess or if you know why, try to give examples and share your experiences in the forum. The optional projects below will help.


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy):__ You created a monster, or a small drawing during Week 3: now please animate it! For example, make it move horizontally on the screen and bounce when it hits a vertical border.
+ __Project 2 (easy):__ Change the color of your drawing every 0.5s. Professionals would do this using the timeStamp parameter passed to the function called by requestAnimationFrame, and do some computations, etc. But this is for advanced users. Others will simply use requestAnimationFrame for the smooth shape movements at 60 frames/s (using translate, rotate and increments, as shown in the course), and will use setInterval, for example for calling another function every 0.5s, or every second, that could change a color, a speed, etc.


  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
      onclick="window.open('https://tinyurl.com/y2xzkdb8')"
      src    ="https://tinyurl.com/y3s7dpws"
      alt    ="Transmogify monster"
      title  ="Transmogify monster"
    />
  </figure>

  [Try the "Transmogrify monster" on JsBin](https://jsbin.com/wucowah/1/edit?html,output), by Bill Graham. Uses color changes + bounces on vertical borders.

+ __Project 3 (easy):__ Run several animations at the same time (beware not to clear the canvas in all of them during each animation loop - one clear is enough). You can also have multiple calls to setInterval. Try and learn from experience. Then discuss your findings in the forum.

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
      onclick="window.open('https://tinyurl.com/y2xzkdb8')"
      src    ="https://tinyurl.com/y25a3vyk"
      alt    ="Bouncing monster with motion blur"
      title  ="Bouncing monster with motion blur"
    />
  </figure>

  [Try the above example on CodePen](https://codepen.io/dilipporwal/pen/yNKJOM) (by Dilip Dorwal). It uses animation and motion blur.

+ __Project 4 (easy):__ Implement motion blur for free! Instead of using clearRect(...) for clearing the canvas content, please comment this line and replace it by drawing a filled rectangle of the size of the canvas, that has some transparency. Use the following two lines, for example:

  ```js
  //ctx.clearRect(0, 0, canvas.width, canvas.height);
  // Next line sets the color for filled shapes.
  // We will use transparency here to create a blurred effect.
  // Try different values for the last param (transparency): 0.05, 0.01, etc.

  ctx.fillStyle = "rgba(0, 240, 240, 0.2)";

  ctx.fillRect (0, 0, width, height);
  //It will erase the canvas content using color defined above.
  ```




