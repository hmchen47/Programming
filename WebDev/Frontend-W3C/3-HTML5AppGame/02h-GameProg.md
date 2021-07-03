# Module 2: Game programming with HTML5 section


## 2.8 Exercises - Module 2 (12 Questions)

### 2.8.1 User interaction (1-4)

1. Listen in the loop?

  What is the best way to deal with multiple events (multiple keys + mouse buttons, movements, etc.) at the same time?

  a. Use a global object to store the state of the input keys, check it in the mainloop, update the x and y position of the player accordingly<br>
  b. Update the x and y position of the player directly in the input event listeners<br>

  Ans: a<br>
  Explanation: In the mainloop, the best practice is to check the states of the different input devices. This is done very quickly and produces smooth movements: the left key is down. Then do x = x-1, and this is done sixty times per second -> smooth movement. On the other hand, changing x and y in the listeners is a bad idea: keep a key pressed and you will enter in the listener maybe 10 times per second, producing a sluggish animation.


2. Gamepad updated or not....

  In order to get the gamepad(s) status (buttons, joysticks) up to date, is it best practice to call navigator.getGamepads() regularly (in the game loop, for example)?

  a. Yes.<br>
  b. No, it's not necessary: once you get a reference to a gamepad (for example, in the gamepadconnected event listener), its state reflects its current status. It's updated automatically by the browser.<br>

  Ans: a<br>
  Explanation:
    + In the course's examples, we check for connected gamepads every 1/60th second, and we update the gamepad global variable with the first gamepad object returned by the browser. We need to do this as what we get is a "snapshot" of the gamepad state, with fixed values for the buttons, axes, etc. If we want to check the current button and joystick statuses, we need to poll the browser at a high frequency and ask for an updated snapshot.
    + From the specification: "getGamepads retrieves a snapshot of the data for the the currently connected and interacted-with gamepads."


3. Axes values?

  The values of the gamepad axes are...?

  a. Between -5 and +5<br>
  b. Between -1 and +1<br>
  c. Between 1 and 0<br>

  Ans: b<br>
  Explanation: These values, between -1 and +1, correspond to the cosinus or the sinus of the angle made by the joystick.


4. Trigger me!

  How do you test if a gamepad button is analog (eg an R2 or L2 trigger on a XBox 360 or PS2/PS3 gamepad)?

  a. We test if the button's property `pressed` is true, then if its `value` property is defined. This property gives the pressure on the trigger.<br>
  b. Analog buttons are considered as axes.<br>

  Ans: a<br>
  Explanation: Let `b` be a gamepad button. If `b.pressed` is true, then `b` is pressed. If `b.value` is defined, then `b` is an analog trigger and `b.value` is a floating point value between 0 and 1.


### 2.8.2 Time-based animation (5-8)

5. What time is it?

  A graphic object moves across the screen. With time-based animation, how quickly does it move?

  a. It will remain constant<br>
  b. It will depend on the device running the script<br>

  Ans: a<br>
  Explanation: With time-based animation, we compute the time that has elapsed between the previous frame drawn and the current one, and depending on this delta of time, we adjust the distance we move objects on the screen so that their speed in pixels per second remains constant.


6. Setting the frame rate

  We have a mainloop that targets 60 frames/second and we use the `requestAnimationFrame` API for implementing it. How can we set the frame rate to nearly 37 frames/s, for example?

  a. We can measure the deltas of time between frames, and sum them up. If the sum is superior to the delay that corresponds to 1/37s, then we draw the frame, otherwise we do nothing.<br>
  b. We should stop using `requestAnimationFrame` and use `setInterval` instead - it's better.<br>
  c. We can't.<br>

  Ans: a<br>
  Explanation: The mainloop, for all the reasons explained during the HTML5 Part 1 course, should use the `requestAnimation` API. In order not to draw at 60 frames/s but less, we should measure the time elapsed and sum the deltas of time. When the sum is superior to the delay that corresponds to 1/37s (for 37 frames/s), then we draw the frame.


7. I prefer HD!

  Which of these gives a high resolution time (with a sub millisecond accuracy)? (2 correct answers.)

  a. `var time = new Date().getTime();`<br>
  b. `var time = performance.now();`<br>
  c. `var time = Date.now();`<br>
  d. Use the parameter passed to the `mainloop` when called by `requestAnimationFrame(mainloop)`<br>

  Ans: bd<br>
  Explanation: The `performance.now()` and the `requestAnimationFrame` APIs provide high resolution time.


