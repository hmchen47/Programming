# Module 2: Game programming with HTML5 section


## 2.4 Time-based animation


### 2.4.1 Introduction


#### Live coding video: time-based animation

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3gHlYqg)


#### Time-based animation

Let's study an important technique known as "time-based animation", that is used by nearly all "real" video games.

This technique is useful when:

+ __Your application runs on different devices, and where 60 frames/s are definitely not possible. More generally, you want your animated objects to move at the same speed on screen, regardless of the device that runs the game.__

  For example, imagine a game or an animation running on a smartphone and on a desktop computer with a powerful GPU. On the phone, you might achieve a maximum of 20 fps with no guarantee that this number will be constant; whereas on the desktop, you will reliably achieve 60 fps. If the application is a car racing game, for example, your car will take 30s to make a complete loop on the race track when running on a desktop, whilst on a smartphone it might take 5 minutes.

  The way to address this is to run at a lower frame-rate on the phone. This will enable the car to race around the track in the same amount of (real) time as it does on a powerful desktop computer.

  __Solution:__ you need to compute the amount of time that has elapsed between the last frame that was drawn and the current one; and depending on this delta of time, adjust the distance the car must move across the screen. We will see several examples of this later.

+ __You want to perform some animations only a few times per second.__ For example, in sprite-based animation (drawing different images as a character moves, for example), you will not change the images of the animation 60 times/s, but only ten times per second. Mario will walk on the screen in a 60 fps animation, but his posture will not change every 1/60th of second.
+ __You may also want to accurately set the framerate__, leaving some CPU time for other tasks. Many games consoles limit the frame-rate to 1/30th of a second, in order to allow time for other sorts of computations (physics engine, artificial intelligence, etc.)


#### How to measure time when we use `requestAnimationFrame`?

Let's take a simple example with a small rectangle that moves from left to right. At each animation loop, we erase the canvas content, calculate the rectangle's new position, draw the rectangle, and call the animation loop again. So you animate a shape as follows (note: steps 2 and 3 can be swapped):

1. erase the canvas,
1. draw the shapes,
1. move the shapes,
1. go to step 1.

When we use requestAnimationFrame for implementing such an animation, as we did in the previous lessons, the browser tries to keep the frame-rate at 60 fps, meaning that the ideal time between frames will be 1/60 second = 16.66 ms.


#### Example #1: no use of time-based animation

