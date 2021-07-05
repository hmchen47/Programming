# Module 3: HTML5 file upload and download section


## 3.3 Drag and drop


### 3.3.1 Introduction

From [the W3C HTML 5.1 specification](https://www.w3.org/TR/html51/editing.html#dnd): 
>"the drag and drop API defines an event-based drag-and-drop mechanism, it does not define exactly what a drag-and-drop operation actually is".

We decided to present this API in a section about HTML5 client-side persistence, as it is very often used for dragging and dropping files. However, we will also address drag and drop of elements within an HTML document.

We will start by presenting the API itself, and then we will focus on the particular case of drag and dropping files.

#### External resources

+ MDN article about [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API).
+ Medium article entitled "[How to Drag & Drop HTML Elements and Files using Javascript](https://bit.ly/3wfFqif)"
+ Nice [shopping cart demo](https://bit.ly/3xiKp36).


#### Notes for 3.3.1 Introduction

+ Drag and drop API
  + defining an event-based drag-and-drop machansim
  + not defining what a drag-and-drop operation
  + often used for dragging and dropping files
  + resources
    + MDN article about [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API).
    + Medium article entitled "[How to Drag & Drop HTML Elements and Files using Javascript](https://bit.ly/3wfFqif)"
    + Nice [shopping cart demo](https://bit.ly/3xiKp36).
 

### 3.3.2 Drag detection

#### Live coding video: drag and drop basics

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2TEzEcC)


#### Draggable attribute and detection

In order to make any visible element draggable, add the `draggable="true"` attribute to any visible HTML5 element. Notice that some elements are draggable by default, such as `<img>` elements.

In order to detect a drag, add an event listener for the `dragstart` event:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;ol</span><span class="pln"> </span><strong><span class="atn">ondragstart</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragStartHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span></strong><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><strong><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span></strong><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-apple"</span><span class="tag">&gt;</span><span class="pln">Apples</span><span class="tag">&lt;/li&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><strong><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span></strong><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-orange"</span><span class="tag">&gt;</span><span class="pln">Oranges</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><strong><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span></strong><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-pear"</span><span class="tag">&gt;</span><span class="pln">Pears</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/ol&gt;</span></li>
</ol></div>

In the above code, we made all of the `<li>` elements draggable, and we detect a dragstart event occurring to any item within the ordered list: `<ol ondragstart="dragStarthandler(event)">`.

<p style="margin: 10px; border: 1px solid; padding: 10px;">When you put an <code>ondragstart</code> handler on an element, each of its draggable children could fire the event! It's a sort of "inheritance of handlers"... In the above example, the handler is declared at the<code> &lt;ol&gt; level, so any subordinate</code>&nbsp;<code>&lt;li&gt;</code> element will fire the event.</p>

Try the following interactive example in your browser (just click and drag one of the list items) or [play with it at CodePen](https://codepen.io/w3devcampus/pen/MaWKZb).

[Local Demo](src/03c-example01.html)

Screenshot:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2UZ5EZk')"
    src    = "https://bit.ly/2TEAbv8"
    alt    = "drag n drop fruits"
    title  = "drag n drop fruits"
  />
</figure>

Complete code from the example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> dragStartHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'dragstart event, target: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;p&gt;</span><span class="pln">What fruits do you like? Try to drag an element!</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;ol</span><span class="pln"> </span><span class="atn">ondragstart</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragStartHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-apple"</span><span class="tag">&gt;</span><span class="pln">Apples</span><span class="tag">&lt;/li&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-orange"</span><span class="tag">&gt;</span><span class="pln">Oranges</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-pear"</span><span class="tag">&gt;</span><span class="pln">Pears</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;/ol&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Drop your favorite fruits below:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag">&lt;body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;html&gt;</span></li>
</ol></div>

In this script, the event handler will only display an alert showing the name of the target element that launched the event. 


#### Notes for 3.3.2 Drag detection

+ Draggable attribute
  + making any visible elementdraggable w/ `true` value
  + some elements draggable by default, such as `<img>`
  + example: `<li dragable=true data-value="fruit-apple">Apple</li>`

+ `dragstart` event
  + add listener to detect a drag
  + `ondragstart` for HTML event handler
  + inheritance of handler: each of its children triggering the event
  + example: `<ol ondragstart="dragStartHandler(evt)"> ... </ol>`

+ [`data` attribute](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes)
  + storing extra info on standard elements w/o other hacks
  + html syntax: `data` attribute: any attribute started w/ `data-`
  + Javascrip access
    + using `getAttribute()` w/ their full HTML name to read
    + alternative: reading out via a `dataset` property
  + example
    + html: `<article id="electric-cars" data-column="3" data-index-numbser="12314" data-parent="cars">...</article>`
    + access element: `const article = document.querySelector("#electric-cars");`
    + get column: `article.dataset.columns; // "3"`
    + get index number: `article.dataset.indexNumber; // "12314"`
    + get parent: `article.dataset.parent; // "cars"`

+ Example: dragable attribute and event handler
  + HTML snippet<a name="drag"></a>:
    + ordered list: `<ol ondragstart="dragStartHandler(evt)"> ... </ol>`
    + item apples: `<li draggable=true data-value="fruit-apple">Apples</li>`
    + item oranges: `<li draggable=true data-value="fruit-orange">Oranges</li>`
    + item pears: `<li draggable=true data-value="fruit-pear">Pears</li>`
  + event handler: `function dragStartHandler(evt) { alert('dragstart event, target: ' + event.target.innerHTML); }`


### 3.3.3 Drop detection

Let's continue to develop the example. We show how to drag an element and detect a drop, receiving a value which corresponds to the dragged element. Then we change the page content accordingly.

#### Handling drop

__Step #1: in the `dragstart` handler, copy a value in the drag and drop clipboard for later use__

When a draggable `<li>` element is being dragged, in the `dragstart` handler [get the value of its data-value attribute](https://html5doctor.com/html5-custom-data-attributes/) and copy it to the "_drag and drop clipboard_" for later use.

When data is copied to this clipboard, a key/value pair must be given. The data copied to the clipboard is associated with this name.

The variable `event.target` at line 5 below is the `<li>` element that has been dragged, and event.target.dataset.value is the value of its data-value attribute (in our case "apples", "oranges" or "pears"):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> dragStartHandler</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'dragstart event, target: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target.innerHTML</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Copy&nbsp;to the drag'n'drop clipboard the value of the </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // data* attribute of the target, </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // with a type "Fruit".</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="kwd">event</span><span class="pun">.</span><span class="pln">dataTransfer</span><span class="pun">.</span><span class="pln">setData</span><span class="pun">(</span><span class="str">"Fruit"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">dataset</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>

__Step #2: define a "drop zone"__

Any visible HTML element may become a "drop zone"; if we attach an event listener for the `drop` event. Note that most of the time, as events may be propagated, we will also listen for `dragover` or `dragend` events and stop their propagation. More on this later...

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;div</span><span class="pln"> </span><strong><span class="atn">ondragover</span><span class="pun">=</span><span class="atv">"</span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">false</span><span class="atv">"</span></strong><span class="pln"> </span><strong><span class="atn">ondrop</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dropHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> Drop your favorite fruits below:</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;ol</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"droppedFruits"</span><span class="tag">&gt;&lt;/ol&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/div&gt;</span></li>
</ol></div>

Whenever the mouse is moving above a (any) drop zone, dragover events will fire. Accordingly, a large number of dragover events may need to be handled before the element is finally dropped. The `ondragover` handler is used to avoid propagating `dragover` events. This is done by returning the `false` value at _line 1_.

__Step #3: write a `drop` handler, fetch content from the clipboard, and do something with it__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> dropHandler</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'drop event, target: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">target.innerHTML</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// get the data from the drag'n'drop clipboard,GET </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// with a type="Fruit"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> data </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">dataTransfer</span><span class="pun">.</span><span class="pln">getData</span><span class="pun">(</span><span class="str">"Fruit"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// do something with the data</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
</ol></div>

Typically, in the `drop` handler, we need to acquire data about the element that has been dropped (we get this from the clipboard at _lines 6-8_, the data was copied there during step 1 in the `dragstart` handler).

#### Complete example

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3xiKFz7')"
    src    = "https://bit.ly/3e1Q6ej"
    alt    = "drag n drop fruits"
    title  = "drag n drop fruits"
  />
</figure>


Try it in your browser below or [play with it at CodePen](https://codepen.io/w3devcampus/pen/YyzWKy):

[Local Demo](src/03c-example02.html)

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp;&nbsp;function</span><span class="pln"> dragStartHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'dragstart event, target: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Copy&nbsp;to the drag'n'drop clipboard the value </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // of the data* attribute of </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // the target, with a type "Fruits".</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">dataTransfer</span><span class="pun">.</span><span class="pln">setData</span><span class="pun">(</span><span class="str">"Fruit"</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">dataset</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> dropHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'drop event, target: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> li </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'li'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// get the data from the drag'n'drop clipboard, </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// with a type="Fruit"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> data </span><span class="pun">=</span><span class="pln"> event</span><span class="pun">.</span><span class="pln">dataTransfer</span><span class="pun">.</span><span class="pln">getData</span><span class="pun">(</span><span class="str">"Fruit"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">data </span><span class="pun">==</span><span class="pln"> </span><span class="str">'fruit-apple'</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Apples'</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">data </span><span class="pun">==</span><span class="pln"> </span><span class="str">'fruit-orange'</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Oranges'</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">data </span><span class="pun">==</span><span class="pln"> </span><span class="str">'fruit-pear'</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Pears'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Unknown Fruit'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// add the dropped data as a child of the list.</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#droppedFruits"</span><span class="pun">).</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">li</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;/script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;p&gt;</span><span class="pln">What fruits do you like? Try to drag an element!</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;ol</span><span class="pln"> </span><span class="atn">ondragstart</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragStartHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-apple"</span><span class="tag">&gt;</span><span class="pln">Apples</span><span class="tag">&lt;/li&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-orange"</span><span class="tag">&gt;</span><span class="pln">Oranges</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-pear"</span><span class="tag">&gt;</span><span class="pln">Pears</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;/ol&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">ondragover</span><span class="pun">=</span><span class="atv">"</span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">false</span><span class="atv">"</span><span class="pln"> </span><span class="atn">ondrop</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dropHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;Drop your favorite fruits below:</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;ol</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"droppedFruits"</span><span class="tag">&gt;&lt;/ol&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;/div&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;html&gt;</span></li>
</ol></div>

In the above code, note:

+ _Line 44_: we define the drop zone (`ondrop=...`), and when a drag enters the zone we prevent event propagation (`ondragover="return false"`)
+ When we enter the `dragstart` listener (_line 5_), we copy the dragged-element's `data-value` attribute to the drag and drop clipboard with a name/key equal to "Fruit" (_line 11_),
+ When a drop occurs in the "drop zone" (the `<div>` at line 44), the `dropHandler(event)` function is called. This always occurs after a call to the `dragstart` handler. In other words: when we enter the `drop` handler, there must always be something on the clipboard! We use an event.`dataTransfer.setData(...)` in the dragstart handler, and an `event.dataTransfer.getData(...)` in the drop handler.
+ The `dropHandler` function is called (_line 15_), we get the object with a name/key equal to "Fruit" (_line 21_) from the clipboard , we create a `<li>` element (line 18), and set its value according to the value in that clipboard object (_lines 23-31_),
+ Finally we add the `<li>` element to the `<ol>` list within the drop zone `<div>`.

Notice that we use some CSS to set aside some screen-space for the drop zone (not presented in the source code above, but available in the online example):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">div </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;height</span><span class="pun">:</span><span class="pln"> </span><span class="lit">150px</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">150px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">float</span><span class="pun">:</span><span class="pln"> left</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid </span><span class="com">#666666; </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> </span><span class="com">#ccc;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;margin</span><span class="pun">-</span><span class="pln">right</span><span class="pun">:</span><span class="pln"> </span><span class="lit">5px</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">-</span><span class="pln">radius</span><span class="pun">:</span><span class="pln"> </span><span class="lit">10px</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;box</span><span class="pun">-</span><span class="pln">shadow</span><span class="pun">:</span><span class="pln"> inset </span><span class="lit">0</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="lit">3px</span><span class="pln"> </span><span class="com">#000;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;cursor</span><span class="pun">:</span><span class="pln"> move</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> li</span><span class="pun">:</span><span class="pln">hover </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> dashed </span><span class="com">#000;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 3.3.3 Drop detection

+ Procedure to handle drop
  1. in the `dragstart` handler, copy a value to in the drag and drop clipboard for later use
  2. define a "drop zone"
  3. write a `drop` handler, fetch content from the clipboard , and do something with it

+ Utilizing drag and drop clipboard
  + get the value of the data-value attribute from the dragged element w/ `dragStart` handler
  + copy the obtained value into "drag and drop clipboard"
  + data as key/value pair
  + example: `function dragStartHandler(evt) { evt.dataTransfer.setData("Fruit", evt.target.dataset.value); }`

+ Defining drop zone
  + any visible element if `drop` event listener attached
  + listen for `dragover` or `dragend` events and stop their propagation
  + mouse moving over any drop zone triggering `dragover` event
  + a few dragover events to be handled before the element finally dropped
  + `ondragover` handler used to avoid propagating `dragover` events
  + example: `<dic ondragover="return false" ondrop="dropHandler(event);">...</div>`

+ Processing fetched content w/ `drop` handler
  + `drop` event triggered once the dragged element placed
  + acquiring data from "drag and drop clipboard"
  + example: `function dropHandler(evt) { var data = evt.dataTransfer.getData("Fruit"); // do sth. w/ the data }`

+ Example: handling drag and drop
  + tasks
    + define drop zone and prevent event propagation
    + copy `data-value` of dragged element into drag'n'drop clipboard
    + handle `drop` event to fetch data and add dropped-item as a listed item
  + HTML snippet:
    + ordered list and listed item elements w/ [drag](#drag)
    + element for drop zone: `<div ondragover="return false" ondrop="dropHandler(evt);">Drop your favorite fruits below: <ol id="droppedFruits"></ol></div>`
  + JavaScript snippet
    + add drag handler: `function dragStartHandler(event) {...}`
      + log msg: `console.log('dragstart event, target: ' + event.target.innerHTML);`
      + copy dragged element into drag'n'drop clipboard: `event.dataTransfer.setData("Fruit", event.target.dataset.value);`
    + add drop handler: `function dropHandler(event) {...}`
      + log msg: `console.log('drop event, target: ' + event.target.innerHTML);`
      + create listed item: `var li = document.createElement("li");`
      + get data from drag'n'drop clipboard: `var data = event.dataTransfer,getData("Fruit");`
      + check data as apples: `if (data === 'fruit-apple') { li.textContent = 'Apples'; }`
      + check data as oranges: `else if (data === 'fruit-orange') { li.textContent = 'Orange'; }`
      + check data as pears: `else if (data === 'fruit-pears') { li.textContext = 'Pears'; }`
      + check data as other: `else { li.textContent = 'Unknown Fruit'; }`
      + add listed into page: `document.querySelector("#droppedFruits").appendChild(li);`








