# Week 4: HTML5 Animations


## 4.3 Canvas and user interaction


### 4.3.0 Lecture Notes

+ [DOM events](#431-events-input-and-output)
  + use the DOM JavaScript API to create event handlers
  + js: events made by users as an input and manipulating the DOM structure as an output
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
      + e.g.,: `document.getElementById('someDiv').addEventListener('click', function(evt) { alert('clicked!'); }, false);`
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
  + keyup listerner: `window.addEventListener('keyup', handleKeyup, false);`
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
    + `mouseup` and `mousedown` events: a user presses or releases any mouse button
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

  + example: move charater w/ mouse and rotate w/ buttom pressed
    + mouse listeners: `canvas.addEventListener('mousemove', handleMousemove, false); canvas.addEventListener('mousedown', handleMousedown, false); canvas.addEventListener('mouseup', handleMouseup, false);`
    + start the animation: `equestId = requestAnimationFrame(animationLoop);`
    + the mousePos will be taken into account in the animationLoop: `mousePos = getMousePos(canvas, evt);`
    + mousePos taken into account in the animationLoop: `function handleMousemove(evt) { mousePos = getMousePos(canvas, evt); }`
    + increment on the angle taken into account in the animationLoop: `function handleMousedown(evt) { incrementAngle = 0.1; }`
    + stop the rotation: `function handleMouseup(evt) { incrementAngle = 0; }`
    + get mouse position in canvas: `function getMousePos(canvas, evt) {...}`
    + `animationLoop` function: `function animationLoop() {...}`
      + clear:; `ctx.clearRect(0, 0, canvas.width, canvas.height);`
      + draw: `drawMonster(monsterX, monsterY, monsterAngle, 'green', 'yellow');`
      + move if in canvas: `if(mousePos !== undefined) { monsterX = mousePos.x; monsterY = mousePos.y; monsterAngle += incrementAngle; }`
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

    + onload fucntion after loading page: ` window.onload = function () {...}`
      + unable to draw any line before mouse moved into canvas: `started = false;`
      + listen to tne movment of mouse: ` canvas.addEventListener('mousemove', handleMouseMove, false);`
  + example: draw only when mouse button pressed
    + event listeners: `canvas.addEventListener('mousemove', handleMouseMove, false); canvas.addEventListener('mousedown', clicked); canvas.addEventListener('mouseup', released);`
    + press mouse button: `function clicked(evt) {previousMousePos = getMousePos(canvas, evt); painting = true;}`
    + release mouse button: `function released(evt) { painting = flase; }`
    + draw lines following the mouse position: `function handleMouseMove(evt) {...}`

+ [Responsive canvas](#434-responsive-canvas)
  + rules of resizing a canvas
    + changing `width` and `height` property $\to$ erase the content and reset the context
    + using `%` in the CSS `width` and `height` properties of a canvas $\to$ scaling the existing pixels w/o erasing the content, given a blurry image
  + __best practice__: never use CSS percentage on a canvas width or height
  + responsive canvas
    + embedded in a `<div>` or in any parent container
    + using CSS w/ percentages on the width and the height CSS properties of the parent
    + using a `resize` listerner on the parent of the canvas
    + changing the `weight` and `height` properties of the canvas from the JS resize listener function
    + redraw content, scaled accordingly tot he size of the parent
  + example: resize canvas
    + HTML code: `<div id="parentDiv"> <canvas id="myCanvas" width="100" height="100" ></canvas> </div>`
    + CSS code for `<div>` resize: `#parentDiv { width:100%; height:50%; margin-right: 10px; border: 1px solid red; }`
    + unable to listen to a DIV's resize byt listen to the window instead: `window.addEventListener('resize',     resizeCanvasAccordingToParentSize, false);`
    + adjust canvas size, take parent's size, this erases content: `canvas.width = divcanvas.clientWidth; canvas.height = divcanvas.clientHeight;`
    + resize character w/ `ctx.resize()` in draw fucntion: `function drawMonster(x, y, angle, headColor, eyeColor) {...}`
      + save and restore at begining and end of function
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


### 4.3.1 Events: input and output

In JavaScript, we treat events made by users as an input, and we manipulate the DOM structure as an output. Most of the time in games/animations, we will change state variables of moving objects, such as position or speed of an alien ship, and the animation loop will take care of these variables to move the objects.

The events are called DOM events, and we use the _DOM JavaScript API_ to create _event handlers_.


#### There are three ways to manage events in the DOM structure

__First way: declare event handlers in the HTML code__

You will often find this in examples on the Web:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"someDiv"</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">);</span><span class="atv">"</span></strong><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; content of the div </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/div&gt;</span></li>
</ol></div>

Note: this is not the recommended way to handle events, even if it's very easy to use. Mixing the 'visual layer' (HTML) and the 'logic layer' (JavaScript) in one place is ok for small examples (we have used this in some examples in this course) but is not the recommended way for full scale applications where a clean separation is best.


__Second way: add an event handler to an HTML element in JavaScript__

Here is an example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'someDiv'</span><span class="pun">).</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(evt)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

This method is fine, but  you will not be able to attach several listener functions. If you need to do this, the preferred version is the next one.


__Third way: register a callback to the event listener with the `addEventListener` method__

This is how we do it:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'someDiv'</span><span class="pun">).</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(evt)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'clicked!'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div>

