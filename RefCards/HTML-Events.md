# HTML DOM Events

## Events

+ [DOM events](../WebDev/Frontend-W3C/2-HTML5Coding/04c-Animations.md#431-events-input-and-output)
  + use the DOM JavaScript API to create event handlers
  + JavaScript: events made by users as an input and manipulating the DOM structure as an output
  + games/animations:
    + input: change state variables of moving objects
    + output: animation loop taking care of these variables to move the objects
  + ways to manage events in the DOM structure
    + declare event handlers in the HTML code
      + e.g., <prep><div id="someDiv" <strong>onclick="alert('clicked!')</strong>;"></prep>
      + not the recommended way to handle events
      + mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) in one place
      + not the recommended way for full scale applications where a clean separation is the best
    + add an event handler to an HTML element in JavaScript
      + e.g., `document.getElementById('someDiv').onclick = function(evt) { alert('clicked!'); }`
      + unable to attach several listener functions
    + register a callback to the event listener with the `addEventListener` method
      + e.g., `document.getElementById('someDiv').addEventListener('click', function(evt) { alert('clicked!'); }, false);`
      + third parameter not important for now, just set it to false or ignore
  + DOM event and event listener function
    + create an EventListener and attach it to an element
    + an event object passed as a parameter to the callback
    + example:

      ```js
      element.addEventListener('click', function(event) {
        // now you can use the event object inside the callback
      }, false);
      ```

    + use different properties from the event object in order to get useful information

