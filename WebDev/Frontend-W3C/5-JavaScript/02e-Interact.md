# Module 2: Adding interactivity to HTML documents



## 2.5 The DOM API


### 2.5.1 Introducing the DOM

When a user clicks on a link or enters a URL in the address of your Web browser, it downloads the page’s HTML text and builds up a model of the document’s structure called the DOM (Document Object Model). This model is used to render the HTML page on the screen.

The DOM is a standard  that describes how a document must be manipulated. It defines a “language- and platform neutral interface”. So, __every browser offers the same JavaScript DOM API.__

The DOM API is a programming interface the JavaScript programmer can use to modify the HTML content or the CSS style of HTML elements on the fly.

The DOM API provides the `document` object as a structured object, a group of nodes represented as a tree. We saw this in Module 1 when we revised the basic principles of HTML .

The `document` object also exposes a large set of methods to access and manipulate the structured document. Through the DOM, look for nodes (html elements that compose the page), move nodes, delete nodes, modify nodes (attributes, content), and also handle their associated events.

In JavaScript, the DOM is accessible through the property `document` of the global object `window`. We rarely manipulate the window object directly as it is implicit: `window.document` is the same as `document`. 

So by using this object, we can access and manipulate our page from JavaScript as a structured document.


#### Reminder from Module 1: HTML and the DOM

'Elements' are the pieces themselves, i.e., a paragraph, a header, and even the body are elements. Most elements can contain other elements - for example, the body element would contain header elements, paragraph elements, in fact pretty much all of the visible elements of the Document Object Model (developers call it the "DOM").

Let's take, for example, a simplified version of the last HTML code we showed you:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Your first HTML page</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;h1&gt;</span><span class="pln">My home page</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;p&gt;</span><span class="pln">Hi! Welcome to my Home Page! My name is Michel Buffa,</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> I'm a professor at the University of Côte d'Azur, in France,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> and I'm also the author <br></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">of two other W3CX MOOCS</span>.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;/p&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/body&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Click the red circle next to HTML to unfold this HTML document structure (we can also say "see its DOM structure"):

[CodePen Demo](https://codepen.io/w3devcampus/pen/BRNpYQ)

[Local Demo](src/02e-example01.html)

Consider the figure above.  It contains a single `html` element.  It turns out this includes within it the entire content of your html file.  If you click on the "html" red node, you'll find that it contains two components, a head and a body.  Clicking on each of these will reveal their respective contents.  This structure is what we computer scientists call a "tree".  Any given element (except for the outermost 'html' element) is wholly contained inside another element, referred to as the "parent" element.  Not surprisingly, the elements that a given element contains are its "child" elements.  And, yes, children of a common parent are often referred to as "siblings".

Thus in the example above, the top element is the html element, which contains just two elements, the head and body.  The head element contains a title element and the body contains an h1 element and a p element.  In a more typical example, the body would contain many more children, but for our purposes this is enough. p is for "paragraph" (the text between <p> and </p> will be separated by some space before the next element is displayed in the final HTML page rendering), h1 means "heading level 1", and will be rendered by default in bold with a bigger char size than any other text element, etc.


#### Different types of nodes in the DOM

There are different types of nodes, but don't worry - the most useful ones are highlighted in bold.

+ __Element (example: `<ul></ul>`)__
+ __Text (example: `<p>the text within the element p is a node of type text</p>`)__
+ Document, DocumentFragment, DocumentType (example: `<!doctype html>` for html5), Comment (example: `<!-- left column -->`), ProcessingInstruction (example: `<?php echo $name ?>`)

#### Exploring the DOM with the devtool console

You can explore the DOM with the devtool console. This time we used Firefox for exploring the DOM, as it proposes a good structured view of the DOM and of its properties/methods:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5lhj79m')"
    src    ="https://tinyurl.com/y48535lm"
    alt    ="Document.body in the FF devtool console"
    title  ="Document.body in the FF devtool console"
  />
</figure>


If you scroll down the right panel of the devtool console, as in the above screenshot, you will be able to look at all the properties, all the methods, all the event listeners:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5lhj79m')"
    src    ="https://tinyurl.com/yypdt53o"
    alt    ="document.body in the FF devtool console, continued"
    title  ="document.body in the FF devtool console, continued"
  />
</figure>


You can also use the "DOM inspector" to locate a particular element with the mouse: click the target icon and click on  the element on the page that you want to inspect, this time with Google Chrome, but you will find this option in all modern browsers' devtool consoles:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5lhj79m')"
    src    ="https://tinyurl.com/y23kfkrd"
    alt    ="DOM inspector in the browser devtools"
    title  ="DOM inspector in the browser devtools"
  />
</figure>


#### Notes for 2.5.1 Introducing the DOM

