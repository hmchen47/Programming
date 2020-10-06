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

  Ans: bcf<br/>
  Explanation: There are no rotateX or rotateY methods, nor a zoom method.



9. Translate then rotate, or rotate then translate?

  <pre>// VERSION 1
  ctx.translate(100, 100);
  ctx.rotate(Math.PI/4);

  // VERSION 2
  ctx.rotate(Math.PI/4);
  ctx.translate(100, 100);
  </pre>

  Will the two instructions of version 1 in the above code produce the same results as the two lines of version 2? (Yes/No)

  Ans: <span style="color: magenta;">No</span>, Yes<br/>
  Explanation: The order of transformation is important. If we translate (100, 0), then rotate PI/4, we will have a coordinate system with its origin at (100, 0) rotated. If we first rotate, then the translation will move 100 pixels along the rotated X axis. The origin will no longer be at (100, 0). The two versions will produce different results.



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
  b. Only the first rectangle.<br/>

  Ans: a<br/>
  Explanation: Any transformation applied to the coordinate system is "global" and will affect all future drawings. The correct answer is "both rectangles".


### 3.6.4 Saving and restoring the context (11-12)

11. Changing the context?

  What does "changing the context" mean?

  a. Changing only the coordinate system by calling 2D transformation methods of the context.<br/>
  b. Either changing any property of the context (lineWidth, font, etc.) or changing the coordinate system by applying 2D transformations to the coordinate system.<br/>
  c. Changing only the value of the fillStyle or strokeStyle property.<br/>

  Ans: <span style="color: magenta;">b</span>, c<br/>
  Explanation: Any modification in the context properties or any 2D transformation changes the context.



12. Best practice?

  What best practice has been introduced in the course?

  a. Call `ctx.save()` at the beginning of any function that changes the context, call `ctx.restore()` at the end of the function.<br/>
  a. No need to save / restore the context, it suffices to set fillStyle, strokeStyle, lineWidth, etc. and apply the correct 2D transforms before any drawing.<br/>

  Ans: a<br/>
  Explanation: Of course, the best practice is to save the context at the beginning of any function that changes the context, and then restore it at the end of the function.


### 3.6.5 Immediate drawing mode (13-18)

13. Immediate shapes?

  Which shapes can be drawn in immediate mode? (3 correct answers.)

  a. Line<br/>
  b. Image<br/>
  c. Rectangle<br/>
  d. Circle<br/>
  e. Text<br/>
  f. Polygon<br/>

  Ans: bce<br/>
  Explanation: Only `rectangles`, `text` and `images` can be drawn in immediate mode.



14. Undersize me!

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick="window.open('https://tinyurl.com/y3aaeuzj')"
      src    ="https://tinyurl.com/y3a63ey3"
      alt    ="the text Hello World is written many times and in different sizes using maxWidth and in different colors using fillText"
      title  ="the text Hello World is written many times and in different sizes using maxWidth and in different colors using fillText"
    />
  </figure>

  How would you do the drawing above?

  a. I would draw these shapes using images stretched with Photoshop, for example, and call ctx.drawImage(...).<br/>
  b. I would use the `maxWidth` parameter of the `strokeText` or `fillText` method of the context.<br/>
  c. I would use a different character font for each line, using the font property of the context.<br/>

  Ans: b<br/>
  Explanation: The `maxWidth` parameter of the `strokeText` or the `fillText` method of the context have been especially designed for setting constraints on the horizontal size of the text.



15. Not yet there...

  Drawing images before they have been entirely loaded by the browser...

  a. Is a bad practice.<br/>
  b. Is ok, images will be drawn incomplete and the missing data will appear as data is loaded, line by line.<br/>

  Ans: a<br/>
  Explanation: No, trying to draw an image that has not been completely loaded in memory will produce unpredictable results.



__Source code for the next question (16)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// It is necessary to wait until the web page has loaded before running this code.</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myCanvas"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> context </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">"2d"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> imageObj </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong>// load the image</strong></span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;imageObj</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln"> </span><span class="str">"https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png"</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln"> </span><span class="com">// draw the image</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></strong><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"512"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"512"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

16. Call me back please!

  What's wrong with the above code?

  a. The instruction at line 16 will try to draw an image without being sure it has entirely loaded.<br/>
  b. Nothing.<br/>

  Ans: a<br/>
  Explanation: The instruction at line 12 will start loading the image in the background. However, before the image has been entirely loaded, the instruction at line 16 will try to draw it. This will not work. We must be sure that the image has been entirely loaded before trying to draw it. The course shows how to create a callback function that will be called only when the image is ready to be drawn.


__Source code for the next question (17)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"512"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"512"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Original image as an </span><span class="tag">&lt;img&gt;</span><span class="pln"> element:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"logo"</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"http://orig15.deviantart.net/0b3d/f/2013/149/b/8/texture_85_by_voyager168-d670m68.jpg"</span><span class="tag">&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myCanvas"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">"2d"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> logo </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#logo"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>&nbsp;ctx</strong></span><strong><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">logo</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