8. Sprites and time based animation?

  The sprite animation framework proposed in the course...

  a. used time-based animation in the draw method of the sprite object model<br>
  b. did not use time-based animation as it did not address the moving object problem<br>

  Ans: <font style="color: magenta;">a</font>, xb<br>
  Explanation: It used time-based animation in the draw function of the sprite model to set the number of times we will draw a new image of animation, per second.


### 2.8.3 Sprite-based animation (9-11)

9. Do you want a Sprite?

  What is a sprite animated character?

  a. A graphic character that will be animated by drawing different images rapidly<br>
  b. A graphic character drawn using an animated gif image, for example<br>

  Ans: a<br>
  Explanation: A sprite animated character is made of different sub-images that we draw consecutively.

<hr>

__Source code for the next questions (10 and 11)__

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong style="color: red;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;robot</span><span class="pun" style="color: #bb6600;">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">onload&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #bb6600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">getElementById</span><span class="pun" style="color: #bb6600;">(</span><span class="str" style="color: #008800;">"canvas"</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">getContext</span><span class="pun" style="color: #bb6600;">(</span><span class="str" style="color: #008800;">"2d"</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Load the spritesheet</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; spritesheet&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Image</span><span class="pun" style="color: #bb6600;">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; spritesheet</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">src&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;SPRITESHEET_URL</span><span class="pun" style="color: #bb6600;">;</span><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Called when the spritesheet has been loaded</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; spritesheet</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">onload&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #bb6600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #bb6600;">&nbsp; &nbsp; ...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;<strong style="color: red;">robot&nbsp;</strong></span><strong style="color: red;"><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Sprite</span><span class="pun" style="color: #bb6600;">();</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pun" style="color: #bb6600;">&nbsp; &nbsp; // 1 is the posture number in the stylesheet. We have</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pun" style="color: #bb6600;">&nbsp; &nbsp; // only one with the robot.</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln" style="line-height: 1.6;">&nbsp; &nbsp; robot</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">extractSprites</span><span class="pun" style="line-height: 1.6;">(</span><span class="pln" style="line-height: 1.6;">spritesheet</span><span class="pun" style="line-height: 1.6;">,</span><span class="pln" style="line-height: 1.6;">&nbsp;NB_POSTURES</span><span class="pun" style="line-height: 1.6;">, 1</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;NB_FRAMES_PER_POSTURE</span><span class="pun" style="color: #bb6600;">,</span><span class="pln"></span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;SPRITE_WIDTH</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;SPRITE_HEIGHT</span><span class="pun" style="color: #bb6600;">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; &nbsp; robot</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">setNbImagesPerSecond</span><span class="pun" style="color: #bb6600;">(</span><span class="lit" style="color: #006666;">20</span><span class="pun" style="color: #bb6600;">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">mainloop</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">};</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// onload</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #bb6600;">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;mainloop</span><span class="pun" style="color: #bb6600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Clear the canvas</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">clearRect</span><span class="pun" style="color: #bb6600;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">width</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">height</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong style="color: red;"><span class="com" style="color: #880000;">// draw sprite at 0, 0 in the small canvas</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong style="color: red;"><span class="pln">&nbsp; robot</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">draw</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">ctx</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1</span><span class="pun" style="color: #bb6600;">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">mainloop</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #bb6600;">}</span></li>
</ol></div><br>

