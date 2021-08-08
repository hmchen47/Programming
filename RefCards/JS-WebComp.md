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





