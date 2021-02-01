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
  + types of nodes (moste useful ones highlighted)
    + __element__, e.g., `<ul></ul>`
    + __text__, e.g., `<p>the text within the element p is a node of type text</p>`
    + Document, DocumentFragment, DocumentType, Comment, ProcessingInstruction
  + viewing DOM w/ devtool
    + Firfox: devtool > console > type "document.body"
    + Chrome: ([devtool video](https://youtu.be/VYyQv0CSZOE))
      + devtool > console > tyep "window"
      + devtool > console > type "inspec(document.querySlector("input"));" to focus on 'input' element


### 2.5.2 A warning about the DOM API

The DOM and the DOM API can be cumbersome and complicated. There are many methods and properties for manipulating the DOM tree, that are not "very JavaScript". There are historical reasons for this: the DOM wasn’t designed exclusively for JavaScript. Rather, it tries to define a language-neutral interface that can be used in other systems as well — not just HTML but also XML, which is a generic data format with an HTML-like syntax.

HTML5 made some additions that are not in the DOM API but which greatly help the JavaScript programmer (we'll see this in a minute with the "selector API", for example).

So we've decided to focus on only 20% of the DOM API and on the selector API (for selecting elements in the DOM). These are the most useful parts and it will give you enough knowledge to solve nearly every problem where you need to manipulate the DOM.


### 2.5.3 Accessing HTML elements

#### Live coding video: accessing HTML elements

<a href="https://edx-video.net/W3CJSIXX2016-V003100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](tinyurl.com/1qt6jhfu)

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

  Example: `var elm = document.getElementById('myDiv'); is equivalent to document.querySelector('#myDiv');`

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




