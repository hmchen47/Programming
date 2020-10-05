# Week 3: HTML5 Graphics

## 3.4 Path drawing mode

 
### 3.4.0 Lecture Notes

+ [Intermediate mode vs. path mode](#341-immediate-mode-vs-path-mode)
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
  
+ [Time measuring](#341-immediate-mode-vs-path-mode)
  + `console.time(name_of_timer)` and `console.timeEnd(name_of_timer)`: used to calculate time elapsed
  + results displayed only in the browser's console

+ [Summary of path mode principles](#341-immediate-mode-vs-path-mode)
  + call drawing methods that work in path mode, e.g., `ctx.rect(...)` instead of `ctx.strokeRect(...)` or `ctx.fillRect(...)`
  + `ctx.stroke()` or `ctx.fill()`: draw the buffer's contents
  + two consecutive calls to `ctx.stroke()` will draw the buffer contents twice
  + use `ctx.beginPath()` to empty it if needed
  + path drawing faster than immediate drawing (parallelization possible)

+ [Drawing lines in path mode](#343-drawing-lines)
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
  + [Drawing line w/ style](#344-drawing-lines-with-different-styles)
    + `fill()` or `stroke()` draws the whole path, even if disconnected, and even if already drawn
    + using the `ctx.beginPath()` method to draw two different paths
    + `ctx.beginPath()` erase the buffer but not change any context properties
  + [good practice](#345-drawing-lines-in-immediate-mode): save/restore of the context at the beginning/end of the function to avoid affecting other functions' context
  + [`ctx.closePath()` method](#347-closing-a-path): draw from the last point to the first point

+ [Drawing arrows](#346-drawing-arrows)
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

+ [Drawing circles and arcs](#348-drawing-circles-and-arcs)
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

+ [Drawing rounded rectangles](#349-drawing-rounded-rectangles)
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

+ [Rounded rectangle](#349-drawing-rounded-rectangles)
  + function: `var roundedRect=function(ctx,x,y,width,height,radius,fill,stroke) {...}`
  + draw top and top right corner: `ctx.moveTo(x+radius,y); ctx.arcTo(x+width,y,x+width,y+radius,radius);`
  + draw right side and bottom right corner: `ctx.arcTo(x+width,y+height,x+width-radius,y+height,radius);`
  + draw bottom and bottom left corner: `ctx.arcTo(x,y+height,x,y+height-radius,radius);`
  + draw left and top left corner: `ctx.arcTo(x,y,x+radius,y,radius);`
  + fill inside: `if(fill) { ctx.fill(); }`
  + draw stoke:  `if(stroke){ ctx.stroke(); }`
  + usage: `var canvas = document.getElementById('myCanvas'); var ctx    = canvas.getContext('2d'); ctx.strokeStyle = 'rgb(150,0,0)'; ctx.fillStyle   = 'rgb(0,150,0)'; ctx.lineWidth   = 7; roundedRect(ctx, 15, 15, 160, 120, 20, true, true);`
  + alternative: `ctx.moveTo(x+radius, y); ctx.arcTo(x+width, y,x+width, y+height, radius); ctx.arcTo(x+width, y+height, x, y+height, radius);  ctx.arcTo(x, y+height, x, y,radius); ctx.arcTo(x, y, x+width, y,radius);`

+ [Drawing quadratic curve](#3410-quadratic-curves)
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

+ [Curved arrow](#3411-curved-arrows)
  + function: `function drawCurvedArrow(startPointX, startPointY, endPointX, endPointY, quadPointX, quadPointY, lineWidth, arrowWidth, color) {...}`
  + save/restore context at beginning/end of function: `ctx.save();` & `ctx.restore();`
  + compute angle of the end tangent, useful for drawing the arrow head: `var arrowAngle = Math.atan2(quadPointX - endPointX, quadPointY - endPointY) + Math.PI;`
  + start a new path: `ctx.beginPath();`
  + draw body of the arrow: `ctx.moveTo(startPointX, startPointY); ctx.quadraticCurveTo(quadPointX, quadPointY, endPointX, endPointY);`
  + compute the rotated endpoints of the two lines of the arrow head: `tx.moveTo(endPointX - (arrowWidth * Math.sin(arrowAngle - Math.PI / 6)), endPointY - (arrowWidth * Math.cos(arrowAngle - Math.PI / 6))); ctx.lineTo(endPointX, endPointY); ctx.lineTo(endPointX - (arrowWidth * Math.sin(arrowAngle + Math.PI / 6)), endPointY - (arrowWidth * Math.cos(arrowAngle + Math.PI / 6)));`
  + complete drawing: `ctx.stroke(); ctx.closePath();`

+ [Drawing B&eacute;zier curves](#3412-bzier-curves)
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

+ [HTML Canvas Reference](https://www.w3schools.com/tags/ref_canvas.asp)

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
  


### 3.4.1 Immediate mode vs. path mode


#### Immediate mode = executing a call to a drawing method means immediately drawing in the canvas

In the previous examples, we saw how to draw rectangles using the `fillRect(x, y, width, height)` and `strokeRect(x, y, width, height)` methods of the context.

We also learned how to draw a text message using the `fillText(message, x, y)` and `strokeText(message, x, y)` methods that draws a text in filled and wireframe mode, respectively.

These methods, along with the `drawImage(...)` method already seen in section 3.3.3, are "immediate methods": as soon as they are executed, the results are displayed on screen, the drawings are performed, pixels on the canvas area change their colors, etc.

Here is a code extract that will draw 1000 random rectangles in a canvas, using immediate mode rectangle drawing calls.


[Online example](https://jsbin.com/yenuvikuno/1/edit?html,output): ([Local Example - Random Rectangles](src/3.4.1-example1.html))

<div><ol>
<li value="1">var canvas, ctx, w, h;</li>
<li> </li>
<li>function init() {</li>
<li>&nbsp; &nbsp; canvas = document.getElementById('myCanvas');</li>
<li>&nbsp; &nbsp; ctx = canvas.getContext('2d');</li>
<li> </li>
<li>&nbsp; &nbsp; w = canvas.width;</li>
<li>&nbsp; &nbsp; h = canvas.height;</li>
<li> </li>
<li>&nbsp; &nbsp; console.time("time to draw");</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;for(var i=0; i &lt; 1000; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var x = Math.random() * w;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var y = Math.random() * h;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var width = Math.random() * w;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var height = Math.random() * h;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;ctx.strokeRect(x, y, width, height); </li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; console.timeEnd("time to draw");</li>
<li>}</li>
</ol></div>

_Lines 12-18_ draw 1000 rectangles of random sizes in immediate mode. We also measure the time using the usual `console.time(name_of_timer)` and `console.timeEnd(name_of_timer)` that will write in the browser console the time elapsed. Note that `console.time(...)` and `console.timeEnd(...)` display results only in the browser's console, not in the JSBin console.

On a Mac Book Pro from 2015, the result is an average time of 4.034ms for drawing all these rectangles:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y37m6gzx')"
    src    ="https://tinyurl.com/y5u9la5o"
    alt    ="Image of the devtool console that shows random time values. The average time elapsed is around 4s"
    title  ="Image of the devtool console that shows random time values. The average time elapsed is around 4s"
  />
</figure>


#### Path mode = fill a buffer then execute all buffered orders at once to enable optimization and parallelism

There is another drawing mode called "path drawing mode" where you first send drawing orders to the graphics processor, and these orders are stored in a buffer. Then you call methods to draw the whole buffer at once. There are also methods to erase the buffer's content.

Path drawing mode allows parallelism: if you need to draw 10,000 rectangles, it's better to store the orders in the graphics card, then execute the drawing all at once, rather than doing 10,000 immediate calls to `strokeRect(...)` for example. With the buffered mode, the Graphic Processing Unit (GPU) of the graphics card hardware will be able to parallelize the computations (modern graphics cards can execute hundreds/thousands of things in parallel).

Same example as before, this time using the buffered mode for drawing rectangles - see the new example online.

Extract from source code (the part that draws the rectangles):

<div><ol>
<li value="1"> for(var i=0; i &lt; 1000; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;var x = Math.random() * w;</li>
<li>&nbsp; &nbsp; &nbsp;var y = Math.random() * h;</li>
<li>&nbsp; &nbsp; &nbsp;var width = Math.random() * w;</li>
<li>&nbsp; &nbsp; &nbsp;var height = Math.random() * h;</li>
<li> </li>
<li>&nbsp; &nbsp; <strong>ctx</strong><strong>.rect(x, y, width, height); // store&nbsp;a rectangle in path/buffer</strong></li>
<li> }</li>
<li><strong> ctx.stroke(); // draws the whole buffer (the 1000 rectangles) at once</strong></li>
</ol></div>


Instead of calling `strokeRect(...)` or `fillRect(...)`, we just call the `rect(...)` method of the context (line 7). This is how we can delay the drawing of the rectangles. The 1000 rectangles are stored in a buffer in the hardware.

The call to `ctx.stroke()` (line 9) or to its sister method `ctx.fill()` will draw the entire buffer contents in fill or stroke mode.

And here is what the timer gives: a slightly faster execution time. Changing 1000 to 100,000 will give even larger differences.

<span style="color: red; font-weight: bold;">Path mode is faster than immediate mode! We have now an average time of 3.1ms</span>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y37m6gzx')"
    src    ="https://tinyurl.com/y64drn5q"
    alt    ="Image of the devtool console that shows random time values. The average time elapsed is around 3.1mss"
    title  ="Image of the devtool console that shows random time values. The average time elapsed is around 3.1mss"
  />
</figure>



#### Reset the path mode buffer

A call to `ctx.beginPath()` will reset the buffer (empty its contents). We will see many more examples of using the Path drawing mode in another section later on this week. 

<div><ol>
<li value="1"> // start a new buffer / path</li>
<li><strong> ctx.beginPath();</strong></li>
<li> </li>
<li> // all these orders are in a buffer/path</li>
<li> ctx.moveTo(10, 10);</li>
<li> ctx.lineTo(100, 100);</li>
<li> ctx.lineTo(150, 70);</li>
<li> </li>
<li> // Draw the buffer</li>
<li> ctx.stroke();</li>
</ol></div>


#### Summary of path mode principles

+ Call drawing methods that work in path mode, for example call `ctx.rect(...)` instead of `ctx.strokeRect(...)` or `ctx.fillRect(...)`
+ Call `ctx.stroke()` or `ctx.fill()` to draw the buffer's contents,
+ Beware that the buffer is never emptied, two consecutive calls to `ctx.stroke()` will draw the buffer contents twice! Instead, use `ctx.beginPath()` to empty it if needed.
+ It is possible to empty the buffer by calling `ctx.beginPath()`.
+ Path drawing is faster than immediate drawing (parallelization is possible).


#### Knowledge check 3.4.1

1. The path drawing mode...<br/>
  a. Enables parallelization by storing drawing instructions in a buffer of the graphics card.<br/>
  b. Draws shapes that compose a path immediately after each instruction is executed.<br/>

  Ans: a<br/>
  Explanation: The first answer is correct. All drawing methods of the context that work in path mode will store instructions in a buffer. These instructions will be interpreted and shapes drawn in the canvas only when we call `ctx.stroke()` or `ctx.fill()`.
  

### 3.4.2 A warning

__Warning__: you do not need to spend too much time on each part of this sub-section

You do not need to memorize or learn by heart all the examples in the following pages. They are given as references. There will be no exercises about curves as they are not often done "by hand", but are generated by tools such as Adobe Illustrator or online generators.

+ __You need to draw arcs?__ Then, please use the corresponding section as a reference: you know you will find one or more examples, also available on JSBin, and a detailed explanation.
+ __You need to draw lines? Arrows? Curves?__ Same thing: go to the corresponding pages and look at the examples!

Also, do not forget to use your favorite HTML5 canvas cheatsheet (provided before in the last section). You will find it very helpful when you start playing with the canvas.


### 3.4.3 Drawing lines

We have been drawing rectangles so far.

Now let's go a bit further by introducing the notion of "path drawing". This approach uses the `ctx.moveTo(x, y)` method of the context, in conjunction with other drawing methods that end in "To", such as `ctx.lineTo(x, y)`.

This makes it easier to draw multiple connected lines. Consecutive calls to `ctx.lineTo(x, y)` will store in the path/buffer a set of connected lines that we will draw altogether by a single call to `ctx.stroke()` or `ctx.fill()`.

Here are the 5 different steps:

1. Put the "pencil" somewhere with a call to `ctx.moveTo(x1, y1)`. This will be the origin of the first line.
2. Call the `ctx.lineTo(x2, y2)` method to draw a line from the previous position (previous step) to the position passed as parameters to the `lineTo(...) `method. This position will serve as the origin for the next line to be drawn.
3. Call `lineTo(x3, y3)` again to draw a line that goes from (x2, y2) to (x3, y3). This line will start at the end of the previous one.
4. Repeat step 3 to draw more connected lines.
5. Call the `ctx.stroke()` or the `ctx.fill()` methods to draw the path defined by the different lines.

Note the call to `ctx.stroke()` or `ctx.fill()` will use the current values of the strokeStyle or fillStyle properties. It is possible to call `ctx.moveTo(x, y)` in the middle of steps 1 through 5 in order to move the pen somewhere else without connecting to the last drawn line.


#### Drawing a grid

Here is the [example online](https://jsbin.com/wolurahofa/1/edit?html,output): ([Local Example - Grid](src/3.4.3-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y436ts2w')"
    src    ="https://tinyurl.com/ybgcv49l"
    alt    ="a blue grid made of multiple vertical and horizontal lines"
    title  ="a blue grid made of multiple vertical and horizontal lines"
  />
</figure>

<div><ol>
<li value="1">var canvas=document.getElementById('myCanvas');</li>
<li>var ctx=canvas.getContext('2d');</li>
<li> </li>
<li>// Vertical lines</li>
<li>for (var x = 0.5; x &lt; 500; x += 10) { </li>
<li>&nbsp; &nbsp; ctx.moveTo(x, 0); </li>
<li>&nbsp; &nbsp; ctx.lineTo(x, 375);</li>
<li>}</li>
<li> </li>
<li>// Horizontal lines</li>
<li>for (var y = 0.5; y &lt; 375; y += 10) {</li>
<li>&nbsp; &nbsp; ctx.moveTo(0, y); </li>
<li>&nbsp; &nbsp; ctx.lineTo(500, y);</li>
<li>}</li>
<li>&nbsp;</li>
<li>// Draw in blue</li>
<li>ctx.strokeStyle = "#0000FF";</li>
<li>&nbsp;</li>
<li>// Until the execution of the next line, nothing has been drawn!</li>
<li> ctx.stroke(); </li>
</ol></div>

In this example, the entire grid is drawn during the execution of the last line of code, with the single call to `ctx.stroke()`.


#### Mixing filled and wireframe shapes (and immediate and path modes)

Try this [interactive example](https://jsbin.com/fatayogapo/1/edit?html,js,output): ([Local Example - Mixing styles and modes](src/3.4.3-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y436ts2w')"
    src    ="https://tinyurl.com/y64548a3"
    alt    ="two consecutive lines and a filled rectangle in immediate mode"
    title  ="two consecutive lines and a filled rectangle in immediate mode"
  />
</figure>

<div><ol>
<li value="1">var canvas=document.getElementById('myCanvas');</li>
<li>var ctx=canvas.getContext('2d');</li>
<li></li>
<li>// a filled rectangle in immediate mode</li>
<li>ctx.fillStyle='#FF0000';</li>
<li>ctx.fillRect(0,0,80,100);</li>
<li> </li>
<li>// two consecutive lines in path mode</li>
<li>ctx.moveTo(0,0);</li>
<li>ctx.lineTo(100, 100); </li>
<li>ctx.lineTo(100,0);</li>
<li> </li>
<li>// draws only the two lines in wireframe mode</li>
<li>ctx.strokeStyle = "#0000FF";</li>
<li>ctx.stroke();</li>
</ol></div>

This example shows that filled and wireframe shapes should be drawn differently (here a filled rectangle is drawn using a call to the `fillRect(...)` method while a wireframe set of connected lines is drawn using the `stroke()` method of the context).

#### Drawing a single path made with disconnected lines / parts

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y436ts2w')"
    src    ="https://tinyurl.com/y69gh9ql"
    alt    ="One path made of two disconnected lines"
    title  ="One path made of two disconnected lines"
  />
</figure>


<div><ol>
<li value="1">var canvas=document.getElementById('myCanvas');</li>
<li>var ctx=canvas.getContext('2d');</li>
<li> </li>
<li>// first part of the path</li>
<li>ctx.moveTo(20,20);</li>
<li>ctx.lineTo(100, 100); </li>
<li>ctx.lineTo(100,0);</li>
<li> </li>
<li>// second part of the path, moveTo(...) is used to "jump" to another place</li>
<li>ctx.moveTo(120,20);</li>
<li>ctx.lineTo(200, 100); </li>
<li>ctx.lineTo(200,0);</li>
<li> </li>
<li>// indicate stroke color + draw the path</li>
<li>ctx.strokeStyle = "#0000FF";</li>
<li>ctx.stroke();</li>
</ol></div>

In this last example, we simply called the `moveTo()` method between each part of the path. And we called `stroke()` only once to draw the whole path.


#### Knowledge check 3.4.3

1. How would you draw a line from (10, 10) to (100, 100)?<br/>

  a. `ctx.moveTo(10, 10); ctx.lineTo(100, 100); ctx. stroke();`<br/>
  b. `ctx.LineTo(10, 10, 100, 100); ctx.stroke();`<br/>
  c. `ctx.line(10, 10, 100, 100); ctx.stroke();`<br/>

  Ans: a<br/>
  Explanation: First, you must move the "pencil" to the starting position (10, 10), and second, draw a line to the ending position (100, 100). Finally, you must call stroke() to execute the drawing orders in the buffer.


### 3.4.4 Drawing lines with different styles

#### Common mistake: drawing the same path twice

Let's look at the drawing from the last example of the previous section:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y6a2vp3r')"
    src    ="https://tinyurl.com/y69gh9ql"
    alt    ="two wireframe shapes, disconnected in one single path"
    title  ="two wireframe shapes, disconnected in one single path"
  />
</figure>


Imagine that we would like to draw them with different styles and colors: the shape on the left will stay as it is now (blue, wireframe), while the shape on the right will be filled, colored in pink. Let's look at how we can do this...

Drawing two paths with different styles: the WRONG and the right way!
First, the wrong way!
In this example, we will draw the two parts of the path with different styles: the first part in wireframe mode, and the second part in filled mode.

What we will try first is to call stroke() after the first half of the path, then call fill() after the second half of the path (check [this interactive example](https://jsbin.com/gutagumoho/edit?html,output)): ([Local Example - Twice Paths](src/3.4.4-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y6a2vp3r')"
    src    ="https://tinyurl.com/y8zebtj5"
    alt    ="twice drawn path"
    title  ="twice drawn path"
  />
</figure>


Here is the code:

<div><ol>
<li value="1">var canvas=document.getElementById('myCanvas');</li>
<li>var ctx=canvas.getContext('2d');</li>
<li> </li>
<li>// first part of the path</li>
<li>ctx.moveTo(20,20);</li>
<li>ctx.lineTo(100, 100); </li>
<li>ctx.lineTo(100,0);</li>
<li> </li>
<li>// indicate stroke color + draw first part of the path</li>
<li>ctx.strokeStyle = "#0000FF";</li>
<li>ctx.stroke();</li>
<li> </li>
<li>// second part of the path</li>
<li>ctx.moveTo(120,20);</li>
<li>ctx.lineTo(200, 100); </li>
<li>ctx.lineTo(200,0);</li>
<li> </li>
<li>// indicate stroke color + draw the path</li>
<li>ctx.fillStyle = "pink";</li>
<li>ctx.fill();</li>
</ol></div>


Hey - it does not work! Weirdly, the two parts of the path are filled in pink! But we called `stroke()` after the first half of the path was drawn (lines 5-8). Then we called `fill()` only after the second part of the path was specified (lines 14-19)... so, what happened?

Remember that fill() or stroke() draws the whole path, even if it is disconnected, and even if it has already been drawn!

What happened is:

+ The call to `stroke()` has drawn the path corresponding to the lines 5-7. Indeed, the first part of the path (on the left) has actually been drawn once in wireframe mode, and in blue.
+ Then, the call to `fill()` at line 20 has drawn the whole path again, but in pink and in filled mode. But this time the path corresponds to lines 5-7 plus lines 14-16 that make up the second shape on the right. So the path that has been drawn this time is made of both of the triangles.

<div style="border: 1px solid red; padding: 20px;">
<p style="text-align: center;"><strong>Important</strong>: If you do not want to draw parts of the same path several times, you need to draw two different paths, <br>using the <span style="font-family: 'courier new', courier;">ctx.beginPath() method, as shown in the next example.</p>
</div>


#### Now, the right way!

[Online example](https://jsbin.com/fayuduyamo/1/edit?html,output): ([Local Example - 2 Paths](src/3.4.4-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y6a2vp3r')"
    src    ="https://tinyurl.com/y8elj46x"
    alt    ="two different paths"
    title  ="two different paths"
  />
</figure>


Source code:

<div><ol>
<li value="1">var canvas=document.getElementById('myCanvas');</li>
<li>var ctx=canvas.getContext('2d');</li>
<li> </li>
<li>// first part of the path</li>
<li>ctx.moveTo(20,20);</li>
<li>ctx.lineTo(100, 100); </li>
<li>ctx.lineTo(100,0);</li>
<li> </li>
<li>// indicate stroke color + draw first part of the path</li>
<li>ctx.strokeStyle = "#0000FF";</li>
<li>ctx.stroke();</li>
<li> </li>
<li><strong>// start a new path, empty the current buffer</strong></li>
<li><span style="color: #ffff00;"><strong>ctx.beginPath();</strong></li>
<li> </li>
<li>// second part of the path</li>
<li>ctx.moveTo(120,20);</li>
<li>ctx.lineTo(200, 100); </li>
<li>ctx.lineTo(200,0);</li>
<li> </li>
<li>// indicate stroke color + draw the path</li>
<li>ctx.fillStyle = "pink";</li>
<li>ctx.fill();</li>
</ol></div>

This time, in order to draw the two shapes differently, we defined two separate paths. The way to do this is just to call `ctx.beginPath()` to start a new path. In this example, the first path has been drawn in wireframe mode, then a new path has been started that is drawn in filled mode.


#### Knowledge check 3.4.4

1. We must call ctx.beginPath() before drawing any new path, but what does it do exactly?<br/>

  a. It will empty the current path (reset the buffer of drawing orders), but it will not change the context properties.<br/>
  b. It will reset all properties of the graphic context.<br/>

  Ans: <span style="color: magenta;">a, xb<br/>
  Explanation: Indeed, calling `ctx.beginPath()` will erase the buffer but will not change any context properties. This method is useful for starting a new path.


### 3.4.5 Drawing lines in immediate mode

Sometimes, it might be useful to draw just one line without being in another path.

It's interesting to see how we can write a single "draw line" function that takes the start and end coordinates, the color, the line width, etc.

Here is the code:

<div><ol>
<li value="1">function drawLine(x1, y1, x2, y2, color, width) {</li>
<li>&nbsp; &nbsp; ctx.save();</li>
<li> </li>
<li>&nbsp; &nbsp; // set color and lineWidth, if these parameters</li>
<li>&nbsp; &nbsp;&nbsp;// are not defined, do nothing (default values)</li>
<li>&nbsp; &nbsp;&nbsp;if(color)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.strokeStyle = color;</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;if(width)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ctx.lineWidth = width;</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// start a new path</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li> </li>
<li>&nbsp; &nbsp; ctx.moveTo(x1, y1);</li>
<li>&nbsp; &nbsp; ctx.lineTo(x2, y2);</li>
<li>&nbsp; &nbsp; ctx.stroke();</li>
<li></li>
<li>&nbsp; &nbsp; ctx.restore();</li>
<li>}</li>
</ol></div>

Notice the save/restore of the context at the beginning/end of the function. This is a REALLY good practice to avoid affecting other functions' context.

+ _Line 13_ starts a new path so that the function will only draw what it is meant to draw: a single line.
+ _Lines 15-17_ move the "pen" at (x1, y1) then draw a line to (x2, y2), and the stroke at _line 17_ makes it appear on the screen.

Here is an example (see [online example](https://jsbin.com/soferaraya/edit?html,output)): ([Local Example - 3 Lines](src/3.4.5-example1.html))

<div><ol>
<li value="1"> drawLine(0, 0, 100, 100);</li>
<li> drawLine(0, 50, 150, 200, 'red');</li>
<li> drawLine(10, 100, 100, 10, 'green', 10);</li>
</ol></div>

Result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/yaoejj5d')"
    src    ="https://tinyurl.com/y83qzvku"
    alt    ="3 lines"
    title  ="3 lines"
  />
</figure>


### 3.4.6 Drawing arrows

In this section, we present a function that draws arrows in a canvas, such as in the illustration below:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y94q93to')"
    src    ="https://tinyurl.com/y78qe9qe"
    alt    ="example of drawing arrows"
    title  ="example of drawing arrows"
  />
</figure>


You may find multiple implementations on the Web for drawing arrows in a canvas, but the one we are presenting has the advantage of being rather simple and enables you to set the color and line width of the arrows.

#### Examples

__Example #1:__

<div><ol>
<li value="1">// Adapted from : https://stackoverflow.com/questions/808826/draw-arrow-on-canvas-tag</li>
<li>function drawArrow(ctx, fromx, fromy, tox, toy, arrowWidth, color){</li>
<li>&nbsp; &nbsp;&nbsp;//variables to be used when creating the arrow</li>
<li>&nbsp; &nbsp;&nbsp;var headlen = 10;</li>
<li>&nbsp; &nbsp;&nbsp;var angle = Math.atan2(toy-fromy,tox-fromx);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; ctx.save();</li>
<li>&nbsp; &nbsp; ctx.strokeStyle = color;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;//starting path of the arrow from the start square to the end square </li>
<li>&nbsp; &nbsp; //and drawing the stroke</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li>&nbsp; &nbsp; ctx.moveTo(fromx, fromy);</li>
<li>&nbsp; &nbsp; ctx.lineTo(tox, toy);</li>
<li>&nbsp; &nbsp; ctx.lineWidth = arrowWidth;</li>
<li>&nbsp; &nbsp; ctx.stroke();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;//starting a new path from the head of the arrow to one of the sides of </li>
<li>&nbsp; &nbsp; //the point</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li>&nbsp; &nbsp; ctx.moveTo(tox, toy);</li>
<li>&nbsp; &nbsp; ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;toy-headlen*Math.sin(angle-Math.PI/7));</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;//path from the side point of the arrow, to the other side point</li>
<li>&nbsp; &nbsp; ctx.lineTo(tox-headlen*Math.cos(angle+Math.PI/7),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;toy-headlen*Math.sin(angle+Math.PI/7));</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;//path from the side point back to the tip of the arrow, and then </li>
<li>&nbsp; &nbsp; //again to the opposite side point</li>
<li>&nbsp; &nbsp; ctx.lineTo(tox, toy);</li>
<li>&nbsp; &nbsp; ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7),</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;toy-headlen*Math.sin(angle-Math.PI/7));</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;//draws the paths created above</li>
<li>&nbsp; &nbsp; ctx.stroke();</li>
<li></li>
<li>&nbsp; &nbsp; ctx.restore();</li>
<li>}</li>
</ol></div>

An arrow is made of one line (the arrow body) and three connected lines (the arrow head). 

As we modify some context properties in this function, we call `save()` and `restore()` at the beginning and at the end of the function.

This function can be improved in many ways: adding shadows, using `fill()` instead of `stroke()`, which gives strange results when the width is too big, etc.


__Example #2__

[Online example](https://jsbin.com/lebutokage/2/edit?html,output) that uses the above code: ([Local Example - Arrows](src/3.4.6-example1.html))

<div><ol>
<li value="1"> drawArrow(ctx, 10, 10, 100, 100, 10, 'red');</li>
<li> </li>
<li> drawArrow(ctx, 100, 10, 140, 140, 3, 'black');</li>
</ol></div>

Result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y94q93to')"
    src    ="https://tinyurl.com/yd5gcg64"
    alt    ="2 arrows"
    title  ="2 arrows"
  />
</figure>



#### How to draw nicer arrows?

On the Web, you will find many different ways to draw arrows.

This [article on drawing lines and arcs with arrow heads](http://www.dbp-consulting.com/tutorials/canvas/CanvasArrow.html) is worth reading. It details how to draw arrows with curved heads and different styles for the head. Note, however, that you will need to modify some parts if you want it to support different line widths, etc.

Screenshot from a demo available on the above Web site:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y94q93to')"
    src    ="https://tinyurl.com/y7j9jz6q"
    alt    ="a clock with arrows"
    title  ="a clock with arrows"
  />
</figure>


In a later part of the course dedicated to curve drawing in a canvas, we will also show how to draw curved arrows, with very simple code (much simpler than the one used for drawing the clock's hands above).


### 3.4.7 Closing a path

The `ctx.closePath()` method indicates that we would like a closed path: draw from the last point to the first.

Try this [interactive example](https://jsbin.com/kajuniyuma/edit?html,output): ([Local Example - Closing Path](src/3.4.7-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y78ooma9')"
    src    ="https://tinyurl.com/y7x28v9f"
    alt    ="closed path"
    title  ="closed path"
  />
</figure>


Source code:

<div><ol>
<li value="1">var canvas=document.getElementById('myCanvas');</li>
<li>var ctx=canvas.getContext('2d');</li>
<li> </li>
<li>// Path made of three points (defines two lines)</li>
<li>ctx.moveTo(20,20);</li>
<li>ctx.lineTo(100, 100); </li>
<li>ctx.lineTo(100,0);</li>
<li> </li>
<li><strong>// Close the path, try commenting this line</strong></li>
<li><strong>ctx.closePath();</strong></li>
<li> </li>
<li>// indicate stroke color + draw first part of the path</li>
<li>ctx.strokeStyle = "blue";</li>
<li>ctx.stroke();</li>
</ol></div>

+ _Lines 5-7_ corresponds to a path made of two consecutive lines. If we just call `stroke()` after that, two lines will be drawn on the canvas.
+ _Line 10_ indicates that we would like a closed path. In this case, the call to `stroke()` at line 14 will draw the two lines plus an extra line that connects the last point of the path to the first one. It will draw a closed triangle!

Try commenting the line in the online example and see the results!


### 3.4.8 Drawing circles and arcs

The `ctx.arc(cx, cy, radius, startAngle, endAngle, drawInverse)` method is useful for drawing arcs of circles. It takes the center of the circle/arc, its radius, the starting angle of the arc (turning clockwise), the ending angle of the arc, and an optional parameter we will talk about later.

Note: the figures in this page have been borrowed from the [HTML5 Canvas Tutorials Web site](https://www.html5canvastutorials.com/tutorials/html5-canvas-arcs/).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y7wuv8vt')"
    src    ="https://tinyurl.com/ydxcvvmr"
    alt    ="drawing circle, coordinate system"
    title  ="drawing circle, coordinate system"
  />
</figure>



#### Typical usage

Typical usage for drawing an arc/circle/ellipse is:

<div><ol>
<li value="1">ctx.arc(centerX, centerY, radius, startAngle, endAngle); // clockwise drawing</li>
<li> </li>
<li>ctx.arc(centerX, centerY, radius, startAngle, endAngle, <strong>false</strong>);</li>
</ol></div>

The angles are in radians (between `0` and `2*Math.PI`). The arc is drawn clockwise. Beware that this may not seem natural if you're used to the trigonometric order.

The last parameter is optional and has a value of `false` by default. If `true`, instead of drawing an arc of circle that corresponds to the parameters, it will draw its complementary. See the examples below to see the difference.


#### Examples

__Example #1: drawing an arc with radius = 50, starting angle = 0, end angle = PI/2__

Try this [example online](https://jsbin.com/vusijenele/edit?html,output): ([Local Example - Arc w/ Radius](src/3.4.8-example1.html))

<div><ol>
<li value="1">ctx.beginPath();</li>
<li>// we ommited the last parameter</li>
<li>ctx.arc(100,&nbsp;75,&nbsp;50,&nbsp;0,&nbsp;Math.PI/2);</li>
<li>&nbsp;</li>
<li>ctx.lineWidth&nbsp;=&nbsp;10;</li>
<li>ctx.stroke();</li>
</ol></div>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 5vw;"
    onclick="window.open('https://tinyurl.com/y7wuv8vt')"
    src    ="https://tinyurl.com/y95m6q4x"
    alt    ="arc of circle"
    title  ="arc of circle"
  />
</figure>


If we change the last parameter (we omitted it, so it took a value of `false` by default):

<div><ol>
<li value="1">ctx.beginPath();</li>
<li>// we omitted the last parameter</li>
<li>ctx.arc(100,&nbsp;75,&nbsp;50,&nbsp;0,&nbsp;Math.PI/2, <strong>true</strong>);</li>
<li>&nbsp;</li>
<li>ctx.lineWidth&nbsp;=&nbsp;10;</li>
<li>ctx.stroke();</li>
</ol></div>

Then, the result is the "complementary" of the previous arc:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y7wuv8vt')"
    src    ="https://tinyurl.com/ycpj7h8g"
    alt    ="complementary of previous arc is drawn"
    title  ="complementary of previous arc is drawn"
  />
</figure>



__Example #2: drawing a Full circle (filled + outlined)__

Try this [example](https://jsbin.com/juvicubata/edit?html,output): ([Local Example - Circle](src/3.4.8-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y7wuv8vt')"
    src    ="https://tinyurl.com/ybn6755f"
    alt    ="full circle outlined"
    title  ="full circle outlined"
  />
</figure>


Source code:

<div><ol>
<li value="1">var canvas = document.getElementById("myCanvas");</li>
<li>var ctx = canvas.getContext("2d");</li>
<li>var centerX = canvas.width / 2;</li>
<li>var centerY = canvas.height / 2;</li>
<li>var radius = 70;</li>
<li> </li>
<li><strong> ctx.beginPath();</strong></li>
<li> </li>
<li>// Add to the path a full circle (from 0 to 2PI)</li>
<li><strong> ctx.arc(centerX, centerY, radius, 0, 2*Math.PI, false);</strong></li>
<li> </li>
<li>// With path drawing you can change the context</li>
<li>// properties until a call to stroke() or fill() is performed</li>
<li> ctx.fillStyle = "lightBlue";</li>
<li>// Draws the filled circle in light blue</li>
<li><strong> ctx.fill();</strong></li>
<li> </li>
<li> // Prepare for the outline</li>
<li> ctx.lineWidth = 5;</li>
<li> ctx.strokeStyle = "black";</li>
<li> </li>
<li>// draws the path (the circle) AGAIN, this</li>
<li>// time in wireframe</li>
<li><strong> ctx.stroke();</strong></li>
<li> </li>
<li><strong>// Notice we called ctx.arc() only once ! And drew it twice </strong></li>
<li><strong>// with different styles</strong></li>
</ol></div>

Notice that we called `ctx.arc()` only once! And drew it twice, with different styles, with calls to `ctx.stroke()` and `ctx.fill().` Each call drew the defined path in wireframe and in filled mode!


#### Proposed projects

__Project #1: modify the [previous example](https://jsbin.com/gaseramuse/edit?html,output) in order to get:__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y7wuv8vt')"
    src    ="https://tinyurl.com/ya6ox87h"
    alt    ="half circle"
    title  ="half circle"
  />
</figure>


__Project #2: make a small program that draws a smiling head like this (or make something better!)__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y7wuv8vt')"
    src    ="https://tinyurl.com/ybqwpf2p"
    alt    ="smiling head"
    title  ="smiling head"
  />
</figure>


#### Knowledge check 3.4.8

<pre>ctx.beginPath();
ctx.moveTo(100, 100);
ctx.lineTo(200, 200);

ctx.arc(500, 500, 100, 0, 2*Math.PI);
ctx.stroke();
</pre>

1. Will the circle above be "connected" to the last extremity of the line drawn from (100, 100) to (200, 200)? (Yes/No)

  Ans: <span style="color: magenta;">Yes, xNo<br/>
  Explanation: 
    + Indeed, arcs and lines are working in "path mode", so the final drawing produced by the above code will show a line going from (100, 100) to (200, 200), then another line that goes from (200, 200) to the first pixel of the circle outline (corresponding to the arc at angle=0: 100 pixels to the right of the circle center), and the circle of radius = 100, centered in (500, 500). In order to avoid having this line, the easiest solution would be to use TWO paths here. Insert `ctx.stroke()`; `ctx.beginPath()` in the blank line in the code above and you will get a line and a circle, disconnected.
    + Another possibility would be to add the blank line ctx.moveTo(600, 500); without an extra `ctx.beginPath()`. In this case, the "pencil would jump" to the position where the circle starts being drawn (500, 500) + add the horizontal radius to the x pos, giving (600, 500).


### 3.4.9 Drawing rounded rectangles

There is another method called `ctx.arcTo(x1, y1, x2, y2, radius)`, which is a bit complex to use, but very practical for drawing rounded rectangles.

In fact, the `arcTo(...)` method draws an arc of a circle depending on some tangents. Let's look at these pictures for a better understanding (from [this original picture](http://www.dbp-consulting.com/tutorials/canvas/CanvasArcTo.html)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y9gy7o2d')"
    src    ="https://tinyurl.com/ycz22yx5"
    alt    ="arcTo coordinates"
    title  ="arcTo coordinates"
  />
</figure>



#### Typical use

<div><ol>
<li value="1">ctx.moveTo(x0, y0);</li>
<li> </li>
<li>ctx.arcTo(x1, y1, x2, y2, radius);</li>
</ol></div>

This method can be confusing. It was defined mainly for drawing rounded shapes like rounded rectangles. We used an excerpt here from the excellent [tutorial on the arcTo(...) method](http://www.dbp-consulting.com/tutorials/canvas/CanvasArcTo.html).

It works like this:

1. Draw an imaginary line through `(x0,y0)` and `(x1,y1)`, draw another imaginary line through `(x1,y1)` and `(x2,y2)`,
1. Take an imaginary circle of radius r, and slide it up between the two lines until it just touches both lines. The two points at which the circle touches the lines are called the tangent points.
1. `arcTo(x1, y1, x2, y2, r)` will draw a line from the current point `(x0,y0)` to the first tangent point on the line from `(x0,y0)` to `(x1,y1)`,
1. It will also draw an arc from that tangent point to the other tangent point on the line from `(x1,y1)` to `(x2,y2)` along the circumference of the circle.
1. Finally, it adds the tangent point where the arc ends up, on the line from `(x1,y1)` to `(x2,y2)` to the path as the new current point on the path.



#### Examples

__Example #1: simple use__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y9gy7o2d')"
    src    ="https://tinyurl.com/ycfsntdg"
    alt    ="arcTO example 1"
    title  ="arcTO example 1"
  />
</figure>


Try this [interactive example](https://jsbin.com/hagozisiba/1/edit?html,output): ([Local Example - Simple Use](src/3.4.9-example1.html))

<div><ol>
<li value="1">context.beginPath();</li>
<li>context.moveTo(0, 20);</li>
<li>context.arcTo(100, 100, 200, 20, 50);</li>
<li> </li>
<li>context.lineWidth = 5;</li>
<li>context.strokeStyle = "#0000ff";</li>
<li>context.stroke();</li>
</ol></div>


__Example #2: draw A rounded rectangle__

Try this [interactive example](https://jsbin.com/vomuqaseti/1/edit?html,output):  ([Local Example - Rounded Rectangle](src/3.4.9-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y9gy7o2d')"
    src    ="https://tinyurl.com/y8succvf"
    alt    ="rounded rectangle"
    title  ="rounded rectangle"
  />
</figure>


Source code:

<div><ol>
<li value="1">var roundedRect=function(ctx,x,y,width,height,radius,fill,stroke) {</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li></li>
<li>&nbsp; &nbsp;// draw top and top right corner</li>
<li>&nbsp; &nbsp;ctx.moveTo(x+radius,y);</li>
<li>&nbsp; &nbsp;ctx.arcTo(x+width,y,x+width,y+radius,radius);</li>
<li>&nbsp; &nbsp;// draw right side and bottom right corner</li>
<li>&nbsp; &nbsp;ctx.arcTo(x+width,y+height,x+width-radius,y+height,radius);</li>
<li>&nbsp; &nbsp;// draw bottom and bottom left corner</li>
<li>&nbsp; &nbsp;ctx.arcTo(x,y+height,x,y+height-radius,radius);</li>
<li>&nbsp; &nbsp;// draw left and top left corner</li>
<li>&nbsp; &nbsp;ctx.arcTo(x,y,x+radius,y,radius);</li>
<li></li>
<li>&nbsp; &nbsp;if(fill) {</li>
<li>&nbsp; &nbsp; &nbsp; ctx.fill();</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;if(stroke){</li>
<li>&nbsp; &nbsp; &nbsp; ctx.stroke();</li>
<li>&nbsp; &nbsp;}</li>
<li>} </li>
<li> </li>
<li>var canvas&nbsp;=&nbsp;document.getElementById('myCanvas');</li>
<li>var ctx &nbsp; &nbsp;=&nbsp;canvas.getContext('2d');</li>
<li> </li>
<li>ctx.strokeStyle&nbsp;=&nbsp;'rgb(150,0,0)';</li>
<li>ctx.fillStyle &nbsp;&nbsp;=&nbsp;'rgb(0,150,0)';</li>
<li>ctx.lineWidth &nbsp;&nbsp;=&nbsp;7;</li>
<li></li>
<li>roundedRect(ctx,&nbsp;15,&nbsp;15,&nbsp;160,&nbsp;120,&nbsp;20,&nbsp;true,&nbsp;true);</li>
</ol></div>

In this example, each call to `ctx.arcTo(...)` draws a side plus a corner. This makes us suspect that the arcTo() method has been designed primarily for drawing rounded rectangles...


__Example #3: comparison between lineTo and arcTo__

This example at JS Bin is the same as the previous one, except that we added at the end of the roundedRect function the same lines of code that draw the rounded rectangle, but using lineTo instead of arcTo. Just take a look!

[JSBin example](https://jsbin.com/wavizucule/1/edit?html,console,output) ([Local Example - LineTo vs. arcTo](src/3.4.9-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y9gy7o2d')"
    src    ="https://tinyurl.com/yc6ym2wt"
    alt    ="lineTo vs arcTo"
    title  ="lineTo vs arcTo"
  />
</figure>


__Example #4: use the unrounded vertices in arcTo__

For drawing a rounded square, this code also works:

<div><ol>
<li value="1">ctx.moveTo(x+radius,&nbsp;y);</li>
<li>ctx.arcTo(x+width,&nbsp;y,x+width,&nbsp;y+height,&nbsp;radius);</li>
<li>ctx.arcTo(x+width,&nbsp;y+height,&nbsp;x,&nbsp;y+height,&nbsp;radius);&nbsp;</li>
<li>ctx.arcTo(x,&nbsp;y+height,&nbsp;x,&nbsp;y,radius);</li>
<li>ctx.arcTo(x,&nbsp;y,&nbsp;x+width,&nbsp;y,radius);</li>
</ol></div>

which might be easier than trying to figure out where the arc will end like this:

<div><ol>
<li value="1">ctx.moveTo(x+radius,&nbsp;y);</li>
<li>ctx.arcTo(x+width,&nbsp;y,&nbsp;x+width,&nbsp;y+radius,&nbsp;radius);</li>
<li>ctx.arcTo(x+width,&nbsp;y+height,&nbsp;x+width-radius,&nbsp;y+height,radius);&nbsp;</li>
<li>ctx.arcTo(x,&nbsp;y+height,&nbsp;x,&nbsp;y+height-radius,&nbsp;radius);</li>
<li>ctx.arcTo(x,&nbsp;y,&nbsp;x+radius,&nbsp;y,radius);</li>
</ol></div>

This could be particularly helpful if you are dealing with something other than a rectangle, like this rounded triangle ([try the code at JsBin](https://jsbin.com/depaxoxexi/edit?html,output)): ([Local Example - Triangle](src/3.4.9-example4.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y9gy7o2d')"
    src    ="https://tinyurl.com/yask5w9x"
    alt    ="rounded triangle"
    title  ="rounded triangle"
  />
</figure>


### 3.4.10 Quadratic curves

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://www.html5canvastutorials.com/tutorials/html5-canvas-quadratic-curves/')"
    src    ="https://tinyurl.com/y93lpz8k"
    alt    ="quadratic curve"
    title  ="quadratic curve"
  />
</figure>

(Picture taken from the [HTML5 Canvas Tutorials Web site](https://www.html5canvastutorials.com/tutorials/html5-canvas-quadratic-curves/))


#### Introduction

Quadratic curves are defined by a starting point (called a "context point"), a control point, and an ending point. The curve fits the tangents between the context and control points and between the control and ending points.

The context point may be defined by a call to the `moveTo(x, y)` method of the context, or it may be the ending point of a previous path, if we're drawing a path made of several shapes. For example, drawing a line and a quadratic curve will make the endpoint of the line the context point for the quadratic curve.

The control point controls the curvature - if we move the control point farther we get a sharper curve.


#### Typical use

<div><ol>
<li value="1">context.moveTo(contextX, contextY);</li>
<li>context.quadraticCurveTo(controlX, controlY, endX, endY);</li>
<li>// Optional : set lineWidth and stroke color</li>
<li><span style="line-height: 23.2727279663086px;">context</span>.lineWidth = 5;</li>
<li><span style="line-height: 23.2727279663086px; background-color: #eeeeee;">context</span>.strokeStyle = "#0000ff";</li>
<li>// Draw!</li>
<li><span style="line-height: 23.2727279663086px; background-color: #eeeeee;">context</span>.stroke(); </li>
</ol></div>


#### Examples

__Example #1: quadratic curve__

Try this [interactive example](https://jsbin.com/zabefafuge/1/edit?html,output): ([Local Example - Quadratic Curve](src/3.4.10-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yaxrn3tc')"
    src    ="https://tinyurl.com/yac2vax7"
    alt    ="quadratic curve example 1"
    title  ="quadratic curve example 1"
  />
</figure>


Source code:

<div><ol>
<li value="1">var canvas=document.querySelector('#myCanvas1');</li>
<li>var context=canvas.getContext('2d');</li>
<li>&nbsp;</li>
<li>context.beginPath();</li>
<li>&nbsp;</li>
<li>context.moveTo(100, 20);</li>
<li>context.quadraticCurveTo(230, 200, 250, 20);</li>
<li>&nbsp;</li>
<li>context.lineWidth = 5;</li>
<li>context.strokeStyle = "#0000ff";</li>
<li>context.stroke();</li>
</ol></div>

We set a starting point in line 6: `moveTo(...)`, then set the control and ending points with a call to `quadraticCurve(...)`, at line 7, then set some properties for color, thickness, and finally we call the `stroke()` method for drawing the curve.


__Example #2: lines connected with a quadratic curve__

Try this [interactive example](https://jsbin.com/sahemetere/1/edit?html,output): ([Local Example - Connect w/ Quadratic curve](src/3.4.10-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yaxrn3tc')"
    src    ="https://tinyurl.com/y77fqa6y"
    alt    ="a line followed by a curve followed by a curve"
    title  ="a line followed by a curve followed by a curve"
  />
</figure>


Source code:

<div><ol>
<li value="1">context.beginPath();</li>
<li> </li>
<li>context.moveTo(100, 20);</li>
<li>context.lineTo(200, 80);</li>
<li>context.quadraticCurveTo(230, 200, 250, 20);</li>
<li>context.lineTo(500, 90);</li>
<li> </li>
<li>context.lineWidth = 5;</li>
<li>context.strokeStyle = "#0000ff";</li>
<li>context.stroke();</li>
</ol></div>


### 3.4.11 Curved arrows

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y7ufmzdv')"
    src    ="https://tinyurl.com/yc7e3h3g"
    alt    ="curved arrow"
    title  ="curved arrow"
  />
</figure>

See the [example online](https://jsbin.com/rehuhudawo/1/edit?html,output) on JsBin. ([Local Example - Curved Arrow](src/3.4.11-example1.html))

We propose a useful function for drawing curved arrows. The code is a modified version of one that has been proposed by several contributors to [this thread at StackOverflow](https://stackoverflow.com/questions/27778951/drawing-an-arrow-on-an-html5-canvas-quadratic-curve).

Source code of the function that draws a curved arrow:

<div><ol>
<li value="1">function drawCurvedArrow(startPointX, startPointY,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;endPointX, endPointY,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;quadPointX, quadPointY,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;lineWidth,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;arrowWidth, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;color) {</li>
<li>&nbsp; &nbsp;&nbsp;// BEST PRACTICE: the function changes color and lineWidth -&gt; save context!</li>
<li>&nbsp; &nbsp; ctx.save();</li>
<li></li>
<li>&nbsp; &nbsp; ctx.strokeStyle = color;</li>
<li>&nbsp; &nbsp; ctx.lineWidth = lineWidth;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// angle of the end tangeant, useful for drawing the arrow head</li>
<li>&nbsp; &nbsp;&nbsp;var arrowAngle = Math.atan2(quadPointX - endPointX, quadPointY - endPointY) + Math.PI;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// start a new path</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #800000;">// Body of the arrow</span></li>
<li>&nbsp; &nbsp; ctx.moveTo(startPointX, startPointY);</li>
<li>&nbsp; &nbsp; ctx.quadraticCurveTo(quadPointX, quadPointY, endPointX, endPointY);</li>
<li></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #800000;">// Head of the arrow</span></li>
<li>&nbsp; &nbsp; ctx.moveTo(endPointX - (arrowWidth * Math.sin(arrowAngle - Math.PI / 6)), </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;endPointY - (arrowWidth * Math.cos(arrowAngle - Math.PI / 6)));</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; ctx.lineTo(endPointX, endPointY);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; ctx.lineTo(endPointX - (arrowWidth * Math.sin(arrowAngle + Math.PI / 6)), </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;endPointY - (arrowWidth * Math.cos(arrowAngle + Math.PI / 6)));</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; ctx.stroke();</li>
<li>&nbsp; &nbsp; ctx.closePath();</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// BEST PRACTICE -&gt; restore the context as we saved it at the beginning</li>
<li>&nbsp; &nbsp;&nbsp;// of the function</li>
<li>&nbsp; &nbsp; ctx.restore();</li>
<li>}</li>
</ol></div>

This function takes as parameters the start and end points, the control point of the curve, the arrow width, the width of the arrow head.

It computes the angle of the arrow at its endpoint (line 14) in order to compute the rotated endpoints of the two lines of the arrow head (lines 24 and 29).

Notice that once again, as we modify the context properties (color, lineWidth) in the body of the function, we save and restore the context at the beginning / end of the function.


### 3.4.12 B&eacute;zier curves

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y8wrd29d')"
    src    ="https://tinyurl.com/yblxspul"
    alt    ="bezier curve in S"
    title  ="bezier curve in S"
  />
</figure>

(image taken from [SitePoint](http://blogs.sitepointstatic.com/examples/tech/canvas-curves/bezier-curve.html))


#### Introduction

B&eacute;zier curves are interesting - used mostly for drawing "S" shapes or asymmetric curves.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y8wrd29d')"
    src    ="https://tinyurl.com/ydzyueee"
    alt    ="bezier curve control points"
    title  ="bezier curve control points"
  />
</figure>


(Picture taken from the [HTML5 Canvas Tutorials Web site](https://www.html5canvastutorials.com/tutorials/html5-canvas-bezier-curves/))

B&eacute;zier curves are defined by a context point, like quadratic curves, two control points that define two tangents, and an ending point.

The first part of the curve is tangential to the imaginary line defined by the context point and the first control point. The second part of the curve is tangential to the imaginary line defined by the second control point and the ending point.

The best way to understand how they work is to check out one of these interactive applications:

+ [Canvas B&eacute;zier Curve Example](http://blogs.sitepointstatic.com/examples/tech/canvas-curves/bezier-curve.html)
+ [IvanK Lib graphics demos](http://lib.ivank.net/?p=demos&d=bezier)
+ Nice video tutorial: [B&eacute;zier curves under the hood](https://vimeo.com/106757336)


#### Typical usage of B&eacute;zier curves

Source code:

<div><ol>
<li value="1">ctx.moveTo(contextX, contextY);</li>
<li>context.bezierCurveTo(controlX1, controlY1, controlX2, controlY2, endX, endY);</li>
<li>// Optional : set lineWidth and stroke color</li>
<li>context.lineWidth = 5;</li>
<li>context.strokeStyle = "#0000ff";</li>
<li>// Draw!</li>
<li>ctx.stroke();</li>
</ol></div>


#### Examples

__Example #1__

Try this [interactive example](https://jsbin.com/jeribimohi/1/edit?html,output): ([Local Example - Curve](src/3.4.12-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y8wrd29d')"
    src    ="https://tinyurl.com/ya6wxkem"
    alt    ="bezier curve example"
    title  ="bezier curve example"
  />
</figure>


<div><ol>
<li value="1">context.beginPath();</li>
<li> </li>
<li>context.moveTo(100, 20);</li>
<li>context.bezierCurveTo(290, -40, 200, 200, 400, 100);</li>
<li> </li>
<li>context.lineWidth = 5;</li>
<li>context.strokeStyle = "#0000ff";</li>
<li>context.stroke();</li>
</ol></div>


__Example #2: with lines, quadratic, and bezier curves in a path__

Try this [example online](https://jsbin.com/nizopekodi/edit?html,output): ([Local Example - Lines, Quadratic, and Bezier Curve](src/3.4.12-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y8wrd29d')"
    src    ="https://tinyurl.com/yd8qao4j"
    alt    ="path with bezier curve, quadratic curve and line in the same, closed path"
    title  ="path with bezier curve, quadratic curve and line in the same, closed path"
  />
</figure>


Extract from source code:

<div><ol>
<li value="1">context.beginPath();</li>
<li> </li>
<li>context.moveTo(100, 20);</li>
<li> </li>
<li>context.lineTo(200, 160);</li>
<li>context.quadraticCurveTo(230, 200, 250, 120);</li>
<li>context.bezierCurveTo(290, -40, 300, 200, 400, 150);</li>
<li>context.lineTo(500, 90);</li>
<li> </li>
<li>// TRY COMMENTING THIS LINE OUT</li>
<li>context.closePath();</li>
<li>context.lineWidth = 5;</li>
<li>context.strokeStyle = "#0000ff";</li>
<li>context.stroke();</li>
</ol></div>

In this example we use the `closePath()` method to draw a line between the last path point and the first path point (line 11), so that the drawing looks like a pair of goggles.

Note how the different parts are linked together and make a "path":

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y8wrd29d')"
    src    ="https://tinyurl.com/y8bgqhpy"
    alt    ="path composition explained"
    title  ="path composition explained"
  />
</figure>


#### Interesting, interactive tool for generating code that draws B&eacute;zier curves

This B&eacute;zier tool ("HTML5 `<canvas>` bezierCurveTo command generator") is available [online](https://www.victoriakirst.com/beziertool/): try it!

Screenshot:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y8wrd29d')"
    src    ="https://tinyurl.com/ybbz6ljz"
    alt    ="bezier curves code generator"
    title  ="bezier curves code generator"
  />
</figure>


### 3.4.13 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ On the Web, please find utility functions for drawing ellipses, stars, polygons, etc. and share them with your fellow students. You can also write some of your own.
+ Do you know tools that help work with curves? Please share them too...


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

__Project 1 (easy)__: Create a small monster using rectangles, arcs, lines, etc. Just drawing a monster head will do the work. Start with something simple: a circle for the head, two squares for the eyes, a line for the mouth, etc., then set some colors and line widths.

__Project 2__: Same as above but make use of patterns.

__Project 3 (harder)__: Try to draw the current image of a video played in background, hidden using CSS, as the animated background of the canvas.

__Project 4 (follow-up of project 3)__: You can also use the trick with the video to create animated textures for the eyes, skin, etc.




