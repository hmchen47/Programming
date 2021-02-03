# Module 2: Adding interactivity to HTML documents



## 2.6 Let's write a small game


### 2.6.1 Drawing

<a href="https://edx-video.net/W3CxJS.0x-V000100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](tinyurl.com/ynysboc7)

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

The canvas declaration is at line 8. Use attributes to give it a `width` and a `height`, but unless you add some CSS properties, you will not see it on the screen because it's transparent!

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
+ And if we change the coordinate system (this is what the call to `ctx.translate(...)` does) in a function, it is good practice to always save the previous context at the beginning of the function and restore it at the end of the function (lines 27 and 50).


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
    + two functions to draw fille rectangle w/ a given color and filled circle w/ a given color, respectively
    + function parameters: values for `x`, `y`, `width`, `height`, `radius`, `color`, etc.
    + move the shapes by calling `ctx.translate(x, y)` w/ given (x, y)
  + example: [monster](src/02f-example03.html)
  



