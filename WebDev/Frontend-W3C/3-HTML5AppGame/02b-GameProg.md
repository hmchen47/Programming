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

The requestAnimationFrame API targets 60 frames per second animation in canvases. This API is quite simple and also comes with a high resolution timer. Animation at 60 fps is often easy to obtain with simple 2D games on major desktop computers. This is the preferred way to perform animation, as the browser will ensure that animation is not performed when the canvas is not visible, thus saving CPU resources.


#### Videos and animated textures: the `<video>` element

The HTML5 `<video>` element was introduced in the HTML5 specification for the purpose of playing streamed videos or movies, partially replacing the object element.  The JavaScript API is nearly the same as the one of the `<audio>` element and enables full control from JavaScript.

By combining the capabilities of the `<video>` and `<canvas>` elements, it is possible to manipulate video data to incorporate a variety of visual effects  in real time, and conversely, to use images from videos as "animated textures" over graphic objects.


#### `<audio>` Element and the Web Audio API

__Audio (streamed audio and real time sound effects): the `<audio>` element and the Web Audio API__

__The `<audio>` element__

`<audio>` is an HTML element that was introduced to give a consistent API for playing streamed sounds in browsers. File format support varies between browsers, but MP3 works in nearly all browsers today. Unfortunately, the `<audio>` element is only for streaming compressed audio, so it consumes CPU resources, and is not adapted for sound effects where you would like to change the playing speed or add real time effects such as reverberation or doppler. For this, [the Web Audio API](https://www.w3.org/TR/webaudio/) is preferable.


__The Web Audio API__

This is a 100% JavaScript API designed for working in real time with uncompressed sound samples or for generating procedural music. Sound samples will need to be loaded into memory and decompressed prior to being used. Up to 12 sound effects are provided natively by browsers that support the API (all major browsers except IE, although Microsoft Edge supports it).


#### Keyboard & Mouse Events and The GamePad API

__Interacting: dealing with keyboard and mouse events, the GamePad API__

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






