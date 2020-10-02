# Week 3: HTML5 Graphics

## 3.5 Colors, gradients, patterns, etc.

### 2.5.0 Lecture Notes

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
    + the last color of the gradient repeated w/0 any interpolation (columns 200-300 are red)
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
    + creating a Javascript image object; e.g., `var imageObj = new Image();`
    + define a callback function called once the fully loaded image in memory; e.g., `imageObj.onload = function(){...}`
    + set the source image tot he URL of the pattern; e.g., `imageObj.src = "https://www.myserver.com/myRepeatablePattern.png";`
    + an HTTP request sent in background by the browser and loading the image into memory, then call the callback function
      + callback called asynchronously, after the `src` attribute of `imageObj` is set: `imageObj.onload = function(){...}`
      + enter `imageObj.onload` after image loaded to create a pattern object: `pattern1 = ctx.createPattern(imageObj, "repeat");`
      + good practice: set the pattern as a global variable, easier to share
    + draw pattern within the callback function
      + draw a textured rectangle: `ctx.fillStyle = pattern1; ctx.fillRect(10, 10, 500, 800);`

+ [Multi-image Pattern](#355-a-multiple-image-loader)
  + load all image before drawing
  + only when all images have been loaded, start drawing.
  + solution: use a multiple image loader that counts the loaded images and calls a function you pass when done
  + an array of URLs that used by multiple image loader
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

  + use of image loader: `loadImages(imagesToLoad, function(imagesLoaded) {...}`
    + create patterns from the loaded image: `patternFlowers = ctx.createPattern(imagesLoaded.flowers, 'repeat'); patternLion    = ctx.createPattern(imagesLoaded.lion, 'repeat'); patternBW = ctx.createPattern(imagesLoaded.blackAndWhiteLys, 'repeat'); patternFloor   = ctx.createPattern(imagesLoaded.tiledFloor, 'repeat');`
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
      + define the 4 properties for better clarity: `ctx.shadowColor = "Grey"; ctx.shadowBlur = 20; x.shadowOffsetX = 15; ctx.shadowOffsetY = 15;`
    + green filled rectangle w/ shadow: `ctx.fillStyle = "#22FFDD"; ctx.fillRect(20, 20, 200, 100);`
    + stroked rectangle w/ shadow: `ctx.strokeStyle = "purple";  ctx.lineWidth=10; ctx.strokeRect(20, 150, 200, 100);`
  + example: unwanted shadow
    + add the path a full circle: `ctx.arc(centerX, centerY, radius, 0, 2*Math.PI, false);`
    + w/ path drawing to change the context properties until a call to `stroke()` or `fill()` performed: `ctx.fillStyle = "lightBlue";
    + add shadows before drawing the filled circle: `addShadows() {...}`
      + set color: `ctx.shadowColor = "Grey"; // color`
      + set shadow blur level: `ctx.shadowBlur = 20;      // blur level`
      + set shadow horizontal level: `ctx.shadowOffsetX = 15;   // horizontal offset`
      + set shadow vertical offset: `ctx.shadowOffsetY = 15;   // vertical offset`
    + draw the filled circle in light blue: `ctx.fill();`
    + set outline properties: `ctx.lineWidth = 5; ctx.strokeStyle = "black";`
    + draw wireframe along the path: `ctx.stroke()`
    + `ctx.fill()` and `ctx.stroke()` casts a shadow along the whole path $\to$ unwanted shadow inside the circle
    + solution to remove unwanted shadow
      + save the context before setting the shadow properties
      + draw the filled circle
      + restore the context (to its previous state: without shadows)
      + draw the outlined circle by calling `ctx.stroke()`




### 3.5.1 Canvas context: colors

In previous examples, we saw how to set the current color using the `strokeStyle` and `fillStyle` properties of the canvas context object.

Let's look at color in a little more detail, and see how we can use gradients or patterns/textures/images (in other words: fill shapes or fill the outline of the shapes with some images that repeat themselves).


#### Colors and transparency

You can use [the same syntax for colors that is supported by CSS3](https://www.w3.org/TR/css3-color/). The next lines show possible values/syntaxes.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#00ff00"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"rgb(0, 0, 255)"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"rgba(0, 0, 255, 0.5)"</span><span class="pun">;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">createLinearGradient</span><span class="pun">(</span><span class="pln">x0</span><span class="pun">,</span><span class="pln">y0</span><span class="pun">,</span><span class="pln">x1</span><span class="pun">,</span><span class="pln">y1</span><span class="pun">);</span><span class="pln"> </span></li>
</ol></div>

... where the `(x0, y0)` and `(x1, y1)` parameters define "the direction of the gradient" (as a vector with a starting and an ending point). This direction is an invisible line along which the colors that compose the gradient will be interpolated.

Let's see an example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> grdFrenchFlag </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createLinearGradient</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">300</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
</ol></div>

This line defines the direction of the gradient: a virtual, invisible line that goes from the top left corner of the canvas (0, 0) to the top right corner of the canvas (300, 0). The interpolated colors will propagate along this line. 

If this gradient is going to be reused by different functions, it is good practice to create/initialize it in a function called when the page is loaded and to store it in a global variable.


__Step #2: add a number of "color stops" to this gradient__

We will add a set of "colors" and "stops" to this gradient. The stops go from 0 (beginning of the virtual line defined just above), to 1 (end of the virtual line). A color associated with a value of 0.5 will be right in the middle of the virtual line.

Here is an example that corresponds to an interpolated version of the French flag, going from blue to white, then to red, with proportional intervals. We define three colors, blue at position 0, white at position 0.5 and red at position 1:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> grdFrenchFlag</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> grdFrenchFlag</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.5</span><span class="pun">,</span><span class="pln"> </span><span class="str">"white"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> grdFrenchFlag</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="str">"red"</span><span class="pun">);</span><span class="pln"> </span></li>
</ol></div>


__Step 3: draw some shapes__

First, let's set the `fillStyle` or `strokeStyle` of the context with this gradient, then let's draw some shapes "on top of the gradient".

In our example, the gradient corresponds to an invisible rectangle that fills the canvas. If we draw a rectangle of the canvas size, it should be filled with the entire gradient:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> grdFrenchFlag</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">300</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">grdFrenchFlag </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createLinearGradient</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">300</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> grdFrenchFlag</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
</ol></div>

This code is rather ugly isn't it? It would have been better  to use a loop...

Here is function that draws a chessboard ([online example at JsBin](https://jsbin.com/netijalofu/1/edit?html,output)): ([Loca Example - Chessboard](src/3.5.2-example4.html))

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// n = number of cells per row/column</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> drawCheckboard</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> grdFrenchFlag</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> l </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> h </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cellWidth </span><span class="pun">=</span><span class="pln"> l </span><span class="pun">/</span><span class="pln"> n</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cellHeight </span><span class="pun">=</span><span class="pln"> h </span><span class="pun">/</span><span class="pln"> n</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="pln">i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="pln">j </span><span class="pun">=</span><span class="pln">&nbsp;i % 2</span><span class="pun">;</span><span class="pln"> j </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> j</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">cellWidth</span><span class="pun">*i</span><span class="pun">,</span><span class="pln"> cellHeight</span><span class="pun">*</span><span class="pln">j</span><span class="pun">,</span><span class="pln"> cellWidth</span><span class="pun">,</span><span class="pln"> cellHeight</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawCheckboard</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> grdFrenchFlag</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineWidth</span><span class="pun">=</span><span class="lit">10</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;">&nbsp; &nbsp; ...</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="pln">i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="pln">j </span><span class="pun">=</span><span class="pln">&nbsp;<span style="color: #006666;" color="#006666">i % 2</span></span><span class="pun">;</span><span class="pln"> j </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> j</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln"><strong>stroke</strong>Rect</span><span class="pun">(</span><span class="pln">cellWidth</span><span class="pun">*i</span><span class="pun">,</span><span class="pln"> cellHeight</span><span class="pun">*</span><span class="pln">j</span><span class="pun">,</span><span class="pln"> cellWidth</span><span class="pun">,</span><span class="pln"> cellHeight</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### What happens if we define a gradient smaller than the canvas?

Let's go back to the very first example on this page - the one with the blue-white-red interpolated French flag. This time we will define a smaller gradient. Instead of going from (0, 0) to (300, 0), it will go from (100, 0) to (200, 0), while the canvas remains the same (width=300, height=200).

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> grdFrenchFlag </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createLinearGradient</span><span class="pun">(</span><strong><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span></strong><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">grdFrenchFlag </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createLinearGradient</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">600</span><span class="pun">,</span><span class="pln"> </span><span class="lit">400</span></strong><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> setGradient</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; grdFrenchFlag </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createLinearGradient</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; grdFrenchFlag</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; grdFrenchFlag</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.5</span><span class="pun">,</span><span class="pln"> </span><span class="str">"white"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; grdFrenchFlag</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="str">"red"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // set the new gradient to the current fillStyle</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> grdFrenchFlag</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">// n = number of cells per row/column</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> drawCheckboard</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> l </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> h </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cellWidth </span><span class="pun">=</span><span class="pln"> l </span><span class="pun">/</span><span class="pln"> n</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cellHeight </span><span class="pun">=</span><span class="pln"> h </span><span class="pun">/</span><span class="pln"> n</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="pln">i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">+=</span><span class="lit">2</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="pln">j </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> j </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> j</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> cellWidth</span><span class="pun">*(</span><span class="pln">i</span><span class="pun">+</span><span class="pln">j</span><span class="pun">%</span><span class="lit">2</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> cellHeight</span><span class="pun">*</span><span class="pln">j</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>setGradient</strong></span><strong><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> x</span><span class="pun">+</span><span class="pln">cellWidth</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">+</span><span class="pln">cellHeight</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> cellWidth</span><span class="pun">,</span><span class="pln"> cellHeight</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> grd </span><span class="pun">=</span><span class="pln"> context</span><span class="pun">.</span><strong><span class="pln">createRadialGradient</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> grd</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="str">"red"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> grd</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.17</span><span class="pun">,</span><span class="pln"> </span><span class="str">"orange"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> grd</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.33</span><span class="pun">,</span><span class="pln"> </span><span class="str">"yellow"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> grd</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.5</span><span class="pun">,</span><span class="pln"> </span><span class="str">"green"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> grd</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.666</span><span class="pun">,</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> grd</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="str">"violet"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> grd</span><span class="pun">;</span></li>
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

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln">&nbsp;imageObj&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;new Image();</span></li>
  </ol></div>

2. __Define a callback function that will be called once the image has been fully loaded__ in memory; we cannot draw before the image has been loaded.

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">imageObj</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">...</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
  </ol></div>

3. __Set the source of this image to the URL of the pattern__ (in our example with [url of the pattern](https://tinyurl.com/y6snxuju)),

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">imageObj</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://www.myserver.com/myRepeatablePattern.png"</span><span class="pun">;</span><span class="pln"> </span></li>
  </ol></div>

4. As soon as step 3 is executed, an HTTP request is sent in background by the browser, and when the image is loaded in memory, the callback defined at step 2 is called. We create a pattern object inside, from the loaded image:

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// callback called asynchronously, after the src attribute of imageObj is set</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln"> imageObj</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){&nbsp;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // We enter here when the image is loaded, we create a pattern object.</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // It is good practice to set this as a global variable, easier to share</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>pattern1 </strong></span><strong><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="str">"repeat"</span><span class="pun">);</span></strong></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pun">};</span></li>
  </ol></div>

5. __Inside the callback function (or inside a function called from inside the callback) we can draw.__

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// callback called asynchronously, after the src attribute of imageObj is set</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln"> imageObj</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; pattern1 </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="str">"repeat"</span><span class="pun">);</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
  <li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Draw a textured rectangle</span></strong></li>
  <li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> pattern1</span><span class="pun">;</span></strong></li>
  <li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">500</span><span class="pun">,</span><span class="pln"> </span><span class="lit">800</span><span class="pun">);</span></strong></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pun">};</span></li>
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

<div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"500"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;Your browser does not support the canvas tag. </span><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

JavaScript source code:

<div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">,</span><span class="pln"> pattern1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// We need 1) to create an empty image object, 2) to set a callback function</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// that will be called when the image is fully loaded, 3) to create a </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// pattern object, 4) to set the fillStyle or the strokeStyle property of </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// the context with this pattern, 5) to draw something</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// WE CANNOT DRAW UNTIL THE IMAGE IS FULLY LOADED -&gt; draw from inside the</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="com">// onload callback only !</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - Allocate an image</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> imageObj </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com"><span style="color: #000000;" color="#000000">&nbsp; &nbsp;</span>// 2 - callback called asynchronously, after the src attribute of imageObj </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// is set</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;imageObj</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// We enter here only when the image has been loaded by the browser</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// 4 - Pattern creation using the image object</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// Instead of "repeat", try different values : repeat-x, repeat-y, </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// or no-repeat, You may draw larger shapes in order to see </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// different results</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// It is good practice to leave this as a global variable if it</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// will be reused by other functions</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; pattern1 </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="str">"repeat"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="com">// 5 - Draw things. Here a textured rectangle</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> pattern1</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span>// ... And a wireframe one</li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineWidth</span><span class="pun">=</span><span class="lit">20</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeStyle</span><span class="pun">=</span><span class="pln">pattern1</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">230</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; };</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; // 3 - Send the request to load the image</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; // Setting the src attribute&nbsp;will tell the browser to send an asynchronous </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; // request.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; // When the browser gets an answer, the callback above will be called</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; imageObj</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://www.dreamstime.com/colourful-flowers-repeatable-pattern-thumb18692760.jpg"</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">pattern1 </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="str">"<strong>repeat</strong>"</span><span class="pun">);</span></li>
</ol></div>

Please try: `repeat-x`, `repeat-y` or `no-repeat` as acceptable values. Just change this line in the online example and you will see live results.


#### Knowledge check 3.5.4

1. Patterns are images that can be used to "fill" shapes, eventually repeating themselves?<br/>

  a. Yes, but only with filled shapes; patterns cannot be used with the `strokeStyle` property of the context.<br/>
  b. Yes<br/>
  c. No<br/>

  Ans: B<BR/>
  eXPLANATION: Patterns can be used with all kinds of shapes, and with both `strokeStyle` and `fillStyle`



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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// List of images to load, we used a JavaScript object instead of </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// an array, so that named indexes (aka properties)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// can be used -&gt; easier to manipulate</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> imagesToLoad </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;flowers</span><span class="pun">: </span><span class="pln"></span><span class="str">'https://i.ibb.co/4NN9Sgn/flowers.jpg'</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;lion</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://i.ibb.co/3NyqKnY/lion.jpg'</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;blackAndWhiteLys</span><span class="pun">:</span><span class="pln"> </span><span class="str">'https://i.ibb.co/VNLVpcL/final.jpg'</span><span class="pun">,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;tiledFloor</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; 'https://i.ibb.co/Dt6txmG/repeatable-Pattern.jpg'</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div>

Notice that instead of using a traditional array, we defined this list as a JavaScript object, with properties whose names will be easier to manipulate (flowers, lion, tiledFloor, etc.).


#### The image loader function

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> loadImages</span><span class="pun">(</span><span class="pln">imagesToBeLoaded</span><span class="pun">,</span><span class="pln"> drawCallback</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> imagesLoaded </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> loadedImages </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> numberOfImagesToLoad </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// get num of&nbsp;images to load</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> name </span><span class="kwd">in</span><span class="pln"> imagesToBeLoaded</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;numberOfImagesToLoad</span><span class="pun">++;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> name </span><span class="kwd">in</span><span class="pln"> imagesToBeLoaded</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;imagesLoaded</span><span class="pun">[</span><span class="pln">name</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;imagesLoaded</span><span class="pun">[</span><span class="pln">name</span><span class="pun">].</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(++</span><span class="pln">loadedImages </span><span class="pun">&gt;=</span><span class="pln"> numberOfImagesToLoad</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;drawCallback</span><span class="pun">(</span><span class="pln">imagesLoaded</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="com">// if</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">};</span><span class="pln"> </span><span class="com">// function</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;imagesLoaded</span><span class="pun">[</span><span class="pln">name</span><span class="pun">].</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> imagesToBeLoaded</span><span class="pun">[</span><span class="pln">name</span><span class="pun">];</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="com">// for</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span><span class="com">// function</span></li>
</ol></div>

__Explanations:__

+ This function takes as a parameter the list of images to be loaded, and a drawCallback function that will be called only once all images have been loaded. This callback takes as a parameter a new object that is the list of images that have been loaded (see line 16).
+ We first count the number of images to load (lines 7-9), then for each image to be loaded we create a new JavaScript image object (line 12) and set its src attribute (line 19) - this will start to load the image.
+ When an image comes in, the onload callback is called (line 14) and inside, we increment the number of images loaded (line 15) and test if this number is >=  the total number of images that should be loaded. If this is the case, the callback function is called (line 16).


#### Example of use of this loader

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> loadImages</span><span class="pun">(</span><span class="pln">imagesToLoad</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">imagesLoaded</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; patternFlowers </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imagesLoaded</span><span class="pun">.</span><span class="pln">flowers</span><span class="pun">,</span><span class="pln"> </span><span class="str">'repeat'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; patternLion &nbsp; &nbsp;</span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imagesLoaded</span><span class="pun">.</span><span class="pln">lion</span><span class="pun">,</span><span class="pln"> </span><span class="str">'repeat'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; patternBW </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imagesLoaded</span><span class="pun">.</span><span class="pln">blackAndWhiteLys</span><span class="pun">,</span><span class="pln"> </span><span class="str">'repeat'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; patternFloor &nbsp;&nbsp;</span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createPattern</span><span class="pun">(</span><span class="pln">imagesLoaded</span><span class="pun">.</span><span class="pln">tiledFloor</span><span class="pun">,</span><span class="pln"> </span><span class="str">'repeat'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawRectanglesWithPatterns</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">});</span><span class="pln"> </span></li>
</ol></div>


__Explanations:__

+ Line 1 is the call to the image loader, the first parameter is the list of images to be loaded, while the second parameter is the callback function that will be called once all images have been loaded.
+ Lines 2-5: in this callback we create patterns from the loaded images (note the use of the property names imagesLoaded.flowers, etc. that makes the code easier to read).
+ Line 7: then we call a function that will draw the rectangles.

Here is the function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawRectanglesWithPatterns</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">patternFloor</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">patternLion</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">patternFlowers</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">patternBW</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> init</span><span class="pun">();</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"400"</span><span class="pln"> </span><span class="atn">height</span><span class="pln"> </span><span class="pun">=</span><span class="atv">800</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; Your browser does not support the canvas tag.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // call to a function that will set the 4 context properties for shadows</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; setShadow</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // all drawings that will occur will cast shadows</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// first green filled rectangle</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#22FFDD"</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// second stroked rectangle</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"purple"</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineWidth</span><span class="pun">=</span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">// We define the 4 properties in a dedicated function, for clarity</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> setShadow</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowColor </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Grey"</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// color</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowBlur </span><span class="pun">=</span><span class="pln"> </span><span class="lit">20</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// blur level</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowOffsetX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">15</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// horizontal offset</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowOffsetY </span><span class="pun">=</span><span class="pln"> </span><span class="lit">15</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// vertical offset</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Add to the path a full circle (from 0 to 2PI)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">arc</span><span class="pun">(</span><span class="pln">centerX</span><span class="pun">,</span><span class="pln"> centerY</span><span class="pun">,</span><span class="pln"> radius</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// With path drawing you can change the context</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// properties until a call to stroke() or fill() is performed</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"lightBlue"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="com">// add shadows before drawing the filled circle</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln"> addShadows</span><span class="pun">();</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Draws the filled circle in light blue</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// Prepare for the outline</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"black"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">// draws the path AGAIN (the circle), this</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// time in wireframe</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">/</span><span class="com">/ Notice we only once called context.arc()! And drew it twice </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// with different styles</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><strong><span class="pln"> addShadows</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowColor </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Grey"</span><span class="pun">;</span><span class="pln"> </span><span class="com">// color</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowBlur </span><span class="pun">=</span><span class="pln"> </span><span class="lit">20</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// blur level</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowOffsetX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">15</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp;</span><span class="com">// horizontal offset</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">shadowOffsetY </span><span class="pun">=</span><span class="pln"> </span><span class="lit">15</span><span class="pun">;</span><span class="pln">&nbsp; &nbsp;</span><span class="com">// vertical offset</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="com">// save the context before setting shadows and drawing the filled circle</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// With path drawing you can change the context</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// properties until a call to stroke() or fill() is performed</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"lightBlue"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="com">// add shadows before drawing the filled circle</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong>addShadows</strong></span><strong><span class="pun">();</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draws the filled circle in light blue</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="com">// restore the context to its previous saved state</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">...</span></li>
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
  Explanation" No, shadows have four properties just for them: `shadowColor`, `shadowBlur`, `shadowOffsetX` and `shadowOffsetY`.



### 3.5.7 Styling lines

Several context properties can be used to set the thickness of the shape outlines, the way line end caps are drawn, etc.

They apply to all shapes that are drawn in path mode (lines, curves, arcs) and some also apply to rectangles.


#### Line style: change the line thickness

We have seen this before. This is done by changing the value (in pixels) of the lineWidth property of the context:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></strong><span class="pln"> </span><span class="com">// set the thickness of every shape drawn in stroke/wireframe mode to 10 pixels</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span>&lt;title&gt;</span><span class="pln">A simple example of lineWidth property use</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span></span><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"500"</span><span class="tag">&gt;</span><span class="pln">Your browser does not support the canvas tag.</span><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span></span><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span></span><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// first path</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// second part of the path</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln"><span class="pln">&nbsp; </span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">120</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;</span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// indicate stroke color + draw first part of the path</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#0000FF"</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Current line thickness is 20 pixels </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">20</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draws a rectangle</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">230</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span></span><span class="tag">&lt;/script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp;<span class="pln">&nbsp; </span></span></span><span class="tag">&lt;/body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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


Try the [next example interactively](https://jsbin.com/reqavetipu/1/edit?html,output): ([Local Example - Line End Cap](src/5.3.7-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yyo8vyv8')"
    src    ="https://tinyurl.com/y4sytr78"
    alt    ="line cap values table"
    title  ="line cap values table"
  />
</figure>


Note that in this example, the rectangle is not affected. It has no line ends visible - all its sides meet. However, the next property we're going to look at will have an effect on rectangles!


#### Line style: setting the type of corner when two lines meet

The `lineJoin` property of the context indicates the way corners are rendered, when two lines meet. Possible values are miter (the default) for creating sharp corners, `round`, or `bevel` for "cut corners".

Try the [next example interactively](https://jsbin.com/yivaraposi/1/edit?html,output): ([Local Example - Corner Type](src/5.3.7-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
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


You can try an interactive example [here](https://jsbin.com/nadaloqebu/edit?html,output).

In the example, try different values for the `miterLimit` property. You'll see that the way the corners are rendered changes at values around 2 and 3.


#### Knowledge check 3.5.7

1. Which context property defines the shape of line extremities?<br/>

  a. lineWidth<br/>
  b. lineCap<br/>
  c. lineJoin<br/>

  Ans: 




