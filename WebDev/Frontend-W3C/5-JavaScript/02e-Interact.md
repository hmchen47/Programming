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





