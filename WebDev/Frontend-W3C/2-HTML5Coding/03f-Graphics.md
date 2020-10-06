# Week 3: HTML5 Graphics


## 3.6 Exercises - Week 3


### 3.6.1 Intro exercises - Week 3

Here is an opportunity to show that you have learned the basics of drawing 2D Web graphics, and are ready to proceed with the rest of the course.

Please complete the following 33 exercises in a timely manner. As stated in the grading policy page, they count towards 15% of your final grade.



### 3.6.2 Basics of HTML5 canvas (1-7)

1. Hardware acceleration?

  Nowadays, most major desktop browsers take advantage of hardware acceleration in their implementation of the canvas API: (True/False)

  Ans: True<br/>
  Explanation: Indeed, most (all?) major browsers use hardware acceleration for drawing and animating in the HTML5 canvas. This is also true of their respective mobile versions.


2. Where is my context?

  <pre>  function init() {
      // This function is called after the page is loaded
      // 1 - Get the canvas
      canvas = document.getElementById('myCanvas');
      // 2 - Get the context
      ctx = <b>AAA</b>
      // 3 - We can draw
      drawSomething();
    }
  </pre>

  How do you set the graphic context of the above canvas for drawing in 2D? What would you use instead of the __AAA__ string in the code above?

  a. `canvas.createContext('webgl');`<br/>
  b. `canvas.createContext('2d');`<br/>
  c. `canvas.getContext('2d');`<br/>
  d. `canvas.getContext();`<br/>

  Ans: c<br/>
  Explanation: The correct way to get a context for 2D graphics is `ctx = canvas.getContext('2d');`.


3. Where is my pixel?

  In a canvas of size 400x400 pixels, where is the pixel at x=300, y=100 located?

  a. In the bottom right quadrant of the canvas<br/>
  b. In the top right quadrant of the canvas<br/>
  c. In the bottom left quadrant of the canvas<br/>
  d. In the top left quadrant of the canvas<br/>

  Ans: b<br/>
  Explanation: In the canvas coordinate system, the X axis is horizontal, directed to the right, and the Y axis is vertical, directed downwards. The (300, 100) position is located in the top right quadrant of the canvas.



4. Prepare your backpack

  What is __absolutely necessary__ to do before drawing in a canvas? (4 correct answers.)

  a. Declare a canvas element in the HTML code.<br/>
  b. Add CSS rules for drawing a border around the canvas.<br/>
  c. Get the canvas using the DOM API (in other words: set a variable that points to the canvas).<br/>
  d. Get the canvas graphic context (from the canvas object).<br/>
  e. Be sure that the page has been loaded and that the DOM is ready before trying to access the canvas element using the DOM API.<br/>

  Ans: acde<br/>
  Explanation: Indeed, we must 1) declare a canvas element in the HTML code, 2) access the canvas, but 3) be sure that the DOM of the page has been built before requesting the canvas using the DOM API (getElementById, querySelector etc.) and 4) get the grahic context from the canvas object. Having a CSS border is not necessary.


5. Change my color!

  <pre>var canvas = document.querySelector("#myCanvas");
  var ctx = canvas.getContext("2d");
  ...
  </pre>

  What property is useful for setting the color of wireframe shapes?

  a. `ctx.fillStyle`<br/>
  b. `canvas.color`<br/>
  c. `ctx.strokeStyle`<br/>
  d. `ctx.color`<br/>
  e. `canvas.color`<br/>
  f. `canvas.strokeStyle`<br/>

  Ans: c<br/>
  Explanation: We only set the color using a context property, not a canvas property: `strokeStyle` for wireframe shapes and `fillStyle` for filled shapes.


__Source code for the next question (6)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// 1 - Get the canvas</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// 2 - Get the context</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// 3 - Let's draw</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> drawSomething</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="com">// WHAT COLOR WILL THIS SHAPE BE?</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawSomething</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// set the global context values</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'blue'</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// font for all text drawing</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">'italic 20pt Calibri'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw the two filled red rectangles</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">110</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw the two blue wireframe rectangles</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">110</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw a message above the rectangles</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"hello"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">22</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>

6. Global or local?

  What will be the color of the wireframe rectangle (color of its outline) drawn after the call to drawSomething() (the line that draws the rectangle is at line 13, in bold)?

  a. blue<br/>
  b. black (default color)<br/>
  c. red<br/>

  Ans: a<br/>
  Explanation: `strokeStyle` for wireframe shapes and `fillStyle` for filled shapes are sort of "global variables". The call to `drawSomething()` will set the strokeStyle property to 'blue' (line 20), then all wireframe shapes drawn after this will be blue. `ctx.strokeRect(...)` will draw a blue wireframe rectangle.  Check this correction on JS Bin with the example from the question, you can clearly see a blue wireframe rectangle. Comment the call to `drawSomething()`, it will be black.


7. Write me a message!

  Which of these methods and properties are specialized for drawing text? Select the valid examples: (2 correct answers.)

  a. `ctx.drawText("Hello World", 100, 100);`<br/>
  b. `ctx.police = 'italic 20pt Calibri';`<br/>
  c. `ctx.strokeText(100, 100, "Hello World");`<br/>
  d. `ctx.fillText("Hello World", 100, 100);`<br/>
  e. `ctx.setFont('italic 20pt Calibri');`<br/>
  f. `ctx.font = 'italic 20pt Calibri';`<br/>

  Ans: df<br/>
  Explanation: `ctx.fillText(message, x, y)` and `ctx.font` are correct.


### 3.6.3 2D transformations (8-10)

8. Transform me!

  Which of these methods are valid for applying 2D transformations to the coordinate system? (3 correct answers.)

  a. `ctx.zoom(zoomFactor)`<br/>
  b. `ctx.translate(x, y)`<br/>
  c. `ctx.rotate(angle)`<br/>
  d. `ctx.rotateX(angle)`<br/>
  e. `ctx.rotateY(angle)`<br/>
  f. `ctx.scale(sx, sy)`<br/>

  Ans: <br/>
  Explanation: 



9. Translate then rotate, or rotate then translate?

  <pre>// VERSION 1
  ctx.translate(100, 100);
  ctx.rotate(Math.PI/4);

  // VERSION 2
  ctx.rotate(Math.PI/4);
  ctx.translate(100, 100);
  </pre>

  Will the two instructions of version 1 in the above code produce the same results as the two lines of version 2? (Yes/No)

  Ans: <br/>
  Explanation: 



10. Global or local transformations?

  <pre>&lt;canvas id="myCanvas" width=400 height=600&gt;&lt;/canvas&gt;
  </pre>
  ...
  <pre>ctx.translate(100, 60);
  ctx.rotate(Math.PI/4);
  // First drawing
  ctx.fillRect(0, 0, 100, 100);
  // second drawing
  ctx.strokeRect(100, 100, 100, 100);
  </pre>

  How many rectangles will be drawn in the translated and rotated coordinate system?

  a. Both rectangles.<br/>
  a. Only the first rectangle.<br/>

  Ans: <br/>
  Explanation: 