[Online example at JSBin](https://jsbin.com/dibuze/edit)

[Local Demo](src/02d-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open("https://bit.ly/3gJ34xX")"
    src    = "https://bit.ly/3iU60KX"
    alt    = "image of a small rectangle in a canvas, moving from left to right"
    title  = "image of a small rectangle in a canvas, moving from left to right"
  />
</figure>

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">utf-8</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;title&gt;</span><span class="pln">Small animation example</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> speedX</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Called after the DOM is ready (page loaded)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// init the different variables</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#mycanvas"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;width </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;height </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;x</span><span class="pun">=</span><span class="lit">10</span><span class="pun">;</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Move 3 pixels left or right at each frame</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;speedX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Start animation</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;animationLoop</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// an animation involves: 1) clear canvas and 2) draw shapes, </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// 3) move shapes, 4) recall the loop with requestAnimationFrame</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// clear canvas</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// move rectangle</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;x </span><span class="pun">+=</span><span class="pln"> speedX</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// check collision on left or right</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(((</span><span class="pln">x</span><span class="pun">+</span><span class="lit">5</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&gt;</span><span class="pln"> width</span><span class="pun">)</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> </span><span class="pun">(</span><span class="pln">x </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// cancel move + inverse speed</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x </span><span class="pun">-=</span><span class="pln"> speedX</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedX </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// animate.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mycanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"200"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"50"</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid black</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/canvas&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

If you try this example on a low-end smartphone (use this URL for the example in stand-alone mode) and if you run it at the same time on a desktop PC, it is obvious that the rectangle moves faster on the desktop computer screen than on your phone.

This is because the frame rate differs between the computer and the smartphone: perhaps 60 fps on the computer and 25 fps on the phone. As we only move the rectangle in the animationLoop, in one second the rectangle will be moved 25 times on the smartphone compared with 60 times on the computer! Since we move the rectangle the same number of pixels each time, the rectangle moves faster on the computer!

#### Example #2: simulating a low-end device

Here is the same example to which we have added a loop that wastes time right in the middle of the animation loop. It will artificially extend the time spent inside the animation loop, making the 1/60th of second ideal impossible to reach.

[Try it on JsBin](https://jsbin.com/remide/edit) and notice that the square moves much slower on the screen. Indeed, its speed is a direct consequence of the extra time spent in the animation loop.

[Local Demo](src/02d-example02.html)

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">50000000</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// slow down artificially the animation</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
</ol></div>

#### Notes for 2.4.1 Introduction

+ Time-based animation
  + animate objects to move at the same speed on screen, regardless of the device running the game
    + compute the amount of time elapsed btw the last frame and the current one
    + adjust the distance the objects move across the screen depending on the delta of time
  + perform some animations only a few times per second
    + sprite-based animation: drawing different images as an object moves
    + draw object only ten times per second, not change the images of the animation 60 times/s
    + screen still performs 60 fps
  + accurate set the framerate
    + leave some CPU time for other tasks
    + many games consoles limit the frame-rate tp 1/30th of a second

+ Procedure to measure time btw frames
  + erase the canvas
  + draw the shapes
  + move the shapes
  + got to the 1st step

+ Example: regular animation
  + rectangle moves faster on the desktop computer screen that on mobile phone
  + declare variables: `var canvas, ctx; var width, height; var x, y; var speedX;`
  + init page after DOM ready<a name="init"></a>: `function init() {...}`
    + init variables: `canvas = document.queryAnimationFrame("#myCanvas"); ctx = canvas.getContext('2d'); width = canvas.width = width; height = canvas.height; x= 10; y = 10;`
    + set speed<a name="speed"></a>: `speedX = 3;`
    + start animation: `animationLoop();`
  + generate animation loop<a name="animationLoop"></a>: `function animationLoop() {...}`
    + clear canvas: `ctx.cleanRec(0, 0, 10, 10);`
    + draw shape: `ctx.strokeRect(x, y, 10, 10);`
    + move rectangle: `x += speedX;`
    + check collision on left and right: `if (((x+5) > width) || (x <= 0)) { x -= speedX; speedX = -speedX; }`
    + call next frame: `requestAnimationFrame(animationLoop);`

+ Example: simulating a low-end device
  + generate [animation loop](#animationLoop)
  + additional loop to slow the animaton loop after clear rectangle<a name="simulation"></a>: `for (var i=0; i<50000000; i++) { // slow down artificially the animation };`


### 2.4.2 Measuring time between frames

Let's find out how to measuring time between frames to achieve a constant speed on screen, even when the frame rate changes.

#### Method #1: using the JavaScript Date object

Let's modify the example from the previous lesson slightly by adding a _time-based animation_.  Here we use the "standard JavaScript" way for measuring time, using JavaScript's Date object:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;time&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Date</span><span class="pun" style="color: #669900;">().</span><span class="pln">getTime</span><span class="pun" style="color: #669900;">();</span></li>
</ol></div><br>

The `getTime()` method returns the number of milliseconds since midnight on January 1, 1970. This is the number of milliseconds that have elapsed during the Unix epoch (!).

There is an alternative. We could have called:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;time&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Date</span><span class="pun" style="color: #669900;">.</span><span class="pln">now</span><span class="pun" style="color: #669900;">();</span></li>
</ol></div><br>

So, if we measure the time at the beginning of each animation loop, and store it, we can then compute the delta of times elapsed between two consecutive loops.

We then apply some simple math to compute the number of pixels we need to move the shape to achieve a given speed (in pixels/s).


__Example #1: using time based animation: the bouncing square__

[Online example at JSBin](https://jsbin.com/riferi/edit):

[Local Demo](src/02d-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3cYaKeJ")"
    src    = "https://bit.ly/3gF086H"
    alt    = "Bouncing square with time bases animation"
    title  = "Bouncing square with time bases animation"
  />
</figure>


Source code from the example:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec" style="color: #aa0066;">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;html</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">lang</span><span class="pun" style="color: #669900;">=</span><span class="atv" style="color: #008800;">"en"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&nbsp; &lt;meta</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">charset</span><span class="pun" style="color: #669900;">=</span><span class="atv" style="color: #008800;">utf-8</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&nbsp; &lt;title&gt;</span><span class="pln">Move rectangle using time based animation</span><span class="tag" style="color: #008888;">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag" style="color: #008888;">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;ctx</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #669900;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// incX is the distance from the previously drawn</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // rectangle to the new one</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;speedX</span><span class="pun" style="color: #669900;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// speedX is the target speed of the rectangle, in pixels/s</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// for time based animation</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #669900;">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;then&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Date</span><span class="pun" style="color: #669900;">().</span><span class="pln">getTime</span><span class="pun" style="color: #669900;">();</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Called after the DOM is ready (page loaded)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;init</span><span class="pun" style="color: #669900;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Init the different variables</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; canvas&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #669900;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #669900;">(</span><span class="str" style="color: #008800;">"#mycanvas"</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; ctx&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #669900;">.</span><span class="pln">getContext</span><span class="pun" style="color: #669900;">(</span><span class="str" style="color: #008800;">'2d'</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; width&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #669900;">.</span><span class="pln">width</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; height&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #669900;">.</span><span class="pln">height</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; x</span><span class="pun" style="color: #669900;">=</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #669900;">;</span><span class="pln">&nbsp;y&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Target speed in pixels/second, try with high values, 1000, 2000...</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; speedX&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">200</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Start animation</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;animationLoop</span><span class="pun" style="color: #669900;">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #669900;">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;animationLoop</span><span class="pun" style="color: #669900;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// Measure time</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">now&nbsp;</strong></span><strong style="color: red;"><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Date</span><span class="pun" style="color: #669900;">().</span><span class="pln">getTime</span><span class="pun" style="color: #669900;">();</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// How long between the current frame and the previous one?</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">delta&nbsp;</strong></span><strong style="color: red;"><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;now&nbsp;</span><span class="pun" style="color: #669900;">-</span><span class="pln">&nbsp;then</span><span class="pun" style="color: #669900;">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">//console.log(delta);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Compute the displacement in x (in pixels) in function of the time elapsed and</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// in function of the wanted speed</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">incX&nbsp;</strong></span><strong style="color: red;"><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;calcDistanceToMove</span><span class="pun" style="color: #669900;">(</span><span class="pln">delta</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;speedX</span><span class="pun" style="color: #669900;">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// an animation involves: 1) clear canvas and 2) draw shapes,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// 3) move shapes, 4) recall the loop with requestAnimationFrame</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// clear canvas</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #669900;">.</span><span class="pln">clearRect</span><span class="pun" style="color: #669900;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #669900;">.</span><span class="pln">strokeRect</span><span class="pun" style="color: #669900;">(</span><span class="pln">x</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// move rectangle</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;x&nbsp;</span><span class="pun" style="color: #669900;">+=</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// check collision on left or right</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">if</span><span class="pun" style="color: #669900;">((</span><span class="pln">x</span><span class="pun" style="color: #669900;">+</span><span class="lit" style="color: #006666;">10</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">&gt;=</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #669900;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">||</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">(</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #669900;">&lt;=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #669900;">))</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// cancel move + inverse speed</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; x&nbsp;</span><span class="pun" style="color: #669900;">-=</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; speedX&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">-</span><span class="pln">speedX</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun" style="color: #669900;">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// Store time</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">then&nbsp;</strong></span><strong style="color: red;"><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #669900;">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;requestAnimationFrame</span><span class="pun" style="color: #669900;">(</span><span class="pln">animationLoop</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">}</span><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// We want the rectangle to move at a speed given in pixels/second</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp;// (there are 60 frames in a second)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// If we are really running at 60 frames/s, the delay between </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp;// frames should be 1/60</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// = 16.66 ms, so the number of pixels to move = (speed * del)/1000. </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp;// If the delay&nbsp;</span>is twice as</li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// long, the formula works: let's move the rectangle for twice as long!</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;calcDistanceToMove&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #669900;">(</span><span class="pln">delta</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;speed</span><span class="pun" style="color: #669900;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">return</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">(</span><span class="pln">speed&nbsp;</span><span class="pun" style="color: #669900;">*</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #669900;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">/</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1000</span><span class="pun" style="color: #669900;">;</span><span class="pln"></span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;/script&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/head&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;body</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">onload</span><span class="pun" style="color: #669900;">=</span><span class="atv" style="color: #008800;">"</span><span class="pln">init</span><span class="pun" style="color: #669900;">();</span><span class="atv" style="color: #008800;">"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;canvas</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">id</span><span class="pun" style="color: #669900;">=</span><span class="atv" style="color: #008800;">"mycanvas"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">width</span><span class="pun" style="color: #669900;">=</span><span class="atv" style="color: #008800;">"200"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">height</span><span class="pun" style="color: #669900;">=</span><span class="atv" style="color: #008800;">"50"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">style</span><span class="pun" style="color: #669900;">=</span><span class="atv" style="color: #008800;">"</span><span class="pln">border</span><span class="pun" style="color: #669900;">:</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2px</span><span class="pln">&nbsp;solid black</span><span class="atv" style="color: #008800;">"</span><span class="tag" style="color: #008888;">&gt;&lt;/canvas&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/html&gt;</span></li>
</ol></div><br>

In this example, we only added a few lines of code for measuring the time and computing the time elapsed between two consecutive frames (see line 38). Normally, requestAnimationFrame(callback) tries to call the callback function every 16.66 ms (this corresponds to 60 frames/s)... but this is never exactly the case. If you do a console.log(delta)in the animation loop, you will see that even on a very powerful computer, the delta is "very close" to 16.6666 ms, but 99% of the time it will be slightly different.

The function `calcDistanceToMove(delta, speed)` takes two parameters: 1) the time elapsed in ms, and 2) the target speed in pixels/s. 

Try this example on a smartphone, use this [link](https://jsbin.com/jeribi) to run the JSBin example in stand-alone mode. Normally you should see no difference in speed, but it may look a bit jerky on a low-end smartphone or on a slow computer. _This is the correct behavior._

Or you can try the next example that simulates a complex animation loop that takes a long time to draw each frame...


__Example #2: using a simulation that spends a lot of time in the animation loop, to compare with the previous example__

[Try it on JsBin](https://jsbin.com/jeribi/edit):

[Local Demo](src/02d-example04.html)

We added a long loop in the middle of the animation loop. This time, the animation should be very jerky. However, notice that the apparent speed of the square is the same as in the previous example: the animation adapts itself!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Measure time</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; now </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Date</span><span class="pun">().</span><span class="pln">getTime</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// How long between the current frame and the previous one ?</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; delta </span><span class="pun">=</span><span class="pln"> now </span><span class="pun">-</span><span class="pln"> </span><span class="kwd">then</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">//console.log(delta);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Compute the displacement in x (in pixels) in function of the time elapsed and</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// in function of the wanted speed</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; incX </span><span class="pun">=</span><span class="pln"> calcDistanceToMove</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln"> speedX</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// an animation is : 1) clear canvas and 2) draw shapes, </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// 3) move shapes, 4) recall the loop with requestAnimationFrame</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// clear canvas</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">50000000</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// just to slow down the animation</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// move rectangle</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; x </span><span class="pun">+=</span><span class="pln"> incX</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// check collision on left or right</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">((</span><span class="pln">x</span><span class="pun">+</span><span class="lit">10</span><span class="pln"> </span><span class="pun">&gt;=</span><span class="pln"> width</span><span class="pun">)</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> </span><span class="pun">(</span><span class="pln">x </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// cancel move + inverse speed</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;x </span><span class="pun">-=</span><span class="pln"> incX</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;speedX </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Store time</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">then</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> now</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
</ol></div><br>


#### Method #2: using the new HTML5 high-resolution timer

Since the beginning of HTML5, game developers, musicians, and others have asked for a sub-millisecond timer to be able to avoid some glitches that occur with the regular JavaScript timer. This API is called the "[High Resolution Time API](https://www.w3.org/TR/hr-time/)".

This API is very simple to use - just do:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;time&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;performance</span><span class="pun" style="color: #669900;">.</span><span class="pln">now</span><span class="pun" style="color: #669900;">();</span></li>
</ol></div><br>

... to get a sub-millisecond time-stamp. It is similar to `Date.now()` except that the accuracy is much higher and that the result is not exactly the same. The value returned is a floating point number, not an integer value!

From this article that explains the High Resolution Time API: 
> "The only method exposed is `now()`, which returns a DOMHighResTimeStamp representing the current time in milliseconds. The timestamp is very accurate, with precision to a thousandth of a millisecond. Please note that while `Date.now()` returns the number of milliseconds elapsed since 1 January 1970 00:00:00 UTC, `performance.now()` returns the number of milliseconds, with microseconds in the fractional part, from performance.`timing.navigationStart()`, the start of navigation of the document, to the `performance.now()` call. Another important difference between `Date.now()` and `performance.now()` is that the latter is monotonically increasing, so the difference between two calls will never be negative."

To sum up:

+ `performance.now()` returns the time since the load of the document (it is called a `DOMHighResTimeStamp`), with a sub mill-second accuracy, as a floating point value, with very high accuracy.
+ `Date.now()` returns the number of mill-seconds since the Unix epoch, as an integer value.

Support for this API is quite good - see the compatibility table [online](https://caniuse.com/#feat=high-resolution-time).

Here is [a version on JSBin](https://jsbin.com/wecaho/edit) of the previous example with the bouncing rectangle, that uses the high resolution timer.

[Local Demo](src/02d-example05.html)

Source code of the example:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #669900;">...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;speedX</span><span class="pun" style="color: #669900;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// speedX is the target speed of the rectangle in pixels/s</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// for time based animation</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// High resolution timer</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">then</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;performance</span><span class="pun" style="color: #669900;">.</span><span class="pln">now</span><span class="pun" style="color: #669900;">();</span></strong><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Called after the DOM is ready (page loaded)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;init</span><span class="pun" style="color: #669900;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun" style="color: #669900;">...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #669900;">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;animationLoop</span><span class="pun" style="color: #669900;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// Measure time, with high resolution timer</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">now&nbsp;</strong></span><strong style="color: red;"><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;performance</span><span class="pun" style="color: #669900;">.</span><span class="pln">now</span><span class="pun" style="color: #669900;">();</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// How long between the current frame and the previous one?</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; delta&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;now&nbsp;</span><span class="pun" style="color: #669900;">-</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">then</span><span class="pun" style="color: #669900;">;</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">//console.log(delta);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Compute the displacement in x (in pixels) in function </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp; // of the time elapsed and</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// in function of the wanted speed</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; incX&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;calcDistanceToMove</span><span class="pun" style="color: #669900;">(</span><span class="pln">delta</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;speedX</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">//console.log("dist = " + incX);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// an animation involves: 1) clear canvas and 2) draw shapes,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// 3) move shapes, 4) recall the loop with requestAnimationFrame</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// clear canvas</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #669900;">.</span><span class="pln">clearRect</span><span class="pun" style="color: #669900;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #669900;">.</span><span class="pln">strokeRect</span><span class="pun" style="color: #669900;">(</span><span class="pln">x</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #669900;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// move rectangle</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;x&nbsp;</span><span class="pun" style="color: #669900;">+=</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// check collision on left or right</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">if</span><span class="pun" style="color: #669900;">((</span><span class="pln">x</span><span class="pun" style="color: #669900;">+</span><span class="lit" style="color: #006666;">10</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">&gt;=</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #669900;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">||</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">(</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #669900;">&lt;=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #669900;">))</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// cancel move + inverse speed</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; x&nbsp;</span><span class="pun" style="color: #669900;">-=</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; speedX&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">-</span><span class="pln">speedX</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #669900;">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Store time</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">then</span><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">=</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #669900;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// call the animation loop again</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestAnimationFrame</span><span class="pun" style="color: #669900;">(</span><span class="pln">animationLoop</span><span class="pun" style="color: #669900;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">}</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #669900;">&lt;/</span><span class="pln">script</span><span class="pun" style="color: #669900;">&gt;</span></li>
</ol></div><br>

Only two lines have changed but the accuracy is much higher, if you uncomment the console.log(...) calls in the main loop. You will see the difference.


#### Method #3: using timestamp parameter of requestAnimationFrame

__Method #3: using the optional timestamp parameter of the callback function of requestAnimationFrame__

<p class="exampleHTML" style="text-align: center;"><span style="color: #ff0000;"><strong style="color: red;"><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">This is the recommended method!</span></strong></span></p>

There is an optional parameter that is passed to the callback function called by `requestAnimationFrame`: a timestamp!

[The requestAnimationFrame API specification](https://www.w3.org/TR/html51/webappapis.html#animation-frames) says that this timestamp corresponds to the time elapsed since the page has been loaded.

It is similar to the value sent by the high resolution timer using `performance.now()`.

Here is a running example  of the animated rectangle, that uses this `timestamp` parameter.

[Online example at JSBin](https://jsbin.com/kuvumu/edit):

[Local Demo](src/02d-example06.html)

Source code of the example:

<div class="source-code" style="line-height: 25.6px;"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln">&nbsp;</span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;meta</span><span class="pln">&nbsp;</span><span class="atn">charset</span><span class="pun">=</span><span class="atv">utf-8</span><span class="pln">&nbsp;</span><span class="tag">/&gt;</span><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;title&gt;</span><span class="pln">Time based animation using the parameter of the requestAnimationFrame callback</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;canvas</span><span class="pun">,</span><span class="pln">&nbsp;ctx</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;width</span><span class="pun">,</span><span class="pln">&nbsp;height</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;x</span><span class="pun">,</span><span class="pln">&nbsp;y</span><span class="pun">,</span><span class="pln">&nbsp;incX</span><span class="pun">;</span><span class="pln">&nbsp;</span><span class="com">// incX is the distance from the previously drawn rectangle</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// to the new one</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;speedX</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// speedX is the target speed of the rectangle in pixels/s</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// for time based animation</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;now</span><span class="pun">,</span><span class="pln">&nbsp;delta</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// High resolution timer</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;oldTime&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Called after the DOM is ready (page loaded)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln">&nbsp;init</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// init the different variables</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;canvas&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#mycanvas"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;width&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;height&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;x</span><span class="pun">=</span><span class="lit">10</span><span class="pun">;</span><span class="pln">&nbsp;y&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Target speed in pixels/second, try with high values, 1000, 2000...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;speedX&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="lit">200</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Start animation</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln">&nbsp;animationLoop</span><span class="pun">(</span><strong style="color: red;"><span class="pln">currentTime</span></strong><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// How long between the current frame and the previous one?</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">delta&nbsp;</strong></span><strong style="color: red;"><span class="pun">=</span><span class="pln">&nbsp;currentTime&nbsp;</span><span class="pun">-</span><span class="pln">&nbsp;oldTime</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Compute the displacement in x (in pixels) in function of the time elapsed and</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// in function of the wanted speed</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;incX&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;calcDistanceToMove</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln">&nbsp;speedX</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pln">&nbsp;</span><span class="com">// clear canvas</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">0</span><span class="pun">,</span><span class="pln">&nbsp;width</span><span class="pun">,</span><span class="pln">&nbsp;height</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln">&nbsp;y</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// move rectangle</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;x&nbsp;</span><span class="pun">+=</span><span class="pln">&nbsp;incX</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// check collision on left or right</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(((</span><span class="pln">x</span><span class="pun">+</span><span class="lit">10</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">&gt;</span><span class="pln">&nbsp;width</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">||</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">x&nbsp;</span><span class="pun">&lt;</span><span class="pln">&nbsp;</span><span class="lit">0</span><span class="pun">))</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// inverse speed</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;x&nbsp;</span><span class="pun">-=</span><span class="pln">&nbsp;incX</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;speedX&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="pun">-</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Store time</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;oldTime&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;currentTime</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// asks for next frame</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;calcDistanceToMove&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">delta</span><span class="pun">,</span><span class="pln">&nbsp;speed</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">speed&nbsp;</span><span class="pun">*</span><span class="pln">&nbsp;delta</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">/</span><span class="pln">&nbsp;</span><span class="lit">1000</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag">&lt;/script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln">&nbsp;</span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag">&lt;canvas</span><span class="pln">&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mycanvas"</span><span class="pln">&nbsp;</span><span class="atn">width</span><span class="pun">=</span><span class="atv">"200"</span><span class="pln">&nbsp;</span><span class="atn">height</span><span class="pun">=</span><span class="atv">"50"</span><span class="pln">&nbsp;</span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">border</span><span class="pun">:</span><span class="pln">&nbsp;</span><span class="lit">2px</span><span class="pln">&nbsp;solid black</span><span class="atv">"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>


#### Notes for 2.4.2 Measuring time between frames

+ Methods to measure time btw frames
  + using the JavaScript `Data` object
    + standard JavaScript for measuring time: `var time = new Date().getTime();`
    + alternative solution: `var time = Date().now();`
    + `getTime()` method: return an integer number of millisecond (Unix epoch) since midnight on 1970-01-01
    + procedure
      + measure the time at the beginning of each animation loop
      + store the time
      + compute the delta of times elapsed btw two consecutive loops
    + applying some simple math to compute the number of pixels $\to$ move the object to achieve a given speed (in pixels/s)
  + using the new HTML5 high-resolution timer
    + [Hight Resolution Time API](https://www.w3.org/TR/hr-time/): a working draft
    + `performance.now()`:
      + get a sub-millisecond time-stamp
      + similar to `Date.now()` but w/ much higher accuracy
      + return a floating point number, called a `DOMHighResTimeStamp`
  + using timestamps parameter of rge callback function of `requestAnimationFrame`
    + recommended method
    + timestamps as optional parameter
    + corresponding too the time elapsed since the page loaded
    + similar to the value sent by the high resolution timer using `performance.now()`

+ Example: using Date object
  + declare variables<a name="vars"></a>: `var canvas, ctx; var width, height; var x, y, incX; var speedX;`
  + declare and set time-related variables<a name="timeVars"></a>: `var now, delta = 0; var then = new Date().getTime();`
  + [init page after DOM ready](#init) w/ change `speedX = 200;`
  + generate [animation loop](#animationLoop) w/ time measurement and change
    + measure time<a name=measureTime></a>: `now = new Date().getTime(); delta = now - then;`
    + change `speedX` to `incX` for assigning `x`
    + store current frame time before request next frame: `then = now;`
  + compute the distance to move<a name="calcDist"></a>: `var calcDistanceToMove = function(delta, speed) {return (speed * delta)/1000;}`

+ Example: simulation spending time in animation loop
  + generate [animation loop](#animationLoop) w/ time measurement and change
    + [measure time](#measureTime)
    + call to compute distance: `incX = calcDistanceToMove(delta, speedX);`
    + add [simulation](#simulation) after clear canvas
    + measure time<a name=measureTime></a>: `now = new Date().getTime(); delta = now - then;`
    + change `speedX` to `incX` for assigning `x`
    + store current frame time before request next frame: `then = now;`

+ Example: high resultion API
  + declare variable: `var speedX; var now, delta;`
  + get high resultion timer: `var then = performance.now();`
  + [init page after DOM ready](#init)
  + generate [animation loop](#animationLoop) w/ additional code
    + get current time: `var now = performance.now();`
    + calculate distance: `incX = calcDistanceToMove(delta, speedX);`
    + store current frame time before request next frame: `then = now;`

+ Example: using timestamp parameter of `requestAnimationFrame`
  + [declar variables](#vars) w/ `var oldTime = 0;`
  + [declar time variables](#timeVars)
  + [init page after DOM ready](#init) w/ timestamps parameter
  + generate animation loop: `function animationLoop(currentTime) {...}`
    + compute time difference: `delta = currentTime - oldTime;`
    + call to compute the distance: `calcDistanceToMove(delta, speedX);`
    + clear and redraw object as [old animation loop](#animationLoop)
    + reset old frame timer: `oldTime = currentTime;`
    + call for next frame: `requestAnimationFrame(animationLoop);`
  + calculate [distance to move](#calcDist)


### 2.4.3 Setting the frame rate

Principle: even if the mainloop is called 60 times per second, ignore some frames in order to reach the desired frame rate.

It is also possible to set the frame rate using time based animation. We can set a global variable that corresponds to the desired frame rate and compare the elapsed time between two executions of the animation loop:

+ If the time elapsed is too short for the target frame rate: do nothing,
+ If the time elapsed exceeds the delay corresponding to the chosen frame rate: draw the frame and reset this time to zero.

Here is the [online example](https://jsbin.com/bonutur/edit) at JSBin.

[Local Demo](src/02d-example07.html)

Try to change the parameter value of the call to: 

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">setFrameRateInFramesPerSecond</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">5</span><span class="pun" style="color: #666666;">);</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// try other values!</span></li>
</ol></div><br>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3gGsRYD")"
    src    = "https://bit.ly/3iYegcK"
    alt    = "Screenshot of a jsbin example with an animated curve, we can set the framerate in this example..."
    title  = "Screenshot of a jsbin example with an animated curve, we can set the framerate in this example..."
  />
</figure>

Source code of the example:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec" style="color: #aa0066;">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;html</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">lang</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"en"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;meta</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">charset</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">utf-8</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;title&gt;</span><span class="pln">Set framerate using a high resolution timer</span><span class="tag" style="color: #008888;">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;p&gt;</span><span class="pln">This example measures and sums deltas of time between consecutive frames of animation. It includes a&nbsp;</span><span class="tag" style="color: #008888;">&lt;code&gt;</span><span class="pln">setFrameRateInFramesPerSecond</span><span class="tag" style="color: #008888;">&lt;/code&gt;</span><span class="pln">&nbsp;function you can use to reduce the number of frames per second of the main animation.</span><span class="tag" style="color: #008888;">&lt;/p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;canvas</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">id</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"myCanvas"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">width</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"700"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">height</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"350"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;/canvas&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;canvas&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"#myCanvas"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;ctx&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">.</span><span class="pln">getContext</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"2d"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;width&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">.</span><span class="pln">width</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;height&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">.</span><span class="pln">height</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;lastX&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;width&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;lastY&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;height&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;hue&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// Michel Buffa: set the target frame rate. TRY TO CHANGE THIS VALUE AND SEE</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// THE RESULT. Try 2 frames/s, 10 frames/s, 60 frames/s Normally there</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// should be a limit&nbsp;of 60 frames/s in the browser's implementations.</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp;setFrameRateInFramesPerSecond</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">60</span><span class="pun" style="color: #666666;">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// for time based animation. DelayInMS corresponds to the target framerate</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;delayInMS</span><span class="pun" style="color: #666666;">,</span><strong style="color: red;"><span class="pln">&nbsp;totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// High resolution timer</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;then&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;performance</span><span class="pun" style="color: #666666;">.</span><span class="pln">now</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// start the animation</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun" style="color: #666666;">(</span><span class="pln">mainloop</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong style="color: red;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;setFrameRateInFramesPerSecond</span><span class="pun" style="color: #666666;">(</span><span class="pln">frameRate</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; delayInMs&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1000</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;frameRate</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp;&nbsp;</span><span class="pun" style="color: #666666;">}</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// each function that is going to be run as an animation should end by</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// asking again for a new frame of animation</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;<g class="gr_ gr_68 gr-alert gr_spell gr_run_anim ContextualSpelling ins-del multiReplace" id="68" data-gr-id="68">mainloop</g></span><span class="pun" style="color: #666666;">(time)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Here we will only redraw something if the time we want between frames has</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// elapsed</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Measure time with high resolution timer</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; now&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;time</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// How long between the current frame and the previous one?</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; delta&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;now&nbsp;</span><span class="pun" style="color: #666666;">-</span><span class="pln">&nbsp;then</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// TRY TO UNCOMMENT THIS LINE AND LOOK AT THE CONSOLE</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// console.log("delay = " + delayInMs + " delta = " + delta + " total time = " +</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp; // totalTimeSinceLastRedraw);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// If the total time since the last redraw is &gt; delay corresponding to the wanted</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// framerate, then redraw, else add the delta time between the last call to line()</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp; // by requestAnimFrame&nbsp;</span>to the total time..</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">if</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">(</span><span class="pln">totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln">&nbsp;delayInMs</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// if the time between the last frame and now is &gt; delay then we</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// clear the canvas and redraw</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">save</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Trick to make a blur effect: instead of clearing the canvas</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// we draw a rectangle with a transparent color. Changing the 0.1</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// for a smaller value will increase the blur...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">fillStyle&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"rgba(0,0,0,0.1)"</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">fillRect</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">translate</span><span class="pun" style="color: #666666;">(</span><span class="pln">width&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;height&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">scale</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">0.9</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0.9</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">translate</span><span class="pun" style="color: #666666;">(-</span><span class="pln">width&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">-</span><span class="pln">height&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">beginPath</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">lineWidth&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">5</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">+</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">moveTo</span><span class="pun" style="color: #666666;">(</span><span class="pln">lastX</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;lastY</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;lastX&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;width&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;lastY&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;height&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">bezierCurveTo</span><span class="pun" style="color: #666666;">(</span><span class="pln">width&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">(),</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;height&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">(),</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;width&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">(),</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;height&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">(),</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;lastX</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;lastY</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;hue&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;hue&nbsp;</span><span class="pun" style="color: #666666;">+</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #666666;">.</span><span class="pln">random</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">strokeStyle&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"hsl("</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">+</span><span class="pln">&nbsp;hue&nbsp;</span><span class="pun" style="color: #666666;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">", 50%, 50%)"</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">shadowColor&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"white"</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">shadowBlur&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">stroke</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">restore</span><span class="pun" style="color: #666666;">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// reset the total time since last redraw</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666666;">}</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">else</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// sum the total time since last redraw</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #666666;">+=</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Store time</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; then&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// request new frame</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun" style="color: #666666;">(</span><span class="pln">mainloop</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;/script&gt;</span><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;/body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/html&gt;</span></li>
</ol></div><br>


#### Same technique with the bouncing rectangle

See how we can set both the speed (in pixels/s) and the frame-rate using a high-resolution time with this [modified version on JSBin](https://jsbin.com/momeci/edit) of the example with the rectangle that also uses this technique.

[Local Demo](src/02d-example07.html)


Source code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec" style="color: #aa0066;">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;html</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">lang</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"en"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;meta</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">charset</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">utf-8</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;title&gt;</span><span class="pln">Bouncing rectangle with high resolution timer and adjustable frame rate</span><span class="tag" style="color: #008888;">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;ctx</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #666666;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// incX is the distance from the previously drawn rectangle</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// to the new one</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;speedX</span><span class="pun" style="color: #666666;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// speedX is the target speed of the rectangle in pixels/s</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// for time based animation, DelayInMS corresponds to the target frame rate</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;delayInMS</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;totalTimeSinceLastRedraw</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// High resolution timer</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;then&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;performance</span><span class="pun" style="color: #666666;">.</span><span class="pln">now</span><span class="pun" style="color: #666666;">();</span><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Michel Buffa: set the target frame rate. TRY TO CHANGE THIS VALUE AND SEE</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// THE RESULT. Try 2 frames/s, 10 frames/s, 60, 100 frames/s Normally there</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// should be a limit&nbsp;of 60 frames/s in the browser's implementations, but you can&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp;// try higher values</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;setFrameRateInFramesPerSecond</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">25</span><span class="pun" style="color: #666666;">);</span><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;setFrameRateInFramesPerSecond</span><span class="pun" style="color: #666666;">(</span><span class="pln">framerate</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;delayInMs&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1000</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;framerate</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Called after the DOM is ready (page loaded)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;init</span><span class="pun" style="color: #666666;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// init the different variables</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;canvas&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666666;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">"#mycanvas"</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">.</span><span class="pln">getContext</span><span class="pun" style="color: #666666;">(</span><span class="str" style="color: #008800;">'2d'</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;width&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">.</span><span class="pln">width</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;height&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666666;">.</span><span class="pln">height</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;x</span><span class="pun" style="color: #666666;">=</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #666666;">;</span><span class="pln">&nbsp;y&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Target speed in pixels/second, try with high values, 1000, 2000...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;speedX&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2000</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Start animation</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;requestAnimationFrame</span><span class="pun" style="color: #666666;">(</span><span class="pln">animationLoop</span><span class="pun" style="color: #666666;">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;animationLoop</span><span class="pun" style="color: #666666;">(time)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Measure time with high resolution timer</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;now&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;time</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// How long between the current frame and the previous one?</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;delta&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;now&nbsp;</span><span class="pun" style="color: #666666;">-</span><span class="pln">&nbsp;then</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">if</span><span class="pun" style="color: #666666;">(</span><span class="pln">totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #666666;">&gt;</span><span class="pln">&nbsp;delayInMs</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Compute the displacement in x (in pixels) in function of the time elapsed</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp; &nbsp; &nbsp;// since the last draw and</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// in function of the wanted speed. This time, instead of delta we</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// use totalTimeSinceLastRedraw as we're not always drawing at</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// each execution of mainloop</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;incX&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;calcDistanceToMove</span><span class="pun" style="color: #666666;">(</span><strong style="color: red;"><span class="pln">totalTimeSinceLastRedraw</span></strong><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;speedX</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// an animation involves: 1) clear canvas and 2) draw shapes,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// 3) move shapes, 4) recall the loop with requestAnimationFrame</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// clear canvas</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">clearRect</span><span class="pun" style="color: #666666;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;height</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun" style="color: #666666;">.</span><span class="pln">strokeRect</span><span class="pun" style="color: #666666;">(</span><span class="pln">x</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// move rectangle</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;x&nbsp;</span><span class="pun" style="color: #666666;">+=</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// check collision on left or right</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">if</span><span class="pun" style="color: #666666;">((</span><span class="pln">x</span><span class="pun" style="color: #666666;">+</span><span class="lit" style="color: #006666;">10</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">&gt;=</span><span class="pln">&nbsp;width</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">||</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">(</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #666666;">&lt;=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666666;">))</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// cancel move + inverse speed</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; x&nbsp;</span><span class="pun" style="color: #666666;">-=</span><span class="pln">&nbsp;incX</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; speedX&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">-</span><span class="pln">speedX</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong style="color: red;">&nbsp;</strong></span><strong style="color: red;"><span class="com" style="color: #880000;">// reset the total time since last redraw</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp; totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #666666;">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">}</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">else</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">// sum the total time since last redraw</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #666666;">+=</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Store time</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;then&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #666666;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// animate.&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestAnimationFrame</span><span class="pun" style="color: #666666;">(</span><span class="pln">animationLoop</span><span class="pun" style="color: #666666;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">}</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;calcDistanceToMove&nbsp;</span><span class="pun" style="color: #666666;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666666;">(</span><span class="pln">delta</span><span class="pun" style="color: #666666;">,</span><span class="pln">&nbsp;speed</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">return</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">(</span><span class="pln">speed&nbsp;</span><span class="pun" style="color: #666666;">*</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #666666;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">/</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1000</span><span class="pun" style="color: #666666;">;</span><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #666666;">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;/script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;body</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">onload</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"</span><span class="pln">init</span><span class="pun" style="color: #666666;">();</span><span class="atv" style="color: #008800;">"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;canvas</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">id</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"mycanvas"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">width</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"200"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">height</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"50"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">style</span><span class="pun" style="color: #666666;">=</span><span class="atv" style="color: #008800;">"</span><span class="pln">border</span><span class="pun" style="color: #666666;">:</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2px</span><span class="pln">&nbsp;solid black</span><span class="atv" style="color: #008800;">"</span><span class="tag" style="color: #008888;">&gt;&lt;/canvas&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/html&gt;</span></li>
</ol></div><br>


#### Can we use setInterval?

It's quite possible to use `setInterval(function, interval)` if you do not need an accurate scheduling.

To animate a monster at 60 fps but blinking his eyes once per second, you would use a mainloop with `requestAnimationFrame` and target a 60 fps animation, but you would also have a call to `setInterval(changeEyeColor, 1000);` and the changeEyeColor function will update a global variable, `eyeColor`, every second, which will be taken into account within the `drawMonster` function, called 60 times/s from the mainloop.


#### Notes for 2.4.3 Setting the frame rate

+ Frame rate
  + ignore some frames to reach desired frame rate w/ `requestAnimationFrame`
  + possible to set the frame rate using time based nimation
    + set a global variable corresponding to the desired frame rate
    + compare the elapsed time btw two executions of the animation loop
      + time elapsed too short for the target frame rate: do nothing
      + time elapsed exceeding the delay corresponding to the choosen frame rate: draw the frame and reset the time to zero
  + change frame rate: `setFrameRateInFramesPerSecond(nb);`

+ Example: change frame rate
  + access canvas element: `var canvas = document.querySelector("#myCanvas"); var ctx = canvas.getContext("2d");`
  + declare variable: `var width = canvas.width, height = canvas.width;; var lastX = width * Math.random(); var lastY = height * Math.random(); var hue =0;`
  + call to set frame rate: `setFrameRateInFramesPerSecond(60);`
  + declared time relatred variables: `var now, delta, delayInMS, totalTimeSinceLastDraw = 0; var then = performance.now();`
  + call to start animation: `requestAnimationFrame(mainloop);`
  + set frame rate<a name="frameRate"></a>: `function setFrameRateInFramesPerSecond(frameRate) { delayInMS = 1000/frameRate; }`
  + generate animation loop: `function mainloop(time) {...}`
    + set time-related variables: `now = time; delta = now = tehn;`
    + check time to redraw: `if (totalTimeSinceLastRedraw > delayInMS) {...}`
      + save context: `ctx.save();`
      + draw blurred rectangle: `ctx.fillStyle = "rgba(0, 0, 0, 0.1); ctx.fillRect(0, 0, width, height);`
      + translate the ctx: `ctx.translate(width/2, height/2); ctx.scale(0.9, 0.9); ctx.translate(-width/2, -height/2);`
      + begin a new draw: `ctx.beginPath();`
      + set style and position for new curve: `ctx.lineWidth = 5 + Math.random() * 10; ctx.moveTo(lastX, lastY);`
      + set end position for curve: `lastX = width * Math.random(); lastY = height * Math.random();`
      + set curve path: `ctx.beizierCurveTo(width*Math.random(), height*Math.random(), width*Math.random(), height*Math.random(), lastX, lastY);`
      + set curve style and draw: `hue = hue + 10 * Math.random(); ctx.strokeStyle = "hsl(" + hue + ", 50%, 50%)"; ctx.shadowColor = "white"; ctx.shadowBlur = 10; ctx.stroke();`
      + restore ctx: `ctx.restore();`
      + reset last redraw time: `totalTimeLastSinceRedraw = 0;`
    + increase time if redraw not reached: `else { totalTimeSinceLastRedraw += delta; }`
    + call for next frame: `requestAnimationFrame();`

+ Example: bouncing rectangle w/ adjustable frame rate
  + [declare variables](#vars)
  + declare time-related variables: `var now, delta, delayInMS, totalTimeSinceLastRedraw = 0; var then = performance.now();`
  + call to set frame rate: `setFramerateInFramesPerSeconf(25);`
  + set [frame rate](#frameRate)
  + [init page after DOM ready](#init) w/ speed change `speedX = 2000;`
  + generate animation loop: `function mainloop(time) {...}`
    + set time variables: `now = time; delta = now -then;`
    + check time to redraw: `if (totalTimeSinceLastRedraw > delayInMS) {...}`
      + call to calculate distance to move: `incX = calcDisatnceToMove(totalTimeSinceLastRedraw, speedX);`
      + perform animation: `ctx.clearRect(0, 0, width, height); ctx.strokeRect(x, y, 10, 10); x += incX; if ((x+10 >= 10) || (x<=0)) {x -= incX; speedX = -speedX;}`
      + reset redraw time: `totalTimeSinceLastRedraw = 0;`
    + increase time w/p redraw: `else {totalTimeSinceLastRedraw += delta;}`
    + store time: `then = now;`
    + call for next frame: `requestAnimarionFrame(mainloop);`
  + calculate [distance to move](#calcDist)







