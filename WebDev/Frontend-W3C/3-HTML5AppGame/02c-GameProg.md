# Module 2: Game programming with HTML5 section


## 2.3 A simple game framework


### 2.3.1 A game framework skeleton

We are going to develop a game - not all at once, let's divide the whole job into a series of smaller tasks. The first step is to create a foundation or basic structure.

Let's start by building the skeleton of a small game framework, based on [the Black Box Driven Development in JavaScript](https://hacks.mozilla.org/2014/08/black-box-driven-development-in-javascript/) methodology. In other words: a game framework skeleton is a simple object-based model that uses encapsulation to expose only useful methods and properties.

We will evolve this framework throughout the lessons in this course, and cut it in different files once it becomes too large to fit within one single file.

Here is the starting point:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> GF </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">time</span><span class="pun">){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//Main function, called each frame</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> start </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Our GameFramework returns a public API visible from outside its scope</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; // Here we only expose the start method, under the "start" property name.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; start</span><span class="pun">:</span><span class="pln"> start</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>

With this skeleton, it's very easy to create a new game instance:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> game </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> GF</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Launch the game, start the animation loop, etc.</span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">game</span><span class="pun">.</span><span class="pln">start</span><span class="pun">();</span></strong></li>
</ol></div>


#### Examples

__Let's put something into the mainLoop function, and check if it works__

Try this [online example at JSBin](https://jsbin.com/tatowa/edit), with a new `mainloop`:  (check the JavaScript and output tabs). This page should display a different random number every 1/60 second. We don't have a real game yet, but we're improving our game engine :-)

[Local Demo](src/02b-example04.html)

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">time</span><span class="pun">){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// main function, called each frame</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// call the animation loop every 1/60th of second</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
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
    onclick= "window.open("https://bit.ly/3xuD14p")"
    src    = "https://bit.ly/3q2qd2v"
    alt    = "screenshot of the example that displays 60 frames/s"
    title  = "screenshot of the example that displays 60 frames/s"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">&nbsp;&nbsp; // vars for counting frames/s, used by the measureFPS function</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> frameCount </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> lastTime</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> fpsContainer</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> fps</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> measureFPS </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">newTime</span><span class="pun">){</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// test for the very first invocation</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">lastTime </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;lastTime </span><span class="pun">=</span><span class="pln"> newTime</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// calculate the delta&nbsp;between last &amp; current frame</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> diffTime </span><span class="pun">=</span><span class="pln"> newTime </span><span class="pun">-</span><span class="pln"> lastTime</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">diffTime </span><span class="pun">&gt;=</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;fps </span><span class="pun">=</span><span class="pln"> frameCount</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;frameCount </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;lastTime </span><span class="pun">=</span><span class="pln"> newTime</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// and display it in an element we appended to the </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// document in the start() function</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;fpsContainer</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">'FPS: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> fps</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;frameCount</span><span class="pun">++;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div><br>

Now we can call the `measureFPS` function from inside the animation loop, passing it the current time, given by the high resolution timer that comes with the `requestAnimationFrame` API:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><strong><span class="pln">time</span></strong><span class="pun">){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">//&nbsp;compute FPS,&nbsp;called each frame, uses the high resolution time parameter&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; //&nbsp;given&nbsp;by the browser that implements the requestAnimationFrame API</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>measureFPS</strong></span><strong><span class="pun">(</span><span class="pln">time</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// call the animation loop every 1/60th of second</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>

And the `<div>` element used to display FPS on the screen is created in this example by the `start()` function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> start </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// adds a div for displaying the fps value</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; fpsContainer </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'div'</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">fpsContainer</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div>


__Hack:  achieving more than 60 fPS? It's possible but to be avoided except in hackers' circles!__

We also know methods of implementing loops in JavaScript which achieve even more than 60fps (this is the limit using `requestAnimationFrame`).

My favorite hack uses the onerror callback on an `<img>` element like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln">&nbsp;mainloop</span><span class="pun">(</span><span class="pun">){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> img </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; img</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="pun"><span style="line-height: 23.2727px;">mainloop</span>;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; img</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">'data:image/png,'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

What we are doing here, is creating a new image on each frame and providing invalid data as a source of the image. The image cannot be displayed properly, so the browser calls the onerror event handler that is the mainloop function itself, and so on.

Funny right? Please try this and check the number of FPS displayed with this [JSBin example](https://jsbin.com/notupe/edit).

[Local Demo](src/02b-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3xuD14p")"
    src    = "https://bit.ly/3wtWW3n"
    alt    = "Screenshot of example with 4441 FPS displayed"
    title  = "Screenshot of example with 4441 FPS displayed"
  />
</figure>


Source code extract of this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// main function, called each frame </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; measureFPS</span><span class="pun">(+(</span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Date</span><span class="pun">()));</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// call the animation loop every LOTS of seconds using previous hack method</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> img </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; img</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> mainLoop</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; img</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">'data:image/png,'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div><br>


#### Notes for 2.3.1 A game framework skeleton

+ Game framework skeleton
  + based on the [Black Box Driven Development](https://hacks.mozilla.org/2014/08/black-box-driven-development-in-javascript/)
    + principle 1: modularize everything
    + principle 2: expose only public methods
    + principle 3: use composition over inheritance
  + a simple objected-based model using encapsulation to expose only useful methods and properties
  + cut into several files once becoming too large to fit into one single file

+ Example: game framework starting point
  + generate game framework: `var GF = function() {...}`
    + create animation loop: `var mainloop = function() { requestAnimationFrame(mainloop); };`
    + init game loop: `var star = function() { requestAnimationFrame(mainloop); };`
    + return a public API: `return { start: start };`
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
    + $Delta$:
      + used in mathematics as an abbreviation for measuring the change in some object
      + how quickly the mainloop running
      + the maimum spped, rate of change, at which the game display will be updated
      + rate of change able to be measured in frames per second (fps)
    + $\delta$
      + determin the achievable frame rate
      + the shorter the delta (in ms), the faster the possible rate of change (in fps)

+ Example: counting frames/s
  + delcare variables: `var frameCount = 0; var lastTime; var fpsContainer; var fps;`
  + measure FPS: `var measureFPS = function(newTime) {...}`
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
  + initialize the game framework: `var start = function() {...}`
  + add div container: `fpsContainer = document.createElement('div');`
  + add div contain to page: `document.body.appendChild(fpsContainer);`
  + init the animation loop: `requestAnimationFrame(mainloop);`

+ Example: image element w/ error callback
  + create animation loop: `function mainloop {...}`
  + delcare variable: `var img = new image;`
  + assign error callback: `img.onerror = mainloop;`
  + assign image source: `img.src = 'data:image/png,' + Math.random();`

+ Example: check the number of FPS
  + create animation loop: `var mainloop = function() {...}`
  + measure FPS w/ current time: `measureFPS(+(new Date()));`
  + generate new image: `var img = new Image();`
  + handle error: `img.error = mainloop;`
  + assign image source: `img.src = 'data.image/pbg' + Math.random();`


#### Knowledge check 2.3.1

1. How do we measure the time between two consecutive animations?

  a. We use the parameter passed by the browser to the animation loop. This is a requestAnimationFrame API feature.<br>
  a. We use the Date() JavaScript object, that returns the current time.<br>

  Ans: <br/>
  Explanation: 
  





