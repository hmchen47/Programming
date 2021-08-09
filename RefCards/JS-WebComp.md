# Web Components


## Overview

+ [Web components](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-422-introduction)
  + a standard way to build customer own widget/components
  + using similar methdos to those used by browser developers to construct the `<video>`, `<audio>` and `<input type="date">` elements
  + enabling to use custom HTML elements in HTML documents
  + rendering as complex widgets, such as a better-looking calendar, an input text w/ vocal recognition, a nice chart. etc.
  + [X-Tag library](https://x-tag.github.io/): a lightweight, power-packed Web Components library
  + example: `<x-gif src="https://i.imgur.com/iKXH4E2.gif" ping-pong></x-fig>`

+ [HTML import](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-422-introduction)
  + syntax: `<link rel="import" href="dist/x-gif.html>`
  + importing another HTML document
  + including its own HTML, CSS, and JavaScript code-base into the page
  + the code for the animated GIF player located in the import HTML file
  + GIF player rendered when the browser encounters the custom HTML element `<x-fig>`
  + imported HTML file 
    + probably including or defining CSS and JavaScript content
    + no DOM for the animated GIF player
    + unable to view the source code (HTML/CSS/JS) used for creating it

+ [Web components availability](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-422-introduction)
  + great collection: [webcomponents.org](https://www.webcomponents.org/)
  + importing the HTML file defining the components used
  + probably importing a polyfill to use them in browsers w/o Web Components supported
  + searching for Web components tagged w/ keywords

+ [W3C standard in 2021](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-422-introduction)
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


## HTML Templates

+ [HTML template](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-423-html-templates)
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

+ Example: [define a template](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-423-html-templates)

  ```html
  <template id="mytemplate">
    <img src="xyz.png" alt="an image">
    <div></div>
  </template>
  ```

+ [Cloning contents](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-423-html-templates)
  + using the `document.importNode(templateContent, deepCopy)` method
  + node: the template's content
  + `deepCopy`: deep copy the content

+ Example: [typical template](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-423-html-templates)


## Shadow DOM

+ [The Shadow DOM API](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-424-shadow-dom)
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

+ [`<video>` element as Shadow DOM](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-424-shadow-dom)
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

+ Example: [shadow DOM](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-424-shadow-dom)

+ [Inserting content
  + injection point defined in header part: `<slot name="my-text>...</slot>`
  + injected content defined in body part: `<span slot="my-text">...</span>`
  + when the classic template instantiation and its addition to a shadow host node in the page is done, the HTML produced will contain "Injected Content" instead of

+ Example: ]inserting content](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-426-shadow-dom-insert-content)



## Shadow DOM Encapsulation

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

+ Example: differentiating the template and normal elements


## HTML Custom elements

+ [HTML costom elements](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-427-html-custom-elements)
  + another API described as HTML Web components
  + extending HTML by defining new elements
  + telling the browser how to render them
  + basic syntax: `customElement.define('my-widget', MyWidget);`
  + constraints
    + containing a dash in the element's new name, e.g., `<my-calendar>`, `<app-list>`, etc.
    + `MyWidget`: a JS class object defining the behavior
    + optional 3rd parameter: a JS object containing an extended property, specifying the built-in element inherited
  + local document:
    + the one corresponding to the page to avoid ambiguity of multiple WebComponents files
    + syntax to select: `document.currentScript`
    + selecting the document only in the HTML of document attached to the JavaScript: `var localDoc = document.currentScript.ownerDocument`
    + Web components probably included in other HTML pages
    + good practice: selecting elements only in the HTML page of the Web Components, not in the document that will import the Web Components
  + registration of a new custom element named `<my-widget>`
    + syntax: `customElements.define('my-widget', MyWidget);`
    + when the browser encounters `<my-widget>` within an HTML document, it will create an instance of the `MyWidget` class and render the shadow DOM of the Web Component

+ Example: [custom elements](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-427-html-custom-elements)


## HTML Imports

+ [Replacement of HTML imports](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-428-html-imports)
  + dropped since 2020 and no clear replacement
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

+ [HTML imports](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-428-html-imports)
  + simplest API from Web Components
  + syntax: `<link rel="import" href="your_html_file">`
  + importing all the html/css/js code to define a Web component
    + similar to including CSS in the page
    + package components into an HTML page and import it

+ Example: [html imports](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-428-html-imports)


## Web Components as JS Modules

+ [JavaScrip modules as Web components](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-429-web-components-as-javascript-modules)
  + HTML Imports APIs removed from standard
  + solution: embedding in the JavaScript part of the components
    + the HTML template part of the components
    + the CSS part for the styling of the component
  + able to include the JavaScript as a regular JavaScript file, using 
    + `<script src="yourComponent.js"></script>`
    + the new EcmaScript import statement and import the file as a JS Module

+ Example: [the host html page importing and instantiating the Web Components](../WebDev/Frontend-W3C/3-HTML5AppGame/04b-Components.md#notes-for-429-web-components-as-javascript-modules)




