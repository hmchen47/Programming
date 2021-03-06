# Week 3: HTML5 Graphics

## 3.5 Colors, gradients, patterns, etc.


### 3.5.0 Lecture Notes

+ [Colors and transparency](#colors-and-transparency)
  + same syntax for [colors supported by CSS3](https://www.w3.org/TR/css-color-3/)
  + rgba =  red, green, blue & alpha channel
  + alpha channel: value btw 0 (completely transparent) and 1 (opaque)
  + examples:
    + `ctx.strokeStyle = 'red';`
    + `ctx.fillStyle = "#00ff00";`
    + `ctx.strokeStyle = "rgb(0, 0, 255)";`
    + `ctx.fillStyle = "rgba(0, 0, 255, 0.5)";`
  
+ [Linear Gradient](#352-canvas-context-linear-gradients)
  + visible gradient: draw shapes on top of the invisible gradient
  + procedure to create gradients
    + define linear gradient: `ctx.createLinearGradient(x0,y0,x1,y1);`
      + `(x0, y0)` and `(x1, y1)` parameters define "the direction of the gradient"
      + a vector with a starting and an ending point
      + direction: an invisible line along which the colors that compose the gradient interpolated
      + examples
        + `grdFrenchFlag = ctx.createLinearGradient(0, 0, 300, 0);`
          + a virtual, invisible line that goes from the top left corner of the canvas (0, 0) to the top right corner of the canvas (300, 0)
          + interpolated colors propagated along this line
        + `grdFrenchFlag = ctx.createLinearGradient(0, 0, 300, 200);`: a diagonal direction from (0, 0) to (300, 200)
      + good practice: create/initialize reused gradient in a function called when the page is loaded and to store it in a global variable
    + add a number of "color stops" to this gradient
      + add a set of "colors" and "stops" to this gradient
      + stops: from 0 (beginning of the virtual line defined just above), to 1 (end of the virtual line)
      + color associated w/ stop=0.5: right in the middle of the virtual line
      + example: `grdFrenchFlag.addColorStop(0, "blue"); grdFrenchFlag.addColorStop(0.5, "white"); grdFrenchFlag.addColorStop(1, "red");`
    + draw some shapes
      + set the `fillStyle` or `strokeStyle` of the context with this gradient
      + draw some shapes "on top of the gradient"
      + example: `ctx.fillStyle = grdFrenchFlag; ctx.fillRect(0, 0, 300, 200);`
  + [cheeseboard w/ gradient](#drawing-shapes-that-do-not-cover-the-whole-gradient)
    + default background color: not drawing anything
    + draw cheeseboard w/ gradient: `ctx.fillStyle = grdFrenchFlag;  ctx.fillRect(0, 0, 50, 50); ctx.fillRect(100, 0, 50, 50);  ctx.fillRect(200, 0, 50, 50); ctx.fillRect(50, 50, 50, 50);  ctx.fillRect(150, 50, 50, 50); ...`
    + alternative solution: `function drawCheckboard(n) {...}`: two loops draw only one cell out of two
  + [outlined shapes with gradients](#drawing-outlined-shapes-with-gradients)
    + use `strokeStyle` and `strokeRect` in order to draw wireframed rectangles
    + used the `lineWidth` property to set the outline of the rectangles
  + [gradient smaller than the canvas](#what-happens-if-we-define-a-gradient-smaller-than-the-canvas)
    + e.g., `grdFrenchFlag = ctx.createLinearGradient(100, 0, 200, 0);` as canvas w/ width=300, height=200
    + 1st color of the gradient: repeated w/o any interpolation (columns 0-100 are all blue)
    + "see through" and the gradient drawn (columns 100-200)
    + the last color of the gradient repeated w/o any interpolation (columns 200-300 are red)
  + [gradient bigger than the canvas](#what-happens-if-we-define-a-gradient-bigger-than-the-canvas)
    + e.g., `grdFrenchFlag = ctx.createLinearGradient(0, 0, 600, 400);`
    + red color beyond the bottom right corner
  + [same gradient in each cell](#draw-shapes-that-share-the-same-gradient-as-a-whole)
    + creates a gradient and set the fillStyle context property: `function setGradient(x, y, width, height) {...}`
      + create linear gradient w/ given width and height: `grdFrenchFlag = ctx.createLinearGradient(x, y, width, height);`
      + set pattern: `grdFrenchFlag.addColorStop(0, "blue"); grdFrenchFlag.addColorStop(0.5, "white"); grdFrenchFlag.addColorStop(1, "red");`
      + set the new gradient to the current `fillStyle`: `ctx.fillStyle = grdFrenchFlag;`
    + draw  check board w/ n rows and columns: `function drawCheckboard(n) {`...}`
      + calculate the width and height for each cell: `var cellWidth = l / n; var cellHeight = h / n;`
      + two for loops w/ alternate patterned cells: 

        ```js
        for(i = 0; i < n; i+=2) {
          for(j = 0; j < n; j++) {
            var x = cellWidth*(i+j%2);
            var y = cellHeight*j;
            setGradient(x, y, x+cellWidth, y+cellHeight);
            ctx.fillRect(x, y, cellWidth, cellHeight);
          }
        }
        ```

+ [Radial gradients](#353-canvas-context-radial-gradients)
  + creating gradients that propagate/interpolate colors along circles instead of propagating/interpolating along a virtual line, like linear gradients
  + an invisible shape on the screen
  + the radial gradient made of two circles: an inner and an outer circle
  + colors interpolated btw two circles
  + `createRadialGradient(cx1, cy1, radius1, cx2, cy2, radius2)` method:
    + `(cx1, cy1)` w/ `radius1`: the "starting" circle of the gradient
    + `(cx2, cy2)` w/ `radius2`: the "ending" circle of the gradient
  + the "first color" defined for the inner circle, the "last color" corresponding to the outer circle
    + the first color: color inside the first circle
    + the last color: color outside the outer circle
    + interpolated colors btw these two circles
  + example
    + defind the inner and outter circles: `var grd = context.createRadialGradient(150, 100, 30, 150, 100, 100);`
    + add color circles: `grd.addColorStop(0, "red");`, `grd.addColorStop(0.17, "orange");`, ..., `grd.addColorStop(1, "violet");`
    + fill all radial gradients: `context.fillStyle = grd`
  + [off center radial gradients](#what-happens-if-the-circles-are-not-located-at-the-same-place): `grd = ctx.createRadialGradient(150, 100, 30, 210, 100, 100);`

+ [Patterns / Textures](#354-canvas-context-patternstextures)
  + principle of "pattern" drawing: based on repeating an image for filling the surface of objects to be drawn (either filled or stroked)
  + SYNTAX: `context.createPattern(image,"repeat|repeat-x|repeat-y|no-repeat");`
  + procedure of creating pattern
    + creating a JavaScript image object; e.g., `var imageObj = new Image();`
    + define a callback function called once the fully loaded image in memory; e.g., `imageObj.onload = function(){...}`
    + set the source image to the URL of the pattern; e.g., `imageObj.src = "https://www.myserver.com/myRepeatablePattern.png";`
    + an HTTP request sent in background by the browser and loading the image into memory, then call the callback function
      + callback called asynchronously, after the `src` attribute of `imageObj` is set: `imageObj.onload = function(){...}`
      + enter `imageObj.onload` after image loaded to create a pattern object: `pattern1 = ctx.createPattern(imageObj, "repeat");`
      + good practice: set the pattern as a global variable, easier to share
    + draw pattern within the callback function; e.g, a textured rectangle: `ctx.fillStyle = pattern1; ctx.fillRect(10, 10, 500, 800);`

+ [Multi-image Pattern](#355-a-multiple-image-loader)
  + load all image before drawing
  + only when all images have been loaded, start drawing.
  + solution: use a multiple image loader that counts the loaded images and calls a function you pass when done
  + an array of URLs used by multiple image loader
  + onload callback called once per image loaded to count the number of images effectively loaded
  + list of images to load: `var imagesToLoad = { flowers: 'https://i.ibb.co/4NN9Sgn/flowers.jpg', lion: 'https://i.ibb.co/3NyqKnY/lion.jpg', ...}`
  + image loader function: `function loadImages(imagesToBeLoaded, drawCallback) {...}`
    + parameters: the list of images to be loaded & drawCallback function called only once all images loaded
    + counting the number of images to load: ` for(var name in imagesToBeLoaded) { numberOfImagesToLoad++; }`
    + iterate to load all images: `for(var name in imagesToBeLoaded) {...}`
    + onload callback function within iteration and draw pattern only all images loaded

      ```js
      imagesLoaded[name].onload = function() {
          if(++loadedImages >= numberOfImagesToLoad) {
              drawCallback(imagesLoaded);
          } // if
      }; // function
      ```

  + use of image loader: `loadImages(imagesToLoad, function(imagesLoaded) {...});`
    + create patterns from the loaded image:

      ```js
      patternFlowers = ctx.createPattern(imagesLoaded.flowers, 'repeat');
      patternLion    = ctx.createPattern(imagesLoaded.lion, 'repeat');
      patternBW = ctx.createPattern(imagesLoaded.blackAndWhiteLys, 'repeat'); 
      patternFloor   = ctx.createPattern(imagesLoaded.tiledFloor, 'repeat');
      ```

    + call a function to draw the rectangle: `drawRectanglesWithPatterns();`
  + function to draw rectangle w/ patterns: `function drawRectanglesWithPatterns() {...}`
    + draw each pattern w/ given rectangle area
    + floor pattern on top left corner: `ctx.fillStyle=patternFloor; ctx.fillRect(0,0,200,200);`
    + Lion pattern on top right corner: `ctx.fillStyle=patternLion; ctx.fillRect(200,0,200,200);`
    + flower pattern on bottom left corner: `ctx.fillStyle=patternFlowers; ctx.fillRect(0,200,200,200);`
    + black-white pattern on the bottom right corner: `ctx.fillStyle=patternBW; ctx.fillRect(200,200,200,200);`
  
+ [Drawing shadows](#356-drawing-shadows)
  + properties to draw shapes with shadows:
    + `shadowColor`: color to use for shadows
    + `shadowBlur`: blur level for shadows
    + `shadowOffsetX`: horizontal distance of the shadow from the shape
    + `shadowOffsetY`: vertical distance of the shadow from the shape
  + example: simple shadow
    + a function that will set the 4 context properties for shadows: `function setShadow() {...}`
      + all drawings casting this shadows
      + define the 4 properties for better clarity: `ctx.shadowColor = "Grey"; ctx.shadowBlur = 20; ctx.shadowOffsetX = 15; ctx.shadowOffsetY = 15;`
    + green filled rectangle w/ shadow: `ctx.fillStyle = "#22FFDD"; ctx.fillRect(20, 20, 200, 100);`
    + stroked rectangle w/ shadow: `ctx.strokeStyle = "purple";  ctx.lineWidth=10; ctx.strokeRect(20, 150, 200, 100);`
  + example: unwanted shadow
    + add the path a full circle: `ctx.arc(centerX, centerY, radius, 0, 2*Math.PI, false);`
    + w/ path drawing to change the context properties until a call to `stroke()` or `fill()` performed: `ctx.fillStyle = "lightBlue";`
    + add shadows before drawing the filled circle: `addShadows() {...}`
      + set color: `ctx.shadowColor = "Grey"; // color`
      + set shadow blur level: `ctx.shadowBlur = 20;      // blur level`
      + set shadow horizontal level: `ctx.shadowOffsetX = 15;   // horizontal offset`
      + set shadow vertical offset: `ctx.shadowOffsetY = 15;   // vertical offset`
    + draw the filled circle in light blue: `ctx.fill();`
    + set outline properties: `ctx.lineWidth = 5; ctx.strokeStyle = "black";`
    + draw wireframe along the path: `ctx.stroke()`
    + `ctx.fill()` and `ctx.stroke()` casts a shadow along the whole path $\to$ unwanted shadow inside the circle produced by `ctx.stroke()`
    + solution to remove unwanted shadow
      + save the context before setting the shadow properties
      + draw the filled circle
      + restore the context (to its previous state: without shadows)
      + draw the outlined circle by calling `ctx.stroke()`

+ [Styling lines](#357-styling-lines)
  + [line thickness](#line-style-change-the-line-thickness)
    + changing the value (in pixels) of the `lineWidth` property of the context
    + set the thickness of every shape drawn in stroke/wireframe mode to `x` pixels: `ctx.lineWidth = x;`
  + [line end cap style](#line-style-changing-the-end-caps-for-a-line)
    + `lineCap` property: the way line end caps rendered
    + Possible values: `butt` (default), `round`, `square`
  + [line corner type](#line-style-setting-the-type-of-corner-when-two-lines-meet)
    + `lineJoin` property: the way corners rendered, when two lines meet
    + Possible values: `miter` (the default) for creating sharp corners, `round`, or `bevel` for "cut corners"
    + `miterLimit` property:
      + the maximum `miter` length, a threshold value
      + the distance between the inner corner and the outer corner where two lines meet
      + the angle of a corner between two lines gets smaller, the miter length grows and become too long
      + exceed the miterLimit value $\to$ the corner rendered as if `lineJoin = "bevel"` and the corner "cut"



### 3.5.1 Canvas context: colors

In previous examples, we saw how to set the current color using the `strokeStyle` and `fillStyle` properties of the canvas context object.

Let's look at color in a little more detail, and see how we can use gradients or patterns/textures/images (in other words: fill shapes or fill the outline of the shapes with some images that repeat themselves).


#### Colors and transparency

You can use [the same syntax for colors that is supported by CSS3](https://www.w3.org/TR/css3-color/). The next lines show possible values/syntaxes.

<div><ol>
<li value="1">ctx.strokeStyle = 'red';</li>
<li>ctx.fillStyle = "#00ff00";</li>
<li>ctx.strokeStyle = "rgb(0, 0, 255)";</li>
<li>ctx.fillStyle = "rgba(0, 0, 255, 0.5)";</li>
</ol></div>

Note that:

+ All values are strings;
+ Line 4 defines a "transparent color", the "a" of "rgba" means "alpha channel". Its value is between 0 and 1, where 0 means "completely transparent" and 1 means "opaque".

Here is an example that shows how to draw different filled rectangles in blue, with different levels of transparency. 

Try [it online](https://jsbin.com/famoxoteju/1/edit?html,output): ([Local Example - Transparency](src/3.5.1-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yxtz9qk2')"
    src    ="https://tinyurl.com/y4te8ph7"
    alt    ="transparent rgba color example"
    title  ="transparent rgba color example"
  />
</figure>


#### Knowledge check 3.5.1

1. Do the color values that can be used to set the `fillStyle` or `strokeStyle` follow the CSS3 syntax? (Yes/No)

  Ans: Yes<br/>
  Explanation: The syntax of the colors follows the CSS3 syntax.


### 3.5.2 Canvas context: linear gradients

It is possible to define the stroke or the fill style as a "gradient", a set of interpolated colors, like in this example below (try [it online](https://jsbin.com/lokawoduyu/edit?html,output)): ([Local Example - Gradient](src/3.5.2-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/yxqj36pp"
    alt    ="linear gradient from blue to white to red"
    title  ="linear gradient from blue to white to red"
  />
</figure>


The concept of linear gradient is seen as an "invisible" rectangle in which a set of colors are interpolated along a line.

The gradient becomes visible when we draw shapes on top of the invisible gradient, and when the `fillStyle` or `strokeStyle` property has for value this gradient.


#### How to create gradients

There are 3 steps:

__Step #1: define a linear gradient__

Syntax: 

<div><ol>
<li value="1">ctx.createLinearGradient(x0,y0,x1,y1); </li>
</ol></div>

... where the `(x0, y0)` and `(x1, y1)` parameters define "the direction of the gradient" (as a vector with a starting and an ending point). This direction is an invisible line along which the colors that compose the gradient will be interpolated.

Let's see an example:

<div><ol>
<li value="1"> grdFrenchFlag = ctx.createLinearGradient(0, 0, 300, 0);</li>
</ol></div>

This line defines the direction of the gradient: a virtual, invisible line that goes from the top left corner of the canvas (0, 0) to the top right corner of the canvas (300, 0). The interpolated colors will propagate along this line. 

If this gradient is going to be reused by different functions, it is good practice to create/initialize it in a function called when the page is loaded and to store it in a global variable.


__Step #2: add a number of "color stops" to this gradient__

We will add a set of "colors" and "stops" to this gradient. The stops go from 0 (beginning of the virtual line defined just above), to 1 (end of the virtual line). A color associated with a value of 0.5 will be right in the middle of the virtual line.

Here is an example that corresponds to an interpolated version of the French flag, going from blue to white, then to red, with proportional intervals. We define three colors, blue at position 0, white at position 0.5 and red at position 1:

<div><ol>
<li value="1"> grdFrenchFlag.addColorStop(0, "blue"); </li>
<li> grdFrenchFlag.addColorStop(0.5, "white");</li>
<li> grdFrenchFlag.addColorStop(1, "red"); </li>
</ol></div>


__Step 3: draw some shapes__

First, let's set the `fillStyle` or `strokeStyle` of the context with this gradient, then let's draw some shapes "on top of the gradient".

In our example, the gradient corresponds to an invisible rectangle that fills the canvas. If we draw a rectangle of the canvas size, it should be filled with the entire gradient:

<div><ol>
<li value="1"> ctx.fillStyle = grdFrenchFlag;</li>
<li> ctx.fillRect(0, 0, 300, 200);</li>
</ol></div>

The result is shown below: a big rectangle that fills the whole canvas, with colors going from blue (left) to white (middle) to red (right).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/yxqj36pp"
    alt    ="linear gradient from blue to white to red, left to right"
    title  ="linear gradient from blue to white to red, left to right"
  />
</figure>


#### Changing the direction of the gradient

If you modify the source code that defines the direction of the gradient as follows...

<div><ol>
<li value="1">grdFrenchFlag = ctx.createLinearGradient(0, 0, 300, 200);</li>
</ol></div>

... then you will define a gradient that goes from the top left corner of the canvas to the bottom right of the canvas. Let's see what it does (see [online version](https://jsbin.com/gisinezini/edit?html,js,output)): ([Local Example - Gradient Direction](src/3.5.2-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/y5qlq7c7"
    alt    ="diagonal gradient from top left to bottom right"
    title  ="diagonal gradient from top left to bottom right"
  />
</figure>



#### Drawing shapes that do not cover the whole gradient

Instead of drawing a filled rectangle that covers the whole surface of the canvas, let's draw several smaller rectangles.

[Online example](https://jsbin.com/xobexawitu/1/edit?html,output): ([Local Example - Small Gradients](src/3.5.2-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/y686fck5"
    alt    ="smaller rectangle on top of a gradient"
    title  ="smaller rectangle on top of a gradient"
  />
</figure>


Note that the canvas has its default background color where we did not draw anything. And where we have drawn rectangles, we can see "through" and the colors from the gradient are visible.

Here is the code that draws the checkboard:

<div><ol>
<li value="1"> ctx.fillStyle = grdFrenchFlag;</li>
<li> ctx.fillRect(0, 0, 50, 50);</li>
<li> ctx.fillRect(100, 0, 50, 50);</li>
<li> ctx.fillRect(200, 0, 50, 50);</li>
<li> ctx.fillRect(50, 50, 50, 50);</li>
<li> ctx.fillRect(150, 50, 50, 50);</li>
<li> ctx.fillRect(250, 50, 50, 50);</li>
<li> ctx.fillRect(0, 100, 50, 50);</li>
<li> ctx.fillRect(100, 100, 50, 50);</li>
<li> ctx.fillRect(200, 100, 50, 50);</li>
<li> ctx.fillRect(50, 150, 50, 50);</li>
<li> ctx.fillRect(150, 150, 50, 50);</li>
<li> ctx.fillRect(250, 150, 50, 50);</li>
</ol></div>

This code is rather ugly isn't it? It would have been better  to use a loop...

Here is function that draws a chessboard ([online example at JsBin](https://jsbin.com/netijalofu/1/edit?html,output)): ([Loca Example - Chessboard](src/3.5.2-example4.html))

<div><ol>
<li value="1">// n = number of cells per row/column</li>
<li>function drawCheckboard(n) {</li>
<li>&nbsp; &nbsp; ctx.fillStyle = grdFrenchFlag;</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;var l = canvas.width;</li>
<li>&nbsp; &nbsp;&nbsp;var h = canvas.height;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;var cellWidth = l / n;</li>
<li>&nbsp; &nbsp;&nbsp;var cellHeight = h / n;</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;for(i = 0; i &lt; n; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;for(j =&nbsp;i % 2; j &lt; n; j++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx.fillRect(cellWidth*i, cellHeight*j, cellWidth, cellHeight); </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
</ol></div>

The two loops (_lines 11-15_) draw only one cell out of two (see the `j = i % 2` at _line 12_). i is the column number and if the column is odd or even, either we draw or we do not draw a rectangle.

This code is much more complex than the previous one, taking 16 lines instead of 13, but is much more powerful. Try to call the function with a value of 10, 20, or 2... 


#### Drawing outlined shapes with gradients

Just as we used `fillStyle` and `fillRect` for drawing rectangles filled with a gradient, we can also use strokeStyle and strokeRect in order to draw wireframed rectangles. In the next example, which is just a variation of the previous one, we have used the `lineWidth` property to set the outline of the rectangles at 5 pixels: [try this example at JsBin](https://jsbin.com/daqicarawu/1/edit?html,output). ([Local Example - Outlined Shapes w/ Gradients](src/3.5.2-example5.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/yyppze3z"
    alt    ="stroke rectangles with gradient"
    title  ="stroke rectangles with gradient"
  />
</figure>


Extract from source code:

<div><ol>
<li value="1">function drawCheckboard(n) {</li>
<li>&nbsp; &nbsp; <strong>ctx</strong><strong>.strokeStyle = grdFrenchFlag;</strong></li>
<li><strong>&nbsp; &nbsp; ctx.lineWidth=10;</strong></li>
<li>&nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp;&nbsp;for(i = 0; i &lt; n; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;for(j =&nbsp;<span style="color: #006666;" color="#006666">i % 2</span>; j &lt; n; j++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx.<strong>stroke</strong>Rect(cellWidth*i, cellHeight*j, cellWidth, cellHeight); </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;} </li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
</ol></div>


#### What happens if we define a gradient smaller than the canvas?

Let's go back to the very first example on this page - the one with the blue-white-red interpolated French flag. This time we will define a smaller gradient. Instead of going from (0, 0) to (300, 0), it will go from (100, 0) to (200, 0), while the canvas remains the same (width=300, height=200).

<div><ol>
<li value="1"> grdFrenchFlag = ctx.createLinearGradient(<strong>100, 0, 200, 0</strong>);</li>
</ol></div>

Like in the first example we will draw a filled rectangle that is the same size as the canvas. Here is the online version, and here is a screenshot of the result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/y59huxjo"
    alt    ="gradient smaller thant the drawn shape"
    title  ="gradient smaller thant the drawn shape"
  />
</figure>


We notice that "before" the gradient starts, the first color of the gradient is repeated without any interpolation (columns 0-100 are all blue), then we "see through" and the gradient is drawn (columns 100-200), then the last color of the gradient is repeated without any interpolation (columns 200-300 are red).


#### What happens if we define a gradient bigger than the canvas?

Nothing special; we will "see through the drawn shapes", and the parts of the gradient that are located in the canvas area will be shown. You can try this example that defines a gradient twice the size of the canvas: 

<div><ol>
<li value="1">grdFrenchFlag = ctx.createLinearGradient(0, 0, <strong>600, 400</strong>);</li>
</ol></div>

And if we draw the same rectangle with the canvas size, here is the result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/y2dzfdya"
    alt    ="gradient bigger than the canvas size"
    title  ="gradient bigger than the canvas size"
  />
</figure>


The red color is beyond the bottom right corner.... we see only the top left quarter of the gradient.


#### Draw shapes that share the same gradient as a whole

This time, we would like to draw the chessboard with the gradient in each cell. How can we do this with one single gradient?

We can't! At least we can't without recreating it for each cell!

It suffices to create a new gradient before drawing each filled rectangle, and set it with the starting and ending point of its direction/virtual line accordingly to the rectangle coordinates. Here is an [online example](https://jsbin.com/wuganabuno/edit?html,output) and the resulting display: ([Local Example - Same Small Gradients](src/3.5.2-example6.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/y5h3ms3q"
    alt    ="chessboard with individual gradient for each cell"
    title  ="chessboard with individual gradient for each cell"
  />
</figure>


Extract from source code:

<div><ol>
<li value="1">function setGradient(x, y, width, height) {</li>
<li>&nbsp; &nbsp; grdFrenchFlag = ctx.createLinearGradient(x, y, width, height);</li>
<li> </li>
<li>&nbsp; &nbsp; grdFrenchFlag.addColorStop(0, "blue"); </li>
<li>&nbsp; &nbsp; grdFrenchFlag.addColorStop(0.5, "white");</li>
<li>&nbsp; &nbsp; grdFrenchFlag.addColorStop(1, "red"); </li>
<li>&nbsp; &nbsp; // set the new gradient to the current fillStyle</li>
<li>&nbsp; &nbsp; ctx.fillStyle = grdFrenchFlag;</li>
<li>}</li>
<li>&nbsp;</li>
<li>// n = number of cells per row/column</li>
<li>function drawCheckboard(n) {</li>
<li> </li>
<li>&nbsp; &nbsp;var l = canvas.width;</li>
<li>&nbsp; &nbsp;var h = canvas.height;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;var cellWidth = l / n;</li>
<li>&nbsp; &nbsp;var cellHeight = h / n;</li>
<li> </li>
<li>&nbsp; &nbsp;for(i = 0; i &lt; n; i+=2) {</li>
<li>&nbsp; &nbsp; &nbsp;for(j = 0; j &lt; n; j++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; var x = cellWidth*(i+j%2);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; var y = cellHeight*j;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>setGradient</strong><strong>(x, y, x+cellWidth, y+cellHeight);</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.fillRect(x, y, cellWidth, cellHeight); </li>
<li>&nbsp; &nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp;}</li>
<li>}</li>
</ol></div>

We wrote a function `setGradient(startX, startY, endX, endY)` that creates a gradient and set the `fillStyle` context property so that any filled shape drawn will have this gradient.

In the `drawCheckBoard(...)` function we call it just before drawing rectangles. In this way, each rectangle is drawn using its own gradient.


#### This flag does not really look like the French flag, does it?

Indeed the French flag in these images is more accurate:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/y3gzc8uh"
    alt    ="french flag with linear gradient"
    title  ="french flag with linear gradient"
  />
</figure>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y3ug336b')"
    src    ="https://tinyurl.com/y5kqnegw"
    alt    ="french flag with linear gradient"
    title  ="french flag with linear gradient"
  />
</figure>

We slightly modified the examples of this chapter so that the flag looks more like the French flag. Look at the modified versions below, and try to find out what has changed in the gradient definitions:

+ [Version 1](https://jsbin.com/mapeweyoze/1/edit?html,output)
+ [Version 2](https://jsbin.com/mapeweyoze/1/edit?html,output)
+ [Version 3](https://jsbin.com/mapeweyoze/1/edit?html,output)
+ [Version 4](https://jsbin.com/mapeweyoze/1/edit?html,output)
+ [Version 5](https://jsbin.com/mapeweyoze/1/edit?html,output)
+ [Version 6](https://jsbin.com/mapeweyoze/1/edit?html,output)



#### Knowledge check 3.5.2

<pre>grdFrenchFlag = ctx.createLinearGradient(0, 0, 300, 0);
grdFrenchFlag.addColorStop(0, "blue");
grdFrenchFlag.addColorStop(0.5, "white");
grdFrenchFlag.addColorStop(1, "red");
</pre>

1. The gradient above defines...<br/>

  a. A gradient that goes from (0, 0) to (300, 0), defining an invisible line. Colors will be interpolated horizontally along this line. Shapes drawn in the canvas between X=0 and X=300 will be drawn using interpolated colors defined by this gradient.<br/>
  b. Same as above but colors will be interpolated diagonally.<br/>
  
  Ans: a<br/>
  Explanation: This line defines the direction of the gradient: a virtual, invisible line that goes from the top left corner of the canvas (0, 0) to the top right corner of the canvas (300, 0). The interpolated colors will propagate along this line. Shapes drawn in the canvas between X=0 and X=300 will be drawn using interpolated colors defined by this gradient. Shapes further than X=300 will be all red.


### 3.5.3 Canvas context: radial gradients

#### Basic principle / syntax: define two circles at gradient creation

Radial gradients are for creating gradients that propagate/interpolate colors along circles instead of propagating/interpolating along a virtual line, like linear gradients.

Here is an example of a radial gradient that interpolates the color of the rainbow (see the [online version](https://jsbin.com/hovulegacu/1/edit?html,output)): ([Local Example - Gradient Circle](src/3.5.3-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y4bf7lzs')"
    src    ="https://tinyurl.com/yxo2oayb"
    alt    ="radial gradient example: circles with the rainbow colors"
    title  ="radial gradient example: circles with the rainbow colors"
  />
</figure>

The gradient is defined as follows:

<div><ol>
<li value="1">var grd = context.<strong>createRadialGradient(150, 100, 30, 150, 100, 100);</strong></li>
<li> grd.addColorStop(0, "red");</li>
<li> grd.addColorStop(0.17, "orange");</li>
<li> grd.addColorStop(0.33, "yellow");</li>
<li> grd.addColorStop(0.5, "green");</li>
<li> grd.addColorStop(0.666, "blue");</li>
<li> grd.addColorStop(1, "violet");</li>
<li> </li>
<li> context.fillStyle = grd;</li>
</ol></div>

The method from the context object `createRadialGradient(cx1, cy1, radius1, cx2, cy2, radius2)` takes as the first three parameters the "starting" circle of the gradient, and as the three last parameters, the "ending circle".

In the above example, the gradients starts at a circle located at (150, 100), with a radius of 30, and propagates to a circle with the same center as the first (150, 100), but with a bigger radius of 100, as shown below:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y4bf7lzs')"
    src    ="https://tinyurl.com/y5a24a63"
    alt    ="radial gradient"
    title  ="radial gradient"
  />
</figure>


We added color stops using a method similar to that used for linear gradients.


#### What happens if the circles are not located at the same place?

You get some nice effects; here we set the second circle's center 60 pixels to the right of the first circle's center (cx = 210 instead of 150). [Online example](https://jsbin.com/masofafoti/edit?html,output): ([Local Example - Circles w/ different centers](src/3.5.3-example2.html))

grd = ctx.createRadialGradient(150, 100, 30, 210, 100, 100);

And here is the result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y4bf7lzs')"
    src    ="https://tinyurl.com/y427ngpr"
    alt    ="radial gradient with circles non aligned"
    title  ="radial gradient with circles non aligned"
  />
</figure>


#### What happens if the gradient is smaller or larger than the shapes we draw?

A gradient is an invisible shape on the screen: the radial gradient is made of two circles: an inner and an outer circle. Between these two circles, colors are interpolated.

We call the "first color" the color defined for the inner circle, the "last color" the last color of the gradient, that corresponds to the outer circle:

+ The color inside the first circle will be the first color. In our example above, the first color is red: and the small circle of the gradient in our example is filled in red!
+ The color outside the outer circle will be the last color of the gradient - which is not interpolated. The last color in our example is purple, and it fills the rest of the filled rectangle area "after" the external circle of the gradient.
+ The colors between the two circles will be interpolated.


### 3.5.4 Canvas context: patterns/textures

#### Principle

The principle of "pattern" drawing is based on repeating an image (if the image is smaller than the surface of the shape you are going to draw) for filling the surface of objects to be drawn (either filled or stroked).

To illustrate this principle, in the next examples, we are going to draw rectangles using this pattern: 

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yymdr2v8')"
    src    ="https://tinyurl.com/y37v3nkh"
    alt    ="an example of repeateable pattern"
    title  ="an example of repeateable pattern"
  />
</figure>


There are a few steps we have to take before doing this:

1. __Create a JavaScript image object__

  <div><ol style="list-style-type: decimal;">
  <li value="1">var&nbsp;imageObj&nbsp;=&nbsp;new Image();</li>
  </ol></div>

2. __Define a callback function that will be called once the image has been fully loaded__ in memory; we cannot draw before the image has been loaded.

  <div><ol style="list-style-type: decimal;">
  <li value="1">imageObj.onload = function(){</li>
  <li> ...</li>
  <li>}</li>
  </ol></div>

3. __Set the source of this image to the URL of the pattern__ (in our example with [url of the pattern](https://tinyurl.com/y6snxuju)),

  <div><ol style="list-style-type: decimal;">
  <li value="1">imageObj.src = "https://www.myserver.com/myRepeatablePattern.png"; </li>
  </ol></div>

4. As soon as step 3 is executed, an HTTP request is sent in background by the browser, and when the image is loaded in memory, the callback defined at step 2 is called. We create a pattern object inside, from the loaded image:

  <div><ol style="list-style-type: decimal;">
  <li value="1"> // callback called asynchronously, after the src attribute of imageObj is set</li>
  <li> imageObj.onload = function(){&nbsp;</li>
  <li>&nbsp; &nbsp; // We enter here when the image is loaded, we create a pattern object.</li>
  <li>&nbsp; &nbsp; // It is good practice to set this as a global variable, easier to share</li>
  <li>&nbsp; &nbsp; <strong>pattern1 </strong><strong>= ctx.createPattern(imageObj, "repeat");</strong></li>
  <li>};</li>
  </ol></div>

5. __Inside the callback function (or inside a function called from inside the callback) we can draw.__

  <div><ol style="list-style-type: decimal;">
  <li value="1"> // callback called asynchronously, after the src attribute of imageObj is set</li>
  <li> imageObj.onload = function(){</li>
  <li>&nbsp; &nbsp; pattern1 = ctx.createPattern(imageObj, "repeat");</li>
  <li> </li>
  <li><strong>&nbsp; &nbsp;&nbsp;// Draw a textured rectangle</strong></li>
  <li><strong>&nbsp; &nbsp; ctx.fillStyle = pattern1;</strong></li>
  <li><strong>&nbsp; &nbsp; ctx.fillRect(10, 10, 500, 800);</strong></li>
  <li>};</li>
  </ol></div>


#### Examples

__Example #1: draw two rectangles with a pattern (one filled, one stroked)__

[Online example](https://jsbin.com/qicamatoqa/1/edit?html,output): ([Local Example - Filled & Stroked Patterns](src/3.5.4-example1.html))

Here we have two rectangles drawn using a pattern (an image that can be repeated along the X and Y axis). The first is a filled rectangle while the second is "stroked" with a lineWidth of 10 pixels.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yymdr2v8')"
    src    ="https://tinyurl.com/y37v3nkh"
    alt    ="example of painting with patterns"
    title  ="example of painting with patterns"
  />
</figure>


HTML source code:

<div><ol style="list-style-type: decimal;">
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</li>
<li>&lt;body onload="init();"&gt;</li>
<li>&nbsp; &nbsp;&lt;canvas id="myCanvas" width="500" height="400"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;Your browser does not support the canvas tag. &lt;/canvas&gt;</li>
<li>&nbsp; &nbsp;&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

JavaScript source code:

<div><ol style="list-style-type: decimal;">
<li value="1">var canvas, ctx, pattern1;</li>
<li>&nbsp;</li>
<li>function init() {</li>
<li>&nbsp; &nbsp;canvas = document.querySelector('#myCanvas');</li>
<li>&nbsp; &nbsp;ctx = canvas.getContext('2d');</li>
<li> </li>
<li>&nbsp; &nbsp;// We need 1) to create an empty image object, 2) to set a callback function</li>
<li>&nbsp; &nbsp;// that will be called when the image is fully loaded, 3) to create a </li>
<li>&nbsp; &nbsp;// pattern object, 4) to set the fillStyle or the strokeStyle property of </li>
<li>&nbsp; &nbsp;// the context with this pattern, 5) to draw something</li>
<li>&nbsp; &nbsp;<strong>// WE CANNOT DRAW UNTIL THE IMAGE IS FULLY LOADED -&gt; draw from inside the</strong></li>
<li><strong>&nbsp; &nbsp;// onload callback only !</strong></li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp;// 1 - Allocate an image</li>
<li>&nbsp; &nbsp;var imageObj = new Image();</li>
<li>&nbsp;</li>
<li><span style="color: #000000;" color="#000000">&nbsp; &nbsp;</span>// 2 - callback called asynchronously, after the src attribute of imageObj </li>
<li>&nbsp; &nbsp;// is set</li>
<li>&nbsp; &nbsp;imageObj.onload = function(){</li>
<li>&nbsp; &nbsp; &nbsp; // We enter here only when the image has been loaded by the browser</li>
<li>&nbsp; &nbsp; &nbsp; // 4 - Pattern creation using the image object</li>
<li>&nbsp; &nbsp; &nbsp; // Instead of "repeat", try different values : repeat-x, repeat-y, </li>
<li>&nbsp; &nbsp; &nbsp; // or no-repeat, You may draw larger shapes in order to see </li>
<li>&nbsp; &nbsp; &nbsp; // different results</li>
<li>&nbsp; &nbsp; &nbsp; // It is good practice to leave this as a global variable if it</li>
<li>&nbsp; &nbsp; &nbsp; // will be reused by other functions</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; pattern1 = ctx.createPattern(imageObj, "repeat");</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; // 5 - Draw things. Here a textured rectangle</li>
<li>&nbsp; &nbsp; &nbsp; ctx.fillStyle = pattern1;</li>
<li>&nbsp; &nbsp; &nbsp; ctx.fillRect(10, 10, 200, 200);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; // ... And a wireframe one</li>
<li>&nbsp; &nbsp; &nbsp; ctx.lineWidth=20;</li>
<li>&nbsp; &nbsp; &nbsp; ctx.strokeStyle=pattern1;</li>
<li>&nbsp; &nbsp; &nbsp; ctx.strokeRect(230, 20, 150, 100);</li>
<li>&nbsp; };</li>
<li> </li>
<li>&nbsp; // 3 - Send the request to load the image</li>
<li>&nbsp; // Setting the src attribute&nbsp;will tell the browser to send an asynchronous </li>
<li>&nbsp; // request.</li>
<li>&nbsp; // When the browser gets an answer, the callback above will be called</li>
<li>&nbsp; imageObj.src = "https://www.dreamstime.com/colourful-flowers-repeatable-pattern-thumb18692760.jpg"; </li>
<li>}</li>
</ol></div><br/>


__Example 2: the repeatability of a pattern__

To "better" see the repeatability of the pattern, here is the same example with a 1000x1000 pixel wide canvas.

Online version [here](https://jsbin.com/hexomamiyi/1/edit?html,output) and here is the result: ([Local Example - Repeated Pattern](src/3.5.4-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yymdr2v8')"
    src    ="https://tinyurl.com/y49sxv9n"
    alt    ="same example with bigger canvas and bigger rectangles"
    title  ="same example with bigger canvas and bigger rectangles"
  />
</figure>


You can change the way the pattern is repeated by modifying the second parameter of this method:

<div><ol>
<li value="1">pattern1 = ctx.createPattern(imageObj, "<strong>repeat</strong>");</li>
</ol></div>

Please try: `repeat-x`, `repeat-y` or `no-repeat` as acceptable values. Just change this line in the online example and you will see live results.


#### Knowledge check 3.5.4

1. Patterns are images that can be used to "fill" shapes, eventually repeating themselves?<br/>

  a. Yes, but only with filled shapes; patterns cannot be used with the `strokeStyle` property of the context.<br/>
  b. Yes<br/>
  c. No<br/>

  Ans: b<BR/>
  Explanation: Patterns can be used with all kinds of shapes, and with both `strokeStyle` and `fillStyle`



### 3.5.5 A multiple image loader

#### Draw with multiple patterns? We need to load all of them before drawing!

Below are 4 rectangles drawn with 4 different patterns.


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y6yxw84l')"
    src    ="https://tinyurl.com/y3c8cz7c"
    alt    ="4 rectangles drawn with different patterns"
    title  ="4 rectangles drawn with different patterns"
  />
</figure>

We said earlier that we cannot draw before the image used by a pattern is loaded. This can become rapidly complicated if we need to draw using multiple patterns. We need a way to load all images and then, _only when all images have been loaded, start drawing_.

JavaScript is an asynchronous language. When you set the src attribute of an image, then an asynchronous request is sent by the browser, and then after a while, the onload callback is called... The difficult part to understand for those who are not familiar with JavaScript is that these requests are done in parallel and we do not know when, and in what order, the images will be loaded.

__The solution is to use a multiple image loader that counts the loaded images and calls a function you pass when done!__

The trick is to have an array of URLs that will be used by our multiple image loader, then in the onload callback, this will be called once per image loaded, so we can count the number of images effectively loaded.

When all images have been loaded, we call a callback function that has been passed to our loader.

A complete example code that produces the result shown at the beginning of this page is at [available online](https://jsbin.com/suxiwif/edit?html,output) at JsBin. ([Local Example - Multiple Image Pattern](src/3.5.5-example1.html))


#### Define the list of images to be loaded

<div><ol>
<li value="1"> // List of images to load, we used a JavaScript object instead of </li>
<li> // an array, so that named indexes (aka properties)</li>
<li> // can be used -&gt; easier to manipulate</li>
<li> var imagesToLoad = {</li>
<li>&nbsp; &nbsp; &nbsp;flowers: 'https://i.ibb.co/4NN9Sgn/flowers.jpg',</li>
<li>&nbsp; &nbsp; &nbsp;lion: 'https://i.ibb.co/3NyqKnY/lion.jpg',</li>
<li>&nbsp; &nbsp; &nbsp;blackAndWhiteLys: 'https://i.ibb.co/VNLVpcL/final.jpg',</li>
<li>&nbsp; &nbsp; &nbsp;tiledFloor: </li>
<li>&nbsp; &nbsp; &nbsp; 'https://i.ibb.co/Dt6txmG/repeatable-Pattern.jpg'</li>
<li> };</li>
</ol></div>

Notice that instead of using a traditional array, we defined this list as a JavaScript object, with properties whose names will be easier to manipulate (flowers, lion, tiledFloor, etc.).


#### The image loader function

<div><ol>
<li value="1"> function loadImages(imagesToBeLoaded, drawCallback) {</li>
<li>&nbsp; &nbsp; &nbsp;var imagesLoaded = {};</li>
<li>&nbsp; &nbsp; &nbsp;var loadedImages = 0;</li>
<li>&nbsp; &nbsp; &nbsp;var numberOfImagesToLoad = 0;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// get num of&nbsp;images to load</li>
<li>&nbsp; &nbsp; &nbsp;for(var name in imagesToBeLoaded) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;numberOfImagesToLoad++;</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;for(var name in imagesToBeLoaded) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;imagesLoaded[name] = new Image();</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;imagesLoaded[name].onload = function() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(++loadedImages &gt;= numberOfImagesToLoad) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;drawCallback(imagesLoaded);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;} // if</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}; // function</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;imagesLoaded[name].src = imagesToBeLoaded[name];</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} // for</li>
<li>} // function</li>
</ol></div>

__Explanations:__

+ This function takes as a parameter the list of images to be loaded, and a drawCallback function that will be called only once all images have been loaded. This callback takes as a parameter a new object that is the list of images that have been loaded (see line 16).
+ We first count the number of images to load (lines 7-9), then for each image to be loaded we create a new JavaScript image object (line 12) and set its src attribute (line 19) - this will start to load the image.
+ When an image comes in, the onload callback is called (line 14) and inside, we increment the number of images loaded (line 15) and test if this number is >=  the total number of images that should be loaded. If this is the case, the callback function is called (line 16).


#### Example of use of this loader

<div><ol>
<li value="1"> loadImages(imagesToLoad, function(imagesLoaded) {</li>
<li>&nbsp; &nbsp; patternFlowers = ctx.createPattern(imagesLoaded.flowers, 'repeat');</li>
<li>&nbsp; &nbsp; patternLion &nbsp; &nbsp;= ctx.createPattern(imagesLoaded.lion, 'repeat');</li>
<li>&nbsp; &nbsp; patternBW = ctx.createPattern(imagesLoaded.blackAndWhiteLys, 'repeat');</li>
<li>&nbsp; &nbsp; patternFloor &nbsp;&nbsp;= ctx.createPattern(imagesLoaded.tiledFloor, 'repeat');</li>
<li> </li>
<li>&nbsp; &nbsp; drawRectanglesWithPatterns(); </li>
<li> }); </li>
</ol></div>


__Explanations:__

+ Line 1 is the call to the image loader, the first parameter is the list of images to be loaded, while the second parameter is the callback function that will be called once all images have been loaded.
+ Lines 2-5: in this callback we create patterns from the loaded images (note the use of the property names imagesLoaded.flowers, etc. that makes the code easier to read).
+ Line 7: then we call a function that will draw the rectangles.

Here is the function:

<div><ol>
<li value="1">function drawRectanglesWithPatterns() { </li>
<li>&nbsp; &nbsp; ctx.fillStyle=patternFloor;</li>
<li>&nbsp; &nbsp; ctx.fillRect(0,0,200,200);</li>
<li> </li>
<li>&nbsp; &nbsp; ctx.fillStyle=patternLion;</li>
<li>&nbsp; &nbsp; ctx.fillRect(200,0,200,200);</li>
<li> </li>
<li>&nbsp; &nbsp; ctx.fillStyle=patternFlowers;</li>
<li>&nbsp; &nbsp; ctx.fillRect(0,200,200,200);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; ctx.fillStyle=patternBW;</li>
<li>&nbsp; &nbsp; ctx.fillRect(200,200,200,200);</li>
<li> }</li>
</ol></div>


### 3.5.6 Drawing shadows

#### Context properties to draw with shadows

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y299m8e8')"
    src    ="https://tinyurl.com/y2j8qrd9"
    alt    ="a green shadowed rectangle"
    title  ="a green shadowed rectangle"
  />
</figure>


There are 4 properties of the canvas context that are useful for indicating that we want to draw shapes with shadows:

+ `shadowColor`: color to use for shadows,
+ `shadowBlur`: blur level for shadows,
+ `shadowOffsetX`: horizontal distance of the shadow from the shape,
+ `shadowOffsetY`: vertical distance of the shadow from the shape


#### Examples

__Example #1: simple shadow__

[Online example](https://jsbin.com/kimohoyore/edit?html,output) gives this result: ([Local Example - Simple Shadow](src/3.5.6-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y299m8e8')"
    src    ="https://tinyurl.com/y3784b7x"
    alt    ="two shadowed rectangles"
    title  ="two shadowed rectangles"
  />
</figure>


HTML source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</li>
<li>&lt;body onload = init();&gt;</li>
<li>&nbsp; &nbsp; &lt;canvas id="myCanvas" width="400" height =800&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; Your browser does not support the canvas tag.</li>
<li>&lt;/canvas&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

JavaScript source code:

<div><ol>
<li value="1">var canvas, ctx;</li>
<li> </li>
<li>function init() {</li>
<li>&nbsp; &nbsp; canvas = document.getElementById('myCanvas');</li>
<li>&nbsp; &nbsp; ctx = canvas.getContext('2d');</li>
<li> </li>
<li>&nbsp; &nbsp; // call to a function that will set the 4 context properties for shadows</li>
<li>&nbsp; &nbsp; setShadow();</li>
<li>&nbsp; &nbsp; // all drawings that will occur will cast shadows</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// first green filled rectangle</li>
<li>&nbsp; &nbsp; ctx.fillStyle = "#22FFDD";&nbsp;</li>
<li>&nbsp; &nbsp; ctx.fillRect(20, 20, 200, 100); </li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// second stroked rectangle</li>
<li>&nbsp; &nbsp; ctx.strokeStyle = "purple";&nbsp;</li>
<li>&nbsp; &nbsp; ctx.lineWidth=10;</li>
<li>&nbsp; &nbsp; ctx.strokeRect(20, 150, 200, 100);</li>
<li>}</li>
<li>&nbsp;</li>
<li>// We define the 4 properties in a dedicated function, for clarity</li>
<li>function setShadow() {</li>
<li>&nbsp; &nbsp; ctx.shadowColor = "Grey";&nbsp; &nbsp;&nbsp;// color</li>
<li>&nbsp; &nbsp; ctx.shadowBlur = 20;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// blur level</li>
<li>&nbsp; &nbsp; ctx.shadowOffsetX = 15;&nbsp; &nbsp; &nbsp;&nbsp;// horizontal offset</li>
<li>&nbsp; &nbsp; ctx.shadowOffsetY = 15;&nbsp; &nbsp; &nbsp;&nbsp;// vertical offset</li>
<li>}</li>
</ol></div>


__Explanations:__

+ _Lines 21-27_: we set the 4 properties that define shadows in a dedicated function, for better clarity.
+ _Line 8_: we called this function once before drawing the rectangles.
+ _Lines 11-18_: we draw a filled and a stroked rectangle. Both rectangles cast shadows.


__Example #2: unwanted shadows!__

Let's take a [previous example](https://jsbin.com/juyevutoli/1/edit?html,output), the one that draws a filled circle with an outline: ([Local Example - Circle](src/3.5.6-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y299m8e8')"
    src    ="https://tinyurl.com/ybn6755f"
    alt    ="filled circle with outline"
    title  ="filled circle with outline"
  />
</figure>


Now, let's add a shadow to it (see the [example online](https://jsbin.com/kimafojixa/edit?html,output)): ([Local Example - Undesired Shadows](src/3.5.6-example3.html))

Here is an extract from the code:

<div><ol>
<li value="1">...</li>
<li> ctx.beginPath();</li>
<li> </li>
<li>// Add to the path a full circle (from 0 to 2PI)</li>
<li> ctx.arc(centerX, centerY, radius, 0, 2*Math.PI, false);</li>
<li> </li>
<li>// With path drawing you can change the context</li>
<li>// properties until a call to stroke() or fill() is performed</li>
<li> ctx.fillStyle = "lightBlue";</li>
<li> </li>
<li><strong>// add shadows before drawing the filled circle</strong></li>
<li><strong> addShadows();</strong></li>
<li> </li>
<li>// Draws the filled circle in light blue</li>
<li> ctx.fill();</li>
<li> </li>
<li>// Prepare for the outline</li>
<li> ctx.lineWidth = 5;</li>
<li> ctx.strokeStyle = "black";</li>
<li> </li>
<li>// draws the path AGAIN (the circle), this</li>
<li>// time in wireframe</li>
<li> ctx.stroke();</li>
<li> </li>
<li>// Notice we only once called context.arc()! And drew it twice </li>
<li>// with different styles</li>
<li>...</li>
<li>&nbsp;</li>
<li>function<strong> addShadows()</strong> {</li>
<li>&nbsp; &nbsp; ctx.shadowColor = "Grey"; // color</li>
<li>&nbsp; &nbsp; ctx.shadowBlur = 20;&nbsp; &nbsp; &nbsp;&nbsp;// blur level</li>
<li>&nbsp; &nbsp; ctx.shadowOffsetX = 15;&nbsp; &nbsp;// horizontal offset</li>
<li>&nbsp; &nbsp; ctx.shadowOffsetY = 15;&nbsp; &nbsp;// vertical offset</li>
<li> }</li>
</ol></div>


And here is the result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y299m8e8')"
    src    ="https://tinyurl.com/yxolb727"
    alt    ="unwanted shadow casted by the outline"
    title  ="unwanted shadow casted by the outline"
  />
</figure>


Ah, indeed, the call to `ctx.fill()` casts a shadow, but the call to `ctx.stroke()`, that paints the whole path again, casts a shadow too, and this time the outline produces an unwanted shadow... How can we avoid this effect, while using the same technique for drawing the path?

The trick is to save the context before setting the shadow properties, then draw the filled circle, then restore the context (to its previous state: without shadows), then draw the outlined circle by calling `ctx.stroke()`.

Correct version of the code (see [online](https://jsbin.com/patumofama/edit?html,output)): ([Local Example - Corrected Shadow](src/3.5.6-example4.html))

<div><ol>
<li value="1">... </li>
<li> <strong>// save the context before setting shadows and drawing the filled circle</strong></li>
<li>&nbsp;<strong>ctx</strong><strong>.save();</strong></li>
<li> </li>
<li> // With path drawing you can change the context</li>
<li> // properties until a call to stroke() or fill() is performed</li>
<li>&nbsp;ctx.fillStyle = "lightBlue";</li>
<li> </li>
<li> <strong>// add shadows before drawing the filled circle</strong></li>
<li>&nbsp;<strong>addShadows</strong><strong>();</strong></li>
<li> </li>
<li> // Draws the filled circle in light blue</li>
<li>&nbsp;ctx.fill();</li>
<li> </li>
<li> <strong>// restore the context to its previous saved state</strong></li>
<li>&nbsp;<strong>ctx</strong><strong>.restore();</strong></li>
<li>...</li>
</ol></div>

And here is the final result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y299m8e8')"
    src    ="https://tinyurl.com/y3g8mfqe"
    alt    ="unwanted shadow disappeared"
    title  ="unwanted shadow disappeared"
  />
</figure>


#### Knowledge check 3.5.6

1. Shadows are set using the `strokeStyle` or `fillStyle` property of the context? (Yes/No)

  Ans: <span style="color: magenta;">No</span>, xYes<br/>
  Explanation: No, shadows have four properties just for them: `shadowColor`, `shadowBlur`, `shadowOffsetX` and `shadowOffsetY`.



### 3.5.7 Styling lines

Several context properties can be used to set the thickness of the shape outlines, the way line end caps are drawn, etc.

They apply to all shapes that are drawn in path mode (lines, curves, arcs) and some also apply to rectangles.


#### Line style: change the line thickness

We have seen this before. This is done by changing the value (in pixels) of the lineWidth property of the context:

<div><ol>
<li value="1"><strong>ctx.lineWidth = 10;</strong> // set the thickness of every shape drawn in stroke/wireframe mode to 10 pixels</li>
</ol></div>

Here is a complete example where we draw with a lineWidth of 20 pixels. You can play with the [complete interactive example here](https://jsbin.com/bixugayaba/edit?html,output): ([Local Example - Thickness](src/3.5.7-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyo8vyv8')"
    src    ="https://tinyurl.com/y6n2l3op"
    alt    ="line width changed"
    title  ="line width changed"
  />
</figure>


Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp;&nbsp;&nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp;&nbsp;&nbsp; &lt;title&gt;A simple example of lineWidth property use&lt;/title&gt;</li>
<li> </li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp;&nbsp;&nbsp; &lt;canvas id="myCanvas" width="500"&gt;Your browser does not support the canvas tag.&lt;/canvas&gt;</li>
<li>&nbsp;&nbsp;&nbsp; &lt;script&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var canvas = document.getElementById('myCanvas');</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; var ctx = canvas.getContext('2d');</li>
<li>&nbsp;</li>
<li> // first path</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.moveTo(20, 20);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.lineTo(100, 100);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.lineTo(100, 0);</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li> // second part of the path</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.moveTo(120, 20);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctx.lineTo(200, 100);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.lineTo(200, 0);</li>
<li>&nbsp;</li>
<li> // indicate stroke color + draw first part of the path</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.strokeStyle = "#0000FF";</li>
<li> // Current line thickness is 20 pixels </li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.lineWidth = 20;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.stroke();</li>
<li>&nbsp;</li>
<li> // Draws a rectangle</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ctx.strokeRect(230, 10, 100, 100);</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;/script&gt;</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;&nbsp; &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


#### Line style: changing the end caps for a line

The `lineCap` property of the context indicates the way line end caps are rendered. Possible values are `butt` (default), `round`, `square` (from top to bottom in the next illustration). Note that a value of "round" or "square" makes the lines slightly longer than the default value "butt".

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 5vw;"
    onclick="window.open('https://tinyurl.com/yyo8vyv8')"
    src    ="https://tinyurl.com/y4v4jaco"
    alt    ="line cap values"
    title  ="line cap values"
  />
</figure>


Try the [next example interactively](https://jsbin.com/reqavetipu/1/edit?html,output): ([Local Example - Line End Cap](src/3.5.7-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yyo8vyv8')"
    src    ="https://tinyurl.com/y4sytr78"
    alt    ="line cap values table"
    title  ="line cap values table"
  />
</figure>


Note that in this example, the rectangle is not affected. It has no line ends visible - all its sides meet. However, the next property we're going to look at will have an effect on rectangles!


#### Line style: setting the type of corner when two lines meet

The `lineJoin` property of the context indicates the way corners are rendered, when two lines meet. Possible values are miter (the default) for creating sharp corners, `round`, or `bevel` for "cut corners".

Try the [next example interactively](https://jsbin.com/yivaraposi/1/edit?html,output): ([Local Example - Corner Type](src/3.5.7-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yyo8vyv8')"
    src    ="https://tinyurl.com/y4mganaj"
    alt    ="lineJoin value table"
    title  ="lineJoin value table"
  />
</figure>


#### Line style: specific case of lineJoin="miter", the `miterLimit` property, a way to avoid looooooong corners!

The `miterLimit` property value corresponds to the maximum miter length: the distance between the inner corner and the outer corner where two lines meet. When the angle of a corner between two lines gets smaller, the miter length grows and can become too long.

In order to avoid this situation, we can set the miterLimit property of the context to a threshold value. If the miter length exceeds the miterLimit value, then the corner will be rendered as if the lineJoin property had been set to "bevel" and the corner will be "cut".

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyo8vyv8')"
    src    ="https://tinyurl.com/y4vh9opq"
    alt    ="miterLimit property shown with 3 different angles, we see that the part tha goes out of the angle can become very long"
    title  ="miterLimit property shown with 3 different angles, we see that the part tha goes out of the angle can become very long"
  />
</figure>


You can try an interactive example [here](https://jsbin.com/nadaloqebu/edit?html,output). ([Local Example - Limited Length](src/3.5.7-example4.html))

In the example, try different values for the `miterLimit` property. You'll see that the way the corners are rendered changes at values around 2 and 3.


#### Knowledge check 3.5.7

1. Which context property defines the shape of line extremities?<br/>

  a. lineWidth<br/>
  b. lineCap<br/>
  c. lineJoin<br/>

  Ans: <span style="color: magenta;">b</span>, xc<br/>
  Explanation: Indeed, the value of the `lineCap` property defines the shape of the line ends.



### 3.5.8 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ The course did not cover all of them, but there are multiple libraries built on top of the canvas for visualizing data, for writing games, etc. If you have experience with some, please post reviews and share experiences in this discussion forum.
+ Next week we will see how to do animations and how to manage user interactions (mouse, keyboard). What are your expectations?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will all be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy)__: Take any of the previous suggested projects, and improve them with shadows, gradients, patterns, etc.
+ __Project 2 (a bit harder)__: Try to use the multiple image loader showed in the course, in one of your projects.



