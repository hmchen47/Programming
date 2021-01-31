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


### 2.4.3 The event object

The event object is the only parameter passed to event listeners.

Typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">function<span class="pln"> processClick</span><span class="pun">(</span><strong><span class="pln">evt</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">"Button clicked!"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>

Each event listener has a single parameter that is  a "DOM event object". It has various properties and methods that can be very useful.

For example, with a `'keyup'`, `'keydown'` or `'keypress'` event, the event object contains the code of the key that has been pressed/released, with a `'mousemove'` listener we can get the relative position of the mouse in the DOM element that has generated the event, etc.

The event object contains some important properties and methods that are common to all types of events:

+ __evt.type__: the name of the event
+ __evt.target__: for example, is the HTML element that has fired the event. In our previous examples with the click listeners on a button, __evt.target__ in the event listener is the button itself.
+ __evt.stopPropagation()__: will not propagate the event to all other elements that listen to it. If several elements are registered for a click event - for example, you have a click listener on a button and on the window (the whole page). If you click on the button, and if in its click event listener you call `evt.stopPropagation();` then the click event listener on the window object will never be called.
+ __evt.preventDefault()__: the default browser behavior will not be executed. For example, in a 'contextmenu' event listener attached to an object, if you call __evt.preventDefault()__, instead of having the right click default context menu of your browser displayed, you'll be able to display your own context menu, like [in this example](https://jsbin.com/kuyorac/edit?html,css,js,console,output). ([Local Demo]())

It also contains properties that are associated with the type of the event, for example:

+ __evt.button__: the mouse button that has been used in the case of a mouse event listener
+ __evt.keyCode__: the code of the key that has been used
+ __evt.pageX__: coordinate of the mouse relative to the page
+ etc.

In the subsequent sections of this course we will look at the most common types of events in detail.


#### Reference table

The most useful common properties are:

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray;" valign="top">type</td>
  <td style="border: 2px solid LightSlateGray;" valign="top">Returns the name of the event.</td>
</tr>
<tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray;" valign="top">target</td>
  <td style="border: 2px solid LightSlateGray;" valign="top">Returns the element that triggered the event.</td>
</tr>
</tbody>
</table>

The most useful common methods are:

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top">preventDefault()</td>
  <td style="border: 2px solid SlateGray;" valign="top">Cancels the event if it is "cancelable", meaning that the default action that belongs to the event will not occur. It is useful for cancelling the default browser behavior. <em>For example</em>: if you want to create a context menu that pops up with a right click, you must prevent the default behavior of the browser that will pop up its default context menu.</td>
</tr>
<tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top">stopPropagation()</td>
  <td style="border: 2px solid SlateGray;" valign="top">Prevents further propagation of an event during event flow.<br><br></td>
</tr>
</tbody>
</table>


#### Notes for 2.4.3 The event object

+ Event object
  + DOM event object
    + the only parameter passed to event listener
    + containing various properties and methods
  + common properties and methods
    + `evt.type`: the name of the event
    + `evt.target`: the HTML element fired the event, e.g., `evt.target` = button as the click listeners on the button
    + `evt.stopPropagation()`:
      + several elements registered for an event
      + not propagating the event to all other elements that listen to it
      + example:
        + several element registered for a click on the button
        + a click listener on a button and on the window (the whole page)
        + click on the button, the event listener calling `evt.stopPropagation()`
        + the click event listener on the window object never be called
    + `evt.preventDefault()`:
      + default browser behavior not be executed
      + example: `contextmenu` event listener attached to an object for user's own contextmenu
  + typical specific properties associated w/ the type of the event
    + `evt.button`: mouse button used in case of a mouse event listerner
    + `evt.keyCode`: code of the key been used
    + `evt.pageX`: coordinate of the mouse relative to the page
  + examples
    + key related events: `keyup`, `keydown` and `keypress` for key pressed/released
    + mouse related position: `mouseover` to get mouse postion in the DOM element generated the event

+ Most useful common properties and methods
  + properties
    + `type`: returning the name of the event
    + `target`: returning the element triggering the event
  + methods
    + `preventDefault()`:
      + cancelling the cancelable event
      + the default action belonging to the event not occuring
      + useful for cancelling the default browser behavior
    + `stopPropagation()`: preventing further propagation of an event flow


### 2.4.4 Page lifecycle events

#### Live coding video: page 'load' event and the event object

<a href="https://edx-video.net/W3CJSIXX2016-V003000_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y4u8h54w)

