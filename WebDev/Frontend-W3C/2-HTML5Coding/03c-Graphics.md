# Week 3: HTML5 Graphics


## 3.3 Immediate drawing mode

### 3.3.0 Lecture Notes

+ [Drawing modes of graphics](#331-immediate-mode)
  + immediate mode:
    + the HTML5 canvas in this mode
    + as soon as drawn a shape on the canvas, the canvas no longer knows anything about that shape
    + shape visible, but unable to manipulate that shape individually
    + executing a call to a drawing method means immediately drawing in the canvas
    + easier to program as all graphic instructions produce results as soon as the instructions are executed
    + only a few methods work in immediate drawing mode
    + all shapes, including rectangles, text, images, etc.
  + path/buffered mode:
    + useful for drawing lines, curves, arcs, and also rectangles
    + fill a buffer then execute all buffered orders at once to enable optimization and parallelism
  + rectangles: the only shapes that have methods for drawing them immediately and also other methods for drawing them in "path/buffered mode"

+ [Steps to draw graphics on an HTML5 canvas](http://tutorials.jenkov.com/html5-canvas/overview.html)
  + Wait for the page to be fully loaded.
  + Obtain a reference to the canvas element.
  + Obtain a 2D context from the canvas element.
  + Draw graphics using the draw functions of 2D context.

+ [Drawing text](#332-drawing-text)
  + two main methods: `ctx.strokeText(message, x, y)` and `ctx.fillText(message, x, y)`
  + `ctx.font` property
    + specify the font style (plain, bold, italic), the size, and the font name
    + accepted values: font-style, font-weight, font-size, font-face
    + possible values
      + font-style: normal, italic, oblique
      + font-weight: normal, bold, bolder, lighter
      + font-size: a size in pixels or in points, such as 60pt, 20px, 36px, etc.
      + font-face: Arial, Calibri, Times, Courier, etc. Some font faces may not work in all browsers
    + examples:
      + `context.font = "60pt Calibri";`
      + `context.font = "normal normal 20px Verdana";`
      + `context.font = "normal 36px Arial";`
      + `context.font = "italic bold 36px Arial";`
  + `fillText()` & `strokeText()` methods
    + syntax: `fillText(message, x, y[, maxWidth])` & `strokeText(message, x, y[, maxWidth])`
    + draw a text message at the origin of the baseline position
    + `maxWidth`: force the text to fit into a given width, distorting it if necessary
  + `ctx.measureText()` method
    + get the current width in pixels of a given text
    + taking into account the diverse properties involved such as font, size, shadow, lineWidth, etc.
  + `ctx.textbaseline` property
    + change the way the text horizontal drawn
    + used to specify the different ways one can position the baseline of a given text
    + default: `alphabetic`
    + tell how the `y` parameter of the `fillText("some text", x, y)` and `strokeText("some text", x, y)` methods interpreted
    + possible values
  + `textAlign` property
    + how the x parameter will be used when calling `strokeText("some text", x, y)` and `fillText("some text", x, y)`
    + possible values: left, center, right, start, end
  
      <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
        <a href="https://tinyurl.com/y5wfa4y5" ismap target="_blank">
          <img style="margin: 0.1em;" width=300
            src    ="https://tinyurl.com/yxa5jg2k"
            alt    ="text baseline"
            title  ="text baseline"
          >
          <img style="margin: 0.1em;" width=100
            src    ="https://tinyurl.com/y2kwbxfo"
            alt    ="horizontal text alignment"
            title  ="horizontal text alignment"
          >
        </a>
      </div>

+ [Drawing images](#333-drawing-images)
  + wait for the image loaded before drawing
  + loading images: an asynchronous process
  + possible to draw images from a video stream, images corresponding to another canvas content, or images that are defined by  HTML elements in the page
  + procedure to draw image
    + create a JavaScript Image object, e.g., `var imageObj = new Image();`
    + send an asynchronous request in the background by the browser w/ the `src` attribute of this object with the URL of the image file; e.g., `imageObj.src = "https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png"; };`
    + call the `onload` callback associated with the image; e.g., `window.onload = function () {...}`
    + draw the image only from inside this callback; e.g., `context.drawImage(imageObj, 0, 0);`
  + `drawImage` method: numerous variants
    + `drawImage(img, x, y)`: draw the image at position x, y, keeping the original image size
    + `drawImage(img, x, y, sizeX, sizeY)`: same as before except that the image drawn is resized.
    + `drawImage(img, sx, sy, sw, sh, dx, dy, dw, dh)`: for drawing sub-images, (sx, sy, sw, sh) define the source rectangle, while dx, dy, dw, sh define the target rectangle

      <figure style="margin: 0.5em; text-align: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
          onclick="window.open('https://tinyurl.com/yyucaazn')"
          src    ="https://tinyurl.com/yyuawz85"
          alt    ="drawing images with subimages"
          title  ="drawing images with subimages"
        />
      </figure>

    + e.g., `context.drawImage(imageObj, 0, 10, 100, 100);`, `context.drawImage(imageObj, 80, 10, 150, 150);` & `context.drawImage(imageObj, 0, 0, 512, 100, 100, 250, 256, 50);`
  + image defined in `<img src="...">`
    + add an `<img>` in the document, then the browser starts downloading it in background
    + draw w/ `document.querySelector(#img)`: work well w/ most of small images $\to# asynchronous process
  + best practice: only draw an image that is fully loaded, use the `onload` callback!
  + `window.onload = function() {...};`: execute after the page loaded, i.e., the large image file loaded first, then draw images in the canvas

+ [Drawing images from a video stream](#334-drawing-images-from-a-video-stream)
  + `drawImage` method
    + take a video element as its first parameter
    + drawn is the one currently played by the video stream
    + e.g., `ctx.drawImage(video, 0, 0, 320, 180);`, `ctx.drawImage(video, 0, 180, 320, 180);` & `ctx.drawImage(video, 320, 180, 320, 180);`
  + `setInterval(function, delay)` method: make the browser execute the processFrame function each delayed ms
  + rotating video effect: `function drawRotatingVideo(x, y) {...}`
    + use of context save/restore primordial as this function changes the coordinate system at each call; e.g., `ctx.save();` & `ctx.restore();`
    + translating and rotating; e.g., `ctx.translate(x, y);`, `ctx.rotate(angle += 0.01);` & `ctx.translate(-80, -45);`
      + second translates the coordinate system backwards with half of the size of the image that is drawn
      + making the image rotate around the center of the rectangle, instead of around the top left corner at (0, 0) by default



### 3.3.1 Immediate mode

In the previous sections, we learned how to draw filled or wireframe rectangles.

As soon as the `ctx.strokeRect(x, y, width, height)` or the `ctx.fillRect(x, y, width, height)` method is called, a rectangle is indeed drawn immediately in the canvas. 

While drawing rectangles with `strokeRect` or `fillRect`, drawing text or drawing images, all these shapes will be drawn in _immediate mode_.

Another mode called "path mode" or "buffered mode" will be seen later in this course, which will be useful for drawing lines, curves, arcs, and also rectangles. Rectangles are the only shapes that have methods for drawing them immediately and also other methods for drawing them in "_path/buffered mode_".


#### Example: drawing rectangles in immediate mode using best practice

Let's give an example that draws several rectangles, filled or wireframe, with different colors and line widths.

[Online example on JSBin](https://jsbin.com/wijoqak/1/edit?html,output) ([Local Example - Lines and Colors](src/3.3.1-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y6k8evg9')"
    src    ="https://tinyurl.com/y3ms4ta8"
    alt    ="rectangles drawn at different positions"
    title  ="rectangles drawn at different positions"
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2"><span class="pln">&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L5"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;style&gt;</span></li>
<li class="L6"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="com">#myCanvas {</span></li>
<li class="L7"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L8"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L9"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/style&gt;</span></li>
<li class="L0"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln"></span><span class="tag"></span><span class="tag">&lt;script&gt;</span></li>
<li class="L1"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L2"><span class="pln">&nbsp;</span></li>
<li class="L3"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L5"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L6"><span class="pln">&nbsp;</span></li>
<li class="L7"><span class="pln"> </span><span class="com">// black rectangle, default color (black)</span></li>
<li class="L8"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L9"><span class="pln"> </span><span class="com">// outlined rectangle, default color</span></li>
<li class="L0"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L1"><span class="pln">&nbsp;</span></li>
<li class="L2"><span class="pln"> </span><span class="com">// outlined rectangle filled in red, outline blue</span></li>
<li class="L3"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L4"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'lightBlue'</span><span class="pun">;</span></li>
<li class="L5"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L6"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L7"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L8"><span class="pln">&nbsp;</span></li>
<li class="L9"><span class="pln"> </span><span class="com">// A function to automatize previous drawing</span></li>
<li class="L0"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> angle </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI </span><span class="pun">/</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L1"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>drawFilledRectangle</span><span class="pun">(</span><span class="lit">300</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="str">'pink'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">);</span></li>
<li class="L2"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>drawFilledRectangle</span><span class="pun">(</span><span class="lit">300</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'purple'</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> angle </span><span class="pun">+</span><span class="pln"> </span><span class="lit">0.5</span><span class="pun">);</span></li>
<li class="L3"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">};</span></li>
<li class="L4"><span class="pln">&nbsp;</span></li>
<li class="L5"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">function</span><span class="pln"> drawFilledRectangle</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">,</span><span class="pln"> fillColor</span><span class="pun">,</span><span class="pln"> strokeColor</span><span class="pun">,</span><span class="pln"> lw</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6"><span class="pln"> </span><span class="com">// BEST PRACTICE : save if the function change the context or coordinate </span></li>
<li class="L7"><span class="pln"> </span><span class="com">// system</span></li>
<li class="L8"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L9"><span class="pln">&nbsp;</span></li>
<li class="L0"><span class="pln"> </span><span class="com">// position coordinate system</span></li>
<li class="L1"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L2"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span></li>
<li class="L3"><span class="pln">&nbsp;</span></li>
<li class="L4"><span class="pln"> </span><span class="com">// set colors, line width...</span></li>
<li class="L5"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> lw</span><span class="pun">;</span></li>
<li class="L6"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> fillColor</span><span class="pun">;</span></li>
<li class="L7"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> strokeColor</span><span class="pun">;</span></li>
<li class="L8"><span class="pln">&nbsp;</span></li>
<li class="L9"><span class="pln"> </span><span class="com">// draw at 0, 0 as we translated the coordinate</span></li>
<li class="L0"><span class="pln"> </span><span class="com">// system already</span></li>
<li class="L1"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L2"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L3"><span class="pln">&nbsp;</span></li>
<li class="L4"><span class="pln"> </span><span class="com">// BEST PRACTICE : a restore for a save!</span></li>
<li class="L5"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L6"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L7"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L9"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;body&gt;</span></li>
<li class="L0"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"578"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;</span></li>
<li class="L1"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L2"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/body&gt;</span></li>
<li class="L3"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


#### Knowledge check 3.3.1

1. What does immediate drawing mode mean?<br/>
  a. The HTML5 canvas works all the time in a special mode called "immediate drawing mode". It's easier to program as all graphic instructions produce results as soon as the instructions are executed. All methods that produce drawings work in this way.<br/>
  b. The HTML5 canvas' graphic context provides a few drawing methods that work in "immediate drawing mode". When calling these methods, the drawings appear on the canvas as soon as the instructions are executed.<br/>

  Ans: a<br/>
  Explanation: Only a few methods work in immediate drawing mode and are described in this part of the course. Others (lines, arcs, etc.) work in "path mode" or "buffered mode", and these methods will be studied later on.


### 3.3.2 Drawing text

The canvas API provides two main methods for drawing text: `ctx.strokeText(message, x, y)` and `ctx.fillText(message, x, y)`.

It also provides a set of context properties for setting the character font and style, for laying out the text, etc.


#### Typical use

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y5wfa4y5')"
    src    ="https://tinyurl.com/y5o9r5bn"
    alt    ="example of text drawn in a canvas"
    title  ="example of text drawn in a canvas"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="pln">context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"60pt Calibri"</span><span class="pun">;</span></li>
<li class="L1"><span class="com">// .. set color, lineWidth, shadow etc.</span></li>
<li class="L2"><span class="pln"> </span></li>
<li class="L3"><span class="com">// 10, 10 is the start of the baseline, bottom of left leg of the "H" in the </span></li>
<li class="L4"><span class="com">// "Hello World" example.</span></li>
<li class="L5"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L6"><span class="com">// Or</span></li>
<li class="L7"><span class="pln">context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
</ol></div>

Look at the [code from the example](https://jsbin.com/dazefoz/1/edit?html,output) provided: change the position where the text is drawn, change font attributes, etc. ([Local Example - Typical Use](src/3.3.2-example1.html))


#### The context.font property

It is possible to draw text in a canvas using the `font` property of the context to specify the font style (plain, bold, italic), the size, and the font name. Other properties such as `strokeStyle` or `fillStyle`, as well as other properties that are detailed in the next pages, are also going to be taken into account.

The `font` property accepts values like: `font-style`,  `font-weight`, `font-size`, `font-face`.

Accepted values are: 

+ `font-style: normal, italic, oblique`
+ `font-weight: normal, bold, bolder, lighter`
+ `font-size: a size in pixels or in points, such as 60pt, 20px, 36px, etc. `
+ `font-face:  Arial, Calibri, Times, Courier, etc. Some font faces may not work in all browsers.`

Examples:

+ `context.font = "60pt Calibri";`
+ `context.font = "normal normal 20px Verdana";`
+ `context.font = "normal 36px Arial";`
+ `context.font = "italic bold 36px Arial";`


#### The fillText() or strokeText() methods

The `fillText(message, x, y)` or `strokeText(message, x, y)` methods from the context will actually draw a text message at the origin of the baseline position. In the "Hello World" example, this is located at the bottom of the left leg of the "H".

There is a fourth optional parameter maxWidth that forces the text to fit into a given width, distorting it if necessary:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="pln">context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> x</span><span class="pun">,</span><span class="pln"> y</span><span class="pln">&nbsp;</span><span class="pun">[,</span><span class="pln"> maxWidth</span><span class="pun">]);</span><span class="pln"> </span></li>
<li class="L1"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> x</span><span class="pun">,</span><span class="pln"> y</span><span class="pln">&nbsp;</span><span class="pun">[,</span><span class="pln"> maxWidth</span><span class="pun">]);</span><span class="pln"> </span></li>
</ol></div>


#### Example that uses the maxWidth  parameter of the strokeText() or fillText() methods

Try it [online](https://jsbin.com/quweqab/1/edit?html,output): ([Local Example - maxWidth](src/3.3.2-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y5wfa4y5')"
    src    ="https://tinyurl.com/y3a63ey3"
    alt    ="distorded text"
    title  ="distorded text"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="pun">...</span></li>
<li class="L1"><span class="pln">context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"60pt Calibri"</span><span class="pun">;</span></li>
<li class="L2"><span class="pln"> context</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L3"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">;</span></li>
<li class="L4"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"red"</span><span class="pun">;</span></li>
<li class="L5"><span class="pln"> </span></li>
<li class="L6"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L7"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L8"><span class="pln"> </span></li>
<li class="L9"><span class="pln"> </span><span class="com">// Draw text with constrained width of 250 pixels</span></li>
<li class="L0"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">160</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">250</span></strong><span class="pun">);</span></li>
<li class="L1"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">160</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">250</span></strong><span class="pun">);</span></li>
<li class="L2"><span class="pln"> </span></li>
<li class="L3"><span class="com">// Constrain width to 150 pixels</span></li>
<li class="L4"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">220</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">150</span></strong><span class="pun">);</span></li>
<li class="L5"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">220</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">150</span></strong><span class="pun">);</span></li>
</ol></div>


#### Measuring the width of a given text (bounding box)

Try this [example online](https://jsbin.com/kecezim/1/edit?html,output):  ([Local Example - Text Width](src/3.3.2-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y5wfa4y5')"
    src    ="https://tinyurl.com/y4tq6pb3"
    alt    ="measure text width"
    title  ="measure text width"
  />
</figure>


The `ctx.measureText()` method can be used to get the current width in pixels of a given text, taking into account the diverse properties involved such as font, size, shadow, lineWidth, etc.

Source code extract from this example:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="pln">context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"60pt Calibri"</span><span class="pun">;</span></li>
<li class="L1"><span class="pln"> context</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L2"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">;</span></li>
<li class="L3"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"red"</span><span class="pun">;</span></li>
<li class="L4"><span class="pln"> </span></li>
<li class="L5"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L6"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L7"><span class="pln"> </span></li>
<li class="L8"><strong><span class="kwd">var</span><span class="pln"> textMetrics </span><span class="pun">=</span><span class="pln"> context</span><span class="pun">.</span><span class="pln">measureText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">);</span></strong></li>
<li class="L9"><strong><span class="kwd">var</span><span class="pln"> width </span><span class="pun">=</span><span class="pln"> textMetrics</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></strong></li>
<li class="L0"><span class="pln"> </span></li>
<li class="L1"><span class="com">// Draw a text that displays the width of the previous drawn text</span></li>
<li class="L2"><span class="pln"> context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"20pt Arial"</span><span class="pun">;</span></li>
<li class="L3"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Width of previous text: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> width </span><span class="pun">+</span><span class="pln"> </span><span class="str">"pixels"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L4"><span class="pln"> </span></li>
<li class="L5"><span class="pln"> </span><span class="com">// Draw the baseline of the given width</span></li>
<li class="L6"><span class="pln"> context</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L7"><span class="pln"> context</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">width</span><span class="pun">+</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L8"><span class="pln"> context</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
</ol></div>


#### The ctx.textbaseline property: change the way the text is horizontally drawn

[Try this example at JSBin](https://jsbin.com/haxiru/1/edit?html,output) (borrowed and adapted from [Jenkov's canvas tutorial](http://tutorials.jenkov.com/html5-canvas/text.html)): ([Local Example - Text Horizontal Draw](src/3.3.2-example4.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5wfa4y5')"
    src    ="https://tinyurl.com/yxa5jg2k"
    alt    ="text baseline"
    title  ="text baseline"
  />
</figure>


The text baseline is important as it tells how the y parameter of the `fillText("some text", x, y)` and `strokeText("some text", x, y)` methods is interpreted.

The `textBaseline` property of the context is used to specify the different ways one can position the baseline of a given text. The example above shows the different possible values for this property and the corresponding results. The default value is "`alphabetic`" and corresponds to what has been used in the previous "Hello World" example.

Possible values:

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif; width: 50vw; margin: 0 auto;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
<td style="padding: 5px; background-color: #004ce5; color: white; font-size: 150%; border: 2px solid LightSlateGray; text-align: center;" colspan="2">Possible values for the <span style="font-family: 'courier new', courier;">textBaseline</span> property</td>
</tr>
<tr>
<td style="text-align: center; background-color: #004ce5; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top">top</td>
<td style="border: 2px solid LightSlateGray;" valign="top">The text is aligned based on the top of the tallest glyph in the text.</td>
</tr>
<tr>
<td style="text-align: center; background-color: #004ce5; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top">hanging</td>
<td style="border: 2px solid LightSlateGray;" valign="top">The text is aligned based on the line the text seems to hang from. This is almost identical to top, and in many cases, you cannot see the difference.</td>
</tr>
<tr>
<td style="text-align: center; background-color: #004ce5; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top">middle</td>
<td style="border: 2px solid LightSlateGray;" valign="top">The text is aligned according to the middle of the text.</td>
</tr>
<tr>
<td style="text-align: center; background-color: #004ce5; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top">alphabetic</td>
<td style="border: 2px solid LightSlateGray;" valign="top">The bottom of vertically oriented glyphs, e.g. western alphabet like the Latin.</td>
</tr>
<tr>
<td style="text-align: center; background-color: #004ce5; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top">ideographic</td>
<td style="border: 2px solid LightSlateGray;" valign="top">The bottom of horizontally oriented glyphs.</td>
</tr>
<tr>
<td style="text-align: center; background-color: #004ce5; color: white; font-size: 150%; border: 2px solid LightSlateGray;" valign="top">bottom</td>
<td style="border: 2px solid LightSlateGray;" valign="top">The text is aligned based on the bottom of the glyph in the text, that extends furthest&nbsp;down in the text.</td>
</tr>
</tbody>
</table>

Typical use (taken from the example above):

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textBaseline </span><span class="pun">=</span><span class="pln"> </span><span class="str">"top"</span><span class="pun">;</span></strong></li>
<li class="L1"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"top"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">75</span><span class="pun">);</span></li>
<li class="L2"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textBaseline </span><span class="pun">=</span><span class="pln"> </span><span class="str">"hanging"</span><span class="pun">;</span></strong></li>
<li class="L3"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"hanging"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">,</span><span class="pln"> </span><span class="lit">75</span><span class="pun">);</span></li>
<li class="L4"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textBaseline </span><span class="pun">=</span><span class="pln"> </span><span class="str">"middle"</span><span class="pun">;</span></strong></li>
<li class="L5"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"middle"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">120</span><span class="pun">,</span><span class="pln"> </span><span class="lit">75</span><span class="pun">);</span></li>
</ol></div>


#### Horizontal text alignment

Try this [example online](https://jsbin.com/yapiqi/1/edit?html,output):  ([Local Example - Horizontal alignment](src/43.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y5wfa4y5')"
    src    ="https://tinyurl.com/y2kwbxfo"
    alt    ="horizontal text alignment"
    title  ="horizontal text alignment"
  />
</figure>


The `textAlign` property of the context tells how the x parameter will be used when calling `strokeText("some text", x, y)` and `fillText("some text", x, y)`. For example, with `textAlign="center"`, the x parameter gives the position of the vertical center of the text, while in textAlign="right", x corresponds to the rightmost position of the text. 

Typical use (source code taken from the above example):

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"center"</span><span class="pun">;</span></strong></li>
<li class="L1"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"center"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L2"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"start"</span><span class="pun">;</span></strong></li>
<li class="L3"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"start"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">);</span></li>
<li class="L4"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"end"</span><span class="pun">;</span></strong></li>
<li class="L5"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"end"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">60</span><span class="pun">);</span></li>
<li class="L6"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"left"</span><span class="pun">;</span></strong></li>
<li class="L7"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"left"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">80</span><span class="pun">);</span></li>
<li class="L8"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"right"</span><span class="pun">;</span></strong></li>
<li class="L9"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"right"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
</ol></div><br/>


#### Knowledge check 3.3.2

1. Which of these context properties are relevant to drawing text? (3 correct answers)<br/>
  a. ctx.font<br/>
  b. ctx.size<br/>
  c. ctx.width<br/>
  d. ctx.textAlign<br/>
  e. ctx.textBaseline<br/>
  f. ctx.textOutlineWidth<br/>

  Ans: ade<br/>
  Explanation: Of those listed, only `font`, `textAlign` and `textBaseline` are valid. Of course, other properties are relevant too: `strokeStyle`, `fillStyle`, lineWidth etc.



### 3.3.3 Drawing images

__Load images in the background, wait for them to be loaded before drawing!__

Working with images is rather simple, except that we need the images to be fully loaded into memory before drawing them. Loading images is an asynchronous process we need to take care of. Working with multiple images might also be difficult for beginners. We present a multiple image loader later on in this course.

It is also possible to draw images from a video stream, images corresponding to another canvas content, or images that are defined by <img> HTML elements in the page. We will see that as well in the following parts of this chapter.

But let's start with a basic example!


#### Example #1: drawing an image

Try [this example online](https://tinyurl.com/y6hqthlk): ([Local Example - Image](src/3.3.3-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyucaazn')"
    src    ="https://tinyurl.com/yyn5twc2"
    alt    ="html5 logo"
    title  ="html5 logo"
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L4"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Simple image drawing in a canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;script&gt;</span></li>
<li class="L6"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7"><span class="pln"> </span><span class="com">// Necessity to run this code only after the web page has been loaded.</span></li>
<li class="L8"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myCanvas"</span><span class="pun">);</span></li>
<li class="L9"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> context </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">"2d"</span><span class="pun">);</span></li>
<li class="L0"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> imageObj </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">();</span></li>
<li class="L1"><span class="pln"> </span><span class="com">// Callback function called by the imageObj.src = .... line</span></li>
<li class="L2"><span class="pln"> </span><span class="com">//located after this function</span></li>
<li class="L3"><span class="pln"> </span><span class="pln"><strong><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></strong></span><span class="pln"><strong><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></strong></span><span class="pln"><strong><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span></strong>imageObj</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4"><span class="pln"> </span><span class="com">// Draw the image only when we have the guarantee </span></li>
<li class="L5"><span class="pln"> </span><span class="com">// that it has been loaded</span></li>
<li class="L6"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L7"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">};</span></li>
<li class="L8"><span class="pln">&nbsp;</span></li>
<li class="L9"><span class="pln"> </span><span class="com">// Calls the imageObj.onload function asynchronously</span></li>
<li class="L0"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>imageObj</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span></li>
<li class="L1"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="str">"https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png"</span><span class="pun">;</span></li>
<li class="L2"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">};</span></li>
<li class="L3"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;/script&gt;</span></li>
<li class="L4"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L5"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;body&gt;</span></li>
<li class="L6"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"512"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"512"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L7"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/body&gt;</span></li>
<li class="L8"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

__Several things need to be explained here:__

1. We have to __create a JavaScript Image object__ (line 10),
1. When we set the src attribute of this object with the URL of the image file, then __an asynchronous request is sent in the background by the browser__. Loading a big image may take some time, so the rest of the JavaScript code continues running. This is why we call it "asynchronous".
1. When the image file has been loaded, __the browser calls the `onload` callback associated with the image__ (line 14). 
1. __We draw the image only from inside this callback__, otherwise we have no guarantee that the image has been loaded and can be usable. The actual drawing here is done line 17.

__There are numerous variants of the `drawImage(...)` context method at <i>line 17</i>__

+ `drawImage(img, x, y)`: draws the image at position x, y, keeping the original image size.
+ `drawImage(img, x, y, sizeX, sizeY)`: same as before except that the image drawn is resized.
+ `drawImage(img, sx, sy, sw, sh, dx, dy, dw, dh)`: for drawing sub-images, (sx, sy, sw, sh) define the source rectangle, while dx, dy, dw, sh define the target rectangle. If these rectangles don't have the same size, the source sub-image is resized.

See picture below :

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yyucaazn')"
    src    ="https://tinyurl.com/yyuawz85"
    alt    ="drawing images with subimages"
    title  ="drawing images with subimages"
  />
</figure>


#### Example #2: show the different variants of drawImage(...)

[Online example](https://jsbin.com/yetozeh/1/edit?html,css,output): ([Local Example - Image Variants](src/3.3.3-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyucaazn')"
    src    ="https://tinyurl.com/y4enxq32"
    alt    ="variants of drawImages, with the HTML5 logo drawn at different sizes, or with just a sub part of it"
    title  ="variants of drawImages, with the HTML5 logo drawn at different sizes, or with just a sub part of it"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> imageObj </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">();</span></li>
<li class="L1"><span class="pln">&nbsp;</span></li>
<li class="L2"><span class="pln"> imageObj</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Try commenting/uncommenting the following lines to see the</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp;</span><span class="com">// effect of the different drawImage variants</span></li>
<li class="L5"><span class="pln"> </span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Original, big image</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp;</span><span class="com">// context.drawImage(imageObj, 0, 10);</span></li>
<li class="L8"><span class="pln"> </span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Original image drawn with size = 100x100 pixels</span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp;context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp;</span><span class="com">// with size = 150x150</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp;context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">80</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp;</span><span class="com">// with size = 200x200</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp;context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">210</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L5"><span class="pln">&nbsp;</span></li>
<li class="L6"><span class="pln">&nbsp;&nbsp;</span><span class="com">// draw the sub image at 0, 0, width = 512, height = 100</span></li>
<li class="L7"><span class="pln">&nbsp;&nbsp;</span><span class="com">// at position 100, 250, with a width of 256 and a height of 50</span></li>
<li class="L8"><span class="pln">&nbsp; context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">512</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">256</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span></li>
<li class="L0"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L1"><span class="pln"> imageObj</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png"</span><span class="pun">;</span></li>
<li class="L2"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div>


#### Example #3: draw an image defined in the page by an `<img src="...">` element

Sometimes, you may want to draw an image that is already declared in the HTML document as an `<img src="...">` element. Remember that when you add an `<img>` in the document, the browser starts downloading it in background. 

__WRONG__ => indeed, you could try drawing it using some code like this:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="tag">&lt;body&gt;</span></li>
<li class="L1"><span class="pln"> </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"512"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"512"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L2"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Original image as an </span><span class="tag">&lt;img&gt;</span><span class="pln"> element:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L3"><span class="pln"> </span><strong><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"logo"</span></strong></li>
<li class="L4"><strong><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://fc07.deviantart.net/fs70/f/2013/149/b/8/texture_85_by_voyager168-d670m68.jpg"</span><span class="tag">&gt;</span></strong></li>
<li class="L5"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pln">&nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myCanvas"</span><span class="pun">);</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">"2d"</span><span class="pun">);</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> logo </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#logo"</span><span class="pun">);</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">logo</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></strong></li>
<li class="L0"><span class="tag">&lt;/script&gt;</span></li>
<li class="L1"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>


Although you will find many examples on the Web that do it this way, they will only work most of the time with small images, or with images that are in the browser's cache. Remember that __you cannot draw an image that has not been fully loaded!__

If you try to draw an image that is not loaded or partially loaded, you will have unexpected results!

<div style="border: 1px solid red; margin: 20px; padding: 10px;">
<p style="text-align: center;"><strong><em>Best practice: </em></strong><em>only draw an image that is fully loaded, use <br>the </em><em><span style="font-family: 'courier new', courier;">onload</span> callback!</em></p>
</div>

__GOOD =>__ the right way to do this is shown in this [online example](https://jsbin.com/sejoyen/1/edit?html,css,output), that starts drawing only from the onload callback function: ([Local Example - onboard callback](src/3.3.3-example3.html))

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="dec">&lt;!DOCTYPE HTML&gt;</span></li>
<li class="L1"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L4"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Simple image drawing in a canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;script&gt;</span></li>
<li class="L6"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> context</span><span class="pun">,</span><span class="pln"> imageObj</span><span class="pun">;</span></li>
<li class="L7"><span class="pln"> </span></li>
<li class="L8"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myCanvas"</span><span class="pun">);</span></li>
<li class="L0"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>context </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">"2d"</span><span class="pun">);</span></li>
<li class="L1"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>imageObj </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#logo"</span><span class="pun">);</span></li>
<li class="L2"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>drawAllImages</span><span class="pun">();</span></li>
<li class="L3"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">};</span></li>
<li class="L4"><span class="pln"> </span></li>
<li class="L5"><span class="pln"> </span></li>
<li class="L6"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">function</span><span class="pln"> drawAllImages</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"image is already loaded, we draw it!"</span><span class="pun">);</span></li>
<li class="L8"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="com">// Original image drawn with size = 100x100 pixels</span></li>
<li class="L9"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L0"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="com">// with size = 150x150</span></li>
<li class="L1"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">80</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L2"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="com">// with size = 200x200</span></li>
<li class="L3"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">210</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L4"><span class="pln">&nbsp;</span></li>
<li class="L5"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="com">// draw the sub image at 0, 0, width = 512, height = 100</span></li>
<li class="L6"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="com">// at position 100, 250, with a width of 256 and a height of 50</span></li>
<li class="L7"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>context</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">imageObj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">512</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">256</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8"><span class="pln"> </span></li>
<li class="L9"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L0"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;/script&gt;</span></li>
<li class="L1"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L2"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;body&gt;</span></li>
<li class="L3"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;p&gt;</span><span class="pln">A canvas with an image that is further in the page, loaded by the </span><span class="tag">&lt;code&gt;&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">...</span><span class="tag">&gt;&lt;/code&gt;</span><span class="pln"> tag. This is not the recommended way to load images, except if the image is already in your page. Use the onload callback to be sure that the image is in the page.</span></li>
<li class="L4"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"512"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"512"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L5"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;p&gt;</span><span class="pln">Original image as an </span><span class="tag">&lt;img&gt;</span><span class="pln"> element:</span></li>
<li class="L6"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"logo"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png"</span><span class="pln"> </span><span class="atn">alt</span><span class="pun">=</span><span class="atv">"html5 logo"</span><span class="tag">&gt;</span></li>
<li class="L8"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/body&gt;</span></li>
<li class="L9"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


With large image files, this will not break nor produce unexpected results - see the [related JsBin example](http://jsbin.com/wasiwa/1/edit?html,css,output). The [DOM Level 2 Events specification](https://tinyurl.com/y3qf2q6q) says: "<i>The load event occurs when the DOM implementation finishes loading all content within a document, <strong>all frames</strong> within a FRAMESET, or an OBJECT element.</i>" ([Local Example - Large Image](src/3.3.3-example4.html))

Results with a very large image (5160x3270 pixels):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yyucaazn')"
    src    ="https://tinyurl.com/y2vsc93j"
    alt    ="same example with a large image"
    title  ="same example with a large image"
  />
</figure>


#### Knowledge check 3.3.3

1. In this page, we mentioned an "onload callback"... why?<br/>

  a. For checking that an image has been loaded entirely before we try to draw it in a canvas.<br/>
  b. It's just a recommendation, checking if an image is loaded is generally not necessary before trying to draw it, as it will appear anyway line by line as image data arrive in the browser.<br/>

  Ans: a<br/>
  Explanation: The `onload` callback is a way to be sure that an image is loaded. It is very important to check that an image is loaded before drawing it in a canvas.
  

### 3.3.4 Drawing images from a video stream

The `drawImage(...)` function can take a video element as its first parameter. The image that will be drawn is the one currently played by the video stream. This can be done at video frequency on most modern computers or mobile devices.

[Online example at jsBin](https://jsbin.com/canotip/1/edit?html,output) ([Local Example - Drawing Video Image](src/3.3.4-example1.html))

This example shows:

+ a `<video>` element on top, and four images drawn in a canvas below.
+ The images are drawn every XXX milliseconds using the setInterval(function, delay) method.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y6sgaaek')"
    src    ="https://tinyurl.com/y67qnpa7"
    alt    ="video wall with on top a video element playing a streames video file, and at bottom a canvas with the current video image drawn 4 times, including a rotating one"
    title  ="video wall with on top a video element playing a streames video file, and at bottom a canvas with the current video image drawn 4 times, including a rotating one"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> video</span><span class="pun">;</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> angle </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L4"><span class="pln">&nbsp;</span></li>
<li class="L5"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp;<strong>video </strong></span><strong><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'sourcevid'</span><span class="pun">);</span></strong></li>
<li class="L7"><span class="pln">&nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp;ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L9"><span class="pln">&nbsp;</span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp;<strong>setInterval</strong></span><strong><span class="pun">(</span><span class="str">"processFrame()"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">25</span><span class="pun">); // call processFrame&nbsp;each 25ms</span></strong></li>
<li class="L1"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2"><span class="pln">&nbsp;</span></li>
<li class="L3"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> processFrame</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4"><span class="pln">&nbsp;</span>&nbsp; &nbsp;<span class="pln">ctx</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">video</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">320</span><span class="pun">,</span><span class="pln"> </span><span class="lit">180</span><span class="pun">);<br><br></span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp; drawRotatingVideo</span><span class="pun">(</span><span class="lit">480</span><span class="pun">,</span><span class="pln"> </span><span class="lit">90</span><span class="pun">);<br><br></span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pln" style="line-height: 1.6;">ctx</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">drawImage</span><span class="pun" style="line-height: 1.6;">(</span><span class="pln" style="line-height: 1.6;">video</span><span class="pun" style="line-height: 1.6;">,</span><span class="pln" style="line-height: 1.6;"> </span><span class="lit" style="line-height: 1.6;">0</span><span class="pun" style="line-height: 1.6;">,</span><span class="pln" style="line-height: 1.6;"> </span><span class="lit" style="line-height: 1.6;">180</span><span class="pun" style="line-height: 1.6;">,</span><span class="pln" style="line-height: 1.6;"> </span><span class="lit" style="line-height: 1.6;">320</span><span class="pun" style="line-height: 1.6;">,</span><span class="pln" style="line-height: 1.6;"> </span><span class="lit" style="line-height: 1.6;">180</span><span class="pun" style="line-height: 1.6;">);</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">video</span><span class="pun">,</span><span class="pln"> </span><span class="lit">320</span><span class="pun">,</span><span class="pln"> </span><span class="lit">180</span><span class="pun">,</span><span class="pln"> </span><span class="lit">320</span><span class="pun">,</span><span class="pln"> </span><span class="lit">180</span><span class="pun">);</span></li>
<li class="L5"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L6"><span class="pln">&nbsp;</span></li>
<li class="L7"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawRotatingVideo</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Clear the zone at the top right quarter of the canvas</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">320</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">320</span><span class="pun">,</span><span class="pln"> </span><span class="lit">180</span><span class="pun">);</span></li>
<li class="L0"><span class="pln">&nbsp;</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// We are going to change the coordinate system, save the context!</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// translate, rotate and recenter the image at its "real" center, </span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//not the top left corner</span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">0.01</span><span class="pun">); // rotate and increment the current angle</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(-</span><span class="lit">80</span><span class="pun">,</span><span class="pln"> </span><span class="pun">-</span><span class="lit">45</span><span class="pun">);</span></li>
<li class="L8"><span class="pln">&nbsp;</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">video</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">160</span><span class="pun">,</span><span class="pln"> </span><span class="lit">90</span><span class="pun">);</span></li>
<li class="L0"><span class="pln">&nbsp;</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// restore the context</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L4"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L6"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L7"><span class="pln">&nbsp;</span></li>
<li class="L8"><span class="pln"> </span><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">()</span><span class="atv">"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L9"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">This is a </span><span class="tag">&lt;video&gt;</span><span class="pln"> element: </span><span class="tag">&lt;/p&gt;</span></li>
<li class="L0"><span class="pln"> </span><strong><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"sourcevid"</span><span class="pln"> </span><span class="atn">autoplay</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span><span class="atn">loop</span><span class="pun">=</span><span class="atv">"true"</span><span class="tag">&gt;</span></strong></li>
<li class="L1"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/BigBuckBunny_640x360.mp4"</span><span class="pln"> </span></li>
<li class="L1"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/BigBuckBunny_640x360.ogv"</span><span class="pln"> </span></li>
<li class="L2"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/ogg"</span><span class="tag">/&gt;</span></li>
<li class="L3"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span></li>
<li class="L4"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">This is a </span><span class="tag">&lt;canvas&gt;</span><span class="pln"> element: </span><span class="tag">&lt;/p&gt;</span></li>
<li class="L5"><span class="pln"> </span><strong><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"620"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"360"</span><span class="tag">&gt;&lt;/canvas&gt;</span></strong></li>
<li class="L6"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
</ol></div>


__Explanations:__

+ _Line 11_: the call to `setInterval` will make the browser execute the processFrame function each 25ms.
+ _Lines 15, 17 and 18_: in processFrame, `drawImage(...)` is called 3 times with the video element passed as first parameter.
+ _Line 43_: the video element declared at line 43 has `autoplay=true` and `loop=true`, it starts playing the video as soon as possible and will loop it.
+ _Line 21_: We implemented a rotating video effect in the drawRotatingVideo. The use of context save/restore is primordial as this function changes the coordinate system at each call, translating and rotating it. Notice the extra translation at line 31 that translates the coordinate system backwards with half of the size of the image that is drawn. We did this in order to make the image rotate around the center of the rectangle, instead of around the top left corner at (0, 0) by default. Try commenting out this line in the running example and you will see what we mean.


### 3.3.5 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ Drawing images is a bit tricky for JavaScript newcomers as it involves loading them asynchronously before drawing. Do you have any further questions about this? 
+ Did you know we can also draw images from the Webcam? If we start from the Week 2 examples which use the getUserMedia API, it is possible to take screenshots of a person in front of the Webcam. Use the video that plays the Webcam stream as the first parameter of `drawImage(...)`. This is useful for registering forms, for example.


#### Optional projects 

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

__Project 1 (easy)__: Make a funny application by mixing all the things seen so far: images, colors, texts, video...

__Project 2__: Write a small application triggering a screenshot from the Webcam.

__Project 3 (a bit harder, need to know how to use CSS positioning and the CSS z-index property)__: Try to position a canvas on top of a video element and draw shapes on top of the video.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y3gv7b7t" ismap target="_blank">
    <img style="margin: 0.1em;" width=300
    src    ="https://tinyurl.com/y4kvv99x"
    alt    ="canvas and video superposed. Text is drawn on the canvas"
    title  ="canvas and video superposed. Text is drawn on the canvas"
    >
  </a>
  <a href="url" ismap target="_blank">
    <img style="margin: 0.1em;" width=300
    src    ="https://tinyurl.com/y5ptvzuu"
    alt    ="canvas and video"
    title  ="canvas and video"
    >
  </a>
</div>


__Project 4 (follow-up of project 3)__: Play two videos in loop mode at the same time, and draw the current image of the video 2 in the canvas on top of video 1, in a smaller size.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3gv7b7t')"
    src    ="https://tinyurl.com/yxqeqv9u"
    alt    ="video 2 drawn on top of video 1"
    title  ="video 2 drawn on top of video 1"
  />
</figure>


Other example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3gv7b7t')"
    src    ="https://tinyurl.com/y2nmno46"
    alt    ="two videos one on top of the other"
    title  ="two videos one on top of the other"
  />
</figure>



