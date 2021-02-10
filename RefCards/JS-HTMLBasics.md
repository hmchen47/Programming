# JavaScript Basic HTML APIs


## Events

### Overview of Events

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


### Reference table

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



### Event Listening

+ [Event listerners](../WebDev/Frontend-W3C/5-JavaScript/02d-Interact.md#242-adding-and-removing-event-listeners)
  + `addEventListener` function
    + one possible syntax for registering as function to be called when a given type of event occurs
    + syntax: `addEventListener(typeOfEvent, callbackFunction)`
    + able to register more than one event listener
    + procedure
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


### Event Object

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


### Page Lifecycle

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


### Key Events

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



### Mouse Events

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



### Form and Input Field Events

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



## The DOM API


### Overview of the DOM API

+ [Overview of DOM](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#251-introducing-the-dom)
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


### Accessing HTML Elements

+ [The `selector` API](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#253-accessing-html-elements)
  + a way of easily accessing elements in the DOM
  + a way to use CSS selector for requesting the DOM
  + methdos
    + `querySelector`: return the 1st element int he DOM that matched the selector
    + `querySelectorAll`: return a collection of HTML elements of all elements matching the selector
  + example: [typical usage](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example02.html)
    + HTML: `<img src="https://i.imgur.com/Ntvj5rq.png" id="img1" width=200> <img src="https://i.imgur.com/yiU59oi.gif" width=200>`
    + JavaScript
      + initialization: `window.onload = init;`
      + `init` function executed as soon as the page loaded (DOM ready)
  + example: [get all `<li>` directly in a `<ul>` of class nav](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example03.html)
  + example: [display all checked `<input type="checkbox">` elements](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example04.html)
  + example: [change the back ground of all paragraphs](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example04.html)
  + examples: more complex selectors
    + `var el = document.querySelector('#nav ul li');`: all elements `li` in `ul` elements in an element of `id`= `nav`
    + `var els = document.querySelectorAll('ul li:nth-child(even)');`: all li in a ul, but only even elements
    + `var els = document.querySelectorAll('form.test > tr > td');`: all `td` directly in `tr` in a form of class test
    + `querySelectorAll("p.warning, p.error");`: all paragraphs of class warning or error
    + `querySelector("#foo, #bar");`: first element of `id` = `foo` or `id` = `bar`
    + `var div = document.getElementById("bar"); var p = div.querySelector("p");`: first `p` in a `div`

+ [The `getElement` APIs](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#253-accessing-html-elements)
  + able to be replaced by `querySelector` and `querySelectorAll` methods
  + `document.getElementById(identifier)` method
    + return the element which has the `id` “identifier”.
    + equivalent to `document.querySelector("#identifier');`
  + `document.getElementsByTagName(tagName)` method
    + return a list of elements which are named “tagName”.
    + equivalent to `document.querySelectorAll(tagName);`
  + `document.getElementsByClassName(className)` method
    + return a list of elements which have the class “className”.
    + equivalent to `document.querySelectorAll('.className');`


### Changing Styles and Attributes

+ [The `style` attribute](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#254-changing-the-style-of-selected-html-elements)
  + most common way to modify the CSS style of one of several elements
  + typical usage: `var p = document.querySelector('#paragraph1'); p.style.color = 'red';`
  + rule to change syntax of attribute in JS
    + remove the "-" sign in CSS attributes if presented
    + capitalize the word after the "-" sign
  + most useful CSS properties
    + `color`: changing the color of the text content of selected element(s)
    + `background-color`: the background color of the select element(s)
    + `margin` and `padding`: external and internal space, including `margin-top`, `margin-left`, `margin-bottom`, and `margin-right` and also `padding-top`, etc.
    + `border` and `border-radius`: chnage the border, type, color, thickness, rounded corners, etc.
    + `box-shadow`: add shadow to selected elements
    + `font` and `font-style`: font characters and style (italic, bold, plain)
    + `text-align`: text alignment

+ [The `ClassList` interface](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#254-changing-the-style-of-selected-html-elements)
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
  + example: [add and remove multiple CSS properties](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example07.html)


### Manipulating HTMl Elements

+ [Value of a selected DOM node](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#255-modifying-selected-html-elements)
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
  + modifying the attributes:
    + directly using the name of attribute as the property
    + `value` property of objects in many cases

+ [Adding new node w/ the DOM API](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#256-adding-new-elements-to-the-dom)
  + create a new element by calling `createElement()` method
    + syntax: `var elm = document.createElement(name_of_the_element)`
    + example: `var li = document.createElement('li');`
  + set some attributes / values / styles for this element, e.g.,
    + `li.innerHTML = '<b>This is a new list item in bold!</b>';` & `li.textContent = 'Another new list item';`
    + `li.style.color = 'green';`
    + `img.src = "https://..../myImage.jpg";` & `img.width = 200;`
  + add the newly created element to another element in the DOM
    + using `append()`, `appendChild()`, `insertBefore()` or the `innerHTML` property

+ [Moving HTML elements](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#257-moving-html-elements-in-the-dom)
  + `append()`, `appendChild()`: adding a new element to an existing one
  + moving from its original location to become a child of the targetElem
  + example: [drag'n'drop](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example13.html)

+ [Removing elements](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#258-removing-elements-from-the-dom)
  + `removeChild()`: remove a chile element from the DOM document
  + removing all children of an element using the `innerHTML` property




## Web Storage APIs

### Web Storage API

+ [Web Storage API](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#621-the-web-storage-api)
  + similar to HTTP session cookies
  + two related mechanisms for storing structured data on the client side
    + `sessionStorage`:
      + erased when the tab/browser closed
      + tab specific and scoped to the lifetime of the tab
      + useful for storing small amounts of session specific information
      + used with caution: synchronous and blocking the main thread
      + limited to about 5MB and containing only strings
      + not accessible from web workers or service workers
      + data never transferred to the server
      + storage limit larger than a cookie
    + `localStorage`:
      + data remained until deleted
      + avoided due to synchronous to block the main thread
      + limited to about 5MB and containing only strings
      + not accessible from web workers or service workers
      + stored data w/o expiration date
      + get cleared only through JavaScript, or clearing the Browser cache / Locally Stored Data
      + storage limit: the maximum among the three
  + main difference: data longevity
  + key-value store for `localStorage`
    + a simple key-value store
    + the keys and values: strings
    + only one store per domain
    + same applied to `sessionStorage` 
    + functionality exposed through the globally available `localStorage` object
  + [example: save & restore form contents on the fly](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#622-example-1)

+ [Example for local storage API](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#example-that-shows-all-the-methods-of-the-local-storage-api-in-action)
  + HTML button to activate the JS function: `<button onclick="resetStore()">reset store (erase all key/value pairs)</button>`
  + retrieve all data: `function getCountValue() { document.querySelector("#counter").innerHTML = localStorage.count; }`
  + view all stored data
  + reset all stored data: `function resetStore() { localStorage.clear(); document.querySelector('#list').innerHTML=""; }`
  + add/remove some data to local storage

+ [Example to save/restore states](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#624-example-2)
  + save initial preferences
  + load preferences



### Cookie

+ [Cookies & Web Storage](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#differences-with-cookies)
  + main difference: size limit
  + cookie:
    + a popular way to store key-value pairs
    + cookies limited to a few KBytes
    + generate additional HTTP request traffic: request a Web page, an image, a stylesheet, a JavaScript file, etc.
    + not used for storage
    + sent with every HTTP request
    + storing anything more than a small amount of data
    + significantly increasing the size of every web request
    + limited to only strings
  + Web Storage: a more powerful technique than cookies
    + Web Storage extended to several MBytes
    + objects managed no longer carried on the network and HTTP
    + easily accessible (read, change and delete) from JavaScript
    + using the Web Storage API

+ [sessionStorage key/values vs cookies](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#sessionstorage-keyvalues-instead-of-cookies)
  + store session-based data in a manner more powerful than cookies
  + `sessionStorage` object working in exactly the same way as `localStorage`
  + lifetime limited to a single browser session (lifetime of your tab/window)
  + `sessionStorage` advantage: being scoped to a given browser tab (or similar execution context)
  + Cookies' security drawback
    + two tabs open to the same site $\to$ share the same cookies
    + storing information about a given operation using cookies in one tab
    + probably leaking the information to the other side
    + confusing if performing different tasks in each
  + `sessionStorage` data scoped and not leak across tabs


### Set & Get Web Storage

+ [getItem and setItem methods](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#gettingsetting-values-using-the-getitemkey-and-setitemkey-value-methods)
  + using `var value = getItem(key)` to retrieve a key's value and `setItem(key, value)` to set it
  + a counter counting the number of times a given user loaded the application
  + spaces acceptable: `localStorage.setItem("Instructor's name", "Michel");` and `var name = localStorage.getItem("Instructor's name");`
  + not acceptable: `var name = localStorage.Instructor's name; will not work!`
  + syntax to set/get `localStorage` values within loop or iterator


### Delete & Reset Web Storage

+ [removeItem and clear methods](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#deleting-a-key-with-removeitemkey-or-all-keys-with-clear)
  + `removeItem(key)`: delete a key
  + `localStorage.clear()`:
    + reset the entire store
    + rare occasion to clear the entire store by the user in production software
    + a common operation needed during development
      + bugs may store faulty data the persistence of which can break your application
      + the way to store data may evolve over time
      + test the experience of the user when first using the application
  + one way of reseting the entire store
    + add a user interface button that calls `clear()` when clicked
    + remember to remove it when you ship
  + recommended approach: simply open the dev. tool's console and type `localStorage.clear()`

+ [Example for generic functions](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#625-example-3)
  + calling `init()` function when the page loaded
  + adding input listeners:
    + taking an input field as parameter and attaching an `oninput` listener to it
    + saving the field's content each time a value entered
  + restore the last saved value for each input field, if present.
    + get the list of input fields: `document.querySelectorAll("input");`
    + iterate through the list: `for(var i= 0; i < listOfInputsInForm.length; i++) {...}`
    + get `id` of input fields as the key in `localStorage` for the previous data saved for this field: `var fieldToRestore = listOfInputsInForm[i]; var id = fieldToRestore.id;`
    + restore by setting the value of the input field if not undefined: `if(savedValue !== undefined) { fieldToRestore.value = savedValue; }`


### Size of Web Storage

+ [Size of Web storage](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#626-size-limitations-etc)
  + related mechanism w/ user agents (browsers) according to Web storage specification
    + limiting the total amount of space allowed for storage areas
    + allowing the user to grant more space to a site, when reaching quotas
    + allowing users to see how much space each domain is using
    + giving at least 5Mb per origin
  + local storage required for saving/loading data on demand in many cases
  + more complex solutions:
    + processing transaction: require more available space than local storage
    + e.g., IndexedDB, a No SQL database
  + limit amount of data to prevent from storing anything anything huge
  + storage not necessarily permanent
  + serious applications
    + synchronizing existing data with the server on a regular basis
    + avoid data loss when using the same service from multiple devices at once


### JavaScript Object Notation (JSON)

+ [JSON to structure key-value pairs](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#626-size-limitations-etc)
  + `JSON.stringify()` and `JSON.parse() methods`: manipulate minimal record format to store complex data
  + JSON (JavaScript Object Notation)
    + a lightweight data-interchange format
    + easy for machines to parse and generate.
    + a text format completely programming language independent
    + providing a great way of encoding and decoding data
    + a really good match for JavaScript
    + careful not to use circular data structures or non-serializable objects
    + straightforward plugging yo support local store in vast majority of cases
    + two structures:
      + a collection of name/value pairs
      + an ordered list of values
  + typical usage:
    + `locaStorage.key = JSON.stringify(object);`
    + `localStorage.setItem(key, JSON.stringify(object));`
  + example:
    + store the object as a JSON String: `localStorage.setItem('testObject', JSON.stringify(personObject));`
    + retrieve the object from storage: `retrievedObject = JSON.parse(localStorage.getItem('testObject'));`



## File APIs


### File APIs

+ [Interface of HTML5 File API specification](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#634-blob-and-file) 
  + __FileList__ interface: the files property
  + __File__ interface: useful for getting details about a file
  + __Blob__ interface: read binary data (only) accessed slice by slice (as chunks of data, each one being a "Blob")
  + __FileReader__ interface: reading file content

+ [File API](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#631-introduction)
  + features for accessing file metadata (name, size, type) from client-side JavaScript
  + methods for reading file contents directly in the browser
  + particularly interesting for displaying preview of images before uploading them
  + much more interesting: developing Web applications work with local files w/o the need for a server
  + [File API Specification](https://www.w3.org/TR/FileAPI/)
  + example: loading image files for preview


### File Metadata

+ [File metadata](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#633-reading-file-metadata)
  + metadata: name, size, type and last modification date
  + select one or more files: `<input type="file" id="input" ... />`
    + rendered as a "select files" or "browse files" button
    + file chooser dialog popped-up to select one file
    + do nothing in the client-side before HTML5 die to no access from JavaScript
  + File API 
    + define a file property on the DOM node corresponding to the `<input type="file".../>` input field
    + property as an array
    + the metadata related to `selectedFile` variable: `selectedFile.name, selectedFile.size, selectedFile.type, selectedFile.lastModifiedDate`
  + example: read file metadata from `<input type="file" id="input" onchange="displayFirstSelectedFileMetadata();"/>`
  + example: display metadata of multiple files w/ a filter on the file type
    + select several images: `<input type="file" accept="image/*" multiple onchange="filesProcess(this.files)" name="selection"/>`
    + `accept="image/*"` attribute: a filter restricting selection to images only
    + `filesProcess(...)` function: passing as parameter the list of selected files for the current element (`this.files`)
    + `for` loop builds all the rows that compose the table, adding HTML code to the selection string variable
      + prepare the HTML code for building a `<table>` with the results
      + build table and headings: `var selection = "<table><tr><th>Name</th><th>Bytes</th><th>MIME Type</th> <th>Last modified date</th></tr>";`
      + build rows iteratively
      + closing table: `selection += "</table>";`
    + table added to the page: `document.getElementById("result").innerHTML = selection;`
      + table appears on the page dynamically
      + use the innerHTML attribute of the DOM element corresponding to the `<div id="result">` in order to insert the table as its child in the DOM tree


### Bolb Object

+ [Blob object](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#the-blob-object)
  + a structure representing binary data available as read-only
  + two properties, namely: size and type
  + retrieving the size in bytes of the data handled by the Blob and their MIME type


### File Object

+ [File object](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#the-file-object)
  + useful for manipulating files
  + inherit the properties and methods of `Blob` objects
  + two additional properties
    + name: the file name
    + lastModifiedDate: the date of the last modification of the file

+ [Procedure to read file contents](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#635-reading-file-content)
  + create a FileReader object
    + several methods for reading file content, each taken from the `FileReader` interface
    + create a FileReader object: `var reader = new FileReader();`
  + call a method of the FileReader object for reading the file content
    + three different methods available for reading a file's content: `readAsText`, `readAsArrayBuffer` and `readAsDataURL`
    + `readAsArrayBuffer` for binary data
    + `readAsDataURL`
      + content as a URL used to set the `src` field of an `<img src=...>`, `<audio>`, `<video>`
      + all existing methods/properties that accept a URL
    + start reading the file asynchronously: `reader.readAsText(f);`
    + executed by the browser in the background
    + `reader.onload `callback only when the file is read entirely
  + get the file content in an `onload` callback
    + called only when the file content loaded
    + the content: `e.target.result`
    + called only when the file content available: `reader.onload = function(e) {...}`
    + event `e` as a unique parameter
    + `e.target.result` = the file content


### Text Files

+ [Read text file](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#636-read-file-content-as-text)
  + read a single file's content
    + start reading the file asynchronously: `reader.readAsText(files[0]);`
    + call the `onload` callback when the file is read
    + called when the file content is loaded: `reader.onload = function(e) {...}`
      + the file content: `e.target.result`
      + display content in the `textarea` with `id="fileContent"`: `document.getElementById("fileContent").value= e.target.result;`
  + read multiple files
    + select multiple files: `<input type="file" id="files" multiple onchange="readFilesAndDisplayAsText(this.files);"/><br/>`
    + `onload` listener to print the name of the file...
    + iterate to read files
  
+ [Character encoding for text file](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#about-character-encoding)
  + optionally indicate the encoding of the file going to read
  + default: UTF-8
  + e.g., `reader.readAsText(file, 'UTF-8'); reader.readAsText(file, 'ISO-8859-1');`


### Binary Files

+ [Read binary file](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#637-read-file-content-as-binary)
  + rarely used, except for loading "raw" binary data
  + HTML page for specific binary files
    + image files or drawing in a canvas: using the `<img src= tag>`
    + audio files: using the `<audio>` elements
    + video files: using the `<video>` elements
  + image, drawing, audio, and video files: referable to use the `readAsDataURL` method
  + `readAsArrayBuffer` method used for purposes
    + reading audio samples that should be loaded in memory  
    + played using the WebAudio API
    + loading textures that you will use with WebGL for 3D animations
  + WebAudio API
    + useful for reading audio sound samples from memory (no streaming)
    + designed for music application and games
  + example: read audio file and play w/ WebAudio API
    + read a local audio file and play directly in the Browser
    + user selects file and read it as an `ArrayBuffer` and pass to the API: `var fileInput = document.querySelector('input[type="file"]');`
    + define a change listener: `fileInput.addEventListener('change', function(e) {...}`
      + after choosing a file, the listener executed
      + start the reading of the file content, as a binary file: `reader.readAsArrayBuffer(this.files[0]);`
      + once the file entirely read, the `onload` callback asynchronously called by the browser
    + executed the `onload` callback when the file content is loaded in memory
    + pass the file content to the `initSound(e.target.result);` function to play


### dataURL method

+ [Read file as dataURL](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#638-read-file-content-as-dataurl)
  + data URL: a URL including type and content at the same time
  + useful for in-lining images or videos in the HTML of a Web page
  + mobile devices: speed up the loading of the page by reducing the number of HTTP requests
  + example: the red square w/ dataURL
    + dataURL: `data:image/png;base64,iVBOR...`
    + `src` attribute of an image element `<img src="data:image/png....">` with the data URL: `<img src="data:image/png;base64,iVBORw..." alt="Red square" width=50 height=50/>`
  + dataURL format
    + enabling file content to be stored in a base64 format (as a string)
    + adding the MIME type specification of the content
    + able to store a file as a URL readable with modern browsers
    + commonly used on the Web
    + especially for mobile applications, in-lining images reducing the number of HTTP requests and making the Web page load faster
    + [Image to Data URI converter](https://ezgif.com/image-to-datauri)
    + able to encode any type of file as dataURL
    + most frequently used with media files (images, audio, video)
  + example: read images as data URL & display
    + starts the reading of the file `f`: `reader.readAsDataURL(f);`
    + when `f` read, the `onload` callback called: `reader.onload = function(e) {...}`
      + render thumbnail
      + `e.target.result` = the image content as a data URL
      + create a span with CSS `class="thumb"` for nicer layout: `var span = document.createElement('span');`
      + add an `<img src=...>` in the span, with src= the dataURL of the image: `span.innerHTML = "<img class='thumb' src='" + e.target.result + "' alt='a picture'/>";`
      + insert the span in the `<output id="list"></output>`:  `document.getElementById('list').insertBefore(span, null);`
  + example: read local image file and use it with drawImage in a canvas
    + create an image object to draw an image on a canvas: `var img = new Image();`
    + `e.target.result` as the dataURL
    + set the `src` attribute of the image object: `img.src= e.target.result`
    + asynchronously call the `onload` callback: `img.onload = function(e) { ctx.drawImage(img, 0, 0, 400, 400); }`





## Geolocaltion APIs

### Geolocation APIs


+ [Geolocation API](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#641-introduction)
  + implemented by most modern Web browsers
  + using different means to get the current location: GPS, GSM/3G triangulation, Wifi, IP address, etc.
  + mobile phones:
    + prompt the user to activate the GPS and ask for a particular mean among those available
    + track the current position when it changes
    + useful for writing a navigation application
    + useful for tracking in real time the position of different participants
    + application involving several persons at the same time (using WebSockets, for example)
  + typical usage

    ```js
    navigator.geolocation.getCurrentPosition(showPosition, onError);

    function showPosition(position) {
        console.log("latitude is: " + position.coords.latitude);
        console.log("longitude is: " + position.coords.longitude);
    }

    function onError(err) {
        console.log("Could not get the position");
    }
    ```

  + example: get location
    + check if the Web browser supports the `geolocation` API by testing the variable `navigator.geolocation`:
      + `navigator.geolocation.getCurrentPosition(showPosition)` passing a callback function as a parameter
      + when a current position available, the callback function called asynchronously
      + the input parameter of this callback function = the current position

      ```js
      function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            displayCoords.innerHTML="Geolocation API not supported by your browser.";
        }
      }
      ```

    + position objects w/ a `coords` property: the longitude and the latitude

      ```js
      function showPosition(position) {
        displayCoords.innerHTML="Latitude: " + position.coords.latitude +
                               "<br />Longitude: " + position.coords.longitude;
      }
      ```

  + [Geolocation API Specification](https://www.w3.org/TR/geolocation-API/)
  + [Geolocation API - WDN](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)

+ [coords object properties](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#642-the-coords-object-properties)
  + __latitude:__ the latitude of the position
  + __longitude:__ the longitude of the position
  + __altitude:__ the altitude of the position
  + __accuracy:__ the accuracy of the measure of the longitude and latitude (in meters)
  + __altitudeAccuracy:__ the accuracy of the measure of the altitude (in meters)
  + __heading:__ giving the orientation relative to north, in degrees
  + __speed:__ current speed in meters/second

+ [Geolocation error codes](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#643-geolocation-error-codes)
  + `navigator.geolocation.getCurrentPosition` method possible to pass a second parameter in case of errror
  + example: error handler
    + get location: `navigator.geolocation.getCurrentPosition(showPosition, errorPosition);`
    + error handling

      ```js 
      function errorPosition(error) {
        var info = "Error during geolocation: ";
        switch(error.code) {
          case error.TIMEOUT:
              info += "Timeout !";
              break;
          case error.PERMISSION_DENIED:
              info += "Permission denied, geolocation could not be obtained...";
              break;
          case error.POSITION_UNAVAILABLE:
              info += "Location could not be obtained though the available means...";
              break;
          case error.UNKNOWN_ERROR:
              info += "Unknown error";
              break;
        }
        displayCoords.innerHTML = info;
      }
      ```

+ [Tracking position](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#644-tracking-a-position) 
  + syntax: `watchPosition(onSuccess, onError)`
    + get the callback function only when the current position changes
    + return an `id` to use the `clearWatch(id)` method to stop the current tracking
  + track the current position
  + typical usage:
    + get an id of the current tracking: `var watchPosId = navigator.geolocation.watchPosition(showPosition);`
    + stop the tracking: `navigator.geolocation.clearWatch(watchPosId);`


### Tracking Position

+ [Properties of the coords object for real time tracking](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#options-available-when-using-the-geolocation-api-in-particular-real-time-tracking)
  + __enableHighAccuracy:__ 
    + a boolean (true/false) indicating to the device wish to obtain its most accurate readings
    + using the GPS
    + probably making a difference, depending on your hardware, GPS availability, etc.
  + __maximumAge:__
    + the maximum amount of time (in milliseconds) the position  in the cache
    + appropriate as the device may cache readings to save power and/or bandwidth
  + __timeout:__
    + the maximum time (in milliseconds)
    + prepared to allow the device to try to obtain a Geo location
    + after this timeout, call the `onError` callback

+ [Example: tracking position](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#example-of-use)
  + ask to turn GPS on, if available: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {enableHighAccuracy:true});`
  + the position cached for 10 mins useful when in tunnels: `maximumAge = 10 mins` 
  + when the device tries to get a position, if it does not succeed, then go on error immediately: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:600000, timeout:0});`
  + position will never come from the cache (maximumAge: 0), and if after 0.1s the position could not be computed, then go on error: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:0, timeout:100});`
  + ask for GPS, cache for 30s, 27s before going on error: `watchId=navigator.geolocation.watchPosition(onSuccess, onError, {enableHighAccuracy:true, maximumAge:30000, timeout:27000});`


### 

+ [Get a map centered on given longitude and latitude](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#645-geolocation-and-maps)
  + rendering a map with the [Leaflet API for OpenStreetMaps](https://leafletjs.com/reference-1.6.0.html)
  + required files to use the Leaflet API :
    + `<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css">`
    + `<script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>`
  + container to display the interactive map: `<div id="map"></div>`
  + using the [Geolocation API](https://www.w3.org/TR/geolocation-API/) to get the current position: `navigator.geolocation.getCurrentPosition(success, error);`
  + successfully get the location: `function success(position) {...}`
    + get the longitude and latitude properties from the location: `latitude = position.coords.latitude, longitude = position.coords.longitude;`
    + instance map using leaflet w/ `id='map'`: `map = L.map('map').setView([latitude, longitude], 13);`
    + tile layer using key API at cloudmade.com
    + marker using leaflet: `marker = L.marker([latitude, longitude]).addTo(map);`
    + popup in leaflet: `marker.bindPopup('<p>Your location</p>').openPopup();`
  + get current position fail: `alert('Get current position fail. Please access codepen to get geolocation.');`



### Reverse Geocoding

+ [Reverse Geocoding](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#646-reverse-geocoding)
  + Web services:
    + used to get an address from longitude and latitude
    + mostly free of charge, but ask to register an API key and enter your credit card number
    + if too many requests, you will be charged
    + examples:
      + the [Google Reverse Geocoding JavaScript API](https://tinyurl.com/pdlpfjc)
      + Leaflet plugin (an extension to Leaflet) based on the Gisgraphy (free open source framework)
  + example: get address from longitude & latitude
    + access Google API: `<script src="https://maps.googleapis.com/maps/api/js?key=PUT_HERE_YOUR_API_KEY&v=3.exp&sensor=false">`
    + using the google apis: `var infowindow = new google.maps.InfoWindow();`
    + initializing JS after page loaded: `function init() {...}`
      + linking w/ html elements: `displayCoords=document.getElementById("msg"); myAddress = document.getElementById("address");`
      + access Google map: `geocoder = new google.maps.Geocoder();`
      + displaying something before click button: `geocoder = new google.maps.Geocoder();`
      + parameters for Google map: `var mapOptions = { zoom: 8, center: latlng, mapTypeId: 'roadmap' }`
      + get initial map: `map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);`
    + button clicked: `navigator.geolocation.getCurrentPosition(showPosition);`
    + show position as available: `function showPosition(position) {...}`
      + insert HTML code: `displayCoords.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;`
      + display map: `showOnGoogleMap(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));`
    + ask google geocoder for an address: `function showOnGoogleMap(latlng) {...}`
      + the reverse geocoder sends back an array of "guesses", i.e. not just one address object, but several
      + each entry in this array has several properties such as street, city, etc.
      + using the "formatted_address" one here
      + probably interesting to get the detailed properties in other applications like a form with street, city, zip code etc.
      + the reverse geocoder: `geocoder.geocode({'latLng': latlng},reverseGeocoderSuccess);`
    + process the map: `function reverseGeocoderSuccess(results, status) {...}`
      + display marker if success: `status == google.maps.GeocoderStatus.OK`
      + showing warning message: `alert('Geocoder failed due to: ' + status);`






