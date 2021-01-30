# Module 2: Adding interactivity to HTML documents

## 2.4 Handling events

### 2.4.1 Introduction

Adding interactivity to a Web application can be achieved by using only CSS, such as by using the `:hover`2.4.1 Introduction pseudo CSS class.

For example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/gmvgxa)

[Local Demo](src/02d-example01.html)

However, firing a specific action when the button is clicked, knowing which mouse button has been used, computing the (x, y) mouse pointer position in the button system coordinate, or executing more complex tasks can only be done through JavaScript.

With JavaScript, a button click, a move of the mouse, a resized window, and many other interactions create what are called "events".  The timing and order of events cannot be predicted in advance. We say that "event processing" is asynchronous. Web browsers detect events as they occur, and may pass them to JavaScript code. They do this by allowing you to register functions as _event listeners_, also called _handlers_ or _callbacks_ for specific events.

Each time an event occurs, the browser puts it in a "queue of events".

Then the browser looks at a list of "Event Listeners" and calls the ones that correspond to the type of event "they listen to".

#### Notes for 2.4.1 Introduction

+ Interactivity of Web application
  + CSS:
    + limited w/ pseudo CSS class
    + example. `.hover`
  + JavaScript:
    + extended features
    + examples: mouse button clicked
      + which mouse button used
      + mouse pointer position in button system coordinate
      + executing more complex tasks
  + events
    + interaction created, e.g., button clicked, mouse movement, window resized
    + timing and order unable to be predicted in advance
    + asynchronous event processing
    + event listerners
      + a.k.a. handlers or callbacks for special event
      + registered functions
      + web browser detecting events as they occur
      + pass these events to JavaScript code
    + events placed in "queue of events"
    + browser looks at a list of "Event Listerners" and calls the ones corresponding to the type of evenet listening to


### 2.4.2 Adding and removing event listeners

#### Live coding video: adding an event listener to a document

<a href="https://edx-video.net/W3CJSIXX2016-V002800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y6ebbnap)

Online example used in the above video:

