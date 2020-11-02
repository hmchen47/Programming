# Week 4: HTML5 Animations


## 4.3 Canvas and user interaction


### 4.3.0 Lecture Notes

+ [DOM events](#431-events-input-and-output)
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

+ [Mouse events](#433-mouse-interaction-mouse-events)
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
    + example: wrong mouse position - window coordinates

      ```js
      function getMousePos(canvas, evt) {
        return {
            x: evt.clientX,
            y: evt.clientY
        };
      }
      ```

    + example: good mouse position - canvas coordinates

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

  + [mouse positions w/ button pressed and released](#how-to-display-the-mouse-position-and-the-mouse-button-that-has-been-pressed-or-released)

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
    + mouse listeners: `canvas.addEventListener('mousemove', handleMousemove, false); canvas.addEventListener('mousedown', handleMousedown, false); canvas.addEventListener('mouseup', handleMouseup, false);`
    + start the animation: `requestId = requestAnimationFrame(animationLoop);`
    + mousePos taken into account in the animationLoop: `function handleMousemove(evt) { mousePos = getMousePos(canvas, evt); }`
    + increment on the angle taken into account in the animationLoop: `function handleMousedown(evt) { incrementAngle = 0.1; }`
    + stop the rotation: `function handleMouseup(evt) { incrementAngle = 0; }`
    + get mouse position in canvas: `function getMousePos(canvas, evt) {...}`
    + `animationLoop` function: `function animationLoop() {...}`
      + clear: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
      + draw: `drawMonster(monsterX, monsterY, monsterAngle, 'green', 'yellow');`
      + move in canvas: `if(mousePos !== undefined) { monsterX = mousePos.x; monsterY = mousePos.y; monsterAngle += incrementAngle; }`
  + example: move mouse as pencil to draw in canvas
    + a line is a path w/ a single draw order
    + at each mouse event draw the whole path from the beginning 
    + lines normally only usable in path mode

      ```js
      function drawLineImmediate(x1, y1, x2, y2) {
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.line(x2, y2);
        ctx.stroke();
      }
      ```

    + draw lines following the mouse position: `function handleMouseMove(evt) {...}`

      ```js
      if (!started) {
        previousMousePos = mousePos;  // get the current mouse position
        started = true;
      } else {
        // get two consecutive mouse positions before drawing a line
        drawLineImmediate(preeviousMousePos.x, previousMousePos.y, mousePosx, mousePosy);
        previousMousePos = mousePos;
      }
      ```

    + onload function after loading page: `window.onload = function () {...}`
      + unable to draw any line before mouse moved into canvas: `started = false;`
      + listen to the movement of mouse: `canvas.addEventListener('mousemove', handleMouseMove, false);`
  + example: draw only when mouse button pressed
    + event listeners: `canvas.addEventListener('mousemove', handleMouseMove, false); canvas.addEventListener('mousedown', clicked); canvas.addEventListener('mouseup', released);`
    + press mouse button: `function clicked(evt) {previousMousePos = getMousePos(canvas, evt); painting = true;}`
    + release mouse button: `function released(evt) { painting = flase; }`
    + draw lines following the mouse position: `function handleMouseMove(evt) {...}`

+ [Responsive canvas](#434-responsive-canvas)
  + rules of resizing a canvas
    + changing `width` and `height` property $\to$ erase the content and reset the context
    + using `%` in the CSS `width` and `height` properties of a canvas $\to$ scaling the existing pixels w/o erasing the content, given a blurry image
  + __<mark style="color: black; background-color: lightpink;">best practice</mark>__: never use CSS percentage on a canvas width or height
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
        ```

+ [Keycode values](https://tinyurl.com/y333tfjx)


### 4.3.1 Events: input and output

In JavaScript, we treat events made by users as an input, and we manipulate the DOM structure as an output. Most of the time in games/animations, we will change state variables of moving objects, such as position or speed of an alien ship, and the animation loop will take care of these variables to move the objects.

The events are called DOM events, and we use the _DOM JavaScript API_ to create _event handlers_.


#### There are three ways to manage events in the DOM structure

__First way: declare event handlers in the HTML code__

You will often find this in examples on the Web:

<div><ol>
<li value="1">&lt;div id="someDiv" <strong>onclick="alert('clicked!');"</strong>&gt; </li>
<li>&nbsp; &nbsp; content of the div </li>
<li>&lt;/div&gt;</li>
</ol></div>

Note: this is not the recommended way to handle events, even if it's very easy to use. Mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) in one place is ok for small examples (we have used this in some examples in this course) but is not the recommended way for full scale applications where a clean separation is best.


__Second way: add an event handler to an HTML element in JavaScript__

Here is an example:

<div><ol>
<li value="1">document.getElementById('someDiv').onclick = function(evt) {</li>
<li>&nbsp; alert('clicked!');</li>
<li>}</li>
</ol></div>

This method is fine, but  you will not be able to attach several listener functions. If you need to do this, the preferred version is the next one.


__Third way: register a callback to the event listener with the `addEventListener` method__

This is how we do it:

<div><ol>
<li value="1">document.getElementById('someDiv').addEventListener('click', function(evt) {</li>
<li>&nbsp; &nbsp; alert('clicked!');</li>
<li>}, false);</li>
</ol></div>

The third parameter is not important for now, just set it to `false`, or simply do not add a third parameter.


#### The DOM event that is passed to the event listener function

When you create an EventListener and attach it to an element,  an event object will be passed as a parameter to your callback, just like this:

<div><ol>
<li value="1">element.addEventListener('click', function(<strong>event</strong>) {</li>
<li>&nbsp; &nbsp;<strong>// now you can use the event object inside the callback</strong></li>
<li>}, false);</li>
</ol></div>

Depending on the type of event you are listening to, we will use different properties from the event object in order to get useful information like: "what keys have been pressed down?", "what is the position of the mouse cursor?", "which mouse button is down?", etc.

Let's see next how to deal with the keyboard and the mouse. In the [W3Cx HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games) course, we look at additional APIs such as the [gamePad API](https://www.w3.org/TR/gamepad/) for using USB or wireless gamepads/joysticks/game controllers.


#### Knowledge check 4.3.1

Source code for the knowledge check 4.3.1

[Online example on JS Bin](http://jsbin.com/korele/edit)

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Click on button&lt;/title&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &nbsp;<strong>&lt;button id="myButton"&gt;Click me!&lt;/button&gt;</strong></li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp;var button = document.getElementById('myButton');</li>
<li>&nbsp; &nbsp;<strong>// Define a click listener on the button</strong></li>
<li><strong>&nbsp; &nbsp;button.addEventListener('click', processClick);</strong></li>
<li> </li>
<li>&nbsp; &nbsp;// callback</li>
<li>&nbsp; &nbsp;function processClick(<strong>event</strong>) {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("Button clicked");</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong>// What is the event parameter?</strong></li>
<li>&nbsp; &nbsp;}</li>
<li> &lt;/script&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


1. When you create an event listener like in the code above, what is the event parameter (line 15) passed to the callback function useful for?

  a. It will hold relevant data about the interaction (element that fired the event, key code, mouse button and position of the mouse cursor, etc.)<br/>
  b. It's not useful, it's just here for debug purposes.<br/>

  Ans: a<br/>
  Explanation: The event is useful for getting information about what fired the event, button, mouse, etc... The data it holds depends on the type of the event. This [example shows how we can get the id of the button that has been clicked and the value of the button label](https://jsbin.com/ruzofa/edit).



### 4.3.2 Keyboard interaction, key events

This has been a bit of a nightmare for years, as different browsers have had different ways of handling key events and key codes (read [this article](https://unixpapa.com/js/key.html) if you are fond of JavaScript archeology). Fortunately it's much better today, and we are able to rely on methods that should work on any browser.

When you listen to keyboard related events (`keydown`, `keyup` or `keypressed`), the event parameter passed to the listener function will contain the code of the key that fired the event. Then it is possible to test what key has been pressed or released, like this:

<div><ol>
<li value="1">window.addEventListener('keydown', function(event) {</li>
<li>&nbsp; &nbsp;if (<strong>event.keyCode === 37</strong>) {</li>
<li>&nbsp; &nbsp; &nbsp;//left arrow was pressed</li>
<li>&nbsp; &nbsp;}</li>
<li>}, false);</li>
</ol></div>

At line 2, the value "37" is the key code that corresponds to the left arrow. It might be difficult to know the correspondences between real keyboard keys and codes, so here are handy pointers:

+ Try key codes with this [interactive test page](http://www.asquare.net/javascript/tests/KeyCode.html).
+ And find a list of keyCodes below (taken from this [CSS Tricks article](https://css-tricks.com/snippets/javascript/javascript-keycodes/)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y333tfjx')"
    src    ="https://tinyurl.com/y5y53a2e"
    alt    ="JavaScript keycode table. This is a screenshot of the HTML table presented in https://css-tricks.com/snippets/javascript/javascript-keycodes/#keycode-values"
    title  ="JavaScript keycode table. This is a screenshot of the HTML table presented in https://css-tricks.com/snippets/javascript/javascript-keycodes/#keycode-values"
  />
</figure>


#### Examples

Example #1: adding a key listener to the window object
A lot of people think that the canvas element is not able to get key events. Many examples on the Web handle key events on canvas by adding a listener to the window object directly, like this:

[Online example](https://jsbin.com/boqumo/1/edit?html,output):  ([Local Example - Keydown Listener](src/4.3.2-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/y572v8ul"
    alt    ="key detected"
    title  ="key detected"
  />
</figure>


Extract from source code:

<div><ol>
<li value="1">&lt;canvas id="myCanvas" width="350" height="200"&gt;</li>
<li>&lt;/canvas&gt;</li>
<li>&nbsp;</li>
<li>&lt;script&gt;</li>
<li> </li>
<li>function init() {</li>
<li>&nbsp; &nbsp;&nbsp;<strong>// This will work when you press a key, anywhere on the document</strong></li>
<li>&nbsp; &nbsp; <strong>window</strong><strong>.addEventListener('keydown', handleKeydown, false);</strong></li>
<li> }</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li>function handleKeydown(e){</li>
<li>&nbsp; &nbsp; alert('keycode: '+e.keyCode);</li>
<li>&nbsp; &nbsp;&nbsp;return false;</li>
<li> };</li>
<li>&lt;/script&gt;</li>
</ol></div>

Indeed this solution works well if you write a game, and want to detect events wherever the mouse cursor is, and without worrying about what HTML element has the focus, etc...


__Move the monster with the keyboard__

[Online example at JS Bin](https://jsbin.com/galebil/1/edit?html,output): ([Local Example - Move w/ Keyboard](src/4.3.2-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/yx8zot2n"
    alt    ="monster moving with jeys"
    title  ="monster moving with jeys"
  />
</figure>


Extract from source code:

<div><ol>
<li value="1">&lt;script&gt;</li>
<li> var canvas, ctx;</li>
<li> var<strong> monsterX=100</strong>, monsterY=100, monsterAngle=0;</li>
<li> var<strong> incrementX = 0</strong>;</li>
<li> </li>
<li> function init() {</li>
<li>&nbsp; &nbsp;&nbsp;// This function is called after the page is loaded</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// 1 - Get the canvas</li>
<li>&nbsp; &nbsp; canvas = document.getElementById('myCanvas');</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// 2 - Get the context</li>
<li>&nbsp; &nbsp; ctx=canvas.getContext('2d');</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;<strong>// 3 add key listeners to the window element</strong></li>
<li>&nbsp; &nbsp; <strong>window</strong><strong>.addEventListener('keydown', handleKeydown, false);</strong></li>
<li>&nbsp; &nbsp; <strong>window</strong><strong>.addEventListener('keyup', handleKeyup, false);</strong></li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// 4 - start the animation</li>
<li>&nbsp; &nbsp; requestId = requestAnimationFrame(animationLoop);</li>
<li> }</li>
<li> </li>
<li> function<strong> handleKeydown(evt)</strong> {</li>
<li>&nbsp; &nbsp;&nbsp;if (<strong>evt.keyCode === 37</strong>) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>//left key </strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>incrementX </strong><strong>= -1;</strong></li>
<li>&nbsp; &nbsp;&nbsp;} else if (<strong>evt.keyCode === 39</strong>) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>// right key</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>incrementX </strong><strong>= 1;</strong></li>
<li>&nbsp; &nbsp;&nbsp;} </li>
<li> }</li>
<li> function<strong> handleKeyup(evt)</strong> {</li>
<li>&nbsp; &nbsp; <strong>incrementX </strong><strong>= 0;</strong></li>
<li> }</li>
<li> </li>
<li> function animationLoop() {</li>
<li>&nbsp; &nbsp;&nbsp;// 1 - Clear</li>
<li>&nbsp; &nbsp; ctx.clearRect(0, 0, canvas.width, canvas.height);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// 2 Draw</li>
<li>&nbsp; &nbsp; drawMonster(monsterX, monsterY, monsterAngle, 'green', 'yellow');</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;<strong>// 3 Move</strong></li>
<li>&nbsp; &nbsp; <strong>monsterX </strong><strong>+= incrementX;</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// call again mainloop after 16.6 ms (60 frames/s)</li>
<li>&nbsp; &nbsp; requestId = requestAnimationFrame(animationLoop);</li>
<li> } </li>
<li>&lt;/script&gt;</li>
</ol></div>


__Example #2: what if I want to listen to key events only in my canvas?__

If you add a key listener to a canvas element, the problem is that it will get events only when it has the focus. And by default, it will never have the focus!

The `tabindex` attribute of the canvas element makes it focusable. Without it, it will never get the focus!

The trick is to declare the canvas like this:

<div><ol>
<li value="1">&lt;canvas id="myCanvas" width="350" <strong>tabindex="1"</strong> height="200"&gt;</li>
<li>&lt;/canvas&gt;</li>
</ol></div>

And we force the canvas to get the focus with:

<div><ol>
<li value="1">canvas=document.getElementById('myCanvas');</li>
<li>...</li>
<li><strong>canvas.focus();</strong></li>
</ol></div>

Now, if we try an example with the above canvas declaration, we show when an HTML element has the focus: a border is added to it, as shown in this [JSBin code](https://jsbin.com/hobuni/1/edit?html,output). ([Local Example - within Canvas](src/4.3.2-example3.html))

Note that the line that forces the focus to the canvas is commented by default. Try to click on the canvas, then press a key, then click out of the canvas, then press a key: this time nothing happens!

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/y52m7baf"
    alt    ="a border appears when the canvas has the focus"
    title  ="a border appears when the canvas has the focus"
  />
</figure>


Extract from the code:

<div><ol>
<li value="1"> var canvas;</li>
<li> </li>
<li> function init() {</li>
<li>&nbsp; &nbsp; &nbsp;canvas=document.getElementById('myCanvas');</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;// This will work only if the canvas has the focus </li>
<li>&nbsp; &nbsp; &nbsp;<strong>canvas</strong><strong>.addEventListener('keydown', handleKeydown, false);</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;<strong>// We can set the focus on the canvas like this:</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong>//canvas.focus();</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// ... but it will stop working if we click somewhere else</li>
<li>&nbsp; &nbsp; &nbsp;// in the document</li>
<li> }</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li> function handleKeydown(e){</li>
<li>&nbsp; &nbsp; &nbsp;alert('keycode: '+e.keyCode);</li>
<li>&nbsp; &nbsp; &nbsp;return false;</li>
<li> };</li>
</ol></div>

Line 10 is useful to initially set the focus on the canvas, but this trick will not work if we click somewhere else in the HTML page.

__Example #3: a better way: set the focus when the mouse cursor enters the canvas__

A better way to manage key events on a canvas is to set the focus when the mouse is over the canvas, and to un-focus it otherwise.

Here is a modified version of the "move monster example" seen earlier. This time, you move the monster with the left and right arrow only when the mouse cursor is over the canvas. We added two mouse event listeners on the canvas: one for the `mouseenter` event and the other for the `mouseout` event.

When the mouse enters the canvas we call `canvas.focus()` to set the focus to the canvas, and when the mouse cursor goes out of the canvas, we call `canvas.blur()` to unset the focus.

[Online example at JS Bin](https://jsbin.com/koboniz/1/edit?html,output) ([Local Example - Mouse Hoover](src/4.3.2-example4.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yx9ukm7g')"
    src    ="https://tinyurl.com/y4ha3n96"
    alt    ="canvas gets focus only when mouse is over it..."
    title  ="canvas gets focus only when mouse is over it..."
  />
</figure>


Extract from the code:

<div><ol>
<li value="1"> function init() {</li>
<li>&nbsp; &nbsp;// This function is called after the page is loaded</li>
<li>&nbsp; &nbsp;// 1 - Get the canvas</li>
<li>&nbsp; &nbsp;canvas = document.getElementById('myCanvas');</li>
<li>&nbsp; &nbsp;// 2 - Get the context</li>
<li>&nbsp; &nbsp;ctx=canvas.getContext('2d');</li>
<li></li>
<li>&nbsp; &nbsp;// 3 - Add key listeners to the window element</li>
<li>&nbsp; &nbsp;canvas.addEventListener('keydown', handleKeydown, false);</li>
<li>&nbsp; &nbsp;canvas.addEventListener('keyup', handleKeyup, false);</li>
<li></li>
<li>&nbsp; &nbsp;<strong>canvas</strong><strong>.addEventListener('mouseenter', setFocus, false);</strong></li>
<li>&nbsp; &nbsp;<strong>canvas</strong><strong>.addEventListener('mouseout', unsetFocus, false);</strong></li>
<li> </li>
<li>&nbsp; &nbsp;// 4 - Start the animation</li>
<li>&nbsp; &nbsp;requestId = requestAnimationFrame(animationLoop);</li>
<li> }</li>
<li> </li>
<li> function setFocus(evt) {</li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.focus();</strong> </li>
<li> };</li>
<li> </li>
<li> </li>
<li> function unsetFocus(evt) {</li>
<li>&nbsp; &nbsp;<strong>canvas</strong><strong>.blur();</strong> </li>
<li><strong>&nbsp; &nbsp;<span style="color: #222222; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 14px; line-height: 20.72px;">incrementX = 0; // stop the monster if the mouse exists the canvas</span></strong></li>
<li> };</li>
</ol></div>

The third parameter (false) of _lines 12_ and _13_ means "we do not want to propagate the event to the ancestors of the canvas in the DOM." 


#### Knowledge check 4.3.2

1. Suppose we have defined a key event listener to a canvas: should this canvas have the focus in order to fire key events? (Yes/No)

  Ans: <span style="color: magenta;">Yes</span>, xNo<br/>
  Explanation: The problem with adding a key listener to a canvas element is that it will get events only when the canvas has the focus. And by default, it will never have the focus! The course shows how to handle different cases.



### 4.3.3 Mouse interaction, mouse events

Detecting mouse events in a canvas is quite straightforward: you add an event listener to the canvas, and the browser invokes that listener when the event occurs.

The example below is about listening to `mouseup` and `mousedown` events (when a user presses or releases any mouse button):

<div><ol>
<li value="1">canvas.addEventListener('mousedown', function (evt) {</li>
<li> // do something with&nbsp;to the mousedown event</li>
<li>});</li>
</ol></div>

The event received by the listener function will be used for getting the button number or the coordinates of the mouse cursor. Before looking at different examples, let's look at the different event types we can listen to.

#### The different mouse events

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5c8orsx')"
    src    ="https://tinyurl.com/y5gvuk7r"
    alt    ="Mouse events illustrated"
    title  ="Mouse events illustrated"
  />
</figure>


We saw in the last example how to detect the `mouseenter` and `mouseout` events.

There are other events related to the mouse:

+ `mouseleave`: similar to `mouseout`, fired when the mouse leaves the surface of the element. The difference between `mouseleave` and `mouseout` is that `mouseleave` does not fire when the cursor moves over descendant elements, and `mouseout` is fired when the element moved is outside of the bounds of the original element or is a child of the original element.
+ `mouseover`: the mouse cursor is moving over the element that listens to that event. A `mouseover` event occurs on an element when you are over it - <u>coming from either its child OR parent element</u>, but a `mouseenter` event only occurs when the mouse <u>moves from the parent element to the child element</u>.
+ `mousedown`: fired when a mouse button is pressed.
+ `mouseup`: fired when a mouse button is released.
+ `mouseclick`: fired after a `mousedown` and a `mouseup` have occurred.
+ `mousemove`: fired while the mouse moves over the element. Each time the mouse moves, a new event is fired, unlike with `mouseover` or `mouseenter`, where only one event is fired.


__The tricky part: accurately getting the mouse position relative to the canvas__

When you listen to any of the above events, the event object (we call it a "DOM event"), passed to the listener function, has properties that correspond to the mouse coordinates: `clientX` and `clientY`.

However, these are what we call "window coordinates". Instead of being relative to the canvas itself, they are relative to the window (the page).

Most of the time you need to work with the mouse position relative to the canvas, not to the window, so you must convert the coordinates between the window and the canvas. This will take into account the position of the canvas, and the CSS properties that may affect the canvas position (margin, etc.).

Fortunately, there exists a method for getting the position and size of any element in the page: `getBoundingClientRect()`.

Play with the [example online](https://jsbin.com/dugibiz/1/edit?html,output) that shows the problem. ([Local Example - Bad Mouse Position](src/4.3.3-example1.html))

__WRONG code:__

<div><ol>
<li value="1">...</li>
<li><strong> canvas.addEventListener('mousemove', function (evt) {</strong></li>
<li>&nbsp; &nbsp; <strong>mousePos </strong><strong>= getMousePos(canvas, evt);</strong></li>
<li>&nbsp; &nbsp;&nbsp;var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;</li>
<li>&nbsp; &nbsp; writeMessage(canvas, message);</li>
<li> }, false);</li>
<li>&nbsp;</li>
<li>...</li>
<li><strong>function getMousePos(canvas, evt) {</strong></li>
<li>&nbsp; <strong>&nbsp;</strong><strong>//&nbsp;WRONG!!!</strong></li>
<li>&nbsp; &nbsp;return {</li>
<li>&nbsp; &nbsp; &nbsp; <strong>x</strong><strong>: evt.clientX,</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong>y</strong><strong>: evt.clientY</strong></li>
<li>&nbsp; &nbsp;};</li>
<li>}</li>
</ol></div>

Here is the result, when the mouse is approximately at the top left corner of the canvas:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y5c8orsx')"
    src    ="https://tinyurl.com/y68d2qqn"
    alt    ="bad mouse coords"
    title  ="bad mouse coords"
  />
</figure>


[GOOD version of the code](https://jsbin.com/woxogun/edit?html,output): ([Local Example - Good Mouse Position](src/4.3.3-example2.html))

<div><ol>
<li value="1">function getMousePos(canvas, evt) {</li>
<li>&nbsp; &nbsp;<strong>// necessary to take into account CSS boundaries</strong></li>
<li>&nbsp; &nbsp;<strong>var rect = canvas.getBoundingClientRect();</strong></li>
<li>&nbsp; &nbsp;return {</li>
<li>&nbsp; &nbsp; &nbsp; x: evt.clientX <strong>- rect.left,</strong></li>
<li>&nbsp; &nbsp; &nbsp; y: evt.clientY <strong>- rect.top</strong></li>
<li>&nbsp; &nbsp;};</li>
<li>}</li>
</ol></div>

Result (the cursor is approximately at the top left corner):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y5c8orsx')"
    src    ="https://tinyurl.com/y53uz4hr"
    alt    ="mouse at zero zero"
    title  ="mouse at zero zero"
  />
</figure>


#### How to display the mouse position, and the mouse button that has been pressed or released

This example uses the previous function for computing the mouse position correctly. It listens to `mousemove`, `mousedown` and `mouseup` events, and shows how to get the mouse button number using the `evt.button` property.

[Online example](https://jsbin.com/qivexid/1/edit?html,output): ([Local Example - Mouse Press/Release](src/4.3.3-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5c8orsx')"
    src    ="https://tinyurl.com/y2fje7pm"
    alt    ="mouse event example"
    title  ="mouse event example"
  />
</figure>


Extract from source code:

<div><ol>
<li value="1">var canvas, ctx, mousePos, mouseButton;</li>
<li>&nbsp;</li>
<li>window.onload = function init() {</li>
<li>&nbsp; &nbsp; canvas = document.getElementById('myCanvas');</li>
<li>&nbsp; &nbsp; ctx = canvas.getContext('2d');</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mousemove', function (evt) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>mousePos </strong><strong>= getMousePos(canvas, evt);</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; writeMessage(canvas, message);</li>
<li>&nbsp; &nbsp;&nbsp;}, false);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mousedown', function (evt) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>mouseButton </strong><strong>= evt.button;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var message = "Mouse button " + evt.button + " down at position: " + mousePos.x + ',' + mousePos.y;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; writeMessage(canvas, message);</li>
<li>&nbsp; &nbsp;&nbsp;}, false);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mouseup', function (evt) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var message = "Mouse up at position: " + mousePos.x + ',' + mousePos.y;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; writeMessage(canvas, message);</li>
<li>&nbsp; &nbsp;&nbsp;}, false);</li>
<li>};</li>
<li>&nbsp;&nbsp;</li>
<li>function writeMessage(canvas, message) {</li>
<li>&nbsp; &nbsp;ctx.save();</li>
<li>&nbsp; &nbsp;ctx.clearRect(0, 0, canvas.width, canvas.height);</li>
<li>&nbsp; &nbsp;ctx.font = '18pt Calibri';</li>
<li>&nbsp; &nbsp;ctx.fillStyle = 'black';</li>
<li>&nbsp; &nbsp;ctx.fillText(message, 10, 25);</li>
<li>&nbsp; &nbsp;ctx.restore();</li>
<li>}</li>
<li>&nbsp;</li>
<li>function getMousePos(canvas, evt) {</li>
<li>&nbsp; &nbsp;<strong>// necessary to take into account CSS boudaries</strong></li>
<li>&nbsp; <strong>&nbsp;</strong><strong>var rect = canvas.getBoundingClientRect();</strong></li>
<li>&nbsp; &nbsp;return {</li>
<li>&nbsp; &nbsp; &nbsp; <strong>x</strong><strong>: evt.clientX - rect.left</strong>,</li>
<li>&nbsp; &nbsp; &nbsp; <strong>y</strong><strong>: evt.clientY - rect.top</strong></li>
<li>&nbsp; &nbsp;};</li>
<li>}</li>
</ol></div>


#### More examples

__Example #1: move the monster with the mouse, rotate it when a mouse button is pressed__

This example shows an animation at 60 frames/s using `requestAnimationFrame`, were the monster is drawn at the mouse position, and if a mouse button is pressed, the monster starts rotating around its center. If we release the mouse button, the rotation stops.

[Online example](https://jsbin.com/hovopim/edit?html,output): ([Local Example - Mouse to Rotate](src/4.3.3-example4.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5c8orsx')"
    src    ="https://tinyurl.com/yxoc885f"
    alt    ="monster follows the mouse + rotate"
    title  ="monster follows the mouse + rotate"
  />
</figure>


Extract from source code:

<div><ol>
<li value="1"> var canvas, ctx;</li>
<li> var<strong> monsterX=100, monsterY=100, monsterAngle=0</strong>;</li>
<li> var incrementX = 0;</li>
<li> var<strong> incrementAngle =0;</strong></li>
<li> <strong>var mousePos;</strong></li>
<li> </li>
<li> function init() {</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;// 3bis - Add mouse listeners</li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mousemove', handleMousemove, false);</strong></li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mousedown', handleMousedown, false);</strong></li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mouseup', handleMouseup, false);</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;// 4 - Start the animation</li>
<li>&nbsp; &nbsp; requestId = requestAnimationFrame(animationLoop);</li>
<li> }</li>
<li> </li>
<li> function<strong> handleMousemove</strong>(evt) {</li>
<li>&nbsp; &nbsp; <strong>// The mousePos will be taken into account in the animationLoop</strong></li>
<li>&nbsp; &nbsp; <strong>mousePos </strong><strong>= getMousePos(canvas, evt);</strong></li>
<li> }</li>
<li> </li>
<li> function handleMousedown(evt) {</li>
<li>&nbsp; &nbsp;<strong>// the increment on the angle will be</strong></li>
<li>&nbsp; &nbsp;<strong>// taken into account in the animationLoop</strong></li>
<li>&nbsp; &nbsp;<strong>incrementAngle </strong><strong>= 0.1;</strong></li>
<li> }</li>
<li> </li>
<li> function<strong> handleMouseup(evt)</strong> {</li>
<li>&nbsp; &nbsp; <strong>incrementAngle </strong><strong>= 0; &nbsp;// stops the rotation</strong></li>
<li> }</li>
<li> </li>
<li> function getMousePos(canvas, evt) {</li>
<li>&nbsp;... // same as before</li>
<li>}</li>
<li>...</li>
<li> function animationLoop() {</li>
<li>&nbsp; &nbsp;// 1 - Clear</li>
<li>&nbsp; &nbsp;ctx.clearRect(0, 0, canvas.width, canvas.height);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// 2 - Draw</li>
<li>&nbsp; &nbsp;drawMonster(monsterX, monsterY, monsterAngle, 'green', 'yellow');</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// 3 - Move</li>
<li>&nbsp; &nbsp;<strong>if(mousePos !== undefined) { // test necessary, maybe the mouse is not yet on canvas</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong>monsterX </strong><strong>= mousePos.x;</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong>monsterY </strong><strong>= mousePos.y;</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong>monsterAngle </strong><strong>+= incrementAngle;</strong></li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// call again mainloop after 16.6 ms (60 frames/s)</li>
<li>&nbsp; &nbsp;requestId = requestAnimationFrame(animationLoop);</li>
<li> }</li>
</ol></div>

This example shows one very important good practice when doing animation and interaction: if you want to achieve a smooth animation, set the state variables 60 times/s inside the animation loop (lines 45-49), depending on increments you set in event listeners (lines 23-31).


__Example #2: draw in a canvas as if you were using a pencil__

[Online example](https://jsbin.com/tofiril/1/edit?html,output): ([Local Example - draw w/ pencil](src/4.3.3-example5.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5c8orsx')"
    src    ="https://tinyurl.com/y2rur2jt"
    alt    ="paint in a canvas"
    title  ="paint in a canvas"
  />
</figure>


Source code:

<div><ol>
<li value="1">...</li>
<li> &lt;script&gt;</li>
<li> var canvas, ctx, previousMousePos;</li>
<li>...</li>
<li> function drawLineImmediate(x1, y1, x2, y2) {</li>
<li>&nbsp; &nbsp;&nbsp;// a line is a path with a single draw order</li>
<li>&nbsp; &nbsp;&nbsp;// we need to do this in this example otherwise</li>
<li>&nbsp; &nbsp;&nbsp;// at each mouse event we would draw the whole path</li>
<li>&nbsp; &nbsp;&nbsp;// from the beginning. Remember that lines</li>
<li>&nbsp; &nbsp;&nbsp;// normally are only usable in path mode</li>
<li>&nbsp; &nbsp; ctx.beginPath();</li>
<li>&nbsp; &nbsp; ctx.moveTo(x1, y1);</li>
<li>&nbsp; &nbsp; ctx.lineTo(x2, y2);</li>
<li>&nbsp; &nbsp; ctx.stroke();</li>
<li> }</li>
<li>&nbsp;</li>
<li> function handleMouseMove(evt) {</li>
<li>&nbsp; &nbsp; &nbsp;var mousePos = getMousePos(canvas, evt);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;// Let's draw some lines that follow the mouse pos</li>
<li>&nbsp; &nbsp; &nbsp;if (!started) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;previousMousePos = mousePos; // get the current mouse position</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;started = true;</li>
<li>&nbsp; &nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// We need to have two consecutive mouse positions before drawing a line</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;drawLineImmediate(previousMousePos.x, previousMousePos.y,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos.x,&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos.y);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="line-height: 1.6; background-color: #ffffff;">previousMousePos = mousePos;</span></li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> }</li>
<li></li>
<li>&nbsp;window.onload = function () {</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;started = false;</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;<strong>canvas</strong><strong>.addEventListener('mousemove', handleMouseMove, false);</strong></li>
<li> };</li>
<li> &lt;/script&gt;</li>
</ol></div>

We had to define a variable started=false; as we cannot draw any line before the mouse moved (we need at least two consecutive positions). This is done in the test at line 21.


__Example #3: same as example #2 but we draw only when a mouse button is pressed__

[Online example](https://jsbin.com/pizikal/1/edit?html,output):  ([Local Example - Draw w/ Mouse Pressed](src/4.3.3-example6.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5c8orsx')"
    src    ="https://tinyurl.com/y44zl9gx"
    alt    ="paint when mouse is pressed"
    title  ="paint when mouse is pressed"
  />
</figure>


We just added `mouseup` and `mousedown` listeners, extract from the source code:

<div><ol>
<li value="1"> function handleMouseMove(evt) {</li>
<li>&nbsp; &nbsp; &nbsp;var mousePos = getMousePos(canvas, evt);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;// Let's draw some lines that follow the mouse pos</li>
<li>&nbsp; &nbsp; &nbsp;<strong>if (painting) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;drawLineImmediate(previousMousePos.x, previousMousePos.y,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos.x,&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos.y);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;previousMousePos = mousePos;</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> }</li>
<li> </li>
<li> function clicked(evt) {</li>
<li>&nbsp; &nbsp; previousMousePos = getMousePos(canvas, evt);</li>
<li>&nbsp; &nbsp; <strong>painting </strong><strong>= true;</strong></li>
<li> }</li>
<li>&nbsp;</li>
<li> function released(evt) {</li>
<li>&nbsp; &nbsp; <strong>painting </strong><strong>= false;</strong></li>
<li> }</li>
<li>&nbsp;</li>
<li>&nbsp;window.onload = function () {</li>
<li>&nbsp; &nbsp; canvas = document.getElementById('myCanvas');</li>
<li>&nbsp; &nbsp; ctx = canvas.getContext('2d');</li>
<li>&nbsp; &nbsp; <strong>painting </strong><strong>= false;</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; canvas.addEventListener('mousemove', handleMouseMove, false);</li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mousedown', clicked);</strong></li>
<li>&nbsp; &nbsp; <strong>canvas</strong><strong>.addEventListener('mouseup', released);</strong></li>
<li> };</li>
</ol></div>


#### Knowledge check 4.3.3

1. What is the __correct__ way to get the mouse coordinates in a mousemove listener attached to a canvas, in the canvas coordinate system?

  a. There are multiple ways to get the mouse cursor coordinates: using the clientX and clientY properties of the event passed to the listener, using the event.pageX and event.pageY properties works too...<br/>
  b. Getting the mouse coordinate in the canvas coordinate system is not straightforward: we must take into account the position of the canvas into the page, the different CSS margins, etc.<br/>
  c. No problem: use the event.mouseX and event.mouseY properties.<br/>

  Ans: b<br/>
  Explanation:
    + Most of the time you need to work with the mouse position relative to the canvas, not to the window, so you must convert the coordinates between the window and the canvas. This will take into account the position of the canvas, and the CSS properties that may affect the canvas position (margin, etc.).
    + Fortunately, there exists a method for getting the position and size of any element in the page: `getBoundingClientRect()`.


### 4.3.4 Responsive canvas

Resizing a canvas can be tricky if we don't know a few rules that might not be easily guessed:

1. Changing the `width` or `height` property of a canvas in JavaScript erases its content and resets its context,
2. Using percentages (%) in the CSS `width` and `height` properties of a canvas does _not change its number of pixels/resolution_. Instead, it scales the existing pixels without erasing the content, giving a blurry effect when a canvas becomes larger, for example.

Before looking at how best to handle canvas resizing, let's see some examples below:


#### Examples

__Example #1: changing the size of a canvas on the fly erases its content!__

[Online example](https://jsbin.com/tukave/2/edit): ([Local Example - Resize Canvas and Erase Contents](src/4.3.4-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/y5f75scx"
    alt    ="canvas do not resize"
    title  ="canvas do not resize"
  />
</figure>

<div><ol>
<li value="1">&lt;script&gt;</li>
<li>...</li>
<li> function resizeCanvas() {</li>
<li>&nbsp; &nbsp; &nbsp;<strong>canvas</strong><strong>.width = 300;</strong></li>
<li> }</li>
<li>&nbsp;</li>
<li>&lt;/script&gt;</li>
<li>...</li>
<li>&lt;button <strong>onclick="resizeCanvas();</strong>"&gt;</li>
<li>&nbsp; &nbsp; Click this button to resize the canvas and erase it!</li>
<li>&lt;/button&gt;</li>
</ol></div>


__Example #2 : resize a canvas using CSS width and height properties with percentages__

This time we are using a similar example as above, but we removed the button for resizing it, and we set the size of the canvas to 100x100 pixels. Instead of drawing inside, we draw two lines that join the diagonals.

Here is the [online version](https://jsbin.com/wuxatud/1/edit?html,output):  ([Local Example - Origin](src/4.3.4-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 5vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/y3csv9ab"
    alt    ="small canvas 100x100 pixels with diagonals"
    title  ="small canvas 100x100 pixels with diagonals"
  />
</figure>


Then, we added this CSS rule. Try it [online](https://jsbin.com/johovo/1/edit?html,output) (resize the windows, you will see what happens): ([Local Example - Resize w/ CSS in percentage](src/4.3.4-example3.html))

It's the same example as before, just adding the CSS:

<div><ol>
<li value="1"> &lt;style&gt;</li>
<li>&nbsp; &nbsp;&nbsp;#myCanvas {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;border: 1px solid black;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>width</strong><strong>:100%</strong></li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li> &lt;/style&gt;</li>
</ol></div>

And the result shows clearly that the resolution is still the same, only the pixels are bigger! 

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/yxogntvd"
    alt    ="blurry canvas resized using CSS width=100%"
    title  ="blurry canvas resized using CSS width=100%"
  />
</figure>


Even bigger: 

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/y2mmbkrw"
    alt    ="blurry effect"
    title  ="blurry effect"
  />
</figure>


<div style="border: 1px solid red; margin: 20px; padding: 10px;">
<p style="text-align: center;"><em><strong><mark style="color: black; background-color: lightpink;">Best practice</mark>: <span style="color: #ff0000;">never use CSS percentages on a canvas width or height!</span></strong></em></p>
</div>


__Example #3: a responsive canvas using a resize listener +  a parent element__

This is the trick to create a really responsive canvas:

1. Embed it in a `<div>` or in any parent container,
2. Use CSS with percentages on the width and the height CSS properties __of the parent__,
3. Use a `resize` listener on the  parent of the canvas,
4. Change the `width` and `height` properties of the canvas <u>from the JavaScript resize listener function</u> (content will be erased),
5. Redraw the content, scaled accordingly to the size of the parent.

Yep, this is not a straightforward process...

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/y6sswlc9"
    alt    ="div and canvas inside. Div has CSS width=100% and height = 50%"
    title  ="div and canvas inside. Div has CSS width=100% and height = 50%"
  />
</figure>


HTML code:

<div><ol>
<li value="1"> <strong>&lt;div id="parentDiv"&gt;</strong></li>
<li>&nbsp; &nbsp;&nbsp;&lt;canvas id="myCanvas" width="100" height="100" &gt;&lt;/canvas&gt;</li>
<li> <strong>&lt;/div&gt;</strong></li>
</ol></div>

CSS code:

<div><ol>
<li value="1"> &lt;style&gt;</li>
<li>&nbsp; &nbsp;&nbsp;#parentDiv {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>width</strong><strong>:100%;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>height</strong><strong>:50%;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; margin-right: 10px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; border: 1px solid red;</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; canvas {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;border: 2px solid black;</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li> &lt;/style&gt;</li>
</ol></div>

JavaScript code for the resize event listener:

<div><ol>
<li value="1">function init() {</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;// IMPORTANT: there is NO WAY to listen to a DIV's resize</li>
<li>&nbsp; &nbsp;// listen to the window instead.</li>
<li>&nbsp; &nbsp;window.addEventListener('resize',&nbsp; &nbsp; &nbsp; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; resizeCanvasAccordingToParentSize, false);</li>
<li>&nbsp; &nbsp;...</li>
<li>}</li>
<li>&nbsp;</li>
<li> function resizeCanvasAccordingToParentSize() {</li>
<li>&nbsp; &nbsp; &nbsp;<strong>// adjust canvas size, take parent's size, this erases content</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong>canvas</strong><strong>.width = divcanvas.clientWidth;</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong>canvas</strong><strong>.height = divcanvas.clientHeight;</strong></li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp; &nbsp;// draw something, taking into account the new canvas size</li>
<li> }</li>
</ol></div>

See the [complete example](https://jsbin.com/quvapib/1/edit?html,output) that corresponds to the above code. ([Local Example - Resize Canvas w/ Listerner](src/4.3.4-example4.html))

Original window size:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/yyb9jb8d"
    alt    ="original size of canvas"
    title  ="original size of canvas"
  />
</figure>


We resize the window horizontally:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/y4xnda9d"
    alt    ="new size"
    title  ="new size"
  />
</figure>


__Example #4: the same example with the monster__

[Online example](https://jsbin.com/fayire/1/edit?html,output): ([Local Example - Resize Monster](src/4.3.4-example5.html))

Initial size:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/y5m8k2c3"
    alt    ="monster normal size"
    title  ="monster normal size"
  />
</figure>


When the canvas is resized, its width became smaller than the monster's size. We __scaled__ down the monster (using `ctx.scale`!)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 5vw;"
    onclick="window.open('https://tinyurl.com/y6alvpte')"
    src    ="https://tinyurl.com/y3of86e2"
    alt    ="monster scaled to fit"
    title  ="monster scaled to fit"
  />
</figure>


The code is very similar to the previous example, we just replaced `drawDiagonals()` by `drawMonster(...)`, and we added a test in the `drawMonster(...)` function for scaling the monster if it's bigger than the canvas width (look at lines 10-16), this is a common trick:

<div><ol>
<li value="1"> function drawMonster(x, y, angle, headColor, eyeColor) { </li>
<li>&nbsp; &nbsp; &nbsp;// GOOD PRACTICE: SAVE CONTEXT AND RESTORE IT AT THE END</li>
<li>&nbsp; &nbsp; &nbsp;ctx.save();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// Moves the coordinate system so that the monster is drawn</li>
<li>&nbsp; &nbsp; &nbsp;// at position (x, y)</li>
<li>&nbsp; &nbsp; &nbsp;ctx.translate(x, y);</li>
<li>&nbsp; &nbsp; &nbsp;ctx.rotate(angle);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;<strong>// Adjust the scale of the monster (200x200) if the canvas </strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong>// is too small</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong>if(canvas.width &lt; 200) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>var scaleX = canvas.width/200;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>var scaleY = scaleX;</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong>}</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong>ctx</strong><strong>.scale(scaleX, scaleY);</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// head</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillStyle=headColor;</li>
<li>&nbsp; &nbsp; &nbsp;ctx.fillRect(0,0,200,200);</li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li>}</li>
</ol></div>


#### Knowledge check 4.3.4

<pre>#myCanvas {
       border: 1px solid black;
       width:100%
}
</pre>

1. Using CSS % for resizing a canvas is?

  a. Ok<br/>
  b. Bad practice<br/>
  c. Recommended<br/>
  d. Not possible<br/>

  Ans: <span style="color: magenta;">b</span><br/>
  Explanation: Using % in CSS is <mark style="background-color: lightpink;">not recommended</mark>, and is considered a bad practice as this will modify the size of the canvas pixels and produce a blurry effect. If the size is increased, the resolution is kept the same, only with bigger pixels.


### 4.3.5 Advanced canvas

The canvas API is a "big beast", and we have presented all the essential techniques for drawing and animating. However, we could not fit everything in this course. Exotic features that are rarely used by developers, or advanced techniques that require more than 20 lines of JavaScript, have been put aside for the [W3Cx HTML5 Apps and Games course](https://www.edx.org/course/html5-apps-and-games).

In that course, you will learn:

+ __Techniques useful for writing HTML5 games:__ time-based animation, advanced user interactions (detecting multiple keys plus mouse plus gamepad plus touch events all at the same time in a single version of the code), sprite based animation, collision detection, particle animation;
+ __Pixel-level operations:__ special FX like blue-screen videos and augmented reality;
+ __And many other things, such as:__ masking/clipping, stacking canvases in layers, composition modes, saving and restoring canvas contents, saving canvas content to disk client-side, drawing a canvas into a canvas, etc.

#### Examples studied in the HTML5 advanced course

+ __Small game framework / object oriented JavaScript / advanced event handling / collision detection / time based animation__ - see [example online](https://jsbin.com/jifutoj/1/edit?html,js,console,output).
+ __Sprite based animation:__ like this [one](https://jsbin.com/libakum/1/edit?html,js,console,output) (this is ugly code to demonstrate the principle - in the course we develop a clean, sprite animation framework). Use the arrow keys after clicking in the canvas. It's better to try in standalone mode (click on the small black arrow in the top right of the JSBin window).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4s3gtss')"
    src    ="https://tinyurl.com/y2xhunvy"
    alt    ="sprite sheet"
    title  ="sprite sheet"
  />
</figure>


### 4.3.6 Discussion, projects and a challenge!

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects, and a challenge!!


#### Suggested topics

+ Did you already know about event handling in JavaScript or was this new to you?
+ How can we more efficiently handle multiple key presses together with mouse button clicks, mouse moves, etc? The course gives all the basics but there may be other more elegant ways.
+ Did you know about [Gamepad API](https://www.w3.org/TR/gamepad/)? [Read this](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API/Using_the_Gamepad_API) if you want to try it. 
+ How do we make a responsive game that works in a canvas?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy):__ Make one of your drawings move in all directions (left, right up, down, then diagonals) using the arrow keys.
+ __Project 2 (a bit harder):__ Make an animated chart. When the page is loaded, the chart "grows" until the chart bars reach  their "normal" value. Another variant is to use animated colors or shadows in your chart.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y4exujpc')"
    src    ="https://tinyurl.com/y2shoemt"
    alt    ="animated by graph simple"
    title  ="animated by graph simple"
  />
</figure>


Animated bar graph (very simple JS code) by Grant Winney, a student from a previous run of this course. [Try it on JsBin](https://jsbin.com/sabuwof/1/edit?html,js,output).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y4exujpc')"
    src    ="https://tinyurl.com/y25qvbn6"
    alt    ="animlated bar graph"
    title  ="animlated bar graph"
  />
</figure>


Animated bar graph by David Neil. [Try it on JsBin](https://jsbin.com/vuxotu/edit?js,output). A little more complex as it comes with more features (labels, etc).

+ <span style="color: magenta; font-weight: bold;">We have a "Snake" challenge for you, look at the bottom of this page!!</span>
+ __Project 3 (a bit harder):__ Make your monster follow the mouse + open its mouth and change color when we click on a mouse button. If you manage to make it scream, it's even better (use a hidden audio element and call `play()`. Advanced users may want to take a look at the [howler.js JavaScript library](https://howlerjs.com/) that loads sound samples in memory and plays them on demand).
+ __Project 4 (advanced):__ On the Web, look for JavaScript functions for detecting collisions (circle/circle or rectangle/rectangle), and try to make a small game in which your monster must "eat" some balls that bounce on the screen. Every 5s new balls appear on the canvas. Make your monster go towards the mouse pointer. You can use `var angle = Math.atan2(dy, dx);` in order to compute the monster angle, dx and dy = difference between the monster and mouse positions.
+ __Project 5 (easy to intermediate):__ Put into practice what you've learned about the responsive canvas and develop an example of your own. The difficulty may vary depending on the things that are drawn or animated.


#### The "Snake" challenge

Just for fun, and for those of you who like a challenge, I adapted a small snake animation from a version written in processing to HTML5 / canvas / requestAnimationFrame. 

[Try it on JsBin!](https://jsbin.com/capace/edit?html,js,console,output)

Please make some improvements to the snake by adding a nice head and tail, changing the colors, adding a background, etc. Be creative and tweak this according to your artistic taste :-) 

Please post your creations and comments in the discussion forum below: there is a dedicated thread for that!

It's also a very interesting example that shows the power of 2D transformations + interesting use of `ctx.save()` / `ctx.restore()`, as each segment of the snake is always drawn at a fixed position: only the coordinate system of the previous segment is translated/rotated -> no complicated computations!

The challenge is on! I hope you'll enjoy it!A nicer snake with textures

What you could try:

+ Be creative!
+ Add some interesting features (forked tongue, head, tail, snake tortoise shells...), longer, faster, slower, drunk, etc
+ Make the snake chase the mouse (the snakes moves slower, so it tries to follow the mouse)
+ Animate not one snake, but many
+ Make a game of it
+ You can just change the loop of drawSnake to reverse the stacking order of segments. Try with this:another small nice snake `for(var i=x.length-1; i >=0; i--)` in `drawSnake()`

As shown in [this example](https://jsbin.com/sopiget/1/edit?html,js,console,output), if the snake's body crosses over itself, it will pass "on top", not "under", __producing a nice "elastic effect". Do you understand why this effect is produced?__

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y4exujpc" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y2t4s86r" 
      alt  ="Small snake example" 
      title="Small snake example"
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/yyltqkta" 
      alt  ="Brown snake challeneg" 
      title="Brown snake challeneg"
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/yx8uhtaa" 
      alt  ="green snake challenge" 
      title="green snake challenge"
    >
  </a>
</div>


