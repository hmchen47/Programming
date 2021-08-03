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

<div><ol>
<li value="1">&lt;x-gif src="https://i.imgur.com/iKXH4E2.gif" ping-pong&gt;&lt;/x-gif&gt;</li>
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

<div><ol>
<li value="1">&lt;link rel="import" href="dist/x-gif.html"&gt;</li>
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
  + [X-Tag library](https://x-tag.github.io/): a lightweight, power-packed Web Components library
  + example: `<x-gif src="https://i.imgur.com/iKXH4E2.gif" ping-pong></x-fig>`
    + rendering an animated gif
    + looping forever in ping-pong mode
    + reversed order of the animation when the last image reached
    + playing again when the animation force back to the 1st image

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
    + the Custom Elements specification and W3C [Web Components repository](https://github.com/w3c/webcomponents/)
    + [the HTML Imports specification](https://w3c.github.io/webcomponents/spec/imports/)
  + current support for these APIs: [MS Edge's Web Components](https://bit.ly/372rZIc) and [CanIUse](https://www.caniuse.com/)
    + [HTML Template support in CanIuse](https://caniuse.com/#feat=template)
    + [Shadow DOM v1 in CanIuse](https://caniuse.com/shadowdomv1)
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

<div><ol>
<li value="1">&lt;template id="mytemplate"&gt;</li>
<li>&nbsp;&nbsp; &lt;img src="" alt="great image"&gt;</li>
<li>&nbsp;&nbsp; &lt;div class="comment"&gt;&lt;/div&gt;</li>
<li>&lt;/template&gt;</li>
</ol></div>

Note that it's ok to have the src attribute empty here, we will initialize it when the template is activated.


#### To use a template, clone its content!

A template has "content" (the lines of code between `<template>` and `</template>`), and to manipulate it we use the DOM API and the content attribute of the DOM node that corresponds to a given template (_line_ 3 of the source code example below).

In order to use a template's content, we clone it using the `document.importNode(templateContent, true)` method, where the node is the template's content and true means "deep copy" the content.

A template is typically used like this:

<div><ol>
<li value="1">var t = document.querySelector('#mytemplate');</li>
<li>// Populate the src at runtime.</li>
<li>t.content.querySelector('img').src = 'https://webcomponents.github.io/img/logo.svg';</li>
<li> </li>
<li>// Clone the template, sort of "instantiation"!</li>
<li>var clone = document.importNode(t.content, true);</li>
<li>document.body.appendChild(clone);</li>
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

<div><ol>
<li value="1">&lt;template id="mytemplate"&gt;</li>
<li>&nbsp;&nbsp; &lt;img src="" alt="great image"&gt;</li>
<li>&nbsp;&nbsp; &lt;div class="comment"&gt;hello&lt;/div&gt;</li>
<li>&lt;/template&gt; </li>
<li> </li>
<li>&lt;body&gt;</li>
<li>&nbsp;&nbsp; &lt;button onclick="instantiate()"&gt;Instantiate the template&lt;/button&gt;&lt;br&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

The JavaScript part:

<div><ol>
<li value="1">function instantiate() {</li>
<li>&nbsp;&nbsp; var t = document.querySelector('#mytemplate');</li>
<li>&nbsp;&nbsp; // Populate the src at runtime.</li>
<li>&nbsp;&nbsp; t.content.querySelector('img').src = </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;'https://webcomponents.github.io/img/logo.svg';</li>
<li> </li>
<li>&nbsp;&nbsp; var clone = document.importNode(t.content, true);</li>
<li>&nbsp;&nbsp; document.body.appendChild(clone); </li>
<li>}</li>
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
  <template id="mytemplate">
    <img src="xyz.png" alt="an image">
    <div></div>
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
  + populate the src at runtime: `t.content.querySelector('img').src = 'https://webcomponents.github.io/img/logo.svg';`
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
  <p style="color: red;"><strong style="color: red;">The three rules of Shadow DOM:</strong></p>
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

<div><ol>
<li value="1"> &lt;div&gt;Hello this is not rendered!&lt;/div&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp; // the div is the Shadow Host. Its content will not be rendered</li>
<li>&nbsp; &nbsp; var host = document.querySelector('div');</li>
<li> </li>
<li>&nbsp; &nbsp; // Create the shadow ROOT, the root node of the shadow DOM</li>
<li>&nbsp; &nbsp; // using mode:open makes it available, mode:close would return null</li>
<li>&nbsp; &nbsp; const shadowRoot = host.attachShadow({mode: 'open'});</li>
<li> </li>
<li>&nbsp; &nbsp; // insert something into the shadow DOM, this will be rendered</li>
<li>&nbsp; &nbsp; shadowRoot.innerHTML = '&lt;h1&gt;Hello Shadow DOM&lt;/h1&gt;'; // Could also use appendChild().</li>
<li>&lt;/script&gt; </li>
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

+ The Shadow DOM API
  + providing DOM encapsulation
  + serving to hide what is not necessary to see
  + already used by browser's developers for
    + `<audio>` or `<video>` elements
    + `<input type="date">`, `<input type="color">` elements
    + etc.
  + rules
    + __shadow root:__ element associated w/ a new kind of node w/ Shadow DOM
    + __shadow host:__ element w/ a shadow root w/ it
    + the content of a shadow host isn't rendered; the content of the shadow root is rendered instead
  + ref: object-oriented technology
    + [information hiding](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)), Wikipedia
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
  + HTML snippet: `<div>Hello, this is not rendered!</div>`
  + access element: `var host = document.querySelector('div');`
  + create shadow root: `const shadowRoot = host.attachShadow({mode: 'open'});`
  + insert sth, into the Shadow DOM: `shadowRoot.innerHTML = '<h1>Hello, Shadow DOM</h1>';`


### 4.2.5 Shadow DOM: encapsulate code

By mixing templates and the shadow DOM, it is possible to hide a template's content by embedding it in the shadow root. In this scenario, it's easy to encapsulate CSS styles and/or JavaScript code so that it will affect only the content of the shadow root. Conversely, external CSS will not apply inside the shadow root.

This is an important feature: the content of a new "widget" that is hidden in a shadow root is protected from external CSS, scripts, etc.

#### An example that mixes templates and shadow DOM

HTML part:

<div><ol>
<li value="1">&lt;template id="mytemplate"&gt;</li>
<li>&nbsp;&nbsp; &lt;style&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; h1 {color:white; background:red}</li>
<li>&nbsp;&nbsp; &lt;/style&gt;</li>
<li>&nbsp;&nbsp; &lt;h1&gt;This is a shadowed H1&lt;/h1&gt;</li>
<li>&lt;/template&gt;</li>
</ol></div>

The JavaScript part:

<div><ol>
<li value="1">// Instanciate the template</li>
<li>var t = document.querySelector('#mytemplate');</li>
<li>&nbsp;</li>
<li>// Create a root node under our H1 title</li>
<li>var host = document.querySelector('#withShadowDom');</li>
<li>&nbsp;</li>
<li>const shadowRoot = host.attachShadow({mode: 'open'});</li>
<li> </li>
<li>// insert something into the shadow DOM, this will be rendered</li>
<li>shadowRoot.appendChild(document.importNode(t.content, true)); </li>
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

<div><ol>
<li value="1">&lt;template id="mytemplate"&gt;</li>
<li>&nbsp;&nbsp; &lt;style&gt;</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp; h1 {color:white; background:red}</li>
<li>&nbsp;&nbsp; &lt;/style&gt; </li>
<li>&nbsp;&nbsp; &lt;h1&gt;This is a shadowed H1&lt;/h1&gt;</li>
<li>&lt;/template&gt; </li>
<li> </li>
<li>&lt;body&gt;</li>
<li>&nbsp;&nbsp; &lt;h1 id="withShadowDom"&gt;This is a text header&lt;/h1&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &lt;h1&gt;Normal header with no shadow DOM associated.&lt;/h1&gt;</li>
<li>&lt;/body&gt;</li>
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
  + CSS rule only applying to the template's content w/o side-effect on other elements outside

+ Example: mixing templates and shadow DOM
  + tasks
    + the content shown as the shadow root + the styles applied
    + styles applied those defined in the template's content
  + HTML template<a name="h1Template"></a>:
    + declare template: `<template id="mytemplate">...</template>`
    + declare CSS style: `<style> h1 { color: white; background: red; } </style>`
    + heading: `<h1> This is a shadowed H1. </h1>`
  + JavaScript snippet:
    + instanciate (instantiate in English) the template: `var t = document.querySelector("#mytemplate"`);`
    + create a root node under H1 title: `var host = document.querySelector("#withShadowDom"); const shadowRoot = host.attachShadow({mode: 'open'});`
    + insert sth into the shadow DOM, going to be rendered: `shadowRoot.appendChild(document.importNode(t.content, true));`

+ Example: differentiating the template and noremal elements
  + [HTTP template](#h1Template)
  + HTML snippet:
    + main body: `<body>...</body>`
    + title will be replaced: `<h1 id="withShadowDom">This is a text header.</h1>`
    + title will not be replaced: `<h1>Normal header with no shadow DOM associated.</h1>`


### 4.2.6 Shadow DOM: insert content

Let's see how to insert content from the host element within the Shadow DOM using slots.

It is possible to define a part of the template into which external HTML content will be "injected". For this, we use the `<slot>...</slot>` element, as shown below:

<div><ol>
<li value="1">&lt;template id="mytemplate"&gt;</li>
<li>&nbsp; &nbsp; &lt;h1 part='heading'&gt;This is a shadowed H1&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &lt;p part="paragraph"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;slot name="my-text"&gt;My default text&lt;/slot&gt;</li>
<li>&nbsp; &nbsp; &lt;/p&gt;</li>
<li>&lt;/template&gt; </li>
<li>&nbsp;</li>
<li>&lt;body&gt;</li>
<li> &lt;h1 id="myWidget"&gt;</li>
<li>&nbsp; &nbsp; &lt;span slot="my-text"&gt;Injected content using slot elem&lt;/span&gt;</li>
<li> &lt;/h1&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

__Explanations:__

+ Look at _line 4_, this is the "injection point"'!
+ And _line 10_ is the content which will be injected into the template code. So, when the classic template instantiation and its addition to a shadow host node in the page is done, the HTML produced will contain "Injected Content" instead of <slot mname="my-text"></slot>.

See [the complete online example at JSBin](https://jsbin.com/jepucoz/edit?html,js,output):

[Local Demo](src/04b-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/371mqtG')"
    src    = "https://bit.ly/2UXgH5N"
    alt    = "Content injection in HTML templates using slot elements"
    title  = "Content injection in HTML templates using slot elements"
  />
</figure>

#### External resources

+ An MDN article on "[Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_templates_and_slots)"
+ Medium articles:
  + "[Add Flexibility to Web Components With Slots](https://bit.ly/3i9PPZc)"
  + "[Creating Web Components — Templates and Slots](https://bit.ly/2ULQgjv)"


#### Notes for 4.2.6 Shadow DOM: insert content

+ Inserting content
  + injection point defined in header part: `<slot name="my-text>...</slot>`
  + injected content defined in body part: `<span slot="my-text">...</span>`
  + when the classic template instantiation and its addition to a shadow host node in the page is done, the HTML produced will "Injected Content" instead of

+ Example: inserting content
  + template snippet: `<template id="mytemplate">...</template>`
    + H1 title: `<h1 part="heading">This is a shadow H1</h1>`
    + paragraph contents: `<p par="paragraph">...</p>`
    + injection point: `<slot name="my-text">My default text</slot>`
  + body contents: `<body>...</body>`
    + h1 title: `<h1 id="myWidget">...<h1>`
    + span element injected into the template code: `<span slot="my-text">Injected content using slot elem</span>`

+ Resources:
  + [Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_templates_and_slots)
  + Medium articles:
    + "[Add Flexibility to Web Components With Slots](https://bit.ly/3i9PPZc)"
    + "[Creating Web Components — Templates and Slots](https://bit.ly/2ULQgjv)"


### 4.2.7 HTML Custom elements

#### Custom elements

HTML Custom Elements is another API described as HTML Web components. It allows you to extend HTML by defining new elements, and to tell the browser how to render them.

Basic usage:

<div><ol>
<li value="1">customElements.define('my-widget', MyWidget);</li>
</ol></div>

This is done using JavaScript and there are some constraints:

1. The element's new name should have a dash (ex: `<my-calendar>`, `<app-list>`, etc.)
2. The second parameter is a JavaScript class object that defines the behavior of the element. See further examples.

Optionally, a third parameter can be used: a JavaScript object containing an extends property, which specifies the built-in element your element inherits from if any:

<div><ol>
<li value="1">customElements.define('my-widget', MyWidget, { extends: 'p' });</li>
</ol></div>

"Inheritance" is another aspect of object-oriented programming. If it is new to you, please see earlier reference material.

Here is an example which defines a new element named <my-widget>, that will render as an instance of a template with a shadow DOM:

HTML code for the use of the custom element:

<div><ol>
<li value="1">&lt;body&gt;</li>
<li> &lt;my-widget&gt;</li>
<li>&nbsp; &nbsp;&lt;span slot="my-title"&gt;Title injected&lt;/span&gt;</li>
<li>&nbsp; &nbsp;&lt;span slot="my-paragraph"&gt;Paragraph injected&lt;/span&gt;</li>
<li> &lt;/my-widget&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

Look at lines 2 and 5...

HTML code for the declaration of the template (the same as in one of the previous examples):

<div><ol>
<li value="1">&lt;template id="mytemplate"&gt;</li>
<li>&nbsp; &lt;style&gt;</li>
<li>&nbsp; &nbsp; h1 {</li>
<li>&nbsp; &nbsp; &nbsp; color:white;</li>
<li>&nbsp; &nbsp; &nbsp; background:red;</li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; &lt;/style&gt;</li>
<li>&nbsp; &lt;h1&gt;</li>
<li>&nbsp; &nbsp; &lt;slot name="my-title"&gt;My default text&lt;/slot&gt; </li>
<li>&nbsp; &lt;/h1&gt;</li>
<li>&nbsp; &lt;p&gt;</li>
<li>&nbsp; &nbsp; &lt;slot name="my-paragraph"&gt;My default text&lt;/slot</li>
<li>&nbsp; &lt;/p&gt;</li>
<li>&lt;/template&gt;</li>
</ol></div>

JavaScript code:

<div><ol>
<li value="1">// TIP : use "document.currentScript" here to select</li>
<li>// the "local document", the one corresponding to this page.</li>
<li>// this may avoid problems when multiple WebComponents files</li>
<li>// are inserted in the same document. See below...</li>
<li>var localDoc = document.currentScript.ownerDocument;</li>
<li>&nbsp;</li>
<li>class MyWidget extends HTMLElement {</li>
<li>&nbsp; constructor() {</li>
<li>&nbsp; &nbsp; super(); // mandatory</li>
<li>&nbsp; &nbsp; const shadowRoot = this.attachShadow({mode: 'open'});</li>
<li> </li>
<li>&nbsp; &nbsp; // instanciate template</li>
<li>&nbsp; &nbsp; let t = localDoc.querySelector('#mytemplate');</li>
<li>&nbsp; &nbsp; // add it to the shadow DOM</li>
<li> </li>
<li>&nbsp; &nbsp; shadowRoot.appendChild(document.importNode(t.content, true));</li>
<li>&nbsp; }</li>
<li>}</li>
<li>&nbsp;</li>
<li>try {</li>
<li>&nbsp; // Define the custom element to the browser</li>
<li>&nbsp; <strong style="color: red;">customElements</strong><strong style="color: red;">.define('my-widget', MyWidget);</strong></li>
<li>&nbsp; console.log("Element defined");</li>
<li>} catch (error) {</li>
<li>&nbsp; console.log(error);</li>
<li>}</li>
</ol></div>

__Explanations:__

+ _Line 5_: we use this particular selector for safety. It means "select the element only in the HTML of the document that is attached to this JavaScript. Web Components might be included in other HTML pages, as we will see in the next pages of this course. A good practice is to select elements only in the HTML page of the Web Component, not in the document that will import the Web Component.
+ _Line 7_: definition of the Web Component class attached to the custom element `<my-widget>`
+ _Lines 8-17_:  the constructor definition for the class always starts by calling super() so that the correct prototype chain is established. Inside the constructor, we define all the functionality the element will have. Very often this starts by cloning a template in the Shadow DOM.
+ _Lines 22_: registration of a new custom element named `<my-widget>`. When the browser encounters `<my-widget>` within an HTML document, it will create an instance of the `MyWidget` class and render the shadow DOM of the Web Component.

#### Full example

Now, we can use the newly created element and inject content.  The template used here is the last one we studied in a previous lesson about HTML templates. Check the [full example online at JSBin](https://jsbin.com/cacuvuf/edit?html,js,console,output):

[Local Demo](src/04b-example07.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3i8fCRx')"
    src    = "https://bit.ly/37bLjml"
    alt    = "Custom element full example at JsBin"
    title  = "Custom element full example at JsBin"
  />
</figure>


#### External resources

This lesson is only an introduction to custom elements. Here are a few pointers for learners who would like to see how a custom element can inherit from another custom element.

+ MDN article: [Using Custom Elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)
+ From Google devs: [Custom Elements v1: Reusable Web Components](https://developers.google.com/web/fundamentals/web-components/customelements)


#### Notes for 4.2.7 HTML Custom elements

+ HTML costom elements
  + another API described as HTML Web components
  + extending HTML b y defining new elements
  + telling the browser how to render them
  + basic syntax: `customElement.define('my--widget', MyWidget);`
  + constraints
    + containing a dash in the element's new name, e.g., `<my-calendar>`, `<app-list>`, etc.
    + `MyWidget`: a JS class object defining the behavior
    + optional 3rd parameter: a JS object containing an extended property, specifying the built-in element inherited
  + `document.currentScript` syntax
    + selecting the "local document", the one corresponding to the page to avoid ambiguity of multiple WebComponents files
    + `var localDoc = document.currentScript.ownerDocument`: select the document only in the HTML of document attached to the JavaScript
    + Web components probably included in other HTMLpages
    + good practice: selecting elements only in the HTML page of the Web Component, not in the document that will import the Web Component
  + registration of a new custom element named `<my-widget>`
    + syntax: `customElements.define('my-widget', MyWidget);`
    + when the browser encounters `<my-widget>` within an HTML document, it will create an instance of the `MyWidget` class and render the shadow DOM of the Web Component

+ Example: custom elements
  + HTML snippet in body part:
    + custom element: `<my-widget>...</my-widget>`
    + title slot: `<span slot='my-text'>Title injected`
    + paragraph slot: `<span slot="my-paragraph'>Paragraph injected`
  + HTML template: `<template id="mytemplate">...</template>`
    + CSS style: `<style>h1 { color: white; background: red; }</style>`
    + H1 element: `<h1> <slot name="my-title">My default text</slot> </h1>`
    + paragraph element: `<p> <slot name="my-paragraph">My default text</slot> </p>`
  + JavaScript snippet
    + get local document: `var local Doc = document.currentScript.ownerDocument;`
    + define the Web Component class attached tot he custom element `<my-widget>`: `class MyWidget extends HTMLElement {...}`
    + constructor: `constructor() {...}`
      + mandator statement to establish the correct prototype chain: `super();`
      + declare shadow root: `const shadowRoot = this.attachShadow({mode: 'open'});`
      + instantiate template: `let t = localDoc.querySelector("#mytemplate");`
      + add to the shadow DOM: `shadowRoot.appendChild(document.importNode(t.content, true));`
    + exception handler: `try {...} catch(error) { console.log(error); }`
      + define the custom element to the browser: `customElements.define('my-widget', MyWidget);`
      + log msg: `console.log('Element defined');`

+ Resource:
  + [Using Custom Elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)
  + [Custom Elements v1: Reusable Web Components](https://developers.google.com/web/fundamentals/web-components/customelements)


### 4.2.8 HTML Imports

__\*\*\*\*\* Important note \*\*\*\*\*__

As of 2020, HTML imports have been dropped, and there is no clear replacing solution. While you can use polyfills to use existing WebComponents that use them (like the ones from section 4.2.1 - the component that displays animated GIFs, or the voice component), we propose some ways to import WebComponents using JavaScript in the next part of this chapter.

HTML imports have been implemented so far only by Google Chrome. But Google announced that this feature is obsolete since Chrome 73. Although it may still work in some browsers, its use is discouraged since it could be removed at any time. Try to avoid using it!

The reason other browser vendors did not agree to implement them is the merge of ES6 imports and modules. Mozilla, for example, do not want to re-implement something that existed for its main features, covered by ES6 modules (read this [discussion about HTML imports](https://hacks.mozilla.org/2015/06/the-state-of-web-components/)).

When we created this course, Web Components were a hot topic and imports were the only way to reuse external components. Many Web sites still use them, such as YouTube. And Google itself is struggling to replace them, as there is no easy way today to do something 100% equivalent to what HTML imports does today.

There is also an interesting [discussion on the Chromium-dev mailing list](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/h-JwMiPUnuU/sl79aLoLBQAJ) about how HTML imports should be replaced, and about what you can do today to keep your applications working (you will note that I'm part of this discussion too ;-) ).

So... is there a replacement for HTML imports today? The answer is clearly NO. But __there are ways to still use HTML imports__ or to use a more complicated "JavaScript bundler". Also, the people at W3C working on Web Components talk a lot about a future "HTML module" that would do something similar to HTML imports, but this is not even in a specification yet...

Here is where we are:

+ __RECOMMENDED:__ There is a polyfill for HTML imports that works very well. Just include it and your code that use HTML imports will work out of the box on recent browsers (see [ref.](https://github.com/webcomponents/html-imports#dynamic-imports)). We use it on our own applications and it works 100% with cascading imports, imports created dynamically, etc. Very solid.
+ __RECOMMENDED:__ The above polyfill is also integrated in the "Web Component polyfill" that will also emulate other Web Components features (see [webcomponentsjs](https://github.com/webcomponents/webcomponentsjs)). It is  the one used in the course's examples. This "global" polyfill has been made to make apps that use Web Components cross-browser compatible. If you have old Web Components code that use the version 0 of the APIs, you can use its v0 branch and your old code will work on modern browsers . There are also other alternative polyfills for each feature, like [AshleyScirra’s](https://github.com/AshleyScirra/html-imports-polyfill)  but we haven't tried these...
+ __WORKS BUT REQUIRES EXTRA WORK:__ You can bundle the code of your Web Components into a single JavaScript file, using bundlers like [webpack](https://webpack.js.org/) or [parcel](https://parceljs.org/), then use JavaScript modules (`<script type="module" src=...>`).  This is what the Polymer 3 Web Component framework dev team did when they had to remove HTML imports.
+ __MAYBE A FUTURE STANDARD WAY?__ There is a lot of debate in W3C about future "HTML modules" that would do something close to HTML imports did, but while this topic has been under discussion since 2017, it's still not even in a specification. See [the discussion](https://github.com/w3c/webcomponents/blob/gh-pages/proposals/HTML-Imports-and-ES-Modules.md).

__If you want to know what HTML Imports were about...__

HTML Imports is the simplest API from Web components :-)

Add a `<link rel="import" href="your_html_file">` and all the html/css/js code, that defines a Web component you plan to use, will be imported:

+ It is similar to including CSS in your page!
+ Package your components into an HTML page (can include CSS, JS, etc) and import it!

It is as simple as:

<div><ol>
<li value="1">&lt;head&gt;</li>
<li>&nbsp; &nbsp;<strong style="color: red;"> &lt;link</strong><strong style="color: red;"> rel="import" href="components/myComponents.html"&gt;</strong></li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &lt;my-widget&gt;</li>
<li>&nbsp; &nbsp; &lt;span slot="my-title"&gt;Title injected&lt;/span&gt;</li>
<li>&nbsp; &nbsp; &lt;span slot="my-paragraph"&gt;Paragraph injected&lt;/span&gt;</li>
<li>&nbsp; &lt;/my-widget&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

Look at _line 2_: this is where the importation of the HTML, CSS and JS code of new "components" is done. The HTML+JS+CSS code that defines templates, attachment to a shadow host, CSS, and registering of new custom HTML elements is located in `myComponents.html`.

You could create a `my-widget.html` file, add the HTML template and the JavaScript code to that file, and import `my-widget.html` into your document and use `<my-widget>...</my-widget>` from the last lesson directly!

#### External resource

+ MDN's documentation: [HTML Imports](https://developer.mozilla.org/en-US/docs/Web/Web_Components/HTML_Imports)


#### Notes for 4.2.8 HTML Imports

+ Replacement of HTML imports
  + dropped since 202 and no clear replacement
  + implemented only by Google Chrome but obsoleted since Chrome 73
  + many web sites still using them, including YouTube
  + possible replacement solutions:
    + a polyfill for HTML imports (RECOMMENDED)
      + including polyfill into the code $\to$ working out of the box on recent browser
      + using it on applications
      + working 100% w/ cascading imports, imports created dynamically, etc.
    + integrating polyfill in the "Web Component polyfill" (RECOMMENDED)
      + emulating other Web Components features
      + the "global" polyfill made to make apps using Web Components cross-browser compatible
      + old Web Components code using the version 0 of the APIs $\to$ using its v0 branch and old code working on modern browsers
    + bundling the code of Web Components into a single JS file (WORKING BUT EXTRA WORK REQUIRED)
      + using bundler, like [webpack](https://webpack.js.org/) or [parcel](https://parceljs.org/)
      + besides, using JS modules, `<script type="module" src=...>`
      + a.k.a. Polymer 3 Web Component framework
    + HTML modules: under discussion since 2017

+ HTML imports
  + simplest API from Web components
  + syntax: `<link rel="import" href="your_html_file">`
  + importing all the html/css/js code to define a Web component
    + similar to including CSS in the page
    + package components into an HTML page and import it

+ Example: html imports
  + tasks:
    + the importation of the HTML, CSS, and JS code odf new components
    + `myComponents.html` probably containing
      + HTML+JS+CSS code defining templates
      + attachment to a shadow host, CSS
      + registering oof new custom HTML elements
  + HTML head part: `<link rel="import" href="components/myComponents.html">`
  + HTML body part: 
    + add widget: `<my-widget>...</my-widget>`
    + title slot: `<span slot="my-title">Title injected</span>`
    + paragraph slot: `<span slot="my-paragraph">Paragraph injected</span>`


### 4.2.9 Web Components as JavaScript Modules

In the previous section, we said that the proposed way to import Web Components, the so-called HTML Imports API, has been removed from the standard. So.... how can you define a complete Web Component (HTML, CSS, JavaScript) and use it in a HTML page or within the HTML of another component?

Well, if you want to rely only on the Web languages (HTML/CSS/JS), you will have to embed the HTML template part of your component, the CSS part for the styling of your component, in the JavaScript part of your component. Then, you will be able to include the JavaScript that defines your Web Component, as a regular JavaScript file, using `<script src="yourComponent.js"></script>` or using the new EcmaScript import statement and import the file as a ES Module.

Here is an example :

index.html (the host html page that imports and instantiates the Web Components) :

<div><ol>
<li value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li><span>&lt;head&gt;</span></li>
<li><span></span><span>&nbsp; &lt;meta</span><span> </span><span>charset</span><span>=</span><span>"UTF-8"</span><span>&gt;</span></li>
<li><span></span><span>&nbsp; &lt;title&gt;</span><span>WebComponent as aJavaScript module</span><span>&lt;/title&gt;</span></li>
<li><span></span><strong style="color: red;"><span>&nbsp; &lt;script</span><span> </span><span>type</span><span>=</span><span>"module"</span><span> </span><span>src</span><span>=</span><span>"./mycomponent/index.js"</span><span>&gt;&lt;/script&gt;</span></strong></li>
<li><span>&lt;/head&gt;</span></li>
<li><span>&lt;body&gt;</span></li>
<li><span></span><span>&nbsp; <strong style="color: red;">&lt;my-component</strong></span><strong style="color: red;"><span> </span><span>name</span><span>=</span><span>"Michel Buffa"</span><span>&gt;&lt;/my-component&gt;</span></strong></li>
<li><strong style="color: red;"><span></span><span>&nbsp; &lt;my-component</span><span> </span><span>name</span><span>=</span><span>"Marie-Claire Forgue"</span><span>&gt;&lt;/my-component&gt;</span></strong></li>
<li><span>&lt;/body&gt;</span></li>
<li><span>&lt;/html&gt;</span></li>
</ol></div>

__Explanations:__

+ _Line 6_: In this example, the Web Component is in a single JavaScript file (./mycomponent/index.js), that is imported as JavaScript module (`<script type="module"....>`).
+ _Lines 9 and 10_: it can then be used like any Web Component, by adding it with its custom HTML tag (`<my-components>`). The components have one HTML attribute "name".

And here is the code of the Web Component (in `./mycomponent/index.js`):

```js
customElements.define(
    "my-component",
    class extends HTMLElement {
        constructor() {
            super();
            this.root = this.attachShadow({ mode: 'open'});
            this.name = this.getAttribute(name); // get the "name" attribute value
        }

        connectedCallback() {
            // called when the component is added to the DOM of its host
            // css+html
            this.css = `
                #div_menu {
                    border : 1px solid black;
                }
                h1 {
                    color: red;
                }
            `;
            this.html = `
                <div id='div_menu'>
                    <h1>${this.name}
                </div>
            `;
            this.root.innerHTML = "<style>${this.css}</style><div id='wrapper'>${this.html}</div>";
        } //connectedCallback
    } // class extends HTMLElement
);
```


__Explanations:__

+ _Line 1_: we call `customElements.define` and pass as the first parameter the name of the Web Component (here `<my-component>`), and as a second parameter the JavaScript class that defines the Web Component. Instead of using the className, in this example, the class itself is embedded in the call to define(....).
+ _Line 10_: we used the connectedCallback method that is called automatically when  the component is created and connected to the DOM of its host. In this method we use JavaScript template literals to embed the [HTML template](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) of the component and its CSS associated style in the class properties this.html and this.css. This is a convenient way to define in a single line both the HTML and the CSS for the component (this is done in _line 26_).
+ Of course, we could have defined a more complex component. This simple example shows how we can embed the CSS and HTML template in the JavaScript code of the component.


#### Notes for 4.2.9 Web Components as JavaScript Modules

+ JavaScrip modules as Web components
  + HTML Imports APIs removed from standard
  + solution: embedding in the JavaScript part of you components
    + the HTML templaste part of the components
    + the CSS part for the styling of the component
  + able to include the JavaScript as a regular JavaScript file, using 
    + `<script src="yourComponent.js"></script>`
    + the new EcmaScript import statement and import the file as a ES Module
  + `customElement.define`

+ Example: the host html page importing and instantiating the Web Components
  + HTML snippet: `index.html`
    + import the Web Component in a single JS file: `<script type="module" src="./mycomponent/index.js"></script>`
    + add Web component w/ its custom HTML tag: `<my-component name="Michel Buffa"></my-component> <my-component name="Mrie-Claire Forgue"></my=component>`
  + JavaScript snippet: `./mycomponent/index.js`

    ```js
    customElements.define(
        "my-component",
        class extends HTMLElement {
            constructor() {
                super();
                this.root = this.attachShadow({ mode: 'open'});
                this.name = this.getAttribute(name); // get the "name" attribute value
            }

            connectedCallback() {
                // called when the component is added to the DOM of its host
                // css+html
                this.css = `
                    #div_menu {
                        border : 1px solid black;
                    }
                    h1 {
                        color: red;
                    }
                `;
                this.html = `
                    <div id='div_menu'>
                        <h1>${this.name}
                    </div>
                `;
                this.root.innerHTML = "<style>${this.css}</style><div id='wrapper'>${this.html}</div>";
            } //connectedCallback
        } // class extends HTMLElement
    );
    ```


### 4.2.10 Discussion and projects

Here is the discussion forum for this part of the course. Please post your comments/observations/questions and share your creations.

#### Suggested topics of discussion:

+ If you've followed the course, then you've visited the [webcomponents.org](https://www.webcomponents.org/) Web site and browsed some Web components galleries. Did you find any super cool components? Did you try them? Please share your findings in the forum!
+ What Web component would you like to use and could not find out of the box?


#### Optional projects:

+ Try-out [these WebAudio control widgets that look incredibly good](https://github.com/g200kg/webaudio-controls) (I used them with my Guitar Amp Simulator). And use them in your audio player or other applications that would look cool with rotating knobs, switches, LEDs, etc.

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://bit.ly/2TEEyXa" ismap target="_blank">
      <img style="margin: 0.1em;" height=150
        src   = "https://bit.ly/377gOhA"
        alt   = "web audio controls"
        title = "web audio controls"
      >
      <img style="margin: 0.1em;" height=150
        src   = "https://bit.ly/3l60vcW"
        alt   = "guitar amp sim with web components"
        title = "guitar amp sim with web components"
      >
    </a>
  </div>

+ Try making your own Web component! For example: an enhanced audio player that uses Web Audio. 
+ How about building a`<gamepad-tester>` component which will display progress bars and the states of the different buttons/joysticks - reuse the example from the course! I couldn't find any Web component like this! Another challenge ;)
+ Try writing a small tutorial about reusing and customizing a super cool Web component you have found!




