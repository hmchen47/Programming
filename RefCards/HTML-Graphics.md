# HTML4 - Graphics

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





