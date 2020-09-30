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




