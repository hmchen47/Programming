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

  a. We use the parameter passed by the browser to the animation loop. This is a `requestAnimationFrame` API feature.<br>
  a. We use the Date() JavaScript object, that returns the current time.<br>

  Ans: <span style="color: magenta;">a</span>, xb<br/>
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
    onclick= "window.open("https://bit.ly/2UeN679")"
    src    = "https://bit.ly/3xrMtFt"
    alt    = "Small monster drawn in a canvas"
    title  = "Small monster drawn in a canvas"
  />
</figure>


HTML code (declaration of the canvas):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">Draw a monster in a canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"200"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;&lt;/canvas&gt;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

The canvas declaration is at _line 8_. Use attributes to give it a `width` and a `height`, but unless you add some CSS properties, you will not see it on the screen because it's transparent!

Let's use CSS to reveal the canvas, for example, add a 1px black border around it:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">canvas </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

And here is a reminder of best practices when using the canvas, as described in the HTML5 Part 1 course:

1. Use a function that is called AFTER the page is fully loaded (and the DOM is ready), set a pointer to the canvas node in the DOM.
1. Then, get a 2D graphic context for this canvas (the `context` is an object we will use to draw on the canvas, to set global properties such as color, gradients, patterns and line width).
1. Only then can you can draw something,
1. Do not forget to use global variables for the canvas and context objects. I also recommend keeping the width and height of the canvas somewhere. These might be useful later.
1. For each function that will change the context (color, line width, coordinate system, etc.), start by saving the context, and end by restoring it.

Here is JavaScript code which implements those best practices:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// useful to have them as global variables</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> <g class="gr_ gr_126 gr-alert gr_spell gr_disable_anim_appear ContextualSpelling ins-del multiReplace" id="126" data-gr-id="126">ctx</g></span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Called AFTER the page has been loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Often useful</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; w </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; h </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Important, we will draw with this object</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Ready to go!</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Try to change the parameter values to move</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// the monster</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; drawMyMonster</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> drawMyMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Draw a big monster!</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Head</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// BEST practice: save the context, use 2D transformations</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Translate the coordinate system, draw relative to it</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// (0, 0) is the top left corner of the monster.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Eyes</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">65</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Nose</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">45</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Mouth</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">35</span><span class="pun">,</span><span class="pln"> </span><span class="lit">84</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Teeth</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">38</span><span class="pun">,</span><span class="pln"> </span><span class="lit">84</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">52</span><span class="pun">,</span><span class="pln"> </span><span class="lit">84</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// BEST practice: restore the context</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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
    onclick= "window.open("https://bit.ly/2UeN679")"
    src    = "https://bit.ly/35v4GpW"
    alt    = "Screenshot of a trembling monster in a 60 f/s animation"
    title  = "Screenshot of a trembling monster in a 60 f/s animation"
  />
</figure>


HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Trembling monster in the Game Framework</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"200"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;&lt;/canvas&gt;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

