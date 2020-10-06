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

+ [Intermediate mode vs. path mode](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#341-immediate-mode-vs-path-mode)
  + intermediate mode
    + executing a call to a drawing method immediately drawing in the canvas
    + as soon as they executed
      + the results displayed on screen
      + the drawings performed
      + pixels on the canvas area change their colors
      + etc.
    + example methods: `drawImage(...)`, `fillRect(x, y, width, height)`, `strokeRect(x, y, width, height)`, `fillText(message, x, y)` and `strokeText(message, x, y)`
  + path mode
    + fill a buffer then execute all buffered orders at once to enable optimization and parallelism
    + first send drawing orders to the graphics processor, and these orders are stored in a buffer
    + then call methods to draw the whole buffer at once
    + parallelism: GPU of the graphics card hardware able to parallelize the computations
    + example: instead of calling `strokeRect(...)` or `fillRect(...)` many times, just call `rect(...)` method of the context once
    + slightly faster execution time
    + `ctx.beginPath()`: reset the buffer (empty its contents) to start a new buffer / path

+ [Summary of path mode principles](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#341-immediate-mode-vs-path-mode)
  + call drawing methods that work in path mode, e.g., `ctx.rect(...)` instead of `ctx.strokeRect(...)` or `ctx.fillRect(...)`
  + `ctx.stroke()` or `ctx.fill()`: draw the buffer's contents
  + two consecutive calls to `ctx.stroke()` will draw the buffer contents twice
  + use `ctx.beginPath()` to empty it if needed
  + path drawing faster than immediate drawing (parallelization possible)



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

+ [Time measuring](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#341-immediate-mode-vs-path-mode)
  + `console.time(name_of_timer)` and `console.timeEnd(name_of_timer)`: used to calculate time elapsed
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

+ [Drawing rounded rectangles](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#349-drawing-rounded-rectangles)
  + `ctx.arcTo(x1, y1, x2, y2, radius)` method: a bit complex to use, but very practical for drawing rounded rectangles
  + rounded rectangle corners: draw an arc of a circle depending on some tangents
    + draw imaginary lines: `(x0, y0)` & `(x1, y1)` and `(x1, y1)` & `(x2, y2)`
    + tangent points: take an imaginary circle of radius `r` and slide it up two lines until touching both lines
    + `arcTo(x1, y1, x2, y2, r)`: draw an arc line from the current point `(x0, y0)` to the first tangent point on the line from `(x0, y0)` to `(x1, y1)`
    + draw an arc from that tangent point to another tangent point on the line from `(x1, y1)` to `(x2, y2)` along the circumference of the circle
    + add the tangent point where the arc ends up, on the line from `(x1, y1)` to `(x2, y2)` to the path as the new current point on the path

      <figure style="margin: 0.5em; text-align: center;">
        <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
          onclick="window.open('http://www.dbp-consulting.com/tutorials/canvas/CanvasArcTo.html')"
          src    ="https://tinyurl.com/ycz22yx5"
          alt    ="arcTo coordinates"
          title  ="arcTo coordinates"
        />
      </figure>

+ [Rounded rectangle](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#349-drawing-rounded-rectangles)
  + function: `var roundedRect=function(ctx,x,y,width,height,radius,fill,stroke) {...}`
  + draw top and top right corner: `ctx.moveTo(x+radius,y); ctx.arcTo(x+width,y,x+width,y+radius,radius);`
  + draw right side and bottom right corner: `ctx.arcTo(x+width,y+height,x+width-radius,y+height,radius);`
  + draw bottom and bottom left corner: `ctx.arcTo(x,y+height,x,y+height-radius,radius);`
  + draw left and top left corner: `ctx.arcTo(x,y,x+radius,y,radius);`
  + fill inside: `if(fill) { ctx.fill(); }`
  + draw stoke:  `if(stroke){ ctx.stroke(); }`
  + usage: `ctx.moveTo(x+radius, y); ctx.arcTo(x+width, y,x+width, y+height, radius); ctx.arcTo(x+width, y+height, x, y+height, radius);  ctx.arcTo(x, y+height, x, y,radius); ctx.arcTo(x, y, x+width, y,radius);`



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







## Drawing Lines

+ [Drawing lines in path mode](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#343-drawing-lines)
  + path drawing: `ctx.moveTo(x, y)` in conjunction w/ other drawing methods ending in "To", such as `ctx.lineTo(x, y)`
  + consecutive calls to `ctx.lineTo(x, y)`: store in the path/buffer a set of connected lines
  + draw altogether by a single call to `ctx.stroke()` or `ctx.fill()`
  + procedure of drawing lines
    + put the "pencil" somewhere w/ a call to `ctx.moveTo(x1, y1)`, origin of the 1st line
    + call `ctx.lineTo(x2, y2)` to draw a line from origin (x1, y1) to position(x2, y2), then (x2, y2) serve as an origin for the next line
    + call `ctx.lineTo(x3, y3)` to draw a new line from (x2, y2) to (x3, y3), and (x3, y3) as the new origin
    + repeat the previous steps to draw more lines
    + call the `ctx.stroke()` or `ctx.fill()` to draw the path defined
  + `ctx.stroke()` or `ctx.fill()`: use the current values of the strokeStyle or fillStyle properties
  + `ctx.moveTo(x, y)` method: move the origin to the new origin (x, y) w/o connecting them
  + [Drawing line w/ style](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#344-drawing-lines-with-different-styles)
    + `fill()` or `stroke()` draws the whole path, even if disconnected, and even if already drawn
    + using the `ctx.beginPath()` method to draw two different paths
    + `ctx.beginPath()` erase the buffer but not change any context properties
  + [good practice](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#345-drawing-lines-in-immediate-mode): save/restore of the context at the beginning/end of the function to avoid affecting other functions' context
  + [`ctx.closePath()` method](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#347-closing-a-path): draw from the last point to the first point


+ [Line style](../WebDev/Frontend-W3C/2-HTML5Coding/03e-Graphics.md#357-styling-lines)
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



## Drawing Arrows

+ [Drawing arrows](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#346-drawing-arrows)
  + adapted from [Stackoverflow]( https://stackoverflow.com/questions/808826/draw-arrow-on-canvas-tag)
  + draw an arrow in a single function: `function drawArrow(ctx, fromx, fromy, tox, toy, arrowWidth, color){...}`
  + fixing the head length: `var headlen = 10;`
  + calculate the angle from given the beginning (fromx, fromy) to the end (arrow) (tox, toy): `var angle = Math.atan2(toy-fromy,tox-fromx);`
  + store/restore the drawings in canvas: `ctx.save()` & `ctx.restor()`
  + draw one line (the arrow body) w/ given width: `ctx.beginPath(); ctx.moveTo(fromx, fromy); ctx.lineTo(tox, toy); ctx.lineWidth = arrowWidth; ctx.stroke();`
  + draw three connected lines (the arrow head)
    + starting a new path from the head of the arrow to one of the sides of the point: `ctx.beginPath(); ctx.moveTo(tox, toy); ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7), toy-headlen*Math.sin(angle-Math.PI/7));`
    + path from the side point of the arrow, to the other side point: `ctx.lineTo(tox-headlen*Math.cos(angle+Math.PI/7), toy-headlen*Math.sin(angle+Math.PI/7));`
    + path from the side point back to the tip of the arrow, and then again to the opposite side point: `ctx.lineTo(tox, toy); ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7), toy-headlen*Math.sin(angle-Math.PI/7));`
  + draws the paths created above: `ctx.stroke();`
  + [drawing lines and arcs with arrow heads](http://www.dbp-consulting.com/tutorials/canvas/CanvasArrow.html)




## Drawing Circles & Arcs

+ [Drawing circles and arcs](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#348-drawing-circles-and-arcs)
  + [HTML5 Canvas Arc Tutorials](https://www.html5canvastutorials.com/tutorials/html5-canvas-arcs/)
  + `ctx.arc(cx, cy, radius, startAngle, endAngle, drawInverse)` method: used for drawing arcs of circles
  + parameters: center of the circle/arc, radius, starting angle of the arc (turning clockwise), the ending angle of the arc, and an optional parameter

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
        onclick="window.open('https://tinyurl.com/y7wuv8vt')"
        src    ="https://tinyurl.com/ydxcvvmr"
        alt    ="drawing circle, coordinate system"
        title  ="drawing circle, coordinate system"
      />
    </figure>

    + optional parameter:
      + false: (default) drawing an arc of circle corresponding to the parameters
      + true: drawing complementary

      <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
        <a href="https://tinyurl.com/y7wuv8vt" ismap target="_blank">
          <img style="margin: 0.1em;" height=100
            src    ="https://tinyurl.com/y95m6q4x"
            alt    ="arc of circle"
            title  ="arc of circle"
          >
          <img style="margin: 0.1em;" height=100
            src    ="https://tinyurl.com/ycpj7h8g"
            alt    ="complementary of previous arc is drawn"
            title  ="complementary of previous arc is drawn"
          >
        </a>
      </div>

    + radius between `0` and `2*Math.PI`
  + drawing circle: call `ctx.arc(centerX, centerY, radius, 0, 2*Math.PI, false);` once w/ `startAngle = 0` and `endAngle = 2*Math.PI`




## Drawing Curves and Curve Arrows

+ [Drawing quadratic curve](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#3410-quadratic-curves)
  + defined by a starting point (called a "context point"), a control point, and an ending point
  + curve fitting the tangents between the context and control points and between the control and ending points
  + define the context point: `moveTo(x, y)` or the ending point of a previous path
  + the control point controls the curvature: moving the control point farther $\to$ a sharper curve

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick="window.open('https://www.html5canvastutorials.com/tutorials/html5-canvas-quadratic-curves/')"
        src    ="https://tinyurl.com/y93lpz8k"
        alt    ="quadratic curve"
        title  ="quadratic curve"
      />
    </figure>

  + typical use

    <div><ol style="list-style-type: decimal;">
    <li value="1">context.moveTo(contextX, contextY);</li>
    <li>context.quadraticCurveTo(controlX, controlY, endX, endY);</li>
    <li>// Optional : set lineWidth and stroke color</li>
    <li><span style="line-height: 23.2727279663086px;">context</span>.lineWidth = 5;</li>
    <li><span style="line-height: 23.2727279663086px; background-color: #eeeeee;">context</span>.strokeStyle = "#0000ff";</li>
    <li>// Draw!</li>
    <li><span style="line-height: 23.2727279663086px; background-color: #eeeeee;">context</span>.stroke(); </li>
    </ol></div>

+ [Curved arrow](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#3411-curved-arrows)
  + function: `function drawCurvedArrow(startPointX, startPointY, endPointX, endPointY, quadPointX, quadPointY, lineWidth, arrowWidth, color) {...}`
  + save/restore context at beginning/end of function: `ctx.save();` & `ctx.restore();`
  + compute angle of the end tangent, useful for drawing the arrow head: `var arrowAngle = Math.atan2(quadPointX - endPointX, quadPointY - endPointY) + Math.PI;`
  + start a new path: `ctx.beginPath();`
  + draw body of the arrow: `ctx.moveTo(startPointX, startPointY); ctx.quadraticCurveTo(quadPointX, quadPointY, endPointX, endPointY);`
  + compute the rotated endpoints of the two lines of the arrow head: `tx.moveTo(endPointX - (arrowWidth * Math.sin(arrowAngle - Math.PI / 6)), endPointY - (arrowWidth * Math.cos(arrowAngle - Math.PI / 6))); ctx.lineTo(endPointX, endPointY); ctx.lineTo(endPointX - (arrowWidth * Math.sin(arrowAngle + Math.PI / 6)), endPointY - (arrowWidth * Math.cos(arrowAngle + Math.PI / 6)));`
  + complete drawing: `ctx.stroke(); ctx.closePath();`

+ [Drawing B&eacute;zier curves](../WebDev/Frontend-W3C/2-HTML5Coding/03d-Graphics.md#3412-bzier-curves)
  + `ctx.bezierCurveTo(controlX1, controlY1, controlX2, controlY2, endX, endY)` method
    + used mostly for drawing "S" shapes or asymmetric curves
    + defined by a context point, like quadratic curves, two control points that define two tangents, and an ending point (see diagram)
    + 1st part of the curve: tangential to the imaginary line defined by the context point and the first control point
    + 2nd part of the curve: tangential to the imaginary line defined by the second control point and the ending point

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
        onclick="window.open('https://tinyurl.com/y27jjh7y')"
        src    ="https://tinyurl.com/y6rotc24"
        alt    ="A bezier curve is defined by the current context point, two control points, and an ending point. The first part of the curve is tangential to the imaginary line that is defined by the context point and the first control point. The second part of the curve is tangential to the imaginary line that is defined by the second control point and the ending point."
        title  ="A bezier curve is defined by the current context point, two control points, and an ending point."
      />
    </figure>

  + interactive applications & tool
    + [Canvas Bézier Curve Example](http://blogs.sitepointstatic.com/examples/tech/canvas-curves/bezier-curve.html)
    + [IvanK Lib graphics demos](http://lib.ivank.net/?p=demos&d=bezier)
    + Nice video tutorial: [Bézier curves under the hood](https://vimeo.com/106757336)
    + [bezierCurveTo command generator](https://www.victoriakirst.com/beziertool/)
  + typical use:
    + move to context point (initial point): `ctx.moveTo(contextX, contextY);`
    + draw B&eacute;zier curve: `ctx.bezierCurveTo(controlX1, controlY1, controlX2, controlY2, endX, endY);`




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




