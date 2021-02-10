# Module 2: Adding interactivity to HTML documents


## 2.6 Let's write a small game

### 2.6.1 Drawing

<a href="https://edx-video.net/W3CxJS.0x-V000100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/ynysboc7)

The HTML5 canvas is a transparent element that is useful for drawing and animating. We'll see some simple examples here, as we're going to finish this week by writing a small, simple game together, that will use most of what we've learnt so far: loops, conditional statements, events, functions, callbacks, simple objects, a few input fields, etc.

A typical HTML code for adding a canvas to a Web page:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;title&gt;</span><span class="pln">Draw a monster in a canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"200"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

The canvas declaration is at _line 8_. Use attributes to give it a `width` and a `height`, but unless you add some CSS properties, you will not see it on the screen because it's transparent!

Let's use CSS to reveal the canvas, for example, add a 1px black border around it:

<div class="source-code" style="margin: 0px; padding: 0px 30px; border: 1px solid black;"><ol class="linenums">
<li class="L0" style="font-family: 'Courier New';" value="1"><span class="pln">canvas&nbsp;</span><span class="pun">{</span></li>
<li class="L1" style="font-family: 'Courier New';"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln">&nbsp;</span><span class="lit">1px</span><span class="pln">&nbsp;solid black</span><span class="pun">;</span></li>
<li class="L2" style="font-family: 'Courier New';"><span class="pun">}</span></li>
</ol></div>

And here is a reminder of best practices when using the canvas:

1. __Use a function that is called AFTER the page is fully loaded__ (and the DOM is ready), select the canvas in the DOM (this is the init function (as in window.onload = init) we already saw many times).
2. __Then, get a 2D graphic context for this canvas__ (the context is an object we will use to draw on the canvas, to set global properties such as color, gradients, patterns and line width).
3. __Only then can you can draw something.__
4. __Do not forget to use global variables for the canvas and context objects.__ I also recommend keeping the width and height of the canvas somewhere. These might be useful later.
5. __For each function that will change the context (color, line width, coordinate system, etc.), start by saving the context, and end by restoring it.__


#### Examples

__Example #1: some drawing examples (wireframe and filled rectangle, filled circle, filled text, changing colors)__

[CodePen Demo](https://codepen.io/w3devcampus/pen/PpLOQw)

[Local Demo](src/02f-example01.html)

Extract from the JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// useful to have them as global variables</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // called AFTER the page has been loaded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>canvas </strong></span><strong><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // important, we will draw with this object</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>ctx </strong></span><strong><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // ready to go! We can use the context for drawing</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; // or changing colors, line widths, etc.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // filled rectangle</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // wireframe rectangle</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">4</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong> ctx</strong></span><strong><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">,</span><span class="pln"> </span><span class="lit">40</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // fill circle, will use current ctx.fillStyle</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">arc</span><span class="pun">(</span><span class="lit">60</span><span class="pun">,</span><span class="pln"> </span><span class="lit">60</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fill</span><span class="pun">(); // or ctx.stroke() for a wireframe circle</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // some text</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">"purple"</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">"20px Arial"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong> ctx</strong></span><strong><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"Hello!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">60</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">); // or ctx.strokeText for wireframe</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Explanations:__

1. We use a function (_line 4_) called after the page is loaded (we say "after the DOM is ready"), so that the `querySelector` at _line 6_ will return the canvas.  If the page was not completely loaded and if this code had been run before it had finished loading, the canvas value would have been "undefined".
1. Once we have the canvas, we request a "graphic context" (_line 8_). This is a variable for 2D or 3D  drawing on a canvas (in our case: 2D!) that we will use for drawing or setting colors, line widths, text fonts, etc.
1. Then we can draw. Here we show only a few things you can do with the canvas API, but believe me, you can do much more (draw images, gradients, textures, etc.)!
1. At _line 15_, we draw a filled rectangle. Parameters are the x and y coordinates of the top left corner (x goes to the right, y to the bottom of your screen), and the width and the height of the rectangle. At __line 14__, we used the fillStyle property of the context to set the color of filled shapes. This means: "now, all filled shapes you are going to draw will be in red!". It's like a global setting.
1. _Lines 17-20_ draw a green wireframe rectangle, with a line width equal to 4 pixels. Notice the use of "stroke" instead of "fill" in the property name `strokeStyle/fillStyle` and in the context method for drawing a rectangle `strokeRect/fillRect`.
1. _Lines 23-25_ draw a filled circle. The syntax is a bit different as circles are parts of a "path" (see the HTML5 fundamentals course, we explain the concept of "path" in the canvas API). Just keep in mind for now that before drawing a circle you need to call `beginPath()`. The call to `arc(x, y, radius, start_angle, end_angle)` does not draw the circle, it defines it. The next instruction `ctx.fill()` at line 25 will draw all shapes that have been defined since a new path began, as filled shapes. Calling ctx.stroke() here, instead of `ctx.fill()` would have drawn a wireframe circle instead of a filled one. Also note that the filled circle is red even if we did not specify the color. Remember that we set ctx.fillStyle = 'red' at _line 14_. Unless we change this, all filled shapes will be red.
1. _Lines 28-30_ draw a filled text. The call to `filltext(message, x, y)` draws a filled text at the x,y position; this time in purple as we called `ctx.fillStyle='purple'` before calling `fillText(...)`


__Example #2: functions that save and restore the context before drawing__

[CodepPen Demo](https://codepen.io/w3devcampus/pen/EWMbmE)

[Local Demo](src/02f-example02.html)

__Explanations:__

This time we've written two functions for a cleaner code: one function that draws a filled rectangle with a given color, and one function that draws a filled circle, with a given color.

The values for `x`, `y`, `width`, `height`, `radius`, `color` can be passed as parameters to these functions.

When a function changes anything to the "global context": filled or stroke color, line width, or the position of the coordinate system (located by default in 0, 0, at the top left of the canvas), then it is good practice to save this context at the beginning of the function, with a call to `ctx.save()`, and to restore it at the end of the function, with a call to `ctx.restore()`. In this way, any change to the "global context" won't have any effect outside of the function.

We used also `ctx.translate(x, y)` in order to move the rectangle and the circle (look, they have been drawn at x=0, y=0, but as we translate the origin of the coordinate system with `ctx.translate`, the shapes are located in x, y on in the canvas). This is also a good practice: indeed, if we add more shapes (like eyes in the rectangle, in order to draw a monster), using coordinates relative to 0, 0, the whole set of shapes will be translated by the call to `ctx.translate(x, y)`. This will make it easier to draw characters, monsters, etc. as we will see in a third example.


__Example #3: draw a monster instead of a simple rectangle or circle__

This is where you reap the benefits of your good habits of saving/restoring the context and using `ctx.translate(x, y)`!

[CodePen Demo](https://codepen.io/w3devcampus/pen/aJMMzL)

[Local Demo](src/02f-example03.html)

Here is JavaScript code that implements these best practices:

<div class="source-code" style="padding: 0px 30px; border: 1px solid black; line-height: 1.4em;"><ol class="linenums">
<li class="L0" style="font-family: 'Courier New';" value="1"><span class="com">// useful to have them as global variables</span></li>
<li class="L1" style="font-family: 'Courier New';"><span class="kwd">var</span><span class="pln">&nbsp;canvas</span><span class="pun">,</span><span class="pln">&nbsp;<g class="gr_ gr_126 gr-alert gr_spell gr_disable_anim_appear ContextualSpelling ins-del multiReplace" id="126" style=" line-height: 1.4em;" data-gr-id="126">ctx</g></span><span class="pun">,</span><span class="pln">&nbsp;w</span><span class="pun">,</span><span class="pln">&nbsp;h</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L2" style="font-family: 'Courier New';"><span class="pln">&nbsp;</span></li>
<li class="L4" style="font-family: 'Courier New';"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="kwd">function</span><span class="pln">&nbsp;init</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L5" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Called AFTER the page has been loaded</span></li>
<li class="L6" style="font-family: 'Courier New';"><span class="pln">&nbsp; canvas&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str" style="color: #008800;">"#myCanvas"</span><span class="pun">);</span></li>
<li class="L7" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L8" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Often useful</span></li>
<li class="L9" style="font-family: 'Courier New';list-style-type: decimal !important;"><span class="pln">&nbsp; w&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L0" style="font-family: 'Courier New';"><span class="pln">&nbsp; h&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L1" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L2" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Important, we will draw with this object</span></li>
<li class="L3" style="font-family: 'Courier New';"><span class="pln">&nbsp; ctx&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str" style="color: #008800;">'2d'</span><span class="pun">);</span></li>
<li class="L4" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L5" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Ready to go!</span></li>
<li class="L6" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Try to change the parameter values to move</span></li>
<li class="L7" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// the monster</span></li>
<li class="L8" style="font-family: 'Courier New';"><span class="pln">&nbsp; drawMyMonster</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">); <strong>// try to change that</strong></span></li>
<li class="L9" style="font-family: 'Courier New';list-style-type: decimal !important;"><span class="pun">};</span></li>
<li class="L0" style="font-family: 'Courier New';"><span class="pln">&nbsp;</span></li>
<li class="L1" style="font-family: 'Courier New';"><span class="kwd">function</span><span class="pln">&nbsp;drawMyMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln">&nbsp;y</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L2" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Draw a big monster!</span></li>
<li class="L3" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Head</span></li>
<li class="L4" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L5" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// BEST practice: save the context, use 2D transformations</span></strong></li>
<li class="L6" style="font-family: 'Courier New';"><strong><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></strong></li>
<li class="L7" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L8" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// Translate the coordinate system, draw relative to it</span></strong></li>
<li class="L9" style="font-family: 'Courier New';list-style-type: decimal !important;"><strong><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln">&nbsp;y</span><span class="pun">);</span></strong></li>
<li class="L0" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L1" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// (0, 0) is the top left corner of the monster.</span></li>
<li class="L2" style="font-family: 'Courier New';"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><strong><span class="lit">0</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">0</span></strong><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">100</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L3" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L4" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Eyes</span></li>
<li class="L5" style="font-family: 'Courier New';"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">20</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">20</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L6" style="font-family: 'Courier New';"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">65</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">20</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L7" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L8" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Nose</span></li>
<li class="L9" style="font-family: 'Courier New';list-style-type: decimal !important;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">45</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">40</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">40</span><span class="pun">);</span></li>
<li class="L0" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L1" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Mouth</span></li>
<li class="L2" style="font-family: 'Courier New';"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">35</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">84</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">30</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L3" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L4" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Teeth</span></li>
<li class="L5" style="font-family: 'Courier New';"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">38</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">84</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L6" style="font-family: 'Courier New';"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">52</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">84</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L7" style="font-family: 'Courier New';"><span class="pln"></span></li>
<li class="L8" style="font-family: 'Courier New';"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// BEST practice: restore the context</span></strong></li>
<li class="L9" style="font-family: 'Courier New';list-style-type: decimal !important;"><span class="pln">&nbsp; <strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></strong></li>
<li class="L0" style="font-family: 'Courier New';"><span class="pun">}</span></li>
</ol></div>


