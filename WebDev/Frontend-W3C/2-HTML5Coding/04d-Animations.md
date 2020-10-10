# Week 4: HTML5 Animations

## 4.4 Exercises - Week 4


### 4.4.1 Intro exercises - Week 4

Here is an opportunity to show that you can now animate content on the Web, and are ready to have fun drawing and animating a monster!

Please complete the following 12 exercises in a timely manner. As stated in the grading policy page, they count towards 15% of your final grade.


### 4.4.2 Old methods... (1-3)

1. Draw me!

  <pre>setInterval(draw, 2000);

  function draw() {
    // ...
  }
  </pre>

  The call to setInterval will...

  a. Call it after 2000 seconds<br/>
  b. Call the draw function repeatedly every 2 seconds<br/>
  c. Call it once after 2 seconds<br/>

  Ans: b<br/>
  Explanation: The second parameter is the interval of time between each call of the function draw. It's in milliseconds.


2. Am I late?

  <pre>setTimeout(draw, 2000);

  function draw() {
    // ...
    setTimeout(draw, 2000);
  }
  </pre>

  What will the above code do?

  a. This is not the correct way to use setTimeout for doing animation.<br/>
  b. The animation will start after 2 seconds. Call the draw function every two seconds once the animation has started.<br/>
  c. The animation will start immediately. Call the draw function every two seconds once the animation has started.<br/>

  Ans: <span style="color: magenta;">b</span>, xa<br/>
  Explanation: `setTimeout` calls the function passed as first parameter after a delay passed as second parameter, in milliseconds (ms). Draw is called the first time after 2seconds. Then, as setTimeout is called again at the end of draw, draw will be called every two seconds again and again.


3. Choose carefully!

  I want to perform an animation at 60 frames/s on modern browsers. What is my preferred choice?

  a. Using requestAnimationFrame<br/>
  b. Using setTimeout<br/>
  c. Using setInterval<br/>

  Ans: a<br/>
  Explanation: HTML5 introduced the `requestAnimationFrame` API for 60 frames/s animation as a target. This method comes with many advantages presented in the course: optimization, merging of multiple animations, better scheduling accuracy, etc.


### 4.4.3 Basic animation techniques (4-6)

__Source code for the three questions (4, 5 and 6):__

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
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;moveShapes</span><span class="pun">(...)</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// call again mainloop after XXX milliseconds</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="pln">requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">&nbsp;function</span><span class="pln"> startAnimation</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>id </strong></span><strong><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>


4. Just in time!

  In the above code, how often will the browser try to call the animationLoop function?

  a. There is another optional parameter that we could have used to change the interval of time: requestAnimationFrame(animationLoop, milliseconds).<br/>
  b. Every 1/60th of a second (16.6 ms).<br/>
  c. Every 1/30th of a second.<br/>

  Ans: <br/>
  Explanation: 


5. Can I see your ID?

  What is the id returned by the call to requestAnimationFrame at line 29 useful for?

  a. It is useful to stop an animation by calling cancelAnimationFrame(id).<br/>
  a. It is used to get the delta of time elapsed (using the id.delta property).<br/>
  a. It is used to set properties or to call methods of the requestAnimaTionFrame scheduler, like this: id.interval=25, or id.stop() in order to stop the animation.<br/>

  Ans: <br/>
  Explanation: 


6. How long did this animation take?

  What is the timeStamp parameter passed to the animationLoop at line 17?

  a. It gives a high resolution time (with sub-millisecond accuracy). By comparing two consecutive values of this parameter with two consecutive executions of the animation loops, we can compute the amount of time elapsed between frames. This is useful when writing Web games.<br/>
  b.No need to compute these deltas, this parameter IS the time elapsed between each frame of animation.<br/>

  Ans: <br/>
  Explanation: 

