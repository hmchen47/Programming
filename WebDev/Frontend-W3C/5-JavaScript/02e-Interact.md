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

<div><ol>
<li" value="1">&lt;!DOCTYPE html&gt;</li>
<li"> &lt;html lang="en"&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &lt;head&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &lt;title&gt;Your first HTML page&lt;/title&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &lt;meta charset="utf-8"&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &lt;/head&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &lt;body&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &lt;h1&gt;My home page&lt;/h1&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &lt;p&gt;Hi! Welcome to my Home Page! My name is Michel Buffa,</li>
<li"> I'm a professor at the University of Côte d'Azur, in France,</li>
<li"> and I'm also the author <br></li>
<li">of two other W3CX MOOCS.</li>
<li">&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &lt;/p&gt;</li>
<li">&nbsp;&nbsp;&nbsp; &lt;/body&gt;</li>
<li"> &lt;/html&gt;</li>
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

<div><ol>
<li" value="1">...</li>
<li"> &lt;button onclick="addBorderToFirstImage();"&gt;</li>
<li">&nbsp; &nbsp; Add a border to the first image</li>
<li"> &lt;/button&gt;</li>
<li"> &lt;br&gt;</li>
<li"> &lt;button onclick="resizeAllImages();"&gt;</li>
<li">&nbsp; &nbsp; Resize all images</li>
<li"> &lt;/button&gt;</li>
<li"> &lt;br&gt;</li>
<li"> &lt;p&gt;Click one of the buttons above!&lt;/p&gt;</li>
<li">&lt;img src="https://i.imgur.com/Ntvj5rq.png" </li>
<li"><span style="color: #000000;" color="#000000">&nbsp; &nbsp; &nbsp;</span>id="img1"</li>
<li">&nbsp; &nbsp; &nbsp;width=200&gt;</li>
<li">&lt;img src="https://i.imgur.com/yiU59oi.gif" </li>
<li">&nbsp; &nbsp; &nbsp;width=200&gt;</li>
<li">&lt;img src="https://i.imgur.com/6FstYbc.jpg" </li>
<li">&nbsp; &nbsp; &nbsp;width=200&gt;</li>
<li">&lt;img src="https://i.imgur.com/L97CyS4.png" </li>
<li">&nbsp; &nbsp; &nbsp;width=200&gt;</li>
<li">...</li>
</ol></div>

__JavaScript part:__ the `init` function is executed as soon as the page is loaded (and the DOM is ready), in this function we add a shadow and margins to all images (_lines 3-21_). The two other functions are called when one of the HTML buttons is clicked (_line 23_ and _line 31_).

<div><ol>
<li" value="1"><strong>window.onload = init; // run init once the page is loaded</strong></li>
<li">&nbsp;</li>
<li"><strong>function init()</strong> {</li>
<li">&nbsp; &nbsp; // we're sure that the DOM is ready</li>
<li">&nbsp; &nbsp; // before querying it</li>
<li">&nbsp; &nbsp; // <strong>this function runs once the page is loaded</strong></li>
<li"> </li>
<li">&nbsp; &nbsp; // add a shadow to all images</li>
<li">&nbsp; &nbsp; // <strong>select all images</strong></li>
<li">&nbsp; &nbsp; var listImages =<strong> document.querySelectorAll("img");</strong></li>
<li">&nbsp;</li>
<li">&nbsp; &nbsp; // change all their width to 100px</li>
<li">&nbsp; &nbsp; listImages.forEach(function(img) {</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; // img = current image</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; // add a shadow 5px left, 5 pixel down, 15px blur, 5px spread</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; // grey</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; img.style.boxShadow = "5px 5px 15px 5px grey";</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// add a margin 10px on each side</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; img.style.margin = "10px";</li>
<li">&nbsp; &nbsp; });</li>
<li">}</li>
<li">&nbsp;</li>
<li"><strong>function addBorderToFirstImage()</strong> {</li>
<li">&nbsp; &nbsp; // select the first image with id = img1</li>
<li">&nbsp; &nbsp; var img1 =<strong> document.querySelector('#img1');</strong></li>
<li">&nbsp;</li>
<li">&nbsp; &nbsp; // Add a red border, 3px wide</li>
<li">&nbsp; &nbsp; img1.style.border = '3px solid red'; </li>
<li">}</li>
<li">&nbsp;</li>
<li"><strong>function resizeAllImages()</strong> {</li>
<li">&nbsp; &nbsp; // select all images</li>
<li">&nbsp; &nbsp; var listImages = document.querySelectorAll("img");</li>
<li">&nbsp;</li>
<li">&nbsp; &nbsp; // change all their width to 100px</li>
<li">&nbsp; &nbsp; listImages.forEach(function(img) {</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; // img = current image, we resize it by changing its</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; // width attribute</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; img.width = 100;</li>
<li">&nbsp; &nbsp; });</li>
<li">}</li>
</ol></div>


