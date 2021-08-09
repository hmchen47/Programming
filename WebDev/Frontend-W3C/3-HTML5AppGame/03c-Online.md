# Module 3: HTML5 file upload and download section


## 3.3 Drag and drop


### 3.3.1 Introduction

From [the W3C HTML 5.1 specification](https://www.w3.org/TR/html51/editing.html#dnd): 
> "the drag and drop API defines an event-based drag-and-drop mechanism, it does not define exactly what a drag-and-drop operation actually is".

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
  + ref: E. Bidelman and R. Andrew, [Using the HTML5 Drag and Drop API](https://web.dev/drag-and-drop/), 2020


### 3.3.2 Drag detection

#### Live coding video: drag and drop basics

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2TEzEcC)


#### Draggable attribute and detection

In order to make any visible element draggable, add the `draggable="true"` attribute to any visible HTML5 element. Notice that some elements are draggable by default, such as `<img>` elements.

In order to detect a drag, add an event listener for the `dragstart` event:

<div><ol>
<li value="1">&lt;ol <strong style="color: red;">ondragstart="dragStartHandler(event)"</strong>&gt;</li>
<li>&nbsp; &nbsp;&lt;li <strong style="color: red;">draggable="true"</strong> data-value="fruit-apple"&gt;Apples&lt;/li&gt; </li>
<li>&nbsp; &nbsp;&lt;li <strong style="color: red;">draggable="true"</strong> data-value="fruit-orange"&gt;Oranges&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&lt;li <strong style="color: red;">draggable="true"</strong> data-value="fruit-pear"&gt;Pears&lt;/li&gt;</li>
<li>&lt;/ol&gt;</li>
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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp;function dragStartHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;alert('dragstart event, target: ' + event.target.innerHTML);</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;&lt;/script&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp;&nbsp;&lt;p&gt;What fruits do you like? Try to drag an element!&lt;/p&gt;</li>
<li>&nbsp;&nbsp;&lt;ol ondragstart="dragStartHandler(event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-apple"&gt;Apples&lt;/li&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-orange"&gt;Oranges&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-pear"&gt;Pears&lt;/li&gt;</li>
<li>&nbsp;&nbsp;&lt;/ol&gt;</li>
<li> &lt;p&gt;Drop your favorite fruits below:&lt;/p&gt;</li>
<li>&nbsp;&lt;body&gt;</li>
<li> &lt;html&gt;</li>
</ol></div>

In this script, the event handler will only display an alert showing the name of the target element that launched the event. 


#### Notes for 3.3.2 Drag detection

+ Draggable attribute
  + making any visible element draggable w/ `true` value
  + some elements draggable by default, such as `<img>`
  + example: `<li draggable=true data-value="fruit-apple">Apple</li>`

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

+ Example: draggable attribute and event handler
  + HTML snippet<a name="draggable"></a>:
    + ordered list: `<ol ondragstart="dragStartHandler(evt)"> ... </ol>`
    + item apples: `<li draggable=true data-value="fruit-apple">Apples</li>`
    + item oranges: `<li draggable=true data-value="fruit-orange">Oranges</li>`
    + item pears: `<li draggable=true data-value="fruit-pear">Pears</li>`
  + event handler: `function dragStartHandler(evt) { alert('dragstart event, target: ' + evt.target.innerHTML); }`


### 3.3.3 Drop detection

Let's continue to develop the example. We show how to drag an element and detect a drop, receiving a value which corresponds to the dragged element. Then we change the page content accordingly.

#### Handling drop

__Step #1: in the `dragstart` handler, copy a value in the drag and drop clipboard for later use__

When a draggable `<li>` element is being dragged, in the `dragstart` handler [get the value of its data-value attribute](https://html5doctor.com/html5-custom-data-attributes/) and copy it to the "_drag and drop clipboard_" for later use.

When data is copied to this clipboard, a key/value pair must be given. The data copied to the clipboard is associated with this name.

The variable `event.target` at line 5 below is the `<li>` element that has been dragged, and event.target.dataset.value is the value of its data-value attribute (in our case "apples", "oranges" or "pears"):

<div><ol>
<li value="1">function dragStartHandler(event) {</li>
<li>&nbsp; &nbsp; console.log('dragstart event, target: ' + event.target.innerHTML);</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// Copy&nbsp;to the drag'n'drop clipboard the value of the </li>
<li>&nbsp; &nbsp; // data* attribute of the target, </li>
<li>&nbsp; &nbsp; // with a type "Fruit".</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">event.dataTransfer.setData("Fruit", event.target.dataset.value);</strong></li>
<li> }</li>
</ol></div>

__Step #2: define a "drop zone"__

Any visible HTML element may become a "drop zone"; if we attach an event listener for the `drop` event. Note that most of the time, as events may be propagated, we will also listen for `dragover` or `dragend` events and stop their propagation. More on this later...

<div><ol>
<li value="1">&lt;div <strong style="color: red;">ondragover="return false"</strong> <strong style="color: red;">ondrop="dropHandler(event);</strong>"&gt;</li>
<li> Drop your favorite fruits below:</li>
<li> &lt;ol id="droppedFruits"&gt;&lt;/ol&gt;</li>
<li>&lt;/div&gt;</li>
</ol></div>

Whenever the mouse is moving above a (any) drop zone, dragover events will fire. Accordingly, a large number of dragover events may need to be handled before the element is finally dropped. The `ondragover` handler is used to avoid propagating `dragover` events. This is done by returning the `false` value at _line 1_.

__Step #3: write a `drop` handler, fetch content from the clipboard, and do something with it__

<div><ol>
<li value="1">function dropHandler(event) {</li>
<li>&nbsp; &nbsp;console.log('drop event, target: ' + event.target.innerHTML);</li>
<li> </li>
<li>&nbsp; &nbsp;...</li>
<li> </li>
<li>&nbsp; &nbsp;// get the data from the drag'n'drop clipboard,GET </li>
<li>&nbsp; &nbsp;// with a type="Fruit"</li>
<li>&nbsp; &nbsp;var data = event.dataTransfer.getData("Fruit");</li>
<li> </li>
<li>&nbsp; &nbsp;// do something with the data</li>
<li>&nbsp; &nbsp;...</li>
<li>} </li>
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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dragStartHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log('dragstart event, target: ' + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.target.innerHTML);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Copy&nbsp;to the drag'n'drop clipboard the value </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // of the data* attribute of </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // the target, with a type "Fruits".</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.dataTransfer.setData("Fruit", </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.dataset.value);</li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dropHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log('drop event, target: ' + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.innerHTML);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var li = document.createElement('li');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// get the data from the drag'n'drop clipboard, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// with a type="Fruit"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var data = event.dataTransfer.getData("Fruit");</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if (data == 'fruit-apple') {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Apples';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;} else if (data == 'fruit-orange') {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Oranges';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;} else if (data == 'fruit-pear') {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Pears';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Unknown Fruit';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// add the dropped data as a child of the list.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document.querySelector("#droppedFruits").appendChild(li);</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;&lt;/script&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &nbsp;&lt;p&gt;What fruits do you like? Try to drag an element!&lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;ol ondragstart="dragStartHandler(event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-apple"&gt;Apples&lt;/li&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-orange"&gt;Oranges&lt;/li&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-pear"&gt;Pears&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&lt;/ol&gt;</li>
<li>&nbsp; &nbsp;&lt;div ondragover="return false" ondrop="dropHandler(event);"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;Drop your favorite fruits below:</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;ol id="droppedFruits"&gt;&lt;/ol&gt;</li>
<li>&nbsp; &nbsp;&lt;/div&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;html&gt;</li>
</ol></div>

In the above code, note:

+ _Line 44_: we define the drop zone (`ondrop=...`), and when a drag enters the zone we prevent event propagation (`ondragover="return false"`)
+ When we enter the `dragstart` listener (_line 5_), we copy the dragged-element's `data-value` attribute to the drag and drop clipboard with a name/key equal to "Fruit" (_line 11_),
+ When a drop occurs in the "drop zone" (the `<div>` at line 44), the `dropHandler(event)` function is called. This always occurs after a call to the `dragstart` handler. In other words: when we enter the `drop` handler, there must always be something on the clipboard! We use an event.`dataTransfer.setData(...)` in the dragstart handler, and an `event.dataTransfer.getData(...)` in the drop handler.
+ The `dropHandler` function is called (_line 15_), we get the object with a name/key equal to "Fruit" (_line 21_) from the clipboard , we create a `<li>` element (line 18), and set its value according to the value in that clipboard object (_lines 23-31_),
+ Finally we add the `<li>` element to the `<ol>` list within the drop zone `<div>`.

Notice that we use some CSS to set aside some screen-space for the drop zone (not presented in the source code above, but available in the online example):

<div><ol>
<li value="1">div {</li>
<li>&nbsp; &nbsp;height: 150px;</li>
<li>&nbsp; &nbsp;width: 150px;</li>
<li>&nbsp; &nbsp;float: left;</li>
<li>&nbsp; &nbsp;border: 2px solid #666666; </li>
<li>&nbsp; &nbsp;background-color: #ccc;</li>
<li>&nbsp; &nbsp;margin-right: 5px;</li>
<li>&nbsp; &nbsp;border-radius: 10px;</li>
<li>&nbsp; &nbsp;box-shadow: inset 0 0 3px #000;</li>
<li>&nbsp; &nbsp;text-align: center;</li>
<li>&nbsp; &nbsp;cursor: move;</li>
<li> }</li>
<li> </li>
<li> li:hover {</li>
<li>&nbsp; &nbsp;border: 2px dashed #000;</li>
<li>}</li>
</ol></div>

#### Notes for 3.3.3 Drop detection

+ Procedure to handle drop
  <ol style="list-style-type: decimal;">
    <li> in the <code>dragstart</code> handler, copy a value in the drag and drop clipboard for later use</li>
    <li> define a "drop zone"</li>
    <li> write a <code>drop</code> handler, fetch content from the clipboard , and do something with it</li>
  </ol>

+ Utilizing drag and drop clipboard
  + get the value of the data-value attribute from the dragged element w/ `dragStart` handler
  + copy the obtained value into "drag and drop clipboard"
  + data as key/value pair
  + example: `function dragStartHandler(evt) { evt.dataTransfer.setData("Fruit", evt.target.dataset.value); }`

+ Defining drop zone
  + any visible element if `drop` event listener attached
  + listen for `dragover` or `dragend` events and stop their propagation
  + mouse moving over any drop zone triggering `dragover` event
  + a few `dragover` events to be handled before the element finally dropped
  + `ondragover` handler used to avoid propagating `dragover` events
  + example: `<div ondragover="return false" ondrop="dropHandler(event);">...</div>`

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
    + ordered list and listed item elements w/ [drag](#draggable)
    + element for drop zone: `<div ondragover="return false" ondrop="dropHandler(evt);">Drop your favorite fruits below: <ol id="droppedFruits"></ol></div>`
  + CSS style for mouse hover item: `li.hover { border: 2px dashed #000; }`
  + JavaScript snippet
    + add drag handler: `function dragStartHandler(event) {...}`
      + log msg: `console.log('dragstart event, target: ' + event.target.innerHTML);`
      + copy dragged element into drag'n'drop clipboard: `event.dataTransfer.setData("Fruit", event.target.dataset.value);`
    + add drop handler<a name="drop"></a>: `function dropHandler(event) {...}`
      + log msg: `console.log('drop event, target: ' + event.target.innerHTML);`
      + create listed item: `var li = document.createElement("li");`
      + get data from drag'n'drop clipboard: `var data = event.dataTransfer.getData("Fruit");`
      + check data as apples: `if (data === 'fruit-apple') { li.textContent = 'Apples'; }`
      + check data as oranges: `else if (data === 'fruit-orange') { li.textContent = 'Orange'; }`
      + check data as pears: `else if (data === 'fruit-pears') { li.textContext = 'Pears'; }`
      + check data as other: `else { li.textContent = 'Unknown Fruit'; }`
      + add listed into page: `document.querySelector("#droppedFruits").appendChild(li);`


### 3.3.4 A few words about data-* attributes


#### Arbitrary data in HTML elements

Microdata is a powerful way to add structured data into HTML code, but HTML5 has also added the possibility of adding arbitrary data to an HTML element. For example, adding an attribute to specify the name of the photographer (or painter?) of a picture, or any kind of information that does not be fit within the regular attributes of the `<img>` element, like `alt`.

Suppose you coded: <code>&lt;img src="photo.jpg" <span style="color: #ff0000;">photographer="Michel Buffa" date="14July2020"&gt;</strong></code>?  It would __not__ be valid!

However with HTML5 we may add attributes that start with data- followed by any string literal (WITH NO UPPERCASE) and it will be treated as a storage area for private data. This can later be accessed in your JavaScript code.

Valid HTML5 code: <code>&lt;img src="photo.jpg" <span style="color: #ff0000;">data-photographer="Michel Buffa" date="14July2020"&gt;</code>

The reason for this addition is that, in a bid to keep the HTML code valid, some classic attributes like `alt`, `rel` and `title` have often been misused for storing arbitrary data. The `data-*` attributes of HTML5 are an "official" way to add arbitrary data to HTML elements that is also valid HTML code.

The specification says: "Custom data attributes are intended to store custom data private to the page or application, for which there are no more appropriate attributes or elements."

__Data attributes are meant to be used by JavaScript and eventually by CSS rules: embed initial values for some data, or use data- attributes instead of JavaScript variables for easier CSS mapping, etc.__


#### JavaScript API: the `dataset` property

Data attributes can be created and accessed using the `dataset` property of any HTML element.

Here is an [online at JsBin](https://jsbin.com/yowimebawo/edit?html,css,js,output) example:

[Local Demo](src/03c-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3weljRr')"
    src    = "https://bit.ly/2TGNyuR"
    alt    = "Data attribute example 1"
    title  = "Data attribute example 1"
  />
</figure>


In this example, when you click on the sentence that starts with "John Says", the end of the sentence changes, and the values displayed are taken from data­-* attributes of the `<li>` element.

HTML code from the example:

<div><ol>
<li value="1">&lt;li class="user" <strong style="color: red;">data-name="John Resig"</strong> <strong style="color: red;">data-city="Boston"</strong> </li>
<li>&nbsp; &nbsp; <strong style="color: red;">data-lang</strong><strong style="color: red;">="js"</strong> <strong style="color: red;">data-food="Bacon"</strong>&gt;</li>
<li> &lt;b&gt;John says:&lt;/b&gt; &lt;span&gt;Hello, how are you?&lt;/span&gt;</li>
<li>&lt;/li&gt;</li>
</ol></div>

We just defined four data‐ attributes. 

JavaScript code from the example:

<div><ol>
<li value="1">&lt;script&gt;</li>
<li>&nbsp; var user = document.getElementsByTagName("li")[0];</li>
<li>&nbsp; var pos = 0, span = user.getElementsByTagName("span")[0];</li>
<li>&nbsp; var phrases = [</li>
<li>&nbsp; &nbsp; {name: "city", prefix: "I am from "},</li>
<li>&nbsp; &nbsp; {name: "food", prefix: "I like to eat "},</li>
<li>&nbsp; &nbsp; {name: "lang", prefix: "I like to program in "}</li>
<li>&nbsp; ];</li>
<li>&nbsp; user.addEventListener( "click", function(){</li>
<li>&nbsp; &nbsp; // Pick the first, second or third phrase</li>
<li>&nbsp; &nbsp; var phrase = phrases[ pos++ % 3 ];</li>
<li> </li>
<li>&nbsp; &nbsp; // Use the .dataset property depending on the value of phrase.name</li>
<li>&nbsp; &nbsp; // phrase.name is "city", "food" or "lang"</li>
<li>&nbsp; &nbsp; span.innerHTML = phrase.prefix + user.dataset[ phrase.name ];</li>
<li> </li>
<li>&nbsp; &nbsp; // could be replaces by old way..</li>
<li>&nbsp; &nbsp; // span.innerHTML = phrase.prefix + user.getAttribute("data-" + phrase.name );</li>
<li>&nbsp; }, false);</li>
<li>&lt;/script&gt;</li>
</ol></div>

All `data‐` attributes are accessed using the `dataset` property of the HTML element: in this example, `user.dataset[phrase.name]` is either `user.dataset.city`, `user.dataset.food`, or `user.dataset.lang`.


#### Accessing `data-` attributes from CSS pseudo elemets

__Using CSS pseudo elements `::before` and `::after` with the `attr()` function to display the value of `data-*` attributes__

This example shows how `data-*` attributes can be added on the fly by JavaScript code and accessed from a CSS rule using the `attr()` CSS function.

Try the [online example at JsBin](https://jsbin.com/alunuk/6/edit).

[Local Demo](src/03c-example04.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3weljRr')"
    src    = "https://bit.ly/3e47BdZ"
    alt    = "Using CSS attr() function"
    title  = "Using CSS attr() function"
  />
</figure>


HTML code from this example:

<div><ol>
<li value="1">&lt;input type="range" min="0" max="100" value="25"&gt;</li>
</ol></div>

This is just one of the new input types introduced by HTML5.

JavaScript code from this example:

<div><ol>
<li value="1">&lt;script&gt;</li>
<li>var input = document.querySelector('input');</li>
<li>&nbsp;</li>
<li>input.dataset.myvaluename = input.value; // Set an initial value.</li>
<li>&nbsp;</li>
<li>input.addEventListener('change', function(e) {</li>
<li>&nbsp; &nbsp; this.dataset.myvaluename = this.value;</li>
<li>});</li>
<li>&lt;/script&gt;</li>
</ol></div>

CSS code from this example:

<div><ol>
<li value="1">&lt;style&gt;</li>
<li> input::after {</li>
<li>&nbsp; &nbsp; color:red;</li>
<li>&nbsp; &nbsp; content:<strong style="color: red;"> attr(data-myvaluename)</strong> '/' attr(max);</li>
<li>&nbsp; &nbsp; position: relative;</li>
<li>&nbsp; &nbsp; left: 100px; top: -15px;</li>
<li>}</li>
<li>&lt;/style&gt; </li>
</ol></div>

The `attr()` function takes an attribute name as a parameter and returns its value. Here we used the name of the attribute we added on the fly.


#### Notes for 3.3.4 A few words about data-* attributes

+ `data-*` attributes
  + metadata: a powerful way to add structured data into HTML code
  + HTML5 adding the possibility of adding arbitrary data to an HTML element
    + attributes starting w/ `data-` followed by any string literal (w/o uppercase)
    + treated as a storage area for private data
  + some classic attributes, including `alt`, `rel` and `title`, misused for storing arbitrary data
  + official way to add arbitrary data to HTML elements
  + custom data attributes: intended to store customer data private to the page or application
  + creating and accessing data attributes by the `dataset` property
  + `attr()` function: taking an attribute name as a parameter and return its value
  + examples:
    + invalid: <code>&lt;img src="photo.jpg" <span style="color: #ff0000;">photographer="Michel Buffa" date="14July2020"&gt;</strong></code>
    + valid: <code>&lt;img src="photo.jpg" <span style="color: #ff0000;">data-photographer="Michel Buffa" date="14July2020"&gt;</code>

+ Example: accessing dataset property
  + task: access `data-` attributes w/ `dataset` property
  + HTML snippet: `<li data-name="John Resig" data-city="Boston" data-lang="js" data-food="Bacon"><b>John says:</b> Hello, how are you?</li>`
  + JavaScript snippet:
    + access elements: `var user = document.getElementsByTagName("li")[0]; var pos = 0, span = user.getElementsByTagName("span")[0];`
    + declare variable for phrases: `var phrases = [ {name: "city", prefix: "I am from "}, {name: "food", prefix: "I like to eat "}, {name: "lang", prefix: "I like to program in "} ];`
    + add click listener: `user.addEventListener("click", function() {...}, false);`
      + pick a phrase: `var phrase = phrases[pos++ % 3];`
      + access dataset property and display: `span.innerHTML = phrase.prefix + user.dataset[phrase.name];`
      + access data attribute and display in old way: `span.innerHTML = phrase.prefix + user.getAttribute("data-" + phrase.name);`

+ Example: adding `data-` attributes w/ CSS
  + task: using `attr()` in CSS to take an attribute name as a parameter and return its value
  + HTML snippet: `<input type="range" min=0 max=100 value=25>`
  + JavaScript snippet:
    + access input element: `var input = document.querySelector("input");`
    + set init value: `input.dataset.myvaluename = input.value;`
    + add change listener: `input.addEventListener('change', function(e) { this.dataset.myvaluename = this.value; });`
  + CSS snippet: <code>input::after { color: red; content: <strong style="color: red;">attr(data-myvaluename)</strong> '/' attr(max); position: relative; left: 100px; top: -15px; }</code>


### 3.3.5 Add visual feedback

#### Live coding video: add visual feedback

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/36cfOs9)


#### Visual feeback on draggable object and drop zone

__Add visual feedback when you drag something, when the mouse enters a drop zone, etc.__

We can associate some CSS styling with the lifecycle of a drag and drop. This is easy to do as the drag and drop API provides many events we can listen to, and can be used on the draggable elements as well as in the drop zones:

+ __dragstart__: this event, which we discussed in a previous section, is used on draggable elements. We used it to get a value from the element that was dragged, and copied it onto the clipboard. It's a good time to add some visual feedback - for example, by adding a CSS class to the draggable object.
+ __dragend__: this event is launched when the drag has ended (on a drop or if the user releases the mouse button outside a drop zone). In both cases, it is a best practice to reset the style of the draggable object to default.

The next screenshot shows the use of CSS styles (green background + dashed border) triggered by the start of a `drag` operation. As soon as the drag ends and the element is dropped, we reset the style of the dragged object to its default. The full runnable online example is a bit further down the page (it includes, in addition, visual feedback on the drop zone):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3hFYL6S')"
    src    = "https://bit.ly/3qVCLta"
    alt    = "drag n drop colorful"
    title  = "drag n drop colorful"
  />
</figure>


Source code extract:

<div><ol>
<li value="1">...</li>
<li>&lt;style&gt;</li>
<li>&nbsp;&nbsp;.dragged {</li>
<li>&nbsp; &nbsp; &nbsp;border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp;background-color: green;</li>
<li>&nbsp;&nbsp;}</li>
<li>&lt;/style&gt;</li>
<li>&lt;script&gt;</li>
<li>&nbsp;&nbsp;function dragStartHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">// Change CSS class for visual feedback</strong></li>
<li>&nbsp; &nbsp; &nbsp;event.target.style.opacity = '0.4';</li>
<li>&nbsp; &nbsp; &nbsp;event.target.<strong style="color: red;">classList</strong>.add('dragged');</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;console.log('dragstart event, target: ' + event.target);</li>
<li>&nbsp; &nbsp; &nbsp;// Copy&nbsp;to the drag'n'drop clipboard the value of the data* attribute of the target, </li>
<li>&nbsp; &nbsp; &nbsp;// with a type "Fruits".</li>
<li>&nbsp; &nbsp; &nbsp;event.dataTransfer.setData("Fruit", event.target.dataset.value);</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp;&nbsp;function dragEndHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp;console.log("drag end");</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">// Set draggable object to default style</strong></li>
<li>&nbsp; &nbsp; &nbsp;event.target.style.opacity = '1';</li>
<li>&nbsp; &nbsp; &nbsp;event.target.classList.remove('dragged'); </li>
<li>&nbsp;&nbsp;}</li>
<li>&lt;/script&gt;</li>
<li>...</li>
<li> &lt;ol ondragstart="dragStartHandler(event)" ondragend="dragEndHandler(event)" &gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-apple"&gt;Apples&lt;/li&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-orange"&gt;Oranges&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-pear"&gt;Pears&lt;/li&gt;</li>
<li> &lt;/ol&gt;</li>
</ol></div>

Notice at _lines 12 and 24_ the use of the `classlist` property that has been introduced with HTML5 in order to allow CSS class manipulation from JavaScript.

Other events can also be handled:

+ __dragenter__: usually we bind this event to the drop zone. The event occurs when a dragged object enters a drop zone. So, we could change the look of the drop zone.
+ __dragleave__: this event is also used in relation to the drop zone. When a dragged element leaves the drop zone (maybe the user changed his mind?), we must set the look of the drop zone back to normal.
+ __dragover__: this event is also generally bound to elements that correspond to a drop zone. A best practice here is to prevent the propagation of the event, and also to prevent the default behavior of the browser (i.e. if we drop an image, the default behavior is to display its full size in a new page, etc.)
+ __drop__: also on the drop zone. This is when we actually process the drop (get the value from the clipboard, etc). It's also necessary to reset the look of the drop zone to default.


#### Example with visual feedback on draggable object

__Complete example with visual feedback on draggable objects and the drop zone__

The following example shows how to use these events in a droppable zone. 

Try it in your browser below or [directly at CodePen](https://codepen.io/w3devcampus/pen/ojNLEL):

[Local Demo](src/03c-example05.html)

Complete source code (for clarity's sake, we put the CSS and JavaScript into a single HTML page):

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp;div {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; height: 150px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; width: 150px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;float: left;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; border: 2px solid #666666; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; background-color: #ccc;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; margin-right: 5px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; border-radius: 10px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; box-shadow: inset 0 0 3px #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; text-align: center;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; cursor: move;</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;.dragged {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;.draggedOver {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> &lt;/style&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp;function dragStartHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Change css class for visual feedback</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.target.style.opacity = '0.4';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.add('dragged');</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log('dragstart event, target: ' + event.target.innerHTML);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Copy in the drag'n'drop clipboard the value of the data* attribute of the target, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // with a type "Fruits".</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.dataTransfer.setData("Fruit", event.target.dataset.value);</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dragEndHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log("drag end");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.target.style.opacity = '1';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.remove('dragged'); </li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dragLeaveHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log("drag leave");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.remove('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dragEnterHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log("Drag enter");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.add('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dragOverHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;//console.log("Drag over a droppable zone");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.preventDefault(); // Necessary. Allows us to drop.</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dropHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log('drop event, target: ' + event.target);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// reset the visual look of the drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.remove('draggedOver'); </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var li = document.createElement('li');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// get the data from the drag'n'drop clipboard, with a type="Fruit"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var data = event.dataTransfer.getData("Fruit");</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;if (data == 'fruit-apple') {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Apples'; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;} else if (data == 'fruit-orange') {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Oranges';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;} else if (data == 'fruit-pear') {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Pears';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = 'Unknown Fruit';</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;// add the dropped data as a child of the list.</li>
<li>&nbsp; &nbsp; &nbsp;document.querySelector("#droppedFruits").appendChild(li);</li>
<li>&nbsp; &nbsp;} </li>
<li>&nbsp;&nbsp;&lt;/script&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;p&gt;What fruits do you like? Try to drag an element!&lt;/p&gt;</li>
<li> &lt;ol ondragstart="dragStartHandler(event)" ondragend="dragEndHandler(event)" &gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-apple"&gt;Apples&lt;/li&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-orange"&gt;Oranges&lt;/li&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;li draggable="true" data-value="fruit-pear"&gt;Pears&lt;/li&gt;</li>
<li> &lt;/ol&gt;</li>
<li> &lt;div id="droppableZone" ondragenter="dragEnterHandler(event)" ondrop="dropHandler(event)"</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;ondragover="dragOverHandler(event)" ondragleave="dragLeaveHandler(event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; Drop your favorite fruits below:</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;&lt;ol id="droppedFruits"&gt;&lt;/ol&gt;</li>
<li>&nbsp;&lt;/div&gt;</li>
<li>&lt;body&gt;</li>
<li>&lt;html&gt;</li>
</ol></div>


#### Notes for 3.3.5 Add visual feedback

+ Visual feedback for drag & drop
  + scenarios
    + when drag something
    + when mouse enters a drop zone
    + etc.
  + associating CSS styling w/ the lifecycle of a drag and drop

+ Events related to draggable object
  + `dragstart`:
    + used on draggable elements
    + used to get a value from the dragged element
    + copying value to the clipboard
    + good practice: visual feedback on draggable elements
  + `dragend`:
    + launched as the drag ended
    + on a drop or if the user releases the mouse button outside a drop zone
    + best practice: reset the style of the draggable object to default
  + `dragenter`:
    + binding the event to the drop zone
    + occurred when a dragged object enters a drop zone
    + good practice: change the appearance of the drop zone
  + `dragleave`:
    + used in relation to the drop zone
    + good practice: set appearance back to normal once leaving the drop zone
  + `dragover`:
    + generally bound to elements corresponding to a drop zone
    + best practice: preventing the propagation of the event and the default behavior of the browser
  + `drop`:
    + on the drop zone and processing the the drop, such as getting the value from the clipboard, etc.
    + good practice: reset the look of the drop zone to default

+ Example: visualizing the drag and drop
  + HTML snippet: ordered list and listed item elements w/ [drag](#draggable)
  + CSS snippet: `.dragged { border: 2px dashed #000; background-color: green; }`
  + JavaScrip snippet:
    + add drag start handler<a name="dragStart"></a>: `function dragStartHandler(evt) {...}`
      + change CSS class: `evt.target.style.opacity = "0.4"; evt.target.classList.add('dragged');`
      + log msg: `console.log('dragstart event, target: ' + evt.target);`
      + copy to clipboard: `evt.dataTransfer.setData("Fruit", evt.target.dataset.value);`
    + add drag end handler<a name="dragEnd"></a>: `function dragEndHandler(evt) {...}`
      + log msg: `console.log("drag end");`
      + set draggable object to default: `event.target.style.opacity = '1';`
      + remove added CSS style: `evt.target.classList.remove('dragged');`

+ Example: visual feedback on draggable object and the drop zone
  + HTML snippet:
    + ordered list and listed item elements w/ [drag](#draggable)
    + container for drop zone: `<div id="droppableZone" ondragenter="dragEnterHandler(evt)" ondrop="dropHandler(evt)" ondragover="dragOverHandler(evt)" ondragleave="dragLeaveHandler(evt)">Drop your favorite fruits below: <ol id="droppedFruits"></ol></div>`
  + CSS styles
    + container style: `div { height: 150px; width: 150px; float: left; border: 2px solid #666666; background-color: #ccc; ... }`
    + dragged item: `.dragged { border: 2px dashed #000; background-color: green; }`
    + drop zone when mouse over: `.draggedOver { border: 2px dashed #000; background-color: lightgreen; }`
  + JavaScript snippet:
    + add [drag start handler](#dragStart)
    + add [drag end handler](#dragEnd)
    + add drag leave handler<a name="dragLeave"></a>: `function dragLeaveHandler(evt) { console.log("Drag leave"); evt.target.classList.remove("draggedOver"); }`
    + add drag enter handler<a name="dragEnter"></a>: `function dragEnterHandler(evt) { console.log("Drag enter"); evt.target.classList.add("draggedOver"); }`
    + add drag over handler<a name="dragOver"></a>: `function dragOverHandler(evt) { console.log("Drag over a dropped zone"); evt.preventDefault(); }`
    + add [drop handler](#drop)


### 3.3.6 The dropEffect property


#### Feedback with the `dropEffect` property

__More feedback using the `dropEffect` property: changing the cursor's shape__

It is possible to change the cursor's shape during the drag process. The cursor will turn into a "copy", "move" or "link" icon, depending on the semantic of your drag and drop, when you enter a drop zone during a drag. For example, if you "copy" a fruit into the drop zone, as we did in the previous example, a "copy" cursor like the one below would be appropriate: (left diagram)

If you are "moving" objects, this style of cursor would be appropriate: (middle diagram)

And if you are making a "link" or a "shortcut", a cursor would be looking like this: (right diagram)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3ArXRDT" ismap target="_blank">
    <img style="margin-left: 0em;" height=50
      src   = "https://bit.ly/3hAxbYR"
      alt   = "dropEffect"
      title = "dropEffect"
    >
    <img style="margin-left: 1.0em;" height=50
      src   = "https://bit.ly/36d0aN2"
      alt   = "drop effect #2"
      title = "drop effect #2"
    >
    <img style="margin-left: 1.0em;" height=50
      src   = "https://bit.ly/3hjKr5b"
      alt   = "drop effect #3"
      title = "drop effect #3"
    >
  </a>
</div>

Alternatively, you could use any custom image/icon you like:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3ArXRDT')"
    src    = "https://bit.ly/3hFqzZi"
    alt    = "drop effect with image"
    title  = "drop effect with image"
  />
</figure>


To give this visual feedback, we use the `effectAllowed` and `dropEffect` properties of the `dataTransfer` object. To set one of the possible predefined cursors, we specify an effect in the `dragstart` handler, and we set the effect (to "move", "copy", etc.) in the `dragEnter` or `dragOver` handler.

Here is an extract of the code we can add to the example we saw earlier:

<div><ol>
<li value="1">function dragStartHandler(event) {</li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">// Allow a "copy" cursor effect</strong></li>
<li>&nbsp; &nbsp;&nbsp;<strong style="color: red;">event.dataTransfer.effectAllowed = 'copy';</strong></li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>}</li>
</ol></div>

And here is where we can set the cursor to a permitted value:

<ol>
<li value="1">function dragEnterHandler(event) {</li>
<li>&nbsp; &nbsp;<strong style="color: red;">// change the cursor shape to a "+"</strong></li>
<li>&nbsp; &nbsp;<strong style="color: red;">event.dataTransfer.dropEffect = 'copy';</strong> </li>
<li>&nbsp; &nbsp;...</li>
<li>}</li>
</ol><br>

To set a custom image, we also do the following in the `dragstart` handler:

<div><ol>
<li value="1">function dragStartHandler(event) {</li>
<li>&nbsp; &nbsp;// allowed cursor effects</li>
<li>&nbsp; &nbsp;event.dataTransfer.effectAllowed = 'copy';</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">// Load and create an image</strong></li>
<li>&nbsp; &nbsp;var dragIcon = document.createElement('img');</li>
<li>&nbsp; &nbsp;dragIcon.src = 'anImage.png';</li>
<li>&nbsp; &nbsp;dragIcon.width = 100;</li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">// set the cursor to this image, with an offset in X, Y</strong></li>
<li>&nbsp; &nbsp;<strong style="color: red;">event.dataTransfer.setDragImage(dragIcon, -10, -10);</strong></li>
<li>&nbsp; &nbsp;...</li>
<li>}</li>
</ol></div>


#### Complete online example

Here is the previous example (with apples, oranges, etc) that sets a "copy" cursor and a custom image. Try it in your browser below (start to drag and wait a few seconds for the image to be loaded. You might have to try twice before it works) or [play with it at CodePen](https://codepen.io/w3devcampus/pen/ZbEpEE):

[Local Demo](src/03c-example06.html)

Here are the various possible values for cursor states (your browser will not necessarily support all of these; we noticed that copyMove, etc. had no effect with Chrome, for example). The values of "move", "copy", and "link" are widely supported.

All possible values for `dropEffect` and `effectAllowed`:

+ __`dataTransfer.effectAllowed`__ can be set to the following values: `none`, `copy`, `copyLink`, `copyMove`, `link`, `linkMove`, `move`, `all`, and `uninitialized`.
+ __`dataTransfer.dropEffect`__ can take on one of the following values: `none`, `copy`, `link`, `move`.


#### Notes for 3.3.6 The dropEffect property

+ The `dropEffect` property
  + changing the cursor's shape during the drag process
  + turning cursor into a "copy", "move" or "link" icon, depending on the semantic of the drag and drop
    + copy icon: copying an object into the drop zone
    + moving icon: moving an object
    + link icon: making a link or shortcut
  + alternative: using any customized image/icon
  + visual feedback:
    + using the `effectAllowed` and `dropEffect` properties of the `dataTransfer` object
    + specifying an effect in the `dragStart` handler by setting one of the possible predefined cursors
    + specifying the effect (to "copy", "move", etc.) in the `dragEnter` and `dragOver` handlers

+ Possible values for `dropEffect` and `effectAllowed` properties
  + `dataTransfer.effectAllowed`: `none`, `copy`, `copyLink`, `copyMove`, `link`, `linkMove`, `move`, `all`, `uninitialized`
  + `dataTransfer.dropEffect`: `none`, `copy`, `link`, `move`

+ Syntax of visual effect for drag and drop
  + allow a copy cursor effect: `function dragStartHandler(evt) { evt.dataTransfer.effecctAllowed = 'copy'; ... }`
  + change the cursor shape to a '+': `function dragEnterHandler(evt) { evt.dataTransfer.dropEffect = 'copy'; ... }`

+ Example: customerized image
  + add drag start handler: `function dragStartHandler(evt) {...}`
  + allow cursor effect: `evt.dataTransfer.effectAllowed = 'copy';`
  + load and create image: `var dragIcon = document.createElement('img'); dragIcon.src = 'anImage.png'; dragIcon.width = 100;`
  + set the cursor to this image: `evt.dataTransfer.setDragImage(dragIcon, -10, -10);`
  + ...



### 3.3.7 Drag and drop HTML elements


#### Drag and drop images or any HTML element within a document

We saw the main principles of HTML5 drag and drop in the previous sections. There are other interesting uses that differ in the way we copy and paste things to/from the clipboard. The clipboard is accessed through the `dataTransfer` property of the different events:

<div><ol>
<li value="1">event.dataTransfer.setData("Fruit", event.target.dataset.value);</li>
<li>...</li>
<li>var data = event.dataTransfer.getData("Fruit");</li>
</ol></div>

__`<img>` elements are all draggable by default!__

Normally, to make an element draggable, you must add the `draggable=true` attribute. `<img>` elements are an exception: they are draggable by default! The next example shows how to drag and drop an image from one location in the document to another.

#### Example: move images as an HTML subtree

Try this example (adapted from [braincracking.org](https://bit.ly/3ytA18W) (in French)) in your browser below or [play with it at CodePen](https://codepen.io/w3devcampus/pen/xwxEZg):

[Local Demo](src/03c-example07.html)

Code from the example:

<div><ol>
<li value="1">&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;style&gt;</li>
<li>&nbsp; &nbsp;.box {</li>
<li>&nbsp; &nbsp; &nbsp; border: silver solid;</li>
<li>&nbsp; &nbsp; &nbsp; width: 256px;</li>
<li>&nbsp; &nbsp; &nbsp; height: 128px;</li>
<li>&nbsp; &nbsp; &nbsp; margin: 10px;</li>
<li>&nbsp; &nbsp; &nbsp; padding: 5px;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;float: left;</li>
<li>&nbsp; &nbsp;}</li>
<li> &lt;/style&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp;&nbsp;function drag(target, evt) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; evt.dataTransfer.setData("Text", target.id);</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;&nbsp;function drop(target, evt) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var id = evt.dataTransfer.getData("Text");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; target.appendChild(document.getElementById(id));</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// prevent default behavior</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; evt.preventDefault();</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li> &lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> Drag and drop browser images in a zone:&lt;br/&gt;</li>
<li>&nbsp; &nbsp;&lt;img src="https://mainline.i3s.unice.fr/mooc/ABiBCwZ.png" id="cr"&nbsp; &nbsp; &nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ondragstart="drag(this, event)" alt="Logo Chrome"&gt;</li>
<li>&nbsp; &nbsp;&lt;img src="https://mainline.i3s.unice.fr/mooc/n7xo93U.png" id="ff" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ondragstart="drag(this, event)" alt="Logo Firefox"&gt;</li>
<li>&nbsp; &nbsp;&lt;img src="https://mainline.i3s.unice.fr/mooc/ugUmuGQ.png" id="ie" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ondragstart="drag(this, event)" alt="Logo IE"&gt;</li>
<li>&nbsp; &nbsp;&lt;img src="https://mainline.i3s.unice.fr/mooc/jfrNErz.png" id="op" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ondragstart="drag(this, event)" alt="Logo Opera"&gt;</li>
<li>&nbsp; &nbsp;&lt;img src="https://mainline.i3s.unice.fr/mooc/gDJCG0l.png" id="sf" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; ondragstart="drag(this, event)" alt="Logo Safari"&gt;&lt;br/&gt;</li>
<li> </li>
<li>&nbsp; &nbsp;&lt;div class="box" ondragover="return false" ondrop="drop(this, event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;Good web browsers&lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/div&gt;</li>
<li>&nbsp; &nbsp;&lt;div class="box" ondragover="return false" ondrop="drop(this, event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&lt;p&gt;Bad web browsers&lt;/p&gt;</li>
<li>&nbsp; &nbsp;&lt;/div&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

The trick here is to only work on the DOM directly. We used a variant of the event handler proposed by the DOM API. This time, we used handlers with two parameters (the first parameter, `target`, is the element that triggered the event, and the second parameter is the event itself). In the `dragstart` handler we copy just the `id` of the element in the DOM (_line 15_).

In the drop handler, we just move the element from one part of the DOM tree to another (under the `<div>` defined at _line 38_, that is the drop zone). This occurs at _line 18_ (get back the `id` from the clipboard), and _line 19_ (make it a child of the div. Consequently, it is no longer a child of the `<body>`, and indeed we have "moved" one `<img>` from its initial position to another location in the page).


#### Notes for 3.3.7 Drag and drop HTML elements

+ Drag and drop HTML elements
  + copy and past to/from the clipboard
  + clipboard accessed through the `dataTransfer` property of the different evnets
    + copy data into the clipboard: `event.dataTransfer.setData("Fruit", event.targte.dataset.value);`
    + past data from the clipboard: `var data = event.dataTransfer.getData("Fruit");`
  + `<img>` elements all draggable by default

+ Example: moving images as an HTML subtree
  + tasks
    + only work on the DOM directly
    + move icon from child of `<body>` to child of selected container
  + HTML snippet
    + list of browser icons:
      + Chrome: `<img src="https://.../chrome.png" id="cr" ondragstart="drag(this, event)" alt="Logo Chrome">`
      + Firefox: `<img src="https://.../firefox.png" id="ff" ondragstart="drag(this, event)" alt="Logo Firefox">`
      + IE: `<img src="https://.../ie.png" id="ie" ondragstart="drag(this, event)" alt="Logo IE">`
      + Opera: `<img src="https://.../opera.png" id="op" ondragstart="drag(this, event)" alt="Logo Opera">`
      + Safari: `<img src="https://.../safari.png" id="sf" ondragstart="drag(this, event)" alt="Logo Safari">`
    + containers for good and bad browser drop zones
      + good: `<div ondragover="return false" ondrop="drop(this, event)"><p>Good web browsers</p></div>`
      + bad: `<div ondragover="return false" ondrop="drop(this, event)"><p>Bad web browsers</p></div>`
  + CSS style<a name="boxStyle"></a>: `.box { border: silver solid; width: 256px; height: 128px; margin: 10px; padding: 5px; float: left; }`
  + JavaScript snippet
    + add drag handler: `function drag(target, evt) { evt.dataTransfer.setData("Text", target.id); }`
    + add drop handler: `function drop(target, evt) {...}`
      + retrieve selected icon from clipboard: `var id = evt.dataTransfer.getData("Text");`
      + move icon to selected drop zone: `target.appendChild(document.getElementBuId(id));`
      + prevent default behavior: `evt.preventDefault();`


### 3.3.8 Drag and drop a text selection


#### Moving selected text to drop zone

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3jPrsB2')"
    src    = "https://bit.ly/3dN6QFG"
    alt    = "drag and drop text selection"
    title  = "drag and drop text selection"
  />
</figure>


__There is no need to add a `dragstart` handler on an element that contains text.__ Any selected text is automatically added to the clipboard with a name/key equal to "text/plain". Just add a `drop` event handler on the drop zone and fetch the data from the clipboard using "text/plain" as the access key:

<div><ol>
<li value="1">function drop(target, event) {</li>
<li>&nbsp; &nbsp;event.preventDefault();</li>
<li>&nbsp; &nbsp;target.innerHTML = event.dataTransfer.getData(<strong style="color: red;">'text/plain'</strong>);</li>
<li>};</li>
</ol></div>


#### Example: select some text and drag and drop the selection in the drop zone

Try it in your browser below (select text, then drag and drop it into the drop zone) or [play with it at CodePen](https://codepen.io/w3devcampus/pen/vNYXyR):

[Local Demo](src/03c-example08.html)

Complete source code from the example:

<div><ol>
<li value="1">&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;style&gt;</li>
<li>&nbsp; &nbsp;.box {</li>
<li>&nbsp; &nbsp; &nbsp; border: silver solid;</li>
<li>&nbsp; &nbsp; &nbsp; width: 256px;</li>
<li>&nbsp; &nbsp; &nbsp; height: 128px;</li>
<li>&nbsp; &nbsp; &nbsp; margin: 10px;</li>
<li>&nbsp; &nbsp; &nbsp; padding: 5px;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;float: left;</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;.notDraggable {</li>
<li>&nbsp; &nbsp; &nbsp; user-select: none;</li>
<li>&nbsp; &nbsp;}</li>
<li> &lt;/style&gt;</li>
<li> &lt;script&gt; </li>
<li>&nbsp; &nbsp;&nbsp;function drop(target, event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.preventDefault();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;target.innerHTML = event.dataTransfer.getData('text/plain');</li>
<li>&nbsp; &nbsp;&nbsp;};</li>
<li> &lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;p id="text"&gt;</li>
<li>&nbsp; &nbsp; &lt;b&gt;Drag and drop a text selection from this paragraph&lt;/b&gt;. Drag and drop any</li>
<li>&nbsp; &nbsp; part of this text&nbsp;to </li>
<li>&nbsp; &nbsp; the drop zone. Notice in the code: there is no need for a dragstart handler in case of </li>
<li>&nbsp; &nbsp; text selection: </li>
<li>&nbsp; &nbsp; the text is added to the clipboard when dragged with a key/name equal to "text/plain". </li>
<li>&nbsp; &nbsp; Just write a </li>
<li>&nbsp; &nbsp; drop handler that will do an event.dataTransfer.getData("text/plain") and you are </li>
<li>&nbsp; &nbsp; done!</li>
<li>&nbsp;&lt;/p&gt;</li>
<li> </li>
<li> <strong style="color: red;">&lt;p class="notDraggable"&gt;</strong></li>
<li>&nbsp; &nbsp; &nbsp;This paragraph is not <g id="29" data-gr-id="29">selectable</g> however. Look at the CSS in the&nbsp;source code.</li>
<li>&lt;/p&gt;</li>
<li> </li>
<li> &lt;div class="box" ondragover="return false" ondrop="drop(this, event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;p&gt;Drop some text selection here.&lt;/p&gt;</li>
<li> &lt;/div&gt; </li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

Here, we use a CSS trick to make the second paragraph non-selectable, by setting the `user-selected` property to none.

In the next chapter, we will see how to drag and drop files!


#### Notes for 3.3.8 Drag and drop a text selection

+ Moving selected text
  + no need to add a `dragstart` handler on an element containing text
  + selected text automatically added to the clipboard w/ a name/key equal to "text/plain"
  + adding a `drop` event handler on the drop zone
  + "text/plain" as the access key to fetch the data from the clipboard
  + typical syntax: `function drop(target, event) { event.preventDefault(); target.innerHTML = event.dataTransfer.getData('text/plain'); }`

+ Example: moving selected text to the drop zone
  + tasks:
    + use a CSS trick to make a paragraph non-selectable
    + move selected text to a drop zone
  + HTML snippet:
    + text not draggable: `<p>This paragraph is not selectable ...</p>`
    + container for drop zone: `<div ondragover="return false" ondrop="drop(this, event)"><p>Drop some text selectoin here.</p></div>`
  + CSS style
    + [box style](#boxStyle)
    + style for not draggable: `.notDraggable { user-select: none; }`
  + JavaScript snippet:
    + add drop handler: `function drop(target, event) {...}`
    + prevent default: `event.preventDefault();`
    + display selected text: `target.innerHTML = event.dataTransfer.getData("text/plain");`


### 3.3.9 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics of discussion:

+ If you find interesting drag and drop examples on the Web, please share them in the forum.
+ What other example(s) would you like to be added to the course (drag and drop of files is covered in the next lesson)?


#### Optional projects:

+ Code an illustrative drag and drop demo, and share it in the forum. For example, try to add something similar to the "what is your preferred fruit" or "what is your preferred browser" to a form.
+ Order a set of images by dragging and dropping them. A sort of picture gallery, you drag one picture (an <img> element) from its current position and drop it at another location in the gallery (a grid). In the meantime, the other pictures will have to move to give some room for the picture you dropped.


