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
          <img style="margin: 0.1em;" width=20vw
            src    ="https://tinyurl.com/yxa5jg2k"
            alt    ="text baseline"
            title  ="text baseline"
          >
          <img style="margin: 0.1em;" width=20vw
            src    ="https://tinyurl.com/y2kwbxfo"
            alt    ="horizontal text alignment"
            title  ="horizontal text alignment"
          >
        </a>
      </div>







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
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;style&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="com">#myCanvas {</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/style&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln"></span><span class="tag"></span><span class="tag">&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// black rectangle, default color (black)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// outlined rectangle, default color</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// outlined rectangle filled in red, outline blue</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'lightBlue'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// A function to automatize previous drawing</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> angle </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI </span><span class="pun">/</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>drawFilledRectangle</span><span class="pun">(</span><span class="lit">300</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="str">'pink'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>drawFilledRectangle</span><span class="pun">(</span><span class="lit">300</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'purple'</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> angle </span><span class="pun">+</span><span class="pln"> </span><span class="lit">0.5</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="kwd">function</span><span class="pln"> drawFilledRectangle</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">,</span><span class="pln"> fillColor</span><span class="pun">,</span><span class="pln"> strokeColor</span><span class="pun">,</span><span class="pln"> lw</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// BEST PRACTICE : save if the function change the context or coordinate </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// system</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// position coordinate system</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// set colors, line width...</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> lw</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> fillColor</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> strokeColor</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// draw at 0, 0 as we translated the coordinate</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// system already</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// BEST PRACTICE : a restore for a save!</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp; </span><span class="tag"></span></span></span></span>ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"578"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"60pt Calibri"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// .. set color, lineWidth, shadow etc.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// 10, 10 is the start of the baseline, bottom of left leg of the "H" in the </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// "Hello World" example.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// Or</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">);</span></li>
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
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> x</span><span class="pun">,</span><span class="pln"> y</span><span class="pln">&nbsp;</span><span class="pun">[,</span><span class="pln"> maxWidth</span><span class="pun">]);</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> x</span><span class="pun">,</span><span class="pln"> y</span><span class="pln">&nbsp;</span><span class="pun">[,</span><span class="pln"> maxWidth</span><span class="pun">]);</span><span class="pln"> </span></li>
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
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"60pt Calibri"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"red"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw text with constrained width of 250 pixels</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">160</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">250</span></strong><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">160</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">250</span></strong><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Constrain width to 150 pixels</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">220</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">150</span></strong><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">220</span><span class="pun">,</span><span class="pln"> </span><strong><span class="lit">150</span></strong><span class="pun">);</span></li>
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
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"60pt Calibri"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"red"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">strokeText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> textMetrics </span><span class="pun">=</span><span class="pln"> context</span><span class="pun">.</span><span class="pln">measureText</span><span class="pun">(</span><span class="str">"Hello World!"</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> width </span><span class="pun">=</span><span class="pln"> textMetrics</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// Draw a text that displays the width of the previous drawn text</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"20pt Arial"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Width of previous text: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> width </span><span class="pun">+</span><span class="pln"> </span><span class="str">"pixels"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw the baseline of the given width</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">width</span><span class="pun">+</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> context</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
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
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textBaseline </span><span class="pun">=</span><span class="pln"> </span><span class="str">"top"</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"top"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">75</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textBaseline </span><span class="pun">=</span><span class="pln"> </span><span class="str">"hanging"</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"hanging"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">,</span><span class="pln"> </span><span class="lit">75</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textBaseline </span><span class="pun">=</span><span class="pln"> </span><span class="str">"middle"</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"middle"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">120</span><span class="pun">,</span><span class="pln"> </span><span class="lit">75</span><span class="pun">);</span></li>
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
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"center"</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"center"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"start"</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"start"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"end"</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"end"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">60</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"left"</span><span class="pun">;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"left"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">80</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">context</span><span class="pun">.</span><span class="pln">textAlign </span><span class="pun">=</span><span class="pln"> </span><span class="str">"right"</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">context</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"right"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
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







