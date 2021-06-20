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
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">50000000</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// slow down artificially the animation</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></strong></li>
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
  + declare variables: `var canvas, ctx; var width, height; var x, y; var speed;`
  + init page after DOM ready: `function init() {...}`
    + init variables: `canvas = document.queryAnimationFrame("#myCanvas"); ctx = canvas.getContext('2d'); width = canvas.width = width; height = canvas.height; x= 10; y = 10;`
    + set speed: `speedX = 3;`
    + start animation: `animationLoop();`
  + generate animation loop<a name="animationLoop"></a>: `function animationLoop() {...}`
    + clear canvas: `ctx.cleanRec(0, 0, 10, 10);`
    + draw shape: `ctx.strokeRect(x, y, 10, 10);`
    + move rectangle: `x += speedX;`
    + check collision on left and right: `if (((x+5) > width) || (x <= 0)) { x -= speedX; speedX = -speedX; }`
    + call next frame: `requestAnimationFrame(animationLoop);`

+ Example: simulating a low-end device
  + generate [animation loop](#animationLoop)
  + additional loop to slow the animaton loop after clear rectangle: `for (var i=0; i<50000000; i++) { // slow down artifically the animation };`