The third parameter is not important for now, just set it to `false`, or simply do not add a third parameter.


#### The DOM event that is passed to the event listener function

When you create an EventListener and attach it to an element,  an event object will be passed as a parameter to your callback, just like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">element</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><strong><span class="kwd">event</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// now you can use the event object inside the callback</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div>

Depending on the type of event you are listening to, we will use different properties from the event object in order to get useful information like: "what keys have been pressed down?", "what is the position of the mouse cursor?", "which mouse button is down?", etc.

Let's see next how to deal with the keyboard and the mouse. In the [W3Cx HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games) course, we look at additional APIs such as the [gamePad API](https://www.w3.org/TR/gamepad/) for using USB or wireless gamepads/joysticks/game controllers.


#### Knowledge check 4.3.1

Source code for the knowledge check 4.3.1

[Online example on JS Bin](http://jsbin.com/korele/edit)

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Click on button</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myButton"</span><span class="tag">&gt;</span><span class="pln">Click me!</span><span class="tag">&lt;/button&gt;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> button </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myButton'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;<strong>// Define a click listener on the button</strong></span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;button</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> processClick</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// callback</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> processClick</span><span class="pun">(</span><strong><span class="pln">event</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Button clicked"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><strong><span class="com">// What is the event parameter?</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


1. When you create an event listener like in the code above, what is the event parameter (line 15) passed to the callback function useful for?

  a. It will hold relevant data about the interaction (element that fired the event, key code, mouse button and position of the mouse cursor, etc.)<br/>
  b. It's not useful, it's just here for debug purposes.<br/>

  Ans: a<br/>
  Explanation: The event is useful for getting information about what fired the event, button, mouse, etc... The data it holds depends on the type of the event. This [example shows how we can get the id of the button that has been clicked and the value of the button label](https://jsbin.com/ruzofa/edit).



### 4.3.2 Keyboard interaction, key events

This has been a bit of a nightmare for years, as different browsers have had different ways of handling key events and key codes (read [this article](https://unixpapa.com/js/key.html) if you are fond of JavaScript archeology). Fortunately it's much better today, and we are able to rely on methods that should work on any browser.

When you listen to keyboard related events (`keydown`, `keyup` or `keypressed`), the event parameter passed to the listener function will contain the code of the key that fired the event. Then it is possible to test what key has been pressed or released, like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><strong><span class="kwd">event</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">//left arrow was pressed</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"350"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// This will work when you press a key, anywhere on the document</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>window</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> handleKeydown</span><span class="pun">(</span><span class="pln">e</span><span class="pun">){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">'keycode: '</span><span class="pun">+</span><span class="pln">e</span><span class="pun">.</span><span class="pln">keyCode</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><strong><span class="pln"> monsterX</span><span class="pun">=</span><span class="lit">100</span></strong><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">=</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><strong><span class="pln"> incrementX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span></strong><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 1 - Get the canvas</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 2 - Get the context</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// 3 add key listeners to the window element</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>window</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>window</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> handleKeyup</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 4 - start the animation</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><strong><span class="pln"> handleKeydown</span><span class="pun">(evt</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><strong><span class="pln">evt</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">37</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="com">//left key </span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong>incrementX </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><strong><span class="pln">evt</span><span class="pun">.</span><span class="pln">keyCode </span><span class="pun">===</span><span class="pln"> </span><span class="lit">39</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="com">// right key</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong>incrementX </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><strong><span class="pln"> handleKeyup</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>incrementX </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 1 - Clear</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 2 Draw</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawMonster</span><span class="pun">(</span><span class="pln">monsterX</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// 3 Move</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>monsterX </strong></span><strong><span class="pun">+=</span><span class="pln"> incrementX</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// call again mainloop after 16.6 ms (60 frames/s)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
</ol></div>


__Example #2: what if I want to listen to key events only in my canvas?__

If you add a key listener to a canvas element, the problem is that it will get events only when it has the focus. And by default, it will never have the focus!

The `tabindex` attribute of the canvas element makes it focusable. Without it, it will never get the focus!

The trick is to declare the canvas like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"350"</span><span class="pln"> </span><strong><span class="atn">tabindex</span><span class="pun">=</span><span class="atv">"1"</span></strong><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/canvas&gt;</span></li>
</ol></div>

And we force the canvas to get the focus with:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">canvas</span><span class="pun">.</span><span class="pln">focus</span><span class="pun">();</span></strong></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;canvas</span><span class="pun">=</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// This will work only if the canvas has the focus </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="com">// We can set the focus on the canvas like this:</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="com">//canvas.focus();</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// ... but it will stop working if we click somewhere else</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// in the document</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> handleKeydown</span><span class="pun">(</span><span class="pln">e</span><span class="pun">){</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'keycode: '</span><span class="pun">+</span><span class="pln">e</span><span class="pun">.</span><span class="pln">keyCode</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - Get the canvas</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2 - Get the context</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 3 - Add key listeners to the window element</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keydown'</span><span class="pun">,</span><span class="pln"> handleKeydown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'keyup'</span><span class="pun">,</span><span class="pln"> handleKeyup</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseenter'</span><span class="pun">,</span><span class="pln"> setFocus</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseout'</span><span class="pun">,</span><span class="pln"> unsetFocus</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 4 - Start the animation</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> setFocus</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">focus</span><span class="pun">();</span></strong><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> unsetFocus</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">blur</span><span class="pun">();</span></strong><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pun">&nbsp; </span><span class="pun">&nbsp;</span><span style="color: #222222; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 14px; line-height: 20.72px;">incrementX = 0; // stop the monster if the mouse exists the canvas</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
</ol></div>

The third parameter (false) of _lines 12_ and _13_ means "we do not want to propagate the event to the ancestors of the canvas in the DOM." 


#### Knowledge check 4.3.2

1. Suppose we have defined a key event listener to a canvas: should this canvas have the focus in order to fire key events? (Yes/No)

  Ans: <span style="color: magenta;">Yes</span>, xNo<br/>
  Explanation: The problem with adding a key listener to a canvas element is that it will get events only when the canvas has the focus. And by default, it will never have the focus! The course shows how to handle different cases.



### 4.3.3 Mouse interaction, mouse events

Detecting mouse events in a canvas is quite straightforward: you add an event listener to the canvas, and the browser invokes that listener when the event occurs.

The example below is about listening to `mouseup` and `mousedown` events (when a user presses or releases any mouse button):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// do something with&nbsp;to the mousedown event</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">});</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>mousePos </strong></span><strong><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> message </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Mouse position: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">','</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;</strong></span><strong><span class="com">//&nbsp;WRONG!!!</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>x</strong></span><strong><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientX</span><span class="pun">,</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>y</strong></span><strong><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientY</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// necessary to take into account CSS boundaries</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getBoundingClientRect</span><span class="pun">();</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; x</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientX </span><strong><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">left</span><span class="pun">,</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; y</span><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientY </span><strong><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">top</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">,</span><span class="pln"> mousePos</span><span class="pun">,</span><span class="pln"> mouseButton</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>mousePos </strong></span><strong><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> message </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Mouse position: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">','</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedown'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>mouseButton </strong></span><strong><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">button</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> message </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Mouse button "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">button </span><span class="pun">+</span><span class="pln"> </span><span class="str">" down at position: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">','</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseup'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> message </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Mouse up at position: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> </span><span class="str">','</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span>&nbsp;</li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> writeMessage</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">'18pt Calibri'</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'black'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="pln">message</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">25</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// necessary to take into account CSS boudaries</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;</strong></span><strong><span class="kwd">var</span><span class="pln"> rect </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getBoundingClientRect</span><span class="pun">();</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>x</strong></span><strong><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientX </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">left</span></strong><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>y</strong></span><strong><span class="pun">:</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">clientY </span><span class="pun">-</span><span class="pln"> rect</span><span class="pun">.</span><span class="pln">top</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><strong><span class="pln"> monsterX</span><span class="pun">=</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">=</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">=</span><span class="lit">0</span></strong><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> incrementX </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><strong><span class="pln"> incrementAngle </span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> mousePos</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 3bis - Add mouse listeners</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> handleMousemove</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedown'</span><span class="pun">,</span><span class="pln"> handleMousedown</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseup'</span><span class="pun">,</span><span class="pln"> handleMouseup</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 4 - Start the animation</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><strong><span class="pln"> handleMousemove</span></strong><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com"><strong>// The mousePos will be taken into account in the animationLoop</strong></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>mousePos </strong></span><strong><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> handleMousedown</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// the increment on the angle will be</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// taken into account in the animationLoop</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>incrementAngle </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="lit">0.1</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><strong><span class="pln"> handleMouseup</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>incrementAngle </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">; &nbsp;// stops the rotation</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;... // same as before</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> animationLoop</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 1 - Clear</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 2 - Draw</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;drawMonster</span><span class="pun">(</span><span class="pln">monsterX</span><span class="pun">,</span><span class="pln"> monsterY</span><span class="pun">,</span><span class="pln"> monsterAngle</span><span class="pun">,</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// 3 - Move</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">if</span><span class="pun">(</span><span class="pln">mousePos </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ // test necessary, maybe the mouse is not yet on canvas</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>monsterX </strong></span><strong><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>monsterY </strong></span><strong><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>monsterAngle </strong></span><strong><span class="pun">+=</span><span class="pln"> incrementAngle</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// call again mainloop after 16.6 ms (60 frames/s)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestId </span><span class="pun">=</span><span class="pln"> requestAnimationFrame</span><span class="pun">(</span><span class="pln">animationLoop</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">,</span><span class="pln"> previousMousePos</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;">...</li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawLineImmediate</span><span class="pun">(</span><span class="pln">x1</span><span class="pun">,</span><span class="pln"> y1</span><span class="pun">,</span><span class="pln"> x2</span><span class="pun">,</span><span class="pln"> y2</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// a line is a path with a single draw order</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// we need to do this in this example otherwise</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// at each mouse event we would draw the whole path</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// from the beginning. Remember that lines</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// normally are only usable in path mode</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="pln">x1</span><span class="pun">,</span><span class="pln"> y1</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">x2</span><span class="pun">,</span><span class="pln"> y2</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> handleMouseMove</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> mousePos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Let's draw some lines that follow the mouse pos</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(!</span><span class="pln">started</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;previousMousePos </span><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">; // get the current mouse position</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;started </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// We need to have two consecutive mouse positions before drawing a line</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;drawLineImmediate</span><span class="pun">(</span><span class="pln">previousMousePos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> previousMousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pln" style="line-height: 1.6; background-color: #ffffff;">previousMousePos </span><span class="pun" style="line-height: 1.6; background-color: #ffffff;">=</span><span class="pln" style="line-height: 1.6; background-color: #ffffff;"> mousePos</span><span class="pun" style="line-height: 1.6; background-color: #ffffff;">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;">&nbsp; &nbsp;...</li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;started </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> handleMouseMove</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> handleMouseMove</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> mousePos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Let's draw some lines that follow the mouse pos</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">painting</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;drawLineImmediate</span><span class="pun">(</span><span class="pln">previousMousePos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> previousMousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos</span><span class="pun">.</span><span class="pln">x</span><span class="pun">,</span><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;mousePos</span><span class="pun">.</span><span class="pln">y</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;previousMousePos </span><span class="pun">=</span><span class="pln"> mousePos</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> clicked</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; previousMousePos </span><span class="pun">=</span><span class="pln"> getMousePos</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">,</span><span class="pln"> evt</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>painting </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> released</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>painting </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>painting </strong></span><strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousemove'</span><span class="pun">,</span><span class="pln"> handleMouseMove</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mousedown'</span><span class="pun">,</span><span class="pln"> clicked</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'mouseup'</span><span class="pun">,</span><span class="pln"> released</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> resizeCanvas</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">width </span><span class="pun">=</span><span class="pln"> </span><span class="lit">300</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">resizeCanvas</span><span class="pun">();</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Click this button to resize the canvas and erase it!</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;style&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">#myCanvas {</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong>width</strong></span><strong><span class="pun">:</span><span class="lit">100</span><span class="pun">%</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/style&gt;</span></li>
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
<p style="text-align: center;"><em><strong>BEST PRACTICE: <span style="color: #ff0000;">never use CSS percentages on a canvas width or height!</span></strong></em></p>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><strong><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"parentDiv"</span><span class="tag">&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"100"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"100"</span><span class="pln"> </span><span class="tag">&gt;</span>&lt;/canvas&gt;</li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;/div&gt;</span></strong></li>
</ol></div>

CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;style&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">#parentDiv {</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>width</strong></span><strong><span class="pun">:</span><span class="lit">100</span><span class="pun">%;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>height</strong></span><strong><span class="pun">:</span><span class="lit">50</span><span class="pun">%;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; margin</span><span class="pun">-</span><span class="pln">right</span><span class="pun">:</span><span class="pln"> </span><span class="lit">10px</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid red</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/style&gt;</span></li>
</ol></div>

JavaScript code for the resize event listener:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// IMPORTANT: there is NO WAY to listen to a DIV's resize</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// listen to the window instead.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'resize'</span><span class="pun">,</span><span class="pln">&nbsp; &nbsp; &nbsp; </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; resizeCanvasAccordingToParentSize, false</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;...</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> resizeCanvasAccordingToParentSize</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="com">// adjust canvas size, take parent's size, this erases content</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">width </span><span class="pun">=</span><span class="pln"> divcanvas</span><span class="pun">.</span><span class="pln">clientWidth</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>canvas</strong></span><strong><span class="pun">.</span><span class="pln">height </span><span class="pun">=</span><span class="pln"> divcanvas</span><span class="pun">.</span><span class="pln">clientHeight</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// draw something, taking into account the new canvas size</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">,</span><span class="pln"> headColor</span><span class="pun">,</span><span class="pln"> eyeColor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// GOOD PRACTICE: SAVE CONTEXT AND RESTORE IT AT THE END</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Moves the coordinate system so that the monster is drawn</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// at position (x, y)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="com">// Adjust the scale of the monster (200x200) if the canvas </span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp;<strong>// is too small</strong></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="kwd">if</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">width </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">200</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="kwd">var</span><span class="pln"> scaleX </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">/</span><span class="lit">200</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="kwd">var</span><span class="pln"> scaleY </span><span class="pun">=</span><span class="pln"> scaleX</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="pun">}</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>ctx</strong></span><strong><span class="pun">.</span><span class="pln">scale</span><span class="pun">(</span><span class="pln">scaleX</span><span class="pun">,</span><span class="pln"> scaleY</span><span class="pun">);</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// head</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">headColor</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp;...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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

  Ans: 






