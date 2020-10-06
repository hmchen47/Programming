# Week 4: HTML5 Animations


## 4.2 Basic animation techniques


## 4.2.1 Lecture Notes

+ [Animation techniques](421-animation-techniques)
  + basic steps to perform an animation
    + clear the content of the canvas w/ `ctx.clearRect(0, 0, canvasWidth, canvasHeight)` method
    + draw some shapes by using any drawing methods
    + move the shapes by modifying the positions and/or orientation, size, and color
    + repeat the first step
  + perform in a canvas
  + principle: __clear-draw-move-repeat__
  + possible ignore the first step if redrawing the whole canvas content
  
+ [Animations before HTML5](#before-html5)
  + using CSS backgrounds inside `<div>` elements
  + change the CSS top, left, width, and height properties if the divs
  + only solutions: `setInterval(function, ms)` & `setTimeout(function, ms)`: 
  + `setInterval(function, ms)`: run every $n$ milliseconds
  + `setTimeout(function, ms)`: run only once  after $n$ milliseconds (the last step above)

+ [Animation after HTML5](#after-html5)
  + the `<canvas>` element introduced
  + `requestAnimationFrame` API
    + tell the browser to perform an animation
    + request the browser calls a specified function to update an animation before the next repaint
    + take a callback as an argument to be invoked before the repaint




### 4.2.1 Animation techniques

In order to perform an animation, we need to:

1. Clear the content of the canvas: this can be done using the `ctx.clearRect(0, 0, canvasWidth, canvasHeight)` method;
2. Draw some shapes: use any of the drawing methods we have seen so far;
3. Move the shapes: modify the position and/or orientation, size and color of the shapes;
4. Repeat (go to step 1).

These are the basic steps for animating objects in a canvas. The order of the steps can be changed (i.e. you can move the shapes before drawing them), but, the principle is the same: __clear-draw-move-repeat__.

Step 1 could be avoided if you redraw the whole canvas content during step 2.


#### Before HTML5

Even before HTML5 and the introduction of the canvas element, people created HTML games. They used CSS backgrounds inside `<div>` elements, and used to change the CSS top, left, width and height properties of the divs to animate graphic images on the screen.

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

  Ans: b<br/>
  Explanation: Indeed, before HTML5, and with the arrival of JavaScript, it became possible, using functions such as `setInterval` or `setTimeout`, to modify CSS properties of HTML objects in real time, and in a repeated manner. Animation loops could be implemented using this technique. Now, the HTML5 canvas and the new requestAnimationFrame API make drawing and animating easier, with better performance.


### 4.2.2 Basic animation techniques


<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V001700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/>

[Transcript](https://tinyurl.com/y2vunzbl)


See the [online example](https://jsbin.com/nikimovuza/1/edit?html,output) shown in the video, with source code. ([Local Example - Basic Animations](src/4.2.2-example1.html))

Errata: in the video, we use `speed +=1;` in order to increment the speed of the rectangle each time it bounces (in the `changeColor()` function). This is not correct as `speed` can be negative. The online example fixes this by using `speed += Math.sign(speed) * 1;` instead this will add +1 or -1 depending on the sign of `speed`.






