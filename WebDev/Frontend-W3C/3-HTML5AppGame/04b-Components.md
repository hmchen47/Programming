# Module 4: Web components and other HTML5 APIs section

## 4.2 Web Components

### 4.2.1 Web components in video

#### Live coding video: using existing Web components

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3zKZc7F)

__Important note about the above video:__ [webcomponents.org](https://www.webcomponents.org/) and customelements.io have been merged in 2017!

The video uses the customelements.io Web site when searching for Web Components. It has now been merged with the webcomponents.org Web Site. The search field from [webcomponents.org](https://www.webcomponents.org/) is equivalent to the search field that was available on the customelements.io.

The zip file from the video is available for download in the section below.


#### Example from the video

You can download an archive of the example mentioned in the video lecture from: [VideoUsingWebComponents2020.zip](https://bit.ly/3x7eFwS)

You need to unarchive it in the Web server htdocs directory of your WAMP/MAMP/LAMP http distribution, for example. Then open the index.html file located in that directory.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick= "window.open('https://bit.ly/3iGDaMh')"
    src    = "https://bit.ly/3y396kz"
    alt    = "running the example in an Apache Web Server"
    title  = "running the example in an Apache Web Server"
  />
</figure>


### 4.2.2 Introduction

Web components provide a standard way to build your own widgets/components using similar methods to those used by browser developers to construct the `<video>`, `<audio>`, and `<input type="date">` elements, for example.

Web components enable you to use custom HTML elements in your HTML documents, that render as complex widgets: a better-looking calendar, an input text with vocal recognition, a nice chart, etc.

Let's start with an example! This code...:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;x-gif</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://i.imgur.com/iKXH4E2.gif"</span><span class="pln"> </span><span class="atn">ping-pong</span><span class="tag">&gt;&lt;/x-gif&gt;</span></li>
</ol></div>

... renders an animated GIF, and it loops forever in ping-pong mode: the order of the animation is reversed when the last image is reached and again when the animation goes back to the first image.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://geelen.github.io/x-gif/#/https://i.imgur.com/iKXH4E2.gif')"
    src    = "https://bit.ly/3eS1Hgg"
    alt    = "animated gif in a page"
    title  = "animated gif in a page"
  />
</figure>

Click on the image to run the animated GIF  demo, or visit [this Web site](https://geelen.github.io/x-gif/#/https://i.imgur.com/iKXH4E2.gif).

If you look at the source of the demo page, you note the following at the top of the page:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"import"</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"dist/x-gif.html"</span><span class="tag">&gt;</span></li>
</ol></div>

It's called an "HTML import". If your browser supports _HTML imports_, you can now import _another HTML document_, that will come with its own HTML, CSS, and JavaScript code-base, into your HTML page . The code for the animated GIF player, rendered when the browser encounters _the custom HTML element_ `<x-gif>`,  is located in the imported HTML file (and this HTML file can in turn include or define CSS and JavaScript content).

Even more impressive: if you use the devtools or the right click context menu to view the source of the page, you will not see the DOM of this animated GIF player:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3iMBUXQ')"
    src    = "https://bit.ly/3xZ2G5M"
    alt    = "shadow root of the x-gif web component"
    title  = "shadow root of the x-gif web component"
  />
</figure>

_...and your document will still be valid_. Looking at the source code or at the DOM with the devtool's inspector will not reveal the source code (HTML/JavaScript/CSS) used for creating it.


#### Web components availability

There are already hundreds of Web components made by others that you can use. On the [webcomponents.org](https://www.webcomponents.org/) Web site, you will find lots of them. Usually, you need to import the HTML file that defines the components you want to use, and [maybe also a polyfill](https://www.webcomponents.org/polyfills) if you want to use them with browsers that do not yet support Web Components.

_Example:_ let's go to the the [Web Components Web site](https://www.webcomponents.org/).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3iMBUXQ')"
    src    = "https://bit.ly/36ZseUA"
    alt    = "The webcomponents.org home page"
    title  = "The webcomponents.org home page"
  />
</figure>


We then search for Web components tagged with the "voice" tag and find input fields with voice recognition, and a text area that could vocalize the text:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3iMBUXQ')"
    src    = "https://bit.ly/3x3Ij60"
    alt    = "Results for a search on "voice""
    title  = "Results for a search on "voice""
  />
</figure>


Now, please try a [demonstration of this component](https://zenorocha.github.io/voice-elements)!

As you see, re-using Web components is easy :-)

Notice that Google, with its [Polymer project](https://www.polymer-project.org/) and Mozilla, with its [X-Tag library](https://x-tag.github.io/), also offer huge sets of components for creating rich UIs with a common look and feel.


#### Current support

__Web components are built on four different APIS__

In this lesson, we are talking about "Web components". Note that this is not a single API - rather it's what we call an "umbrella API", __built on top of 4 W3C specifications__, which are going to be detailed in subsequent lessons.

The main W3C Web Components resource is on [GitHub](https://github.com/w3c/webcomponents):

1. [The HTML Templates specification](https://www.w3.org/TR/html-templates/)
2. [The Shadow DOM specification](https://www.w3.org/TR/shadow-dom/) (Working Group Note, part of the DOM specification) - see also this MDN's documentation "[Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM)"
3. The Custom Elements specification is being incorporated into the W3C DOM specification and the WHATWG DOM Standard, the W3C HTML specification and the WHATWG HTML Standard, and other relevant specifications. Please check the W3C [Web Components repository](https://github.com/w3c/webcomponents/) for continuing discussions about this subject.
4. [The HTML Imports specification](https://w3c.github.io/webcomponents/spec/imports/) (HTML imports have been deprecated, see further material in this chapter)

You can check the current support for these APIs here: [Microsoft Edge's Web Components](https://bit.ly/3zyCIXi) and on [CanIuse](https://www.caniuse.com/):

+ HTML templates are supported by nearly all modern browsers, including mobile browsers (see also this support table [online](https://caniuse.com/#feat=template)).
+ Shadow DOM v1 is supported by Chrome and Opera, and FireFox/Safari offers partial support (see also [online](https://caniuse.com/#feat=shadowdomv1)).
+ Custom Elements is supported by Chrome and Opera, and FireFox/Safari offers partial support. Edge is implementing them (see also [online](https://caniuse.com/#feat=custom-elementsv1)).
+ HTML Imports is deprecated, but can be used with polyfills . A new way to import Web Components using JavaScript imports is under consideration. More about that in the "HTML imports" material later on.

HTML imports have been replaced by a more standard way involving JavaScript imports (see [discussions](https://bit.ly/36X9wN8)).


#### Notes for 4.2.2 Introduction

+ Web components
  + a standard way to build customer own widget/components
  + using similar methdos to those used by browser developers to construct the `<video>`, `<audio>` and `<input type="date">` elements
  + enabling to use custom HTML elements in HTML documents
  + rendering as complex widgets, such as a better-looking calendar, an input text w/ vocal recognition, a nice chart. etc.
  + [X-Tag library](https://x-tag.github.io/): a lightweight, power-packed Wen Components library
  + example: `<x-gif src="https://i.imgur.com/iKXH4E2.gif" ping-pong></x-fig>`
    + rendering an animated gif
    + looping forever in ping-pong mode
    + reversed order of the animation when the last image reached
    + playing again when the animation foes back to the 1st image

+ HTML import
  + syntax: `<link rel="import" href="dist/x-gif.html>`
  + importing another HTML document
  + including its own HTML, CSS, and JavaScript code-base into the page
  + the code for the animated GIF player located in the import HTML file
  + GIF player rendered when the browser encounters the custom HTML element `<x-fig>`
  + imported HTML file 
    + probably including or defining CSS and JavaScript content
    + no DOM for the animated GIF player
    + unable to view the source code (HTML/CSS/JS) used for creating it

+ Web components availability
  + great collection: [webcomponents.org](https://www.webcomponents.org/)
  + importing the HTML file defining the components used
  + probably importing a polyfill to use them in browsers w/o Web Components supported
  + searching for Web components tagged w/ keywords

+ W3C standard in 2021
  + four different APIs
    + [the HTML Templates specification](https://www.w3.org/TR/html-templates/)
    + [the Shadow DOM specification](https://www.w3.org/TR/shadow-dom/) and [Using shadow DOM](https://mzl.la/2Vc2mly)
    + the Custom Elements specification and W3C [Wen Components repository](https://github.com/w3c/webcomponents/)
    + [the HTML Imports specification](https://w3c.github.io/webcomponents/spec/imports/)
  + current support for these APIs: [MS Edge's Wen Components](https://bit.ly/372rZIc) and [CanIUse](https://www.caniuse.com/)
    + [HTML Template support in CanIuse](https://caniuse.com/#feat=template)
    + []Shadow DOM v1 in CanIuse](https://caniuse.com/shadowdomv1)
    + [Custom Elements in CanIuse](https://caniuse.com/custom-elementsv1)
    + HTML imports deprecated but able to be used polyfill


### 4.2.3 HTML templates

#### Live coding video: HTML templates

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2V5d25z)


#### Overview of HTML Templates

HTML templates are an important building-block of Web components. When you use a custom element like `<x-gif....>`, the browser will (before rendering the document) clone and add  some HTML/CSS/JS code to your document, thanks to the HTML template API that is used behind the scenes.

HTML templates define fragments of code (HTML, JavaScript and CSS styles) that can be reused.

These parts of code are _inert_ (i.e., CSS will not be applied, JavaScript will not be executed, images will not be loaded, videos will not be played, etc.) until the template is used.

Here is an example of code that defines a template:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;template</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mytemplate"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">""</span><span class="pln"> </span><span class="atn">alt</span><span class="pun">=</span><span class="atv">"great image"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"comment"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/template&gt;</span></li>
</ol></div>

Note that it's ok to have the src attribute empty here, we will initialize it when the template is activated.


#### To use a template, clone its content!

A template has "content" (the lines of code between `<template>` and `</template>`), and to manipulate it we use the DOM API and the content attribute of the DOM node that corresponds to a given template (_line_ 3 of the source code example below).

In order to use a template's content, we clone it using the `document.importNode(templateContent, true)` method, where the node is the template's content and true means "deep copy" the content.

A template is typically used like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#mytemplate'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// Populate the src at runtime.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">t</span><span class="pun">.</span><span class="pln">content</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'img'</span><span class="pun">).</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">'https://webcomponents.github.io/img/logo.svg'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// Clone the template, sort of "instantiation"!</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> clone </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">importNode</span><span class="pun">(</span><span class="pln">t</span><span class="pun">.</span><span class="pln">content</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">clone</span><span class="pun">);</span></li>
</ol></div>

__Explanations:__

+ In this example, _line 1_ assigns the DOM node corresponding to the template we defined to variable `t`.
+ `t.content` (_line 3_) is the root of the subtree in the template (in other words, the lines of HTML code inside the `template element`)
+ Note that we set the value of the `src` attribute of the image inside the template at _line 3_, using a CSS selector on the template's content.
+ _Lines 5 and 6_ clone the template's content and add it to the `<body>` of the document.


#### Example

Here is an [online example at JSBin](https://jsbin.com/dozele/edit) that uses exactly the code presented:

[Local Demo](src/04b-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3eR8M0w')"
    src    = "https://bit.ly/3zudjxM"
    alt    = "template use"
    title  = "template use"
  />
</figure>


And here is the complete source code...

The HTML part:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;template</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mytemplate"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">""</span><span class="pln"> </span><span class="atn">alt</span><span class="pun">=</span><span class="atv">"great image"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"comment"</span><span class="tag">&gt;</span><span class="pln">hello</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/template&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">instantiate</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Instantiate the template</span><span class="tag">&lt;/button&gt;&lt;br&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

The JavaScript part:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> instantiate</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#mytemplate'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// Populate the src at runtime.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; t</span><span class="pun">.</span><span class="pln">content</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'img'</span><span class="pun">).</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="str">'https://webcomponents.github.io/img/logo.svg'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="kwd">var</span><span class="pln"> clone </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">importNode</span><span class="pun">(</span><span class="pln">t</span><span class="pun">.</span><span class="pln">content</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">clone</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 4.2.3 HTML templates

+ HTML template
  + an important building-block of Web Components
  + browser going to clone and add some HTML/CSS/JS code to the document
  + defining fragment of code (HTML, CSS style and JS) for reuse
  + the fragment of code __inert__ until the template is used
    + CSS not applied
    + JS not executed
    + images not loaded
    + video not played
    + etc.
  + content
    + the lines of code btw `<template>` and `</template>`
    + using DOM API to manipulate
    + the content attribute of the DOM node corresponding to a given template

+ Example: define a template

  ```html
  <template id="mytemplate>
    <img src="xyz.png" alt="an image">
    <div class="comment"></div>
  </template>
  ```

+ Cloning contents
  + using the `document.importNode(templateContent, deepCopy)` method
  + node: the template's content
  + `deepCopy`: deep copy the content

+ Example: typical template
  + tasks
    + assign the DOM node corresponding to the template
    + `t.content`: the root of the subtree in the template
    + set image `src` attribute
    + clone the template's content and add to page
  + access template: `var t = document.querySelector('#mytemplate');`
  + populate the src at runtime: `t.content.querySelector('img').src = 'https://webcomponents.github.io/img/log.svg'`
  + clone the template: `var clone = document.importNode(t.content, true); document.body.appendChild(clone);`


### 4.2.4 Shadow DOM

#### Live Coding Video: Shadow DOM

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V003000_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3eXRTkY)


#### Overview of Shadow DOM API

The Shadow DOM API provides DOM encapsulation: it serves to hide what is not necessary to see!

<div style="margin: 10px; padding: 10px; border: 1px solid;">If you are new to programming or object-oriented terminology you may find these references a helpful start:<br><ol>
<li><a href="https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)" target="_blank">Wikipedia offers a description</a>&nbsp;especially of the "information hiding" aspect</li>
<li>MDN offers a <a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects" target="_blank">tutorial in programming JavaScript objects</a></li>
</ol></div>

It is not obvious but the Shadow DOM API is already used by browsers' developers for `<audio>` or `<video>` elements, and also for the new `<input type="date">, <input type="color">` elements, etc.

<div  style="margin: 10px; padding: 10px; border: 1px solid;">
  <p style="color: red;"><strong>The three rules of Shadow DOM:</strong></p>
  <ol style="item-style-type: decimal;">
    <li>With Shadow DOM, elements are associated with&nbsp;a new kind of node:&nbsp;<em>a shadow root</em>.</li>
    <li>An element that has a shadow root associated with it is called&nbsp;<em>a shadow host</em>.</li>
    <li><i>The content of a shadow host isn’t rendered; the content of the shadow root is rendered instead.</i></li>
  </ol>
</div>

NB: Because other browsers do not offer the tool-set, all of the examples we discuss on this subject use Google Chrome or Chromium.


#### Example using the Shadow DOM: the `<video>` element

Let's have a look at a simple `<video>` element.

Open this [JSBin example](https://jsbin.com/mojoqaw/edit?html,output) in your browser, and fire up the devtools console (F12 on Windows/Linux, Cmd-Alt-i on Mac OS):

[Local Demo](src/04b-example02.html)

Click on the "Elements" tab in the devtools, or use the magnifying glass and click on the video, to look at the the DOM view of the video element. You will see the exact HTML code that is in this example, but you cannot see the elements that compose the control bar. You don't have access to the play button, etc.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3ryQDd8')"
    src    = "https://bit.ly/3y6mELT"
    alt    = "devtools2"
    title  = "devtools2"
  />
</figure>


Let's take a look behind the scenes, and see the Shadow DOM associated with the `<video>` element.

First, click on the Settings icon (three vertical dots) and select Settings in the drop down menu: (left diagram)

Then scroll down until you see the "Show user agent shadow DOM" option and check it. Close the panel. (right diagram)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3ryQDd8" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3x7mdQr"
      alt   = "shadow dom in devtools 1"
      title = "shadow dom in devtools 1"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3BKSro7"
      alt   = "Show shadow dom option in devtoops"
      title = "Show shadow dom option in devtoops"
    >
  </a>
</div>


Now, look for the video element again and within the DOM view you should see something new: (left diagram)

Open this shadow root by clicking on it, and move the mouse pointer over the different elements: (right diagram)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3ryQDd8" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3kYsewf"
      alt   = "devtools5 4"
      title = "devtools5 4"
    >
    <img style="margin: 0.1em;" height=200
      src   = "https://bit.ly/3eXZvEa"
      alt   = "devtools5"
      title = "devtools5"
    >
  </a>
</div>


Chrome developers are already using the shadow DOM to define their own Web Components, such as `<video>` or `<audio>` elements! And they use the Shadow DOM to hide the internal plumbing.

Furthermore, there is a kind of "boundary" around the `<video>` element, so that external CSS cannot interfere. The content of the `<video>` element is sandboxed (protected from external CSS selectors, for example, or cannot be accessed using `document.querySelector()`, nor inspected by default, using a DOM inspector). Find further reading on the [concept of sandboxing](https://en.wikipedia.org/wiki/Sandbox_(computer_security)).

<p style="margin: 10px; padding: 10px; border: 1px solid;">Browser developers have been using Web Components for a while, and now it's available to every Web developer!</p>

#### Another simple example

Let's have a look at a very simple example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;div&gt;</span><span class="pln">Hello this is not rendered!</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // the div is the Shadow Host. Its content will not be rendered</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> host </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'div'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Create the shadow ROOT, the root node of the shadow DOM</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // using mode:open makes it available, mode:close would return null</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; const</span><span class="pln"> shadowRoot </span><span class="pun">=</span><span class="pln"> host</span><span class="pun">.</span><span class="pln">attachShadow</span><span class="pun">({</span><span class="pln">mode</span><span class="pun">:</span><span class="pln"> </span><span class="str">'open'</span><span class="pun">});</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // insert something into the shadow DOM, this will be rendered</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; shadowRoot</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">'&lt;h1&gt;Hello Shadow DOM&lt;/h1&gt;'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// Could also use appendChild().</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span><span class="pln"> </span></li>
</ol></div>

_Lines 8 and 11_ show how to associate a shadow root with an existing HTML element. In this example, the `<div>` defined at line 1 is a shadow host, and it is associated with the shadow root which contains three words of text (_line 11_).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3ryQDd8')"
    src    = "https://bit.ly/371LDEh"
    alt    = "Shadow DOM simple example"
    title  = "Shadow DOM simple example"
  />
</figure>


This example illustrates the three rules of the shadow DOM. Let's look at them again:

__The three rules of Shadow DOM:__

1. With Shadow DOM, elements are associated with a new kind of node: a shadow root.
2. An element in the HTML which has a shadow root associated with it is called a shadow host.
3. The content of a shadow host doesn’t appear; the content of the shadow root is rendered instead.

And indeed, the above example (try [the online version here at JSBin](https://jsbin.com/peyuxuq/edit?html,console,output)) renders the content of the shadow root, not the content of the button. In the online example, try to change the text of the div (_line 1_), and you will notice that nothing changes. Then modify the text at line 11 and observe the result

[Local Demo](src/04b-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3ryQDd8')"
    src    = "https://bit.ly/3rze7yR"
    alt    = "Shadow DOM: the shadow root is rendered instead of the shadow host content"
    title  = "Shadow DOM: the shadow root is rendered instead of the shadow host content"
  />
</figure>


#### Notes for 4.2.4 Shadow DOM

+ Shadow DOM API
  + providing DOM encapsulation
  + serving to hide what is not necessary to see
  + already use dby browsers's developers for
    + `<audio>` or `<video>` elements
    + `<input type="date">`, `<input type="color">` elements
    + etc.
  + rules
    + __shadow root:__ elements associated w/ a new kind of node w/ Shadow DOM
    + __shadow host:__ element w/ a shadow root w/ it
    + the content of a shadow host isn't rendered; the content of the shadow root is rendered instead
  + ref: object-oriented technology
    + [information hiding in Wikipedia](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))
    + [Introducing JavaScript objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects), MDN Web Docs

+ `<video>` element as Shadow DOM
  + observation in Chrome:
    + looking at the DOM view of the video element
    + devtools > Elements or using the magnifying glass and click on the video
  + unable to see the elements composing the control bar
  + enabling the Shadow DOM associated w/ the `<video>` element
    + Setting icon > enable 'Show user agent shadow DOM'
    + observing video element again
    + within the DOM view to observe the hidden elements (control components)
  + boundary around of the `<video>` elements
    + external CSS unable to interfer
    + content of the `<video>` element sandboxed
    + protected from external CSS selectors
    + unable to be accessed using `document.querySelector()`
    + nor inspected by default w/ a DOM inspector

+ Example: shadow DOM
  + task: associate a shadow root w/ an existing HTML element
  + HTML snippet: `<div>Hello this is nor rendered~</div>`
  + access element: `var host = document.querySelector('div');`
  + create shadow root: `const shadowRoot = host.attachShadow({mode: 'open'});`
  + insert sth, into the Shadow DOM: `shadowRoot.innerHTML = '<h1>Hello Shadow DOM</h1>';`


### 4.2.5 Shadow DOM: encapsulate code

By mixing templates and the shadow DOM, it is possible to hide a template's content by embedding it in the shadow root. In this scenario, it's easy to encapsulate CSS styles and/or JavaScript code so that it will affect only the content of the shadow root. Conversely, external CSS will not apply inside the shadow root.

This is an important feature: the content of a new "widget" that is hidden in a shadow root is protected from external CSS, scripts, etc.

#### An example that mixes templates and shadow DOM

HTML part:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;template</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mytemplate"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;style&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; h1 </span><span class="pun">{</span><span class="pln">color</span><span class="pun">:</span><span class="pln">white</span><span class="pun">;</span><span class="pln"> background</span><span class="pun">:</span><span class="pln">red</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;/style&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;h1&gt;</span><span class="pln">This is a shadowed H1</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/template&gt;</span></li>
</ol></div>

The JavaScript part:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Instanciate the template</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#mytemplate'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Create a root node under our H1 title</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> host </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#withShadowDom'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">const</span><span class="pln"> shadowRoot </span><span class="pun">=</span><span class="pln"> host</span><span class="pun">.</span><span class="pln">attachShadow</span><span class="pun">({</span><span class="pln">mode</span><span class="pun">:</span><span class="pln"> </span><span class="str">'open'</span><span class="pun">});</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// insert something into the shadow DOM, this will be rendered</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">shadowRoot</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">importNode</span><span class="pun">(</span><span class="pln">t</span><span class="pun">.</span><span class="pln">content</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">));</span><span class="pln"> </span></li>
</ol></div>

[Online example at JSBin](https://jsbin.com/quguwa/edit?html,js,output):

[Local Demo](src/04b-example04.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3y6ZcOL')"
    src    = "https://bit.ly/36ZVR8c"
    alt    = "shadow dom 3"
    title  = "shadow dom 3"
  />
</figure>


Note that once again, the content shown is the shadow root + the styles applied. The styles applied are those defined _in the template's content_ that has been cloned and put inside the shadow root.

NB a little bit of French squeezed past our filters. "Instanciate" in French (and other languages) means "Instantiate" in English. We hope you'll translate, as appropriate; but if you seek definitions or use the word in web-searches, then the English spelling will help!

#### Internal CSS does not apply outside the template/shadow DOM

The CSS inside the template will not affect any other H1 elements on the page. This CSS rule (_lines 2-4_ in the HTML part) will only apply to the template's content, with no side-effects on other elements outside. 

Look at [this example at JSBin](https://jsbin.com/jopabat/edit?html,css,js,output) that uses two H1s in the document: one is associated  with a shadow root (defined in a template with an embedded CSS that selects H1 elements and makes them white on red); whereas the other is located in the body of the document and is not affected by the CSS within the Web Component.

[Local Demo](src/04b-example05.html)

The HTML part:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;template</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mytemplate"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;style&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;&nbsp; h1 </span><span class="pun">{</span><span class="pln">color</span><span class="pun">:</span><span class="pln">white</span><span class="pun">;</span><span class="pln"> background</span><span class="pun">:</span><span class="pln">red</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;/style&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;h1&gt;</span><span class="pln">This is a shadowed H1</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/template&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;h1</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"withShadowDom"</span><span class="tag">&gt;</span><span class="pln">This is a text header</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;h1&gt;</span><span class="pln">Normal header with no shadow DOM associated.</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

We added a new H1 at _line 11_. 

And here is the result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3y6ZcOL')"
    src    = "https://bit.ly/3eWYUm8"
    alt    = "shadow dom 4"
    title  = "shadow dom 4"
  />
</figure>

The second H1 is not affected by the CSS defined in the template used by the first H1. Try to add this CSS rule to this example :

```css
h1 {
  color: green;
}
```

And you should see something like that:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3y6ZcOL')"
    src    = "https://bit.ly/2VgJT7p"
    alt    = "The global CSS rule will affect the H1 in the body of the document, not the one in the shadow DOM."
    title  = "The global CSS rule will affect the H1 in the body of the document, not the one in the shadow DOM."
  />
</figure>


In which the "regular" CSS rule changed the color of the H1 located in the body of the document, not the color of the H1 encapsulated in the Shadow DOM.

#### Notes for 4.2.5 Shadow DOM: encapsulate code

+ Encapsulating code
  + mixing the templates and the shadow DOM
    + possible to hide a template's content by embedding it in the shadow root
    + encapsulating CSS and/or JS code $\to$ affect only the content of the shadow root
    + external CSS not able to apply inside the shadow root
  + the content of a widget:
    + hidden in a shadow root
    + protected from external CSS, JS snippets, etc.
  + CSS inside the template not affected any other elements on the page
  + CSS rule only applying to the template's content w/ no side-effect on other elements outside

+ Example: mixing templates and shadow DOM
  + tasks
    + the content shown as the shadow root + the styles applied
    + styles applied those defined in the template's content
  + HTML template<a name="h1Template"></a>:
    + declare template: `<template id="mytemplate">...</template>`
    + declare CSS style: `<style> h1 { color: white; background: red; } </style>`
    + heading: `<h1> This is a shadowed H1 </h1>`
  + JavaScript snippet:
    + instanciate (instantiate in English) the template: `var t = document.querySelector("#mytemplate"`);`
    + create a root node under H! title: `var host = document.querySelector("#withShadowDom"); const shadowRoot = host.attachShadow({mode: 'open'});`
    + insert sth into the shadow DOM, going to be rendered: `shadowRoot.appendChild(document.importNode(t.content, true));`

+ Example: differentiating the template and noremal elements
  + [HTTP template](#h1Template)
  + HTML snippet:
    + main body: `<body>...</body>`
    + title will be replaced: `<h1 id="withShadowDom">This is a text header</h1>`
    + title will not be replaced: `<h1>Normal header with no shadow DOM associated.<h1>`