JavaScript complete code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Inits</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> game </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> GF</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; game</span><span class="pun">.</span><span class="pln">start</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// GAME FRAMEWORK STARTS HERE</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> GF </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// Vars relative to the canvas</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> <g class="gr_ gr_121 gr-alert gr_spell gr_disable_anim_appear ContextualSpelling ins-del multiReplace" id="121" data-gr-id="121">ctx</g></span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">;</span></strong><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> measureFPS </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">newTime</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Clears the canvas content</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> clearCanvas</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Functions for drawing the monster and perhaps other objects</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawMyMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">time</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Main function, called each frame </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; measureFPS</span><span class="pun">(</span><span class="pln">time</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>&nbsp;</strong></span><strong><span class="com">// Clear the canvas</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>clearCanvas</strong></span><strong><span class="pun">();</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// Draw the monster</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>drawMyMonster</strong></span><strong><span class="pun">(</span><span class="lit">10</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()*</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()*</span><span class="lit">10</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Call the animation loop every 1/60th of second</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> start </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// Canvas, context etc.</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas </strong></span><strong><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// often useful</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; w </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span><span class="pln"> </span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; h </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span><span class="pln"> </span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// important, we will draw with this object</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Start the animation</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">//our GameFramework returns a public API visible from outside its scope</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;start</span><span class="pun">:</span><span class="pln"> start</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span></li>
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
  4. do not forget to use global variables for the canvas for the canvas and context object, in particular, the width and height of the cnavas
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
      + draw the frame:  `ctx.translate(0, 0, 100, 100);`
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
      + generate main loop: `var mainloop = function(time) {...}`
        + call to measure FPS: `measureFPS(time);`
        + clear the canvas: `clearCanvas();`
        + call to draw monster: `drawMyMonster(10+Math.random()*10, 10+Math.random()*10);`
        + call to animate: `requestAnimateFrame(mainloop);`
      + [init the GF](#startGF) w/ 
        + [init canvas](#initCanvas) w/o drawing monster
        + start the animation: `requestAnimationFrame('2d');`
      + return [public API](#publicAPI)


### 2.3.3 User interaction and event handling

#### Input & output: how do events work in Web apps & games?

__HTML5 events__

There is no input or output in JavaScript. We treat events caused by user actions as inputs, and we manipulate the DOM structure as output. Usually in games, we will maintain state variables representing moving objects like the position and speed of an alien ship, and the animation loop will refer to these variables in determining the movement of such objects.

In any case, the events are called DOM events, and we use the DOM APIs to create _event handlers_.

__How to listen to events__

There are three ways to manage events in the DOM structure. You could attach an event inline in your HTML code like this:

__Method #1: declare an event handler in the HTML code__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"someDiv"</span><span class="pln"> </span><strong><span class="atn">onclick</span></strong><span class="pun">=</span><span class="atv">"</span><span class="pln">alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">)</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln"> content of the div </span><span class="tag">&lt;/div&gt;</span></li>
</ol></div><br>

This method is very easy to use, but it is not the recommended way to handle events. Indeed, It works today but is _deprecated_ (will probably be abandoned in the future). Mixing 'visual layer' (HTML) and 'logic layer' (JavaScript) in one place is really bad practice and causes a host of problems during development.

__Method #2: attach an event handler to an HTML element in JavaScript__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'someDiv'</span><span class="pun">).</span><strong><span class="pln">onclick </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str"><g class="gr_ gr_54 gr-alert gr_spell gr_disable_anim_appear ContextualSpelling ins-del multiReplace" id="54" data-gr-id="54">'clicked</g>!'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

This method is fine, but  you will not be able to attach multiple _listener_ functions. If you need to do this, use the version shown below.

__Method #3: register a callback to the event listener with the `addEventListener` method (preferred  method)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'someDiv'</span><span class="pun">).</span><strong><span class="pln">addEventListener</span></strong><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div><br>

Note that the third parameter describes whether the _callback_ has to be called during the captured phase. This is not important for now, just set it to false.


#### Details of the DOM event are passed to the event listener function

When you create an event listener and attach it to an element, the listener will create an `event` object to describe what happened. This object is provided as a parameter of the callback function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">element</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str"><g class="gr_ gr_64 gr-alert gr_spell gr_disable_anim_appear ContextualSpelling ins-del multiReplace" id="64" data-gr-id="64">'click</g>'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><strong><span class="kwd">event</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// now you can use event object inside the callback</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
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
    + maintaining state variables respenting moving objects like the position and speed of an alient ship
    + the animation loop refers to the variables in determining the movement of suchg objects
  + listeming the event
    + declare an event handler in the HTML code
      + example: `<div id="someDiv" onclick="alert('clicked!');"> content of the div</div>`
      + easy to use but not recommended $\to$ deprecated
      + bad practice ([separation of concerns](2.3.3 User interaction and event handling)): mixing 'visual layer' (HTML) and 'logical layer' (JavaScript)
    + attach an event handler to an HTML element in JavaScript
      + example: `document.getElementByID('someDiv').onclick = function() { alert('clicked!'); }`
      + not able to attach multiple listener functions
    + register a callback tot he event listener w/ the `addEventListener` method (preferred method)
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str"><g class="gr_ gr_84 gr-alert gr_spell gr_disable_anim_appear ContextualSpelling ins-del multiReplace" id="84" data-gr-id="84">'keydown</g>'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Left arrow was pressed</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div><br>

At line 2, the key code of 37 corresponds to the left arrow key.

You can try key codes with this [interactive example](http://www.asquare.net/javascript/tests/KeyCode.html), and here is a list of keyCodes (from [CSS Tricks](https://css-tricks.com/snippets/javascript/javascript-keycodes/)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/2SH2BEt")"
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
    onclick= "window.open("https://bit.ly/2SH2BEt")"
    src    = "https://bit.ly/3q6zPJI"
    alt    = "trembling monster with multiple key press management."
    title  = "trembling monster with multiple key press management."
  />
</figure>


And here is the complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Inits</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> game </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> GF</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; game</span><span class="pun">.</span><span class="pln">start</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// GAME FRAMEWORK STARTS HERE</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> GF </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">...&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong>// vars for handling inputs</strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> inputStates </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> measureFPS </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">newTime</span><span class="pun">){</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Clears the canvas content</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> clearCanvas</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Functions for drawing the monster and perhaps other objects</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> drawMyMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">time</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Main function, called each frame </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;measureFPS</span><span class="pun">(</span><span class="pln">time</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Clears the canvas</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;clearCanvas</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Draws the monster</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;drawMyMonster</span><span class="pun">(</span><span class="lit">10</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()*</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()*</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong> &nbsp;&nbsp;</strong></span><strong>// check inputStates</strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">left</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"left"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">up</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"up"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">right</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"right"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">80</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">down</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"down"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">120</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">space</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"space bar"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">140</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></strong><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Calls the animation loop every 1/60th of second</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> start </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Important, we will draw with this object</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Default police for text</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">font</span><span class="pun">=</span><span class="str">"20px Arial"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Add the listener to the main, window object, and update the states</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">){</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">left </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">38</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">up </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">39</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">right </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">40</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">down </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">32</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">space </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// If the key&nbsp;is released, change the states object </span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">){</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">left </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">38</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">up </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">39</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">right </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">40</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">down </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">32</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">space </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Starts the animation</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// our GameFramework returns a public API visible from outside its scope</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;start</span><span class="pun">:</span><span class="pln"> start</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>

You may notice that on some computers / operating systems, it is not possible to simultaneously press the up and down arrow keys, or left and right arrow keys, because they are mutually exclusive. However space + up + right should work in combination.


#### Notes for 2.3.4 Adding key listeners

+ Keyboard related events
  + the code of the key passed tot he listener function once key-board event fired
  + example: `window.addEventListener('keydown', function(evt) { if (event.keyCode === 37) { // left arrow pressed } }; flase);`
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
    + add tests to checck which keys are down within main loop

+ Example: handling multiple keyboard-related events
  + [init page](#newGF) after DOM ready
  + [generate game framework](#genGF)
    + declare dictionary to handle inputs: `var inputStates = {};`
    + [measure FPS](#measureFPS)
    + [clear canvas](#clearCanvas)
    + [draw monster](#drawMonster)
    + check input states<a name="chkInput"></a>:
      + left arrow key: `if (inputStates.left) { ctx.fillText("left", 150, 20); }`
      + up arrow key: `if (inputStates.up) { ctx.fillText("up", 150, 50); }`
      + right arrow key: `if (inputStates.right) { ctx.fillText("right", 150, 80); }`
      + down arrow key: `if (inputStates.down) { ctx.fillText("down", 150, 120); }`
      + space bar: `if (inputStates.space) { ctx.fillText("space bar", 140, 150); }`
    + call animation loop: `rrequestAnimationFrame(mainloop);`
  + [init game framework](#initGF) w/ input handling
    + set 2d context: `ctx = canvas.getContext('2d');`
    + set font: `ctx.font = "20px Arial";`
    + add event listener for key pressed<a name="keyDownCode"></a>: `window.addEventListener('keydown', function(evt) {...}), flase);`
      + left arrow key: `if (evt.keyCode === 37) { inputStates.left = true; }`
      + up arrow key: `else if (evt.keyCode === 38) { inputStates.up = true; }`
      + right arrow key: `else if (evt.keyCode === 39) { inputStates.right = true; }`
      + down arrow key: `else if (evt.keyCode === 40) { inputStates.down = true; }`
      + space bar: `else if (evt.keyCode === 32) {inputStates.space = true; }`
    + add event listener for key released<a name="keyUpCode"></a>: `window.addEventListener('keyup', function(evt) {...}), flase);`
      + left arrow key: `if (evt.keyCode === 37) { inputStates.left = flase; }`
      + up arrow key: `else if (evt.keyCode === 38) { inputStates.up = flase; }`
      + right arrow key: `else if (evt.keyCode === 39) { inputStates.right = flase; }`
      + down arrow key: `else if (evt.keyCode === 40) { inputStates.down = flase; }`
      + space bar: `else if (evt.keyCode === 32) {inputStates.space = false; }`
    + start amimation: `requestAnimationFrame(mainloop);`
    + return [public API](#publicAPI)


### 2.3.5 Adding mouse listeners


#### A few reminders

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open("https://bit.ly/35zjZh9")"
    src    = "https://bit.ly/3iRXVGv"
    alt    = "A few remindersa schema of mouse internals"
    title  = "A few remindersa schema of mouse internals"
  />
</figure>

Working with mouse events requires detecting whether a mouse button is up or down, identifying that button, keeping track of mouse movement, getting the x and y coordinates of the cursor, etc.

Special care must be taken when acquiring mouse coordinates because the HTML5 canvas has default (or directed) CSS properties which could produce false coordinates. The trick to get the right x and y mouse cursor coordinates is to use this method from the canvas API:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// necessary to take into account CSS boudaries</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getBoundingClientRect</span><span class="pun">();</span></li>
</ol></div><br>

The width and height of the `rect` object must be taken into account. These dimensions correspond to the padding / margins / borders of the canvas. See how we deal with them in the `getMousePos()` function in the next example.

Here is an [online example at JSBin](https://jsbin.com/metavu/edit) that covers  all cases correctly.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/35zjZh9")"
    src    = "https://bit.ly/3wGu1sL"
    alt    = "screenshot of a JsBin example that shows the mouse position + button pressed"
    title  = "screenshot of a JsBin example that shows the mouse position + button pressed"
  />
</figure>


Move the mouse over the canvas and press or release mouse buttons. Notice that we keep the state of the mouse (position, buttons up or down) as part of the `inputStates` object, just as we do with the keyboard (per previous lesson).

Below is the JavaScript source code for this small example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> inputStates </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>inputStates</strong></span><strong><span class="pun">.</span><span class="pln">mousePos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> message </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Mouse position: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">','</span><span class="pln"> </span><span class="pun">+</span><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>inputStates</strong></span><strong><span class="pun">.</span><span class="pln">mousedown </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>inputStates</strong></span><strong><span class="pun">.</span><span class="pln">mouseButton </span><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">button</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> message </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Mouse button "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">button </span><span class="pun">+</span><span class="pln"> </span><span class="str">" down at position: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln">&nbsp; </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">','</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseup'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>inputStates</strong></span><strong><span class="pun">.</span><span class="pln">mousedown </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> message </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Mouse up at position: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">','</span><span class="pln"> </span><span class="pun">+</span><span class="pln">&nbsp; &nbsp; &nbsp; </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">'18pt Calibri'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'black'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="pln">message</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">25</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="com">// necessary to take into account CSS boudaries</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getBoundingClientRect</span><span class="pun">();</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;x</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientX </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">left</span><span class="pun">,</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;y</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientY </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">top</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
</ol></div>


#### Making an object follow the mouse cursor

Try this [example at JsBin](https://jsbin.com/soduko/edit?js,output)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/35zjZh9")"
    src    = "https://bit.ly/2TEFgmZ"
    alt    = "A rectangle that follows the mouse cursor"
    title  = "A rectangle that follows the mouse cursor"
  />
</figure>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">x</span><span class="pun">:</span><span class="lit">40</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">:</span><span class="lit">40</span><span class="pun">,</span><span class="pln"> rayon</span><span class="pun">:</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">:</span><span class="lit">80</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">:</span><span class="lit">80</span><span class="pun">,</span><span class="pln"> v</span><span class="pun">:</span><span class="lit">1</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> mousepos </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">x</span><span class="pun">:</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">:</span><span class="lit">0</span><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; height </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;mousepos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; mainloop</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> mainloop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1) clear screen</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2) move object</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> dx </span><span class="pun">=</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">x </span><span class="pun">-</span><span class="pln"> mousepos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> dy </span><span class="pun">=</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">y </span><span class="pun">-</span><span class="pln"> mousepos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="kwd">var</span><span class="pln"> angle </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">atan2</span><span class="pun">(</span><span class="pln">dy</span><span class="pun">,</span><span class="pln"> dx</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>rect</strong></span><strong><span class="pun">.</span><span class="pln">x </span><span class="pun">-=</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">v</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">cos</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span><span class="pln"> </span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; rect</span><span class="pun">.</span><span class="pln">y </span><span class="pun">-=</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">v</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sin</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span></strong><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 3) draw object</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawRectangle</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//&nbsp;request new frame</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; window</span><span class="pun">.</span><span class="pln">requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainloop</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> drawRectangle</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// These two lines move the coordinate system</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">rect</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="com">// recenter the coordinate system in the middle</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="com">// the rectangle. Like that it will rotate around</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="com">// this point instead of top left corner</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(-</span><span class="pln">rect</span><span class="pun">.</span><span class="pln">width</span><span class="pun">/</span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="pun">-</span><span class="pln">rect</span><span class="pun">.</span><span class="pln">height</span><span class="pun">/</span><span class="lit">2</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// necessary to take into account CSS boudaries</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getBoundingClientRect</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; x</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientX </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">left</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; y</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientY </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">top</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

__Explanations:__

+ _Line 25_ calculates the angle between mouse cursor and the rectangle,
+ _Lines 27-28_ move the rectangle v pixels along a line between the rectangle's current position and the mouse cursor,
+ _Lines 41-46_ translate the rectangle, rotate it, and recenter the _rotational point_ to the center of the rectangle (in its new position).


#### Adding mouse listeners to the game framework

Now we will include these listeners into our game framework. Notice that we changed some parameters (no need to pass the canvas as a parameter of the `getMousePos()` function, for example).

The [new online version of the game engine](https://jsbin.com/rizuyah/edit) can be tried at JSBin:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/35zjZh9")"
    src    = "https://bit.ly/3q6HaZP"
    alt    = "Screenshot of a JsBin example that shows message on mouse events"
    title  = "Screenshot of a JsBin example that shows message on mouse events"
  />
</figure>


Try pressing arrows and space keys, moving the mouse, and pressing the buttons, all at the same time. You'll see that the game framework handles all these events simultaneously because the global variable named `inputStates` is updated by keyboard and mouse events, and consulted to direct movements every 1/60th second.

JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Inits</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> game </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> GF</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; game</span><span class="pun">.</span><span class="pln">start</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// GAME FRAMEWORK STARTS HERE</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> GF </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Vars for handling inputs</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> inputStates </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> measureFPS </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">newTime</span><span class="pun">){</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun"><span style="color: #000000;" color="#000000">&nbsp;&nbsp;</span>};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Clears the canvas content</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> clearCanvas</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Functions for drawing the monster and perhaps other objects</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> drawMyMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> mainLoop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">time</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Main function, called each frame </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;measureFPS</span><span class="pun">(</span><span class="pln">time</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Clears the canvas</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;clearCanvas</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Draws the monster</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;drawMyMonster</span><span class="pun">(</span><span class="lit">10</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()*</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()*</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Checks inputStates</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">left</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"left"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">up</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"up"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">right</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"right"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">60</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">down</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"down"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">80</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">space</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"space bar"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">140</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"x = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">" y = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">inputStates</span><span class="pun">.</span><span class="pln">mousedown</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"mousedown b"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> inputStates</span><span class="pun">.</span><span class="pln">mouseButton</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">180</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Calls the animation loop every 1/60th of second</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Necessary to take into account CSS boudaries</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getBoundingClientRect</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; x</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientX </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">left</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; y</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientY </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">top</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> start </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">...</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Adds the listener to the main window object, and updates the states</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">){</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">left </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">38</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">up </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">39</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">right </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">40</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">down </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">32</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">space </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// If the key&nbsp;is released, changes the states object </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">left </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">38</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">up </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">39</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">right </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">40</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">down </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">32</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; inputStates</span><span class="pun">.</span><span class="pln">space </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Mouse event listeners</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">mousePos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">mousedown </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">mouseButton </span><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">button</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseup'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;inputStates</span><span class="pun">.</span><span class="pln">mousedown </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Starts the animation</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Our GameFramework returns a public API visible from outside its scope</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; start</span><span class="pun">:</span><span class="pln"> start</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>







