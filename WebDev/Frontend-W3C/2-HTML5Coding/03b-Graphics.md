# Week 3: HTML5 Graphics


## 3.2 Basics of HTML5 canvas


### 3.2.0 Lecture Notes

+ [JavaScript & HTML5](#321-about-javascript-and-html5)
  + adding js code in HTML page: `<script>`...`</script>`
  + JavaScript code executed before the browser could see the rest of the page as the `<script></script>` is located before the `<body>`
  + `console.log(...)`: display in the JavaScript console the message...
  + eg. `<script> console.log("Some JavaScript code has been executed"); </script>`
  + debug:
    + dev. tool on web browser &gt; console tab &ge; error/log msgs
    + allowing to type any JS command

+ [The `<canvas>` element](#322-the-canvas-element)
  + provide scripts with a resolution-dependent bitmap canvas
  + used for rendering graphs, game graphics, or other visual images on the fly
  + designed for pixel-based graphics, while SVG (Scalable Vector Graphics, another W3C standard) for vector-based graphics
  + shapes that canvas JavaScript drawing API supported: lines, rectangles, ellipses, arcs, curves, text, images
  + drawing styles: affect the way shapes drawn, e.g., color, drawing width, shadows, etc.
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
    + [[JavaScript InfoVis Toolkit]](http://thejit.org/): a modular structure, allowing you to only force visitors to download what's absolutely necessary to display your chosen data visualizations
    + [jpGraph](http://jpgraph.net/): a PHP-based solution with a wide range of chart types
    + [Highcharts](http://www.highcharts.com/): a JavaScript charting library with a huge range of chart options available
    + [Google Charts](https://developers.google.com/chart/interactive/docs/): highly flexible and an excellent set of developer tools
    + [Excel](https://tinyurl.com/y43wme3q): a good way of quickly exploring data, or creating visualizations for internal use, but the limited default set of colours, lines and styles make it difficult to create graphics that would be usable in a professional publication or website
    + [CSV](http://en.wikipedia.org/wiki/Comma-separated_values)/[JSON]](http://www.json.org/): common formats for data
    + [Crossfilter](http://square.github.com/crossfilter/): enable clients to wade through their data and create graphs and charts that double as interactive GUI widgets
    + [Tangle](http://worrydream.com/Tangle/): trying to describe a complex interaction or equation, letting the reader tweak the input values and see the outcome for themselves provides both a sense of control and a powerful way to explore data
    + [Polymaps](http://polymaps.org/): a mapping library that is aimed squarely at a data visualization audience
    + [OpenLayers](http://openlayers.org/): probably the most robust of these mapping libraries
    + [Kartograph](http://kartograph.org/): a simple and lightweight framework for building interactive map applications without Google Maps or any other mapping service
    + [Carto](http://cartodb.com/): a must-know sitewith which you can combine tabular data with maps is second to none
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

+ Accessible principles on `<canvas>`
  + providing alternative content for what is drawn on the `<canvas>`
  + exposing the location of shapes, paths, images drawn on the `<canvas>` to assistive technologies
  + visually indicating whether or not a shape in the canvas had keyboard focus

+ `<canvas>` cheetsheet
  + [PDF file](https://tinyurl.com/y6cvfxv9)
  + [HTML file](https://tinyurl.com/kxm2vxf)
  


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


X axis is horizontal, directed to the right
Y axis is vertical, directed downwards






