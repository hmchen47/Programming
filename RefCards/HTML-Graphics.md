# HTML4 - Graphics


## Drawing Modes

+ [Drawing modes of graphics](../WebDev/Frontend-W3C/2-HTML5Coding/03c-Graphics.md#331-immediate-mode)
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




## The `<canvas>` element

+ [The `<canvas>` element](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#322-the-canvas-element)
  + provide scripts with a resolution-dependent bitmap canvas
  + used for rendering graphs, game graphics, or other visual images on the fly
  + designed for pixel-based graphics, while SVG (Scalable Vector Graphics, another W3C standard) for vector-based graphics
  + shapes that canvas JavaScript drawing API supported: lines, rectangles, ellipses, arcs, curves, text, images
  + drawing styles: affect the way shapes drawn, e.g., color, width, shadows, etc.
  + alpha channel: transparent mode
  + [35 incredible dataviz tools](https://www.creativebloq.com/design-tools/data-visualization-712402)
  + 3D drawing: possible using the WebGL API in a `<canvas>` w/ [BabylonJS](https://www.babylonjs.com/) and [ThreeJS](https://threejs.org/)
  + [HTML standard](https://html.spec.whatwg.org/multipage/canvas.html) of the `<canvas>` element

+ [Accessible principles on `<canvas>`](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#323-canvas-and-accessibility)
  + providing alternative content for what is drawn on the `<canvas>`
  + exposing the location of shapes, paths, images drawn on the `<canvas>` to assistive technologies
  + visually indicating whether or not a shape in the canvas had keyboard focus

+ [`<canvas>` cheetsheet](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#324-html-canvas-cheatsheet)
  + [PDF file](https://tinyurl.com/y6cvfxv9)
  + [HTML file](https://tinyurl.com/kxm2vxf)
  
+ [canvas coordinate system](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#325-coordinate-system)
  + (0, 0): the top left corner
  + X axis: from the left to the right
  + Y axis: from the top to the bottom

+ [Steps to draw graphics on an HTML5 canvas](http://tutorials.jenkov.com/html5-canvas/overview.html)
  + Wait for the page fully loaded
  + Obtain a reference to the canvas element
  + Obtain a 2D context from the canvas element
  + Draw graphics using the draw functions of 2D context

+ [Saving and Restoring the context](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#329-saving-and-restoring-the-context)
  + `ctx.save()` & `ctx.restore()` methods
    + saved properties: all properties effecting the drawing
    + probably save the context property values in a hardware register on the graphics card
    + multiple contexts able to be saved consecutively and restored
  + __best practice__: save the context before any activities modifying the context, and restore it at the end of the activities, in particular, a function

  + results displayed only in the browser's console



## HTML Canvas Reference

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 50vw;" cellspacing="0" cellpadding="5" border="1">
    <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.w3schools.com/tags/ref_canvas.asp">HTML Canvas Reference</a></caption>
    <thead>
    </thead>
    <tbody>
    <!-- Colors, Styles, and Shadows -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Colors, Styles, and Shadows </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Property</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_fillstyle.asp">fillStyle</a></td>
        <td>Sets or returns the color, gradient, or pattern used to fill the drawing</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_strokestyle.asp">strokeStyle</a></td>
        <td>Sets or returns the color, gradient, or pattern used for strokes</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_shadowcolor.asp">shadowColor</a></td>
        <td>Sets or returns the color to use for shadows</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_shadowblur.asp">shadowBlur</a></td>
        <td>Sets or returns the blur level for shadows</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_shadowoffsetx.asp">shadowOffsetX</a></td>
        <td>Sets or returns the horizontal distance of the shadow from the shape</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_shadowoffsety.asp">shadowOffsetY</a></td>
        <td>Sets or returns the vertical distance of the shadow from the shape</td>
      </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_createlineargradient.asp"> createLinearGradient()</a></td>
        <td>Creates a linear gradient (to use on canvas content)</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_createpattern.asp">createPattern()</a></td>
        <td>Repeats a specified element in the specified direction</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_createradialgradient.asp">createRadialGradient()</a></td>
        <td>Creates a radial/circular gradient (to use on canvas content)</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_addcolorstop.asp">addColorStop()</a></td>
        <td>Specifies the colors and stop positions in a gradient object</td>
      </tr>
    <!-- Line Style -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Line Style </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Property</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_linecap.asp">lineCap</a></td>
        <td>Sets or returns the style of the end caps for a line</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_linejoin.asp">lineJoin</a></td>
        <td>Sets or returns the type of corner created, when two lines meet</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_linewidth.asp">lineWidth</a></td>
        <td>Sets or returns the current line width</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_miterlimit.asp">miterLimit</a></td>
        <td>Sets or returns the maximum miter length</td>
      </tr>
    <!-- Rectangles -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Rectangles </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_rect.asp">rect()</a></td>
        <td>Creates a rectangle</td>
      </tr>
      <tr>
       <td><a href="https://www.w3schools.com/tags/canvas_fillrect.asp">fillRect()</a></td>
        <td>Draws a "filled" rectangle</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_strokerect.asp">strokeRect()</a></td>
        <td>Draws a rectangle (no fill)</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_clearrect.asp">clearRect()</a></td>
        <td>Clears the specified pixels within a given rectangle</td>
      </tr>
    <!-- Paths -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Paths </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_fill.asp">fill()</a></td>
        <td>Fills the current drawing (path)</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_stroke.asp">stroke()</a></td>
        <td>Actually draws the path you have defined</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_beginpath.asp">beginPath()</a></td>
        <td>Begins a path, or resets the current path</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_moveto.asp">moveTo()</a></td>
        <td>Moves the path to the specified point in the canvas, without creating a line</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_closepath.asp">closePath()</a></td>
        <td>Creates a path from the current point back to the starting point</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_lineto.asp">lineTo()</a></td>
        <td>Adds a new point and creates a line to that point from the last specified point in the canvas</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_clip.asp">clip()</a></td>
        <td>Clips a region of any shape and size from the original canvas</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_quadraticcurveto.asp">quadraticCurveTo()</a></td>
        <td>Creates a quadratic Bézier curve</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_beziercurveto.asp">bezierCurveTo()</a></td>
        <td>Creates a cubic Bézier curve</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_arc.asp">arc()</a></td>
        <td>Creates an arc/curve (used to create circles, or parts of circles)</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_arcto.asp">arcTo()</a></td>
        <td>Creates an arc/curve between two tangents</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_ispointinpath.asp">isPointInPath()</a></td>
        <td>Returns true if the specified point is in the current path, otherwise false</td>
      </tr>
    <!-- Transformations -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Transformations </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_scale.asp">scale()</a></td>
        <td>Scales the current drawing bigger or smaller</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_rotate.asp">rotate()</a></td>
        <td>Rotates the current drawing</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_translate.asp">translate()</a></td>
        <td>Remaps the (0,0) position on the canvas</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_transform.asp">transform()</a></td>
        <td>Replaces the current transformation matrix for the drawing</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_settransform.asp">setTransform()</a></td>
        <td>Resets the current transform to the identity matrix. Then runs <a href="https://www.w3schools.com/tags/canvas_transform.asp"> transform()</a></td>
      </tr>
    <!-- Text -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Text </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Property</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_font.asp">font</a></td>
        <td>Sets or returns the current font properties for text content</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_textalign.asp">textAlign</a></td>
        <td>Sets or returns the current alignment for text content</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_textbaseline.asp">textBaseline</a></td>
        <td>Sets or returns the current text baseline used when drawing text</td>
      </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_filltext.asp">fillText()</a></td>
        <td>Draws "filled" text on the canvas</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_stroketext.asp">strokeText()</a></td>
        <td>Draws text on the canvas (no fill)</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_measuretext.asp">measureText()</a></td>
        <td>Returns an object that contains the width of the specified text</td>
      </tr>
    <!-- Image Drawing -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Image Drawing </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_drawimage.asp">drawImage()</a></td>
        <td>Draws an image, canvas, or video onto the canvas</td>
      </tr>
    <!-- Pixel Manipulation -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Pixel Manipulation </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Property</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_imagedata_width.asp">width</a></td>
        <td>Returns the width of an ImageData object</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_imagedata_height.asp">height</a></td>
        <td>Returns the height of an ImageData object</td>
        </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_imagedata_data.asp">data</a></td>
        <td>Returns an object that contains image data of a specified ImageData object</td>
      </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_createimagedata.asp">createImageData()</a></td>
        <td>Creates a new, blank ImageData object</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_getimagedata.asp">getImageData()</a></td>
        <td>Returns an ImageData object that copies the pixel data for the specified rectangle on a canvas</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_putimagedata.asp">putImageData()</a></td>
        <td>Puts the image data (from a specified ImageData object) back onto the canvas</td>
      </tr>
    <!-- Compositing -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Compositing </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Property</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_globalalpha.asp">globalAlpha</a></td>
        <td>Sets or returns the current alpha or transparency value of the drawing</td>
      </tr>
      <tr>
        <td><a href="https://www.w3schools.com/tags/canvas_globalcompositeoperation.asp">globalCompositeOperation</a></td>
        <td>Sets or returns how a new image is drawn onto an existing image</td>
      </tr>
    <!-- Other -->
    <tr style="font-size: 1.2em; margin: 0.2em;">
      <th colspan="2" style="background-color: beige; color: darkblue;"> Other </th>
    </tr>
    <tr>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:3%;">Method</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
      <tr>
        <td>save()</td>
        <td>Saves the state of the current context</td>
      </tr>
      <tr>
        <td>restore()</td>
        <td>Returns previously saved path state and attributes</td>
      </tr>
      <tr>
        <td>createEvent()</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <td>getContext()</td>
        <td>&nbsp;</td>
      </tr>
      <tr>
        <td>toDataURL()</td>
        <td>&nbsp;</td>
      </tr>
    </tbody>
  </table><br/>
  


## Draw Rectangle

+ [Drawing rectangle](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#326-drawing-rectangles-in-a-canvas)
  + simple drawing
    + add the `<canvas>` element into an HTML page
      + selector to identify the canvas itself
      + specify the size of canvas w/ `width` and `height` attributes
      + NOT supported message placed btw opening and closing tags
      + canvas transparent by default
      + multiple canvas allowed in a page
    + select the `<canvas>` element for use from JavaScript
      + element in the DOM, e.g., `var canvas = document.getElementById("myCanvas");`
      + CSS selector syntax for selecting elements, e.g, `var canvas = document.querySelector("#myCanvas");`
    + get a "2D context" associated with the canvas, useful for drawing and setting drawing properties (color, etc.)
      + `context`: a particular object as the core of the canvas JavaScript API providing methods for drawing
      + access the context: `var ctx=canvas.getContext('2d');`
      + set filled color: `ctx.fillStyle='red';`
      + draw filled rectangle: `ctx.fillRect(x, y, width, height);`
  + only access elements when the DOM is ready
    + select and get 2D context via `init()` function
    + unable to access the elements of the page before the page loaded entirely and before the DOM ready
    + ways to achieve the requirement
      + add `onload` attribute w/ `<body>` element, e.g., `<body onload="init();">` (__good practice__)
      + put the JavaScript code at the end of the document, just before `</body>` between `<script>`...`</script>`
  + access drawing context before manipulating it
    + the drawing context defines the drawing methods and properties
    + __good practice__: get the canvas, the context, the width and height of the canvas and other global objects in this "init" function
  + summary of drawing on a canvas
    + declare the canvas, remembering to add an `id` attribute, and fallback content
    + get a reference to the canvas in a JavaScript variable using the DOM API
    + get the context for drawing in that canvas
    + specify some drawing properties (optional)
    + draw the shape

+ [Drawing principles](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#327-drawing-principles)
  + `fillstyle` property: a property in the context, similar to a CSS property
  + `fillRect(x, y, width, height)` method: draw a filled rectangle
  + `strokeStyle` property: how the shape's outline rendered
  + `strokeRect(x, y, width, height)` method: draw the wireframe mode of a rectangle w/ `strokStyle` property
  + `clearRect(x, y, width, height)` method: erase the specified rectangle
  + `linewidth` property: a property applied only in `stroke` mode w/ value in `px`
  + `font` property: specify the font property of the context, syntax same as in CSS for using 'system font", e,g,. `ctx.font = 'italic 20pt Calibri';`
  + `ctx.fillText(str, x, y)` method:
    + draw text message `str` at (x, y) position
    + `fillStyle` property to modify the color of the message
  + summary 
    + "stroke":
      + wireframe of shapes
      + a prefix for setting properties or calling methods that effect wireframe shapes
    + "fill": filled the shapes
    + `ctx.strokStype=...`: set the property of wireframed shapes
    + `ctx.fillStyle=...`: set the property of filled shapes
    + `ctx.strokeRect(x, y, width, height)`: draw wireframe rectangle from (x, y) to (x+width, y+height)
    + `ctx.fillRect(x, y, width, height)`: draw filled rectangle from (x, y) to (x+width, y+height)
    + `ctx.lineWidth`: set the line width of wireframed shapes
    + `ctx.strokeText(msg, x, y)` or `ctx.fillText(msg, x, y)`: draw a text msg for wireframed or filled text respectively
    + `ctx.font`: set the character font w/ values used in CSS syntax, e.g., `ctx.font = 'italic 20pt Calibri';`



## Drawing Text

+ [Drawing text](../WebDev/Frontend-W3C/2-HTML5Coding/03c-Graphics.md#332-drawing-text)
  + two main methods: `ctx.strokeText(message, x, y)` and `ctx.fillText(message, x, y)`
  + `ctx.font` property
    + specify the font style (plain, bold, italic), the size, and the font name
    + accepted values: font-style, font-weight, font-size, font-face
    + possible values
      + font-style: normal, italic, oblique
      + font-weight: normal, bold, bolder, lighter
      + font-size: a size in pixels or in points, such as 60pt, 20px, 36px, etc.
      + font-face: Arial, Calibri, Times, Courier, etc. Some font faces may not work in all browsers
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
    + tell how the `y` parameter of the `fillText("msg", x, y)` and `strokeText("msg", x, y)` methods interpreted
    + possible values: top, hanging, middle, alphabetic, ideographic, bottom-glyp (left diagram)
  + `textAlign` property
    + how the x parameter used when calling `strokeText("msg", x, y)` and `fillText("msg", x, y)`
    + possible values: left, center, right, start, end (right diagram)
  
      <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
        <a href="https://tinyurl.com/y5wfa4y5" ismap target="_blank">
          <img style="margin: 0.1em;" width=400
            src    ="https://tinyurl.com/yxa5jg2k"
            alt    ="text baseline"
            title  ="text baseline"
          >
          <img style="margin: 0.1em;" width=150
            src    ="https://tinyurl.com/y2kwbxfo"
            alt    ="horizontal text alignment"
            title  ="horizontal text alignment"
          >
        </a>
      </div>



## Drawing Images

+ [Drawing images](../WebDev/Frontend-W3C/2-HTML5Coding/03c-Graphics.md#333-drawing-images)
  + wait for the image loaded before drawing
  + loading images: an asynchronous process
  + possible to draw images from a video stream, images corresponding to another canvas content, or images defined by  HTML elements in the page
  + procedure to draw image
    + create a JavaScript Image object, e.g., `var imageObj = new Image();`
    + send an asynchronous request in the background by the browser w/ the `src` attribute of this object with the URL of the image file; e.g., `imageObj.src = "https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png";`
    + call the `onload` callback associated with the image; e.g., `window.onload = function () {...}`
    + draw the image only from inside this callback; e.g., `context.drawImage(imageObj, 0, 0);`
  + `drawImage` method: numerous variants
    + `drawImage(img, x, y)`: draw the image at position x, y, keeping the original image size
    + `drawImage(img, x, y, sizeX, sizeY)`: same as before except that the image drawn is resized.
    + `drawImage(img, sx, sy, sw, sh, dx, dy, dw, dh)`: for drawing sub-images, (sx, sy, sw, sh) define the source rectangle, while (dx, dy, dw, sh) define the target rectangle

      <figure style="margin: 0.5em; text-align: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
          onclick="window.open('https://tinyurl.com/yyucaazn')"
          src    ="https://tinyurl.com/yyuawz85"
          alt    ="drawing images with subimages"
          title  ="drawing images with subimages"
        />
      </figure>

  + image defined in `<img src="...">`
  + best practice: only draw an fully loaded image, use the `onload` callback!
  + `window.onload = function() {...};`: execute after the page loaded, i.e., the large image file loaded first, then draw images in the canvas

+ [Drawing images from a video stream](../WebDev/Frontend-W3C/2-HTML5Coding/03c-Graphics.md#334-drawing-images-from-a-video-stream)
  + `drawImage` method
    + take a video element as its first parameter
    + drawn the one currently played by the video stream
  + `setInterval(function, delay)` method: make the browser execute the processFrame function each delayed `delay` ms
  + rotating video effect: `function drawRotatingVideo(x, y) {...}`
    + use of context save/restore primordial as this function changes the coordinate system at each call
    + translating and rotating, requiring second translation to centralize the graph









## 2D Transformations

+ [2D transformations](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#328-2d-transformations)
  + translate (or rotate, or scale) the original coordinate system instead of modifying all the coordinates passed as parameters to each call to drawing methods
  + order of transformation: translate, rotate, and then scale
  + `ctx.translate(offsetX, offsetY)`
    + translation to shift (0, 0) to (offsetX, offsetY)
    + change the position of the coordinate system then draw the shape
  + `ctx.rotate(angle)`: rotate the coordinate system w/ angle in radians
  + `ctx.scale (sx, sy)`:
    + `scale(1, 1)`: no zoom, remain the same
    + `scale(2, 2)`: zooming 2x
    + `scale(0.5, 0.5)`: zoom out to see the drawings half as big as before





