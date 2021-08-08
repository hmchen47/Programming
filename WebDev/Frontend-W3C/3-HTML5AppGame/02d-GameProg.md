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
2. draw the shapes,
3. move the shapes,
4. go to step 1.

When we use requestAnimationFrame for implementing such an animation, as we did in the previous lessons, the browser tries to keep the frame-rate at 60 fps, meaning that the ideal time between frames will be 1/60 second = 16.66 ms.


#### Example #1: no use of time-based animation

[Online example at JSBin](https://jsbin.com/dibuze/edit)

[Local Demo](src/02d-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3gJ34xX')"
    src    = "https://bit.ly/3iU60KX"
    alt    = "image of a small rectangle in a canvas, moving from left to right"
    title  = "image of a small rectangle in a canvas, moving from left to right"
  />
</figure>

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li>&nbsp; &lt;meta charset=utf-8 /&gt;</li>
<li>&nbsp; &lt;title&gt;Small animation example&lt;/title&gt;</li>
<li>&nbsp;&nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp;&nbsp;var canvas, ctx;</li>
<li>&nbsp; &nbsp;&nbsp;var width, height;</li>
<li>&nbsp; &nbsp;&nbsp;var x, y;</li>
<li>&nbsp; &nbsp;&nbsp;var speedX;</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// Called after the DOM is ready (page loaded)</li>
<li>&nbsp; &nbsp;&nbsp;function init() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// init the different variables</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;canvas = document.querySelector("#mycanvas");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx = canvas.getContext('2d');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;width = canvas.width;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;height = canvas.height;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;x=10; y = 10;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Move 3 pixels left or right at each frame</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;speedX = 3;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Start animation</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;animationLoop();</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;function animationLoop() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// an animation involves: 1) clear canvas and 2) draw shapes, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// 3) move shapes, 4) recall the loop with requestAnimationFrame</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// clear canvas</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx.clearRect(0, 0, width, height);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx.strokeRect(x, y, 10, 10);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// move rectangle</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;x += speedX;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// check collision on left or right</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if(((x+5) &gt; width) || (x &lt;= 0)) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// cancel move + inverse speed</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x -= speedX;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedX = -speedX;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// animate.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;requestAnimationFrame(animationLoop);</li>
<li>&nbsp; &nbsp;&nbsp;} </li>
<li> &lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li> </li>
<li>&lt;body onload="init();"&gt;</li>
<li> &lt;canvas id="mycanvas" width="200" height="50" style="border: 2px solid black"&gt;</li>
<li>&nbsp;&lt;/canvas&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

If you try this example on a low-end smartphone (use this URL for the example in stand-alone mode) and if you run it at the same time on a desktop PC, it is obvious that the rectangle moves faster on the desktop computer screen than on your phone.

This is because the frame rate differs between the computer and the smartphone: perhaps 60 fps on the computer and 25 fps on the phone. As we only move the rectangle in the animationLoop, in one second the rectangle will be moved 25 times on the smartphone compared with 60 times on the computer! Since we move the rectangle the same number of pixels each time, the rectangle moves faster on the computer!

#### Example #2: simulating a low-end device

Here is the same example to which we have added a loop that wastes time right in the middle of the animation loop. It will artificially extend the time spent inside the animation loop, making the 1/60th of second ideal impossible to reach.

[Try it on JsBin](https://jsbin.com/remide/edit) and notice that the square moves much slower on the screen. Indeed, its speed is a direct consequence of the extra time spent in the animation loop.

[Local Demo](src/02d-example02.html)

<div><ol>
<li value="1"> function animationLoop() {</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">for(var i = 0; i &lt; 50000000; i++) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp;// slow down artificially the animation</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;}</strong></li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp; requestAnimationFrame(animationLoop);</li>
<li> } </li>
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
    + many game consoles limit the frame-rate tp 1/30th of a second

+ Procedure to measure time btw frames
  1. erase the canvas
  2. draw the shapes
  3. move the shapes
  4. go to the 1st step

+ Example: regular animation
  + rectangle moves faster on the desktop computer screen that on mobile phone
  + declare variables: `var canvas, ctx; var width, height; var x, y; var speedX;`
  + init page after DOM ready<a name="init"></a>: `function init() {...}`
    + init variables: `canvas = document.querySelector("#myCanvas"); ctx = canvas.getContext('2d'); width = canvas.width; height = canvas.height; x= 10; y = 10;`
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
  + additional loop to slow the animaton loop after clear rectangle<a name="simulation"></a>: `for (var i=0; i<50000000; i++) { // slow down artificially the animation }`


### 2.4.2 Measuring time between frames

Let's find out how to measuring time between frames to achieve a constant speed on screen, even when the frame rate changes.

#### Method #1: using the JavaScript Date object

Let's modify the example from the previous lesson slightly by adding a _time-based animation_.  Here we use the "standard JavaScript" way for measuring time, using JavaScript's Date object:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">var&nbsp;time&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #008888;">new&nbsp;<span style="color: #aa0066;">Date<span style="color: #669900;">().getTime<span style="color: #669900;">();</li>
</ol></div><br>

The `getTime()` method returns the number of milliseconds since midnight on January 1, 1970. This is the number of milliseconds that have elapsed during the Unix epoch (!).

There is an alternative. We could have called:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">var&nbsp;time&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #aa0066;">Date<span style="color: #669900;">.now<span style="color: #669900;">();</li>
</ol></div><br>

So, if we measure the time at the beginning of each animation loop, and store it, we can then compute the delta of times elapsed between two consecutive loops.

We then apply some simple math to compute the number of pixels we need to move the shape to achieve a given speed (in pixels/s).


__Example #1: using time based animation: the bouncing square__

[Online example at JSBin](https://jsbin.com/riferi/edit):

[Local Demo](src/02d-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3cYaKeJ')"
    src    = "https://bit.ly/3gF086H"
    alt    = "Bouncing square with time bases animation"
    title  = "Bouncing square with time bases animation"
  />
</figure>


Source code from the example:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #aa0066;">&lt;!DOCTYPE html&gt;</li>
<li><span style="color: #008888;">&lt;html&nbsp;<span style="color: #aa0066;">lang<span style="color: #669900;">=<span style="color: #008800;">"en"<span style="color: #008888;">&gt;</li>
<li><span style="color: #008888;">&lt;head&gt;</li>
<li><span style="color: #008888;">&nbsp; &lt;meta&nbsp;<span style="color: #aa0066;">charset<span style="color: #669900;">=<span style="color: #008800;">utf-8&nbsp;<span style="color: #008888;">/&gt;</li>
<li><span style="color: #008888;">&nbsp; &lt;title&gt;Move rectangle using time based animation<span style="color: #008888;">&lt;/title&gt;</li>
<li>&nbsp;&nbsp;<span style="color: #008888;">&lt;script&gt;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">var&nbsp;canvas<span style="color: #669900;">,&nbsp;ctx<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">var&nbsp;width<span style="color: #669900;">,&nbsp;height<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">var&nbsp;x<span style="color: #669900;">,&nbsp;y<span style="color: #669900;">,&nbsp;incX<span style="color: #669900;">;&nbsp;<span style="color: #880000;">// incX is the distance from the previously drawn</li>
<li><span style="color: #880000;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // rectangle to the new one</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;"><span style="color: #008888;">var&nbsp;speedX<span style="color: #669900;">;&nbsp;<span style="color: #880000;">// speedX is the target speed of the rectangle, in pixels/s</strong></li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;"><span style="color: #880000;">// for time based animation</strong></li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;"><span style="color: #008888;">var&nbsp;now<span style="color: #669900;">,&nbsp;delta<span style="color: #669900;">;</strong></li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;"><span style="color: #008888;">var&nbsp;then&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #008888;">new&nbsp;<span style="color: #aa0066;">Date<span style="color: #669900;">().getTime<span style="color: #669900;">();</strong></li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Called after the DOM is ready (page loaded)</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">function&nbsp;init<span style="color: #669900;">()&nbsp;<span style="color: #669900;">{</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Init the different variables</li>
<li>&nbsp; &nbsp; &nbsp; canvas&nbsp;<span style="color: #669900;">=&nbsp;document<span style="color: #669900;">.querySelector<span style="color: #669900;">(<span style="color: #008800;">"#mycanvas"<span style="color: #669900;">);</li>
<li>&nbsp; &nbsp; &nbsp; ctx&nbsp;<span style="color: #669900;">=&nbsp;canvas<span style="color: #669900;">.getContext<span style="color: #669900;">(<span style="color: #008800;">'2d'<span style="color: #669900;">);</li>
<li>&nbsp; &nbsp; &nbsp; width&nbsp;<span style="color: #669900;">=&nbsp;canvas<span style="color: #669900;">.width<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp; &nbsp; height&nbsp;<span style="color: #669900;">=&nbsp;canvas<span style="color: #669900;">.height<span style="color: #669900;">;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; x<span style="color: #669900;">=<span style="color: #006666;">10<span style="color: #669900;">;&nbsp;y&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #006666;">10<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Target speed in pixels/second, try with high values, 1000, 2000...</li>
<li>&nbsp; &nbsp; &nbsp; speedX&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #006666;">200<span style="color: #669900;">;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Start animation</li>
<li>&nbsp; &nbsp; &nbsp;animationLoop<span style="color: #669900;">();</li>
<li>&nbsp; &nbsp;<span style="color: #669900;">}</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">function&nbsp;animationLoop<span style="color: #669900;">()&nbsp;<span style="color: #669900;">{</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;"><span style="color: #880000;">// Measure time</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">now&nbsp;</strong><strong style="color: red;"><span style="color: #669900;">=&nbsp;<span style="color: #008888;">new&nbsp;<span style="color: #aa0066;">Date<span style="color: #669900;">().getTime<span style="color: #669900;">();</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// How long between the current frame and the previous one?</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">delta&nbsp;</strong><strong style="color: red;"><span style="color: #669900;">=&nbsp;now&nbsp;<span style="color: #669900;">-&nbsp;then<span style="color: #669900;">;</strong></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">//console.log(delta);</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Compute the displacement in x (in pixels) in function of the time elapsed and</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// in function of the wanted speed</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">incX&nbsp;</strong><strong style="color: red;"><span style="color: #669900;">=&nbsp;calcDistanceToMove<span style="color: #669900;">(delta<span style="color: #669900;">,&nbsp;speedX<span style="color: #669900;">);</strong></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// an animation involves: 1) clear canvas and 2) draw shapes,</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// 3) move shapes, 4) recall the loop with requestAnimationFrame</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// clear canvas</li>
<li>&nbsp; &nbsp; &nbsp;ctx<span style="color: #669900;">.clearRect<span style="color: #669900;">(<span style="color: #006666;">0<span style="color: #669900;">,&nbsp;<span style="color: #006666;">0<span style="color: #669900;">,&nbsp;width<span style="color: #669900;">,&nbsp;height<span style="color: #669900;">);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;ctx<span style="color: #669900;">.strokeRect<span style="color: #669900;">(x<span style="color: #669900;">,&nbsp;y<span style="color: #669900;">,&nbsp;<span style="color: #006666;">10<span style="color: #669900;">,&nbsp;<span style="color: #006666;">10<span style="color: #669900;">);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// move rectangle</li>
<li>&nbsp; &nbsp; &nbsp;x&nbsp;<span style="color: #669900;">+=&nbsp;incX<span style="color: #669900;">;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// check collision on left or right</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #008888;">if<span style="color: #669900;">((x<span style="color: #669900;">+<span style="color: #006666;">10&nbsp;<span style="color: #669900;">&gt;=&nbsp;width<span style="color: #669900;">)&nbsp;<span style="color: #669900;">||&nbsp;<span style="color: #669900;">(x&nbsp;<span style="color: #669900;">&lt;=&nbsp;<span style="color: #006666;">0<span style="color: #669900;">))&nbsp;<span style="color: #669900;">{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// cancel move + inverse speed</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; x&nbsp;<span style="color: #669900;">-=&nbsp;incX<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; speedX&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #669900;">-speedX<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #669900;">}</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;"><span style="color: #880000;">// Store time</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">then&nbsp;</strong><strong style="color: red;"><span style="color: #669900;">=&nbsp;now<span style="color: #669900;">;</strong></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;requestAnimationFrame<span style="color: #669900;">(animationLoop<span style="color: #669900;">);</li>
<li>&nbsp;<span style="color: #669900;">}</li>
<li></li>
<li></li>
<li></li>
<li>&nbsp;<span style="color: #880000;">// We want the rectangle to move at a speed given in pixels/second</li>
<li><span style="color: #880000;">&nbsp;// (there are 60 frames in a second)</li>
<li>&nbsp;<span style="color: #880000;">// If we are really running at 60 frames/s, the delay between </li>
<li><span style="color: #880000;">&nbsp;// frames should be 1/60</li>
<li>&nbsp;<span style="color: #880000;">// = 16.66 ms, so the number of pixels to move = (speed * del)/1000. </li>
<li><span style="color: #880000;">&nbsp;// If the delay&nbsp;is twice as</li>
<li>&nbsp;<span style="color: #880000;">// long, the formula works: let's move the rectangle for twice as long!</li>
<li><strong style="color: red;">&nbsp;<span style="color: #008888;">var&nbsp;calcDistanceToMove&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #008888;">function<span style="color: #669900;">(delta<span style="color: #669900;">,&nbsp;speed<span style="color: #669900;">)&nbsp;<span style="color: #669900;">{</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;<span style="color: #008888;">return&nbsp;<span style="color: #669900;">(speed&nbsp;<span style="color: #669900;">*&nbsp;delta<span style="color: #669900;">)&nbsp;<span style="color: #669900;">/&nbsp;<span style="color: #006666;">1000<span style="color: #669900;">;</strong></li>
<li><strong style="color: red;">&nbsp;<span style="color: #669900;">}</strong></li>
<li></li>
<li>&nbsp;<span style="color: #008888;">&lt;/script&gt;</li>
<li><span style="color: #008888;">&lt;/head&gt;</li>
<li></li>
<li><span style="color: #008888;">&lt;body&nbsp;<span style="color: #aa0066;">onload<span style="color: #669900;">=<span style="color: #008800;">"init<span style="color: #669900;">();<span style="color: #008800;">"<span style="color: #008888;">&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;canvas&nbsp;<span style="color: #aa0066;">id<span style="color: #669900;">=<span style="color: #008800;">"mycanvas"&nbsp;<span style="color: #aa0066;">width<span style="color: #669900;">=<span style="color: #008800;">"200"&nbsp;<span style="color: #aa0066;">height<span style="color: #669900;">=<span style="color: #008800;">"50"&nbsp;<span style="color: #aa0066;">style<span style="color: #669900;">=<span style="color: #008800;">"border<span style="color: #669900;">:&nbsp;<span style="color: #006666;">2px&nbsp;solid black<span style="color: #008800;">"<span style="color: #008888;">&gt;&lt;/canvas&gt;</li>
<li><span style="color: #008888;">&lt;/body&gt;</li>
<li><span style="color: #008888;">&lt;/html&gt;</li>
</ol></div><br>

In this example, we only added a few lines of code for measuring the time and computing the time elapsed between two consecutive frames (see line 38). Normally, requestAnimationFrame(callback) tries to call the callback function every 16.66 ms (this corresponds to 60 frames/s)... but this is never exactly the case. If you do a console.log(delta)in the animation loop, you will see that even on a very powerful computer, the delta is "very close" to 16.6666 ms, but 99% of the time it will be slightly different.

The function `calcDistanceToMove(delta, speed)` takes two parameters: 1) the time elapsed in ms, and 2) the target speed in pixels/s. 