Online example used in the above video

[CodePen Demo](https://codepen.io/w3devcampus/pen/XgrveY?editors=0001)

[Local Demo](src/02d-example09.html)

The page lifecycle events detect when the page is loaded and when the DOM is ready.

#### Events related to the page lifecycle

There are many other events related to the page life cycle. The most useful ones for an introduction course are shown below:

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border-width: 2px; border-color: lightslategray; vertical-align: middle;" valign="top">load</td>
  <td style="border-width: 2px; border-color: lightslategray;" valign="top">This event occurs when an object has loaded (including all its resources: images, etc.). This event is very useful when you want to run JS code and be sure that the DOM is ready (in other words, be sure that a <span style="font-family: 'courier new', courier;">document.getElementById(...)</span> or <span style="font-family: 'courier new', courier;">document.querySelector(...)</span> will not raise an error because the document has not been loaded and elements you are looking for are not ready).</td>
</tr>
<tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border-width: 2px; border-color: lightslategray; vertical-align: middle;" valign="top">resize</td>
  <td style="border-width: 2px; border-color: lightslategray;" valign="top">The event occurs when the document view is resized. Usually, we get the new size of the window inside the event listener using <span style="font-family: 'courier new', courier;">var w = window.innerWidth;</span> and<br><span style="font-family: 'courier new', courier;">var h = window.innerHeight;</span></td>
</tr>
<tr>
  <td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border-width: 2px; border-color: lightslategray; vertical-align: middle;" valign="top">scroll</td>
  <td style="border-width: 2px; border-color: lightslategray;" valign="top">The event occurs when an element's scrollbar is being scrolled. Usually in the scroll event listener we use things such as:<br>&nbsp;&nbsp;<span style="font-family: 'courier new', courier;">var max = document.body.scrollHeight - innerHeight;</span><br><span style="font-family: 'courier new', courier;">&nbsp;var percent = (pageYOffset / max);</span><br>...to know the percentage of the scroll in the page.</td>
</tr>
</tbody>
</table>


##### Page event properties

There are no particular properties that need to be mentioned here. Usually, the load event listener corresponds to a JavaScript function that can be seen as "the main" function of your Web application. It is a best practice to start everything after the page has been completely loaded. In the resize listener, you get the new size of the window, or the new size of some HTML elements in the page (as they might have been resized too when the window was resized), and then you do something (redraw a graphic in an HTML canvas that takes into account the new canvas size, for example).


#### Examples

##### Example 1: wait until the page is loaded (when the DOM is ready) before doing something

This first variant that uses `<body onload="init();">`

[CodePen Demo](https://codepen.io/w3devcampus/pen/vxMgvw)

[Local Demo](src/02d-example10.html)

This second variant: using `window.onload = init;` in the JavaScript code...

[CodePen Demo](https://codepen.io/w3devcampus/pen/EWJZeE)

[Local Demo](src/02d-example11.html)


##### Example 2: detect a resize of the window

In this example, we're listening to page `load` and page `resize` events. When the window is loaded for the first time, or resized, we call the `resize()` callback function. The `window.innerWidth` and `window.innerHeight` properties are used to display the updated size of the window. We also use `screen.width` and `screen.height` to display the screen size.

[CodePen Demo](https://codepen.io/w3devcampus/pen/YZMZaw)

[Local Demo](src/02d-example12.html)


##### Example 3: do something as the page is being scrolled up or down

[CodePen Demo](https://codepen.io/w3devcampus/pen/EWJWMq)

[Local Demo](src/02d-example13.html)


#### Notes for 2.4.4 Page lifecycle events

+ Page lifecycle events
  + detected when the page loaded and DOM ready
  + related events
    + `load`:
      + occurred when an object loaded (including all resources)
      + ensuring DOM ready before executing JS code, in particular, `document.getElementId(...)` or `document.querySelector(...)`
    + `resize`:
      + occurred when resizing document view
      + new size of window: `var w = window.innerWidth;` & `var h = window.innerHeight;`
    + `scroll`
      + occurred when scrolling an element's scrollbar
      + usually knowing the percentage of the scroll in the page: `var max = document.body.scrollHeight - innerHeight; var percent = (pageYOffset / max);`
  + ways to wait until page loaded
    + `<body onload="init();">` in HTML
    + `window.onload = init;` in JS code
    + `window.addEventListener('load', init);` in JS code
  + window resizing
    + calling callback function as the window loaded for the first time or resized; e.g., `resize()`
    + used to display the updated size of the window w/ `window.innerWidth` and `window.innerHeight`
    + displaying the screen size w/ `screen.width` and `screen.height`


#### Knowledge check 2.4.2

```js
function init(evt) {
   console.log("Page loaded! DOM Ready!");
   // access the DOM using the DOM API or the selector API
   var elem = document.querySelector(...);
   elem.innerHTML = ....;
}
```

1. Check the correct ways to call the function init only when the page has loaded and the DOM is ready:

  a. `<body onload="init();">`<br/>
  b. In a JS code, add `window.onload = init;`<br/>
  c. in a JS code, add `window.addEventListener('load', init);`<br/>

  Ans: <span style="color: brown;">abc</span>, xab<br/>
  Explanation: All answers are correct. All of these syntaxes have the same effect: call init once the page is loaded.


### 2.4.5 Key events

This has been a bit of a nightmare for years, as different browsers have had different ways of handling key events and key codes ([read this](https://unixpapa.com/js/key.html) if you are fond of JavaScript archeology). Fortunately it's much better today, and we are able to rely on methods that should work on any browser.

When you listen to keyboard related events (`keydown`, `keyup` or `keypressed`), the event parameter passed to the listener function will contain the code of the key that fired the event. Then it is possible to test which key has been pressed or released, like this:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun" style="color: #666600;">.</span><span class="pln">addEventListener</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'keydown'</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666600;">(</span><span class="kwd" style="color: #008888;">event</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">if</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">(</span><strong><span class="kwd" style="color: #008888;">event</span><span class="pun" style="color: #666600;">.</span><span class="pln">keyCode&nbsp;</span><span class="pun" style="color: #666600;">===</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">37</span></strong><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com" style="color: #880000;">//left arrow was pressed</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span><span class="pun" style="color: #666600;">);</span></li>
</ol></div>

At _line 2_, the value "37" is the key code that corresponds to the left arrow. It might be difficult to know which codes represent which real keyboard keys, so here are some handy pointers:

+ Try key codes with this [interactive example](http://www.asquare.net/javascript/tests/KeyCode.html).
+ And find a list of keyCodes (taken from this CSS Tricks [article](https://css-tricks.com/snippets/javascript/javascript-keycodes/#keycode-values)).


#### The different key events

##### Event types related to keyboard

<table style="the event occurs when the user presses a keyborder: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">keydown</span></td>
<td style="border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">The event occurs when the user is pressing a key.</span></td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">keyup</span></td>
<td style="border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">The event occurs when the user releases a key.</span></td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">keypress (now deprecated)</span></td>
<td style="border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">The event occurs when the user presses a key (up and release).</span></td>
</tr>
</tbody>
</table>


#### keyboardEvent properties

These are legacy properties, still used by many JavaScript code around the world. However, we do not recommend that you use them if you are targeting modern browsers. `keyCode` has a more powerful/easy to use replacement called `code` @@TJS LE CAS ? (not yet supported by all browsers), that comes with a new `key` property (see the following pages of the course).

<table style="table-layout: auto; border: 5px solid LightSlateGray; color: black; font-size: 100%; font-family: arial,helvetica,sans-serif;" cellspacing="0" cellpadding="5" border="0" align="center">
<tbody>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">keyCode</span></td>
<td style="border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">Returns the Unicode character code of the key that triggered the onkeypress ,onkeydown or onkeyup event.</span></td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">shiftKey</span></td>
<td style="border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">Returns whether the "shift" key was pressed when the key event was triggered.</span></td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 120%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">ctrlKey</span></td>
<td style="border: 2px solid LightSlateGray;" valign="top"><span style="font-family: 'Open Sans',Verdana,Arial,Helvetica,sans-serif;">Returns whether the "ctrl" key was pressed when the key event was triggered.</span></td>
</tr>
<tr>
<td style="text-align: center; background-color: lightslategray; color: white; font-size: 150%; border: 2px solid LightSlateGray; vertical-align: middle;" valign="top">altKey</td>
<td style="border: 2px solid LightSlateGray;" valign="top">Returns whether the "alt" key was pressed when the key event was triggered</td>
</tr>
</tbody>
</table>


#### Examples


##### Example #1: use keyup and keydown on the window object

[CodePen Demo](https://codepen.io/w3devcampus/pen/wJZJZp)

[Local Demo](src/02d-example14.html)


##### Example #2: see  keypress on the window object

See the Pen [keyup and keydown events on window](https://codepen.io/w3devcampus/pen/WpWjey/) by W3Cx ([@w3devcampus](https://codepen.io/w3devcampus)) on [CodePen](https://codepen.io/).

[CodePen Demo](https://codepen.io/w3devcampus/pen/WpWjey/)

[Local Demo](src/02d-example15.html)


##### Example #3: detect a combination of keys + modifier keys (shift, ctrl, alt)

Try to type shift-a for example, ctrl-shift-b or alt-f...

[CodePen Demo](https://codepen.io/w3devcampus/pen/BWERyY)

[Local Demo](src/02d-example16.html)


#### Notes for 2.4.5 Key events

+ Key events
  + related events: `keydown`, `keyup` and `keypress`
  + event parameter passed to the listener function containing the code of the key that fired the event
  + example:

    ```js
    window.addEventListener('keydown', function(evt) {
      if (evt.keyCode === 37) {
        // left arrrow pressed
      }
    })
    ```

  + key code w/ keyboard keys
    + [JavaScript Event KeyCode Test Page](http://www.asquare.net/javascript/tests/KeyCode.html)
    + [list of keycode values](https://css-tricks.com/snippets/javascript/javascript-keycodes/#keycode-values)
  + key events
    + `keydown`: pressing a key
    + `keyup`: releasing a key
    + `keypress` (deprecated): pressing a key or up and release
  + keyboardEvent properties
    + `keyCode`
      + more powerful/easy to use (legacy properties still used by many JS code)
      + return the Unicode character code of the key
      + triggering the onkeypress, onkeydown or onkeyup event
    + `shiftKey`: return whether the "shift" key pressed when the key event triggered
    + `ctrlKey`: return whether the "ctrl" key pressed when the key event triggered
    + `altKey`: return whether the "alt" key pressed when the key event triggered
    + examples:
      + regular keys: `keys.innerHTML += "keypress: " + evt.key + " code: " + evt.keyCode + " Modifiers : ";`
      + modifier keys: `if(evt.ctrlKey) modifiers += "CTRL ";`


#### Knowledge check 2.4.5

1. Which of one of these events is now deprecated?

  a. `keypress`<br/>
  b. `keydown`<br/>
  c. `keyup`<br/>

  Ans: a


### 2.4.6 Dealing with different keyboard layouts

Please do not assume that each key is at the same location on the keyboard in every country!

We've shown how to detect keyup, keydown and keypress events using the DOM API, and how to use the keyCode property of the DOM event.

Be careful when you use the key events in your application, as keyboard layouts vary from one country to another. Most first person shooter games (FPS) use three keys located on the top left of your keyboard to move your character. French AZERTY keyboards will use ZQSD for this (Z = up/move forward, Q and D are for left/right and S is for down/move backward), while US keyboards will use WASD, for example. So keep in mind that keys are not located at the same place on keyboards from different countries.

Extract from the "[Internationalize your keyboard controls](https://hacks.mozilla.org/2017/03/internationalize-your-keyboard-controls/)" article on MDN:

  > "Recently I came across two lovely new graphical demos, and in both cases, the controls would not work on my French [AZERTY keyboard](https://en.wikipedia.org/wiki/AZERTY).

  > There was the wonderful WebGL 2 technological demo [After The Flood](https://www.youtube.com/watch?v=TT7ugKuUMv0/), and the very cute [Alpaca Peck](https://codepen.io/shshaw/full/apwMwM/). [Shaw](https://codepen.io/shshaw/#) was nice enough to fix the latter when I told him about the issue. It turns out the Web browser actually exposes a useful API for this."


#### One keyboard, many layouts

For details, see [Wikipedia’s keyboard layout page](https://en.wikipedia.org/wiki/Keyboard_layout)!

[QWERTY](https://en.wikipedia.org/wiki/QWERTY) layout, used in US, GB, etc. & [AZERTY](https://en.wikipedia.org/wiki/AZERTY) layout, used in some French-speaking countries

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2jwxzxt" ismap target="_blank">
    <img style="margin: 0.1em;" height=120
      src  ="https://tinyurl.com/y6muencp"
      alt  ="QWERTY keyboard layout"
      title="QWERTY keyboard layout"
    >
    <img style="margin: 0.1em;" height=120
      src  ="https://tinyurl.com/yyfmtdkw"
      alt  ="AZERTY keyboard layout"
      title="AZERTY keyboard layout"
    >
  </a>
</div>

In addition, [QWERTZ](https://en.wikipedia.org/wiki/QWERTZ) keyboards are in use in Germany and other European countries, and [DVORAK](https://en.wikipedia.org/wiki/Dvorak_keyboard_layout) is another alternative to QWERTY:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2jwxzxt" ismap target="_blank">
    <img style="margin: 0.1em;" height=120
      src  ="https://tinyurl.com/yyteudcy"
      alt  ="QWERTZ layout keyboard"
      title="QWERTZ layout keyboard"
    >
    <img style="margin: 0.1em;" height=120
      src  ="https://tinyurl.com/yyh46en3"
      alt  ="DVORAK layout keyboard"
      title="DVORAK layout keyboard"
    >
  </a>
</div>

Saudi Arabic keyboard layout (see more [Arabic keyboards](https://en.wikipedia.org/wiki/Arabic_alphabet#Keyboards)) & [Bangla National (Jatiyo) keyboard](https://en.wikipedia.org/wiki/Bengali_input_methods#Bangla_Jatiyo):

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2jwxzxt" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yyrz4ott"
      alt  ="Saoudian Arabic keyboard layout"
      title="Saoudian Arabic keyboard layout"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yykojsjl"
      alt  ="Bangladesh keyboard layout"
      title="Bangladesh keyboard layout"
    >
  </a>
</div>


#### Note for 2.4.6 Dealing with different keyboard layouts

+ Keyboard layouts
  + keyboard layout varying from one country to another
  + keys not located at the same place on keyboards from different countries
  + key events & properties
    + DOM API: `keyup`, `keydown` and `keypress`
    + `KeyCode` property of the DOM event


### 2.4.7 Key and code properties

`key` and `code` are new recommended properties you can use with modern browsers.

You may have noticed that in some examples from the previous course page about key events, we used `event.key` in order to display the character that has been typed. The `key` property has been introduced with a new W3C API called UI Events (or DOM level 3 events), that has been discussed since 2000.  All major browsers have implemented this very practical `key` property. It comes with another property named `code`, which is what `keyCode` should have been. The value of the code property corresponds to a code that is more readable than the value of the old `keyCode` property.

+ __`key`__: when the pressed key is a printable character, you get the character in string form. When the pressed key is not a printable character (for example: Backspace, Control, but also Enter or Tab which actually are printable characters), you get a multi-character descriptive string, like 'Backspace', 'Control', 'Enter', 'Tab'.
+ __`code`__: Gives you the physical key that was pressed, in string form. This means it’s totally independent of the keyboard layout that is being used. So let’s say the user presses the Q key on a QWERTY keyboard. __Then `event.code` gives you 'KeyQ' while `event.key` gives you 'q'.__

<span style="colr: brown; font-weight: bold;">But when an AZERTY keyboard user presses the A key, he also gets <code>'KeyQ'</code> as <code>event.code</code>, yet <code>event.key</code> contains 'a'. This happens because the A key on a AZERTY keyboard is at the same location as the Q key on a QWERTY keyboard.</span>

As for numbers, the top digit bar yields values like 'Digit1', while the numeric pad yields values like 'Numpad1'.

#### List of codes, the reference keyboard

There’s no existing keyboard with all the possible keys. That’s why the W3C published [a specification just for this](https://www.w3.org/TR/uievents-code/). You can read about the [existing mechanical layouts](https://www.w3.org/TR/uievents-code/#keyboard-layout) around the world, as well as their [reference keyboard](https://www.w3.org/TR/uievents-code/#code-value-tables). For instance here is their reference keyboard for the alphanumerical part:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/yyh6fm43')"
    src    ="https://tinyurl.com/y44haoho"
    alt    ="Reference alphanumeric keyboard"
    title  ="Reference alphanumeric keyboard"
  />
</figure>


Also, please read through [the examples given in the specification](https://w3c.github.io/uievents/#code-examples). They show very clearly what happens when the user presses various types of keys, both for code and key.

#### Example that displays the key and code values with your current keyboard

[CodePen Demo](https://codepen.io/w3devcampus/pen/GmYxNY)

[Local Demo](src/02d-example17.html)

I encourage you to take a look and get at least an overview of this specification.

Please note that the W3C has also published a sibling specification describing the values for the key property.


#### Current browser support

+ [CanIUse table for `key`](https://caniuse.com/#feat=keyboardevent-key)
+ [CanIUse table F-for `code`](https://caniuse.com/#feat=keyboardevent-code)