[CodePen Demo](https://codepen.io/w3devcampus/pen/zzOVGB?editors=1000)

[Local Demo](src/02d-example02.html)


#### Live coding video: adding an event listener to a specific HTML element

<a href="https://edx-video.net/W3CJSIXX2016-V002900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/yxpvgolf)

Online example used in the above video

[CodePen](https://codepen.io/w3devcampus/pen/pwzXqb?editors=1000)

[Local Demo](src/02d-example03.html)


#### Event listeners: a typical example

Here is one possible syntax for registering an event listener that listens to "click" events on any part of the window (clicks anywhere on a web document will be processed by this event handler):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">&lt;script&gt;</li>
<li class="L2" style="margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;<span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><strong><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong><br><span class="pln"></span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>document.body.innerHTML += 'Button clicked!';</strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span></strong><span class="pun"><strong>&nbsp; &nbsp; }</strong>);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
</ol></div>

Try it below by clicking anywhere on the document:

[CodePen Demo](https://codepen.io/w3devcampus/pen/peaeoZ)

[Local Demo](src/02d-example04.html)

The `addEventListener` function is one possible syntax for registering a function to be called when a given type of event occurs.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">addEventListener</span><span class="pun">(</span><span class="pln">type_of_event</span><span class="pun">,</span><span class="pln"> callback_function</span><span class="pun">)</span></li>
</ol></div>

In the example below, the type of event is a 'click', and the callback function is the part in bold:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Button clicked!"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

When this function is small (a few lines of code), it's common practice to put its body as the second parameter of the `addEventListener` function.

In other words, this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><strong><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong>document.body.innerHTML += 'Button clicked!';</strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong><span class="pun"><strong>}</strong>);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
</ol></div>

... is the same as this (the function called when a click occurs has its body "outside" of the `addEventListener` parameters, and we use its name as the second parameter):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><strong><span class="pln"> processClick</span></strong><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><strong><span class="pln"> processClick</span></strong><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Button clicked!"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
</ol></div>


#### Adding an event listener to specific HTML elements

Instead of listening to event on the whole document (using `addEventListener` is the same as using `window.addEventListener`), we can listen to specific DOM elements.

For example, here is how we can listen to clicks on a specific button (whereas clicks on the rest of the document will be ignored).

[CodePen Demo](https://codepen.io/w3devcampus/pen/vxdxdm)

[Local Demo](src/02d-example05.html)

In this example, instead of using the `addEventListener` method directly, we used it on a DOM object (the button):

1. Get a reference of the HTML element that can fire the events you want to detect. This is done using the DOM API that we'll cover in detail later this week. In this example we used one of the most common/useful methods: `var b = document.querySelector("#myButton");`
2. Call the `addEventListener` method on this object. In the example: `b.addEventListener('click', callback)`

Every DOM object has an `addEventListener` method. Once you get a reference of  any HMTL element from JavaScript, you can start listening to events on it.

__An alternative method for adding an event listener to an HTML element: use an "on" attribute (ex: `onclick = "...."`)__

Instead of using `b.addEventListener('click', callback)`, it's possible to use an `onclick='doSomething();'` attribute directly in the HTML tag of the element:

[CodePen Demo](https://codepen.io/w3devcampus/pen/aJqWZJ)

[Local Demo](src/02d-example06.html)

This syntax:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myButton"</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">processClick</span><span class="pun">(</span><span class="pln">event</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Click me!</span><span class="tag">&lt;/button&gt;</span></li>
</ol></div>

... is ok when you only need a single event listener to click events for this button, as there can be only one `onclick` attribute per element.

Using the `b.addEventListener('click', callback)` syntax,  you can register more than one event listener. You'll need rarely to do this, so in my opinion it's fine to choose whichever syntax you like.

Remember that for big projects, it's always better to separate the HTML, CSS and JavaScript code. In this case, I'd recommend that you put all your event listener definitions in a separate JavaScript file, and use the `addEventListener` syntax in preference to the "on" attributes syntax.


#### Removing event listeners

When we click on the button, we execute the `processClick(evt)` callback function, and inside we remove the listener we previously registered. Consequence: if we click on the button again, nothing happens as there is no longer a click event listener attached to it.

[CodePen Demo](https://codepen.io/w3devcampus/pen/PpRBxP)

[Local Demo](src/02d-example07.html)

Note that to remove an event listener, you should have added it with its named function, so that we can pass it to both `addEventListener` and `removeEventListener`.


#### Notes for 2.4.2 Adding and removing event listeners

+ Event listerners
  + `addEventListener` function
    + one possible syntax for registering as function to be called when a given type of event occurs
    + syntax: `addEventListener(typeOfEvent, callbackFunction)`
    + able to register more than one event listener
    + procedure
      + listening to event on the whole document: `addEventListener` = `window.addEventListener`
      + listening to specific DOM elements
        + get a reference of the HTML to detect the event; e.g., `var b = document.querySelector("#myButton");`
        + call the `addEventListener` method on the object; e.g., `b.addEventListener('click', callback);`
    + ensuring the existence before electing an element w/ `querySelector`
    + every DOM object w/ an `addEventListener` method starting listening to event on it, once getting a reference of any HTML element from JS
    + example

      ```js
      addEventListener('click', function(evt) {
          document.body.innerHTML += 'Button clicked!';
      });
      ```

  + `on` attribute
    + adding an event listener to an HTML tag of an element directly
    + syntax in HTML: `onclick='doSomething();`
    + limited to a single event listener to click on this button
    + example: `<button id="myButton" onclick="processClick(event);">Click me!</button>`
  + big project
    + better to separate the HTML, CSS and JS code
    + recommended putting all event listener definition in a separate JS file
    + using `addEventListener` syntax in preference to the "on" attribute syntax
  + removing event listener
    + removing previous registered event listener
    + syntax: `removeEventListener(TypeOfEvent, callBackFunction)`
    + must pass `callBackFunction` used in `addEventListener` to remote
    + example: `b.removeEventListener('click', processClick);`

+ Ways to provide callback function
  + standard function block
  + function expression: common practice w/ small function
  + examples

    ```js
    // standard function block
    function(evt) {
      console.log("Button clicked!");
    }
    ```

    ```html
    <!-- function expression -->
    <script>
    addEventListener('click', function(evt) {
        document.body.innerHTML += 'Button clicked!';
    });
    </script>
    ```


#### Knowledge check 2.4.1

1. What precaution should you take when adding an event listener to a given HTML element?

  a. I need to be sure that the element is in the DOM before selecting it using the DOM API or the selector API<br/>
  b. Nothing special<br/>

  Ans: <span style="color: brown;">a</span>, xb<br/>
  Explanation: Indeed, we need to be sure that the element is in the DOM before quering it. You can do that by locating the JavaScript code after the HTML tag that corresponds to the element, or do this in a JavaScript function that is called only when the DOM is ready, for example using <body onload="init()">, and put the code in the init function.