The Sprite constructor function:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Sprite</span><span class="pun" style="color: #bb6600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">spriteArray&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">[];</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">currentFrame&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">delayBetweenFrames&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">extractSprites&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">spritesheet</span><span class="pun" style="color: #bb6600;">,</span><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;nbPostures</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;postureToExtract, </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;nbFramesPerPosture</span><span class="pun" style="color: #bb6600;">,</span><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;spriteWidth</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;spriteHeight</span><span class="pun" style="color: #bb6600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// number of sprites per row in the spritesheet</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;nbSpritesPerRow&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">floor</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">spritesheet</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">width&nbsp;</span><span class="pun" style="color: #bb6600;">/</span><span class="pln">&nbsp;spriteWidth</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Extract each sprite</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp; var startIndex = (postureToExtract -1) *&nbsp;</span><span style="color: #000000; line-height: 25.6px;">nbFramesPerPosture;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span style="color: #000000; line-height: 25.6px;">&nbsp; &nbsp; var endIndex = startIndex +&nbsp;</span><span style="color: #000000; line-height: 25.6px;">nbFramesPerPosture;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">for</span><span class="pun" style="color: #bb6600;">(</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;index&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="pln"><span style="color: #006666;" color="#006666">startIndex</span></span><span class="pun" style="color: #bb6600;">;</span><span class="pln">&nbsp;index&nbsp;</span><span class="pun" style="color: #bb6600;">&lt;</span><span class="pln">&nbsp;maxIndex</span><span class="pun" style="color: #bb6600;">;</span><span class="pln">&nbsp;index</span><span class="pun" style="color: #bb6600;">++)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com" style="color: #880000;">// Computation of the x and y position that corresponds to the sprite</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// index</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// x is the rest of index/nbSpritesPerRow * width of a sprite</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;x&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">index&nbsp;</span><span class="pun" style="color: #bb6600;">%</span><span class="pln">&nbsp;nbSpritesPerRow</span><span class="pun" style="color: #bb6600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">*</span><span class="pln">&nbsp;spriteWidth</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// y is the divisor of index by nbSpritesPerRow * height of a sprite</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;y&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">Math</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">floor</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">index&nbsp;</span><span class="pun" style="color: #bb6600;">/</span><span class="pln">&nbsp;nbSpritesPerRow</span><span class="pun" style="color: #bb6600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">*</span><span class="pln">&nbsp;spriteHeight</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// build a spriteImage object</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;s&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">new</span><span class="pln">&nbsp;</span><span class="typ" style="color: #aa0066;">SpriteImage</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">spritesheet</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;spriteWidth</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;spriteHeight</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">spriteArray</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">push</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">s</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #bb6600;">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun" style="color: #bb6600;">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="kwd" style="color: #008888;">then</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;performance</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">now</span><span class="pun" style="color: #bb6600;">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">draw&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">ctx</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #bb6600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Use time based animation to draw only a few images per second</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;now&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;performance</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">now</span><span class="pun" style="color: #bb6600;">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;delta&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;now&nbsp;</span><span class="pun" style="color: #bb6600;">-</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="kwd" style="color: #008888;">then</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// Draw currentSpriteImage</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;currentSpriteImage&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">spriteArray</span><span class="pun" style="color: #bb6600;">[</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">currentFrame</span><span class="pun" style="color: #bb6600;">];</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// x, y, scale. 1 = size unchanged</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; currentSpriteImage</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">draw</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">ctx</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;x</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;y</span><span class="pun" style="color: #bb6600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1</span><span class="pun" style="color: #bb6600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// if the delay between images is elapsed, go to the next one</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">if</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">(</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #bb6600;">&gt;</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">delayBetweenFrames</span><span class="pun" style="color: #bb6600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com" style="color: #880000;">// Go to the next sprite image</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">currentFrame</span><span class="pun" style="color: #bb6600;">++;</span><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">currentFrame&nbsp;</span><span class="pun" style="color: #bb6600;">%=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">spriteArray</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">length</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com" style="color: #880000;">// reset the total time since last image has been drawn</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #bb6600;">}</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">else</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// sum the total time since last redraw</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">&nbsp;totalTimeSinceLastRedraw&nbsp;</span><span class="pun" style="color: #bb6600;">+=</span><span class="pln">&nbsp;delta</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #bb6600;">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="kwd" style="color: #008888;">then</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;now</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun" style="color: #bb6600;">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">setNbImagesPerSecond&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #bb6600;">(</span><span class="pln">nb</span><span class="pun" style="color: #bb6600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// delay in ms between images</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #008888;">this</span><span class="pun" style="color: #bb6600;">.</span><span class="pln">delayBetweenFrames&nbsp;</span><span class="pun" style="color: #bb6600;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">1000</span><span class="pln">&nbsp;</span><span class="pun" style="color: #bb6600;">/</span><span class="pln">&nbsp;nb</span><span class="pun" style="color: #bb6600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun" style="color: #bb6600;">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun" style="color: #bb6600;">}</span></li>
</ol></div><br>

10. Order is important...

  In the above code, we build the robot sprite inside the `spritesheet.onload` listener. Look at the code that extracts the sprites (_lines 6-29_): does it require the sprite sheet to be loaded in order to work? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, in the above code, the sprite sheet needs to be loaded otherwise its size (width and height) will be undefined or equal to zero. _Line 11_ in the code extractor above will extract `SpriteImages` with the wrong coordinates. It's a best practice when programming games, to load all assets (images, sounds) before doing anything (extracting sprites, start the animation, play the sounds).


11. Sprite animation too fast?

  In the draw function, why is the code dealing with time deltas?

  a. In order to set the number of frames of animation to draw per second<br>
  b. It's not important - I suppose it is going to be useful when we will move the character<br>
  
  Ans: a<br>
  Explanation: It's useful for setting the number of frames per second. We will draw a different image from the spriteArray that composes the animated character.










