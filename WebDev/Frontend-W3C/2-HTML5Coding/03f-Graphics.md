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

<div><ol>
<li value="1"> var canvas, ctx;</li>
<li> </li>
<li> function init() {</li>
<li> // This function is called after the page is loaded</li>
<li> // 1 - Get the canvas</li>
<li> canvas = document.getElementById('myCanvas');</li>
<li> // 2 - Get the context</li>
<li> ctx = canvas.getContext('2d');</li>
<li> // 3 - Let's draw</li>
<li> drawSomething();</li>
<li> </li>
<li><strong>// WHAT COLOR WILL THIS SHAPE BE?</strong></li>
<li><strong> ctx.strokeRect(100, 100, 150, 150);</strong></li>
<li> }</li>
<li> </li>
<li> function drawSomething() {</li>
<li> // set the global context values</li>
<li> ctx.lineWidth = 5;</li>
<li> ctx.fillStyle = 'red';</li>
<li> ctx.strokeStyle = 'blue';</li>
<li> // font for all text drawing</li>
<li> ctx.font = 'italic 20pt Calibri';</li>
<li> </li>
<li> // Draw the two filled red rectangles</li>
<li> ctx.fillRect(10, 30, 70, 150);</li>
<li> ctx.fillRect(110, 30, 70, 150);</li>
<li> </li>
<li> // Draw the two blue wireframe rectangles</li>
<li> ctx.strokeRect(10, 30, 70, 150);</li>
<li> ctx.strokeRect(110, 30, 70, 150);</li>
<li> </li>
<li> // Draw a message above the rectangles</li>
<li> ctx.fillText("hello", 70, 22); </li>
<li> }</li>
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
  ...
  ctx.translate(100, 60);
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

  Ans: <span style="color: magenta;">b</span>, xc<br/>
  Explanation: Any modification in the context properties or any 2D transformation changes the context.



12. Best practice?

  What best practice has been introduced in the course?

  a. Call `ctx.save()` at the beginning of any function that changes the context, call `ctx.restore()` at the end of the function.<br/>
  b. No need to save / restore the context, it suffices to set fillStyle, strokeStyle, lineWidth, etc. and apply the correct 2D transforms before any drawing.<br/>

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

<div><ol>
<li value="1">&lt;!DOCTYPE HTML&gt;</li>
<li>&lt;html&gt;</li>
<li>&lt;head&gt;</li>
<li>&lt;script&gt;</li>
<li> window.onload = function() {</li>
<li> // It is necessary to wait until the web page has loaded before running this code.</li>
<li> var canvas = document.getElementById("myCanvas");</li>
<li> var context = canvas.getContext("2d");</li>
<li> </li>
<li> var imageObj = new Image();</li>
<li>&nbsp;<strong>// load the image</strong></li>
<li><strong>&nbsp;imageObj.src = </strong></li>
<li><strong> "https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png";</strong></li>
<li><strong>&nbsp;</strong></li>
<li><strong> // draw the image</strong></li>
<li><strong>&nbsp;context.drawImage(imageObj, 0, 0);</strong> </li>
<li> };</li>
<li> &lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;canvas id="myCanvas" width="512" height="512"&gt;&lt;/canvas&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

16. Call me back please!

  What's wrong with the above code?

  a. The instruction at line 16 will try to draw an image without being sure it has entirely loaded.<br/>
  b. Nothing.<br/>

  Ans: a<br/>
  Explanation: The instruction at line 12 will start loading the image in the background. However, before the image has been entirely loaded, the instruction at line 16 will try to draw it. This will not work. We must be sure that the image has been entirely loaded before trying to draw it. The course shows how to create a callback function that will be called only when the image is ready to be drawn.


__Source code for the next question (17)__

<div><ol>
<li value="1">&lt;body&gt;</li>
<li> &lt;canvas id="myCanvas" width="512" height="512"&gt;&lt;/canvas&gt;</li>
<li> &lt;p&gt;Original image as an &lt;img&gt; element:&lt;/p&gt;</li>
<li> <strong>&lt;img id="logo"</strong></li>
<li><strong> src="http://orig15.deviantart.net/0b3d/f/2013/149/b/8/texture_85_by_voyager168-d670m68.jpg"&gt;</strong></li>
<li></li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp;var canvas = document.getElementById("myCanvas");</li>
<li>&nbsp; &nbsp; &nbsp;var ctx = canvas.getContext("2d");</li>
<li>&nbsp; &nbsp; &nbsp;var logo = document.querySelector("#logo");</li>
<li>&nbsp; &nbsp; <strong>&nbsp;ctx</strong><strong>.drawImage(logo, 0, 0, 100, 100);</strong></li>
<li>&lt;/script&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

17. Am I completely here?

  Will the above code draw the image every time, even with a large image that is not in the browser's cache? (Yes/No)

  Ans: No<br/>
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


### 3.6.7 Drawing styles (26-33)

