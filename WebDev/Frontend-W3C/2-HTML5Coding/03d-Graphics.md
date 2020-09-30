# Week 3: HTML5 Graphics

## 3.4 Path drawing mode


### 3.4.0 Lecture Notes

+ [Intermediate mode vs. path mode](#341-immediate-mode-vs-path-mode)
  + intermediate mode
    + executing a call to a drawing method immediately drawing in the canvas
    + as soon as they are executed
      + the results are displayed on screen
      + the drawings are performed
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
  + consecutive calls to ctx.lineTo(x, y): store in the path/buffer a set of connected lines
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

+ [Drawing arrows](#346-drawing-arrows)
  + adapted from [Stackoverflow]( https://stackoverflow.com/questions/808826/draw-arrow-on-canvas-tag)
    + draw an arrow in a single function: `function drawArrow(ctx, fromx, fromy, tox, toy, arrowWidth, color){...}`
    + fixing the head length: `var headlen = 10;`
    + calculate the angle from given the beginning (fromx, fromy1) to the end (arrow) (tox, toy): `var angle = Math.atan2(toy-fromy,tox-fromx);`
    + store/restore the drawings in canvas: `ctx.save()` * `ctx.restor()`
    + draw one line (the arrow body) w/ given width: `ctx.beginPath(); ctx.moveTo(fromx, fromy); ctx.lineTo(tox, toy); ctx.lineWidth = arrowWidth; ctx.stroke();`
    + draw three connected lines (the arrow head)
      + starting a new path from the head of the arrow to one of the sides of the point: `ctx.beginPath(); ctx.moveTo(tox, toy); ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7), toy-headlen*Math.sin(angle-Math.PI/7));`
      + path from the side point of the arrow, to the other side point: `ctx.lineTo(tox-headlen*Math.cos(angle+Math.PI/7), toy-headlen*Math.sin(angle+Math.PI/7));`
      + path from the side point back to the tip of the arrow, and then again to the opposite side point: `ctx.lineTo(tox, toy); ctx.lineTo(tox-headlen*Math.cos(angle-Math.PI/7), toy-headlen*Math.sin(angle-Math.PI/7));`
    + draws the paths created above: `ctx.stroke();`
  + [drawing lines and arcs with arrow heads](http://www.dbp-consulting.com/tutorials/canvas/CanvasArrow.html)




### 3.4.1 Immediate mode vs. path mode


#### Immediate mode = executing a call to a drawing method means immediately drawing in the canvas

In the previous examples, we saw how to draw rectangles using the `fillRect(x, y, width, height)` and `strokeRect(x, y, width, height)` methods of the context.

We also learned how to draw a text message using the `fillText(message, x, y)` and `strokeText(message, x, y)` methods that draws a text in filled and wireframe mode, respectively.

These methods, along with the `drawImage(...)` method already seen in section 3.3.3, are "immediate methods": as soon as they are executed, the results are displayed on screen, the drawings are performed, pixels on the canvas area change their colors, etc.

Here is a code extract that will draw 1000 random rectangles in a canvas, using immediate mode rectangle drawing calls.


[Online example](https://jsbin.com/yenuvikuno/1/edit?html,output): ([Local Example - Random Rectangles](src/3.4.1-example1.html))

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; w </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; h </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">time</span><span class="pun">(</span><span class="str">"time to draw"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> w</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> h</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> width </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> w</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> height </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> h</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">timeEnd</span><span class="pun">(</span><span class="str">"time to draw"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> w</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> h</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> width </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> w</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> height </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> h</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">rect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">); // store&nbsp;a rectangle in path/buffer</span></strong><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">(); // draws the whole buffer (the 1000 rectangles) at once</span></strong></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// start a new buffer / path</span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// all these orders are in a buffer/path</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw the buffer</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Vertical lines</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0.5</span><span class="pun">;</span><span class="pln"> x </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">500</span><span class="pun">;</span><span class="pln"> x </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> </span><span class="lit">375</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">// Horizontal lines</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0.5</span><span class="pun">;</span><span class="pln"> y </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">375</span><span class="pun">;</span><span class="pln"> y </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">500</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// Draw in blue</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#0000FF"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// Until the execution of the next line, nothing has been drawn!</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span><span class="pln"> </span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// a filled rectangle in immediate mode</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'#FF0000'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// two consecutive lines in path mode</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// draws only the two lines in wireframe mode</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#0000FF"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
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


<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// first part of the path</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// second part of the path, moveTo(...) is used to "jump" to another place</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">120</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// indicate stroke color + draw the path</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#0000FF"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// first part of the path</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// indicate stroke color + draw first part of the path</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#0000FF"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// second part of the path</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">120</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// indicate stroke color + draw the path</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"pink"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">();</span></li>
</ol></div>


Hey - it does not work! Weirdly, the two parts of the path are filled in pink! But we called `stroke()` after the first half of the path was drawn (lines 5-8). Then we called `fill()` only after the second part of the path was specified (lines 14-19)... so, what happened?

Remember that fill() or stroke() draws the whole path, even if it is disconnected, and even if it has already been drawn!

What happened is:

+ The call to `stroke()` has drawn the path corresponding to the lines 5-7. Indeed, the first part of the path (on the left) has actually been drawn once in wireframe mode, and in blue.
+ Then, the call to `fill()` at line 20 has drawn the whole path again, but in pink and in filled mode. But this time the path corresponds to lines 5-7 plus lines 14-16 that make up the second shape on the right. So the path that has been drawn this time is made of both of the triangles.

<div style="border: 1px solid red; padding: 20px;">
<p style="text-align: center;"><strong>Important</strong>: If you do not want to draw parts of the same path several times, you need to draw two different paths, <br>using the <span style="font-family: 'courier new', courier;">ctx.beginPath()</span> method, as shown in the next example.</p>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// first part of the path</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// indicate stroke color + draw first part of the path</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"#0000FF"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="com">// start a new path, empty the current buffer</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span style="color: #ffff00;"><strong><span class="pln">ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></strong></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// second part of the path</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">120</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="lit">200</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">// indicate stroke color + draw the path</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"pink"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">();</span></li>
</ol></div>

This time, in order to draw the two shapes differently, we defined two separate paths. The way to do this is just to call `ctx.beginPath()` to start a new path. In this example, the first path has been drawn in wireframe mode, then a new path has been started that is drawn in filled mode.


#### Knowledge check 3.4.4

1. We must call ctx.beginPath() before drawing any new path, but what does it do exactly?<br/>

  a. It will empty the current path (reset the buffer of drawing orders), but it will not change the context properties.<br/>
  b. It will reset all properties of the graphic context.<br/>

  Ans: a<br/>
  Explanation: Indeed, calling `ctx.beginPath()` will erase the buffer but will not change any context properties. This method is useful for starting a new path.


### 3.4.5 Drawing lines in immediate mode

Sometimes, it might be useful to draw just one line without being in another path.

It's interesting to see how we can write a single "draw line" function that takes the start and end coordinates, the color, the line width, etc.

Here is the code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawLine</span><span class="pun">(</span><span class="pln">x1</span><span class="pun">,</span><span class="pln"> y1</span><span class="pun">,</span><span class="pln"> x2</span><span class="pun">,</span><span class="pln"> y2</span><span class="pun">,</span><span class="pln"> color</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com">// set color and lineWidth, if these parameters</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// are not defined, do nothing (default values)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">color</span><span class="pun">)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> color</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">width</span><span class="pun">)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> width</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// start a new path</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="pln">x1</span><span class="pun">,</span><span class="pln"> y1</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">x2</span><span class="pun">,</span><span class="pln"> y2</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Notice the save/restore of the context at the beginning/end of the function. This is a REALLY good practice to avoid affecting other functions' context.

+ _Line 13_ starts a new path so that the function will only draw what it is meant to draw: a single line.
+ _Lines 15-17_ move the "pen" at (x1, y1) then draw a line to (x2, y2), and the stroke at _line 17_ makes it appear on the screen.

Here is an example (see [online example](https://jsbin.com/soferaraya/edit?html,output)): ([Local Example - 3 Lines](src/3.4.5-example1.html))

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> drawLine</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> drawLine</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">,</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> drawLine</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Adapted from : https://stackoverflow.com/questions/808826/draw-arrow-on-canvas-tag</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> drawArrow</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">,</span><span class="pln"> fromx</span><span class="pun">,</span><span class="pln"> fromy</span><span class="pun">,</span><span class="pln"> tox</span><span class="pun">,</span><span class="pln"> toy</span><span class="pun">,</span><span class="pln"> arrowWidth</span><span class="pun">,</span><span class="pln"> color</span><span class="pun">){</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//variables to be used when creating the arrow</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> headlen </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> angle </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">atan2</span><span class="pun">(</span><span class="pln">toy</span><span class="pun">-</span><span class="pln">fromy</span><span class="pun">,</span><span class="pln">tox</span><span class="pun">-</span><span class="pln">fromx</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> color</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//starting path of the arrow from the start square to the end square </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; //and drawing the stroke</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="pln">fromx</span><span class="pun">,</span><span class="pln"> fromy</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">tox</span><span class="pun">,</span><span class="pln"> toy</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> arrowWidth</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//starting a new path from the head of the arrow to one of the sides of </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; //the point</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="pln">tox</span><span class="pun">,</span><span class="pln"> toy</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">tox</span><span class="pun">-</span><span class="pln">headlen</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">cos</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">-</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">7</span><span class="pun">),</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;toy</span><span class="pun">-</span><span class="pln">headlen</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sin</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">-</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">7</span><span class="pun">));</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//path from the side point of the arrow, to the other side point</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">tox</span><span class="pun">-</span><span class="pln">headlen</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">cos</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">7</span><span class="pun">),</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;toy</span><span class="pun">-</span><span class="pln">headlen</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sin</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">+</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">7</span><span class="pun">));</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//path from the side point back to the tip of the arrow, and then </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; //again to the opposite side point</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">tox</span><span class="pun">,</span><span class="pln"> toy</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">tox</span><span class="pun">-</span><span class="pln">headlen</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">cos</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">-</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">7</span><span class="pun">),</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;toy</span><span class="pun">-</span><span class="pln">headlen</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">sin</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">-</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">7</span><span class="pun">));</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">//draws the paths created above</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

An arrow is made of one line (the arrow body) and three connected lines (the arrow head). 

As we modify some context properties in this function, we call `save()` and `restore()` at the beginning and at the end of the function.

This function can be improved in many ways: adding shadows, using `fill()` instead of `stroke()`, which gives strange results when the width is too big, etc.


__Example #2__

[Online example](https://jsbin.com/lebutokage/2/edit?html,output) that uses the above code: ([Local Example - Arrows](src/3.4.6-example1.html))

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> drawArrow</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> drawArrow</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">140</span><span class="pun">,</span><span class="pln"> </span><span class="lit">140</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="str">'black'</span><span class="pun">);</span></li>
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




