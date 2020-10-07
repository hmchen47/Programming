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
  + change the CSS top, left, width, and height properties if the divs
  + only solutions: `setInterval(function, ms)` & `setTimeout(function, ms)`: 
  + `setInterval(function, ms)`: run every $n$ milliseconds
  + `setTimeout(function, ms)`: run only once  after $n$ milliseconds (the last step above)

+ [Animation after HTML5](#after-html5)
  + the `<canvas>` element introduced
  + `requestAnimationFrame` API
    + tell the browser to perform an animation
    + request the browser calls a specified function to update an animation before the next repaint
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
    + the basic animation steps: clear-draw-move - `function animationLoop() {...}`
      + using state variables for the position and angle of the character
      + clear the canvas: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
      + draw the character using variables for pos, angle, etc.:  `drawMonster(monsterX, monsterY, monsterAngle, 'green', 'yellow');`
      + move the character by changing pos, angle, size, etc.: `monsterX += 10; monsterX %= canvas.width monsterAngle+= 0.01;`
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
  + schedule a new call to the function passed as first parameter with a timer running in the background
  + issues w/ `setInterval()` and `setTimeout()`
    + `setTimeout()`: probably take slightly longer than the expected timeout period to start executing
    + `setInterval`: the timing not "very" reliable
    + designed long time ago while high precision timers and 60 frames per second animation were not an option
  + __best practice__: avoid using setTimeout for animating in a canvas, except for trivial cases
  + __best practice__: using `requestAnimationFrame` for 60 frames/second animation





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