+ Overview of DOM
  + Document Object Model (DOM): a modle of the dicument's structure
  + used to render the HTML page on the screen
  + a standard describing how a document must be manipulated
  + defining a "language- and platform natural interface"
  + all browers offerring the same JS DOM API
  + DOM API:
    + a programming interface used to modify the HTML content ot the CSS style of HTML element on the fly
    + providing the `document` object as a structure object
  + `document` object
    + a group of nodes represented as a tree
    + exposing a large set of methods to access and manipulate the structured document
    + method capability:
      + look for nodes (html elements that compose the page)
      + move nodes
      + delete nodes
      + modify nodes (attributes, contents)
      + handle associated events
    + a propert of the global object `window`
    + implicitly `window.document` = `document`
  + types of nodes (most useful ones highlighted)
    + __element__, e.g., `<ul></ul>`
    + __text__, e.g., `<p>the text within the element p is a node of type text</p>`
    + Document, DocumentFragment, DocumentType, Comment, ProcessingInstruction
  + viewing DOM w/ devtool
    + Firfox: devtool > console > type "document.body"
    + Chrome: ([devtool video](https://youtu.be/VYyQv0CSZOE))
      + devtool > console > type "window"
      + devtool > console > type "inspec(document.querySelector("input"));" to focus on 'input' element


### 2.5.2 A warning about the DOM API

The DOM and the DOM API can be cumbersome and complicated. There are many methods and properties for manipulating the DOM tree, that are not "very JavaScript". There are historical reasons for this: the DOM wasn’t designed exclusively for JavaScript. Rather, it tries to define a language-neutral interface that can be used in other systems as well — not just HTML but also XML, which is a generic data format with an HTML-like syntax.

HTML5 made some additions that are not in the DOM API but which greatly help the JavaScript programmer (we'll see this in a minute with the "selector API", for example).

So we've decided to focus on only 20% of the DOM API and on the selector API (for selecting elements in the DOM). These are the most useful parts and it will give you enough knowledge to solve nearly every problem where you need to manipulate the DOM.


### 2.5.3 Accessing HTML elements

#### Live coding video: accessing HTML elements

<a href="https://edx-video.net/W3CJSIXX2016-V003100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/1qt6jhfu)

#### Accessing HTML elements with the selector API (recommended)

Extract from [HTML5 selectors API – It’s like a Swiss Army Knife for the DOM](https://tinyurl.com/1xy4oke0) : _"One of the many reasons for the success of JavaScript libraries like [jQuery](https://jquery.com/) and [Prototype](http://prototypejs.org/), on top of their easing the pain of cross-browser development was how they made working with the DOM far less painful than it had previously been, and indeed how it was with the standard DOM. Being able to use arbitrary CSS selector notation to get matching elements from a document made the standard DOM methods seem antiquated, or at the very least, far too much like hard work._

_Luckily, the standards and browser developers took notice. The W3C developed the Selectors API, a way of easily accessing elements in the DOM using standard CSS selector concepts, and browser developers have baked these into all modern browsers, way back to IE8."_

#### The `querySelector(CSSSelector)` and `querySelectorAll(CSSSelector)` methods

Ah... these methods owe a lot to [jQuery in OpenJS](https://jquery.org/)! They introduce a way to use CSS selectors (including CSS3 selectors) for requesting the DOM, like jQuery introduced ages ago.

Any CSS  selector can be passed as a parameter for these methods.

+ While `querySelector(selector)` <span style="color: brown;">will return the first element in the DOM that matches the selector</span> (and you will be able to work with it directly),
+ `querySelectorAll(selector)` <span style="color: brown; font-weight: bold;">returns a collection of HTML elements corresponding to all elements matching the selector</span>. To process the results, it will be necessary to loop over each of the elements in the collection.

__Typical use:__

Looking for an element in the whole document (the whole HTML page): call the `querySelector` method (or `querySelectorAll`) on the `document` object, that corresponds to the whole DOM tree of your web page:

[CodePen Demo](https://codepen.io/w3devcampus/pen/OpdaxM)

[Local Demo](src/02e-example02.html)


##### Source code from the above example:

HTML part: we have two buttons that will call a JavaScript function (_lines 2 and 6_) where we will manipulate the DOM), and we have four images, the first one with an id equal to "img1" (_lines 11, 14, 16 and 18_).

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">addBorderToFirstImage</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Add a border to the first image</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">resizeAllImages</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Resize all images</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/button&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Click one of the buttons above!</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://i.imgur.com/Ntvj5rq.png"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span style="color: #000000;" color="#000000">&nbsp; &nbsp; &nbsp;</span>id<span class="pun">=</span><span class="atv">"img1"</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp;width</span><span class="pun">=</span><span class="atv">200</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://i.imgur.com/yiU59oi.gif"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp;width</span><span class="pun">=</span><span class="atv">200</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://i.imgur.com/6FstYbc.jpg"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp;width</span><span class="pun">=</span><span class="atv">200</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://i.imgur.com/L97CyS4.png"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="atn">&nbsp; &nbsp; &nbsp;width</span><span class="pun">=</span><span class="atv">200</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;">...</li>
</ol></div>

__JavaScript part:__ the `init` function is executed as soon as the page is loaded (and the DOM is ready), in this function we add a shadow and margins to all images (_lines 3-21_). The two other functions are called when one of the HTML buttons is clicked (_line 23_ and _line 31_).

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> init</span><span class="pun">; // run init once the page is loaded</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // we're sure that the DOM is ready</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // before querying it</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // <strong>this function runs once the page is loaded</strong></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // add a shadow to all images</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // <strong>select all images</strong></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> listImages </span><span class="pun">=</span><strong><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"img"</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // change all their width to 100px</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; listImages</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">img</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // img = current image</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // add a shadow 5px left, 5 pixel down, 15px blur, 5px spread</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // grey</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; img</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">boxShadow </span><span class="pun">=</span><span class="pln"> </span><span class="str">"5px 5px 15px 5px grey"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>// add a margin 10px on each side</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; img</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">margin </span><span class="pun">=</span><span class="pln"> </span><span class="str">"10px"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> addBorderToFirstImage</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // select the first image with id = img1</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> img1 </span><span class="pun">=</span><strong><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#img1'</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Add a red border, 3px wide</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; img1</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">border </span><span class="pun">=</span><span class="pln"> </span><span class="str">'3px solid red'</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> resizeAllImages</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // select all images</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> listImages </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"img"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // change all their width to 100px</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; listImages</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">img</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // img = current image, we resize it by changing its</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // width attribute</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; img</span><span class="pun">.</span><span class="pln">width </span><span class="pun">=</span><span class="pln"> </span><span class="lit">100</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Miscellanous examples of use of querySelector(CSSSelector) and querySelectorAll(CSSselector)

Here are some other examples that use more complicated CSS selectors. If you are not familiar with their syntax, we recommend that you follow the CSS basics, and HTML5 and CSS fundamentals courses from [W3Cx](https://www.edx.org/school/w3cx).


__Example #1: get all `<li>` directly in a `<ul>` of class nav__

[CodePen](https://codepen.io/w3devcampus/pen/evxQMr)

[Local Demo](src/02e-example03.html)


Source code extracts:

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><strong><span class="pln">firstLiClassRedInUl</span></strong><span class="pun"><strong>()</strong>;</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Select first li of class red and color it in red</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><strong><span class="pln">allLisInUlOfClassNav</span></strong><span class="pun"><strong>()</strong>;</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Underline All li in a ul of class nav</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;ul</span><span class="pln"> </span><strong><span class="atn">class</span><span class="pun">=</span><span class="atv">"nav"</span></strong><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;li&gt;</span><span class="pln">Home</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;li</span><span class="pln"> </span><strong><span class="atn">class</span><span class="pun">=</span><span class="atv">"red"</span></strong><span class="tag">&gt;</span><span class="pln">Products</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;li&gt;</span><span class="pln">About</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/ul&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> Another list:</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;ul&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;li&gt;</span><span class="pln">Apple</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;li</span><span class="pln"> </span><strong><span class="atn">class</span><span class="pun">=</span><span class="atv">"red"</span></strong><span class="tag">&gt;</span><span class="pln">Cherries</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;li&gt;</span><span class="pln">Oranges</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/ul&gt;</span></li>
</ol></div>

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">function</span><span class="pln"> firstLiClassRedInUl</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // first li of class="red" in a ul</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> elm </span><span class="pun">=</span><strong><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"ul li.red"</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; elm</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> allLisInUlOfClassNav</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // get all li directly in a ul of class nav</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> list </span><span class="pun">=</span><strong><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"ul.nav &gt; li"</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">elm</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; elm</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">textDecoration </span><span class="pun">=</span><span class="pln"> </span><span class="str">"underline"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; })</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Example #2: display all checked `<input type="checkbox">` elements located inside an element of a given id__

[CodePen Demo](https://codepen.io/w3devcampus/pen/MpLzqV)

[Local Demo](src/02e-example04.html)


Extract from the source code:

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><strong><span class="pln">displayListOfCheckedItems</span><span class="pun">();</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">&nbsp; &nbsp; Show Checked items</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;ul</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"fruits"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fruit"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"apples"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Apples</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;/li&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;li&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fruit"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"oranges"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Oranges</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;/li&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;li&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fruit"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"bananas"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Bananas</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;li&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"fruit"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"grapes"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Grapes</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;/li&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/ul&gt;</span></li>
</ol></div>

JavaScript code: we select all elements of type `input` that have an attribute `checked` equal to `true`, and located inside an element whose id is "fruits". Notice the use of `document.querySelectorAll`, for selecting more than one element (_line 6_), then, we iterate on the list (__line 8_) and concatenate to the string variable `listOfSelectedValues` the value of each element (located in its `value` attribute). This is done in _line 9_.

_Lines 9-12_ use the `parentNode` property of the selected nodes in order to change the color of the `<li>` (parents of `<input>` elements selected) in red. In the DOM tree, we selected input elements that are each a child of a `<li>` element. The text displayed: "Apples", "Oranges" etc. belong to the `<li>` element. In order to access it from the `<input>` child we selected, we use elm.parentNode.

Finally, at the end of the document, _line 14_ adds a message followed by this list:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> displayListOfCheckedItems</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // all inputs that have been checked</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> listOfSelectedValues</span><span class="pun">=</span><span class="str">""</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> list </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"#fruits input:checked"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">elm</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; listOfSelectedValues </span><span class="pun">+=</span><span class="pln"> elm</span><span class="pun">.</span><span class="pln">value </span><span class="pun">+</span><span class="pln"> </span><span class="str">" "</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Put the li in red.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // the li is the parent of the current input elem stored</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // in the elm variable</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; elm</span><span class="pun">.</span><span class="pln">parentNode</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; });</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">"You selected: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> listOfSelectedValues</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Example #3: change the background of all paragraphs <p> in an element of a given id__

[CodePen](https://codepen.io/w3devcampus/pen/LWqqqm)

[Local Demo](src/02e-3xample05.html)


HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><strong><span class="pln">changeBackGroundOfPs</span><span class="pun">(</span><span class="str">'firstDiv'</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Change backgrounds of p under a given element known by id</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;div</span><span class="pln"> </span><strong><span class="atn">id</span><span class="pun">=</span><span class="atv">"firstDiv"</span></strong><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;p&gt;</span><span class="pln">First paragraph.</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;p&gt;</span><span class="pln">Second paragraph.</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/div&gt;</span></li>
</ol></div>

JavaScript code: we build a CSS selector using the id passed as a parameter. In this example, the id is 'firstDiv', the id of the div at _line 3_ in the above code.

So, the variable CSS selector at _line 2_ in the JavaScript code below will have a value equal to "`#firstDiv p`", that means: select all `<p>` under an element whose `id` is "firstDiv". The `paragraphs` variable is a list that contains the paragraphs selected. Then we iterate on this list (this time using a for loop, which is an alternative method to using the forEach method used in previous examples) (_lines 5-7_), and we change the background of all selected paragraphs (_line 6_).

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> changeBackGroundOfPs</span><span class="pun">(</span><span class="pln">id</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> paragraphs&nbsp;</span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"#"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> id </span><span class="pun">+</span><span class="pln"> </span><span class="str">" p"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // Another way to iterate on all elements in a collection</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> paragraphs</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++</span><span class="pln"> </span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;paragraphs</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">style</span><span class="pun">.</span><span class="pln">backgroundColor </span><span class="pun">=</span><span class="pln"> </span><span class="str">"lightGreen"</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; }</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

#### Other examples that use more complex selectors:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="com" style="font-family: 'courier new', courier;">// all elements li in ul elements in an element of id=nav</span></li>
<li class="L1"><span class="kwd">var</span><span class="pln"> el </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#nav ul li'</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L2"><span class="pln"> </span></li>
<li class="L3"><span class="com">// all li in a ul, but only even elements</span></li>
<li class="L4"><span class="kwd">var</span><span class="pln"> els </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">'ul li:nth-child(even)'</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5"><span class="pln"> </span></li>
<li class="L6"><span class="pln"> </span></li>
<li class="L7"><span class="com">// all td directly in tr in a form of class test</span></li>
<li class="L8"><span class="kwd">var</span><span class="pln"> els </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">'form.test &gt; tr &gt; td'</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L9"><span class="pln"> </span></li>
<li class="L0"><span class="com">// all paragraphs of class warning or error</span></li>
<li class="L1"><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"p.warning, p.error"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L2"><span class="pln"> </span></li>
<li class="L3"><span class="com">// first element of id=foo or id=bar</span></li>
<li class="L4"><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#foo, #bar"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5"><span class="pln"> </span></li>
<li class="L6"><span class="com">// first p in a div</span></li>
<li class="L7"><span class="kwd">var</span><span class="pln"> div </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"bar"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8"><span class="kwd">var</span><span class="pln"> p </span><span class="pun">=</span><span class="pln"> div</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"p"</span><span class="pun">);</span><span class="pln"> </span></li>
</ol></div>

#### Accessing HTML elements with the DOM API (old fashioned)

These methods are from the DOM API and can all be replaced by the querySelector and querySelectorAll methods that we've discussed. They are still used in many JavaScript applications, and are very simple to understand.

From the document we can access the elements composing our Web page in a few ways:

+ __document.getElementById(identifier)__ returns the element which has the id “identifier”.

  This is equivalent to `document.querySelector("#identifier');` (just add a # before the id when using a CSS selector). 

  Example: `var elm = document.getElementById('myDiv');` is equivalent to `document.querySelector('#myDiv');`

+ __document.getElementsByTagName(tagName)__ returns a list of elements which are named “tagName”.

  This is equivalent to `document.querySelectorAll(tagName);`

  Example: `var list = document.getElementByTagName('img');` is equivalent to `document.querySelector('img');`

+ __document.getElementsByClassName(className)__ returns a list of elements which have the class “className”.

  This is equivalent to `document.querySelectorAll('.className');` 

  Example: `var list = document.getElementByClassName('important'); is equivalent to document.querySelector('.important');` (just add a '.' before the class name when using a CSS selector). 

Notice that `identifier`, `tagName` and `className` must be of type String.


#### Notes for 2.5.3 Accessing HTML elements

+ The `selector` API
  + a way of easily accessing elements in the DOM
  + a way to use CSS selector for requesting the DOM
  + methdos
    + `querySelector`: return the 1st element int he DOM that matched the selector
    + `querySelectorAll`: return a collection of HTML elements of all elements matching the selector
  + example: [typical usage](src/02e-example02.html)
    + HTML: `<img src="https://i.imgur.com/Ntvj5rq.png" id="img1" width=200> <img src="https://i.imgur.com/yiU59oi.gif" width=200>`
    + JavaScript
      + initialization: `window.onload = init;`
      + `init` function executed as soon as the page loaded (DOME ready)

        ```js
        function init() {
            var listImages = document.querySelectorAll("img");

            listImages.forEach(function(img) {
                img.style.boxShadow = "5px 5px 15px 5px grey";
                img.style.margin = "10px";
            });
        }
        ```

      + manipulate the firs image

        ```js
        function addBorderToFirstImage() {
            var img1 = document.querySelector('#img1');
            img1.style.border = '3px solid red';
        }
        ```

      + manipulate all images
 
        ```js
        function resizeAllImages() {
            var listImages = document.querySelectorAll("img");
            listImages.forEach(function(img) {
                img.width = 100;
            });
        }
        ```

  + example: [get all `<li>` directly in a `<ul>` of class nav](src/02e-example03.html)
  + example: `var list = document.querySelectorAll("#fruits input:checked");` in [display all checked `<input type="checkbox">` elements](src/02e-example04.html)
  + example: [change the back ground of all paragraphs](src/02e-example04.html)
    + HTML: `<button onclick="changeBackGroundOfPs('firstDiv');">Change backgrounds of p under a given element known by id</button>`
    + JavaScript: `var paragraphs = document.querySelectorAll("#" + id + " p");`
  + examples: more complex selectors
    + `var el = document.querySelector('#nav ul li');`: all elements li in ul elements in an element of id=nav
    + `var els = document.querySelectorAll('ul li:nth-child(even)');`: all li in a ul, but only even elements
    + `var els = document.querySelectorAll('form.test > tr > td');`: all td directly in tr in a form of class test
    + `querySelectorAll("p.warning, p.error");`: all paragraphs of class warning or error
    + `querySelector("#foo, #bar");`: first element of id=foo or id=bar
    + `var div = document.getElementById("bar"); var p = div.querySelector("p");`: first p in a div

+ The `getElement` APIs
  + able to be replaced by `querySelector` and `querySelectorAll` methods
  + `document.getElementById(identifier)`
    + return the element which has the id “identifier”.
    + equivalent to `document.querySelector("#identifier');`
    + `var elm = document.getElementById('myDiv');` = `document.querySelector('#myDiv');`
  + `document.getElementsByTagName(tagName)`
    + return a list of elements which are named “tagName”.
    + equivalent to `document.querySelectorAll(tagName);`
    + example: `var list = document.getElementByTagName('img');` = `document.querySelector('img');`
  + `document.getElementsByClassName(className)`
    + return a list of elements which have the class “className”.
    + equivalent to `document.querySelectorAll('.className');`
    + example: `var list = document.getElementByClassName('important');` = `document.querySelector('.important');`


### 2.5.4 Changing the style of selected HTML elements


#### The `style` attribute

How to modify an HTML element's CSS properties from JavaScript?

The most common way to modify the CSS style of one of several elements you selected using the DOM or Selector API, is to use the `style` attribute.

Typical use:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// select the paragraph with id = "paragraph1" </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> p </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#paragraph1'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// change its color</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">p</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
</ol></div>


_Warning_: with the style attribute, you can modify (or read) any CSS property, but be careful: the syntax changes a little due to the fact that in JavaScript the "-" is a math operator, while in CSS it is used to separate properties made of multiple words, such as background-color.

When using such properties from JavaScript, the rule is simple:

1. Remove the "-" sign,
1. Capitalize the word after the "-" sign!

Simple, isn't it?

Examples:

+ `text-align` becomes `style.textAlign`
+ `margin-left` becomes `style.marginLeft`
+ etc.

The most useful CSS properties (we do recommend that you follow the W3Cx courses CSS basics, CSS and HTML5 fundamentals from W3Cx to learn more about CSS):

+ `color`: changing the color of the text content of selected element(s),
+ `background-color`: same but this time the background color,
+ `margin` and `padding` properties (external and internal margins), including their variants: `margin-left`, `margin-top`, `margin-right`, `margin-bottom`, also `padding-left`, etc.
+ `border` and `border-radius`: change the border, type (plain, dashed), color, thickness, rounded corners etc.
+ `box-shadow` to add shadows to selected elements, 
+ `font`, `font-style`: font characters and style (italic, bold, plain)
+ `text-align` (centered, etc.)

Here are some examples:

[CodePen Demo](https://codepen.io/w3devcampus/pen/evxoQq)

[Local Demo](src/02e-example06.html)


#### Using the ClassList interface to change more than one CSS property simultaneously

External resources:

+ [The W3C specification about the classList DOM interface](http://www.w3.org/TR/dom/#dom-element-classlist)
+ [An article from the Mozilla Developer's web site](https://hacks.mozilla.org/2010/01/classlist-in-firefox-3-6/)

Until now, to manipulate CSS classes of an HTML element was a bit complex, both for verifying the presence of a class name in an element, and for adding or removing classes associated with a given element.

The ClassList interface simplifies it all by acting as a container object and by providing a set of methods to manipulate its content.

The `classList` property applies to an HTML element, and returns a collection of class names:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> elem</span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.querySelector</span><span class="pun">(</span><span class="str">"#id1"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> allClasses </span><span class="pun">=</span><span class="pln"> elem</span><span class="pun">.</span><strong><span class="pln">classList</span></strong><span class="pun">;</span></li>
</ol></div>


#### The classList API

The list of methods usable on a classList object are `add()`, `remove()`, `toggle()` and `contains()`.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// By default, start without a class in the div: &lt;div class=""/&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Set "foo" as the class by adding it to the classList</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">div</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="str">'foo'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// now &lt;div class="foo"/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// Check that the classList contains the class "foo"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">div</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">contains</span><span class="pun">(</span><span class="str">'foo'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// returns true</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// Remove the class "foo" from the list</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">div</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">remove</span><span class="pun">(</span><span class="str">'foo'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// now &lt;div class=""/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// Check if classList contains the class "foo"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">div</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">contains</span><span class="pun">(</span><span class="str">'foo'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// returns false: "foo" is gone</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// Check if class contains the class "foo",</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// If it does, "foo" is removed, if it doesn't, it's added</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">div</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">toggle</span><span class="pun">(</span><span class="str">'foo'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// class set to &lt;div class="foo"/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">div</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">toggle</span><span class="pun">(</span><span class="str">'foo'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// class set to &lt;div class=""/&gt;</span></li>
</ol></div>


__Another example: add and remove multiple CSS properties in a list of checkboxes__

[CodePen Demo](https://codepen.io/w3devcampus/pen/GWeJzz)

[Local Demo](src/02e-example07.html)


This is a variation of an example from a previous section. This time, when the `<input type="checkbox">` elements have been checked, in order to give the parent `<li>` a background color, a border, and to change the text color, we use a CSS class named "checked":

CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">.</span><span class="kwd">checked</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> dashed </span><span class="com">#000;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> green</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="pln">yellow</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

... and the `classList.add(CSS_class)` and `classList.remove(CSS_class)` methods on the `<li>` elements:

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> displayListOfCheckedItems</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // all inputs that have been checked</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> listOfSelectedValues</span><span class="pun">=</span><span class="str">""</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> list </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"#fruits input:checked"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">elm</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; listOfSelectedValues </span><span class="pun">+=</span><span class="pln"> elm</span><span class="pun">.</span><span class="pln">value </span><span class="pun">+</span><span class="pln"> </span><span class="str">" "</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; <strong>// get the li parent of the current selected input</strong></span></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> liParent </span><span class="pun">=</span><span class="pln"> elm</span><span class="pun">.</span><span class="pln">parentNode</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; // add the CSS class .checked</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; liParent</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="str">"checked"</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; });</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">"You selected: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> listOfSelectedValues</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> reset</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> list </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"#fruits input"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">elm</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // uncheck</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; elm</span><span class="pun">.</span><span class="kwd">checked</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; <strong>// remove CSS decoration</strong></span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> liParent </span><span class="pun">=</span><span class="pln"> elm</span><span class="pun">.</span><span class="pln">parentNode</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; liParent</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">remove</span><span class="pun">(</span><span class="str">"checked"</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; });</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 2.5.4 Changing the style of selected HTML elements

+ The `style` attribute
  + most common way to modify the CSS style of one of several elements
  + typical usage: `var p = document.querySelector('#paragraph1'); p.style.color = 'red';`
  + rule to change syntax of attribute in JS
    + remove the "-" sign in CSS attributes if presented
    + catptalize the word after the "-" sign
    + example: 1text-align` $\to$ `style.textAlign`, `margin-left` $\to$ `style.marginLeft`
  + most useful CSS properties
    + `color`: changing the color of the text content of selected element(s)
    + `background-color`: the background color of the select element(s)
    + `margin` and `padding`: external and internal margins, including `margin-top`, `margin-left`, `margin-bottom`, and `margin-right` and also `padding-top`, etc.
    + `border` and `border-radius`: chnage the border, type, color, thickness, rounded corners, etc.
    + `box-shadow`: add shadow to selected elements
    + `font` and `font-style`: font characterrs and style (italic, bold, plain)
    + `text-align`: text alignment
  + examples: `p.style.backgroundColor = 'lightGreen';`, `p.style.marginLeft = '100px';`, and `p.style.border = '2px solid blue';`

+ The `ClassList` interface
  + simplifying to manipulate CSS classes of an HTML element
  + acting as a container object and providing a set of methods to manipulate its conetnt
  + applyied to an HTML element and returning a collection of class names
  + typical usage: `var elem = document.querySelector("#id1"); var allClasses  elem.classList;`
  + methods usable on a classList objet
    + methods: `add()`, `remove()`, `toggle()` and `contains()`
    + typical usages:
      + `div.classList.add('foo');`: set "foo" as the class by adding it to the classList
      + `div.classList.contains('foo');`: check that the classList contains the class "foo"
      + `div.classList.remove('foo');`: remove the class "foo" from the list
      + `div.classList.toggle('foo');`: add if not existed or remove if existed the class "foo"
  + example: [add and remove multiple CSS properties](src/02e-example07.html)

    ```js
    function displayListOfCheckedItems() {
      var listOfSelectedValues="";
      var list = document.querySelectorAll("#fruits input:checked");

      list.forEach(function(elm) {
        listOfSelectedValues += elm.value + " ";
        var liParent = elm.parentNode;
        liParent.classList.add("checked");
      });
      document.body.append("You selected: " + listOfSelectedValues);
    }
    
    function reset() {
      var list = document.querySelectorAll("#fruits input");
      list.forEach(function(elm) {
        elm.checked = false;
        var liParent = elm.parentNode;
        liParent.classList.remove("checked");
      });
    }
    ```


### 2.5.5 Modifying selected HTML elements

We've already seen many examples in which we selected one or more elements, and modified their content. Let's summarize all the methods we've seen, and perhaps introduce a few new things...

#### Properties that can be used to change the value of selected DOM node

##### Using the `innerHTML` property

This property is useful when you want to change all the children of a given element. It can be used to modify the text content of an element, or to insert a whole set of HTML elements inside another one.

Typical use:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> elem </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#myElem'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">elem</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Hello '</span><span class="pun">;</span><span class="pln"> </span><span class="com">// replace content by Hello</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">elem</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'&lt;b&gt;Michel Buffa&lt;/b&gt;'</span><span class="pun">,</span><span class="pln"> </span><span class="com">// append at the end </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Michel Buffa in bold</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">elem</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Welcome'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> elem</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">;</span><span class="pln"> </span><span class="com">// insert Welcome </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// at the beginning</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">elem</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span><span class="pln"> </span><span class="com">// empty the elem</span></li>
</ol></div>

#### Using the `textContent` property

It's also possible, with selected nodes/elements that contain text, to use the textContent property to read the text content or to modify it. There are subtle differences that can be seen in the above example (click the 'edit on CodePen" part on the top left, and once in codePen, open the devtool console):

[CodePen Demo](https://codepen.io/w3devcampus/pen/MpxEdj)

[Local Demo](src/02e-example08.html)

Extract from the HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"first"</span><span class="tag">&gt;</span><span class="pln">first paragraph</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"second"</span><span class="tag">&gt;&lt;em&gt;</span><span class="pln">second</span><span class="tag">&lt;/em&gt;</span><span class="pln"> paragraph</span><span class="tag">&lt;/p&gt;</span></li>
</ol></div>

JavaScript code: the comments after lines that start with `console.log` correspond to what is printed in the devtool debug console. Notice the difference between the `textNode` value and the `innerHTML` property values at _lines 13-14_: while `textContent` returns only the text inside the second paragraph, innerHTML also returns the `<em>...</em>` that surrounds it. However, when we modify the `textContent` value, it also replaces the text decoration (the `<em>` is removed), this is done at _lines 16-20_.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> init</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// DOM is ready</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> firstP </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#first"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">firstP</span><span class="pun">.</span><span class="pln">textContent</span><span class="pun">); //&nbsp;</span>"first paragraph"</li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">firstP</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">); &nbsp;&nbsp;</span>//&nbsp;<span style="background-color: #eeeeee;">"first paragraph"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;firstP</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Hello I'm the first paragraph"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">firstP</span><span class="pun">.</span><span class="pln">textContent</span><span class="pun">); //&nbsp;</span>"Hello I'm the first paragraph"</li>
<li class="L2">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> secondP </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#second"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">secondP</span><span class="pun">.</span><span class="pln">textContent</span><span class="pun">); //&nbsp;</span>"second paragraph"</li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">secondP</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">); &nbsp; //&nbsp;</span>"&lt;em&gt;second&lt;/em&gt; paragraph"</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;secondP</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Hello I'm the second paragraph"</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">secondP</span><span class="pun">.</span><span class="pln">textContent</span><span class="pun">); //&nbsp;</span>"Hello I'm the second</li>
<li class="L6" style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// paragraph"</li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">secondP</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">); &nbsp;&nbsp;</span>//&nbsp;"Hello I'm the second</li>
<li class="L6">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// paragraph"</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Changing the attributes of selected elements

It's very common to modify the attributes of selected elements: the width of an image, CSS style with the style attribute, value of an input field, etc.

This example shows some of the things we can do:

[CodePen Demo](https://codepen.io/w3devcampus/pen/RpdjwE)

[Local Demo](src/02e-example09.html)


#### Notes for 2.5.5 Modifying selected HTML elements

+ Value of a selected DOM node
  + the `innerHTML` property
    + useful when changing all the children of a given element
    + used to modify the text content of an element or insert a whole set of HTML element inside another one
    + including all contents and child elements
    + example: `var elem = document.querySelector('#myElem');`
      + replace conetnt: `elem.innerHTML = 'Hello ';`
      + append conetnt: `elem.innerHTML += '<b>Michel Buffa</b>',`
  + the `textContent` property
    + used to read the text content or to modify the content
    + only containing the text content
  + example: `<p id="second"><em>second</em> paragraph</p>`
    + `console.log(secondP.textContent);` $\to$ `<em>second</em> paragraph`
    + `console.log(secondP.innerHTML);` $\to$ `second paragraph`
  + modifying the attributes
    + using `value` property of objects
    + examples: `colorChooser.value = "#00FF00";`, `number.value = 10; number.step = "0.1"; number.max = 11;`, `img.src="n_400x400.jpg"; img.width=250;`


### 2.5.6 Adding new elements to the DOM

The DOM API comes with a set of methods you can use on DOM elements.

In general, to add new nodes to the DOM we follow these steps:

1. Create a new element by calling the `createElement()` method, using a syntax like:

  <div class="source-code"><ol class="linenums" style="list-style: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> elm </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="pln">name_of_the_element</span><span class="pun">).</span><span class="pln"> </span></li>
  </ol></div>

  Examples:

  <div class="source-code"><ol class="linenums" style="list-style: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> li </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'li'</span><span class="pun">);</span><span class="pln"> </span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> img </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'img'</span><span class="pun">);</span><span class="pln"> etc</span><span class="pun">.</span></li>
  </ol></div>

2. Set some attributes / values  / styles for this element.

  Examples:

  <div class="source-code"><ol class="linenums" style="list-style: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">li</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">'&lt;b&gt;This is a new list item in bold!&lt;/b&gt;'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// can add HTML in it</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">li</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Another new list item'</span><span class="pun">;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">li</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// green text</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">img</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://..../myImage.jpg"</span><span class="pun">;</span><span class="pln"> </span><span class="com">// url of the image</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">img</span><span class="pun">.</span><span class="pln">width </span><span class="pun">=</span><span class="pln"> </span><span class="lit">200</span><span class="pun">;</span></li>
  </ol></div>

3. Add the newly created element to another element in the DOM, using `append()`, `appendChild()`, `insertBefore()` or the `innerHTML` property

  Examples:

  <div class="source-code"><ol class="linenums" style="list-style: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> ul </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#myList'</span><span class="pun">);</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">ul</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="pln">li</span><span class="pun">);</span><span class="pln"> </span><span class="com">// insert at the end, appendChild() could also be used (old)</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">ul</span><span class="pun">.</span><span class="pln">prepend</span><span class="pun">(</span><span class="pln">li</span><span class="pun">);</span><span class="pln"> </span><span class="com">// insert at the beginning</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pln">ul</span><span class="pun">.</span><span class="pln">insertBefore</span><span class="pun">(</span><span class="pln">li</span><span class="pun">,</span><span class="pln"> another_element_child_of_ul</span><span class="pun">);</span><span class="com">// insert in the middle</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="pln">img</span><span class="pun">);</span><span class="pln"> </span><span class="com">// adds the image at the end of the document</span></li>
  </ol></div>


#### Examples

__Example #1: use of the `createElement()`, `append()` methods and of the textContent attribute__

[CodePen Demo](https://codepen.io/w3devcampus/pen/aWeqzO)

[Local Demo](src/02e-example10.html)

HTML code extract: we use an `<input type="number">` for entering a number (_line 2_). Then if one clicks on the "Add to the list" button, the `add()` JavaScript function is called (_line 3_), this will add the typed number to the empty list at _line 7_. If one presses the "reset" button, it will empty this same list by calling the `reset()` JavaScript function.

<div class="source-code"><ol class="linenums" style="list-style: decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"newNumber"</span><span class="tag">&gt;</span><span class="pln">Please enter a number</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"number"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"newNumber"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">0</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><strong><span class="pln">add</span><span class="pun">();</span></strong><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Add to the list</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><strong><span class="pln">reset</span><span class="pun">();</span></strong><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Reset list</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span><span class="pln">You entered:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;ul</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"numbers"</span><span class="tag">&gt;&lt;/ul&gt;</span></li>
</ol></div>

JavaScript code extract: notice at _line 25_ the use of the innerHTML property for resetting the content of the `<ul>` list. innerHTML corresponds to all the sub DOM contained inside the `<ul>...</ul>`. InnerHTML can be used for adding/deleting/modifying a DOM node's content.

<div class="source-code"><ol class="linenums" style="list-style: decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> add</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // get the current value of the input field</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> val </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#newNumber'</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; if</span><span class="pun">((</span><span class="pln">val </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="pun">(</span><span class="pln">val </span><span class="pun">!==</span><span class="pln"> </span><span class="str">""</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // val exists and non empty</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // get the list of numbers. It's a &lt;ul&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> ul </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#numbers"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // add it to the list as a new &lt;li&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> newNumber </span><span class="pun">=</span><strong><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">"li"</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>newNumber</strong></span><strong><span class="pun">.</span><span class="pln">textContent </span><span class="pun">=</span><span class="pln"> val</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // or newNumber.innerHTML = val</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ul</strong></span><strong><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="pln">newNumber</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; }</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> reset</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // get the list of numbers. It's a &lt;ul&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> ul </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#numbers"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // reset it: no children</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>ul</strong></span><strong><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span></strong><span class="pun"><strong>;</strong> &nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Example #2: using the innerHTML property to add new elements__

This is the same example, but in an abbreviated form, using the `innerHTML` property:

[CodePen Demo](https://codepen.io/w3devcampus/pen/jBJbqM)

[Local Demo](src/02e-example11.html)


#### Notes for 2.5.6 Adding new elements to the DOM

+ Adding new node w/ the DOM API
  + create a new element by calling `createEelement()` method
    + syntax: `var elm = document.createElement(name_of_the_element)`
    + example: `var li = document.createElement('li');`
  + set some attributes / values / styles for this element, e.g.,
    + `li.innerHTML = '<b>This is a new list item in bold!</b>';` & `li.textContent = 'Another new list item';`
    + `li.style.color = 'green';`
    + `img.src = "https://..../myImage.jpg";` & `img.width = 200;`
  + add the newly created element to another element in the DOM
    + using `append()`, `appendChild()`, `insertBefore()` or the `innerHTML` property
    + examples: `var ul = document.querySelector('#myList');`
      + `ul.append(li);`: insert at the end, appendChild() could also be used (old)
      + `ul.prepend(li);`: insert at the beginning
      + `ul.insertBefore(li, another_element_child_of_ul);`: insert in the middle
      + `document.body.append(img);`: adds the image at the end of the document


### 2.5.7 Moving HTML elements in the DOM

The `append()`, `appendChild()` methods normally adds  a new element to an existing one, as shown in this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> li </span><span class="pun">=</span><span class="pln"> createElement</span><span class="pun">(</span><span class="str">'li'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;">ul<span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="pln">li</span><span class="pun">); // adds the new li to the ul element</span></li>
</ol></div>

One interesting thing to know is that if we do not create the new element, but rather get it from somewhere else in the document, it is then removed from its parents and added to the new parent.

In other words: it moves from its original location to become a child of the targetElem.


#### Examples

__Example #1: a simple one__

[CodePen Demo](https://codepen.io/w3devcampus/pen/peYyPz)

[Local Demo](src/02e-example12.html)


__Example #2: a more significant example, that also uses drag'n'drop__

Notice that this example comes from the HTML5 advanced course. Our plan here is not to explain drag'n'drop in detail, but to show how `append()` can be used to move an element.

In this example, when a user starts to drag an element, the `drag()` JavaScript function is called. In this function we use the drag'n'drop clipboard to store the id of the image that is being dragged.

When the image is dropped, the `drop()` method is called. As the drop event listener is declared on the two divs (on the left and the right), we just call `append()` on the target div element, and this will add the dragged image to the div, while removing it from its original location.

[CodePen Demo](https://codepen.io/w3devcampus/pen/xwxEZg)

[Local Demo](src/02d-example13.html)


#### Notes for 2.5.7 Moving HTML elements in the DOM

+ Moving HTML elements
  + `append()`, `appendChild()`: adding a new element to an existing one
  + example: `var li = createElement('li'); ul.append(li);`
  + moving from its original location to become a child of the targetElem
  + example: [drag'n'drop](src/02d-example13.html)
    + HTML: 
      + select element to drag: `<img src="https://.../ABiBCwZ.png" id="cr" ondragstart="drag(this, event)" alt="Logo Chrome">`
      + destination to place elemen: `<div class="box" ondragover="return false" ondrop="drop(this, event)">`
    + Javascript

      ```js
      function drag(target, evt) {
        evt.dataTransfer.setData("browser", target.id);
      }

      function drop(target, evt) {
        var id = evt.dataTransfer.getData("browser");
        
        target.appendChild(document.getElementById(id));
        evt.preventDefault();
      }
      ```


### 2.5.8 Removing elements from the DOM


#### Removing elements using the `removeChild()` method

Let's take an example that we've already encountered. This time, you will check the elements you want to remove from the list!

[CodePen Demo](https://codepen.io/w3devcampus/pen/NpJxdX)

[Local Demo](src/02e-example14.html)


JavaScript code extract: we need to get the `<ul>` that contains all the `<li><input type="checkbox"></li>` elements (_line 3_). This is the element we will use for calling `removeChild(...)`. The loop on the checked element (_lines 5-12_) iterates on a list of checked input elements. In order to make both the text (Apples, Oranges, etc.) AND the checkbox disappear, we need to access the different `<li>` elements that contain the selected checkboxes. This is done in line 10. Then, we can call ul.removeChild(li) on the `<ul>` for removing the `<li>` that contains the selected element (_line 11_). 

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> removeSelected</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> list </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"#fruits input:checked"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; <strong>var</strong></span><strong><span class="pln"> ul </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#fruits"</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">elm</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // elm is an &lt;input type="checkbox"&gt;, its parent is a li</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // we want to remove from the &lt;ul&gt; list</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // when we remove the &lt;li&gt;, the &lt;input&gt; will also</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // be removed, as it's a child of the &lt;li&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; <strong>var</strong></span><strong><span class="pln"> li </span><span class="pun">=</span><span class="pln"> elm</span><span class="pun">.</span><span class="pln">parentNode</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>ul</strong></span><strong><span class="pun">.</span><span class="pln">removeChild</span><span class="pun">(</span><span class="pln">li</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; });</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Removing all children of an element using the `innerHTML` property

In the same example, if you look at the `reset()` JavaScript function, we use the ul's innerHTML property both for emptying the list (_lines 3-4_) and for appending to it all the initial HTML code (_lines 6-17_):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> reset</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; var</span><span class="pln"> ul </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#fruits"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; <strong>// Empty the &lt;ul&gt;</strong></span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; ul</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; // Adds each list item to the &lt;ul&gt; using innerHTML += ...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>ul</strong></span><strong><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span></strong><span class="pln"> </span><span class="str">"&lt;li&gt;&lt;input type='checkbox' name='fruit' &nbsp; <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='apples'&gt;Apples&lt;/li&gt;"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>ul</strong></span><strong><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span></strong><span class="pln"> </span><span class="str">"&lt;input type='checkbox' name='fruit' <br></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='oranges'&gt;Oranges&lt;/li&gt;&lt;br&gt;"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>ul</strong></span><strong><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span></strong><span class="pln"> </span><span class="str">"&lt;input type='checkbox' name='fruit' </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='bananas'&gt;Bananas&lt;/li&gt;&lt;br&gt;"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; ul</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span></strong><span class="pln"> </span><span class="str">"&lt;input type='checkbox' name='fruit' </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='grapes'&gt;Grapes&lt;/li&gt;"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 2.5.8 Removing elements from the DOM

+ Removing elements
  + `removeChild()`: remove a chile element fron the DOM document
  + example: [remove selected item](src/02e-example14.html)

    ```js
    function removeSelected() {  
      var list = document.querySelectorAll("#fruits input:checked"); 
      var ul = document.querySelector("#fruits");
      
      list.forEach(function(elm) {
        var li = elm.parentNode;
        ul.removeChild(li);
      });
    }
    ```

  + removing all children of an element using the `innerHTML` property
    
    ```js
    function reset() {
      var ul = document.querySelector("#fruits");
      ul.innerHTML = "";  // empty all contents of child elements
      ...
    }
    ```


### 2.5.9 Discussion

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ Did you know there were different keyboard layouts?
+ Did you know the best practices in order to make a Web application compatible with different keyboard layouts?
+ Did you know there were different properties for getting the mouse coordinates?
+ Did you know the method we proposed for getting the mouse coordinate relative to the element the mouse is being moved on?
+ Sometimes, detecting key events on a canvas HTML element is tricky. Do not forget to visit the W3Cx [HTML5 Coding essentials and Best practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) MOOC, as we cover these in details in the section about the HTML5 canvas element.