17. Am I completely here?

  Will the above code draw the image every time, even with a large image that is not in the browser's cache? (Yes/No)

  Ans: b<br/>
  Explanation: No, this example comes from the course content. This code may work if the image is very small or is located in the browser cache, but we cannot repeat it often enough: you cannot draw an image in a canvas until you are 100% sure that it has been loaded into memory. The course shows how to do this, using the onload event. Here is the [correct version](https://jsbin.com/faqedu/edit), and here the [same version with a very large image](https://jsbin.com/mayoma/edit).


18. Video screenshot?

  Can `ctx.drawImage(...)` take as first parameter a video and draw the current frame displayed in a video element?

  a. Only with the Webcam stream<br/>
  b. Yes<br/>
  c. It depends on the codec<br/>
  d. No<br/>

  Ans: b<br/>
  Explanation: We have seen in the course that `drawImage` can be used to draw the current frame of a video being played.


### 3.6.6 Path drawing mode (19-25)

19. Path mode?

  What is path mode useful for?

  a. Enabling optimization and parallel processing - all drawing orders are stored in a buffer in the Graphic Processor Unit of the graphics card.<br/>
  b. It's just useful for drawing lines, arcs and curves - there is nothing special about performance.<br/>
  
  Ans: a<br/>
  Explanation: Indeed, having multiple drawing orders in a buffer enables optimization.



20. Choose the right shapes!

  Which of the following shapes can be drawn in path mode? (3 correct answers.)

  a. Line<br/>
  b. Text<br/>
  c. Circle or arc<br/>
  d. Curve (Bézier, quadratic curve)<br/>
  e. Image<br/>
  
  Ans: acd<br/>
  Explanation: Lines, arcs and circles, and curves (Bézier, quadratic) are all in path mode.


21. Two or three lines? (Part 1)

  <pre>ctx.moveTo(20,20);
  ctx.lineTo(100, 100);
  ctx.lineTo(100,0);
  ctx.closePath();

  ctx.strokeStyle = "red";
  ctx.stroke();
  </pre>

  What does the above code do?

  a. It draws a red wireframe triangle.<br/>
  b. It draws two red lines.<br/>

  Ans: a<br/>
  Explanation: The call to `ctx.closePath()` will join the last extremity of the last line to the beginning of the path, forming a triangle.
  

22. Two or three lines? (Part 2)

  <pre>ctx.strokeStyle = "blue";

  ctx.moveTo(20,20);
  ctx.lineTo(100, 100);
  ctx.lineTo(100,0);
  ctx.stroke();

  ctx.moveTo(120,20);
  ctx.lineTo(200, 100);
  ctx.lineTo(200,0);
  ctx.fillStyle = 'red'
  ctx.fill();
  </pre>

  What will the above code produce as a final result on screen?

  a. We will see two red filled triangles, one on the left with two blue lines, and the other triangle on the right.<br/>
  b. We will see two blue lines, and on the right, a single red filled triangle.<br/>
  
  Ans: a<br/>
  Explanation: The last call to `fill()` will execute all the drawing orders in the buffer: the two sets of lines will be drawn, and as we are in filled mode, they will appear as red triangles. The same example is in the course.


23. Empty that buffer please!

  What context method should we call to empty the buffer/clear the path?

  a. `ctx.reset()`<br/>
  b. `ctx.beginPath()`<br/>
  c. `ctx.clearPath()`<br/>
  d. `ctx.empty()`<br/>
  
  Ans: b<br/>
  Explanation: The right answer is `ctx.beginPath()`. This method is very useful for drawing disconnected shapes that use path mode, and that have different colors, width, etc.


24. Your watch on the right or left wrist?

  <pre>// arc of circle starting from 0 to PI/2, located in (100, 100), with radius = 100
  ctx.arc(100, 100, 100, 0, Math.PI/2);
  ctx.stroke();
  </pre>

  The arcs are drawn...

  a. Clockwise<br/>
  b. Counterclockwise<br/>
  
  Ans: a<br/>
  Explanation: Indeed, arcs are drawn clockwise.


25. "Black and blue", not my favorite Rolling Stones record...

  <pre>// arc located in (100, 100), radius = 100, full circle from 0 to 2*PI
  ctx.arc(100, 100, 100, 0, 2*Math.PI);
  ctx.fillStyle = "lightBlue";
  ctx.lineWidth = 5;
  ctx.strokeStyle = "black";
  ctx.fill();
  ctx.stroke();
  </pre>

  What if we execute the above code excerpt? Does it...

  a. Draw just a filled, light blue circle.<br/>
  b. Draw a light blue, filled, circle, with a black outline of 5px.<br/>
  c. Draw a wireframe black circle, with an outline width of 5px.<br/>

  Ans: b<br/>
  Explanation: The two consecutive calls to `fill()` and `stroke()` will draw the same shape, but using the relevant ctx properties: fill will draw a light blue filled circle, then stroke() will draw a black wireframe circle over it, with a line width of 10px. Final result will be a blue circle with a black wireframe.








