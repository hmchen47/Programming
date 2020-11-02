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

  In the above code, how often will the browser try to call the `animationLoop` function?

  a. There is another optional parameter that we could have used to change the interval of time: `requestAnimationFrame(animationLoop, milliseconds)`.<br/>
  b. Every 1/60th of a second (16.6 ms).<br/>
  c. Every 1/30th of a second.<br/>

  Ans: b<br/>
  Explanation: The browser will try to run the `animationLoop` every 16.6 ms, that is 1/60th of a second. However, this time interval may vary slightly depending on: cpu or gpu power, device load, drawing complexity, etc. `requestAnimationFrame` is nevertheless much more optimized than setTimeOut or setInterval and should produce more accurate scheduling.


5. Can I see your ID?

  What is the id returned by the call to `requestAnimationFrame` at line 29 useful for?

  a. It is useful to stop an animation by calling `cancelAnimationFrame(id)`.<br/>
  b. It is used to get the delta of time elapsed (using the id.delta property).<br/>
  c. It is used to set properties or to call methods of the `requestAnimaTionFrame` scheduler, like this: id.interval=25, or id.stop() in order to stop the animation.<br/>

  Ans: a<br/>
  Explanation: The id is useful to cancel an animation. There could be several concurrent animations running at the same time, each having its own id. Notice that `requestAnimationFrame`, unlike `setInterval` or `setTimeout`, will make the browser merge the different animations into a single frame in the graphics card.


6. How long did this animation take?

  What is the `timeStamp` parameter passed to the `animationLoop` at line 17?

  a. It gives a high resolution time (with sub-millisecond accuracy). By comparing two consecutive values of this parameter with two consecutive executions of the animation loops, we can compute the amount of time elapsed between frames. This is useful when writing Web games.<br/>
  b. No need to compute these deltas, this parameter IS the time elapsed between each frame of animation.<br/>

  Ans: <span style="color: magenta;">a</span><br/>
  Explanation: The `timeStamp` parameter of the `animationLoop` function gives a high resolution time. By measuring deltas between two consecutive calls of the `animationLoop`, we will know exactly, with a sub-millisecond accuracy, what is the exact elapsed time between two frames.


### 4.4.4 Canvas and user interactions (7-12)

__Source code for the next question (7):__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Click listener version 1</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">saySomething</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Click me!</span><span class="tag">&lt;/button&gt;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">function</span><span class="pln"> saySomething</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Hello!"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

7. Too simple? 

  The above code shows a way to detect a click on a button (line 8). It works fine for simple examples, but in the course we criticized this method. What are its faults?

  a. Mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) is not the recommended way for full scale applications where a clean separation is best.<br/>
  b. It doesn't work with all events, only with 'click' events.<br/>

  Ans: a<br/>
  Explanation: Indeed, this is not the recommended way to handle events, even if it is very easy to use. Mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) in one place is ok for small examples (as seen in this course), but is not the recommended way for full scale applications where a clean separation is best. Notice that with this method we can pass an event to the callback function; see this example on JS Bin: http://jsbin.com/gixuku/edit.


__Source code for the next question (8):__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Click listener version 2</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myButton"</span><span class="tag">&gt;</span><span class="pln">Click me!</span><span class="tag">&lt;/button&gt;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> button </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myButton"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>// Add an onclick listener to the button &nbsp;&nbsp;</strong></span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; button</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> saySomething</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> saySomething</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Hello! Button with id: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">id </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; " has been clicked"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

8. Click on me please!

  What is the disadvantage of the method used in the above example for defining an event listener (line 14)?

  a. We cannot declare multiple click event listeners.<br/>
  b. The event parameter at line 16 above is always undefined. We cannot get the event with this method.<br/>

  Ans: a<br/>
  Explanation: This method is ok, but you will not be able to attach several click listener functions. For example, you may have three buttons, and you would like a click on any of them to call the same function. In that function you could get the event and test event.target.id to find out which button has been clicked.


__Source code for the next question (9):__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"400"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Your browser does not support the canvas tag.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;/canvas&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span style="color: #000088;" color="#000088">&nbsp;&nbsp;</span>&lt;script&gt;</li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> x</span><span class="pun">=</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">=</span><span class="lit">100</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> incrementX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> handleKeyup</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> handleKeydown</span><span class="pun">(event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">//left key </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;incrementX </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">39</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// right key</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;incrementX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> handleKeyup</span><span class="pun">(event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;incrementX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x </span><span class="pun">+=</span><span class="pln"> incrementX</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></strong><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp;function</span><span class="pln"> start</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Start the animation loop, targets 60 frames/s</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