In this small example, we used the context object to draw a monster using the default color (black) and wireframe and filled modes:

+ `ctx.fillRect(x, y, width, height)`: draws a rectangle whose top left corner is at (x, y) and whose size is specified by the width and height parameters; and both outlined by, and filled with, the default color.
+ `ctx.strokeRect(x, y, width, height)`: same but in wireframe mode.
Note that we use (_line 30_) `ctx.translate(x, y)` to make it easier to move the monster around. So, all the drawing instructions are coded as if the monster was in (0, 0), at the top left corner of the canvas (look at _line 33_). We draw the body outline with a rectangle starting from (0, 0). Calling `context.translate` "changes the coordinate system" by moving the "old (0, 0)" to (x, y) and keeping other coordinates in the same position relative to the origin.
+ _Line 19_: we call the `drawMonster` function with (10, 10) as parameters, which will cause the original coordinate system to be translated by (10, 10).
+ And if we change the coordinate system (this is what the call to `ctx.translate(...)` does) in a function, it is good practice to always save the previous context at the beginning of the function and restore it at the end of the function (_lines 27 and 50_).


#### Notes for 2.6.1 Drawing

+ HTML5 canvas
  + a transparent element useful for drawing and animating
  + adding canvas in HTML: `<canvas id="myCanvas" width="200" height="200"></canvas>`
    + not visible: transparent
    + CSS style border to be visible: `canvas { border: 1px solid black; }`
  + best practice
    + use a function called AFTER the page fully loaded, the DOM ready, and select the canvas
    + get a 2D graph context for this canvas
      + an object used to draw on the canvas and to set global properties
      + syntax: `ctx = canvas.getContext('2d');`
    + draw something
      + `ctx.fillRect(x, y, width, height)`: draw a filled rectangle
      + `ctx.strokeRect(x, y, width, height)`: draw a wireframed rectangle
    + use global variables for the canvas and context objects
      + `ctx.fillStyle = 'color';`: set filled color
      + `ctx.strokeStyle = 'color';`: set wireframe color
      + `ctx.lineWidth = number;`: set framewire line width
      + `ctx.beginPath();`: lift pen to begin a new draw, no line btw the previous ned point and the current starting point
      + useful global properties: `w = canvas.width; h = canvas.height;`
    + typical procedure for function to change the context
      + change any properties of global context: 
        + start by saving the content: `ctx.save();`
        + end by restoring it: `ctx.restore();`
      + properties including color, line, width, coordinate system, etc.
      + the change in the function won't effect anything outside the function
  + coordinate system
    + origin: top left of the canvas
    + default: (0, 0)
    + `ctx.translate(x, y)`: relocate the origin to (x, y) of the canvas
    + useful to have multiple shapes by translating the origin
  + example: [simple drawing](src/02f-example01.html)
    + call `init()` function after page loaded: `window.onload = function init()`
    + get `canvas` element: `canvas = document.querySelector("#myCanvas");`
    + request a graphic context: `ctx = canvas.getContext('2d');`
      + a variable for 2D or 3D drawing on the canvas
      + used for drawing or setting global variables
    + draw
      + red filled rectangle: `ctx.fillStyle = 'red'; ctx.fillRect(10, 10, 30, 30);`
      + green framewire rectangle: `ctx.strokeStyle = 'green'; ctx.lineWidth = 4; ctx.strokeRect(100, 40, 40, 40);`
      + red filled/storked circle: `ctx.beginPath(); ctx.arc(60, 60, 10, 0, 2*Math.PI); ctx.fill();` or `ctx.stroke();`
      + purple filled/stroked text: `ctx.fillStyle = "purple"; ctx.font = "20px Arial"; ctx.fillText("Hello!", 60, 20);` or `ctx.strokeText("Hello!", 60, 20);`
  + example: [function w/ save and restore context](src/02f-example02.html)
    + two functions to draw filled rectangle w/ a given color and filled circle w/ a given color, respectively
    + function parameters: values for `x`, `y`, `width`, `height`, `radius`, `color`, etc.
    + move the shapes by calling `ctx.translate(x, y)` w/ given (x, y)
  + example: [monster](src/02f-example03.html): `drawMyMonster(x, y)` function:
    + save the context by using 2D context: `ctx.save();`
    + translate the corrdinate system w/ given position: `ctx.translate(x, y);`
    + drawing monster: `drawMyMonster(x, y){...}` (relative to the top left corner)
      + head (outter frame): `ctx.strokeRect(0, 0, 100, 100);`
      + eyes: `ctx.fillRect(20, 20, 10, 10); ctx.fillRect(65, 20, 10, 10);`
      + nose: `ctx.strokeRect(45, 40, 10, 40);`
      + mouse: `ctx.strokeRect(35, 84, 30, 10);`
      + teeth: `ctx.fillRect(38, 84, 10, 10); ctx.fillRect(52, 84, 10, 10);`
    + restore the context: `ctx.restore();`