#### Miscellanous examples of use of querySelector(CSSSelector) and querySelectorAll(CSSselector)

Here are some other examples that use more complicated CSS selectors. If you are not familiar with their syntax, we recommend that you follow the CSS basics, and HTML5 and CSS fundamentals courses from [W3Cx](https://www.edx.org/school/w3cx).


__Example #1: get all `<li>` directly in a `<ul>` of class nav__

[CodePen](https://codepen.io/w3devcampus/pen/evxQMr)

[Local Demo](src/02e-example03.html)


Source code extracts:

HTML:

<div><ol>
<li" value="1"> &lt;button onclick="<strong>firstLiClassRedInUl</strong><strong>()</strong>;"&gt;Select first li of class red and color it in red&lt;/button&gt;</li>
<li"> &lt;br&gt;</li>
<li"> &lt;button onclick="<strong>allLisInUlOfClassNav</strong><strong>()</strong>;"&gt;Underline All li in a ul of class nav&lt;/button&gt;</li>
<li"> </li>
<li">&lt;ul <strong>class="nav"</strong>&gt;</li>
<li">&nbsp; &nbsp; &lt;li&gt;Home&lt;/li&gt;</li>
<li">&nbsp; &nbsp; &lt;li <strong>class="red"</strong>&gt;Products&lt;/li&gt;</li>
<li">&nbsp; &nbsp; &lt;li&gt;About&lt;/li&gt;</li>
<li">&lt;/ul&gt;</li>
<li"> Another list:</li>
<li"> &lt;ul&gt;</li>
<li">&nbsp; &nbsp; &lt;li&gt;Apple&lt;/li&gt;</li>
<li">&nbsp; &nbsp; &lt;li <strong>class="red"</strong>&gt;Cherries&lt;/li&gt;</li>
<li">&nbsp; &nbsp; &lt;li&gt;Oranges&lt;/li&gt;</li>
<li">&lt;/ul&gt;</li>
</ol></div>

JavaScript code:

<div><ol>
<li" value="1"><strong>function firstLiClassRedInUl()</strong> {</li>
<li">&nbsp; // first li of in a ul</li>
<li">&nbsp; var elm =<strong> document.querySelector("ul li.red");</strong></li>
<li">&nbsp; elm.style.color = 'red';</li>
<li">}</li>
<li">&nbsp;</li>
<li"><strong>function allLisInUlOfClassNav()</strong> {</li>
<li">&nbsp; // get all li directly in a ul of class nav</li>
<li">&nbsp; var list =<strong> document.querySelectorAll("ul.nav &gt; li");</strong></li>
<li"> </li>
<li">&nbsp; list.forEach(function(elm) {</li>
<li">&nbsp; &nbsp; elm.style.textDecoration = "underline";</li>
<li">&nbsp; })</li>
<li">}</li>
</ol></div>


__Example #2: display all checked `<input type="checkbox">` elements located inside an element of a given id__

[CodePen Demo](https://codepen.io/w3devcampus/pen/MpLzqV)

[Local Demo](src/02e-example04.html)


Extract from the source code:

HTML:

<div><ol>
<li" value="1"> &lt;button onclick="<strong>displayListOfCheckedItems();</strong>"&gt;</li>
<li" value="1">&nbsp; &nbsp; Show Checked items</li>
<li" value="1">&lt;/button&gt;</li>
<li"> &lt;br&gt;</li>
<li">&lt;ul id="fruits"&gt;</li>
<li">&nbsp; &lt;li&gt;</li>
<li">&nbsp; &nbsp; &lt;input type="checkbox" name="fruit" value="apples"&gt;</li>
<li">&nbsp; &nbsp; Apples</li>
<li">&nbsp; &lt;/li&gt;</li>
<li">&nbsp; &lt;li&gt;</li>
<li">&nbsp; &nbsp; &lt;input type="checkbox" name="fruit" value="oranges"&gt;</li>
<li">&nbsp; &nbsp; Oranges</li>
<li">&nbsp; &lt;/li&gt;</li>
<li">&nbsp; &lt;li&gt;</li>
<li">&nbsp; &nbsp; &lt;input type="checkbox" name="fruit" value="bananas"&gt; </li>
<li">&nbsp; &nbsp; Bananas</li>
<li">&nbsp; &lt;/li&gt;</li>
<li">&nbsp; &lt;li&gt;</li>
<li">&nbsp; &nbsp; &lt;input type="checkbox" name="fruit" value="grapes"&gt;</li>
<li">&nbsp; &nbsp; Grapes</li>
<li">&nbsp; &lt;/li&gt;</li>
<li">&lt;/ul&gt;</li>
</ol></div>

JavaScript code: we select all elements of type `input` that have an attribute `checked` equal to `true`, and located inside an element whose id is "fruits". Notice the use of `document.querySelectorAll`, for selecting more than one element (_line 6_), then, we iterate on the list (__line 8_) and concatenate to the string variable `listOfSelectedValues` the value of each element (located in its `value` attribute). This is done in _line 9_.

_Lines 9-12_ use the `parentNode` property of the selected nodes in order to change the color of the `<li>` (parents of `<input>` elements selected) in red. In the DOM tree, we selected input elements that are each a child of a `<li>` element. The text displayed: "Apples", "Oranges" etc. belong to the `<li>` element. In order to access it from the `<input>` child we selected, we use elm.parentNode.

Finally, at the end of the document, _line 14_ adds a message followed by this list:

<div><ol>
<li" value="1">function displayListOfCheckedItems() {</li>
<li">&nbsp; // all inputs that have been checked</li>
<li">&nbsp; var listOfSelectedValues="";</li>
<li"> </li>
<li">&nbsp; var list = document.querySelectorAll("#fruits input:checked"); </li>
<li">&nbsp; list.forEach(function(elm) {</li>
<li">&nbsp; &nbsp; listOfSelectedValues += elm.value + " ";</li>
<li"> </li>
<li">&nbsp; &nbsp; // Put the li in red.</li>
<li">&nbsp; &nbsp; // the li is the parent of the current input elem stored</li>
<li">&nbsp; &nbsp; // in the elm variable</li>
<li">&nbsp; &nbsp; elm.parentNode.style.color = 'green';</li>
<li">&nbsp; });</li>
<li">&nbsp; document.body.append("You selected: " + listOfSelectedValues);</li>
<li">}</li>
</ol></div>


__Example #3: change the background of all paragraphs <p> in an element of a given id__

[CodePen](https://codepen.io/w3devcampus/pen/LWqqqm)

[Local Demo](src/02e-3xample05.html)


HTML code:

<div><ol>
<li" value="1"> &lt;button onclick="<strong>changeBackGroundOfPs('firstDiv');</strong>"&gt;Change backgrounds of p under a given element known by id&lt;/button&gt;</li>
<li"> &lt;br&gt;</li>
<li">&lt;div <strong>id="firstDiv"</strong>&gt;</li>
<li">&nbsp; &lt;p&gt;First paragraph.&lt;/p&gt;</li>
<li">&nbsp; &lt;p&gt;Second paragraph.&lt;/p&gt;</li>
<li">&lt;/div&gt;</li>
</ol></div>

JavaScript code: we build a CSS selector using the id passed as a parameter. In this example, the id is 'firstDiv', the id of the div at _line 3_ in the above code.

So, the variable CSS selector at _line 2_ in the JavaScript code below will have a value equal to "`#firstDiv p`", that means: select all `<p>` under an element whose `id` is "firstDiv". The `paragraphs` variable is a list that contains the paragraphs selected. Then we iterate on this list (this time using a for loop, which is an alternative method to using the forEach method used in previous examples) (_lines 5-7_), and we change the background of all selected paragraphs (_line 6_).

<div><ol>
<li" value="1">function changeBackGroundOfPs(id) {</li>
<li">&nbsp; var paragraphs&nbsp;= document.querySelectorAll("#" + id + " p");</li>
<li">&nbsp;</li>
<li">&nbsp; // Another way to iterate on all elements in a collection</li>
<li">&nbsp; for (var i = 0; i &lt; paragraphs.length; i++ ) {</li>
<li">&nbsp; &nbsp; &nbsp;paragraphs[i].style.backgroundColor = "lightGreen";</li>
<li">&nbsp; }</li>
<li">}</li>
</ol></div>

#### Other examples that use more complex selectors:

<div><ol>
<li value="1"><span style="font-family: 'courier new', courier;">// all elements li in ul elements in an element of id=nav</li>
<li>var el = document.querySelector('#nav ul li'); </li>
<li> </li>
<li>// all li in a ul, but only even elements</li>
<li>var els = document.querySelectorAll('ul li:nth-child(even)'); </li>
<li> </li>
<li> </li>
<li>// all td directly in tr in a form of class test</li>
<li>var els = document.querySelectorAll('form.test &gt; tr &gt; td'); </li>
<li> </li>
<li>// all paragraphs of class warning or error</li>
<li>querySelectorAll("p.warning, p.error"); </li>
<li> </li>
<li>// first element of id=foo or id=bar</li>
<li>querySelector("#foo, #bar"); </li>
<li> </li>
<li>// first p in a div</li>
<li>var div = document.getElementById("bar"); </li>
<li>var p = div.querySelector("p"); </li>
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
      + `init` function executed as soon as the page loaded (DOM ready)

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
    + `var el = document.querySelector('#nav ul li');`: all elements `li` in `ul` elements in an element of `id`= `nav`
    + `var els = document.querySelectorAll('ul li:nth-child(even)');`: all li in a ul, but only even elements
    + `var els = document.querySelectorAll('form.test > tr > td');`: all `td` directly in `tr` in a form of class test
    + `querySelectorAll("p.warning, p.error");`: all paragraphs of class warning or error
    + `querySelector("#foo, #bar");`: first element of `id` = `foo` or `id` = `bar`
    + `var div = document.getElementById("bar"); var p = div.querySelector("p");`: first `p` in a `div`

+ The `getElement` APIs
  + able to be replaced by `querySelector` and `querySelectorAll` methods
  + `document.getElementById(identifier)` method
    + return the element which has the `id` “identifier”.
    + equivalent to `document.querySelector("#identifier');`
    + example: `var elm = document.getElementById('myDiv');` = `document.querySelector('#myDiv');`
  + `document.getElementsByTagName(tagName)` method
    + return a list of elements which are named “tagName”.
    + equivalent to `document.querySelectorAll(tagName);`
    + example: `var list = document.getElementByTagName('img');` = `document.querySelector('img');`
  + `document.getElementsByClassName(className)` method
    + return a list of elements which have the class “className”.
    + equivalent to `document.querySelectorAll('.className');`
    + example: `var list = document.getElementByClassName('important');` = `document.querySelector('.important');`


### 2.5.4 Changing the style of selected HTML elements


#### The `style` attribute

How to modify an HTML element's CSS properties from JavaScript?

The most common way to modify the CSS style of one of several elements you selected using the DOM or Selector API, is to use the `style` attribute.

Typical use:

<div><ol>
<li" value="1">// select the paragraph with id = "paragraph1" </li>
<li"> var p = document.querySelector('#paragraph1');</li>
<li">&nbsp;</li>
<li">// change its color</li>
<li">p.style.color = 'red';</li>
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

<div><ol>
<li" value="1">var elem= document.querySelector("#id1");</li>
<li">&nbsp;</li>
<li">var allClasses = elem.<strong>classList</strong>;</li>
</ol></div>


#### The classList API

The list of methods usable on a classList object are `add()`, `remove()`, `toggle()` and `contains()`.

<div><ol>
<li" value="1">// By default, start without a class in the div: &lt;div/&gt;</li>
<li"> </li>
<li">// Set "foo" as the class by adding it to the classList</li>
<li">div.classList.add('foo'); // now &lt;div/&gt;</li>
<li"> </li>
<li">// Check that the classList contains the class "foo"</li>
<li">div.classList.contains('foo'); // returns true</li>
<li"> </li>
<li">// Remove the class "foo" from the list</li>
<li">div.classList.remove('foo'); // now &lt;div/&gt;</li>
<li"> </li>
<li">// Check if classList contains the class "foo"</li>
<li">div.classList.contains('foo'); // returns false: "foo" is gone</li>
<li"> </li>
<li">// Check if class contains the class "foo",</li>
<li">// If it does, "foo" is removed, if it doesn't, it's added</li>
<li">div.classList.toggle('foo'); // class set to &lt;div/&gt;</li>
<li">div.classList.toggle('foo'); // class set to &lt;div/&gt;</li>
</ol></div>


__Another example: add and remove multiple CSS properties in a list of checkboxes__

[CodePen Demo](https://codepen.io/w3devcampus/pen/GWeJzz)

[Local Demo](src/02e-example07.html)


This is a variation of an example from a previous section. This time, when the `<input type="checkbox">` elements have been checked, in order to give the parent `<li>` a background color, a border, and to change the text color, we use a CSS class named "checked":

CSS code:

<div><ol>
<li" value="1">.checked {</li>
<li">&nbsp; &nbsp; border: 2px dashed #000;</li>
<li">&nbsp; &nbsp; background-color: green;</li>
<li">&nbsp; &nbsp; color:yellow;</li>
<li">}</li>
</ol></div>

... and the `classList.add(CSS_class)` and `classList.remove(CSS_class)` methods on the `<li>` elements:

JavaScript code:

<div><ol>
<li" value="1">function displayListOfCheckedItems() {</li>
<li">&nbsp; // all inputs that have been checked</li>
<li">&nbsp; var listOfSelectedValues="";</li>
<li"> </li>
<li">&nbsp; var list = document.querySelectorAll("#fruits input:checked"); </li>
<li">&nbsp; list.forEach(function(elm) {</li>
<li">&nbsp; &nbsp; listOfSelectedValues += elm.value + " ";</li>
<li"> </li>
<li">&nbsp; &nbsp; <strong>// get the li parent of the current selected input</strong></li>
<li"><strong>&nbsp; &nbsp; var liParent = elm.parentNode;</strong></li>
<li"><strong>&nbsp; &nbsp; // add the CSS class .checked</strong></li>
<li"><strong>&nbsp; &nbsp; liParent.classList.add("checked");</strong></li>
<li">&nbsp; });</li>
<li">&nbsp; document.body.append("You selected: " + listOfSelectedValues);</li>
<li">}</li>
<li">&nbsp;</li>
<li">function reset() {</li>
<li">&nbsp; var list = document.querySelectorAll("#fruits input"); </li>
<li">&nbsp; list.forEach(function(elm) {</li>
<li">&nbsp; &nbsp; // uncheck</li>
<li">&nbsp; &nbsp; elm.checked = false;</li>
<li"> </li>
<li">&nbsp; &nbsp; <strong>// remove CSS decoration</strong></li>
<li"><strong>&nbsp; &nbsp; var liParent = elm.parentNode;</strong></li>
<li"><strong>&nbsp; &nbsp; liParent.classList.remove("checked");</strong></li>
<li">&nbsp; });</li>
<li">}</li>
</ol></div>


#### Notes for 2.5.4 Changing the style of selected HTML elements

+ The `style` attribute
  + most common way to modify the CSS style of one of several elements
  + typical usage: `var p = document.querySelector('#paragraph1'); p.style.color = 'red';`
  + rule to change syntax of attribute in JS
    + remove the "-" sign in CSS attributes if presented
    + capitalize the word after the "-" sign
    + example: `text-align` $\to$ `style.textAlign`, `margin-left` $\to$ `style.marginLeft`
  + most useful CSS properties
    + `color`: changing the color of the text content of selected element(s)
    + `background-color`: the background color of the select element(s)
    + `margin` and `padding`: external and internal space, including `margin-top`, `margin-left`, `margin-bottom`, and `margin-right` and also `padding-top`, etc.
    + `border` and `border-radius`: chnage the border, type, color, thickness, rounded corners, etc.
    + `box-shadow`: add shadow to selected elements
    + `font` and `font-style`: font characters and style (italic, bold, plain)
    + `text-align`: text alignment
  + examples: `p.style.backgroundColor = 'lightGreen';`, `p.style.marginLeft = '100px';`, and `p.style.border = '2px solid blue';`

+ The `ClassList` interface
  + simplifying to manipulate CSS classes of an HTML element
  + acting as a container object and providing a set of methods to manipulate its conetnt
  + applyied to an HTML element and returning a collection of class names
  + typical usage: `var elem = document.querySelector("#id1"); var allClasses = elem.classList;`
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

<div><ol>
<li" value="1">var elem = document.querySelector('#myElem');</li>
<li">&nbsp;</li>
<li">elem.innerHTML = 'Hello '; // replace content by Hello</li>
<li">&nbsp;</li>
<li">elem.innerHTML += '&lt;b&gt;Michel Buffa&lt;/b&gt;', // append at the end </li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Michel Buffa in bold</li>
<li">&nbsp;</li>
<li">elem.innerHTML = 'Welcome' + elem.innerHTML; // insert Welcome </li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// at the beginning</li>
<li">&nbsp;</li>
<li">elem.innerHTML = ''; // empty the elem</li>
</ol></div>

#### Using the `textContent` property

It's also possible, with selected nodes/elements that contain text, to use the textContent property to read the text content or to modify it. There are subtle differences that can be seen in the above example (click the 'edit on CodePen" part on the top left, and once in codePen, open the devtool console):

[CodePen Demo](https://codepen.io/w3devcampus/pen/MpxEdj)

[Local Demo](src/02e-example08.html)

Extract from the HTML code:

<div><ol>
<li" value="1">&lt;p id="first"&gt;first paragraph&lt;/p&gt;</li>
<li">&lt;p id="second"&gt;&lt;em&gt;second&lt;/em&gt; paragraph&lt;/p&gt;</li>
</ol></div>

JavaScript code: the comments after lines that start with `console.log` correspond to what is printed in the devtool debug console. Notice the difference between the `textNode` value and the `innerHTML` property values at _lines 13-14_: while `textContent` returns only the text inside the second paragraph, innerHTML also returns the `<em>...</em>` that surrounds it. However, when we modify the `textContent` value, it also replaces the text decoration (the `<em>` is removed), this is done at _lines 16-20_.

<div><ol>
<li" value="1">window.onload = init;</li>
<li">&nbsp;</li>
<li">function init() {</li>
<li">&nbsp; &nbsp;// DOM is ready</li>
<li">&nbsp; &nbsp;var firstP = document.querySelector("#first");</li>
<li">&nbsp; &nbsp;console.log(firstP.textContent); //&nbsp;"first paragraph"</li>
<li">&nbsp; &nbsp;console.log(firstP.innerHTML); &nbsp;&nbsp;//&nbsp;<span style="background-color: #eeeeee;">"first paragraph"</span></li>
<li">&nbsp;</li>
<li">&nbsp; &nbsp;firstP.textContent = "Hello I'm the first paragraph";</li>
<li">&nbsp; &nbsp;console.log(firstP.textContent); //&nbsp;"Hello I'm the first paragraph"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li>
<li">&nbsp; &nbsp;var secondP = document.querySelector("#second");</li>
<li">&nbsp; &nbsp;console.log(secondP.textContent); //&nbsp;"second paragraph"</li>
<li">&nbsp; &nbsp;console.log(secondP.innerHTML); &nbsp; //&nbsp;"&lt;em&gt;second&lt;/em&gt; paragraph"</li>
<li"> </li>
<li">&nbsp; &nbsp;secondP.textContent = "Hello I'm the second paragraph";</li>
<li">&nbsp; &nbsp;console.log(secondP.textContent); //&nbsp;"Hello I'm the second</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// paragraph"</li>
<li">&nbsp; &nbsp;console.log(secondP.innerHTML); &nbsp;&nbsp;//&nbsp;"Hello I'm the second</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// paragraph"</li>
<li">}</li>
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
    + `console.log(secondP.innerHTML);` $\to$ `<em>second</em> paragraph`
    + `console.log(secondP.textContent);` $\to$ `second paragraph`
  + modifying the attributes
    + directly using the name of attribute as the property
    + `value` property of objects in many cases
    + examples: `colorChooser.value = "#00FF00";`, `number.value = 10; number.step = "0.1"; number.max = 11;`, `img.src="n_400x400.jpg"; img.width=250;`


### 2.5.6 Adding new elements to the DOM

The DOM API comes with a set of methods you can use on DOM elements.

In general, to add new nodes to the DOM we follow these steps:

1. Create a new element by calling the `createElement()` method, using a syntax like:

  <div><ol style="list-style: decimal;">
  <li" value="1">var elm = document.createElement(name_of_the_element). </li>
  </ol></div>

  Examples:

  <div><ol style="list-style: decimal;">
  <li" value="1">var li = document.createElement('li'); </li>
  <li">var img = document.createElement('img'); etc.</li>
  </ol></div>

2. Set some attributes / values  / styles for this element.

  Examples:

  <div><ol style="list-style: decimal;">
  <li" value="1">li.innerHTML = '&lt;b&gt;This is a new list item in bold!&lt;/b&gt;'; // can add HTML in it</li>
  <li">li.textContent = 'Another new list item';</li>
  <li">li.style.color = 'green'; // green text</li>
  <li">img.src = "https://..../myImage.jpg"; // url of the image</li>
  <li">img.width = 200;</li>
  </ol></div>

3. Add the newly created element to another element in the DOM, using `append()`, `appendChild()`, `insertBefore()` or the `innerHTML` property

  Examples:

  <div><ol style="list-style: decimal;">
  <li" value="1">var ul = document.querySelector('#myList');</li>
  <li">ul.append(li); // insert at the end, appendChild() could also be used (old)</li>
  <li">ul.prepend(li); // insert at the beginning</li>
  <li">ul.insertBefore(li, another_element_child_of_ul);// insert in the middle</li>
  <li">document.body.append(img); // adds the image at the end of the document</li>
  </ol></div>


#### Examples

__Example #1: use of the `createElement()`, `append()` methods and of the textContent attribute__

[CodePen Demo](https://codepen.io/w3devcampus/pen/aWeqzO)

[Local Demo](src/02e-example10.html)

HTML code extract: we use an `<input type="number">` for entering a number (_line 2_). Then if one clicks on the "Add to the list" button, the `add()` JavaScript function is called (_line 3_), this will add the typed number to the empty list at _line 7_. If one presses the "reset" button, it will empty this same list by calling the `reset()` JavaScript function.

<div><ol style="list-style: decimal;">
<li" value="1"> &lt;label for="newNumber"&gt;Please enter a number&lt;/label&gt;</li>
<li"> &lt;input type="number" id="newNumber" value=0&gt;</li>
<li"> &lt;button onclick="<strong>add();</strong>"&gt;Add to the list&lt;/button&gt;</li>
<li"> &lt;br&gt;</li>
<li"> &lt;button onclick="<strong>reset();</strong>"&gt;Reset list&lt;/button&gt;</li>
<li">&nbsp;</li>
<li">&lt;p&gt;You entered:&lt;/p&gt;</li>
<li">&lt;ul id="numbers"&gt;&lt;/ul&gt;</li>
</ol></div>

JavaScript code extract: notice at _line 25_ the use of the innerHTML property for resetting the content of the `<ul>` list. innerHTML corresponds to all the sub DOM contained inside the `<ul>...</ul>`. InnerHTML can be used for adding/deleting/modifying a DOM node's content.

<div><ol style="list-style: decimal;">
<li" value="1">function add() {</li>
<li">&nbsp; // get the current value of the input field</li>
<li">&nbsp; var val = document.querySelector('#newNumber').value;</li>
<li"> </li>
<li">&nbsp; if((val !== undefined) &amp;&amp; (val !== "")) {</li>
<li">&nbsp; &nbsp; // val exists and non empty</li>
<li"> </li>
<li">&nbsp; &nbsp; // get the list of numbers. It's a &lt;ul&gt;</li>
<li">&nbsp; &nbsp; var ul = document.querySelector("#numbers");</li>
<li"> </li>
<li">&nbsp; &nbsp; // add it to the list as a new &lt;li&gt;</li>
<li">&nbsp; &nbsp; var newNumber =<strong> document.createElement("li");</strong></li>
<li">&nbsp; &nbsp; <strong>newNumber</strong><strong>.textContent = val;</strong></li>
<li">&nbsp; &nbsp; // or newNumber.innerHTML = val</li>
<li"> </li>
<li">&nbsp; &nbsp; <strong>ul</strong><strong>.append(newNumber);</strong></li>
<li">&nbsp; }</li>
<li">}</li>
<li">&nbsp;</li>
<li">function reset() {</li>
<li">&nbsp; // get the list of numbers. It's a &lt;ul&gt;</li>
<li">&nbsp; var ul = document.querySelector("#numbers");</li>
<li"> </li>
<li">&nbsp; // reset it: no children</li>
<li">&nbsp; <strong>ul</strong><strong>.innerHTML = ""</strong><strong>;</strong> &nbsp;</li>
<li">}</li>
</ol></div>


__Example #2: using the innerHTML property to add new elements__

This is the same example, but in an abbreviated form, using the `innerHTML` property:

[CodePen Demo](https://codepen.io/w3devcampus/pen/jBJbqM)

[Local Demo](src/02e-example11.html)


#### Notes for 2.5.6 Adding new elements to the DOM

+ Adding new node w/ the DOM API
  + create a new element by calling `createElement()` method
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
      + `document.body.append(img);`: add the image at the end of the document


### 2.5.7 Moving HTML elements in the DOM

The `append()`, `appendChild()` methods normally adds  a new element to an existing one, as shown in this example:

<div><ol>
<li" value="1">var li = createElement('li');</li>
<li">ul.append(li); // adds the new li to the ul element</li>
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
      + destination to place element: `<div ondragover="return false" ondrop="drop(this, event)">`
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

<div><ol>
<li" value="1">function removeSelected() { </li>
<li">&nbsp; var list = document.querySelectorAll("#fruits input:checked"); </li>
<li">&nbsp; <strong>var</strong><strong> ul = document.querySelector("#fruits");</strong></li>
<li"> </li>
<li">&nbsp; list.forEach(function(elm) {</li>
<li">&nbsp; &nbsp; // elm is an &lt;input type="checkbox"&gt;, its parent is a li</li>
<li">&nbsp; &nbsp; // we want to remove from the &lt;ul&gt; list</li>
<li">&nbsp; &nbsp; // when we remove the &lt;li&gt;, the &lt;input&gt; will also</li>
<li">&nbsp; &nbsp; // be removed, as it's a child of the &lt;li&gt;</li>
<li">&nbsp; &nbsp; <strong>var</strong><strong> li = elm.parentNode;</strong></li>
<li">&nbsp; &nbsp; <strong>ul</strong><strong>.removeChild(li);</strong></li>
<li">&nbsp; });</li>
<li">}</li>
</ol></div>


#### Removing all children of an element using the `innerHTML` property

In the same example, if you look at the `reset()` JavaScript function, we use the ul's innerHTML property both for emptying the list (_lines 3-4_) and for appending to it all the initial HTML code (_lines 6-17_):

<div><ol>
<li" value="1">function reset() {</li>
<li">&nbsp; var ul = document.querySelector("#fruits");</li>
<li">&nbsp; <strong>// Empty the &lt;ul&gt;</strong></li>
<li"><strong>&nbsp; ul.innerHTML = "";</strong></li>
<li"> </li>
<li">&nbsp; // Adds each list item to the &lt;ul&gt; using innerHTML += ...</li>
<li">&nbsp; <strong>ul</strong><strong>.innerHTML +=</strong> "&lt;li&gt;&lt;input type='checkbox' name='fruit' &nbsp; <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='apples'&gt;Apples&lt;/li&gt;";</li>
<li">&nbsp;</li>
<li">&nbsp; <strong>ul</strong><strong>.innerHTML +=</strong> "&lt;input type='checkbox' name='fruit' <br></li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='oranges'&gt;Oranges&lt;/li&gt;&lt;br&gt;";</li>
<li">&nbsp;</li>
<li">&nbsp; <strong>ul</strong><strong>.innerHTML +=</strong> "&lt;input type='checkbox' name='fruit' </li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='bananas'&gt;Bananas&lt;/li&gt;&lt;br&gt;";</li>
<li">&nbsp;</li>
<li"><strong>&nbsp; ul.innerHTML +=</strong> "&lt;input type='checkbox' name='fruit' </li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value='grapes'&gt;Grapes&lt;/li&gt;";</li>
<li">}</li>
</ol></div>


#### Notes for 2.5.8 Removing elements from the DOM

+ Removing elements
  + `removeChild()`: remove a chile element from the DOM document
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



