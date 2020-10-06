# Week 4: HTML5 Animations


## 4.2 Basic animation techniques


### 4.2.1 Animation techniques

In order to perform an animation, we need to:

1. Clear the content of the canvas: this can be done using the `ctx.clearRect(0, 0, canvasWidth, canvasHeight)` method;
1. Draw some shapes: use any of the drawing methods we have seen so far;
1. Move the shapes: modify the position and/or orientation, size and color of the shapes;
1. Repeat (go to step 1).

These are the basic steps for animating objects in a canvas. The order of the steps can be changed (i.e. you can move the shapes before drawing them), but, the principle is the same: __clear-draw-move-repeat__.

Step 1 could be avoided if you redraw the whole canvas content during step 2.


#### Before HTML5

Even before HTML5 and the introduction of the canvas element, people created HTML games. They used CSS backgrounds inside <div> elements, and used to change the CSS top, left, width and height properties of the divs to animate graphic images on the screen.

During the late 1990s and early 2000s, JavaScript became increasingly popular. The community created a first 'umbrella term' describing a collection of technologies used together to create interactive and animated Web sites - [DHTML (Dynamic HTML)](https://en.wikipedia.org/wiki/Dhtml). For example, check the [games developed at this time by Brent Silby](https://def-logic.com/) (they all use DHTML).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2wdoc4h')"
    src    ="https://tinyurl.com/yyfoxenr"
    alt    ="A mario like DHTML game"
    title  ="A mario like DHTML game"
  />
</figure>


For animation, the `setInterval(function, ms)` and `setTimeout(function, ms)` methods were the only solutions. Both methods take a function as the first parameter, and a number of milliseconds as the second parameter.

The only difference is that the code provided to `setInterval` will run every n milliseconds whereas the code in `setTimeout` will run only once after n milliseconds (meaning that we will have to repeat a call to `setTimeout` at step 4 above).


#### After HTML5

The methods described above are now completed by a new method that comes with multiple advantages: the `requestAnimationFrame` API.

We will compare the old methods with the new one, and implement the same  example with each of them to highlight the differences.


#### Knowledge check 4.2.1

1. Before HTML5, how did people write games?

  a. It was not possible.<br/>
  b. They used JavaScript for animating + the top, left, etc. CSS properties of HTML elements in the page. This set of tricks was called 'DHTML'.<br/>
  c. They used Flash, as it was not possible to draw graphics or perform an animation using Web standards such as HTML, CSS and JavaScript.<br/>

  Ans: 





