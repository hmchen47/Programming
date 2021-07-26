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

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
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