+ [Interaction w/ events](../WebDev/Frontend-W3C/5-JavaScript/01f-JSIntro.md#notes-for-165-adding-interactivity-with-events)
  + possible actions able to react to
    + user interactions (keyboard, mouse, gamepad)
    + changes in the lifecycle of document, e.g., pages loading or resizing, screen rotation on a mobile device
    + notified after compeltion of a long process; e.g. loading a large image or source track from the network

+ [Interactivity of Web application](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#24-handling-events)
  + CSS: limited w/ pseudo CSS class, e.g., `.hover`
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

+ [Interaction](../WebDev/Frontend-W3C/3-HTML5AppGame/02b-GameProg.md#notes-for-222-elements-and-apis-useful-for-writing-games)
  + user input replying on several APIs
  + DOM API used for keyboard, touch, or mouse inputs
  + GamePad API (working draft)
    + define a low-level interface representing gamepad devices
    + already implemented by some browsers



## Reference table

<table style="margin: 0 auto; border: 1px solid black; border-collapse: collapse; width: 70vw;" cellspacing=0 cellpadding=5 border=1 align="center">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#2410-reference-tables">Event Reference Table</a></caption>
  <thead>
  <tr style="border-bottom: double black;">
    <th style="width: 5%; font-size: 1.4em; border-right: double back; text-align: center; background-color: lightslategray; color: white;"> Type </th>
    <th style="width: 5%; font-size: 1.4em; border-right: double back; text-align: center; background-color: lightslategray; color: white;"> Name </th>
    <th style="width: 60%; text-align: center; font-size: 1.4em; background-color: lightslategray; color: white;"> Description </th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan=3 style="text-align: center; font-weight: bolder; line-height: 1.3; vertical-align: middle; font-size: 1.2em; background-color: lightgrey; color: gray;"> Event Object </td> </tr>
    <th rowspan=2 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;"> Common Properties </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> type </td>
    <td style="padding: 0.3em;"> Returns the name of the event </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> target </td>
    <td style="padding: 0.3em;"> Returns the element that triggered the event </td>
  </tr>
  <tr>
    <th rowspan=2 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;"> Common Methods </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> preventDefault() </td>
    <td style="padding: 0.3em;"> Cancels the event if it is cancelable, meaning that the default action that belongs to the event will not occur </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> stopPropagation() </td>
    <td style="padding: 0.3em;"> Prevents further propagation of an event during event flow </td>
  </tr>
  <tr>
    <td colspan=3 style="text-align: center; font-weight: bolder; line-height: 1.3; vertical-align: middle; font-size: 1.2em; background-color: lightgrey; color: gray;"> Page Lifecycle </td> </tr>
    <th rowspan=3 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;"> Events </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> load </td>
    <td style="padding: 0.3em;"> This event occurs when an object has loaded (including all its resources: images, etc.) This event is very useful when you want to run JS code and be sure that the DOM is ready (in other words, be sure that a <code>document.getElementById(...)</code> or <code>document.querySelector(...)</code> will not raise an error because the document has not been loaded and elements you are looking for are not ready. </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> resize </td>
    <td style="padding: 0.3em;"> The event occurs when the document view is resized. Usually we get the new size of the window inside the event listener using <code>var w = window.innerWidth;</code> and <code>var h = window.innerHeight;</code> </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> scroll </td>
    <td style="padding: 0.3em;"> The event occurs when an element's scrollbar is being scrolled. Usually, in the scroll event listener, we use things such as:<br> &nbsp;&nbsp;<code>&var max = document.body.scrollHeight - innerHeight;</code><br>&nbsp;&nbsp;<code>var percent = (pageYOffset / max);</code><br/>...to know the percentage of the scroll in the page. </td>
  </tr>
  <tr>
    <td colspan=3 style="text-align: center; font-weight: bolder; line-height: 1.3; vertical-align: middle; font-size: 1.2em; background-color: lightgrey; color: gray;"> Keyboard </td> </tr>
    <th rowspan=3 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;">  Events </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> keydown </td>
    <td style="padding: 0.3em;"> The event occurs when the user is pressing a key </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> keyup </td>
    <td style="padding: 0.3em;"> The event occurs when the user releases a key </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> keypress </td>
    <td style="padding: 0.3em;"> The event occurs when the user presses a key (up and release) </td>
  </tr>
  <tr>
    <th rowspan=4 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;"> Properties </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> keyCode </td>
    <td style="padding: 0.3em;"> Returns the Unicode character code of the key that triggered the onkeypress ,onkeydown or onkeyup event </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> shiftKey </td>
    <td style="padding: 0.3em;"> Returns whether the "shift" key was pressed when the key event was triggered </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> ctrlKey </td>
    <td style="padding: 0.3em;"> Returns whether the "ctrl" key was pressed when the key event was triggered </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> altKey </td>
    <td style="padding: 0.3em;"> Returns whether the "alt" key was pressed when the key event was triggered </td>
  </tr>
  <tr>
    <td colspan=3 style="text-align: center; font-weight: bolder; line-height: 1.3; vertical-align: middle; font-size: 1.2em; background-color: lightgrey; color: gray;"> Mouse </td> </tr>
    <th rowspan=9 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;">  Events </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> click </td>
    <td style="padding: 0.3em;"> The event occurs when the user clicks on an element (presses a button and releases it) </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> dblclick </td>
    <td style="padding: 0.3em;"> The event occurs when the user double-clicks on an element </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> mousedown </td>
    <td style="padding: 0.3em;"> The event occurs when the user presses a key (up and release) </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> mouseup </td>
    <td style="padding: 0.3em;"> The event occurs when a user releases a mouse button over an element </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> mousemove </td>
    <td style="padding: 0.3em;"> The event occurs when the pointer is moving while it is over an element </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> mouseenter </td>
    <td style="padding: 0.3em;"> The event occurs when the pointer is moved onto an element </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> mouseleave </td>
    <td style="padding: 0.3em;"> The event occurs when the pointer is moved out of an element </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> mouseover </td>
    <td style="padding: 0.3em;"> The event occurs when the pointer is moved onto an element, or onto one of its children </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> contextmenu </td>
    <td style="padding: 0.3em;"> The event occurs when the user right-clicks on an element to open a context menu </td>
  </tr>
  <tr>
    <th rowspan=6 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;">  Properties </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> button </td>
    <td style="padding: 0.3em;"> Returns which mouse button was pressed when the mouse event was triggered </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> clientX and clientY </td>
    <td style="padding: 0.3em;"> Returns the coordinates of the mouse pointer, relative to the element coordinate system that triggered the event </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> pageX and pageY </td>
    <td style="padding: 0.3em;"> Returns the coordinates of the mouse pointer, relative to the document, when the mouse event was triggered </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> screenX and screenY </td>
    <td style="padding: 0.3em;"> Returns the coordinates of the mouse pointer, relative to the screen, when an event was triggered </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> altKey, ctrlKey, shiftKey </td>
    <td style="padding: 0.3em;"> Returns whether the "alt, ctrl and shift" key was pressed when an event was triggered </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> detail </td>
    <td style="padding: 0.3em;"> Returns a number that indicates how many times the mouse was clicked </td>
  </tr>
  <tr>
    <td colspan=3 style="text-align: center; font-weight: bolder; line-height: 1.3; vertical-align: middle; font-size: 1.2em; background-color: lightgrey; color: gray;"> Forms </td> </tr>
    <th rowspan=6 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;">  Events </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> input </td>
    <td style="padding: 0.3em;"> The event occurs when an element gets user input (e.g., a key is typed on an input field, a slider is moved, etc.) </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> change </td>
    <td style="padding: 0.3em;"> The event occurs when the content of a form element, the selection, or the checked state have changed (for &lt;input&gt;, &lt;select&gt;, and &lt;textarea&gt;). A change event listener on a slider will generate an event when the drag/move ended, while input events will be useful to do something as the slider is being moved. </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> focus </td>
    <td style="padding: 0.3em;"> The event occurs when an element gets focus (e.g., the user clicks in an input field) </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> blur </td>
    <td style="padding: 0.3em;"> The event occurs when an element loses focus (e.g., the user clicks on another element) </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> select </td>
    <td style="padding: 0.3em;"> The event occurs after the user selects some text (for &lt;input&gt; and &lt;textarea&gt;) </td>
  </tr>
  <tr>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> submit </td>
    <td style="padding: 0.3em;"> The event occurs after the user selects some text (for &lt;input&gt; and &lt;textarea&gt;) </td>
  </tr>
  <tr>
    <th rowspan=1 style="padding: 0.3em; text-align: left; line-height: 1.5; vertical-align: middle; font-weight: bold;">  Property </th>
    <td style="padding: 0.3em; font-weight: bold; color: brown;"> value </td>
    <td style="padding: 0.3em;"> The content of the different input fields </td>
  </tr>
  </tbody>
</table>



## Event Listening

+ [Event listerners](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#242-adding-and-removing-event-listeners)
  + `addEventListener` function
    + one possible syntax for registering as function to be called when a given type of event occurs
    + syntax: `addEventListener(typeOfEvent, callbackFunction)`
    + able to register more than one event listener
    + scope
      + listening to event on the whole document: `addEventListener` = `window.addEventListener`
      + listening to specific DOM elements
        + get a reference of the HTML to detect the event; e.g., `var b = document.querySelector("#myButton");`
        + call the `addEventListener` method on the object; e.g., `b.addEventListener('click', callback);`
    + ensuring the existence before selecting an element w/ `querySelector`
    + every DOM object w/ an `addEventListener` method starting listening to event on it, once getting a reference of any HTML element from JS

  + [`on` attribute](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#242-adding-and-removing-event-listeners)
    + adding an event listener to an HTML tag of an element directly
    + syntax in HTML: `onclick='doSomething();`
    + limited to a single event listener to click on this button
  + big project
    + better to separate the HTML, CSS and JS code
    + recommended putting all event listener definitions in a separate JS file
    + using `addEventListener` syntax in preference to the "on" attribute syntax
  + removing event listener
    + removing previous registered event listener
    + syntax: `removeEventListener(TypeOfEvent, callBackFunction)`
    + must pass `callBackFunction` used in `addEventListener` to remove

+ [Ways to provide callback function](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#242-adding-and-removing-event-listeners)
  + standard function block
  + function expression: common practice w/ small function


## Event Object

+ [Event object](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#243-the-event-object)
  + DOM event object
    + the only parameter passed to event listener
    + containing various properties and methods
  + common properties and methods
    + `evt.type`: the name of the event
    + `evt.target`: the HTML element fired the event, e.g., `evt.target` = button as the click listeners on the button
    + `evt.stopPropagation()`:
      + several elements registered for an event
      + not propagating the event to all other elements that listen to it
    + `evt.preventDefault()`:
      + default browser behavior not executed
      + example: `contextmenu` event listener attached to an object for user's own contextmenu
  + typical specific properties associated w/ the type of the event
    + `evt.button`: mouse button used in case of a mouse event listener
    + `evt.keyCode`: code of the key been used
    + `evt.pageX`: coordinate of the mouse relative to the page

+[Most useful common properties and methods](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#243-the-event-object)
  + properties
    + `type`: returning the name of the event
    + `target`: returning the element triggering the event
  + methods
    + `preventDefault()`:
      + cancelling the cancelable event
      + the default action belonging to the event not occuring
      + useful for cancelling the default browser behavior
    + `stopPropagation()`: preventing further propagation of an event flow




## Page Lifecycle

+ [Page lifecycle events](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#244-page-lifecycle-events)
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




## Keyboard events

+ [Key events](../WebDev/Frontend-W3C/2-HTML5Coding/04c-Animations.md#432-keyboard-interaction-key-events)
  + syntax: `target.addEventListener(type, listener [, options]);`
    + `type`: case-sensitive string representing the [event type](https://developer.mozilla.org/en-US/docs/Web/Events) to listen for
    + `listener`: an object implementing the [EventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventListener) interface, or a JavaScript [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
    + options:
      + `capture`: a Boolean indicating that events of this type will be dispatched to the registered listener before being dispatched to any EventTarget beneath it in the DOM tree
      + `once`: a Boolean indicating that the listener should be invoked at most once after being added
      + `passive`:
        + true: the function specified by listener will never call `preventDefault()`
        + false: call `preventDefault()` and the user agent will do nothing other than generate a console warning
  + keyboard related events: `keydown`, `keyup` or `keypressed`
  + event parameter passed to the listener function containing the code of the key that fired the event
  + test what key has been pressed or released

    ```js
    window.addEventListener('keydown', function(event) {
      if (event.keyCode === 37) {
        //left arrow was pressed
      }
    }, false);
    ```

  + tools:
    + [KeyboardEvent Value](https://css-tricks.com/snippets/javascript/javascript-keycodes/#tester-tool)
    + [key codes interactive test page](http://www.asquare.net/javascript/tests/KeyCode.html)
  + keydown listener: `window.addEventListener('keydown', handleKeydown, false);`
  + keyup listener: `window.addEventListener('keyup', handleKeyup, false);`
  + capture key evens only in canvas:
    + `tabindex` attribute of the canvas element makes it focusable. e.g., <prep><canvas id="myCanvas" width="350" <strong>tabindex="1"</strong> height="200"></prep>
    + specify the canvas focusable: `canvas.focus();`
  + interact only mouse hoover on canvas
    + set the focus when the mouse is over the canvas
    + two mouse event listeners on the canvas: `mouseenter` event and `mouseout` event
    + the mouse entering the canvas call `canvas.focus()` to set the focus to the canvas
    + the mouse cursor out of the canvas, call `canvas.blur()` to unset the focus
    + event handlers: 
      + key events: `canvas.addEventListener('keydown', handleKeydown, false); canvas.addEventListener('keyup', handleKeyup, false);`
      + mouse event: `canvas.addEventListener('mouseenter', setFocus, false); canvas.addEventListener('mouseout', unsetFocus, false);`


+ [Key events](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#245-key-events)
  + related events: `keydown`, `keyup` and `keypress`
  + event parameter passed to the listener function containing the code of the key that fired the event

  + key code w/ keyboard keys
    + [JavaScript Event KeyCode Test Page](http://www.asquare.net/javascript/tests/KeyCode.html)
    + [list of keycode values](https://css-tricks.com/snippets/javascript/javascript-keycodes/#keycode-values)
  + key events
    + `keydown`: pressing a key
    + `keyup`: releasing a key
    + `keypress` (deprecated): pressing a key or up and release
  + keyboardEvent properties
    + legacy properties still used by many JS code
    + not recommended for modern browser
    + `keyCode`
      + more powerful/easy to use
      + return the Unicode character code of the key
      + triggering the onkeypress, onkeydown or onkeyup event
    + `shiftKey`: return whether the "shift" key pressed when the key event triggered
    + `ctrlKey`: return whether the "ctrl" key pressed when the key event triggered
    + `altKey`: return whether the "alt" key pressed when the key event triggered

+ [Keyboard layouts](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#246-dealing-with-different-keyboard-layouts)
  + keyboard layout varying from one country to another
  + keys not located at the same place on keyboards from different countries
  + key events & properties
    + DOM API: `keyup`, `keydown` and `keypress`
    + `KeyCode` property of the DOM event


## Keycode / key / code properties

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 50vw;" cellspacing="0" cellpadding="5" border="1">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/y333tfjx">KeyCode Values from from event.which</a></caption>
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Key</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Code</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Key</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Code</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Key</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Code</th>
  </tr>
<tbody>
<tr> <td>backspace</td><td>8</td> <td>tab</td><td>9</td> <td>enter</td><td>13</td> </tr>
<tr> <td>shift</td><td>16</td> <td>ctrl</td><td>17</td> <td>alt</td><td>18</td> </tr>
<tr> <td>pause/break</td><td>19</td> <td>caps lock</td><td>20</td> <td>escape</td><td>27</td> </tr>
<tr> <td>(space)</td><td>32</td> <td>page up</td><td>33</td> <td>page down</td><td>34</td> </tr>
<tr> <td>end</td><td>35</td> <td>home</td><td>36</td> <td>left arrow</td><td>37</td> </tr>
<tr> <td>up arrow</td><td>38</td> <td>right arrow</td><td>39</td> <td>down arrow</td><td>40</td> </tr>
<tr> <td>insert</td><td>45</td> <td>delete</td><td>46</td> <td>0</td><td>48</td> </tr>
<tr> <td>1</td><td>49</td> <td>2</td><td>50</td> <td>3</td><td>51</td> </tr>
<tr> <td>4</td><td>52</td> <td>5</td><td>53</td> <td>6</td><td>54</td> </tr>
<tr> <td>7</td><td>55</td> <td> 8</td><td>56</td> <td>9</td><td>57</td> </tr>
<tr> <td>a</td><td>65</td> <td>b</td><td>66</td> <td>c</td><td>67</td> </tr>
<tr> <td>d</td><td>68</td> <td>e</td><td>69</td> <td>f</td><td>70</td> </tr>
<tr> <td>g</td><td>71</td> <td>h</td><td>72</td> <td>i</td><td>73</td> </tr>
<tr> <td>j</td><td>74</td> <td>k</td><td>75</td> <td>l</td><td>76</td> </tr>
<tr> <td>m</td><td>77</td> <td>n</td><td>78</td> <td>o</td><td>79</td> </tr>
<tr> <td>p</td><td>80</td> <td>q</td><td>81</td> <td>r</td><td>82</td> </tr>
<tr> <td>s</td><td>83</td> <td>t</td><td>84</td> <td>t</td><td>84</td> </tr>
<tr> <td>v</td><td>86</td> <td>w</td><td>87</td> <td>x</td><td>88</td> </tr>
<tr> <td>y</td><td>89</td> <td>z</td><td>90</td> <td>left window key</td><td>91</td> </tr>
<tr> <td>right window key</td><td>92</td> <td>select key</td><td>93</td> <td>numpad 0</td><td>96</td> </tr>
<tr> <td>numpad 1</td><td>97</td> <td>numpad 2</td><td>98</td> <td>numpad 3</td><td>99</td> </tr>
<tr> <td>numpad 4</td><td>100</td> <td>numpad 5</td><td>101</td> <td>numpad 6</td><td>102</td> </tr>
<tr> <td>numpad 7</td><td>103</td> <td>numpad 8</td><td>104</td> <td>numpad 9</td><td>105</td> </tr>
<tr> <td>multiply</td><td>106</td> <td>add</td><td>107</td> <td>subtract</td><td>109</td> </tr>
<tr> <td>decimal point</td><td>110</td> <td>divide</td><td>111</td> <td>f1</td><td>112</td> </tr>
<tr> <td>f2</td><td>113</td> <td>f3</td><td>114</td> <td>f4</td><td>115</td> </tr>
<tr> <td>f5</td><td>116</td> <td>f6</td><td>117</td> <td>f7</td><td>118</td> </tr>
<tr> <td>f8</td><td>119</td> <td>f9</td><td>120</td> <td>f10</td><td>121</td> </tr>
<tr> <td>f11</td><td>122</td> <td>f12</td><td>123</td> <td>num lock</td><td>144</td> </tr>
<tr> <td>scroll lock</td><td>145</td> <td>semi-colon</td><td>186</td> <td>equal sign</td><td>187</td> </tr>
<tr> <td>comma</td><td>188</td> <td>dash</td><td>189</td> <td>period</td><td>190</td> </tr>
<tr> <td>forward slash</td><td>191</td> <td>grave accent</td><td>192</td> <td>open bracket</td><td>219</td> </tr>
<tr> <td>back slash</td><td>220</td> <td>close braket</td><td>221</td> <td>single quote</td><td>222</td> </tr>
</tbody>
</table>

+ [`key` and `code` properties](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#247-key-and-code-properties)
  + new recommended properties w/ modern browsers
  + UI Events / DOM level 3 events: a new W3C API
  + both introduced w/ UI Events
  + `key` property
    + a character in string form as the pressed key w/ a printable character
    + a multi-character descriptive string as the pressed key not a printable character, e.g., 'Backspace', 'Control', 'Enter', 'Tab'
    + all major browsers implemented
  + `code` property
    + the physical key pressed in string form
    + totally independent of the keyboard layout
  + example: pressing 'Q' key on a QWERTY keyboard
    + `evt.code` value: `KeyQ`
    + `evt.key` value: `q`
  + example: pressing `A` key on a AZERTY keyboard
    + `evt.code` value: `KeyQ`
    + `evt.key` value: `a`
  + `code` property of number keys
    + top digit bar: 'Digit#', eg, `Digit1'
    + numeric pad: 'Numpad#', eg, 'Numpad1'
  + list of code
    + [specification of UI Events KeyboardEvent code values](https://www.w3.org/TR/uievents-code/)
    + [reference alphanumeric keyboard](https://www.w3.org/TR/uievents-code/#keyboard-key-codes)

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
        onclick="window.open('https://www.w3.org/TR/uievents-code/#key-alphanumeric-writing-system')"
        src    ="https://www.w3.org/TR/uievents-code/images/keyboard-codes-alphanum1.svg"
        alt    ="Reference alphanumeric keyboard"
        title  ="Reference alphanumeric keyboard"
      />
    </figure>


## Mouse events

+ [Mouse events](../WebDev/Frontend-W3C/2-HTML5Coding/04c-Animations.md#433-mouse-interaction-mouse-events)
  + event received by the listener function used for getting the button number or the coordinates of the mouse cursor
  + list of mouse events
    + `mouseleave`: fired when the mouse leaves the surface of the element
    + `mouseover`: mouse cursor moving over the element that listens to that event
    + `mousedown`: fired when a mouse button pressed
    + `mouseup`: fired when a mouse button is released
    + `mouseclick`: fired after a `mousedown` and a `mouseup` occurred
    + `mousemove`:
      + fired while the mouse moves over the element
      + each time the mouse moves, a new event is fired
      + only one event is fired
  + `mouseleave` vs. `mouseout`:
    + `mouseleave` not fired when the cursor moves over descendant elements
    + `mouseout` fired when the element moved outside of the bounds of the original element or a child of the original element
  + `mouseenter` vs. `mouseover`:
    + `mouseover` event occurs on an element when you are over it - coming from either its child OR parent element
    + `mouseenter` event only occurs when the mouse moves from the parent element to the child element
  + tricky part: accurately getting the mouse position relative to the canvas
    + the event object ("DOM event") passed to the listener function
    + properties corresponding to the mouse coordinates: `clientX` and `clientY`
    + window coordinates: not relative to the canvas itself, but relative to the window (the page)
    + requirement: convert the coordinates between the window and the canvas
    + considering the position of the canvas, and the CSS properties that may affect the canvas position (margin, etc.)
    + `getBoundingClientRect()` method: get the position and size of any element in the page
    + example: mouse position w/ canvas coordinates

      ```js
      function getMousePos(canvas, evt) {
        // necessary to take into account CSS boundaries
        var rect = canvas.getBoundingClientRect();
        return {
            x: evt.clientX - rect.left,
            y: evt.clientY - rect.top
        };
      }
      ```

  + [mouse positions w/ button pressed and released](../WebDev/Frontend-W3C/2-HTML5Coding/04c-Animations.md#how-to-display-the-mouse-position-and-the-mouse-button-that-has-been-pressed-or-released)

    ```js
    canvas.addEventListener('mousemove', function (evt) {
        mousePos = getMousePos(canvas, evt);
        var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;
        writeMessage(canvas, message);
    }, false);

    canvas.addEventListener('mousedown', function (evt) {
        mouseButton = evt.button;
        var message = "Mouse button " + evt.button + " down at position: " + mousePos.x + ',' + mousePos.y;
        writeMessage(canvas, message);
    }, false);

    canvas.addEventListener('mouseup', function (evt) {
        var message = "Mouse up at position: " + mousePos.x + ',' + mousePos.y;
        writeMessage(canvas, message);
    }, false);
    ```

  + example: move character w/ mouse and rotate w/ button pressed
  + example: move mouse as pencil to draw in canvas
  + example: draw only when mouse button pressed

+ [Mouse events and properties](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#notes-for-248-mouse-events)
  + events
    + `click`: occurred when the user clicks on an element (press and release)
    + `dblclick`: occurred when the user double-clicks on an element
    + `mousedown`: occurred when the user presses a mouse button
    + `mouseup`: occurred when the user releases a mouse button
    + `mouseenter`: occurred when the pointer is moved onto an element
    + `mouseleave`: occurred when the pointer is moved out of an element
    + `mouseover`: occurred when the pointer is moved onto an element, or onto one of its children
    + `contextmenu`: occurred when the user right-clicks on an element to open a context menu
  + properties
    + `button`: which buttom pressed when the mouse event is triggered
    + `clientX` and `clientY`
      + the coordinates of the mouse pointer
      + relative to the element coordinate system
        + left-top corner: always (0, 0) independent of scroll position
        + coordinates relative to the VIEWPORT (the visualable part of the document page)
      + values changed when page scrolls down and mouse not moved
    + `pageX` and `pageY`
      + the coordinates of the mouse pointer
      + relative to the complete document/page
      + always relative to the very beginning of the document/page, even if the top of the page not visible
    + `screenX` and `screenY`: the coordinates of the mouse pointer, relative to the screen
    + `altKey`, `ctrlKey` and `shiftKey`: whether the "alt", "ctrl" and "shift" pressed
    + `detail`: a number that indicates how many times the mouse clicked
  + event received by the listener used for getting the button number or the coordinates of the mouse cursor
  + example: [listening to `mouseup` and `mousedown` events](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example18.html)
  + example: [mouse position related to an element](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example19.html)
  + example: [click and drag](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example23.html)
  + example: [right-click context menu](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example24.html)




## Form and Input Field Events

+ [Form and input field events](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#249-form-and-input-field-events)
  + form related events
    + `input`: occurred when an element gets user input, e.g., a key is typed on an input field, a slider is moved, etc.
    + `change`
      + occurred when the content of a form element, the selection or the checked state have changed
      + for `<input>`, `<select>` and `<textarea>`
      + change event on a slider: generating an event when drag/move ends
      + input event: useful to do something as the slider is being moved
    + `focus`: occurred when an element gets focus, e.g., the user clicks in an input field
    + `blur`: occurred when an element loses focus, e.g., the user clicks on another element
    + `select`: occurred after the user selects some text (for `<input>` and `<textarea>`)
    + `submit`: occurred when a form is submitted
  + FormEvent properties
    + no particular properties required to be mentioned
    + using `value` property of a form event listener to check the content of the different input fields
  + examples
    + [validating the user input w/ `input` event](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example25.html)
    + [validating the user typed key w/ `keyup` event](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example26.html)
    + [action for moving slider w/ `input` event](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example27.html)
    + [detect number change w/ `input` event](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example28.html)
    + [choose a color w/ `change` event](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example29.html)


 ## JavaScript form validation API

+ [Javascript form validation](../WebDev/Frontend-W3C/2-HTML5Coding/05g-HTMLForms.md#573-javascript-form-validation-api)
  + allowing developers to use their own validation algorithm and customize error messages
  + together w/ some HTML/CSS/JavaScript to make own message bubbles
  + example: password checking

+ [validity property](#574-the-validity-property-of-input-fields)
  + error details when the field is invalid
  + test the different types of validation error
  + typical usage: `var validityState_object = input.validity;`
  + possible values
    + `valueMissing`
    + `typeMismatch`
    + `patternMismatch`
    + `tooLong`
    + `rangeUnderflow`
    + `rangeOverflow`
    + `stepMismatch`
    + `valid`
    + `customError`

+ [validationMessage property](../WebDev/Frontend-W3C/2-HTML5Coding/05g-HTMLForms.md#the-validationmessage-property)
  + the validation error messag
  + useful for making custom error messages
  + typical usage: `console.log("Validation message = " + input.validationMessage);`




## Responsive canvas

+ [Responsive canvas](../WebDev/Frontend-W3C/2-HTML5Coding/04c-Animations.md#434-responsive-canvas)
  + rules of resizing a canvas
    + changing `width` and `height` property $\to$ erase the content and reset the context
    + using `%` in the CSS `width` and `height` properties of a canvas $\to$ scaling the existing pixels w/o erasing the content, given a blurry image
  + __best practice__: never use CSS percentage on a canvas width or height
  + responsive canvas
    + embedded in a `<div>` or in any parent container
    + using CSS w/ percentages on the width and the height CSS properties of the parent
    + using a `resize` listener on the parent of the canvas
    + changing the `weight` and `height` properties of the canvas from the JS resize listener function
    + redraw content, scaled accordingly to the size of the parent
  + example: resize canvas
    + HTML code: `<div id="parentDiv"> <canvas id="myCanvas" width="100" height="100" ></canvas> </div>`
    + CSS code for `<div>` resize: `#parentDiv { width:100%; height:50%; margin-right: 10px; border: 1px solid red; }`
    + unable to listen to a DIV's resize by listening to the window instead: `window.addEventListener('resize',     resizeCanvasAccordingToParentSize, false);`
    + adjust canvas size, take parent's size, this erases content: `canvas.width = divcanvas.clientWidth; canvas.height = divcanvas.clientHeight;`
    + resize character w/ `ctx.resize()` in draw function: `function drawMonster(x, y, angle, headColor, eyeColor) {...}`
      + save and restore at beginning and end of function
      + move the coordinate system to draw the character at position (x, y): `ctx.translate(x, y); ctx.rotate(angle);`
      + adjust the scale of the character if canvas too small to fit the character: 

        ```js
        if(canvas.width < 200) {
            var scaleX = canvas.width/200;
            var scaleY = scaleX;
        }
        ctx.scale(scaleX, scaleY);
        ``






#$# Event Management

+ [Event management in JS](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#2410-reference-tables)
  + no input or output in JS
  + treating events caused by user actions as input
  + manipulating DOM structure as output
  + DOM events:
    + retaining variable info, including the key stroke, the mouse button clicks, and the mouse position
    + the variables referred to determine what action to perform
  + __event handler__ created by the DOM APIs
  + ways to manage events 
    + declaring an event handler in the HTNL code
      + syntax: `<div id="someDiv" onclick="alert('clicked!')"> content of the div </div>`
      + easy to use but not recommended
      + probably duplicated
      + mixing 'visual layer' (HTML) and 'logical layer' (JS) $\to$ a host problems during development
    + attaching an event handler to an HTML element in JS
      + syntax: `document.getElementById('someDiv').onclick = function() { alert('clicked!'); }`
      + unable to attach multiple listener fucntions
    + registering a callback to the event listener w/ the `addEventListener` method
      + syntax: `document.getElementById('someDiv').addEventListener('click', function() { alert('clicked!'); }, false);`
      + 3rd parameter: whether the _callback_ to be called during the captured phase, default as false
  + passing DOM event to the event listener function
    + creating an event listener and attached to an element $\to$ creating an `event` object to describe what happen
    + event object as a parameter of the __callback fucntion__
    + callback function: `element.addEventListener('click', function(event) { // able to use event object inside the callback }, false);`
    + obtaining useful info from the `event` object w/ its properties