Try this example on a smartphone, use this [link](https://jsbin.com/jeribi) to run the JSBin example in stand-alone mode. Normally you should see no difference in speed, but it may look a bit jerky on a low-end smartphone or on a slow computer. _This is the correct behavior._

Or you can try the next example that simulates a complex animation loop that takes a long time to draw each frame...


__Example #2: using a simulation that spends a lot of time in the animation loop, to compare with the previous example__

[Try it on JsBin](https://jsbin.com/jeribi/edit):

[Local Demo](src/02d-example04.html)

We added a long loop in the middle of the animation loop. This time, the animation should be very jerky. However, notice that the apparent speed of the square is the same as in the previous example: the animation adapts itself!

<div><ol>
<li value="1"> function animationLoop() {</li>
<li>&nbsp; &nbsp;// Measure time</li>
<li>&nbsp; now = new Date().getTime();</li>
<li>&nbsp;</li>
<li>&nbsp; // How long between the current frame and the previous one ?</li>
<li>&nbsp; delta = now - then;</li>
<li>&nbsp;&nbsp;//console.log(delta);</li>
<li>&nbsp;&nbsp;// Compute the displacement in x (in pixels) in function of the time elapsed and</li>
<li>&nbsp;&nbsp;// in function of the wanted speed</li>
<li>&nbsp; incX = calcDistanceToMove(delta, speedX);</li>
<li> </li>
<li>&nbsp;&nbsp;// an animation is : 1) clear canvas and 2) draw shapes, </li>
<li>&nbsp;&nbsp;// 3) move shapes, 4) recall the loop with requestAnimationFrame</li>
<li> </li>
<li>&nbsp;&nbsp;// clear canvas</li>
<li>&nbsp; ctx.clearRect(0, 0, width, height);</li>
<li> </li>
<li>&nbsp;&nbsp;<strong style="color: red;">for(var i = 0; i &lt; 50000000; i++) {</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;&nbsp;// just to slow down the animation</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;}</strong></li>
<li> </li>
<li>&nbsp; ctx.strokeRect(x, y, 10, 10);</li>
<li> </li>
<li>&nbsp;&nbsp;// move rectangle</li>
<li>&nbsp; x += incX;</li>
<li> </li>
<li>&nbsp;&nbsp;// check collision on left or right</li>
<li>&nbsp;&nbsp;if((x+10 &gt;= width) || (x &lt;= 0)) {</li>
<li>&nbsp; &nbsp;// cancel move + inverse speed</li>
<li>&nbsp; &nbsp;x -= incX;</li>
<li>&nbsp; &nbsp;speedX = -speedX;</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp;&nbsp;// Store time</li>
<li>&nbsp;&nbsp;then = now;</li>
<li> </li>
<li>&nbsp; requestAnimationFrame(animationLoop);</li>
<li> } </li>
</ol></div><br>


#### Method #2: using the new HTML5 high-resolution timer

Since the beginning of HTML5, game developers, musicians, and others have asked for a sub-millisecond timer to be able to avoid some glitches that occur with the regular JavaScript timer. This API is called the "[High Resolution Time API](https://www.w3.org/TR/hr-time/)".

This API is very simple to use - just do:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">var&nbsp;time&nbsp;<span style="color: #669900;">=&nbsp;performance<span style="color: #669900;">.now<span style="color: #669900;">();</li>
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

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1">&nbsp;<span style="color: #669900;">...</li>
<li>&nbsp;<span style="color: #008800;">&lt;script&gt;</li>
<li>&nbsp; &nbsp;<span style="color: #669900;">...</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;speedX<span style="color: #669900;">;&nbsp;<span style="color: #880000;">// speedX is the target speed of the rectangle in pixels/s</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// for time based animation</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;now<span style="color: #669900;">,&nbsp;delta<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp;<strong style="color: red;"><span style="color: #880000;">// High resolution timer</strong></li>
<li>&nbsp; &nbsp;<strong style="color: red;"><span style="color: #008888;">var&nbsp;<span style="color: #008888;">then&nbsp;<span style="color: #669900;">=&nbsp;performance<span style="color: #669900;">.now<span style="color: #669900;">();</strong></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// Called after the DOM is ready (page loaded)</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">function&nbsp;init<span style="color: #669900;">()&nbsp;<span style="color: #669900;">{</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #669900;">...</li>
<li>&nbsp; &nbsp;<span style="color: #669900;">}</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">function&nbsp;animationLoop<span style="color: #669900;">()&nbsp;<span style="color: #669900;">{</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;"><span style="color: #880000;">// Measure time, with high resolution timer</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">now&nbsp;</strong><strong style="color: red;"><span style="color: #669900;">=&nbsp;performance<span style="color: #669900;">.now<span style="color: #669900;">();</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// How long between the current frame and the previous one?</li>
<li>&nbsp; &nbsp; delta&nbsp;<span style="color: #669900;">=&nbsp;now&nbsp;<span style="color: #669900;">-&nbsp;<span style="color: #008888;">then<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">//console.log(delta);</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Compute the displacement in x (in pixels) in function </li>
<li><span style="color: #880000;">&nbsp; &nbsp; // of the time elapsed and</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// in function of the wanted speed</li>
<li>&nbsp; &nbsp; incX&nbsp;<span style="color: #669900;">=&nbsp;calcDistanceToMove<span style="color: #669900;">(delta<span style="color: #669900;">,&nbsp;speedX<span style="color: #669900;">);</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">//console.log("dist = " + incX);</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// an animation involves: 1) clear canvas and 2) draw shapes,</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// 3) move shapes, 4) recall the loop with requestAnimationFrame</li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// clear canvas</li>
<li>&nbsp; &nbsp;ctx<span style="color: #669900;">.clearRect<span style="color: #669900;">(<span style="color: #006666;">0<span style="color: #669900;">,&nbsp;<span style="color: #006666;">0<span style="color: #669900;">,&nbsp;width<span style="color: #669900;">,&nbsp;height<span style="color: #669900;">);</li>
<li></li>
<li>&nbsp; &nbsp;ctx<span style="color: #669900;">.strokeRect<span style="color: #669900;">(x<span style="color: #669900;">,&nbsp;y<span style="color: #669900;">,&nbsp;<span style="color: #006666;">10<span style="color: #669900;">,&nbsp;<span style="color: #006666;">10<span style="color: #669900;">);</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// move rectangle</li>
<li>&nbsp; &nbsp;x&nbsp;<span style="color: #669900;">+=&nbsp;incX<span style="color: #669900;">;</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// check collision on left or right</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">if<span style="color: #669900;">((x<span style="color: #669900;">+<span style="color: #006666;">10&nbsp;<span style="color: #669900;">&gt;=&nbsp;width<span style="color: #669900;">)&nbsp;<span style="color: #669900;">||&nbsp;<span style="color: #669900;">(x&nbsp;<span style="color: #669900;">&lt;=&nbsp;<span style="color: #006666;">0<span style="color: #669900;">))&nbsp;<span style="color: #669900;">{</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// cancel move + inverse speed</li>
<li>&nbsp; &nbsp; &nbsp; x&nbsp;<span style="color: #669900;">-=&nbsp;incX<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp; &nbsp; speedX&nbsp;<span style="color: #669900;">=&nbsp;<span style="color: #669900;">-speedX<span style="color: #669900;">;</li>
<li>&nbsp; &nbsp;<span style="color: #669900;">}</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// Store time</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">then&nbsp;<span style="color: #669900;">=&nbsp;now<span style="color: #669900;">;</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// call the animation loop again</li>
<li>&nbsp; &nbsp;requestAnimationFrame<span style="color: #669900;">(animationLoop<span style="color: #669900;">);</li>
<li>&nbsp;<span style="color: #669900;">}</li>
<li>&nbsp;<span style="color: #669900;">...</li>
<li></li>
<li>&nbsp;<span style="color: #669900;">&lt;/script<span style="color: #669900;">&gt;</li>
</ol></div><br>

Only two lines have changed but the accuracy is much higher, if you uncomment the console.log(...) calls in the main loop. You will see the difference.


#### Method #3: using timestamp parameter of requestAnimationFrame

__Method #3: using the optional timestamp parameter of the callback function of requestAnimationFrame__

<p style="text-align: center;"><span style="color: #ff0000;"><strong style="color: red;"><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">This is the recommended method!</strong></p>

There is an optional parameter that is passed to the callback function called by `requestAnimationFrame`: a timestamp!

[The requestAnimationFrame API specification](https://www.w3.org/TR/html51/webappapis.html#animation-frames) says that this timestamp corresponds to the time elapsed since the page has been loaded.

It is similar to the value sent by the high resolution timer using `performance.now()`.

Here is a running example  of the animated rectangle, that uses this `timestamp` parameter.

[Online example at JSBin](https://jsbin.com/kuvumu/edit):

[Local Demo](src/02d-example06.html)

Source code of the example:

<div style="line-height: 25.6px;"><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html&nbsp;lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li>&lt;meta&nbsp;charset=utf-8&nbsp;/&gt;</li>
<li>&lt;title&gt;Time based animation using the parameter of the requestAnimationFrame callback&lt;/title&gt;</li>
<li>&nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp;var&nbsp;canvas,&nbsp;ctx;</li>
<li>&nbsp; &nbsp;var&nbsp;width,&nbsp;height;</li>
<li>&nbsp; &nbsp;var&nbsp;x,&nbsp;y,&nbsp;incX;&nbsp;// incX is the distance from the previously drawn rectangle</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// to the new one</li>
<li>&nbsp; &nbsp;var&nbsp;speedX;&nbsp; &nbsp; &nbsp;// speedX is the target speed of the rectangle in pixels/s</li>
<li></li>
<li>&nbsp; &nbsp;// for time based animation</li>
<li>&nbsp; &nbsp;var&nbsp;now,&nbsp;delta=0;</li>
<li>&nbsp; &nbsp;// High resolution timer</li>
<li>&nbsp; &nbsp;var&nbsp;oldTime&nbsp;=&nbsp;0;</li>
<li></li>
<li>&nbsp; &nbsp;// Called after the DOM is ready (page loaded)</li>
<li>&nbsp; &nbsp;function&nbsp;init()&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp;// init the different variables</li>
<li>&nbsp; &nbsp; &nbsp;canvas&nbsp;=&nbsp;document.querySelector("#mycanvas");</li>
<li>&nbsp; &nbsp; &nbsp;ctx&nbsp;=&nbsp;canvas.getContext('2d');</li>
<li>&nbsp; &nbsp; &nbsp;width&nbsp;=&nbsp;canvas.width;</li>
<li>&nbsp; &nbsp; &nbsp;height&nbsp;=&nbsp;canvas.height;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;x=10;&nbsp;y&nbsp;=&nbsp;10;</li>
<li>&nbsp; &nbsp; &nbsp;// Target speed in pixels/second, try with high values, 1000, 2000...</li>
<li>&nbsp; &nbsp; &nbsp;speedX&nbsp;=&nbsp;200;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;// Start animation</li>
<li>&nbsp; &nbsp; &nbsp;requestAnimationFrame(animationLoop);</li>
<li>&nbsp; &nbsp;}</li>
<li></li>
<li>&nbsp; &nbsp;function&nbsp;animationLoop(<strong style="color: red;">currentTime</strong>)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp;// How long between the current frame and the previous one?</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">delta&nbsp;</strong><strong style="color: red;">=&nbsp;currentTime&nbsp;-&nbsp;oldTime;</strong></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;// Compute the displacement in x (in pixels) in function of the time elapsed and</li>
<li>&nbsp; &nbsp; &nbsp;// in function of the wanted speed</li>
<li>&nbsp; &nbsp; &nbsp;incX&nbsp;=&nbsp;calcDistanceToMove(delta,&nbsp;speedX);</li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;&nbsp;// clear canvas</li>
<li>&nbsp; &nbsp; &nbsp;ctx.clearRect(0,&nbsp;0,&nbsp;width,&nbsp;height);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;ctx.strokeRect(x,&nbsp;y,&nbsp;10,&nbsp;10);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;// move rectangle</li>
<li>&nbsp; &nbsp; &nbsp;x&nbsp;+=&nbsp;incX;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;// check collision on left or right</li>
<li>&nbsp; &nbsp; &nbsp;if(((x+10)&nbsp;&gt;&nbsp;width)&nbsp;||&nbsp;(x&nbsp;&lt;&nbsp;0))&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// inverse speed</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;x&nbsp;-=&nbsp;incX;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;speedX&nbsp;=&nbsp;-speedX;</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;// Store time</li>
<li>&nbsp; &nbsp; &nbsp;oldTime&nbsp;=&nbsp;currentTime;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;// asks for next frame</li>
<li>&nbsp; &nbsp; &nbsp;requestAnimationFrame(animationLoop);</li>
<li>&nbsp; &nbsp;}</li>
<li></li>
<li>&nbsp; &nbsp;var&nbsp;calcDistanceToMove&nbsp;=&nbsp;function(delta,&nbsp;speed)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp;return&nbsp;(speed&nbsp;*&nbsp;delta)&nbsp;/&nbsp;1000;</li>
<li>&nbsp; &nbsp;}</li>
<li></li>
<li>&nbsp;&lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li></li>
<li>&lt;body&nbsp;onload="init();"&gt;</li>
<li>&nbsp;&lt;canvas&nbsp;id="mycanvas"&nbsp;width="200"&nbsp;height="50"&nbsp;style="border:&nbsp;2px&nbsp;solid black"&gt;&lt;/canvas&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>


