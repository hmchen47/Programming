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

<div><ol>
<li value="1"><span>&lt;body</span><span> </span><span>onload</span><span>=</span><span>"</span><span>init</span><span>();</span><span>"</span><span>&gt;</span><span> </span></li>
<li><span>&lt;script&gt;</span></li>
<li><span> </span><span>var</span><span> canvas</span><span>,</span><span> ctx</span><span>;</span></li>
<li><span> </span></li>
<li><span> </span><span>function</span><span> init</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp;</span><span>// This function is called after the page is loaded</span></li>
<li><span>&nbsp; &nbsp;</span><span>// 1 - Get the canvas</span></li>
<li><span>&nbsp; &nbsp;canvas </span><span>=</span><span> document</span><span>.</span><span>getElementById</span><span>(</span><span>'myCanvas'</span><span>);</span></li>
<li><span>&nbsp; &nbsp;</span><span>// 2 - Get the context</span></li>
<li><span>&nbsp; &nbsp;ctx</span><span>=</span><span>canvas</span><span>.</span><span>getContext</span><span>(</span><span>'2d'</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;</span><span>// 3 - start the animation</span></li>
<li><span>&nbsp; &nbsp;startAnimation</span><span>();</span></li>
<li><span> </span><span>}</span></li>
<li><span>&nbsp;</span></li>
<li><span>&nbsp;<strong>var</strong></span><strong><span> id</span><span>;</span></strong></li>
<li><span>&nbsp;function</span><span> animationLoop</span><span>(<span style="line-height: 25.6000003814697px;">timeStamp</span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp;</span><span>// 1 - Clear</span></li>
<li><span>&nbsp; &nbsp;ctx</span><span>.</span><span>clearRect</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> canvas</span><span>.</span><span>width</span><span>,</span><span> canvas</span><span>.</span><span>height</span><span>);</span></li>
<li><span>&nbsp; &nbsp;</span><span>// 2 Draw</span></li>
<li><span>&nbsp; &nbsp;drawShapes</span><span>(...);</span></li>
<li><span>&nbsp; &nbsp;</span><span>// 3 Move</span></li>
<li><span>&nbsp; &nbsp;moveShapes</span><span>(...)</span></li>
<li><span>&nbsp; &nbsp;</span><span>// call again mainloop after XXX milliseconds</span></li>
<li><span>&nbsp; &nbsp;</span><strong><span>requestAnimationFrame</span><span>(</span><span>animationLoop</span><span>);</span></strong></li>
<li><span> </span><span>}</span><span> </span></li>
<li><span>&nbsp;</span></li>
<li><span>&nbsp;function</span><span> startAnimation</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp;<strong>id </strong></span><strong><span>=</span><span> requestAnimationFrame</span><span>(</span><span>animationLoop</span><span>);</span></strong></li>
<li><span> </span><span>}</span></li>
<li><span>&nbsp;</span></li>
<li><span>&lt;/script&gt;</span></li>
<li><span>&lt;/body&gt;</span></li>
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

<div><ol>
<li value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li><span>&lt;head&gt;</span></li>
<li><span> </span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li><span> </span><span>&lt;title&gt;</span><span>Click listener version 1</span><span>&lt;/title&gt;</span></li>
<li><span>&lt;/head&gt;</span></li>
<li><span>&lt;body&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><strong><span>&lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>saySomething</span><span>();</span><span>"</span><span>&gt;</span><span>Click me!</span><span>&lt;/button&gt;</span></strong></li>
<li><span>&lt;/body&gt;</span></li>
<li><span></span></li>
<li><span> </span><span>&lt;script&gt;</span></li>
<li><span>&nbsp; &nbsp;</span><strong><span>function</span><span> saySomething</span><span>()</span></strong><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; console</span><span>.</span><span>log</span><span>(</span><span>"Hello!"</span><span>);</span></li>
<li><span>&nbsp; &nbsp;</span><span>}</span></li>
<li><span> </span><span>&lt;/script&gt;</span></li>
<li><span>&lt;/html&gt;</span></li>
</ol></div>