9. Left or right?

  What does the above code do (note: it works! there are no errors in it)?

  a. It draws a small stationary rectangle, and if we use the left and right arrow keys, it moves horizontally to the left or to the right, respectively.<br/>
  b. It draws a small stationary rectangle and if we press the arrow keys, nothing happens.<br/>

  Ans: a<br/>
  Explanation: The above code will display a small rectangle at position x, y = (100, 100), but when an arrow key is pressed, the incrementX variable goes from 0 to -1 or +1 (lines 23 or 26), and then the x position is incremented/decremented in the loop that is executed 60 times/s. The instruction at line 37 will make it move to the left or to the right. Try it: http://jsbin.com/balenu/edit


__Source code for the next question (10):__

This is the `drawMonster` function from the course.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">,</span><span class="pln"> headColor</span><span class="pun">,</span><span class="pln"> eyeColor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// BEST PRACTICE: SAVE CONTEXT AND RESTORE IT AT THE END</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Moves the coordinate system so that the monster is drawn</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// at position (x, y)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// head</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">headColor</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// eyes</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">35</span><span class="pun">,</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">140</span><span class="pun">,</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// interior of eye</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">eyeColor</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">43</span><span class="pun">,</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">143</span><span class="pun">,</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Nose</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'black'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">90</span><span class="pun">,</span><span class="lit">70</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">80</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Mouth</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'purple'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">60</span><span class="pun">,</span><span class="lit">165</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// BEST PRACTICE!</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
</ol></div>

10. Move and rotate that monster!

  We would like to use the above function in our animation loop (code from previous exercice). Here is a new version of the animation loop:

  <pre>
  var angle=0;
  var x = 100;
  var y = 100;

  function animationLoop() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawMonster(x, y, angle, 'green', 'yellow');
        <span style="color:red;"><b>x= ? ;
        angle = ?? ;</b></span>
        requestId = requestAnimationFrame(animationLoop);
  }  
  </pre>

  What would you put instead of '?' and '??' in order to make the monster move continuously to the right (1 pixels per frame) and rotate (also continuously)?

  a. `x = x + 1; angle = 0.1;`<br/>
  b. `x = x + 1; angle = angle + 0.1;`<br/>
  c. `x = x - 1; angle = angle + 0.1;`<br/>
  d. `x = 1; angle = ctx.rotate(angle);`<br/>

  Ans: <span style="color: magenta;">b</span>, xa<br/>
  Explanation: The second answer is correct. By incrementing x and the angle 60 times per second in the animation loop, this will make the monster move and rotate continuously. In the first frame, the monster will be drawn at (100, 100), angle = 0. At the next frame, the monster will be drawn at (101, 100), angle = 0.1. At the next frame after that, at (102, 100), angle = 0.2, etc. The answer 3 is incorrect as x is decremented: this would make the monster go to the left. Answer 1 is incorrect as the angle is never incremented, and the last answer is false as ctx.rotate does not return anything.


11. Resize me at your own risk!

  <pre>...
  canvas.width = 100;
  ...
  </pre>

  Changing the width or height property of a canvas in JavaScript will ...

  a. Erase the canvas' content.<br/>
  a. Change the size of the canvas, preserving its content.<br/>
  
  Ans: a<br/>
  Explanation: If we set the width or height attribute of a canvas object in JavaScript, its content is erased.


12. I do not like percentages, Mr. Banker!

  <pre>&lt;style&gt;
      #myCanvas {
        border: 1px solid black;
        width:100%
      }
  &lt;/style&gt;
  ...
  &lt;canvas id="myCanvas" width="400" height="400"&gt;...&lt;/canvas&gt;
  </pre>

  What is wrong with the above code?

  a. width="400" and height="400" are incompatible with the CSS rule "width = 100%".<br/>
  b. Resizing a canvas using CSS in percentage (%) values is a bad practice.<br/>
  c. Nothing.<br/>

  Ans: b<br/>
  Explanation: 
    + Using percentages (%) in the CSS width and height properties of a canvas does not change its number of pixels/resolution. Instead it scales the existing pixels without erasing the content, giving a blurry effect when a canvas becomes larger. The course gives best practices to implement a responsive canvas.
    + You can always give a default size even if you have CSS rules that change the actual size dynamically.