#### Notes for 2.4.2 Measuring time between frames

+ Methods to measure time btw frames
  + using the JavaScript `Date` object
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
      + get a sub-millisecond timestamp
      + similar to `Date.now()` but w/ much higher accuracy
      + return a floating point number, called a `DOMHighResTimeStamp`
  + using timestamps parameter of the callback function of `requestAnimationFrame`
    + recommended method
    + timestamps as optional parameter
    + corresponding to the time elapsed since the page loaded
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

+ Example: using timestamps parameter of `requestAnimationFrame`
  + [declar variables](#vars) w/ `var oldTime = 0;`
  + [declar time-related variables](#timeVars)
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

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1">setFrameRateInFramesPerSecond<span style="color: #bb6600;">(<span style="color: #006666;">5<span style="color: #bb6600;">);&nbsp;<span style="color: #880000;">// try other values!</li>
</ol></div><br>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3gGsRYD')"
    src    = "https://bit.ly/3iYegcK"
    alt    = "Screenshot of a jsbin example with an animated curve, we can set the framerate in this example..."
    title  = "Screenshot of a jsbin example with an animated curve, we can set the framerate in this example..."
  />
</figure>

Source code of the example:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #aa0066;">&lt;!DOCTYPE html&gt;</li>
<li><span style="color: #008888;">&lt;html&nbsp;<span style="color: #aa0066;">lang<span style="color: #bb6600;">=<span style="color: #008800;">"en"<span style="color: #008888;">&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;head&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;meta&nbsp;<span style="color: #aa0066;">charset<span style="color: #bb6600;">=<span style="color: #008800;">utf-8&nbsp;<span style="color: #008888;">/&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;title&gt;Set framerate using a high resolution timer<span style="color: #008888;">&lt;/title&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;/head&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;body&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;p&gt;This example measures and sums deltas of time between consecutive frames of animation. It includes a&nbsp;<span style="color: #008888;">&lt;code&gt;setFrameRateInFramesPerSecond<span style="color: #008888;">&lt;/code&gt;&nbsp;function you can use to reduce the number of frames per second of the main animation.<span style="color: #008888;">&lt;/p&gt;</li>
<li>&nbsp;</li>
<li>&nbsp;<span style="color: #008888;">&lt;canvas&nbsp;<span style="color: #aa0066;">id<span style="color: #bb6600;">=<span style="color: #008800;">"myCanvas"&nbsp;<span style="color: #aa0066;">width<span style="color: #bb6600;">=<span style="color: #008800;">"700"&nbsp;<span style="color: #aa0066;">height<span style="color: #bb6600;">=<span style="color: #008800;">"350"<span style="color: #008888;">&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;/canvas&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;script&gt;</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;canvas&nbsp;<span style="color: #bb6600;">=&nbsp;document<span style="color: #bb6600;">.querySelector<span style="color: #bb6600;">(<span style="color: #008800;">"#myCanvas"<span style="color: #bb6600;">);</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;ctx&nbsp;<span style="color: #bb6600;">=&nbsp;canvas<span style="color: #bb6600;">.getContext<span style="color: #bb6600;">(<span style="color: #008800;">"2d"<span style="color: #bb6600;">);</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;width&nbsp;<span style="color: #bb6600;">=&nbsp;canvas<span style="color: #bb6600;">.width<span style="color: #bb6600;">,&nbsp;height&nbsp;<span style="color: #bb6600;">=&nbsp;canvas<span style="color: #bb6600;">.height<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;lastX&nbsp;<span style="color: #bb6600;">=&nbsp;width&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">();</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;lastY&nbsp;<span style="color: #bb6600;">=&nbsp;height&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">();</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;hue&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">0<span style="color: #bb6600;">;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;<strong style="color: red;"><span style="color: #880000;">// Michel Buffa: set the target frame rate. TRY TO CHANGE THIS VALUE AND SEE</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;<span style="color: #880000;">// THE RESULT. Try 2 frames/s, 10 frames/s, 60 frames/s Normally there</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;<span style="color: #880000;">// should be a limit&nbsp;of 60 frames/s in the browser's implementations.</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp;setFrameRateInFramesPerSecond<span style="color: #bb6600;">(<span style="color: #006666;">60<span style="color: #bb6600;">);</strong></li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// for time based animation. DelayInMS corresponds to the target framerate</li>
<li>&nbsp;&nbsp;<span style="color: #008888;">var&nbsp;now<span style="color: #bb6600;">,&nbsp;delta<span style="color: #bb6600;">,&nbsp;delayInMS<span style="color: #bb6600;">,<strong style="color: red;">&nbsp;totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">0<span style="color: #bb6600;">;</strong></li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// High resolution timer</li>
<li>&nbsp;&nbsp;<span style="color: #008888;">var&nbsp;then&nbsp;<span style="color: #bb6600;">=&nbsp;performance<span style="color: #bb6600;">.now<span style="color: #bb6600;">();</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// start the animation</li>
<li>&nbsp; requestAnimationFrame<span style="color: #bb6600;">(mainloop<span style="color: #bb6600;">);</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;<strong style="color: red;"><span style="color: #008888;">function&nbsp;setFrameRateInFramesPerSecond<span style="color: #bb6600;">(frameRate<span style="color: #bb6600;">)&nbsp;<span style="color: #bb6600;">{</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; delayInMs&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">1000&nbsp;<span style="color: #bb6600;">/&nbsp;frameRate<span style="color: #bb6600;">;</strong></li>
<li><strong style="color: red;">&nbsp;&nbsp;<span style="color: #bb6600;">}</strong></li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// each function that is going to be run as an animation should end by</li>
<li>&nbsp;&nbsp;<span style="color: #880000;">// asking again for a new frame of animation</li>
<li>&nbsp;&nbsp;<span style="color: #008888;">function&nbsp;<g id="68" data-gr-id="68">mainloop</g><span style="color: #bb6600;">(time)&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Here we will only redraw something if the time we want between frames has</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// elapsed</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Measure time with high resolution timer</li>
<li>&nbsp; &nbsp; now&nbsp;<span style="color: #bb6600;">=&nbsp;time<span style="color: #bb6600;">;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// How long between the current frame and the previous one?</li>
<li>&nbsp; &nbsp; delta&nbsp;<span style="color: #bb6600;">=&nbsp;now&nbsp;<span style="color: #bb6600;">-&nbsp;then<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// TRY TO UNCOMMENT THIS LINE AND LOOK AT THE CONSOLE</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// console.log("delay = " + delayInMs + " delta = " + delta + " total time = " +</li>
<li><span style="color: #880000;">&nbsp; &nbsp; // totalTimeSinceLastRedraw);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// If the total time since the last redraw is &gt; delay corresponding to the wanted</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// framerate, then redraw, else add the delta time between the last call to line()</li>
<li><span style="color: #880000;">&nbsp; &nbsp; // by requestAnimFrame&nbsp;to the total time..</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">if&nbsp;<span style="color: #bb6600;">(totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">&gt;&nbsp;delayInMs<span style="color: #bb6600;">)&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// if the time between the last frame and now is &gt; delay then we</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// clear the canvas and redraw</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.save<span style="color: #bb6600;">();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Trick to make a blur effect: instead of clearing the canvas</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// we draw a rectangle with a transparent color. Changing the 0.1</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// for a smaller value will increase the blur...</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.fillStyle&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #008800;">"rgba(0,0,0,0.1)"<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.fillRect<span style="color: #bb6600;">(<span style="color: #006666;">0<span style="color: #bb6600;">,&nbsp;<span style="color: #006666;">0<span style="color: #bb6600;">,&nbsp;width<span style="color: #bb6600;">,&nbsp;height<span style="color: #bb6600;">);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.translate<span style="color: #bb6600;">(width&nbsp;<span style="color: #bb6600;">/&nbsp;<span style="color: #006666;">2<span style="color: #bb6600;">,&nbsp;height&nbsp;<span style="color: #bb6600;">/&nbsp;<span style="color: #006666;">2<span style="color: #bb6600;">);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.scale<span style="color: #bb6600;">(<span style="color: #006666;">0.9<span style="color: #bb6600;">,&nbsp;<span style="color: #006666;">0.9<span style="color: #bb6600;">);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.translate<span style="color: #bb6600;">(-width&nbsp;<span style="color: #bb6600;">/&nbsp;<span style="color: #006666;">2<span style="color: #bb6600;">,&nbsp;<span style="color: #bb6600;">-height&nbsp;<span style="color: #bb6600;">/&nbsp;<span style="color: #006666;">2<span style="color: #bb6600;">);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.beginPath<span style="color: #bb6600;">();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.lineWidth&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">5&nbsp;<span style="color: #bb6600;">+&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">()&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #006666;">10<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.moveTo<span style="color: #bb6600;">(lastX<span style="color: #bb6600;">,&nbsp;lastY<span style="color: #bb6600;">);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;lastX&nbsp;<span style="color: #bb6600;">=&nbsp;width&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;lastY&nbsp;<span style="color: #bb6600;">=&nbsp;height&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.bezierCurveTo<span style="color: #bb6600;">(width&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">(),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;height&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">(),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;width&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">(),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;height&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">(),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;lastX<span style="color: #bb6600;">,&nbsp;lastY<span style="color: #bb6600;">);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;hue&nbsp;<span style="color: #bb6600;">=&nbsp;hue&nbsp;<span style="color: #bb6600;">+&nbsp;<span style="color: #006666;">10&nbsp;<span style="color: #bb6600;">*&nbsp;<span style="color: #aa0066;">Math<span style="color: #bb6600;">.random<span style="color: #bb6600;">();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.strokeStyle&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #008800;">"hsl("&nbsp;<span style="color: #bb6600;">+&nbsp;hue&nbsp;<span style="color: #bb6600;">+&nbsp;<span style="color: #008800;">", 50%, 50%)"<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.shadowColor&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #008800;">"white"<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.shadowBlur&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">10<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.stroke<span style="color: #bb6600;">();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.restore<span style="color: #bb6600;">();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;"><span style="color: #880000;">// reset the total time since last redraw</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp;totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">0<span style="color: #bb6600;">;</strong></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">}&nbsp;<span style="color: #008888;">else&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;"><span style="color: #880000;">// sum the total time since last redraw</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp;totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">+=&nbsp;delta<span style="color: #bb6600;">;</strong></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// Store time</li>
<li>&nbsp; &nbsp; then&nbsp;<span style="color: #bb6600;">=&nbsp;now<span style="color: #bb6600;">;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #880000;">// request new frame</li>
<li>&nbsp; &nbsp; requestAnimationFrame<span style="color: #bb6600;">(mainloop<span style="color: #bb6600;">);</li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">}</li>
<li>&nbsp;<span style="color: #008888;">&lt;/script&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;/body&gt;</li>
<li><span style="color: #008888;">&lt;/html&gt;</li>
</ol></div><br>


#### Same technique with the bouncing rectangle

See how we can set both the speed (in pixels/s) and the frame-rate using a high-resolution time with this [modified version on JSBin](https://jsbin.com/momeci/edit) of the example with the rectangle that also uses this technique.

[Local Demo](src/02d-example07.html)


Source code:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #aa0066;">&lt;!DOCTYPE html&gt;</li>
<li><span style="color: #008888;">&lt;html&nbsp;<span style="color: #aa0066;">lang<span style="color: #bb6600;">=<span style="color: #008800;">"en"<span style="color: #008888;">&gt;</li>
<li><span style="color: #008888;">&lt;head&gt;</li>
<li><span style="color: #008888;">&lt;meta&nbsp;<span style="color: #aa0066;">charset<span style="color: #bb6600;">=<span style="color: #008800;">utf-8&nbsp;<span style="color: #008888;">/&gt;</li>
<li><span style="color: #008888;">&lt;title&gt;Bouncing rectangle with high resolution timer and adjustable frame rate<span style="color: #008888;">&lt;/title&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;script&gt;</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;canvas<span style="color: #bb6600;">,&nbsp;ctx<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;width<span style="color: #bb6600;">,&nbsp;height<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;x<span style="color: #bb6600;">,&nbsp;y<span style="color: #bb6600;">,&nbsp;incX<span style="color: #bb6600;">;&nbsp;<span style="color: #880000;">// incX is the distance from the previously drawn rectangle</li>
<li><span style="color: #880000;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// to the new one</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;speedX<span style="color: #bb6600;">;&nbsp;<span style="color: #880000;">// speedX is the target speed of the rectangle in pixels/s</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// for time based animation, DelayInMS corresponds to the target frame rate</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;now<span style="color: #bb6600;">,&nbsp;delta<span style="color: #bb6600;">,&nbsp;delayInMS<span style="color: #bb6600;">,&nbsp;totalTimeSinceLastRedraw<span style="color: #bb6600;">=<span style="color: #006666;">0<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// High resolution timer</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var&nbsp;then&nbsp;<span style="color: #bb6600;">=&nbsp;performance<span style="color: #bb6600;">.now<span style="color: #bb6600;">();</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// Michel Buffa: set the target frame rate. TRY TO CHANGE THIS VALUE AND SEE</li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// THE RESULT. Try 2 frames/s, 10 frames/s, 60, 100 frames/s Normally there</li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// should be a limit&nbsp;of 60 frames/s in the browser's implementations, but you can&nbsp;</li>
<li><span style="color: #880000;">&nbsp; &nbsp;// try higher values</li>
<li>&nbsp; &nbsp;setFrameRateInFramesPerSecond<span style="color: #bb6600;">(<span style="color: #006666;">25<span style="color: #bb6600;">);</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">function&nbsp;setFrameRateInFramesPerSecond<span style="color: #bb6600;">(framerate<span style="color: #bb6600;">)&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp;delayInMs&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">1000&nbsp;<span style="color: #bb6600;">/&nbsp;framerate<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">}</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// Called after the DOM is ready (page loaded)</li>
<li>&nbsp; &nbsp;<span style="color: #008888;">function&nbsp;init<span style="color: #bb6600;">()&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// init the different variables</li>
<li>&nbsp; &nbsp; &nbsp;canvas&nbsp;<span style="color: #bb6600;">=&nbsp;document<span style="color: #bb6600;">.querySelector<span style="color: #bb6600;">(<span style="color: #008800;">"#mycanvas"<span style="color: #bb6600;">);</li>
<li>&nbsp; &nbsp; &nbsp;ctx&nbsp;<span style="color: #bb6600;">=&nbsp;canvas<span style="color: #bb6600;">.getContext<span style="color: #bb6600;">(<span style="color: #008800;">'2d'<span style="color: #bb6600;">);</li>
<li>&nbsp; &nbsp; &nbsp;width&nbsp;<span style="color: #bb6600;">=&nbsp;canvas<span style="color: #bb6600;">.width<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp;height&nbsp;<span style="color: #bb6600;">=&nbsp;canvas<span style="color: #bb6600;">.height<span style="color: #bb6600;">;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;x<span style="color: #bb6600;">=<span style="color: #006666;">10<span style="color: #bb6600;">;&nbsp;y&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">10<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Target speed in pixels/second, try with high values, 1000, 2000...</li>
<li>&nbsp; &nbsp; &nbsp;speedX&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #006666;">2000<span style="color: #bb6600;">;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Start animation</li>
<li>&nbsp; &nbsp; &nbsp;requestAnimationFrame<span style="color: #bb6600;">(animationLoop<span style="color: #bb6600;">)</li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">}</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">function&nbsp;animationLoop<span style="color: #bb6600;">(time)&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Measure time with high resolution timer</li>
<li>&nbsp; &nbsp; &nbsp;now&nbsp;<span style="color: #bb6600;">=&nbsp;time<span style="color: #bb6600;">;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// How long between the current frame and the previous one?</li>
<li>&nbsp; &nbsp; &nbsp;delta&nbsp;<span style="color: #bb6600;">=&nbsp;now&nbsp;<span style="color: #bb6600;">-&nbsp;then<span style="color: #bb6600;">;</li>
<li></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp;<span style="color: #008888;">if<span style="color: #bb6600;">(totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">&gt;&nbsp;delayInMs<span style="color: #bb6600;">)&nbsp;<span style="color: #bb6600;">{</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// Compute the displacement in x (in pixels) in function of the time elapsed</li>
<li><span style="color: #880000;">&nbsp; &nbsp; &nbsp; &nbsp;// since the last draw and</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// in function of the wanted speed. This time, instead of delta we</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// use totalTimeSinceLastRedraw as we're not always drawing at</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// each execution of mainloop</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;incX&nbsp;<span style="color: #bb6600;">=&nbsp;calcDistanceToMove<span style="color: #bb6600;">(<strong style="color: red;">totalTimeSinceLastRedraw</strong><span style="color: #bb6600;">,&nbsp;speedX<span style="color: #bb6600;">);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// an animation involves: 1) clear canvas and 2) draw shapes,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// 3) move shapes, 4) recall the loop with requestAnimationFrame</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// clear canvas</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.clearRect<span style="color: #bb6600;">(<span style="color: #006666;">0<span style="color: #bb6600;">,&nbsp;<span style="color: #006666;">0<span style="color: #bb6600;">,&nbsp;width<span style="color: #bb6600;">,&nbsp;height<span style="color: #bb6600;">);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx<span style="color: #bb6600;">.strokeRect<span style="color: #bb6600;">(x<span style="color: #bb6600;">,&nbsp;y<span style="color: #bb6600;">,&nbsp;<span style="color: #006666;">10<span style="color: #bb6600;">,&nbsp;<span style="color: #006666;">10<span style="color: #bb6600;">);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #880000;">// move rectangle</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;x&nbsp;<span style="color: #bb6600;">+=&nbsp;incX<span style="color: #bb6600;">;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// check collision on left or right</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">if<span style="color: #bb6600;">((x<span style="color: #bb6600;">+<span style="color: #006666;">10&nbsp;<span style="color: #bb6600;">&gt;=&nbsp;width<span style="color: #bb6600;">)&nbsp;<span style="color: #bb6600;">||&nbsp;<span style="color: #bb6600;">(x&nbsp;<span style="color: #bb6600;">&lt;=&nbsp;<span style="color: #006666;">0<span style="color: #bb6600;">))&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// cancel move + inverse speed</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; x&nbsp;<span style="color: #bb6600;">-=&nbsp;incX<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; speedX&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #bb6600;">-speedX<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">}</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">&nbsp;</strong><strong style="color: red;"><span style="color: #880000;">// reset the total time since last redraw</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">=&nbsp;delta<span style="color: #bb6600;">;</strong></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">}&nbsp;<span style="color: #008888;">else&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #880000;">// sum the total time since last redraw</li>
<li>&nbsp; &nbsp; &nbsp;totalTimeSinceLastRedraw&nbsp;<span style="color: #bb6600;">+=&nbsp;delta<span style="color: #bb6600;">;</li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">}</li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// Store time</li>
<li>&nbsp; &nbsp;then&nbsp;<span style="color: #bb6600;">=&nbsp;now<span style="color: #bb6600;">;</li>
<li>&nbsp;</li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// animate.&nbsp;</li>
<li>&nbsp; &nbsp;requestAnimationFrame<span style="color: #bb6600;">(animationLoop<span style="color: #bb6600;">);</li>
<li>&nbsp;<span style="color: #bb6600;">}</li>
<li></li>
<li>&nbsp;<span style="color: #008888;">var&nbsp;calcDistanceToMove&nbsp;<span style="color: #bb6600;">=&nbsp;<span style="color: #008888;">function<span style="color: #bb6600;">(delta<span style="color: #bb6600;">,&nbsp;speed<span style="color: #bb6600;">)&nbsp;<span style="color: #bb6600;">{</li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">return&nbsp;<span style="color: #bb6600;">(speed&nbsp;<span style="color: #bb6600;">*&nbsp;delta<span style="color: #bb6600;">)&nbsp;<span style="color: #bb6600;">/&nbsp;<span style="color: #006666;">1000<span style="color: #bb6600;">;</li>
<li>&nbsp;<span style="color: #bb6600;">}</li>
<li></li>
<li>&nbsp;<span style="color: #008888;">&lt;/script&gt;</li>
<li><span style="color: #008888;">&lt;/head&gt;</li>
<li></li>
<li><span style="color: #008888;">&lt;body&nbsp;<span style="color: #aa0066;">onload<span style="color: #bb6600;">=<span style="color: #008800;">"init<span style="color: #bb6600;">();<span style="color: #008800;">"<span style="color: #008888;">&gt;</li>
<li>&nbsp;<span style="color: #008888;">&lt;canvas&nbsp;<span style="color: #aa0066;">id<span style="color: #bb6600;">=<span style="color: #008800;">"mycanvas"&nbsp;<span style="color: #aa0066;">width<span style="color: #bb6600;">=<span style="color: #008800;">"200"&nbsp;<span style="color: #aa0066;">height<span style="color: #bb6600;">=<span style="color: #008800;">"50"&nbsp;<span style="color: #aa0066;">style<span style="color: #bb6600;">=<span style="color: #008800;">"border<span style="color: #bb6600;">:&nbsp;<span style="color: #006666;">2px&nbsp;solid black<span style="color: #008800;">"<span style="color: #008888;">&gt;&lt;/canvas&gt;</li>
<li><span style="color: #008888;">&lt;/body&gt;</li>
<li><span style="color: #008888;">&lt;/html&gt;</li>
</ol></div><br>


#### Can we use setInterval?

It's quite possible to use `setInterval(function, interval)` if you do not need an accurate scheduling.

To animate a monster at 60 fps but blinking his eyes once per second, you would use a mainloop with `requestAnimationFrame` and target a 60 fps animation, but you would also have a call to `setInterval(changeEyeColor, 1000);` and the changeEyeColor function will update a global variable, `eyeColor`, every second, which will be taken into account within the `drawMonster` function, called 60 times/s from the mainloop.


#### Notes for 2.4.3 Setting the frame rate

+ Frame rate
  + ignore some frames to reach desired frame rate w/ `requestAnimationFrame`
  + possible to set the frame rate using time-based animation
    + set a global variable corresponding to the desired frame rate
    + compare the elapsed time btw two executions of the animation loop
      + time elapsed too short for the target frame rate: do nothing
      + time elapsed exceeding the delay corresponding to the choosen frame rate: draw the frame and reset the time to zero
  + change frame rate: `setFrameRateInFramesPerSecond(nb);`

+ Example: change frame rate
  + access canvas element: `var canvas = document.querySelector("#myCanvas"); var ctx = canvas.getContext("2d");`
  + declare variable: `var width = canvas.width, height = canvas.width; var lastX = width * Math.random(); var lastY = height * Math.random(); var hue =0;`
  + call to set frame rate: `setFrameRateInFramesPerSecond(60);`
  + declare time-related variables: `var now, delta, delayInMS, totalTimeSinceLastDraw = 0; var then = performance.now();`
  + call to start animation: `requestAnimationFrame(mainloop);`
  + set frame rate<a name="frameRate"></a>: `function setFrameRateInFramesPerSecond(frameRate) { delayInMS = 1000/frameRate; }`
  + generate animation loop: `function mainloop(time) {...}`
    + set time-related variables: `now = time; delta = now - then;`
    + check time to redraw: `if (totalTimeSinceLastRedraw > delayInMS) {...}`
      + save context: `ctx.save();`
      + draw blurred rectangle: `ctx.fillStyle = "rgba(0, 0, 0, 0.1); ctx.fillRect(0, 0, width, height);`
      + translate ctx: `ctx.translate(width/2, height/2); ctx.scale(0.9, 0.9); ctx.translate(-width/2, -height/2);`
      + begin a new draw: `ctx.beginPath();`
      + set style and position for new curve: `ctx.lineWidth = 5 + Math.random() * 10; ctx.moveTo(lastX, lastY);`
      + set end position for curve: `lastX = width * Math.random(); lastY = height * Math.random();`
      + set curve path: `ctx.bizierCurveTo(width*Math.random(), height*Math.random(), width*Math.random(), height*Math.random(), lastX, lastY);`
      + set curve style and draw: `hue = hue + 10 * Math.random(); ctx.strokeStyle = "hsl(" + hue + ", 50%, 50%)"; ctx.shadowColor = "white"; ctx.shadowBlur = 10; ctx.stroke();`
      + restore ctx: `ctx.restore();`
      + reset last redraw time: `totalTimeLastSinceRedraw = 0;`
    + increase time if redraw not reached: `else { totalTimeSinceLastRedraw += delta; }`
    + call for next frame: `requestAnimationFrame(mainloop);`

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
      + perform animation: `ctx.clearRect(0, 0, width, height); ctx.strokeRect(x, y, 10, 10); x += incX; if ((x+10 >= witdth) || (x <= 0)) {x -= incX; speedX = -speedX;}`
      + reset redraw time: `totalTimeSinceLastRedraw = 0;`
    + increase time w/p redraw: `else {totalTimeSinceLastRedraw += delta;}`
    + store time: `then = now;`
    + call for next frame: `requestAnimationFrame(mainloop);`
  + calculate [distance to move](#calcDist)


### 2.4.4 Adding time-based animation

To add time-based animation to our game engine, we will be using the technique discussed in the previous lesson. This technique is now widely supported by browsers, and adds time-based animation to our game framework, through the timestamp parameter passed to the callback function (`mainLoop`) by the call to `requestAnimationFrame(mainLoop)`.

Here is an [online example of the game framework](https://jsbin.com/xacebu/edit) at JSBin: this time, the monster has a speed in pixels/s and we use time-based animation. Try it and verify the smoothness of the animation; the FPS counter on a Mac Book Pro core i7 shows 60 fps.

[Local Demo](src/02d-example08.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3wLsW2P')"
    src    = "https://bit.ly/2SO5ymI"
    alt    = "screenshot of the monster moving at 60 f/s"
    title  = "screenshot of the monster moving at 60 f/s"
  />
</figure>

Now try this [slightly modified version](https://jsbin.com/gazatuquya/edit?html,js,output) in which we added a delay inside the animation loop. This should slow down the frame rate.  On a Mac Book Pro + core i7, the frame-rate drops down to 37 fps. However, if you move the monster using the arrow keys, its speed on the screen is the same, excepting that it's not as smooth as in the previous version, which ran at 60 fps.

[Local Demo](src/02d-example09.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3wLsW2P')"
    src    = "https://bit.ly/2TRhBQt"
    alt    = "screenshot of example that runs at 37 f/s"
    title  = "screenshot of example that runs at 37 f/s"
  />
</figure>


Here are the parts we changed:

+ Declaration of the monster object - now the speed is in pixels/s instead of in pixels per frame

  <div><ol style="list-style-type: decimal;">
  <li value="1"> // The monster !</li>
  <li> var monster = {</li>
  <li>&nbsp; &nbsp;x:10,</li>
  <li>&nbsp; &nbsp;y:10,</li>
  <li>&nbsp; &nbsp;<strong style="color: red;">speed</strong><strong style="color: red;">:100, // pixels/s this time !</strong></li>
  <li> };</li>
  </ol></div><br>

+ We added a `timer(currentTime)` function that returns the `delta` of the time elapsed since its last call

  We refer to it from the game loop, to measure the time between frames. Notice that here we pass the delta as a parameter to the `updateMonsterPosition` call:

  <div><ol style="list-style-type: decimal;">
  <li value="1"><strong style="color: red;">function timer(currentTime) {</strong></li>
  <li><strong style="color: red;">&nbsp; &nbsp;var delta = currentTime - oldTime;</strong></li>
  <li><strong style="color: red;">&nbsp; &nbsp;oldTime = currentTime;</strong></li>
  <li><strong style="color: red;">&nbsp; &nbsp;return delta;</strong></li>
  <li><strong style="color: red;">}</strong></li>
  <li></li>
  <li>var mainLoop = function(<strong style="color: red;">time</strong>){</li>
  <li>&nbsp; &nbsp;//main function, called each frame </li>
  <li>&nbsp; &nbsp;<strong style="color: red;">measureFPS</strong><strong style="color: red;">(time);</strong></li>
  <li> </li>
  <li>&nbsp; &nbsp;<strong style="color: red;">// number of ms since last frame draw</strong></li>
  <li><strong style="color: red;">&nbsp; &nbsp;delta = timer(time);</strong></li>
  <li> </li>
  <li>&nbsp; &nbsp;// Clear the canvas</li>
  <li>&nbsp; &nbsp;clearCanvas();</li>
  <li> </li>
  <li>&nbsp; &nbsp;// draw the monster</li>
  <li>&nbsp; &nbsp;drawMyMonster(monster.x, monster.y);</li>
  <li> </li>
  <li>&nbsp; &nbsp;<strong style="color: red;">// Check inputs and move the monster</strong></li>
  <li><strong style="color: red;">&nbsp; &nbsp;updateMonsterPosition(delta);</strong></li>
  <li> </li>
  <li>&nbsp; &nbsp;// call the animation loop every 1/60th of second</li>
  <li>&nbsp; &nbsp;requestAnimationFrame(mainLoop);</li>
  <li> };</li>
  </ol></div><br>

+ Finally, we use the time-delta in the `updateMonsterPosition(...)` function

  <div><ol style="list-style-type: decimal;">
  <li value="1"> function updateMonsterPosition(<strong style="color: red;">delta</strong>) {</li>
  <li>&nbsp; &nbsp;...</li>
  <li>&nbsp; &nbsp;// Compute the incX and inY in pixels depending</li>
  <li>&nbsp; &nbsp;// on the time elapsed since last redraw</li>
  <li>&nbsp; &nbsp;<strong style="color: red;">monster</strong><strong style="color: red;">.x += calcDistanceToMove(delta, monster.speedX);</strong></li>
  <li>&nbsp; <strong style="color: red;">&nbsp;monster</strong><strong style="color: red;">.y += calcDistanceToMove(delta, monster.speedY);</strong></li>
  <li>&nbsp;}</li>
  </ol></div>


#### Notes for 2.4.4 Adding time-based animation

+ Example: game framework adding time-based animation
  + declare monster object: `var monster = { x: 10, y: 10, speed: 10 };`
  + measure the time btw feames: `function timer(currentTime) {var delta = currentTime - oldTime; oldTime = currentTime; return delta;}`
  + generate animation loop: `var mainLoop = function(time) {...}`
    + measure FPS: `measureFPS(time);`
    + calculate time different: `delta = timers(time);`
    + call to empty canvas: `clearCanvas();`
    + call to draw the monster: `drawMyMonster(monster.x, monster.y);`
    + call to move the monster: `updateMonsterPosition(delta);`
    + call for next frame: `requestAnimationFrame(mainLoop);`
  + compute the increments on each axis: `function updateMonsterPosition(delta) {...}`
    + x-axis in pixel: `monster.x += calcDistanceToMove(delta, monster.speedX);`
    + y-axis in pixel: `monster.y += calcDistanceToMove(delta, monster.speedY);`


### 2.4.5 Discussion and projects

Please either post your comments/observations/questions or share your creations.

#### Suggested topics of discussion:

+ Did you know that time based animation is used by all "real" games?
+ Many game frameworks available on the web include time based animation. While the course explains the low level operations used in many of these frameworks, it's interesting to know they exist and test some demos. We recommend you look at [phaser.io](https://phaser.io/).
+ How would you design a scheduler for your game, to trigger events at some predefined times (start an enemy wave, use a timed level in the game, etc.)

#### Optional projects:

+ If you have started developing your own small game from the examples given in the course (what, you haven't started yet??? ;) ), please add time-based animation to your project.
+ Add sliders to adjust the frame rate or the speed of the objects in the examples given in the course or in your own project, so as to illustrate the time-based animation concept.




