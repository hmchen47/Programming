# Module 2: Game programming with HTML5 section


## 2.2 Basic concepts of HTML5 game development

### 2.2.1 History of JavaScript games

There is a widely-held belief that games running in Web browsers and without the help of plugins are a relatively new phenomenon. This is not true: back in 1998, Donkey Kong ran in a browser. It was a game by Scott Porter, written using only standard Web technologies (HTML, JavaScript, and CSS) .

Just a few years after the Web was born, JavaScript appeared -  a simple script language with C-like syntax for interacting and changing the structure of documents - together with HTML, the [HyperText Markup Language](https://en.wikipedia.org/wiki/Html) used for describing text documents. For the first time, particular elements could be moved across a browser's screen. This was noticed by Scott Porter who, in 1998, created the first JavaScript game library with the very original name, 'Game Lib'. At this time, Porter focused largely on creating ports of old NES and Atari games using animated gifs, but he also developed a Video Pool game in which he emulated the angle of a cue with [a sprite of 150 different positions](https://bit.ly/3zoyhyW)!

During the late 1990s and early 2000s, JavaScript increased in popularity, and the community coined the term 'DHTML' ([Dynamic HTML](https://en.wikipedia.org/wiki/Dhtml)), which was to be the first umbrella term describing a collection of technologies used together to create interactive and animated Web sites. Developers of the DHTML era hadn't forgotten about Porter's 'Game Lib', and within a couple of years, Brent Silby presented 'Game Lib 2'. It is still possible to play many games created with that library on his Web site.

The DHTML era was a time when JavaScript games were as good as those made in Flash. Developers made many DOM libraries that were useful for game development, such as Peter Nederlof's Beehive with its outstanding [Rotatrix](https://peterned.home.xs4all.nl/games.html#rotatrix) (which, personally, I think is one of the best HTML games EVER). The first very polished browser games were also developed; Jacob Sidelin, creator of 14KB Mario, created [the very first page dedicated to JavaScript games](https://web.archive.org/web/20090519005306/http://www.javascriptgaming.com/).

And then came 2005: 'the year of [AJAX](https://en.wikipedia.org/wiki/Ajax_%28programming%29)'. Even though 'AJAX' just stands for 'Asynchronous JavaScript and XML', in practice it was another umbrella term describing methods, trends and technologies used to create a new kind of Web site - [Web 2.0](https://en.wikipedia.org/wiki/Web_2.0).

Popularization of new JavaScript patterns introduced the ability to create multiplayer connections or even true emulators of old computers. The best examples of this time were '[Freeciv](https://play.freeciv.org/)' by Andreas Rosdal - a port of Sid Meier's Civilization, and [Sarien.net](http://sarien.net/) by Martin Kool, an emulator of old Sierra games. 

And now we are entering a new era in the history of the Web: "HTML5"!


### 2.2.2 Elements and APIs useful for writing games

In the [W3Cx HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) course, we study the canvas, drawing, and animation elements. These are going to be revisited in more details in this section.

Here, we present some elements that are useful in writing games.

#### Drawing: the `<canvas>` element

The `<canvas>` is a new HTML element described as "_a resolution-dependent bitmap canvas which can be used for rendering graphs, game graphics, or other visual images on the fly._" It's a rectangle included in your page where you can draw using scripting with JavaScript. It can, for instance, be used to draw graphs, make photo compositions or do animations. This element comprises a drawable region defined in HTML code with `height` and `width` attributes.

You can have multiple canvas elements on one page, even stacked one on top of another, like transparent layers. Each will be visible in the DOM tree and has it's own state independent of the others. It behaves like a regular DOM element.

The canvas has [a rich JavaScript API](https://www.w3.org/TR/2dcontext/) for drawing all kinds of shapes; we can draw wireframe or filled shapes and set several properties such as color, line width, patterns, gradients, etc. It also supports transparency and pixel level manipulations. It is supported by all browsers, on desktop or mobile phones, and on most devices it will take advantage of hardware acceleration. 

It is undoubtedly the most important element in the HTML5 specification from a game developer's point of view, so we will discuss it in greater detail later in the course.

The W3C [HTML Working Group](https://www.w3.org/html/wg/) published [HTML Canvas 2D Context](https://www.w3.org/TR/2dcontext/) as W3C Recommendation (i.e., Web standard status).


#### Animating at 60 fps: the requestAnimationFrame API

The `requestAnimationFrame` API targets 60 frames per second animation in canvases. This API is quite simple and also comes with a high resolution timer. Animation at 60 fps is often easy to obtain with simple 2D games on major desktop computers. This is the preferred way to perform animation, as the browser will ensure that animation is not performed when the canvas is not visible, thus saving CPU resources.


#### Videos and animated textures: the `<video>` element

The HTML5 `<video>` element was introduced in the HTML5 specification for the purpose of playing streamed videos or movies, partially replacing the object element.  The JavaScript API is nearly the same as the one of the `<audio>` element and enables full control from JavaScript.

By combining the capabilities of the `<video>` and `<canvas>` elements, it is possible to manipulate video data to incorporate a variety of visual effects  in real time, and conversely, to use images from videos as "animated textures" over graphic objects.


#### Audio : the `<audio>` element and the Web Audio API

__The `<audio>` element__

`<audio>` is an HTML element that was introduced to give a consistent API for playing streamed sounds in browsers. File format support varies between browsers, but MP3 works in nearly all browsers today. Unfortunately, the `<audio>` element is only for streaming compressed audio, so it consumes CPU resources, and is not adapted for sound effects where you would like to change the playing speed or add real time effects such as reverberation or doppler. For this, [the Web Audio API](https://www.w3.org/TR/webaudio/) is preferable.


__The Web Audio API__

This is a 100% JavaScript API designed for working in real time with uncompressed sound samples or for generating procedural music. Sound samples will need to be loaded into memory and decompressed prior to being used. Up to 12 sound effects are provided natively by browsers that support the API (all major browsers except IE, although Microsoft Edge supports it).


#### Interacting: dealing with keyboard and mouse events, the GamePad API

User inputs will rely on several APIs, some of which are well established, such as the DOM API that is used for keyboard, touch or mouse inputs. There is also a [Gamepad API](https://www.w3.org/TR/gamepad/) (in W3C Working Draft status) that is already implemented by some browsers, which we will also cover in this course. The Gamepad specification defines a low-level interface that represents gamepad devices.

#### Multi-participants feature: WebSockets

<div style="color: pink">IMPORTANT INFORMATION: NOT COVERED IN THIS COURSE</div>

Using [the WebSockets technology](https://fr.wikipedia.org/wiki/WebSocket) (which is not part of HTML5 but comes from the W3C [WebRTC](https://www.w3.org/TR/webrtc/) specification - "Real-time Communication Between Browsers"), you can create two-way communication sessions between multiple browsers and a server. The WebSocket API, and useful libraries built on top of it such as [socket.io](https://socket.io/), provide the means for sending messages to a server and receiving event-driven responses without having to poll the server for a reply.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open("https://bit.ly/3iHzWtq")"
    src    = "https://bit.ly/3xnz3KU"
    alt    = "a graph showing several clients interacting with a websocket server"
    title  = "a graph showing several clients interacting with a websocket server"
  />
</figure>


#### Notes for 2.2.2 Elements and APIs useful for writing games

+ Drawing
  + `<canvas>` element
    + a new HTML element
    + a resolution-dependent bitmap canvas used for rendering graphs, game graphs, or orther images on-the-fly
    + rectangle shape able to draw by using scripting w/ JavaScript
    + a drawable region defined w/ `height` and `width` attributes
  + multiple canvas on one page
    + possible stacked one on top of another, such as transpreant layer
    + visible in the DOM tree
    + one's state independent of the others
  + a rich JavaScript API
    + all kind of shapes
    + wireframe or filled shapes
    + properties: color, line width, patterns, gradient, etc.
    + transparency and pixel level manipulation
    + supported by all browsers, on desktop or mobile phones, and on most devices

+ Animation
  + `requestAnimationFrame` API
    + targeting 60 fps in canvases
    + w/ high resolution timer
  + 60 fps: easy to obtain w/ simple 2D games on major desktop commputers
  + preferred way to perform animation
  + no animation performed if not visible $\to$ saving CPU resources

+ Video and animated texture
  + `<video>` element
    + playing streaming videos or movies
    + partially replacing the object element
  + JavaScript API
    + nearly the same as the one of the `<audio>` element
    + enabling full control from JavaScript
  + combining the capabilities of the `<video>` and `<canvas>` elements
    + possible to maipulate video data to incorporate a variety of visual effects in real time
    + possible to use images from video as "animated textures" over graphic object

+ Audio
  + the `<audio>` element
    + an HTML element
    + introduced to give a consistent API for playing streamed sounds in browsers
    + file format support varying btw browsers
    + MP3 working nearly all browsers
    + only for streaming compressed audio $\implies$ consuming CPU resources
    + no sound effects, such changing speed and real-time effect
  + the Web Audio API
    + a 100\% JavaScript API designed for working in real-time w/ uncompressed sound samples or for generating procedural music
    + sound samples loaded into memory and decompressed prior to being used
    + up to 12 sound effects natively provided by browsers

+ Interaction
  + user input replying on several APIs
  + DOM API used for keyboard, touch, or mouse inputs
  + GamePad API (working draft)
    + define a low-level interface representing gamepad devices
    + already implemented by some browsers

+ Multiple participants: Websockets
  + not part of HTML5 but W3C [WebRTC](https://www.w3.org/TR/webrtc/) specification, "Real-time Communication between Browsers"
  + creating two-way communication sessions btw multiple browsers and a server
  + [socket.io](https://socket.io/): useful libraries built on top of Websocket API
  + [Websockets](https://fr.wikipedia.org/wiki/WebSocket): providing the means for sending messages to a sever and receiving event-driven responses w/o having to poll the sever for a reply


### 2.2.3 The "game loop"

The "game loop" is the main component of any game. It separates the game logic and the visual layer from a user's input and actions.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open("https://bit.ly/2Ttk7fr")"
    src    = "https://bit.ly/2U3TxcZ"
    alt    = ""
    title  = ""
  />
</figure>

Traditional applications respond to user input and do nothing without it - word processors format text as a user types. If the user doesn't type anything, the word processor is waiting for an action.

Games operate differently: a game must continue to operate regardless of a user's input!

The game loop allows this. The game loop is computing events in our game all the time. Even if the user doesn’t make any action, the game will move the enemies, resolve collisions, play sounds and draw graphics as fast as possible. 


#### Different implementations of the 'Main Game Loop'

There are different ways to perform animation with JavaScript. A very detailed comparison of three different methods has already been presented in the W3Cx HTML5 Coding Essentials course. Below is a quick reminder of the methods, illustrated with new, short, online examples.

__Performing animation using the JavaScript setInterval(...) function__

+ Syntax: `setInterval(function, ms);`

  The setInterval function calls a function or evaluates an expression at specified intervals of time (in milliseconds), and returns a unique id of the action. You can always stop this by calling the clearInterval(id) function with the interval identifier as an argument.

[Try an example at JSBin](https://jsbin.com/qopefu/edit): open the HTML, JavaScript and output tabs to see the code.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/2Ttk7fr")"
    src    = "https://bit.ly/35qR52E"
    alt    = "Screenshot of the JsBin setInterval Example with different tabs opened"
    title  = "Screenshot of the JsBin setInterval Example with different tabs opened"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> addStarToTheBody </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"*"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="com">//this will add one star to the document each 200ms (1/5s)</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">setInterval</span><span class="pun">(</span><span class="pln">addStarToTheBody</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></strong></li>
</ol></div><br>

<span style="color: red;">WRONG:</span>

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">setInterval</span><span class="pun">(‘</span><span class="pln">addStarToTheBody</span><span class="pun">()’,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">setInterval</span><span class="pun">(‘</span><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="pun">“*”;’,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
</ol></div><br>

<span style="color: lightgreen;">GOOD:</span>

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">setInterval</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="pun">“*”;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></li>
</ol></div><br>

or like we did in the example, with an external function.

<font style="pink;">Reminder from the HTML5 Coding Essentials course: with <code>setInterval</code> - if we set the number of milliseconds at, say, 200, it will call our game loop function EACH 200ms, <u>even if the previous one is not yet finished</u></font>.  Because of this disadvantage, we might prefer to use another function, better suited to our goals.

__Using `setTimeout()` instead of `setInterval()`__

+ Syntax: `setTimeout(function, ms);`

  The `setTimeout` function works like `setInterval` but with one little difference: it calls your function AFTER a given amount of time.

[Try an example at JSBin](https://jsbin.com/vuvitu/edit): open the HTML, JavaScript and output tabs to see the code. This example does the same thing as the previous example by adding a "*" to the document every 200ms.

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> addStarToTheBody </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"*"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// calls again itself AFTER 200ms</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>setTimeout</strong></span><strong><span class="pun">(</span><span class="pln">addStarToTheBody</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="com">// calls the function AFTER 200ms</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">setTimeout</span><span class="pun">(</span><span class="pln">addStarToTheBody</span><span class="pun">,</span><span class="pln"> </span><span class="lit">200</span><span class="pun">);</span></strong></li>
</ol></div><br>

This example will work like the previous example. However, it is a definite improvement, because the timer waits for the function to finish everything inside before calling it again. 

For several years, setTimeout was the best and most popular JavaScript implementation of game loops. This changed when Mozilla presented the requestAnimationFrame API, which became the reference W3C standard API for game animation.


__Using the `requestAnimationFrame` API__

  + Note: using `requestAnimationFrame` was covered in detail in the W3Cx HTML5 Coding Essentials course.

When we use timeouts or intervals in our animations, the browser doesn’t have any information about our intentions -- do we want to repaint the DOM structure or a  canvas during every loop? Or maybe we just want to make some calculations or send requests a couple of times per second? For this reason, it is really hard for the browser’s engine to optimize the loop.

And since we want to repaint the game (move the characters, animate sprites, etc.) every frame, Mozilla and other contributors/developers introduced a new approach which they called `requestAnimationFrame`.

This approach helps the browser to optimize all the animations on the screen, no matter whether  Canvas, DOM or WebGL. Also, if the animation loop is running in a browser tab that is not currently visible, the browser won't keep it running.

Basic usage, [online example at JSBin](https://jsbin.com/geqija/1/edit?html,js,output).

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// called after the page is entirely loaded</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>requestAnimationFrame</strong></span><strong><span class="pun">(</span><span class="pln">mainloop</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> mainloop</span><span class="pun">(</span><span class="pln">timestamp</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"*"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// call back itself every 60th of second</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>requestAnimationFrame</strong></span><strong><span class="pun">(</span><span class="pln">mainloop</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Notice that calling `requestAnimationFrame(mainloop)` at _line 10_, asks the browser to call the `mainloop` function every 16.6 ms: this corresponds to 60 times per second (16.6 ms = 1/60 s).

__This target may be hard to reach; the animation loop content may take longer than this, or the scheduler may be a bit early or late.__

__Many "real action games" perform what we call *time-based animation*.__ For this, we need an accurate timer that will tell us the elapsed time between each animation frame. Depending on this time, we can compute the distances each object on the screen must achieve in order to move at a given speed, independently of the CPU or GPU of the computer or mobile device that is running the game. 

The `timestamp` parameter of the `mainloop` function is useful for exactly that: it gives a high resolution time.

We will cover this in more detail, later in the course.