26. Choose your style!

  Which of the following are possible values for the strokeStyle or fillStyle context properties? (3 correct answers.)

  a. An image
  b. A gradient<br/>
  c. A video<br/>
  d. A pattern<br/>
  e. A color<br/>

  Ans: bde<br/>
  Explanation: These context properties can get the value of a color, a pattern or a gradient.


27. My favorite color is...

  <pre>ctx.fillStyle = "rgba(0, 0, 255, 0.5)";
  </pre>

  What color is set by the above code?

  a. Semi transparent blue<br/>
  b. Opaque blue<br/>
  c. Opaque red<br/>

  Ans: a<br/>
  Explanation: Indeed the RGBA CSS3 notation for color takes as the fourth parameter an "alpha channel" that corresponds to the degree of transparency, between 0 (full transparency) and 1 (100% opaque). 0.5 means "half transparent".


28. Color stop!

  What is a "gradient color stop"?

  a. One of the set of points defining the distribution of colors along the gradient.<br/>
  b. The name of the last color of the gradient.<br/>

  Ans: a<br/>
  Explanation: Once a gradient has been created, color stops are placed along it to define how the colors are distributed along the gradient. The color of the gradient at each stop is the color specified for that stop. Between each such stop, the colors and the alpha component must be linearly interpolated over the RGBA space without premultiplying the alpha value to find the color to use at that offset. Before the first stop, the color must be the color of the first stop. After the last stop, the color must be the color of the last stop. When there are no stops, the gradient is transparent black.


29. Visible or not?

  A gradient is invisible until we draw shapes on top of it in the canvas? (True/False)

  Ans: True<br/>
  Explanation: The concept of gradient is seen as an "invisible" rectangle or circle-like shape in which a set of colors are interpolated. The gradient becomes visible when we draw shapes on top of the invisible gradient, and when the fillStyle or strokeStyle property has this gradient as its value.


30. Psychedelia!

  <pre><b>var grd = context.createRadialGradient(150, 100, 30, 150, 100, 100);</b>
  grd.addColorStop(0, "red");
  grd.addColorStop(0.17, "orange");
  grd.addColorStop(0.33, "yellow");
  grd.addColorStop(0.5, "green");
  grd.addColorStop(0.666, "blue");
  grd.addColorStop(1, "violet");
  context.fillStyle = grd;
  </pre>

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://tinyurl.com/y2zkyegy" ismap target="_blank">
      <img style="margin: 0.1em;" height=100
        src  ="https://tinyurl.com/yxo2oayb"
        alt  ="first image shows a symmetric radial gradient"
        title="first image shows a symmetric radial gradient"
      >
      <img style="margin: 0.1em;" height=100
        src  ="https://tinyurl.com/y427ngpr"
        alt  ="second image shows an asymmetric radial gradient"
        title="second image shows an asymmetric radial gradient"
      >
    </a>
  </div>


  Will this gradient produce a result like that in the first or in the second image?

  a. First<br/>
  b. Second<br/>

  Ans: a<br/>
  Explanation: The parameters of createLinearGradient define two circles. Colors will be interpolated from the outline of the first circle to the outline of the second one. The circles in `context.createRadialGradient(150, 100, 30, 150, 100, 100)` are located at the same place (150, 100). This will produce a symmetric gradient that corresponds to the first image.


31. Pattern and images are the same?

  Unlike images, when using patterns we do not need to check if they have been loaded completely by the browser? (False/True)

  Ans: False<br/>
  Explanation: No, this is false, patterns are images that will be used to draw shapes, eventually repeating them horizontally or vertically. It's necessary to define a callback function that will be called once the pattern has been fully loaded in memory (a pattern is an image), we cannot draw using a pattern before the corresponding image has been loaded.


32. Who is standing in the shadow?

  <pre>ctx.shadowColor = "Grey";
  ctx.shadowBlur = 20;
  ctx.shadowOffsetX = 15;
  ctx.shadowOffsetY = 15;  

  ctx.fillStyle = 'red'; 
  ctx.fillRect(20, 20, 200, 100);

  ctx.strokeStyle = 'purple'; 
  ctx.lineWidth=10;
  ctx.strokeRect(20, 150, 200, 100);
  </pre>

  What will the above code produce (we suppose there is a canvas, and ctx has been correctly initialized)?

  a. The shadow will not be visible at all as the blur property takes only values between 0 (opaque color) and 1 (full blurred).<br/>
  b. Two rectangles: one filled red with shadows, another one wireframe purple with an outline of 10px, also with shadows.<br/>
  c. Only the filled rectangle will have shadows, wireframe shapes are not affected.<br/>

  Ans: b<br/>
  Explanation: The definition of shadows is correct (grey, small blur, corresponding to a light source in the top left corner), and will affect all shapes. The right answer is: the two rectangles will both have shadows.


33. Please, set the line with style!

  Which are valid context properties for setting line styles: (3 correct answers.)

  a. `lineCap`<br/>
  b. `lineStyle`<br/>
  c. `lineJoin`<br/>
  d. `lineJoints`<br/>
  e. `lineWidth`<br/>

  Ans: ace<br/>
  Explanation: lineCap, lineJoin and lineWidth are valid properties. The others do not exist.




