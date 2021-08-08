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