### 2.6.2 Animating


#### Live coding video: basic animation techniques

<a href="https://edx-video.net/W3CxJS.0x-V000200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/13acju4l)

A typical animation loop does the following at regular intervals:

1. Clear the canvas
1. Draw graphic objects / shapes
1. Move graphic shapes / objects
1. Go to step 1

Optional steps can be:

+ Look at the keyboard / mouse / gamepad if we need to do something according to their status (i.e. if the left arrow is pressed: move the player to the left)
+ Test collisions: the player collided with an enemy, remove one life
+ Test game states: if there are no more lives, then go to the "game over" state and display a "game over" menu.
+ Etc.


#### Examples

__Example #1: monster on the move__

There are different methods for coding an animation loop in JavaScript, as described in the above video.

The trick is to write a function, and at the end of this function, to ask the browser to call it again in 1/60th of a second if possible. See the CodePen example below

[CodePen Demo](https://codepen.io/w3devcampus/pen/PpLLKY)

[Local Demo](src/02f-example04.html)


__Example #2: bouncing balls__

Here the balls bounce on the sides of the canvas (walls).

[CodePen Demo](https://codepen.io/w3devcampus/pen/OpqqqM)

[Local Demo](src/02f-example05.html)


__Explanations:__

This time, we've used "simple objects" for the circle and the rectangles, and we've called them "player" and "ball":

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> ball </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; x</span><span class="pun">:</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; y</span><span class="pun">:</span><span class="lit">100</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; radius</span><span class="pun">:</span><span class="pln"> </span><span class="lit">15</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; color</span><span class="pun">:</span><span class="str">'green'</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; speedX</span><span class="pun">:</span><span class="lit">2</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; speedY</span><span class="pun">:</span><span class="lit">1</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> player </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; x</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; y</span><span class="pun">:</span><span class="lit">10</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; width</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; height</span><span class="pun">:</span><span class="lit">20</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; color</span><span class="pun">:</span><span class="str">'red'</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

With this syntax, it's easier to manipulate "the x pos of the ball" - you just have to use `ball.x`. we added two properties to the ball object: `speedX` and `speedY`. Their value is the number of pixels that will be added to the current `ball.x` and `ball.y` position, at each frame of animation.

Let's look at the animation loop:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> mainLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // 1 - clear the canvas</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; <strong>// draw the ball and the player</strong></span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; drawFilledRectangle</span><span class="pun">(</span><span class="pln">player</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; drawFilledCircle</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; // animate the ball that is bouncing all over the walls</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; moveBall</span><span class="pun">(</span><span class="pln">ball</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // ask for a new animation frame</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Now, let's decompose the animation loop in some external functions to make it more readable. At each frame of animation, we will clear the canvas, draw the player as a rectangle, draw the ball as a circle, and move the ball. 

You can take a look at the new versions of `drawFilledRectangle` that now take only one parameter named `r`, instead of x, y, width, height and a color. We've only changed a few things in its code (changed x to `r.x`, y to `r.y`, color to `r.color` etc.)

Let's look at the moveBall function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> moveBall</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">speedY</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; testCollisionBallWithWalls</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

This function is called 60 times per second. So, 60 times per second we modify the `b.x` and `b.y` positions of the ball passed as parameter by adding to them the `b.speedX` and `b.speedY` property values.

Notice that we call `moveBall(ball)` from `mainLoop`. In the `moveBall` function, the ball passed as a parameter becomes the `b` parameter. So when we change the `b.x` value inside the function, we are in reality changing the x value of the global object `ball`! 

Ok, and at _line 5_ we call `testCollisionBallWithWalls(b)`, which will test if the ball `b hits` a vertical or horizontal wall. Let's see an extract of this function now:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> testCollisionBallWithWalls</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // COLLISION WITH VERTICAL WALLS?</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pun">((</span><span class="pln">b</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&gt;</span><span class="pln"> w</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // the ball hit the right wall</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // change horizontal direction</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">speedX </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="pln">b</span><span class="pun">.</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // put the ball at the collision point</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;b</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> w </span><span class="pun">-</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span><span class="pln"> </span><span class="pun">...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; ...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

At _line 3_ you can see the test that checks if the ball b hits the right side of the canvas. The right wall is at `w` (the width of the canvas) on the X-axis. If we compare (`b.x + b.radius`) with `w`, we can check if a part of the ball extends beyond the right wall. 

Remember that each 1/60th of a second, the ball moves a certain number of pixels to the right (the exact value is `b.speedX`). Imagine that the ball moves 10 pixels to the right at each frame of animation. At some point, it will "cross the right wall". We cannot just change the sign of `b.speedX` to make it go to the other side. If we did this, it may stay stuck against the side with one half of the ball on either side of the wall. 

If we now remove `b.speedX` to the `ball.x` position, we return the ball to the position it was in before it hit the wall. If we then reverse `speedX`, the ball will indeed start moving with a reverse horizontal speed. This will work but can give a strange visual effect if the balls moves, say, 20 pixels per frame or more. The ball will never be in a position where the eye can "see it against the wall". This is why experienced game coders know that you just need to put the ball "at the contact position", not to its previous position, before reversing the speed value. This is done at _lines 8-9_. Try changing `speedX` to say, 20, and you'll see what we mean.


#### Notes for 2.6.2 Animating

+ Animation
  + ways to animation
    + `setInterval(func, time)`: execute `func` every `time` ms
    + `setTimeout(func, time)`: execute only once after the delay `time` ms
    + `requestAnimationFrame(func)`: request a new frame of animation in 1/60 seconds
  + best practice: `requestAnimationFrame(func)`
  + typical animation loop procedure
    + clear the canvas
    + draw graphic objects / shapes
    + move graphic objects / shapes
    + repeat previous 3 steps
  + optional steps for animation loop
    + observe the keyboard / mouse / gamepad to change status
    + test collisions: decrease one life if player collides
    + test game state: game over if no life left
    + etc.
  + example: [moving monster](src/02f-example04.html)
    + global variables: `var canvas, ctx, w, h; var xMonster = 10; var yMonster = 10; var monsterSpeed = 1;`
    + `init` function after page loaded: `window.onload = function init() {...}`
      + access element: `canvas = document.querySelector("#myCanvas");`
      + regular used info (no `var` or `let` w/ these variables $\to$ global variables): `w = canvas.width; h = canvas.height;`
      + drawing object declaration: `ctx = canvas.getContext('2d');`
      + start the drawing and moving: `mainLoop();`
    + major iteration of the program: `function mainLoop() { baseSetting & mainLoop}`
      + clear the canvas: `ctx.clearRect(0, 0, w, h);`
      + draw the monster: `drawMonster(xMonster, yMonster);`
      + move the monster: `xMonster += monsterSpeed;`
      + test collisions w/ vertical walls: `if (((xMonster + 100)> w) || (xMonster < 0)) { monsterSpeed = -monsterSpeed; }`
      + request a new frame of animation in 1/60s: `requestAnimationFrame(mainLoop);`
  + example: [bouncing balls](src/02f-example05.html)
    + global variables: `var canvas, ctx, w, h; var ball = { x: 100, y:100, radius: 15, color:'green', speedX:2, speedY:1}; var player = { x:10, y:10, width:20, height:20, color:'red'}`
    + major iteration of the program: `function mainLoop() {...}`
      + clear the canvas: `ctx.clearRect(0, 0, w, h);`
      + `init` function after page loaded: `window.onload = function init() { baseSetting & mainLoop}`
      + draw the ball and the player: `drawFilledRectangle(player); drawFilledCircle(ball);` 
      + animate the ball: `moveBall(ball);`
      + ask for a new animation frame: `requestAnimationFrame(mainLoop);`
    + moving ball: `function moveBall(b) { newPosition & collisionDetection }`
      + new position of ball: `b.x += b.speedX; b.y += b.speedY;`
      + collision detection: `testCollisionBallWithWalls(b);`
    + collision detection: `function testCollisionBallWithWalls(b) {...}`
      + collision w/ vertical walls: 

        ```js
        if ((b.x + b.radius) > w) { 
          b.speedX = -b.speedX; b.x = w - b.radius; 
        } else if ((b.x -b.radius) < 0) { 
          b.speedX = -b.speedX; b.x = b.radius; 
        }
        ```

      + collision w/ horizontal walls: 
       
        ```js
        if ((b.y + b.radius) > h) { 
          b.speedY = -b.speedY; b.y = h - b.radius; 
        } else if ((b.y -b.radius) < 0) { 
          b.speedY = -b.speedY; b.y = b.radius; 
        }
        ```


### 2.6.3 Animating multiple objects

Let's animate balls and let's start with 3 the animation of 3 balls: `ball1`, `ball2` and `ball3`. In the animation loop, we draw and move these three balls. Here is the result:

[CodePen Demo](https://codepen.io/w3devcampus/pen/bqZypx)

[Local Demo](src/02f-example06.html)

Extract of the source code: the mainLoop function

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> mainLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // 1 - clear the canvas</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // draw the balls and the player</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawFilledRectangle</span><span class="pun">(</span><span class="pln">player</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>drawFilledCircle</strong></span><strong><span class="pun">(</span><span class="pln">ball1</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; drawFilledCircle</span><span class="pun">(</span><span class="pln">ball2</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; drawFilledCircle</span><span class="pun">(</span><span class="pln">ball3</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // animate the balls bouncing all over the walls</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>moveBall</strong></span><strong><span class="pun">(</span><span class="pln">ball1</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; moveBall</span><span class="pun">(</span><span class="pln">ball2</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; moveBall</span><span class="pun">(</span><span class="pln">ball3</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // ask for a new animation frame</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

And what if we have 100 balls? We're not going to copy and paste the lines that draw and move the balls 100 times!

#### Using arrays and loops for creating any number of balls, for animating and moving any number of balls!

New version: look at the `createBalls`, `drawBalls` and `moveBalls` functions now!

[CodePen Demo](https://codepen.io/w3devcampus/pen/jBJoLo)

[Local Demo](src/02f-example07.html)

Let's look at the new functions we've added: 

__`createBalls(numberOfBalls)`, returns an array of balls:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> createBalls</span><span class="pun">(</span><span class="pln">n</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // empty array</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; <strong>var</strong></span><strong><span class="pln"> ballArray </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // create n balls</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; <strong>for</strong></span><strong><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> n</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; x</span><span class="pun">:</span><span class="pln">w</span><span class="pun">/</span><span class="lit">2</span><span class="pun">,</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; y</span><span class="pun">:</span><span class="pln">h</span><span class="pun">/</span><span class="lit">2</span><span class="pun">,</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; radius</span><span class="pun">:</span><span class="pln"> </span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">30</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span><span class="pln"> </span><span class="com">// between 5 and 35</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedX</span><span class="pun">:</span><span class="pln"> </span><span class="pun">-</span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">10</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span><span class="pln"> </span><span class="com">// between -5 and + 5</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; speedY</span><span class="pun">:</span><span class="pln"> </span><span class="pun">-</span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">10</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">(),</span><span class="pln"> </span><span class="com">// between -5 and + 5</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; color</span><span class="pun">:&nbsp;</span><span class="pln">getARandomColor</span><span class="pun">(),</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; }</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; // add ball b to the array</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>ballArray</strong></span><strong><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; <strong>}</strong></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // returns the array full of randomly created balls</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; return</span><span class="pln"> ballArray</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Explanations:__

+ _Line 3_: we declare an empty array that will contain the balls,
+ _Lines 7-14_: we create a new ball object with random values. Note the use of `Math.random()`, a predefined JavaScript function that returns a + decimal value between 0 and 1. We call another function named `getARandomColor()` that returns a color taken randomly.
+ _Line 16_: we add the newly created ball b to the array,
+ _Line 19_: we return the array to the caller.

The `getARandomColor` function

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> getARandomColor</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> colors </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'red'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'blue'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'cyan'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'purple'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 'pink'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">];</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // a value between 0 and color.length-1</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Math.round = rounded value</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Math.random() a value between 0 and 1</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> colorIndex </span><span class="pun">=</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">round</span><span class="pun">((</span><span class="pln">colors</span><span class="pun">.</span><span class="pln">length</span><span class="pun">-</span><span class="lit">1</span><span class="pun">)*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">());</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>var</strong></span><strong><span class="pln"> c </span><span class="pun">=</span><span class="pln"> colors</span><span class="pun">[</span><span class="pln">colorIndex</span><span class="pun">];</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // return the random color</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>return</strong></span><strong><span class="pln"> c</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Explanations:__

+ _Line 2_: in this function, we use an array of random color names named `colors` (you can go on the codePen example and change these colors or add new ones).
+ _Line 7_: then we compute an index with a random value between 0 and `colors.length-1`. Remember that in an array of n elements, the index of the first is always 0 and the index of the last one is always equal to the length of the array -1. For example: `var myArray = ['red', 'blue', 'green']`, red is at index 0, green at index 2, while `myArray.length = 3`, the number of elements in the array.
+ _Lines 8 and 11_: once we get a random index in the correct range, we can return the corresponding color.

Functions drawAllBalls and moveAllBalls:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawAllBalls</span><span class="pun">(</span><strong><span class="pln">ballArray</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ballArray</strong></span><strong><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; drawFilledCircle</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; <strong>});</strong></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> moveAllBalls</span><span class="pun">(</span><strong><span class="pln">ballArray</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // iterate on all balls in array</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong> ballArray</strong></span><strong><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // b is the current ball in the array</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">speedY</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; testCollisionBallWithWalls</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; <strong>});</strong></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Explanations:__

These two functions use an iterator on the array of balls (using the `forEach` method that looked the best fit here). The code inside the iterator is the same as in the previous example. We did not have to modify the `testCollisionBallWithWalls` code, for example.


#### Notes for 2.6.3 Animating multiple objects

+ Aminating multiple objects
  + `forEach` method: iterate elements in an array
  + example: [3 bouncing balls and the player](src/02f-example06.html)
    + global variables for 3 balls and the player
    + initialize the program: `window.onload = function init() {...}`
    + iterate for moving balls: `function mainLoop(){...}`
      + clear the canvas: `ctx.clearRect(0, 0, w, h);`
      + drawing the balls and the player: `drawFilledRectangle(player); drawFilledCircle(ball1); ...;`
      + animate the balls: `moveBall(ball1); moveBall(ball2); moveBall(ball3);`
      + ask for a new animation frame: `requestAnimationFrame(mainLoop);`
    + move the balls: `function moveBall(b) {...}`
    + collision detection: `testCollisionBallWithWalls(b) {...}`
  + example: [arrays for bouncing balls](src/02f-example07.html)
    + `function createBalls(numberOfBalls)`: return an array of balls
      + init empty array; `var ballArray = [];`
      + create n balls w/ for loop: `for (var i = 0; i < n; i++) { ballProperties & toArray }`
      + ball properties: `var b = {x: w/2, y: h/2, radius: -5 + 30*Math.random(), speedX: ..., speedY: ..., color: getARandomColor()}`
      + add ball to array: `ballArray.push(b);`
    + `function getARandomColor()`: randomly assign ball color
      + init color array: `var colors = ['red', 'blue', ..., 'yellow'];`
      + randonly assign a color: `var colorIdx = Math.round((colors.length-1)*Math.random()); return colors[colorIdx];`
    + `function drawBalls(ballArray){...}`: `ballArray.forEach(function(b){ drawFilledCircle(b)})`
    + moving balls: `function moveBallsArray(ballArray)`
      + iterate on all balls in array: `ballArray.forEach(function(b) { ballPosition & collisionDetect });`
      + ball position: `bx += b.speedX; by += b.speedY;`
      + collision detection: `testCollisionBallWithEWalls(b);`


### 2.6.4 Mouse interactions

Detecting mouse events in a canvas is quite straightforward: you add an event listener to the canvas, and the browser invokes that listener when the event occurs.

The example below is about listening to mouseup and mousedown events (when a user presses or releases any mouse button):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // do something with the mousedown event</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">});</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedup'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // do something with the mouseup event</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">});</span></li>
</ol></div>

The event received by the listener function will be used for getting the button number or the coordinates of the mouse cursor. Before looking at different examples, let's look at the different event types we can listen to.

#### The different mouse events (reminder)

In the last example, we saw how to detect the `mouseup` and `mousedown` events.

There are other events related to the mouse:

+ `mouseleave`: similar to `mouseout`, fired when the mouse leaves the surface of the element. The difference between `mouseleave` and `mouseout` is that `mouseleave` does not fire when the cursor moves over descendant elements, and `mouseout` is fired when the element the cursor moves to is outside the bounds of the original element or is a child of the original element.
+ `mouseover`: the mouse cursor is moving over the element that listens to that event. A `mouseover` event occurs on an element when you are over it - <u>coming from either its child OR parent element</u>, but a `mouseenter` event only occurs when the mouse <u>moves from the parent element to the child element</u>.
+ `mousedown`: fired when a mouse button is pressed.
+ `mouseup`: fired when a mouse button is released.
+ `mouseclick`: fired after a `mousedown` and a `mouseup` have occurred.
+ `mousemove`: fired while the mouse moves over the element. Each time the mouse moves, a new event is fired, unlike with `mouseover` or `mouseenter`, where only one event is fired.


#### The tricky part: getting the position of the mouse relative to the canvas

When you listen to any of the above events, the event object (we call it a "DOM event"), passed to the listener function, has properties that correspond to the mouse coordinates: `clientX` and `clientY`.

<span style="color: brown;">However, these are what we call "viewport coordinates". Instead of being relative to the canvas itself, they are relative to the viewport (the visible part of the page).</span>

Most of the time you need to work with the mouse position relative to the canvas, not to the viewport, so you must convert the coordinates between the viewport and the canvas. This will take into account the position of the canvas in the viewport, and the CSS properties that may affect the canvas position (margin, etc.).

Fortunately, there is a method for getting the position and size of any element in the viewport: `getBoundingClientRect()`.

Here is an example that shows the problem:

[CodePen Demo](https://codepen.io/w3devcampus/pen/Wpmqdw)

[Local Demo](src/02f-example08.html)


__WRONG code used in this example:__

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun" style="color: #666600;">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">canvas</span><span class="pun" style="color: #666600;">.</span><span class="pln">addEventListener</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'mousemove'</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">(</span><span class="pln">evt</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;<strong>mousePos&nbsp;</strong></span><strong><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;getMousePos</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #006688;">var</span><span class="pln">&nbsp;message&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">'Mouse position: '</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">','</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">y</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; writeMessage</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;message</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun" style="color: #666600;">},</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">false</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">...</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;getMousePos</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;<strong>&nbsp;</strong></span><strong><span class="com" style="color: #880000;">//&nbsp;WRONG!!!</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #006688;">return</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;<strong>x</strong></span><strong><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">clientX</span><span class="pun" style="color: #666600;">,</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;<strong>y</strong></span><strong><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">clientY</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div>

Here is the result, when the mouse is approximately at the top left corner of the canvas:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/19s0kpa8')"
    src    ="https://tinyurl.com/13n0iqsk"
    alt    ="bad mouse coords"
    title  ="bad mouse coords"
  />
</figure>


A good version of the code:

[CodePen Demo](https://codepen.io/w3devcampus/pen/MpxMQo)

[Local Demo](src/02f-example09.html)


And here is the fixed version of the getMousePos function:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;getMousePos</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com" style="color: #880000;">// necessary to take into account CSS boundaries</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd" style="color: #006688;">var</span><span class="pln">&nbsp;rect&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666600;">.</span><span class="pln">getBoundingClientRect</span><span class="pun" style="color: #666600;">();</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #006688;">return</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; x</span><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">clientX&nbsp;</span><strong><span class="pun" style="color: #666600;">-</span><span class="pln">&nbsp;rect</span><span class="pun" style="color: #666600;">.</span><span class="pln">left</span><span class="pun" style="color: #666600;">,</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; y</span><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">clientY&nbsp;</span><strong><span class="pun" style="color: #666600;">-</span><span class="pln">&nbsp;rect</span><span class="pun" style="color: #666600;">.</span><span class="pln">top</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div>

Result (the cursor is approximately at the top left corner):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/19s0kpa8')"
    src    ="https://tinyurl.com/3looe5fs"
    alt    ="mouse at zero zero"
    title  ="mouse at zero zero"
  />
</figure>



#### How to display the mouse position, and the mouse button that has been pressed or released

This example uses the previous function for computing the mouse position correctly. It listens to `mousemove`, `mousedown` and `mouseup` events, and shows how to get the mouse button number using the `evt.button` property.

Example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/zZbVjW)

[Local Demo](src/02f-example10.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/19s0kpa8')"
    src    ="https://tinyurl.com/fca8xxkv"
    alt    ="mouse event example"
    title  ="mouse event example"
  />
</figure>


Extract from source code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #006688;">var</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;ctx</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;mouseButton</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun" style="color: #666600;">.</span><span class="pln">onload&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;init</span><span class="pun" style="color: #666600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">getElementById</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'myCanvas'</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666600;">.</span><span class="pln">getContext</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'2d'</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;<strong>canvas</strong></span><strong><span class="pun" style="color: #666600;">.</span><span class="pln">addEventListener</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'mousemove'</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">(</span><span class="pln">evt</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>mousePos&nbsp;</strong></span><strong><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;getMousePos</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #006688;">var</span><span class="pln">&nbsp;message&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">'Mouse position: '</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">','</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">y</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;message</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666600;">},</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">false</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;<strong>canvas</strong></span><strong><span class="pun" style="color: #666600;">.</span><span class="pln">addEventListener</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'mousedown'</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">(</span><span class="pln">evt</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>mouseButton&nbsp;</strong></span><strong><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">button</span><span class="pun" style="color: #666600;">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #006688;">var</span><span class="pln">&nbsp;message&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"Mouse button "</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">button&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">" down at position: "</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">','</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">y</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;message</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666600;">},</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">false</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;<strong>canvas</strong></span><strong><span class="pun" style="color: #666600;">.</span><span class="pln">addEventListener</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'mouseup'</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">(</span><span class="pln">evt</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #006688;">var</span><span class="pln">&nbsp;message&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"Mouse up at position: "</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">x&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">','</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;mousePos</span><span class="pun" style="color: #666600;">.</span><span class="pln">y</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;message</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666600;">},</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #006688;">false</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span>&nbsp;</li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;writeMessage</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;message</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln">save</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln">clearRect</span><span class="pun" style="color: #666600;">(</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666600;">.</span><span class="pln">width</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666600;">.</span><span class="pln">height</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln">font&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">'18pt Calibri'</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln">fillStyle&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">'black'</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln">fillText</span><span class="pun" style="color: #666600;">(</span><span class="pln">message</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">10</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">25</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun" style="color: #666600;">.</span><span class="pln">restore</span><span class="pun" style="color: #666600;">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd" style="color: #006688;">function</span><span class="pln">&nbsp;getMousePos</span><span class="pun" style="color: #666600;">(</span><span class="pln">canvas</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com" style="color: #880000;">// necessary to take into account CSS boudaries</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;<strong>&nbsp;</strong></span><strong><span class="kwd" style="color: #006688;">var</span><span class="pln">&nbsp;rect&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;canvas</span><span class="pun" style="color: #666600;">.</span><span class="pln">getBoundingClientRect</span><span class="pun" style="color: #666600;">();</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #006688;">return</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;<strong>x</strong></span><strong><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">clientX&nbsp;</span><span class="pun" style="color: #666600;">-</span><span class="pln">&nbsp;rect</span><span class="pun" style="color: #666600;">.</span><span class="pln">left</span></strong><span class="pun" style="color: #666600;">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;<strong>y</strong></span><strong><span class="pun" style="color: #666600;">:</span><span class="pln">&nbsp;evt</span><span class="pun" style="color: #666600;">.</span><span class="pln">clientY&nbsp;</span><span class="pun" style="color: #666600;">-</span><span class="pln">&nbsp;rect</span><span class="pun" style="color: #666600;">.</span><span class="pln">top</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div>


#### Notes for 2.6.4 Mouse interactions

+ Mouse interactions in canvas
  + detecting mouse events
    + add event listener to the canvas
    + the browser invoking listener when the event occurs
  + mouse events
    + `mousedown`: mouse button pressed
    + `mouseup`: mouse button released
    + `mouseclick`: fired after a `mousedown` and `mouseup` occurred
    + `mouseover`: mouse coming from either its child OR parent element; mouse cursor moving over the element that listens to the event
    + `mouseenter`: mouse moving from the parent element to child element
    + `mouseleave`: mouse leaving the surface of the element
    + `mouseout`: mouse moving to outside the bounds of the original element or a child of the original element

+ Mouse position relative to the canvas
  + viewport coordinate
    + the mouse coordinate `(clientX, clientY)` passed to the listener function
    + viewport as the visible part of the page
  + most of the time working w/ the mouse position relative to the canvas, not to the viewport
  + converting the coordinates btw the viewport and the canvas
  + considerations
    + the position of the canvas in the viewport
    + the CSS properties probably effecting the canvas position (margin, etc.)
  + `getBoundingClientRect()`: a method for getting the position and size of any element in the viewport
  + mouse position in canvas: `function getMousePos(canvas, evt) {...}`
    + get the canvas position: `var rect = canvas.getBoundingClientRect();`
    + the position relative to the canvas: `{x: evt.clientX - rect.left, y: evt.clientY - rect.top}`
  + `evt.button` property: the mouse button number


### 2.6.5 Moving a player with the mouse

This time, we've added a `mousemove` event listener to the canvas in the init function, and reused the trick that you saw in the previous section to get the correct mouse position:

Working example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/EWMBeR)

[Local Demo](src/02f-example11.html)


Extract from the JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">var</span><span class="pln"> mousePos</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">...</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// create 10 balls</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;balls </span><span class="pun">=</span><span class="pln"> createBalls</span><span class="pun">(</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; <strong>&nbsp;// add a mousemove event listener to the canvas</strong></span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> mouseMoved</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// ready to go !</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;mainLoop</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> mouseMoved</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;mousePos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// from the previous section</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getBoundingClientRect</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; x</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientX </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">left</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; y</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientY </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">top</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp;};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"></li>
</ol></div>

_Line 9_ defines a `mousemove` event listener: the `mouseMoved` callback function will be called each time the user moves the mouse on the canvas.

The `mouseMoved(evt)` function uses the trick from the previous section and puts the correct mouse position in the `mousePos` variable. 

With this code, as soon as we move the mouse on top of the canvas, we'll have this `mousePos` global variable (line1) that will contain the mouse position (in the form of the `mousePos.x` and `mousePos.y` properties).

And here is the new `mainLoop` function. We added a call to the `mousePlayerWithMouse` function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> mainLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // 1 - clear the canvas</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // draw the ball and the player</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawFilledRectangle</span><span class="pun">(</span><span class="pln">player</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawAllBalls</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // animate the ball that is bouncing all over the walls</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; moveAllBalls</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; movePlayerWithMouse</span><span class="pun">();</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // ask for a new animation frame</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


And here is the code of the movePlayerWithMouse function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> movePlayerWithMouse</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">mousePos </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; player</span><span class="pun">.</span><span class="pln">x </span><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; player</span><span class="pun">.</span><span class="pln">y </span><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


If the mouse position is defined, the player's x and y position will equal to the positions of the mouse pointer.

The mouse position may be `undefined` if the animation loop started without the mouse cursor being on top of the canvas. Remember that the mainLoop starts as soon as the page is loaded.

Perhaps it's occurred to you that it might be better to move the player "from its center" instead of from its top left corner. We leave this improvement to you! :-)


#### Notes for 2.6.5 Moving a player with the mouse

+ Moving element w/ mouse pointer
  + get mouse position in a canvas: `getMousePos(evt)`
  + the mouse cursor out of canvas: `mousePos === undefined`
  + mouse positionwithin the canvas: `player.x = mousePos.x; player.y = mousePos.y;`



### 2.6.6 Adding collision detection

Let's make it a game by adding collision detection! And try to move the player to all the balls as fast as you can.

[CodePen Demo](https://codepen.io/w3devcampus/pen/gmEVJG)

[Local Demo](src/02f-example12.html)


#### How do we detect collisions?

First, if you're into game programming, we have a full section about collision detection one of the W3Cx [HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games) course modules.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/7mmfaeyr" ismap target="_blank">
    <img style="margin: 0.1em;" height=80
      src  ="https://tinyurl.com/y8nsrfm2"
      alt  ="circle rect collision (not here)"
      title="circle rect collision (not here)"
    >
    <img style="margin: 0.1em;" height=80
      src  ="https://tinyurl.com/6qu5oc3q"
      alt  ="circle rect collision"
      title="circle rect collision"
    >
  </a>
</div>


We have a player that is a rectangle and other objects that are circles. This is cool, as it allows us to find a short function that tests if a circle collides with a rectangle whose sides are aligned to the X-axis and Y-axis (we implemented this after reading this [thread at StackOverflow](https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection)):

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="com">// Collisions between rectangle and circle</span></li>
<li class="L1"><span class="kwd">function</span><span class="pln">&nbsp;circRectsOverlap</span><span class="pun">(</span><span class="pln">x0</span><span class="pun">,</span><span class="pln">&nbsp;y0</span><span class="pun">,</span><span class="pln">&nbsp;w0</span><span class="pun">,</span><span class="pln">&nbsp;h0</span><span class="pun">,</span><span class="pln">&nbsp;cx</span><span class="pun">,</span><span class="pln">&nbsp;cy</span><span class="pun">,</span><span class="pln">&nbsp;r</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;testX</span><span class="pun">=</span><span class="pln">cx</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;testY</span><span class="pun">=</span><span class="pln">cy</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L4"><span class="pln"></span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">testX&nbsp;</span><span class="pun">&lt;</span><span class="pln">&nbsp;x0</span><span class="pun">)</span><span class="pln">&nbsp;testX</span><span class="pun">=</span><span class="pln">x0</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">testX&nbsp;</span><span class="pun">&gt;</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">x0</span><span class="pun">+</span><span class="pln">w0</span><span class="pun">))</span><span class="pln">&nbsp;testX</span><span class="pun">=(</span><span class="pln">x0</span><span class="pun">+</span><span class="pln">w0</span><span class="pun">);</span><span class="pln"></span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">testY&nbsp;</span><span class="pun">&lt;</span><span class="pln">&nbsp;y0</span><span class="pun">)</span><span class="pln">&nbsp;testY</span><span class="pun">=</span><span class="pln">y0</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">testY&nbsp;</span><span class="pun">&gt;</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">y0</span><span class="pun">+</span><span class="pln">h0</span><span class="pun">))</span><span class="pln">&nbsp;testY</span><span class="pun">=(</span><span class="pln">y0</span><span class="pun">+</span><span class="pln">h0</span><span class="pun">);</span><span class="pln"></span></li>
<li class="L9"><span class="pln"></span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln">&nbsp;</span><span class="pun">(((</span><span class="pln">cx</span><span class="pun">-</span><span class="pln">testX</span><span class="pun">)*(</span><span class="pln">cx</span><span class="pun">-</span><span class="pln">testX</span><span class="pun">)+(</span><span class="pln">cy</span><span class="pun">-</span><span class="pln">testY</span><span class="pun">)*(</span><span class="pln">cy</span><span class="pun">-</span><span class="pln">testY</span><span class="pun">))&lt;&nbsp;</span><span class="pln">r</span><span class="pun">*</span><span class="pln">r</span><span class="pun">);</span><span class="pln"></span></li>
<li class="L1"><span class="pln"></span><span class="pun">}</span></li>
</ol></div>

Let's look at our game! This time, we've added into the loop a collision test between the player and the balls. If the player hits a ball, it's removed from the ball array. We did this test in the moveBalls function, as we were already testing collisions with walls for each ball in the array. Let's look at this new version:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> moveAllBalls</span><span class="pun">(</span><span class="pln">ballArray</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // iterate on all balls in array</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ballArray</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">,</span><strong><span class="pln"> index</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // b is the current ball in the array</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">speedX</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">y </span><span class="pun">+=</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">speedY</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; testCollisionBallWithWalls</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; testCollisionWithPlayer</span><span class="pun">(</span><span class="pln">b</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> testCollisionWithPlayer</span><span class="pun">(</span><span class="pln">b</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">circRectsOverlap</span><span class="pun">(</span><span class="pln">player</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> player</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; player</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> player</span><span class="pun">.</span><span class="pln">height</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; b</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">radius</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp;// we remove the element located at index</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp;// from the balls array</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp;// splice: first parameter = starting index</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp;// second parameter = number of elements to remove</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; balls</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="pln">index</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Explanations:__

+ _Line 3_: Look at the iterator;  this time instead of just one parameter (the current element), we've added a second optional parameter that will be the in`dex of the current element, starting from zero.
+ _Line 10_: for each ball in the array, we will call `testCollisionWithPlayer(b, index);` that will check if there is a collision between the ball b and the player. We also pass the `index` of the ball. If a collision occurs, we will have to remove the ball from the array, and for that, we will need its index in the array.
+ _Line 15_ is the collision test, and if it is `true` (collision with the player), then the ball dies and we remove it from the array using the `splice` method you can use on arrays.
+ _Line 22_: here it is, we remove the current ball in the array using `balls.splice(position, numberOfElementsToRemove)`. The positon is given by `index`, and the number of balls to remove is one.


We've also added a function for displaying the number of balls in the array while we are playing. When this number reaches zero, we display "You Win!":

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawNumberOfBallsAlive</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">font</span><span class="pun">=</span><span class="str">"30px Arial"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">.</span><span class="pln">length </span><span class="pun">===</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"YOU WIN!"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">.</span><span class="pln">length</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

This function is called by the `mainLoop`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> mainLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // 1 - clear the canvas</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> w</span><span class="pun">,</span><span class="pln"> h</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; ...</span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; drawNumberOfBallsAlive</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; ...</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // ask for a new animation frame</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">mainLoop</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 2.6.6 Adding collision detection

+ Collision detection
  + [circle-Rectangle collision detection](https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection)
    + either the circle's center lies insiode the rectangle
    + one of the edges of the rectangle has a point in the circle

    ```shell
    def intersect(Circle(P, R), Rectangle(A, B, C, D)):
      S = Circle(P, R)
      return (pointInRectangle(P, Rectangle(A, B, C, D)) or
              intersectCircle(S, (A, B)) or
              intersectCircle(S, (B, C)) or
              intersectCircle(S, (C, D)) or
              intersectCircle(S, (D, A)))
    ```
  
    + `intersectCircle()`:
      + check if the foot of the perpendicular from `P` to the line is close enough and btw the endpoints
      + check endpoint  otherwise
  + JavaScript implementation

    ```js
    function circRectsOverlap(x0, y0, w0, h0, cx, cy, r) {
      var testX=cx; var testY=cy;

      if (testX < x0) testX=x0;
      if (testX > (x0+w0)) testX=(x0+w0);
      if (testY < y0) testY=y0;
      if (testY > (y0+h0)) testY=(y0+h0);

      return (((cx-testX)*(cx-testX)+(cy-testY)*(cy-testY))< r*r);
    }
    ```

  + example: [collision detection btw balls & the player](src/02f-example12.html)
    + moving all balls: `function moveAllBalls(ballArray) {...}`
      + iterate all balls in the array: `ballArray.forEach(function(b, index) {...}`
        + position of a certain ball: `b.x += b.speedX; b.y += b.speedY;`
        + detect collision w/ walls: `testCollisionBallWithWalls(b);`
        + detect collision btw balls & the player: ` testCollisionWithPlayer(b, index);`
    + detecting collection btw balls & the player (intersection): `function testCollisionWithPlayer(b, index) {...}`
      + check overlap w/ given params: `if(circRectsOverlap(player.x, player.y, player.width, player.height, b.x, b.y, b.radius)) {...}`
      + remove collided element (ball): `balls.splice(index, 1);`
    + printing number of alive balls: `function drawNumberOfBallsAlive(balls) {...}`
      + save context before drawing: `ctx.save();`
      + check and print number of alive balls:

        ```js
        if(balls.length === 0) {
          ctx.fillText("YOU WIN!", 20, 30);
        } else {
          ctx.fillText(balls.length, 20, 30);
        }
        ```

      + restore context: `ctx.restore();`


### 2.6.7 Adding input fields

Let's use some other techniques that we've learnt in this module. There are input fields: sliders, color chooser, number chooser. We are going to use the DOM API to handle them.

We use these input fields to indicate the number of balls we want, the max speed we would like, the color and size of the player, etc.

New version:

[CodePen Demo](https://codepen.io/w3devcampus/pen/RpOyRN)

[Local Demo](src/02f-example13.html)

__Explanations:__

HTML code: this time we've used an `oninput` in each input field, and an `onchange` attribute on the `<select>` HTML drop down menu:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"nbBalls"</span><span class="tag">&gt;</span><span class="pln">Number of balls: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"number"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">1</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">30</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value</span><span class="pun">=</span><span class="atv">10</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"nbBalls"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>oninput</strong></span><strong><span class="pun">=</span><span class="atv">"</span><span class="pln">changeNbBalls</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;p&gt;&lt;/p&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"nbBalls"</span><span class="tag">&gt;</span><span class="pln">Player color: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"color"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">'#FF0000'</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>oninput</strong></span><strong><span class="pun">=</span><span class="atv">"</span><span class="pln">changePlayerColor</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;p&gt;&lt;/p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"nbBalls"</span><span class="tag">&gt;</span><span class="pln">Color of ball to eat: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;select</span><span class="pln"> </span><strong><span class="atn">onchange</span><span class="pun">=</span><span class="atv">"</span><span class="pln">changeColorToEat</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">'red'</span><span class="tag">&gt;</span><span class="pln">red</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">'blue'</span><span class="tag">&gt;</span><span class="pln">blue</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &nbsp; &lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">'green'</span><span class="tag">&gt;</span><span class="pln">green</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;/select&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;p&gt;&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"nbBalls"</span><span class="tag">&gt;</span><span class="pln">Change ball speed: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;- </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">'1'</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; min</span><span class="pun">=</span><span class="atv">0.1</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">3</span><span class="pln"> </span><span class="atn">step</span><span class="pun">=</span><span class="atv">0.1</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>oninput</strong></span><strong><span class="pun">=</span><span class="atv">"</span><span class="pln">changeBallSpeed</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span><span class="atv">"</span></strong><span class="tag">&gt;</span><span class="pln"> + </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;p&gt;&lt;/p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/div&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"></li>
</ol></div>

JavaScript code: we've added some new variables in order to get closer to a real game with a goal, levels, game over menu and so on.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> initialNumberOfBalls</span><span class="pun">; // number of balls at the beginning</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> globalSpeedMutiplier </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">; // will change when we move the speed&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // slider</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> colorToEat </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">; &nbsp; &nbsp; &nbsp; // color of the "good" balls to eat</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> wrongBallsEaten </span><span class="pun">=</span><span class="pln"> goodBallsEaten </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">; //number of good/bad balls </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // eaten</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> numberOfGoodBalls</span><span class="pun">; &nbsp; &nbsp; &nbsp; &nbsp;// number of good balls in the set</span></li>
</ol></div>

And here are the callback functions called when you use the input fields:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> changeNbBalls</span><span class="pun">(</span><span class="pln">nb</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; startGame</span><span class="pun">(</span><span class="pln">nb</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> changeColorToEat</span><span class="pun">(</span><span class="pln">color</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; colorToEat </span><span class="pun">=</span><span class="pln"> color</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; startGame(</span>initialNumberOfBalls);</li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> changePlayerColor</span><span class="pun">(</span><span class="pln">color</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; player</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> color</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> changeBallSpeed</span><span class="pun">(</span><span class="pln">coef</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; globalSpeedMutiplier </span><span class="pun">=</span><span class="pln"> coef</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

Each time we change the number of balls in the game, or the color of the balls you need to eat, we need to restart the game. 

Here is the `startGame(nb_balls)` function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> startGame</span><span class="pun">(</span><span class="pln">nb</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; do</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;balls </span><span class="pun">=</span><span class="pln"> createBalls</span><span class="pun">(</span><span class="pln">nb</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;initialNumberOfBalls </span><span class="pun">=</span><span class="pln"> nb</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;numberOfGoodBalls </span><span class="pun">=</span><span class="pln"> countNumberOfGoodBalls</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">,</span><span class="pln"> colorToEat</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; }</span><span class="pln"> </span><span class="kwd">while</span><span class="pun">(</span><span class="pln">numberOfGoodBalls </span><span class="pun">===</span><span class="pln"> </span><span class="lit">0</span><span class="pun">); // in case no good ball in the set</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; wrongBallsEaten </span><span class="pun">=</span><span class="pln"> goodBallsEaten </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

... and here is the function that counts the number of good balls in the newly created set of balls:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> countNumberOfGoodBalls</span><span class="pun">(</span><span class="pln">balls</span><span class="pun">,</span><span class="pln"> colorToEat</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> nb </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; balls</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">b</span><span class="pun">.</span><span class="pln">color </span><span class="pun">===</span><span class="pln"> colorToEat</span><span class="pun">) // we count the number of balls</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; nb</span><span class="pun">++; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// of this color in the balls array</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; });</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; return</span><span class="pln"> nb</span><span class="pun">; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // return this number to the caller</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 2.6.7 Adding input fields

+ Changing variable dynamically
  + using `input` fields to change the init variables
  + example: [game to collide selected color balls](src/02f-example13.html)
    + HTML input fields
      + number of balls: `<label for="nbBalls">Number of balls: </label> <input type="number" min=1 max=30 value=10 id="nbBalls" oninput="changeNbBalls(this.value);">`
      + payer color: `<label for="nbBalls">Player color: </label> <input type="color" value='#FF0000' oninput="changePlayerColor(this.value);">`
      + color of ball to colide: `<label for="nbBalls">Color of ball to eat: </label> <select onchange="changeColorToEat(this.value);"> <option value='red'>red</option> <option value='blue'>blue</option> <option value='green'>green</option> </select>`
      + ball speed: `<label for="nbBalls">Change ball speed: </label> - <input type="range" value='1' min=0.1 max=3 step=0.1 oninput="changeBallSpeed(this.value);"> +`
    + global variables in JS
      + number of balls at the beginning: `var initialNumberOfBalls;`
      + ball speed slider: `var globalSpeedMutiplier = 1;`
      + color of the "good" balls to eat: `var colorToEat = 'red';`
      + number of good/bad balls eaten: `var wrongBallsEaten = goodBallsEaten = 0;`
      + number of good balls in the set: `var numberOfGoodBalls;`
    + callback functions for input fields
      + change ball numbers: `function changeNbBalls(nb) { startGame(nb); }`
      + change ball color to be eaten: `function changeColorToEat(color) { colorToEat = color; startGame(initialNumberOfBalls); }`
      + change player color: `function changePlayerColor(color) { player.color = color; }`
      + change ball speed: `function changeBallSpeed(coef) { globalSpeedMutiplier = coef; }`
    + starting game: `function startGame(nb) {...}`
      + check good/bad balls left until no good ball: `do {...} while(numberOfGoodBalls === 0);`
      + count the number of good balls: `balls = createBalls(nb); initialNumberOfBalls = nb; numberOfGoodBalls = countNumberOfGoodBalls(balls, colorToEat);`
      + initial value of good/bad balls: `wrongBallsEaten = goodBallsEaten = 0;`
    + count the number ofg good balls: `function countNumberOfGoodBalls(balls, colorToEat) {...}`
      + iterate to check the existence of balls: ` balls.forEach(function(b) { if(b.color === colorToEat) nb++; });`
      + return the number of existed balls: `return nb;`


### 2.6.8 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ First, do not forget to share your creations in the forum!
+ Do you know about jQuery or equivalent libraries that were developed to try to make the DOM easier to manipulate? Some people do not recommend using them now - why is this?


#### Optional projects

+ The game is not completely finished, as you may have noticed :-) So, try to make "levels": when all good balls have been eaten, let's restart automatically, but this time with one more ball in the initial set!
+ Try to display the level number on the right,
+ Try to use a global variable "gameState" that can be equal to "gameRunning" or to "displayGameOverMenu". Use it in the game loop with a switch statement, to display a game over menu when the player hits a certain number of bad balls (say three bad balls eaten and you're done!)
+ When, in the game over menu, listen to keydown events on the canvas and suggest pressing space to go to restart the game.
+ Add other input fields to further customize the game.
+ Try to draw a small monster instead of a red square for the player, and do the same thing with the balls - make some improvements!
+ Try to make ball movements different depending on their color (random direction that changes along the course of a ball, zigzag movements, etc.)
+ Try to make the balls change their size during the animation.
+ More difficult: try to make your player fire bullets to destroy enemy balls :-)