7. Too simple? 

  The above code shows a way to detect a click on a button (line 8). It works fine for simple examples, but in the course we criticized this method. What are its faults?

  a. Mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) is not the recommended way for full scale applications where a clean separation is best.<br/>
  b. It doesn't work with all events, only with 'click' events.<br/>

  Ans: a<br/>
  Explanation: Indeed, this is not the recommended way to handle events, even if it is very easy to use. Mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) in one place is ok for small examples (as seen in this course), but is not the recommended way for full scale applications where a clean separation is best. Notice that with this method we can pass an event to the callback function; see this example on JS Bin: http://jsbin.com/gixuku/edit.


__Source code for the next question (8):__

<div><ol>
<li value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li><span>&lt;head&gt;</span></li>
<li><span> </span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li><span> </span><span>&lt;title&gt;</span><span>Click listener version 2</span><span>&lt;/title&gt;</span></li>
<li><span>&lt;/head&gt;</span></li>
<li><span>&lt;body&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><strong><span>&lt;button</span><span> </span><span>id</span><span>=</span><span>"myButton"</span><span>&gt;</span><span>Click me!</span><span>&lt;/button&gt;</span></strong></li>
<li><span>&lt;/body&gt;</span></li>
<li><span> </span><span>&lt;script&gt;</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>var</span><span> button </span><span>=</span><span> document</span><span>.</span><span>getElementById</span><span>(</span><span>"myButton"</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; <strong>// Add an onclick listener to the button &nbsp;&nbsp;</strong></span></li>
<li><strong><span>&nbsp; &nbsp; button</span><span>.</span><span>onclick </span><span>=</span><span> saySomething</span><span>;</span></strong></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>function</span><span> saySomething</span><span>(</span><span>event</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; console</span><span>.</span><span>log</span><span>(</span><span>"Hello! Button with id: "</span><span> </span><span>+</span><span> event</span><span>.</span><span>target</span><span>.</span><span>id </span><span>+</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; " has been clicked"</span><span>);</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span> </span><span>&lt;/script&gt;</span></li>
<li><span>&lt;/html&gt;</span></li>
</ol></div>

8. Click on me please!

  What is the disadvantage of the method used in the above example for defining an event listener (line 14)?

  a. We cannot declare multiple click event listeners.<br/>
  b. The event parameter at line 16 above is always undefined. We cannot get the event with this method.<br/>

  Ans: a<br/>
  Explanation: This method is ok, but you will not be able to attach several click listener functions. For example, you may have three buttons, and you would like a click on any of them to call the same function. In that function you could get the event and test event.target.id to find out which button has been clicked.


__Source code for the next question (9):__

<div><ol>
<li value="1"><span>&lt;body</span><span> </span><span>onload</span><span>=</span><span>"</span><span>init</span><span>();</span><span>"</span><span>&gt;</span></li>
<li><span>&nbsp; &lt;canvas</span><span> </span><span>id</span><span>=</span><span>"myCanvas"</span><span> </span><span>width</span><span>=</span><span>"400"</span><span> </span><span>height</span><span>=</span><span>"400"</span><span>&gt;</span></li>
<li><span>&nbsp; &nbsp; Your browser does not support the canvas tag.</span></li>
<li><span>&nbsp; &lt;/canvas&gt;</span></li>
<li><span style="color: #000088;" color="#000088">&nbsp;&nbsp;</span>&lt;script&gt;</li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> canvas</span><span>,</span><span> ctx</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> x</span><span>=</span><span>100</span><span>,</span><span> y</span><span>=</span><span>100</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> incrementX </span><span>=</span><span> </span><span>0</span><span>;</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>function</span><span> init</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;canvas </span><span>=</span><span> document</span><span>.</span><span>getElementById</span><span>(</span><span>'myCanvas'</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span>=</span><span>canvas</span><span>.</span><span>getContext</span><span>(</span><span>'2d'</span><span>);</span></li>
<li><span></span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window</span><span>.</span><span>addEventListener</span><span>(</span><span>'keydown'</span><span>,</span><span> handleKeydown</span><span>,</span><span> </span><span>false</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window</span><span>.</span><span>addEventListener</span><span>(</span><span>'keyup'</span><span>,</span><span> handleKeyup</span><span>,</span><span> </span><span>false</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;requestId </span><span>=</span><span> requestAnimationFrame</span><span>(</span><span>animationLoop</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>}</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>function</span><span> handleKeydown</span><span>(event</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>if</span><span> </span><span>(event</span><span>.</span><span>keyCode </span><span>===</span><span> </span><span>37</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>//left key </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;incrementX </span><span>=</span><span> </span><span>-</span><span>1</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span><span> </span><span>else</span><span> </span><span>if</span><span> </span><span>(event</span><span>.</span><span>keyCode </span><span>===</span><span> </span><span>39</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>// right key</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;incrementX </span><span>=</span><span> </span><span>1</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span></li>
<li><span></span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>function</span><span> handleKeyup</span><span>(event</span><span>)</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;incrementX </span><span>=</span><span> </span><span>0</span><span>;</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span>function</span><span> animationLoop</span><span>()</span><span> </span><span>{</span></strong></li>
<li><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span>.</span><span>clearRect</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> canvas</span><span>.</span><span>width</span><span>,</span><span> canvas</span><span>.</span><span>height</span><span>);</span></strong></li>
<li><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>10</span><span>);</span></strong></li>
<li><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x </span><span>+=</span><span> incrementX</span><span>;</span></strong></li>
<li><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; requestId </span><span>=</span><span> requestAnimationFrame</span><span>(</span><span>animationLoop</span><span>);</span></strong></li>
<li><strong><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span></strong><span> </span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;function</span><span> start</span><span>()</span><span> </span><span>{</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>// Start the animation loop, targets 60 frames/s</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;requestId </span><span>=</span><span> requestAnimationFrame</span><span>(</span><span>animationLoop</span><span>);</span></li>
<li><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span></li>
<li><span>&lt;/script&gt;</span></li>
<li><span>&lt;/body&gt;</span></li>
</ol></div>

9. Left or right?

  What does the above code do (note: it works! there are no errors in it)?

  a. It draws a small stationary rectangle, and if we use the left and right arrow keys, it moves horizontally to the left or to the right, respectively.<br/>
  b. It draws a small stationary rectangle and if we press the arrow keys, nothing happens.<br/>

  Ans: a<br/>
  Explanation: The above code will display a small rectangle at position x, y = (100, 100), but when an arrow key is pressed, the incrementX variable goes from 0 to -1 or +1 (lines 23 or 26), and then the x position is incremented/decremented in the loop that is executed 60 times/s. The instruction at line 37 will make it move to the left or to the right. Try it: http://jsbin.com/balenu/edit


__Source code for the next question (10):__

This is the `drawMonster` function from the course.

<div><ol>
<li value="1"><span> </span><span>function</span><span> drawMonster</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> angle</span><span>,</span><span> headColor</span><span>,</span><span> eyeColor</span><span>)</span><span> </span><span>{</span><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// BEST PRACTICE: SAVE CONTEXT AND RESTORE IT AT THE END</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>save</span><span>();</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// Moves the coordinate system so that the monster is drawn</span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// at position (x, y)</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>translate</span><span>(</span><span>x</span><span>,</span><span> y</span><span>);</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>rotate</span><span>(</span><span>angle</span><span>)</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// head</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillStyle</span><span>=</span><span>headColor</span><span>;</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>0</span><span>,</span><span>0</span><span>,</span><span>200</span><span>,</span><span>200</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// eyes</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillStyle</span><span>=</span><span>'red'</span><span>;</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>35</span><span>,</span><span>30</span><span>,</span><span>20</span><span>,</span><span>20</span><span>);</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>140</span><span>,</span><span>30</span><span>,</span><span>20</span><span>,</span><span>20</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// interior of eye</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillStyle</span><span>=</span><span>eyeColor</span><span>;</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>43</span><span>,</span><span>37</span><span>,</span><span>10</span><span>,</span><span>10</span><span>);</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>143</span><span>,</span><span>37</span><span>,</span><span>10</span><span>,</span><span>10</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// Nose</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillStyle</span><span>=</span><span>'black'</span><span>;</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>90</span><span>,</span><span>70</span><span>,</span><span>20</span><span>,</span><span>80</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// Mouth</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillStyle</span><span>=</span><span>'purple'</span><span>;</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>fillRect</span><span>(</span><span>60</span><span>,</span><span>165</span><span>,</span><span>80</span><span>,</span><span>20</span><span>);</span></li>
<li><span> </span></li>
<li><span>&nbsp; &nbsp;&nbsp;</span><span>// BEST PRACTICE!</span></li>
<li><span>&nbsp; &nbsp; ctx</span><span>.</span><span>restore</span><span>();</span></li>
<li><span> </span><span>}</span></li>
<li><span> </span></li>
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



