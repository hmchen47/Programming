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


## Keyboard events

+ [Key events](#432-keyboard-interaction-key-events)
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




