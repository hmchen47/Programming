# Week 3: HTML5 Graphics


## 3.2 Basics of HTML5 canvas


### 3.2.0 Lecture Notes

+ [JavaScript & HTML5](#321-about-javascript-and-html5)
  + adding js code in HTML page: `<script>`...`</script>`
  + JavaScript code executed before the browser could see the rest of the page as the `<script></script>` located before the `<body>`
  + `console.log(...)`: display in the JavaScript console the message...
  + eg. `<script> console.log("Some JavaScript code has been executed"); </script>`
  + debug:
    + dev. tool on web browser &gt; console tab &gt; error/log msgs
    + allowing to type any JS command

+ [The `<canvas>` element](#322-the-canvas-element)
  + provide scripts with a resolution-dependent bitmap canvas
  + used for rendering graphs, game graphics, or other visual images on the fly
  + designed for pixel-based graphics, while SVG (Scalable Vector Graphics, another W3C standard) for vector-based graphics
  + shapes that canvas JavaScript drawing API supported: lines, rectangles, ellipses, arcs, curves, text, images
  + drawing styles: affect the way shapes drawn, e.g., color, width, shadows, etc.
  + alpha channel: transparent mode
  + common usages
    + animations at 60 frames per second (useful for games)
    + videos with special effects
    + displaying a webcam stream
    + and so on
  + [35 incredible dataviz tools](https://www.creativebloq.com/design-tools/data-visualization-712402)
    + [Chart Studio](https://plot.ly/): make charts, presentations and dashboards
    + [DataHero](https://datahero.com/): pull together data from cloud services and create charts and dashboards
    + [Chart.js](http://www.chartjs.org/): the perfect data visualization tool for hobbies and small projects
    + [Tableau](https://public.tableau.com/): a popular data visualization tool packed with graphs, charts, maps and more
    + [RAWGraphs](https://rawgraphs.io/): create vector-based data visualizations
    + [Dygraphs](http://dygraphs.com/): a fast, flexible open source JavaScript charting library that allows users to explore and interpret dense data sets
    + [ZingChart](http://www.zingchart.com/): a JavaScript charting library and feature-rich API set that lets users build interactive Flash or HTML5 charts
    + [InstantAtlas](http://www.instantatlas.com/): a data viz tool with mapping
    + [Modest Maps](http://modestmaps.com/): a lightweight, simple mapping tool for web designers that makes it easy to integrate and develop interactive maps within your site
    + [Leaflet](http://leafletjs.com/): use OpenStreetMap data and integrate fully interactive data visualization in an HTML5/CSS3 wrapper
    + [WolframAlpha](http://www.wolframalpha.com/): intelligently displaying charts in response to data queries, without the need for any configuration
    + [Visualize Free](https://www.visualizefree.com/): a hosted tool that allows you to use publicly available datasets, or upload your own, and build interactive visualizations to illustrate the data
    + [Better World Flux](http://www.betterworldflux.com/): lovely visualizations of some pretty depressing data
    + [FusionCharts](http://www.fusioncharts.com/): 90+ charts and gauges, 965 data-driven maps, and ready-made business dashboards and demos, w/ extensive JavaScript API that makes it easy to integrate it with any AJAX application or JavaScript framework
    + [jqPlot](http://www.jqplot.com/): a nice solution for line and point charts
    + [D3.js](http://d3js.org/): a JavaScript library that uses HTML, SVG, and CSS to render some amazing diagrams and charts from a variety of data sources
    + [JavaScript InfoVis Toolkit](http://thejit.org/): a modular structure, allowing you to only force visitors to download what's absolutely necessary to display your chosen data visualizations
    + [jpGraph](http://jpgraph.net/): a PHP-based solution with a wide range of chart types
    + [Highcharts](http://www.highcharts.com/): a JavaScript charting library with a huge range of chart options available
    + [Google Charts](https://developers.google.com/chart/interactive/docs/): highly flexible and an excellent set of developer tools
    + [Excel](https://tinyurl.com/y43wme3q): a good way of quickly exploring data, or creating visualizations for internal use, but the limited default set of colours, lines and styles make it difficult to create graphics that would be usable in a professional publication or website
    + [CSV](http://en.wikipedia.org/wiki/Comma-separated_values)/[JSON](http://www.json.org/): common formats for data
    + [Crossfilter](http://square.github.com/crossfilter/): enable clients to wade through their data and create graphs and charts that double as interactive GUI widgets
    + [Tangle](http://worrydream.com/Tangle/): trying to describe a complex interaction or equation, letting the reader tweak the input values and see the outcome for themselves provides both a sense of control and a powerful way to explore data
    + [Polymaps](http://polymaps.org/): a mapping library that is aimed squarely at a data visualization audience
    + [OpenLayers](http://openlayers.org/): probably the most robust of these mapping libraries
    + [Kartograph](http://kartograph.org/): a simple and lightweight framework for building interactive map applications without Google Maps or any other mapping service
    + [Carto](http://cartodb.com/): a must-know site with which you can combine tabular data with maps is second to none
    + [Processing](http://processing.org/): the poster child for interactive visualizations
    + [NodeBox](http://nodebox.net/): an OS X application for creating 2D graphics and visualizations
    + [R](http://www.r-project.org/): statistical package used to parse large data sets
    + [Weka](http://www.cs.waikato.ac.nz/ml/weka/): a good tool for classifying and clustering data based on various attributes – both powerful ways to explore data
    + [Gephi](http://gephi.org/): a graph-based visualizer and data explorer about relatedness, social graphs and co-relations
    + [iCharts](http://www.icharts.net/): a hosted solution for creating and presenting compelling charts for inclusion on your website
    + [Flot](http://www.flotcharts.org/): a specialized plotting library for jQuery
  + 3D drawing: possible using the WebGL API in a `<canvas>` w/ [BabylonJS](https://www.babylonjs.com/) and [ThreeJS](https://threejs.org/)
  + [HTML standard](https://html.spec.whatwg.org/multipage/canvas.html) of the `<canvas>` element
    + The 2D rendering context
    + The ImageBitmap rendering context
    + The OffscreenCanvas interface
    + Color spaces and color correction
    + Serializing bitmaps to a file
    + Security with canvas elements

+ [Accessible principles on `<canvas>`](#323-canvas-and-accessibility)
  + providing alternative content for what is drawn on the `<canvas>`
  + exposing the location of shapes, paths, images drawn on the `<canvas>` to assistive technologies
  + visually indicating whether or not a shape in the canvas had keyboard focus

+ [`<canvas>` cheetsheet](#324-html-canvas-cheatsheet)
  + [PDF file](https://tinyurl.com/y6cvfxv9)
  + [HTML file](https://tinyurl.com/kxm2vxf)
  
+ [canvas coordinate system](#325-coordinate-system)
  + (0, 0): the top left corner
  + X axis: from the left to the right
  + Y axis: from the top to the bottom

+ [Drawing rectangle](#326-drawing-rectangles-in-a-canvas)
  + simple drawing
    + add the `<canvas>` element into an HTML page
      + selector to identify the canvas itself
      + specify the size of canvas w/ `width` and `height` attributes
      + NOT supported message placed btw opening and closing tags
      + canvas transparent by default
      + e.g., `<canvas id="myCanvas" width="300" height="225">` 
      + CSS styling make it visible, e.g., ` border:1px solid black;`
      + multiple canvas allowed in a page
    + select the `<canvas>` element for use from JavaScript
      + element in the DOM, e.g., `var canvas = document.getElementById("myCanvas");`
      + CSS selector syntax for selecting elements, e.g, `var canvas = document.querySelector("#myCanvas");`
    + get a "2D context" associated with the canvas, useful for drawing and setting drawing properties (color, etc.)
      + `context`: a particular object as the core of the canvas JavaScript API providing methods for drawing
      + access the context: `var ctx=canvas.getContext('2d');`
      + set filled color: `ctx.fillStyle='red';`
      + draw filled rectangle: `ctx.fillRect(x, y, width, height);`
  + only access elements when the DOM is ready
    + select and get 2D context via `init()` function
    + `init()` only called after the page entirely loaded
    + unable to access the elements of the page before the page loaded entirely and before the DOM ready
    + ways to achieve the requirement
      + add `onload` attribute w/ `<body>` element, e.g., `<body onload="init();">` (good practice)
      + put the JavaScript code at the end of the document, just before `</body>` between `<script>`...`</script>`
  + access drawing context before manipulating it
    + the drawing context defines the drawing methods and properties
    + good practice: get the canvas, the context, the width and height of the canvas and other global objects in this "init" function
  + example: filled rectangle
    + `fillstyle` property: assign a color, a gradient, or a pattern; e.g., `ctx.fillStyle='#FF0000';`
    + `fillRect(top left X coordinate, top left Y coordinate, width, height)` method: draw a filled rectangle
  + summary of drawing on a canvas
    + declare the canvas, remembering to add an `id` attribute, and fallback content
    + get a reference to the canvas in a JavaScript variable using the DOM API
    + get the context for drawing in that canvas
    + specify some drawing properties (optional)
    + draw the shape

+ [Drawing principles](#327-drawing-principles)
  + `fillstyle` property:
    + a property in the context, similar to a CSS property
    + possible values: a color, a pattern (texture), or a gradient
    + default: color black
    + using the value of the property to fill part of the drawing
    + as long as not modified, all drawing commands using the current value
  + `fillRect(x, y, width, height)` method:
    + draw a filled rectangle
    + `x` & `y`: the coordinates of the top left corner of the rectangle
    + e.g., `ctx.fillStyle='pink'; ctx.fillRect(10, 10, 200, 200);` - draw a pink filled rectangle, from (10, 10) to (210, 210)
  + `strokeStyle` property:
    + how the shape's outline rendered
    + possible values: a color, a pattern (texture), or a gradient
  + `strokeRect(x, y, width, height)` method:
    + draw the wireframe mode of a rectangle w/ `strokStyle` property
    + e.g., `ctx.strokeStyle='blue'; ctx.strokeRect(10, 10, 200, 200);` - draw the outline of a rectangle from (10, 10) to (210, 210)
  + `clearRect(x, y, width, height)` method:
    + erase the specified rectangle
    + draw the rectangle w/ color = "transparent black" as the `init` state of rectangle
    + e.g., `ctx.strokStyle='pink'; ctx.fillRect(10, 10, 200, 200); ctx.clearRect(50, 50, 20, 20);` - draw a pink filled rectangle but clear a rectangle within it from (50, 50) to (70, 70)
  + `linewidth` property: a property applied only in `stroke` mode w/ value in `px`
  + `font` property: specify the font property of the context, syntax same as in CSS for using 'system font", e,g,. `ctx.font = 'italic 20pt Calibri';`
  + `ctx.fillText(str, x, y)` method:
    + draw text message `str` at (x, y) position, e.g., `ctx.fillText("hello", 70, 22)`
    + `fillStyle` property to modify the color of the message
  + summary 
    + "stroke":
      + wireframe of shapes
      + a prefix for setting properties or calling methods that effect wireframe shapes
    + "fill": filled the shapes
    + `ctx.strokStype=...`: set the property of wireframed shapes
    + `ctx.fillStyle=...`: set the property of filled shapes
    + `ctx.strokeRect(x, y, width, height)`: draw wireframe rectangle from (x, y) to (x+width, y+height)
    + `ctx.fillRect(x, y, width, height)`: draw filled rectangle from (x, y) to (x+width, y+height)
    + `ctx.lineWidth`: set the line width of wireframed shapes
    + `ctx.strokeText(msg, x, y)` or `ctx.fillText(msg, x, y)`: draw a text msg for wireframed or filled text respectively
    + `ctx.font`: set the character font w/ values used in CSS syntax, e.g., `ctx.font = 'italic 20pt Calibri';`

+ [2D transformations](#328-2d-transformations)
  + translate (or rotate, or scale) the original coordinate system instead of modifying all the coordinates passed as parameters to each call to drawing methods
  + order of transformation: translate, rotate, and then scale
  + `ctx.translate(offsetX, offsetY)`
    + translation to shift (0, 0) to (offsetX, offsetY)
    + change the position of the coordinate system then draw the shape
  + `ctx.rotate(angle)`: rotate the coordinate system w/ angle in radians
  + `ctx.scale (sx, sy)`:
    + `scale(1, 1)`: no zoom, remain the same
    + `scale(2, 2)`: zooming 2x
    + `scale(0.5, 0.5)`: zoom out to see the drawings half as big as before

+ [Saving and Restoring the context](#329-saving-and-restoring-the-context)
  + `ctx.save()` & `ctx.restore()` methods
    + saving the context properties
    + saved properties: all properties effecting the drawing
    + probably save the context property values in a hardware register on the graphics card
    + multiple contexts able to be saved consectively and restored
    + multiple contexts saved in stacked manner
  + best practice: save the context before any activities modifying the context, and restore it at the end of the activities, in particular, a function



### 3.2.1 About JavaScript and HTML5

HTML5 is composed of new elements, but it also comes with many JavaScript APIs for controlling video and sound, drawing and animating things in the new `<canvas>` element, for offline applications, persistence, geolocation, orientation, etc.

So yes, during this course, in particular during Week 3 and 4, you will have to do a bit of JavaScript. __But, DON'T PANIC!__

Here we provide a basic introduction to JavaScript. If you want to learn more, many resources are available on the Web; this document is simply here to give you a head start. Remember that one great thing about these MOOCs courses is that everybody can help each other. Some students are very good in JavaScript and are usually very happy to help others when they encounter difficulties.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>You will learn a lot by looking at examples, tweaking them, cloning and modifying them, etc.</strong> Many previous&nbsp;students who were real JavaScript beginners managed to do <span style="text-decoration: underline;">all</span> the assignments (drawing and animating a monster with keyboard/mouse interaction)! And they did this&nbsp;by just studying the provided examples.</p>


#### External resources

+ The [JavaScript Introduction](https://www.edx.org/course/javascript-introduction) course on W3Cx!
+ Mozilla Developper Network has [a JS guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)


#### What do you need? How to debug? How to catch errors?

We will not look at the JavaScript syntax here, but more at "JavaScript in the browser", how it works, how to start writing code, etc.

First of all, you need to find a way to debug your code and see errors. If your work does not produce any results, you must know why!

For that you will use __the dev. tools of your browser__. Press _F12_ in Windows or _cmd-alt-i_ in Mac to open the dev. tools, then go to the console tab: __this is where errors will be displayed__, or messages of your own (use the console.log(string) JavaScript function in the JavaScript code embedded in your html page). In the console, you will be able to type any JavaScript command.

Let's look at [this example on JS Bin](https://jsbin.com/visariz/1/edit?html,output): ([Local Example - JS](src/3.2.1-example1.html))

<div class="rj_insertcode_html4strict" style="overflow: auto; width: 546.174987792969px; height: auto; border: 1px solid #054b6e; background: #f8f8f8;">
<table class="html4strict" style="max-width: 100%; border-spacing: 0px; width: 545.599975585938px; background-color: transparent;">
<tbody>
<tr class="li1">
<td style="width: 1px; vertical-align: top; color: #676f73; border-right-style: dotted; border-right-color: #dddddd; font-size: 12px; text-align: right; background: #f0f0f0;">
<pre style="padding: 0px 4px; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; color: #333333; border-radius: 4px; margin-top: 0px; margin-bottom: 0px; line-height: 20px; word-break: normal; border: 1px solid rgba(0, 0, 0, 0.14902); vertical-align: top; background: none;">1
2
3
4
5
6
7
8
9
10
11
12
13
</pre>
</td>
<td style="margin-top: 0px; margin-bottom: 0px; vertical-align: top; padding: 0px 4px; font-size: 12px; word-break: normal; background: none;">
<pre style="padding: 0px 4px; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; color: #333333; border-radius: 4px; margin-top: 0px; margin-bottom: 0px; line-height: 20px; word-break: normal; border: 1px solid rgba(0, 0, 0, 0.14902); vertical-align: top; background: none;"><span style="color: #00bbdd;">&lt;!DOCTYPE html&gt;</span>
<span style="color: #009900;">&lt;<a style="color: purple;" href="https://december.com/html/4/element/html.html"><span style="font-weight: bold;">html <span style="text-decoration: underline;"> </span>lang="en"</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="https://december.com/html/4/element/head.html"><span style="font-weight: bold;">head</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="https://december.com/html/4/element/meta.html"><span style="font-weight: bold;">meta</span></a> <span style="color: #000066;">charset</span><span style="color: #66cc66;">=</span>utf-<span style="color: #cc66cc;">8</span> <span style="color: #66cc66;">/</span>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="https://december.com/html/4/element/title.html"><span style="font-weight: bold;">title</span></a>&gt;</span>Web Audio API<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="https://december.com/html/4/element/title.html"><span style="font-weight: bold;">title</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="https://december.com/html/4/element/script.html"><span style="font-weight: bold;">script</span></a>&gt;</span>
&nbsp; &nbsp;console.log("Some JavaScript code has been executed");
&nbsp; <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="https://december.com/html/4/element/script.html"><span style="font-weight: bold;">script</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="https://december.com/html/4/element/head.html"><span style="font-weight: bold;">head</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="https://december.com/html/4/element/body.html"><span style="font-weight: bold;">body</span></a>&gt;</span>
&nbsp; &nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="https://december.com/html/4/element/h1.html"><span style="font-weight: bold;">h1</span></a>&gt;</span>JavaScript debugging using the dev tool console<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="https://december.com/html/4/element/h1.html"><span style="font-weight: bold;">h1</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="https://december.com/html/4/element/body.html"><span style="font-weight: bold;">body</span></a>&gt;</span>
<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="https://december.com/html/4/element/html.html"><span style="font-weight: bold;">html</span></a>&gt;</span></pre>
</td>
</tr>
</tbody>
</table>
</div><br/>

The simplest way to add JavaScript code in an HTML page, is by using the `<script>`...`</script>` element.

The code in this example is executed sequentially when the page is loaded: the JavaScript code is executed before the browser could see the rest of the page (as the `<script></script>` is located before the `<body>`).

The H1 element, for example, does not exist in the Document Object Model, and has not yet been displayed when the JavaScript code is executed. If we move the `<script></script>` at the end of the document, then the H1 would have been built before the JavaScript code is executed.

The only line of code we have is `console.log("Some JavaScript code has been executed");`

This means "display in the JavaScript console the message...". If we open the console tab provided by jsbin.com in a dedicated tab (that redirects all `console.log()` messages), and re-execute the page (just type a space at the end of a line, this will re-render the page and display the message in the console), we see the message in the console tab, as well as in the dev. tools console. This is illustrated by the image below:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4on5466')"
    src    ="https://tinyurl.com/yybjnlgd"
    alt    ="java script console view 1"
    title  ="java script console view 1"
  />
</figure>


It is also possible to use the "real dev. tool console", and for this I recommend running the application in a single window, not in the JS Bin editor. Press the black arrow on the top right of the output window - this will render the page as a standalone Web page, then press _F12_. You should see:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4on5466')"
    src    ="https://tinyurl.com/y32hk8sq"
    alt    ="view of the javascript console"
    title  ="view of the javascript console"
  />
</figure>


Ok, now, let's make an error: change `console.log()` into `consollle.log()`. Let's see what happens:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4on5466')"
    src    ="https://tinyurl.com/yy3ktegl"
    alt    ="view of the javascript console"
    title  ="view of the javascript console"
  />
</figure>


And if we run it standalone and use the dev. tool console:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4on5466')"
    src    ="https://tinyurl.com/y4thhg8d"
    alt    ="View of the JavaScript console"
    title  ="View of the JavaScript console"
  />
</figure>


And if we click on the line number in the right, the dev. tool shows the source code centered on the line that caused the error:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y4on5466')"
    src    ="https://tinyurl.com/y4m9qco7"
    alt    ="View of the JavaScript console. We can see an extract of the source code with different tools for watching variable values over execution etc."
    title  ="View of the JavaScript console. We can see an extract of the source code with different tools for watching variable values over execution etc."
  />
</figure>


Without such tools, debugging JavaScript code is impossible. So you need to look at some basic tutorials on how to use the dev. tools of your browsers, since they differ from one another in the way they work - although the principles remain the same.


#### About the asynchronous nature of JavaScript

Some of you may not be used to "asynchronous programming", "callbacks" etc. We recommend to read [this article on WikiPedia](https://en.wikipedia.org/wiki/Callback_%28computer_programming%29) and [this thread on StackOverflow](https://stackoverflow.com/questions/8736378/what-is-a-callback-in-java).



### 3.2.2 The `<canvas>` element

#### Video: introduction to the canvas

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V000400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/>


#### The `<canvas>` element

The `<canvas>` tag is one of the "Flash killer" features of HTML5. This course focuses on the fundamental drawing capabilities of the HTML5 canvas.

For the [`<canvas>` element](https://html.spec.whatwg.org/multipage/canvas.html#the-canvas-element), the specification states that <i>"The canvas element provides scripts with a <strong>resolution-dependent bitmap canvas</strong>, which can be used for rendering graphs, game graphics, or other visual images on the fly."</i>

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>The canvas has been designed for pixel-based graphics</strong>, while SVG (Scalable Vector Graphics, another W3C standard) is for vector-based graphics.</p>

Indeed, the canvas JavaScript drawing API supports different kind of shapes: lines, rectangles, ellipses, arcs, curves, text, images. Some drawing styles need to be specified that will affect the way shapes are drawn (color, drawing width, shadows, etc.). An alpha channel for drawing in transparent mode is also supported, as well as many advanced drawing modes and global filters (blur, etc.).

The canvas is also used to do animations at 60 frames per second (useful for games), to display videos with special effects, to display a webcam stream, and so on.


#### Examples

__Example 1__

[Foot Chinko](https://www.ravalmatic.com/portfolio/footchinko/) is one popular free HTML5 games:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yy3y7c4c')"
    src    ="https://tinyurl.com/y3aschek"
    alt    ="foot chinko one of the best html5 2D game of 2015"
    title  ="foot chinko one of the best html5 2D game of 2015"
  />
</figure>


__Example #2__

Lots of data visualization tools and JavaScript libraries use the HTML5 canvas element for [Data visualization](https://tinyurl.com/k6wk58p):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yy3y7c4c')"
    src    ="https://tinyurl.com/y6or3n9c"
    alt    ="html5 data visualization"
    title  ="html5 data visualization"
  />
</figure>


__Example #3__

A version of [the arcade game Galaxian](https://intersoft.itch.io/galaxian), that runs at 60 frames per second in an HTML5 canvas element:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yy3y7c4c')"
    src    ="https://tinyurl.com/y3zwgqnz"
    alt    ="A version of the game Galaxian that runs at 60 frames/s in a canvas."
    title  ="A version of the game Galaxian that runs at 60 frames/s in a canvas."
  />
</figure>


Performance is  good, since most Web browsers (mobile and desktop) support hardware acceleration. 

<div style="padding: 10px; border: 1px solid red;">
<p><strong>Note</strong>: 3D drawing using the WebGL API is also possible in a <span style="font-family: 'courier new', courier;">&lt;canvas&gt;</span>, but will not be covered in this course. For the most curious among you, please have&nbsp;a look at the two popular libraries for doing 3D drawing/animation in a <span style="font-family: 'courier new', courier;">&lt;canvas&gt;</span>: <a href="https://www.babylonjs.com/" target="_blank">BabylonJS</a>&nbsp;and <a href="https://threejs.org/" target="_blank">ThreeJS</a>.</p>
</div>


#### External resources

+ Comprehensive [HTML5 canvas tutorials](http://www.html5canvastutorials.com/)
+ An [HTML Canvas Deep Dive](https://joshondesign.com/p/books/canvasdeepdive/title.html)
+ MDN's Web [docs: `<canvas>`: The Graphics Canvas element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
+ The `<canvas>` element is well supported by browsers:
  + CanIUse: [browser support table](http://caniuse.com/#feat=canvas)
  + MDN's [browser compatibility of `<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas#Browser_compatibility)


#### Knowledge check 3.2.2

1. The HTML5 canvas is for:<br/>

  a. Pixel-based graphics (bitmaps)<br/>
  b. Vector-based graphics<br/>

  Ans: a<br/>
  Explanation: The canvas has been designed for pixel based graphics. SVG, another W3C standard, is for vector-based graphics (parametric, resolution independant).


### 3.2.3 Canvas and accessibility

The dynamic nature of the `<canvas>` element has made it difficult to use in applications that need to be accessible to people with disabilities. To be accessible, it must meet the following principles:

+ Providing alternative content for what is drawn on the `<canvas>`,
+ Exposing the location of shapes, paths, images drawn on the `<canvas>` to assistive technologies,
+ Visually indicating whether or not a shape in the canvas had keyboard focus.

Read more on this topic: 

+ An article on [What the canvas element means for accessibility](https://www.creativebloq.com/web-design/canvas-element-accessibility-41514740)
+ From the W3C wiki: [Canvas Element Accessibility Issues](https://www.w3.org/html/wg/wiki/AddedElementCanvas)


### 3.2.4 HTML canvas cheatsheet

We recommend these 2 quick references (or [cheatsheets](https://en.wikipedia.org/wiki/Cheat_sheet)) below. Do not hesitate to keep your favorite one open in a separate browser tab

1. As a [PDF file](https://tinyurl.com/y6cvfxv9), this canvas cheatsheet:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yydo9x7z')"
    src    ="https://tinyurl.com/y4fhj9mz"
    alt    ="snapshot of an HTML Canvas cheatsheet from skilled.com"
    title  ="snapshot of an HTML Canvas cheatsheet from skilled.com"
  />
</figure>


2. Another resource, as an [HTML file](https://tinyurl.com/kxm2vxf):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yydo9x7z')"
    src    ="https://tinyurl.com/yyzk6eb2"
    alt    ="Snapshot of a canvas sheet API"
    title  ="Snapshot of a canvas sheet API"
  />
</figure>


### 3.2.5 Coordinate system

The coordinate system used for drawing in canvases is similar to the one used by many drawing APIs like Java2D: the (0 , 0) is in the top left corner while the X axis is going to the right and the Y axis to the bottom, as  shown in the following picture (by Mark Pilgrim):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yxopdcdh')"
    src    ="https://tinyurl.com/y4kyo9ew"
    alt    ="coordinate system for canvas"
    title  ="coordinate system for canvas"
  />
</figure>

+ X axis is horizontal, directed to the right
+ Y axis is vertical, directed downwards


### 3.2.6 Drawing rectangles in a canvas

#### Live coding video: basic example showing how to draw in a canvas

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V001500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/yy7clvze)

Small errata about what I said in the above video: "So let's get the canvas using the DOM API method `document.getElementById()` or better, use `document.querySelector()` that is a more recent method __from the DOM API__"..

The part is bold is not correct: `querySelector`, technically, comes from [Selectors API](https://www.w3.org/TR/selectors-api/). Just in case some people would like to check the specification.


#### Detailed explanation of the example shown in the above video

Here are the different steps, in a little more detail, of the example demonstrated in the above video:

__1 - Add the `<canvas>` element into an HTML page__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"300"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"225"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Fallback content that will be displayed in case the web browser </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; does not&nbsp;</span><span class="pln" style="line-height: 1.6; background-color: #ffffff;">support the </span><span class="tag" style="line-height: 1.6; background-color: #ffffff;">canvas</span><span class="pln" style="line-height: 1.6; background-color: #ffffff;"> </span><span class="atn" style="line-height: 1.6; background-color: #ffffff;">tag</span><span class="pln" style="line-height: 1.6; background-color: #ffffff;">&nbsp;or in case scripting </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6; background-color: #ffffff;">&nbsp; &nbsp; is disabled.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/canvas&gt;</span></li>
</ol></div>

Place code similar to the above somewhere in an HTML page. This example defines an area of 300 by 225 pixels on which content can be rendered with JavaScript.

Normally you should see nothing as a result; by default canvases are "transparent".

__Make it visible using CSS__: A good practice when you are learning to use canvases is to use some CSS to visualize the shape of the canvas. This is not mandatory, just a good trick...

The three lines of CSS will create a border around the canvas with `id="myCanvas"`, of 1 pixel width, in black:

CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;style&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">#myCanvas {</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/style&gt;</span></li>
</ol></div>


__2 - Select the `<canvas>` element for use from JavaScript__

We can have more than one `<canvas>` in a single page, and canvases will be manipulated with JavaScript like other elements in the DOM.

For example with:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"myCanvas"</span><span class="pun">);</span></li>
</ol></div>

... or with the querySelector() method introduced by HTML5, that use the CSS selector syntax for selecting elements:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></li>
</ol></div>


__3 - Get a "2D context" associated with the canvas, useful for drawing and setting drawing properties (color, etc.)__

Once we have a pointer to the `<canvas>`, we can get <u>a "context"</u>.

This particular object is the core of the canvas JavaScript API.

It provides methods for drawing, like `fillRect(x, y, width, height)` for example, that draws a filled rectangle, and properties for setting the color, shadows, gradients, etc.

Getting the context (do this only once):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
</ol></div>

Set the color for drawing filled shapes:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'red'</span><span class="pun">;</span></li>
</ol></div>

Draw a filled rectangle:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">100</span><span class="pun">);</span></li>
</ol></div>


#### Complete example that draws a filled rectangle in red

[Try it online at JS Bin](https://jsbin.com/felujew/1/edit?html,output) ([Local Example - Filled Rectangle](src/3.2.6-example1.html))

Result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 5vw;"
    onclick="window.open('https://tinyurl.com/yyg9zyn4')"
    src    ="https://tinyurl.com/y56vbnws"
    alt    ="red rectangle draw in a canvas"
    title  ="red rectangle draw in a canvas"
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;style&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="com">#myCanvas {</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span></span>border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid black</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/style&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// 1 - Get the canvas</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// 2 - Get the context</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// 3 - we can draw</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>drawSomething</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="kwd">function</span><span class="pln"> drawSomething</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// draw a red rectangle</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'#FF0000'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/script&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span>&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"200"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"200"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>Your browser does not support the canvas tag.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp; </span><span class="tag"></span><span class="tag">&lt;/canvas&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span>&lt;/body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


__Explanations__

__Only access elements when the DOM is ready:__

Notice that we wrote an "init" function (line 12) that is called only when the page has been entirely loaded (we say "when the DOM is ready"). There are several ways to do this. In this example we used the `<body onload="init();">` method, at line 32.

It's good practice to have such a function, as we cannot access the elements of the page before the page has been loaded entirely and before the DOM is ready.

Another way is to put the JavaScript code at the end of the document (between `<script>`...`</script>`), right before the `</body>`. In this case when the JavaScript code is executed, the DOM has already been constructed.


__Start by getting the canvas and the context:__

Before drawing or doing anything interesting with the canvas, we must first get its drawing "context". The drawing context defines the drawing methods and properties we can use.

Good practice is to get the canvas, the context, the width and height of the canvas and other global objects in this "init" function.


__After the context is set, we can draw, but first let's set the current color for filled shapes:__

The example shows the use of the `fillStyle` property at line 27 - useful for specifying the way shapes will be filled. In our case this line indicates the color of all the filled shapes we are going to draw:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'#FF0000'</span><span class="pun">;</span></li>
</ol></div>

The context property named `fillStyle` is used here. This property can be set with a color, a gradient, or a pattern. We will see examples of these later on in the course.

When we set it with a color, we use [the CSS3 syntax](http://www.w3.org/TR/css3-color/).

The example says that all filled shapes will use the color "#FF0000", which corresponds to a pure red color using the CSS RGB hexadecimal encoding (we could also have used `ctx.fillStyle='red');`


__Then we can draw:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">100</span><span class="pun">);</span></li>
</ol></div>

This line is a call to the method `fillRect(top left X coordinate, top left Y coordinate, width, height)`, which draws a filled rectangle.

The way the rectangle will be filled depends on the current value of several properties of the context, in particular the value of the `fillStyle` property. So, in our case, the rectangle will be red.


#### Summary of the different steps

<ol>
  <li><strong>Declare the canvas,</strong>&nbsp;remembering to add an <span style="font-family: 'courier new', courier;">id</span> attribute, and fallback content: &nbsp;<br><span style="font-family: 'courier new', courier;">&lt;canvas id="myCanvas" width="200" height="200"&gt;<br>...fallback content...<br>&lt;/canvas&gt;</span></li>
  <li><strong>Get a reference to the canvas in a JavaScript variable</strong> using the DOM API: <br><span style="font-family: 'courier new', courier;">var canvas=document.getElementById('myCanvas');</span></li>
  <li>&gt; <strong>Get the context for drawing in that canvas</strong>: &nbsp;<br><span style="font-family: 'courier new', courier;">var ctx=canvas.getContext('2d');</span></li>
  <li><strong>Specify some drawing properties</strong> (optional): &nbsp;<br><span style="font-family: 'courier new', courier;">ctx.fillStyle='#FF0000';</span></li>
  <li><strong>Draw some shapes</strong>: <br><span style="font-family: 'courier new', courier;">ctx.fillRect(0,0,80,100);</span></li>
</ol>


#### Knowledge check 3.2.6

1. Drawing shapes in a canvas is only possible from JavaScript, and the canvas must be selected using the DOM API first, using document.getElementById(...), document.querySelector(...), etc. (True/False)

  Ans: True<br/>
  Explanation: Indeed, while setting an image background in a canvas using CSS is possible, drawing shapes is done by using the canvas JavaScript API.



### 3.2.7 Drawing principles

#### More about the "context" object

Before we go on, we should take some time to clarify the way we draw on HTML5 canvases. We already mentioned that we use a graphic context for all the main operations. Whenever a shape, a text, or an image is drawn, the current values of the different properties of the graphic context are taken into account. Some are relevant only for certain kinds of shapes or drawing modes, but you must be aware that it is always the current values of these drawing properties that are used.

Later on we'll see that there are ways to save and restore this whole set of values, but for now, let's examine in greater detail some of the properties and methods we've already encountered, and introduce new ones.


#### More about properties and methods of the context object

+ __fillStyle is a property of the context, similar in a way to a CSS property__

Its value can be one of the following:

+ a color,
+ a pattern (texture), or
+ a gradient.

The default value is the color black. Any kind of drawing in "fill mode" will use the value of this property to determine how to render the "filled part" of the drawing: any filled rectangle will be filled black by default, any filled circle will be filled in black, and so on.

As long as we don't modify the value of this property, all drawing commands for filled shapes will use the current value.

Note that we will study in detail how to use colors, gradients and patterns later, but for now we introduce some properties and values so that you can understand the principles of canvas drawing.

`fillStyle` and the other context properties can be considered to be "global variables" of the context.

__fillRect(x, y, width, height):  a call to this method draws a filled rectangle__

The two first parameters are the coordinates of the top left corner of the rectangle. This method uses the current value of the `fillStyle` property to determine how to fill the rectangle.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'pink'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
</ol></div>

Produces this result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyjtw55d')"
    src    ="https://tinyurl.com/yyq5abh2"
    alt    ="filled rectangle"
    title  ="filled rectangle"
  />
</figure>


__strokeStyle is a property of the context similar to fillStyle, but this time for indicating how the shape's outline should be rendered__

The possible values are the same as those for the fillStyle property: a color, a pattern, or a gradient. This property will be taken into account when wireframe shapes are drawn.

__strokeRect(x, y, width, height): like fillRect(...), but instead of drawing a filled rectangle the rectangle is drawn in wireframe mode__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">strokeStyle</span><span class="pun">=</span><span class="str">'blue'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
</ol></div>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyjtw55d')"
    src    ="https://tinyurl.com/y4s8bjld"
    alt    ="stroked rectangle"
    title  ="stroked rectangle"
  />
</figure>


Only the outline of the rectangle will be drawn, and it will be drawn using the value of the strokeStyle property.

__clearRect(x, y, width, height): a call to this method erases the specified rectangle__

Actually it draws it in a color called "transparent black" (!) that corresponds to the initial state of the rectangle as if no drawing had occurred.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'pink'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></li>
</ol></div>

The result is:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyjtw55d')"
    src    ="https://tinyurl.com/y4zlqqnz"
    alt    ="clear rect"
    title  ="clear rect"
  />
</figure>


#### Let's see some simple examples

__Example #1: draw a wireframe red rectangle, width lineWidth = 3 pixels__

[Interactive example available here at JSBin](https://jsbin.com/kiduwa/edit?html,output) ([Local Example - Wireframed Rectangle](src/3.2.7-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyjtw55d')"
    src    ="https://tinyurl.com/y5t8r9ec"
    alt    ="wireframe red rectangle with line width = 3 pixels"
    title  ="wireframe red rectangle with line width = 3 pixels"
  />
</figure>


Extract from the source code (the part that draws the rectangle):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawSomething</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// draw a red rectangle, line width=3 pixels</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">lineWidth</span><span class="pun">=</span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">strokeStyle</span><span class="pun">=</span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>

Here, we used "stroke" instead of "fill" in the property and method names (lines 4 and 5): strokeStyle instead of fillStyle, strokeRect(...) instead of fillRect(...).

We also introduced a new property of the context, that applies only when drawing in "stroke" mode, the lineWidth property (line 3), that is used for setting the width of the shape outline. The value is in pixels.

__Example #2: draw two filled red rectangles with a blue outline of 5 pixels and some text__

Let's continue with another example. This time we will draw several shapes that share the same colors - they will be filled in red, with a blue outline. We also show how to draw a text message with a given font.

[Online example on JS Bin](https://jsbin.com/zarihi/edit?html,output) ([Local Example - Two Filled Rectangles](src/3.2.7-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yyjtw55d')"
    src    ="https://tinyurl.com/y34wpnwh"
    alt    ="rectangles and text that shares colors"
    title  ="rectangles and text that shares colors"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawSomething</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// set the global context values</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">lineWidth</span><span class="pun">=</span><span class="lit">5</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeStyle</span><span class="pun">=</span><span class="str">'blue'</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// font for all text drawing</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">font </span><span class="pun">=</span><span class="pln"> </span><span class="str">'italic 20pt Calibri'</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com">// Draw the two filled red rectangles</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">110</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Draw the two blue wireframe rectangles</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">strokeRect</span><span class="pun">(</span><span class="lit">110</span><span class="pun">,</span><span class="pln"> </span><span class="lit">30</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">150</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Draw a message above the rectangles</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillText</span><span class="pun">(</span><span class="str">"hello"</span><span class="pun">,</span><span class="pln"> </span><span class="lit">70</span><span class="pun">,</span><span class="pln"> </span><span class="lit">22</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>

This example shows the "global" nature of the context properties. Once you set the filled color to red, any shapes you draw in filled mode will be red. This is true for all the context properties. We set some of these properties in lines 3-7, and all following calls to context methods for drawing rectangles or text will depend on them. The two filled rectangles at lines 10-11 will be red, the two wireframe rectangles drawn at lines 14-15 will be blue, etc.

Line 18 shows how to draw a text message at an X position of 70 and a Y position of 22. The font is set at line 7 using the font property of the context.  The syntax is the same we use in CSS for using "system fonts".

If you would like to draw the filled text message in green, for example, you should set the `ctx.fillStyle` property to "green" after you draw the rectangles and before you draw the text (i.e just before line 18).


#### Summary of what we've learned

+ "stroke" means "wireframe" or "outlined", it is a prefix for setting properties or calling methods that will affect wireframe shapes, "fill" is a prefix for filled shapes.
+ To set the properties of wireframe shapes use `ctx.strokeStyle= ...`, for filled shapes use `ctx.fillStyle=...` So far the values we have used are colors, expressed as strings. Example: `ctx.strokeStyle  = 'blue';`
+ To draw a wireframe rectangle use `ctx.strokeRect(x, y, width, height)`, to draw a filled rectangle use `ctx.fillRect(x, y, width, height);`
+ To set the line width of wireframe shapes, use the `ctx.lineWidth property`. Example `ctx.lineWidth = 10; ctx.strokeRect(0, 0, 100, 100);`  will draw a 100x100 rectangle in wireframe mode, with an outline width of 10 pixels.
+ To draw a text message use `ctx.strokeText(message, x, y)` or `ctx.fillText(message, x, y)`, for wireframe text or filled text respectively.
+ To set the character font use the `ctx.font` property; the value is a font in CSS syntax, for example:  `ctx.font = 'italic 20pt Calibri';`


#### Knowledge check 3.2.7

1. How would you draw a blue wireframe rectangle at 10, 10, width=200, height=400 with a lineWidth of 10 pixels?<br/>

  a. ctx.line=10; ctx.color='blue'; ctx.strokeRect(10, 10, 200, 400);<br/>
  b. ctx.lineWidth=10; ctx.color='blue'; ctx.strokeRect(200, 400, 10, 10);<br/>
  c. ctx.lineWidth=10; ctx.strokeStyle='blue'; ctx.strokeRect(10, 10, 200, 400);<br/>
  d. ctx.width=10; ctx.color='blue'; ctx.strokeRect(10, 10, 200, 400);<br/>

  Ans: c<br/>
  Explanation: Correct answer is the third one: ctx.line does not exist, the correct way to set the width of outlines is by using the `ctx.lineWidth` property. ctx.color does not exist: we set colors by using the `ctx.strokeStyle` or `ctx.fillStyle` properties, the parameters to the ctx.strokeRect methods are (x, y, width, height).



### 3.2.8 2D transformations

We now introduce the basics of 2D transformations, a powerful tool that will make things easier as soon as you have to:

Draw complex shapes at given positions, with given orientations and sizes,
Draw shapes relative to one another.
Let's start with some simple examples before looking at how we use 2D transforms.


#### Examples

__Let's draw three rectangles!__

If we draw three rectangles of size 100x200 in a 400x400 canvas, one at (0, 0) and another at (150, 0), and a third at (300, 0), here is the result and the corresponding code:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick="window.open('https://tinyurl.com/yxld47ah')"
    src    ="https://tinyurl.com/y4689hee"
    alt    ="3 green rectangles"
    title  ="3 green rectangles"
  />
</figure>


JavaScript code extract (see [the online example at JS Bin](https://jsbin.com/yefuleq/1/edit?html,output) for the complete running code): ([Local Example - 3 Green Bars](src/3.2.8-example1.html))

<div class="source-code"><ol class="linenums" style="list-style-type:decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawSomething</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'lightgreen'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">100</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">150</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">100</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">300</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">100</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>


__Let's modify the code so that we can draw these rectangles at any X and Y position__

What if we wanted to draw these 3 rectangles at another position, as a group? We would like to draw all of them a little closer to the bottom, for example... Let's add some parameters to the function:  the X and Y position of the rectangles.

The full JavaScript code is (see [online running example](https://jsbin.com/jesonuh/edit?html,output)): ([Local Example - Translated 3 green Bards](src/3.2.8-example2.html))

<div class="source-code"><ol class="linenums" style="list-style-type:decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas</span><span class="pun">,</span><span class="pln"> ctx</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com">// This function is called after the page is loaded</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com">// 1 - Get the canvas</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'myCanvas'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com">// 2 - Get the context</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">=</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com">// 3 - we can draw</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawSomething</span><span class="pun">(</span><strong><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span></strong><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawSomething</span><span class="pun">(</span><strong><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="com">// draw&nbsp;3 rectangles</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'lightgreen'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><strong><span class="pln">x</span><span class="pun">,</span><span class="pln">y</span></strong><span class="pun">,</span><span class="lit">100</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><strong><span class="pln">x</span><span class="pun">+</span><span class="lit">150</span></strong><span class="pun">,</span><span class="pln">y</span><span class="pun">,</span><span class="lit">100</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><strong><span class="pln">x</span><span class="pun">+</span><span class="lit">300</span></strong><span class="pun">,</span><span class="pln">y</span><span class="pun">,</span><span class="lit">100</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>

At line 10, we called the `drawSomething(...)` function with 0 and 100 as parameters, meaning "please add an offset of 0 in X and 100 in Y directions to what is drawn by the function...

If you look at the code of the modified function, you will see that each call to `fillRect(...)` uses the x and y parameters instead of hard coded values. In this way, if we call it with parameters (0, 100), then all rectangles will be drawn 100 pixels to the bottom (offset in y). Here is the result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick="window.open('https://tinyurl.com/yxld47ah')"
    src    ="https://tinyurl.com/y6zntfgt"
    alt    ="rectangles are drawn 100 pixels towards the bottom"
    title  ="rectangles are drawn 100 pixels towards the bottom"
  />
</figure>


__Now, let's draw a small monster's head with rectangles__

Now we can start having some fun... let's draw a monster's head using only rectangles ([online version](https://jsbin.com/viqove/1/edit?html,output)): ([Local Example - Monster](src/3.2.8-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick="window.open('https://tinyurl.com/yxld47ah')"
    src    ="https://tinyurl.com/y4tt9mrg"
    alt    ="monster made of rectangles"
    title  ="monster made of rectangles"
  />
</figure>


An extract of the JavaScript source code is:

<div class="source-code"><ol class="linenums" style="list-style-type:decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// head</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'lightgreen'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln">y</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// eyes</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">+</span><span class="lit">35</span><span class="pun">,</span><span class="pln">y</span><span class="pun">+</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">+</span><span class="lit">140</span><span class="pun">,</span><span class="pln">y</span><span class="pun">+</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// interior of eye</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'yellow'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">+</span><span class="lit">43</span><span class="pun">,</span><span class="pln">y</span><span class="pun">+</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">+</span><span class="lit">143</span><span class="pun">,</span><span class="pln">y</span><span class="pun">+</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Nose</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'black'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">+</span><span class="lit">90</span><span class="pun">,</span><span class="pln">y</span><span class="pun">+</span><span class="lit">70</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">80</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Mouth</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'purple'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">+</span><span class="lit">60</span><span class="pun">,</span><span class="pln">y</span><span class="pun">+</span><span class="lit">165</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>


As you can see, the code uses the same technique, becomes less and less readable. The Xs and Ys at the beginning of each call makes understanding the code harder, etc.

However, there is a way to simplify this => 2D geometric transformations! 


#### Geometric transformations: changing the coordinate system

The idea behind 2D transformations is that instead of modifying all the coordinates passed as parameters to each call to drawing methods like `fillRect(...)`, we will keep all the drawing code "as is". For example, if the monster of our previous example was drawn at (0, 0), we could just translate (or rotate, or scale) the original coordinate system.

Let's take a piece of code that draws something corresponding to the original coordinate system, located at the top left corner of the canvas:

<div class="source-code"><ol class="linenums" style="list-style-type:decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// head</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'lightgreen'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// eyes</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">35</span><span class="pun">,</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">140</span><span class="pun">,</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// interior of eye</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'yellow'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">43</span><span class="pun">,</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">143</span><span class="pun">,</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Nose</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'black'</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">90</span><span class="pun">,</span><span class="lit">70</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">80</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Mouth</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'purple'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">60</span><span class="pun">,</span><span class="lit">165</span><span class="pun">,</span><span class="lit">80</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// coordinate system at (0, 0)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;drawArrow</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;drawArrow</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

This code is the just the same as in the previous example except that we removed all Xs and Yx in the code. We also added at the end (lines 25-26) two lines of code that draw the coordinate system. The `drawArrow(startX, startY, endX, endY, width, color)` function is a utility function that we will present later. You can see it in the source code of the complete [online example on JS Bin](https://jsbin.com/fidisig/1/edit?html,output): look in the JavaScript tab. ([Local Example - Monster w/ Arrows](src/3.2.8-example4.html))

Note that the X and Y parameters are useless for now...

Result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick="window.open('https://tinyurl.com/yxld47ah')"
    src    ="https://tinyurl.com/yyklrowb"
    alt    ="monster at 0, 0, coordinate system is drawn too as two arrows"
    title  ="monster at 0, 0, coordinate system is drawn too as two arrows"
  />
</figure>


__Translation using `ctx.translate(offsetX, offsetY)`__

Now, instead of simply calling drawMonster(0, 0), we will call first `ctx.translate(100, 100)`, and look at the result (online code: https://jsbin.com/yuhamu/2/edit) ([Local Example - Translated Monster](src/3.2.8-example5.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick="window.open('https://tinyurl.com/yxld47ah')"
    src    ="https://tinyurl.com/y6889etu"
    alt    ="translated monster"
    title  ="translated monster"
  />
</figure>


JavaScript code extract:

<div class="source-code"><ol class="linenums" style="list-style-type:decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> drawMonster</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
</ol></div>

Line 1 changes the position of the coordinate system, line 2 draws a monster in the new translated coordinate system. All subsequent calls to drawing methods will be affected and will work in this new system too.


__Other transformations: rotate, scale__

There are other transformations available:

+ `ctx.rotate(angle)`, with angle in radians. Note that the order of transformations is important: usually we translate, then rotate, then scale... If you change this order, you need to know what you are doing...
+ `ctx.scale (sx, sy)`, where `scale(1, 1)` corresponds to "no zoom", `scale(2, 2)` corresponds to "zooming 2x" and `scale(0.5, 0.5)` corresponds to zooming out to see the drawings half as big as before. If you do not use the same values for sx and sy, you do "asymmetric scaling", you can distort a shape horizontally or vertically. Try changing the values in the source code of the next online examples.

Here is the previous example, but this time we translated the coordinate system, then rotated it with an angle equal to PI/4 , then we scaled it so that units are half as big (see the [example online](https://jsbin.com/sozehu/1/edit?html,js,output)): ([Local Example - Rotated Monster](src/3.2.8-example6.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 12vw;"
    onclick="window.open('https://tinyurl.com/yxld47ah')"
    src    ="https://tinyurl.com/yxd8e86n"
    alt    ="coordinate system translated, rotated and scaled"
    title  ="coordinate system translated, rotated and scaled"
  />
</figure>


And here is the code of the transformations we used, followed by the call to the function that draws the monster:

<div class="source-code"><ol class="linenums" style="list-style-type:decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">4</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">scale</span><span class="pun">(</span><span class="lit">0.5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0.5</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> drawMonster</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
</ol></div>

_Line 1/2/3_ does and _Line 5_ draws the monster in this new translated, rotated, scaled coordinate system:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/yxld47ah" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
    src    ="https://tinyurl.com/y325erh4"
    alt    ="translate coordinate system"
    title  ="translate coordinate system"
    >
    <img style="margin: 0.1em;" height=200
    src    ="https://tinyurl.com/y64zhwde"
    alt    ="rotate coordinate system"
    title  ="rotate coordinate system"
    >
    <img style="margin: 0.1em;" height=200
    src    ="https://tinyurl.com/y57c25w9"
    alt    ="scale coordinate system"
    title  ="scale coordinate system"
    >
    <img style="margin: 0.1em;" height=200
    src    ="https://tinyurl.com/yxd8e86n"
    alt    ="coordinate system translated, rotated and scaled"
    title  ="coordinate system translated, rotated and scaled"
    >
  </a>
</div>


__BEWARE: all drawings to come will be in that modified coordinate system!__

If we draw two shapes at two different positions, they will be relative to this new coordinate system.

For example, this code (online at https://jsbin.com/yuhamu/4/edit): ([Local Example - Monster w/ Diamon](src/3.2.8-example7.html))

<div class="source-code"><ol class="linenums" style="list-style-type:decimal;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">/</span><span class="lit">4</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">scale</span><span class="pun">(</span><span class="lit">0.5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0.5</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw the monster at (0, 0)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> drawMonster</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Draw a filled rectagle at (250, 0)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">250</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">);</span></li>
</ol></div>

... gives this result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yxld47ah')"
    src    ="https://tinyurl.com/y26lbae8"
    alt    ="monster and rectangle in the same coordinate system"
    title  ="monster and rectangle in the same coordinate system"
  />
</figure>


#### How can we reset the coordinate system, how can we go back to the previous one?

Aha, this is a very interesting question... the answer is in the next page!


#### Knowledge check 3.2.8

<pre>ctx.translate(100, 100);
ctx.scale(2, 2);
ctx.strokeRect(0, 0, 100, 100);
</pre>

1. Where will the rectangle be drawn?<br/>

  a. x=100, y=100, twice the size<br/>
  b. x=0, y=0, twice the size<br/>
  c. x=200, y=200, size unchanged<br/>
  d. x=200, y=200, twice the size<br/>

  Ans: a<br/>
  Explanation: The original coordinate system is translated from (0, 0) to (100, 100), then we apply a scaling x2, so the rectangle will be twice the original size (200x200 instead of 100x100), but the scaling does not change the origin of the coordinate system. To sum up: the rectangle will be drawn in (100, 100), twice the size.


### 3.2.9 Saving and restoring the context

#### Live coding video: saving and restoring the context

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V001600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y27bkcz2)


There are two methods for saving and restoring the context properties: `ctx.save()` and `ctx.restore()`.

What will be saved: `fillStyle` and `strokeStyle`, lineWidth, the previous coordinate system, etc.. Meaning that ALL properties that affect drawing!

A call to `ctx.save()` will probably save the context property values in a hardware register on your graphics card. Multiple contexts can be saved consecutively and restored.

Contexts saved will be stacked, the last one that has been saved will be restored by the next call to `restore()`, so it is very important to have one restore for each save.

<div style="border: 1px solid red; margin: 20px; padding: 10px;">
  <p style="text-align: center;"><em><strong>Best practice</strong>: save the context at the beginning of any function <br>that changes the context, restore it at the end of the function!</em></p>
</div>


#### Example of a function that changes the context and restores it after execution

Online example: https://jsbin.com/moporu/2/edit ([Local Example - Translated Monster](src/3.2.9-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y34n2a5p')"
    src    ="https://tinyurl.com/y5l22xcu"
    alt    ="example of context save / restore : a monster is drawn by a function that saves and restored the context, then a rectangle is draw, with context as it was previously "
    title  ="example of context save / restore : a monster is drawn by a function that saves and restored the context, then a rectangle is draw, with context as it was previously "
  />
</figure>


We took the last example (the one with the monster, from the previous page of the course), and slightly modified the function that draws the monster:

+ We added parameters for setting the position and orientation of the monster, and added calls to `ctx.translate(x, y)` and `ctx.rotate(angle)` in the function.
+ We added parameters for the head color and eye color.
+ We saved the context at the beginning of the function (BEST PRACTICE),
+ We restored it at the end (BEST PRACTICE).

Source code extract of this function: notice at lines 3 and 26 how we save/restore the context at the beginning/end. Right after saving the context, we modify the coordinate system (lines 7-8). The rest of the code is nearly the same as in the last version of the monster example.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> drawMonster</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> angle</span><span class="pun">,</span><span class="pln"> headColor</span><span class="pun">,</span><span class="pln"> eyeColor</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// BEST PRACTICE: SAVE CONTEXT AND RESTORE IT AT THE END</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Moves the coordinate system so that the monster is drawn</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// at position (x, y)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">translate</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">rotate</span><span class="pun">(</span><span class="pln">angle</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// head</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">headColor</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">200</span><span class="pun">,</span><span class="lit">200</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// eyes</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">35</span><span class="pun">,</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">140</span><span class="pun">,</span><span class="lit">30</span><span class="pun">,</span><span class="lit">20</span><span class="pun">,</span><span class="lit">20</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// interior of eye</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">eyeColor</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">43</span><span class="pun">,</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">143</span><span class="pun">,</span><span class="lit">37</span><span class="pun">,</span><span class="lit">10</span><span class="pun">,</span><span class="lit">10</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">...</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="com">// BEST PRACTICE!</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>


#### Knowledge check 3.2.9

<pre>function drawShape(x, y) {
    ctx.translate(x, y);
    ctx.strokeStyle='red';
    ctx.lineWidth=10;
    ctx.strokeRect(0,0,200,200);
 }
</pre>

1. Is the above code well written?<br/>

  a. Yes, but this function changes the context: it should save/restore the context at the beginning/end of its body.<br/>
  b. Yes, I don't see any error in it!<br/>

  Ans: a<br/>
  Explanation: This function changes the context (properties, coordinate system), it should save/restore the context following the good practice presented in this page of the course.
  

### 3.2.10 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ Did you already know about 2D geometric transforms?
+ Have you used 2D geometric transforms in other languages such as Java, Processing, Python, etc.?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will all be glad to try them and give some feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

__Project 1 (easy)__: Make a small drawing by just using rectangles and text  (a car, a monster, a head, or whatever you like).

__Project 2__: Make a histogram (bar charts made of filled rectangles) as an array of integer values such as: `var data = [1, 12, 20, 14, 13, 9, 5]`, for example.

__Project 3 (harder, for those who know JavaScript and a little bit of math)__: Try to draw a human shaped robot using different 2D transforms (translate, rotate). Build a hierarchic skeleton (if we rotate the arm, the forearm and the hand should follow). This can be done by having the function that draws an arm save the context, move the coordinate system, call another function that draws the forearm, that saves the context, move the coordinate system to the end of the arm, call the function that draws the hand, etc. By consecutively calling functions from one another, with each function that saves the context -- moves the coordinate system -- calls another function -- restores the context, we can build a hierarchy of coordinate systems.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4jo6xns')"
    src    ="https://tinyurl.com/y32mh6e8"
    alt    ="Small hierarchized robot"
    title  ="Small hierarchized robot"
  />
</figure>



