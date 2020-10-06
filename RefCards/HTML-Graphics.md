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

+ [Steps to draw graphics on an HTML5 canvas](http://tutorials.jenkov.com/html5-canvas/overview.html)
  + Wait for the page fully loaded
  + Obtain a reference to the canvas element
  + Obtain a 2D context from the canvas element
  + Draw graphics using the draw functions of 2D context



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

+ [Saving and Restoring the context](../WebDev/Frontend-W3C/2-HTML5Coding/03b-Graphics.md#329-saving-and-restoring-the-context)
  + `ctx.save()` & `ctx.restore()` methods
    + saved properties: all properties effecting the drawing
    + probably save the context property values in a hardware register on the graphics card
    + multiple contexts able to be saved consecutively and restored
  + __best practice__: save the context before any activities modifying the context, and restore it at the end of the activities, in particular, a function


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





