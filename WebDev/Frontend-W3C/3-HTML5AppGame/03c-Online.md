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


#### Draggable attribute

In order to make any visible element draggable, add the `draggable="true"` attribute to any visible HTML5 element. Notice that some elements are draggable by default, such as `<img>` elements. In order to detect a drag, add an event listener for the

In order to detect a drag, add an event listener for the `dragstart` event:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;ol</span><span class="pln"> </span><strong><span class="atn">ondragstart</span><span class="pun">=</span><span class="atv">"</span><span class="pln">dragStartHandler</span><span class="pun">(</span><span class="pln">event</span><span class="pun">)</span><span class="atv">"</span></strong><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><strong><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span></strong><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-apple"</span><span class="tag">&gt;</span><span class="pln">Apples</span><span class="tag">&lt;/li&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><strong><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span></strong><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-orange"</span><span class="tag">&gt;</span><span class="pln">Oranges</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;li</span><span class="pln"> </span><strong><span class="atn">draggable</span><span class="pun">=</span><span class="atv">"true"</span></strong><span class="pln"> </span><span class="atn">data-value</span><span class="pun">=</span><span class="atv">"fruit-pear"</span><span class="tag">&gt;</span><span class="pln">Pears</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/ol&gt;</span></li>
</ol></div>

In the above code, we made all of the <li> elements draggable, and we detect a dragstart event occurring to any item within the ordered list: `<ol ondragstart="dragStarthandler(event)">`.

<p style="margin: 10px;">When you put an <code>ondragstart</code> handler on an element, each of its draggable children could fire the event! It's a sort of "inheritance of handlers"... In the above example, the handler is declared at the<code> &lt;ol&gt; level, so any subordinate</code>&nbsp;<code>&lt;li&gt;</code> element will fire the event.</p>

Try the following interactive example in your browser (just click and drag one of the list items) or [play with it at CodePen](https://codepen.io/w3devcampus/pen/MaWKZb).

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







