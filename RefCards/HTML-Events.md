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


## Keycode Values

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



