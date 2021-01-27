# JavaScript Programming Language

## General

+ [JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-123-javascript-is-the-interactive-glue)
  + the "magic trio" of Web page: HTML5/CSS/Javascript
  + the only programming language that a browser can run
  + w/o installing any plugins or extensions
  + a real standard of Web
  + interactive glue btw HTML and CSS
    + more than just in browser
    + able to be run outside of the browser
      + a node JS interpreter on a remote server
      + in scripts run by the OS

+ Learning JavaScript: [Best practice](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + read and tweak small JavaScript code snippet
  + carfully read the references that details some important parts of the language

+ [Folder structure of Web project](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-134-where-to-put-javascript-code)
  + CSS files in `css` subfolder
  + JavaScript file in `js` subfolder

+ [Example: creating project for math function plot](../WebDev/Frontend-W3C/5-JavaScript/01d-JSIntro.md#note-for-141-creating-an-htmlcssjs-project)


## History

+ [Creation of JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-124-javascript-history)
  + born in 1995
  + creator: Brendan Eich's team
  + organization: Netscape, ancestor of Mozilla
  + in association w/ Sun Microsystems, depending on Java, to provide server and client-oriented solutions
  + ispired by Java but only some naming conventions remaining the same
  + success following the popularity of Netscape Navigator 2 in March 1996
  + quickly integrated into other popular browsers
  + standardized by ECMA as the EcmaScript standard in 1996
  + called JavaScript or EcmaScript

+ [Versions of JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-124-javascript-history)
  + stable version supported by all major browsers: EcmaScript version 5 from 2010
  + EcmaScript 6 or ES 2015: introduced many new features
  + a new version every year w/ some adjustments/novelties
  + ES####: naming convention since 2015, #### = year
  + no global support list for browsers but `caniuse.com` used to check feature by feature

+ [JavaScript programming language](../WebDev/Frontend-W3C/5-JavaScript/01b-JSIntro.md#notes-for-124-javascript-history)
  + the only programming language running in browsers
  + integrated into nearly every popular Web browser
  + some applications compiled from JavaScript/HTML/CSS version into "classic" applications w/o a browser
  + invented to work not only on the client side but also on the server side
  + an interpreted language
  + most popular JavaScript engines
    + [SpiderMonkey](https://developer.mozilla.org/fr/docs/SpiderMonkey) (included in Mozilla Firefox)
    + [JavaScriptCore](https://developer.apple.com/reference/javascriptcore) (included in Apple Safari)
    + [Chrome V8](https://developers.google.com/v8/) (included in Google Chrome, in the Node.js server)
    + [Chakra](https://github.com/Microsoft/ChakraCore) (included in Microsoft Internet Explorer and now in the Microsoft Edge browser)


## Standard and Application APIs

+ [Standard APIs](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-132-what-can-be-done-with-javascript)
  + API: an application programming interface
  + DOM: an object representing the document
  + the selector API:
    + targeting the particular part of the DOM
    + using the same syntax as CSS to select element in the document
  + the DOM API:
    + modifying the HTML content or the style of HTML elements
    + `.innerHTML`
      + modifying content of a document
      + implemented natively by the browser
      + calling serval functions/methods or access properties of the DOM
    + `onclick`
      + listening to click event to call a specific function
      + executing the whole action in the called function
  + `style` property
    + changing the look and feel of the document
    + `style`: an object w/ attributes corresponding to the different CSS properties
    + syntax different from CSS: instead of `-` (dash) in CSS and using CamelCase

+ [Application APIs](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-132-what-can-be-done-with-javascript)
  + bowsers w/ many different libraries as standard APIs
  + W3C standards
  + all browseers following the Web Standards
  + standard APIs
    + multimedia: audio & video
    + geolocation: getting the longitude and latitude
    + orientation: on mobile devices
    + accessing webcam or microphone, etc.

+ [Remote HTTP server](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-132-what-can-be-done-with-javascript)
  + download and upload data from browser to remote Web server
  + __AjaX__ (Asynchronous JAvascript and Xml): term used in JS to download & upload data



## Locations of JS code

+ [Locations of JavaScript Code](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-134-where-to-put-javascript-code)
  + in HTML code between `<script>` and `</script>` tag, either within `<body>...</body>` or `<head>...</head>`
  + external file
    + in local files, usually ending w/ `.js` suffix
    + in external file located on the Web
    + advantages
      + separate HTML and code
      + easier to read and maintain
      + reuse JavaScript code
      + cached JavaScript files to speed up page loads
    + usage
      + link the script file w/ `src` attribute of `<script>` tag
      + JavaScript file must end w/ `.js`
      + no `<script>...</script>` in `.js` file
      + external JavaScript file w/ `<script src="..."></script>` = `<script>...</script>` in HTML
      + multiple JavaScript allowed w/ `<script src="..."></script>`



## Debugging

+ [Debugging in JavaScript](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#note-for-135-how-to-debug-javascript)
  + error messages: printing message for debugging code
  + basics of debuging: seeing error messages
    + in the devtool console
    + in the "console tab" of source code editor

+ [Browser devtool for debugging](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#note-for-135-how-to-debug-javascript)
  + Swiss army knife of JavaScript: browser devtools, in particular, the devtool concole
  + open dev tools of browser
    + Windows: F12 (or ctrl-shift-i)
    + MacOS: cmd-option-i
  + console tab: error message or messages of `console.log(string)` JavaScript function displayed
  + example: `console.log("Some JavaScript code has been executed");`
  + code executed in sequence when the page is loaded
  + error message to debug
    + showing the error message in console tab
    + click the top-right corner on the error message to show the source code
    + the line causing error highlighted


## Data Types




## Numbers




## Strings




## Objects

+ [JavaScript object](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + defined by two braces `{...}` w/ a set of properties/values inside, separated by a comma
  + more structured values

+ [Embedded objects](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + arrays: using brackets to create arrays of things
  + different elements within an arrays seperated by commas `,`



## Functions

+ [JavaScript function](../WebDev/Frontend-W3C/5-JavaScript/01c-JSIntro.md#notes-for-131-the-best-way-to-learn-javascript)
  + a piece of code defined somewhere else
  + accepting parameters to do something
  + function parameters: the data passed to the function




## Operators





