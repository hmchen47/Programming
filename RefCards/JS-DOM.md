# JavaScript - Document Object Model (DOM)


## Overview
 
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

+ [Overview of DOM](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#251-introducing-the-dom)
  + Document Object Model (DOM): a modle of the dicument's structure
  + used to render the HTML page on the screen
  + a standard describing how a document must be manipulated
  + defining a "language- and platform natural interface"
  + all browers offerring the same JS DOM API
  + DOM API:
    + a programming interface used to modify the HTML content ot the CSS style of HTML element on the fly
    + providing the `document` object as a structure object
  + `document` object
    + a group of nodes represented as a tree
    + exposing a large set of methods to access and manipulate the structured document
    + method capability:
      + look for nodes (html elements that compose the page)
      + move nodes
      + delete nodes
      + modify nodes (attributes, contents)
      + handle associated events
    + a propert of the global object `window`
    + implicitly `window.document` = `document`
  + types of nodes (most useful ones highlighted)
    + __element__, e.g., `<ul></ul>`
    + __text__, e.g., `<p>the text within the element p is a node of type text</p>`
    + Document, DocumentFragment, DocumentType, Comment, ProcessingInstruction
  + viewing DOM w/ devtool
    + Firfox: devtool > console > type "document.body"
    + Chrome: ([devtool video](https://youtu.be/VYyQv0CSZOE))
      + devtool > console > type "window"
      + devtool > console > type "inspec(document.querySelector("input"));" to focus on 'input' element


## Accessing HTML Elements

+ [The `selector` API](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#253-accessing-html-elements)
  + a way of easily accessing elements in the DOM
  + a way to use CSS selector for requesting the DOM
  + methdos
    + `querySelector`: return the 1st element int he DOM that matched the selector
    + `querySelectorAll`: return a collection of HTML elements of all elements matching the selector
  + example: [typical usage](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example02.html)
    + HTML: `<img src="https://i.imgur.com/Ntvj5rq.png" id="img1" width=200> <img src="https://i.imgur.com/yiU59oi.gif" width=200>`
    + JavaScript
      + initialization: `window.onload = init;`
      + `init` function executed as soon as the page loaded (DOM ready)
  + example: [get all `<li>` directly in a `<ul>` of class nav](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example03.html)
  + example: [display all checked `<input type="checkbox">` elements](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example04.html)
  + example: [change the back ground of all paragraphs](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example04.html)
  + examples: more complex selectors
    + `var el = document.querySelector('#nav ul li');`: all elements `li` in `ul` elements in an element of `id`= `nav`
    + `var els = document.querySelectorAll('ul li:nth-child(even)');`: all li in a ul, but only even elements
    + `var els = document.querySelectorAll('form.test > tr > td');`: all `td` directly in `tr` in a form of class test
    + `querySelectorAll("p.warning, p.error");`: all paragraphs of class warning or error
    + `querySelector("#foo, #bar");`: first element of `id` = `foo` or `id` = `bar`
    + `var div = document.getElementById("bar"); var p = div.querySelector("p");`: first `p` in a `div`

+ [The `getElement` APIs](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#253-accessing-html-elements)
  + able to be replaced by `querySelector` and `querySelectorAll` methods
  + `document.getElementById(identifier)` method
    + return the element which has the `id` “identifier”.
    + equivalent to `document.querySelector("#identifier');`
  + `document.getElementsByTagName(tagName)` method
    + return a list of elements which are named “tagName”.
    + equivalent to `document.querySelectorAll(tagName);`
  + `document.getElementsByClassName(className)` method
    + return a list of elements which have the class “className”.
    + equivalent to `document.querySelectorAll('.className');`




## Manipulating HTML document

+ [Modifying HTML document](../WebDev/Frontend-W3C/5-JavaScript/01f-JSIntro.md#notes-for-163-modifying-an-html-document)
  + selection API:
    + used for "selecting elements in the document"
    + syntax: `document.querySelector("#myId");`
  + DOM API:
    + used for adding content to the body of the page (page = document)
    + syntax: `document.body.innerHTML = "...";`
  + HTML Table JavaScript API: useful for building tables on the fly; e.g.,
    + add new row to end of the table: `var newRow   = tableBody.insertRow();`
    + add cell for the row: `var firstNameCell  = newRow.insertCell(); firstNameCell.innerHTML = firstName;`

+ [Value of a selected DOM node](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#255-modifying-selected-html-elements)
  + the `innerHTML` property
    + useful when changing all the children of a given element
    + used to modify the text content of an element or insert a whole set of HTML element inside another one
    + including all contents and child elements
    + example: `var elem = document.querySelector('#myElem');`
      + replace conetnt: `elem.innerHTML = 'Hello ';`
      + append conetnt: `elem.innerHTML += '<b>Michel Buffa</b>',`
  + the `textContent` property
    + used to read the text content or to modify the content
    + only containing the text content
  + modifying the attributes:
    + directly using the name of attribute as the property
    + `value` property of objects in many cases

+ [Adding new node w/ the DOM API](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#256-adding-new-elements-to-the-dom)
  + create a new element by calling `createElement()` method
    + syntax: `var elm = document.createElement(name_of_the_element)`
    + example: `var li = document.createElement('li');`
  + set some attributes / values / styles for this element, e.g.,
    + `li.innerHTML = '<b>This is a new list item in bold!</b>';` & `li.textContent = 'Another new list item';`
    + `li.style.color = 'green';`
    + `img.src = "https://..../myImage.jpg";` & `img.width = 200;`
  + add the newly created element to another element in the DOM
    + using `append()`, `appendChild()`, `insertBefore()` or the `innerHTML` property

+ [Moving HTML elements](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#257-moving-html-elements-in-the-dom)
  + `append()`, `appendChild()`: adding a new element to an existing one
  + moving from its original location to become a child of the targetElem
  + example: [drag'n'drop](../WebDev/Frontend-W3C/5-JavaScript/src/02d-example13.html)

+ [Removing elements](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#258-removing-elements-from-the-dom)
  + `removeChild()`: remove a chile element from the DOM document
  + removing all children of an element using the `innerHTML` property



## Modifying CSS style

+ [Modifying CSS style](../WebDev/Frontend-W3C/5-JavaScript/01f-JSIntro.md#notes-for-164-modifying-css-styles-on-the-fly)
  + changing the CSS property names to CamelCase as JaVaScript variable names
  + position values (height & width): string values w/ "px" and "%"
  + changing common properties (color, border, background color), e.g.,
    + select element: `divElem = document.querySelector("#theDiv");`
    + modify CSS: `divElem.style.border = "5px dashed purple"; divElem.style.padding = "10px"; divElem.style.backgroundColor = "lightGreen";`
  + changing the background image property w/ external image, e.g.,
    + select element: `divElem = document.querySelector("#theDiv");`
    + modify background: `divElem.innerHTML = ""; divElem.style.width = "100%"; divElem.style.height = "300px"; divElem.style.backgroundImage = "url(https://mainline.i3s.unice.fr/mooc/marioSprite.png)";`
  + using the background image as sprite sheet
    + select element: `divElem = document.querySelector("#theDiv");`
    + animate images: `drawMario(currentImage); currentImage = (currentImage +1) % 3;`
    + draw images

      ```js
      function drawMario(indexImage) {
        divElem.style.marginLeft = leftPos + "px";
        divElem.style.width = "22px";
        divElem.style.height = "32px";
        divElem.innerHTML = "";
        divElem.style.backgroundImage = "url(https://mainline.i3s.unice.fr/mooc/marioSprite.png)";
        divElem.style.backgroundColor = "transparent";
        var offset = indexImage * 24;
        divElem.style.backgroundPosition  = offset + "px";
      }
      ```

+ [The `style` attribute](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#254-changing-the-style-of-selected-html-elements)
  + most common way to modify the CSS style of one of several elements
  + typical usage: `var p = document.querySelector('#paragraph1'); p.style.color = 'red';`
  + rule to change syntax of attribute in JS
    + remove the "-" sign in CSS attributes if presented
    + capitalize the word after the "-" sign
  + most useful CSS properties
    + `color`: changing the color of the text content of selected element(s)
    + `background-color`: the background color of the select element(s)
    + `margin` and `padding`: external and internal space, including `margin-top`, `margin-left`, `margin-bottom`, and `margin-right` and also `padding-top`, etc.
    + `border` and `border-radius`: chnage the border, type, color, thickness, rounded corners, etc.
    + `box-shadow`: add shadow to selected elements
    + `font` and `font-style`: font characters and style (italic, bold, plain)
    + `text-align`: text alignment

+ [The `ClassList` interface](../WebDev/Frontend-W3C/5-JavaScript/02e-Interact.md#254-changing-the-style-of-selected-html-elements)
  + simplifying to manipulate CSS classes of an HTML element
  + acting as a container object and providing a set of methods to manipulate its conetnt
  + applyied to an HTML element and returning a collection of class names
  + typical usage: `var elem = document.querySelector("#id1"); var allClasses = elem.classList;`
  + methods usable on a classList objet
    + methods: `add()`, `remove()`, `toggle()` and `contains()`
    + typical usages:
      + `div.classList.add('foo');`: set "foo" as the class by adding it to the classList
      + `div.classList.contains('foo');`: check that the classList contains the class "foo"
      + `div.classList.remove('foo');`: remove the class "foo" from the list
      + `div.classList.toggle('foo');`: add if not existed or remove if existed the class "foo"
  + example: [add and remove multiple CSS properties](../WebDev/Frontend-W3C/5-JavaScript/src/02e-example07.html)


## Form Validation

+ [Customized validation](../WebDev/Frontend-W3C/2-HTML5Coding/05g-HTMLForms.md#575-changing-the-default-behavior)
  + changing the default behavior, aggregating error messages, removing bubbles, etc.
  + browser built-in validation
    + powerful technique to enhance HTML forms
    + provide interesting features
    + criticized by Web developers
      + not 100% complete, in particular, IE & Safari
      + not possible to aggregate error message, showing error bubble next to the first invalid
      + unable to style bubbles
  + validate API
    + providing enough power to make own validation behavior
    + overridden the default when necessary
    + ref: [Building HTML5 Form Validation Bubble Replacements](https://tinyurl.com/yy85v45z)
  + example: aggregation of error messages + overriding default behavior
    + add an empty unnumbered list (`<ul>`...`</ul>`) to the form in style: `<ul class="error-messages"></ul>`
    + use this class attribute for styling, and hiding by default, the error messages using CSS,: `.error-messages { display: none; ...}`
    + replace the validation UI for all forms via calling `replaceValidationUI(form)` function in JavaScript
    + disable all default behavior
    + add a click listener to the submit button: `submitButton.addEventListener("click", function (event) {...}`
    + get all invalid input fields for that form: `var invalidFields = form.querySelectorAll("input:invalid");`
    + get the value of the name attribute of the corresponding label from each invalid field & build a list of `<li>`...`</li>` to the error message container
    + update the list with the new error messages: `errorMessagesContainer.innerHTML = listHtml;`
    + give focus to the first invalid field and show the error messages container by setting its CSS property `display=block`


## The `<video>` element

+ [DOM JavaScript API](../WebDev/Frontend-W3C/2-HTML5Coding/02b-Multimedia.md#225-control-players-from-javascript)
	+ __methods__: controlling the behavior, such as `play()`, `pause()`, etc.
	+ __properties__:
		+ read/write mode, e.g., volume
		+ read-only mode, e.g., encoding, duration, etc.
	+ __event__:
		+ generated during the lifecycle of the element
		+ processed using JavaScript callbacks
		+ able to send events to control the video player
	+ example:

		<div><ul>
		<li style="margin-bottom: 0px;">var video = document.createElement('video');</li>
		<li style="margin-bottom: 0px;">video.src = 'video.mp4';</li>
		<li style="margin-bottom: 0px;">video.controls = true;</li>
		<li style="margin-bottom: 0px;">document.body.appendChild(video);</li>
		</ul></div>


+ [The `<video>` element JavaScript API](../WebDev/Frontend-W3C/2-HTML5Coding/02b-Multimedia.md#227-the-video-element-javascript-api)
	+ useful for implementing playlists, making custom user interfaces and many other interesting things
	+ use external buttons to control the player's behavior
		+ HTML code
			+ `<button onclick="playVideo();" style="cursor: pointer;">Play</button>`
			+ `<button onclick="pauseVideo();" style="cursor: pointer;">Pause</button>`
		+ JavaScript:
			+ `vid = document.querySelector("#vid");`: get the JavaScript object corresponding to the video element
			+ `vid.play();` & `vid.pause()`: methods from API for plating/pausing the video
			+ `vid.currentTime = 0;`: rewind the video
			+ `vid.load()`: rewind the video to `vid.currentTime = 0` and pause the video
	+ detect end of the video and start another one
		+ HTML code: `vid.addEventListener('ended', playNextVideo, false);`
		+ JavaScript:

			```js
			function playNextVideo(e) {
				// Whatever you want to do after the event, change the src attribute
				// of the video element, for example, in order to play another video
			}
			```

	+ manage playlist
		+ HTML code
			+ `var sources = ["https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4", "https://www.archive.org/.../P1120973_512kb.mp4"];`: a list for videos to play
			+ `<body onload="init()">`: call `init()` as the page loaded
		+ JavaScript:
			+ `myVideo = document.querySelector("#myVideo");`: used the DOM to get the JavaScript object corresponding to the video element
			+ `myVideo.addEventListener('ended', loadAndplayNextVideo, false);`: define the listerner for the `ended` event
			+ `loadNextVideo();`: callback function to react the `ended` event
				+ `currentVideo`: a variable corresonding to the the index of the current video
        + `myVideo.src = sources [currentVideo % sources.length]`: set the `src` of the video element to `sources[0]`, then to `sources[1]`, and module w/ the length of the list to repeat the playing


## The `<audio>` elements

+ [Background music](../WebDev/Frontend-W3C/5-JavaScript/03e-HTML5API.md#351-background-music-streamed)
  + using `WebAudio` API
  + audio element: `<audio src = "https://.../humbug.mp3"  id="audioPlayer"  controls> </audio>`
  + playing music: `function play() {...}`
    + access element: `var player = document.querySelector("#audioPlayer");`
    + play streamed music: `player.play();`
  + pausing music: `function pause() {...}`
    + access element: `var player = document.querySelector("#audioPlayer");`
    + pause playing: `player.pause();`


+ [Sound effect w/ howler.js](../WebDev/Frontend-W3C/5-JavaScript/03e-HTML5API.md#352-sound-effects-using-howlerjs)
  + streamed audio not suitable for short sounds
  + WebAudio API:
    + allowing to download and decode sound samples in memory and play them on demand
    + using nearly zero CPU and w/o delay when playing (no buffering)
    + complicated to use for this purpose
  + [howler.js](https://howlerjs.com/) simplifying the use of the WebAudio API





## The `<track>` element

+ [The `<track>` JavaScript API](../WebDev/Frontend-W3C/2-HTML5Coding/02c-Multimedia.md#237-the-track-javascript-api)
  + powerful API used to develop many interesting features
    + dynamically building a navigation menu
    + synchronizing page content w/ timestamps in the WebVTT file
    + displaying all the subtitles/captions at once
    + making an app for creating on the fly subtitles/captions
    + etc.

+ [The `<track>` element](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-121-the-timed-text-track-api)
  + typically within `<video>` and `<audio>` elements
  + attributes
    + `label`
    + `kind`: subtitle, captions, chapters, matadata, etc.
    + `srclang`: language
    + `src`: a source URL
    + ...

+ [Multiple tracks support](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-121-the-timed-text-track-api)
  + supporting for multiple tracks probably different significantly btw browsers (May 2020)
  + Safari
    + providing a menu to choose which subtitle/track to display
    + `default` attribute: loading the text track by default
  + Chrome & Opera
    + providing a subtitle menu
    + loading the text track which matches the browser's language if existed
    + none loaded if no matching
  + Firefox
    + providing a subtitle menu
    + displaying the first defined text track only if the `default` set
    + loading all tracks in memory as page loaded

+ [WebVTT text racks](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-121-the-timed-text-track-api)
  + [document](https://bit.ly/33RJsl8) in HTML5/HTML5.1 specification
  + enabling to manipulate `<track>` contents from JavaScript
  + cue:
    + element w/ an `id`, a startTime, and an endTime
    + text content: containing HTML tags for styling or associated w/ a "voice"
    + voice element: `<v name_of_speaker> ... </v>`

+ [Values of `readyState` attribute](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-122-the-html-track-element)
  + __0 = NONE__: the text track's cues not obtained
  + __1 = LOADING__: the text track loaded w/o errors yet, further cues able to be added to the track by the parser
  + __2 = LOADED__: the text track loaded w/o errors
  + __3 = ERROR__: the text track enabled but accessing failed, likely missing



## Controls of `<audio>` and `<video>` elements

+ [Control `<audio>` & `<video>` elements](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#332-audio-and-video-player-javascript-api)
  + elements w/ methods, properties/attributes and events to manipulate w/ JS
  + the DOM API
    + methods: controlling behavior, such as `play()`, `pause()`, etc.
    + properties:
      + read/write: volume, current time, etc.
      + read-only mode: encoding, duration, etc.
    + events:
      + generated during the life cycle of the element
      + processed using JS callback
      + possible to trigger event to control the player

+ [JavaScript API for `<video>` and `<audio>` elements](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#332-audio-and-video-player-javascript-api)
  + powerful tools to manipulate element
  + reference: [HTML5 Video Events and API](https://www.w3.org/2010/05/video/mediaevents.html)
  + [event list](https://html.spec.whatwg.org/multipage/media.html#mediaevents)
    + network state: `loadstart`, `progress`, `suspend`, `abort`, `error`, `emptied`, `stalled`
    + ready state: `loadedmetadata`, `loadeddata`, `canplay`, `canplaythrough`, `playing`, `waiting`
    + searching: `seeking`, `seeked`, `ended`
    + playing: `durationchange`, `timeupdate`, `play`, `pause`, `ratechange`
    + element: `resize`, `volumechange`
  + [the most interesting methods, properties, and events provided by the `<video>` element API](../WebDev/Frontend-W3C/2-HTML5Coding/02b-Multimedia.md#226-the-javascript-api)

    <table style="max-width: 100%; border-collapse: collapse; border-spacing: 0px; table-layout: auto border: 2px solid #0f0505; background-color: transparent; margin: 0 auto; width: 60vw;" dir="ltr" rules="all" frame="box" cellpadding="10" border="2">
      <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.w3.org/2010/05/video/mediaevents.html">HTML5 Video Events and API</a></caption>
      <tbody>
      <tr>
      <td style="text-align: center; background-color: cadetblue; width: 5%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Methods</strong></span></td>
      <td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Properties</strong></span></td>
      <td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Events</strong></span></td>
      </tr>
      <tr><td><strong><span style="font-family: 'courier new', courier, monospace;">play()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">currentSrc</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">play</span></strong></td></tr>
      <tr><td><strong><span style="font-family: 'courier new', courier, monospace;">pause()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">currentTime</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">pause</span></strong></td></tr>
      <tr><td><strong><span style="font-family: 'courier new', courier, monospace;">load()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">startTime (readonly)</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">progress</span></strong></td></tr>
      <tr><td><strong>canPlayType()</strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">videoWidth</span></strong></td><td><strong>error</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">videoHeight</span></strong></td><td><strong>timeupdate</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">duration (readonly)</span></strong></td><td><strong>ended</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">ended (readonly)</span></strong></td><td><strong>abort</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">error</span></strong></td><td><strong>empty</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">paused (readonly)</span></strong></td><td><strong>emptied</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">muted</span></strong></td><td><strong>waiting</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">seeking</span></strong></td><td><strong>loadedmetadata</strong></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">volume</span></strong></td><td></td></tr>
      <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">height</span></strong></td><td></td></tr>
      <tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;">width</span></strong></p></td><td></td></tr>
      <tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;" face="courier new, courier, monospace">seekable (readonly)</span></strong></p>
      </td><td></td></tr>
      <tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;">played (readonly)</span></strong></p>
      </td><td></td></tr>
      </tbody>
    </table>



## The `getUserMedia` API - Accessing Webcam & Microphone

+ [The `getUserMedia` API - Webcam access](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#241-webcam)
  + useful for controlling a Webcam video stream
  + one component of the [WebRTC specification](https://www.w3.org/TR/webrtc/)
  + not considered a "real" part of the HTML5 specification
  + dealing w/ video streams: always used in conjunction w/ the `<video>` element
  + specification: https://www.w3.org/TR/mediacapture-streams/
  + Webcam usage
    + set the `srcObject` attribute of a `<video>` element to the live video stream object coming out of the Webcam
    + `navigator.getUserMedia(params)` method: get the stream
    + return an [ES6 promise](https://tinyurl.com/y4atxcjf); ES = ECMAScript
  + mandatory to access the page that contains the JavaScript code through `https://`

+ [The `getUserMedia` API - start/stop the Webcam](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#242-more-on-getusermedia)
  + `navigator.mediaDevices.getUserMedia({audio: true, video: true})`: 
    + parameters to capture the video and the audio from the current device (default Webcam)
    + return an ES6 promise
  + `then(stream)` method: get the current audio/video stream as parameter if success
  + `video.srcObject = stream;`: set the audio/video stream of the default Webcam to the `srcObject` attribute of the video element
  + `video.play();`: displaying stream in the video player
  + `webcamStream = stream;`: store the stream in a global variable
  + `catch((error) => ...)`: catch error event
  + `webcamStream.getTracks()[0].stop(); // audio`: stopping audio of the Webcam
  + `webcamStream.getTracks()[1].stop(); // video`: stopping video of the Webcam

+ [Accessing the microphone](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#243-using-the-microphone)
  + `navigator.getUserMedia({audio:true}, onSuccess, onError)`: capture the microphone input
  + `navigator.getUserMedia({video:true, audio:true}, onSuccess, onError)`: access the video and audio simultaneously
  + [WebRTC](https://www.w3.org/TR/webrtc/): a W3C specification for P2P audio/video/data Real Time Communication

+ [Webcam resolutions](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#244-webcam-resolution)
  + "constraint" object: 
    + As constraints applied to an existing local video stream using the "change constraints" API, where it may cause the video engine to reconfigure the device or codec for that particular stream.
    + As constraints applied to an incoming video stream using the "change constrains" API on a MediaStreamTrack, where it serves to inform the video engine about the desirable properties of the video track, which may lead to the video engine choosing to reencode the video and/or signal a remote video source that it wishes certain constraints to be put in place.
  + [example: different resolutions](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#full-example-choose-between-3-different-resolutions)
    + buttons for different resolutions: `<button id="qvga">QVGA</button>`, `<button id="vga">VGA</button>` & `<button id="hd">HD</button>`
    + initial buttons: ` vgaButton = document.querySelector('button#vga');`, `hdButton = document.querySelector('button#hd');`
    + callback fucntion for different resultions: `getMedia(qvgaConstraints);`, ` getMedia(vgaConstraints);` & `getMedia(hdConstraints);`
    + event listeners:

      ```js
      video.addEventListener('play', function() {
          setTimeout(function() {
                  displayVideoDimensions();
              }, 500);
          });
      }
      ```

    + values for the constraints on resolutions

      ```js
      var qvgaConstraints = {
          video: {
              width: { max: 320 },
              height: { max: 180 }
          }
      };
      ```

  + [rear and front camera in smartphone](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#selecting-the-front-or-rear-camera-on-smartphones)

    ```js
    document.getElementById('flip-button').onclick = function() {
        front = !front;
    };

    // toggle front and back camera (mobile) by clicking a button
    constraints = { video: { facingMode: (front? "user" : "environment") } };
    ```

+ [`MediaDevices.getUserMedia()` - MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)
  + syntax: `var promise = navigator.mediaDevices.getUserMedia(constraints);`
  + parameters
    + `constraints`:
      + a `MediaStreamConstraints` object with two members: `video` and `audio`
      + if the browser cannot find all media tracks with the specified types that meet the constraints given, then the returned promise is rejected with `NotFoundError`
      + `{audio: true, video: true}`: both audio and video without any specific requirements
  + return: a Promise whose fulfillment handler receives a `MediaStream` object when the requested media has successfully been obtained
  + examples
    + `video: {width: 1280, height: 720}` & `video: {width: {min: 1024, ideal: 1280, max: 1920}, height: {min: 576, ideal: 720, max: 1080}}`: request the microphone capabilities w/ additional constraints
    + `{audio: true, video: { facingMode: "user"}}`: prefer the front camera (if one is available) over the rear one
    + `{ audio: true, video: {facingMode: {exact: "environment"}}}`: the rear camera

+ [Accessing Webcam](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#334-using-the-webcam)
  + using `getUserMedia` API for accessing the WebCam
  + example: [callback function](src/03c-example06.html)
    + video element: `<video width=200 height=200 id="video" controls autoplay>`
    + preferred camera resolution: `var constraints = { audio: true, video: { width: 1280, height: 720 } };`
    + callback function

      ```js
      navigator.mediaDevices.getUserMedia(constraints)
      .then(function(mediaStream) {
        var video = document.querySelector('video');
        video.srcObject = mediaStream;
        video.onloadedmetadata = function(e) {
          video.play();
        };
      })
      .catch(function(err) { console.log(err.name + ": " + err.message); });
      ```

  + example: [promises - after DOM ready](src/03c-example07.html)
    + init after DOM ready: `window.onload = init;`
    + raise error message:

      ```js
      function init() {
        navigator.mediaDevices.getUserMedia({audio: true, video: true})
          .then(function (stream) {
              var video = document.querySelector('#video');
              video.srcObject = stream;
              video.play();
          })
          .catch(function(err) {
              alert("something went wrong: " + err)
        });
      }
      ```




## The MediaRecorder API

+ [The MediaRecorder API](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#245-the-mediarecorder-api): [usage procedure](../WebDev/Frontend-W3C/2-HTML5Coding/02d-Multimedia.md#five-steps-are-needed-to-use-the-mediarecorder-object)
  + creating a mediaRecorder from a stream
  + adding a "data handler" and call the `start()` method
    + `var recordedChunks = []; // will hold the recorded stream`: an array of bytes to hold the recorded stream
    + `mediaRecorder.ondataavailable = handleDataAvailable;`: declare the callback function to be called while the stream captured
    + `function handleDataAvailable(event)`: a function collecting the chunk of data that corresponds to a few seconds of video, and store it in the recordedChunks byte array
  + info mediaRecorder to stop while done
    + `mediaRecorder.stop();`: end the periodic execution of the handleDataAvailable method, and stop the data capture
  + creating a blob (large binary object) as the `src` attribute of the video player
    + `recordedChunks` array: a blob
    + `URL.createObjectURL(recordedChunks)`: create another object used as a value to set the `src` attribute
  + download the capture stream
    + creating an invisible link w/ a `download` attribute and a `href` attribute that points to the blob object containing the recorded stream encoded using a given codec
    + generate programmatically a click event on the link


+ [MediaRecorder - MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder)
  + Docstring:
    + Create a new MediaRecorder object, given a MediaStream to record
    + Options available to do things like set the container's MIME type (such as "video/webm" or "video/mp4") and the bit rates of the audio and video tracks or a single overall bit rate.
  + properties:
    + `MediaRecorder.mimeType` (read only): the MIME type selected as the recording container for the MediaRecorder object
    + `MediaRecorder.state` (read only): he current state of the MediaRecorder object (inactive, recording, or paused)
    + `MediaRecorder.stream` (read only): the stream that was passed into the constructor
    + `MediaRecorder.ignoreMutedMedia`: indicate whether the MediaRecorder instance will record input when the input MediaStreamTrack is muted, default: false
    + `MediaRecorder.videoBitsPerSecond` (read only): the video encoding bit rate in use
    + `MediaRecorder.audioBitsPerSecond` (read only): the audio encoding bit rate in use
  + methods
    + `MediaRecorder.pause()`: pause the recording of media
    + `MediaRecorder.requestData()`:
      + a Blob containing the saved data received thus far
      + after calling this method, recording continues, but in a new Blob
    + `MediaRecorder.resume()`: recording of media after having been paused
    + `MediaRecorder.start()`: begin recording media
    + `MediaRecorder.stop()`: stop recording, at which point a `dataavailable` event containing the final Blob of saved data is fired
  + static methods
    + `MediaRecorder.isTypeSupported()`: return a Boolean value indicating if the given MIME media type is supported by the current user agent
  + event handlers
    + `MediaRecorder.ondataavailable`
      + called to handle the `dataavailable` event
      + periodically triggered each time `timeslice` milliseconds of media recorded
    + `MediaRecorder.onerror`: called to handle the `error` event, including reporting errors that arise with media recording
    + `MediaRecorder.onpause`: called to handle the `resume` event, which occurs when media recording resumes after being paused
    + `MediaRecorder.onresume`: called to handle the `resume` event, which occurs when media recording resumes after being paused
    + `MediaRecorder.onstart`: called to handle the `start` event, which occurs when media recording starts
    + `MediaRecorder.onstop`: called to handle the `stop` event, which occurs when media recording ends
  + event
    + listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface
    + `error`: fired when an error occurs, available via the `onerror` property


## The Timed Text Track API

+ [The `TextTrack` object](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-123-the-texttrack-object)
  + containing the cue, not HTML object itself
  + w/ different methods and properties for manipulating track content
  + associated w/ different events

+ [The `mode` property of `TextTrack` objects](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-123-the-texttrack-object)
  + `showing`
    + track already loaded or being loaded by the browser
    + displayed in the video once completely loaded
    + firing event while video played
  + `hidden`
    + track ready loaded or being loaded by the browser
    + firing events while video played
    + nothing visible in the standard video player GUI
  + `disabled`
    + track not loaded
    + stop firing events
  + setting `mode` property as `showing` and `hidden` to force a track to be loaded

+ [Properties & methods of `TextTrack` object](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-124-working-with-cues)
  + properties
    + `kind`
      + equivalent to `kind` attribute of HTML track elements
      + possible values: `"subtitles"`, `"caption"`, `"description"`, `"chapters"`, or `"metadata"`
    + `label`: the label of the track
    + `language`: the language of the text track
    + `mode`: values - "disabled"|"hidden"|"showing"
    + `cues`
      + a list of cues as a `TextTrackCueList` object
      + the complete content of the WebVTT file
    + `activeCues`
      + used in event listeners while video playing
      + corresponding to the cues located in the current time segment
      + start and end time possibly overlapped but rare
      + returning a `TextTrackCueList` object
  + methods
    + `addCue(cue)`: add a cue to the list of cues
    + `removeCue(id)`: return a cue from the list of cues
    + `getCueById(id)`: return the cue w/ a given `id`

+ [Properties & methods of `TexTrackCueList` object](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-124-working-with-cues)
  + object: a collection of cues
  + `ld`: the cue id as written in the starting line of the WebVTT file
  + `startTime` and `endTime`:
    + define the time segment for the cue, in second
    + floating point value
    + not formatted String in the WebVTT file

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://bit.ly/3u8AKda')"
      src    = "https://bit.ly/3eYLZjM"
      alt    = "a webVtt file extract with arrows showing id, startTime, endTime and text"
      title  = "a webVtt file extract with arrows showing id, startTime, endTime and text"
    />
  </figure>

+ [VebVTT file and chapters](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-134-with-a-simple-chapter-navigation-menu)
  + using WebVTT files to define chapters
  + task: display subtitles/caption into `.vtt` files
  + HTML snippet: [video element](#videoElmt)
  + no browser taking chapter track in account

+ [WebVTT file w/ JSON](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-135-with-thumbnails-using-json-cues)
  + possible to use JSON as cue values
  + able to manipulate JSON from JavaScript
  + able to be extracted JSON object w/ `cue.text`
  + a powerful way of embedding metadata
  + particularly used in conjunction w/ listening for cue and track events

+ [Segmenting sound file](../Frontend-W3C/3-HTML5AppGame/01d-Multimedia.md#notes-for-141-creating-tracks-on-the-fly)
  + sound sprites
    + small sounds as parts of a mp3 file
    + able to be played separately
  + each sound defined as a cue in a track associated w/ the `<audio>` element
  + tasks:
    + create a WebVTT file w/ many cues on the fly
    + cut a big sound file into segments
    + play segments on demand
  + defining the different animal sounds in the audio file <a name="sounds"></a>

    ```js
    var sounds = [
        { id: "purr", startTime: 0.200, endTime: 1.800 },
        { id: "meow", startTime: 2.300, endTime: 3.300 },
        { id: "bark", startTime: 3.900, endTime: 4.300 },
        { id: "baa", startTime: 5.000, endTime: 5.800 }
        ...
    ];
    ```

  + ideas
    + create a track on the fly
    + add cues within the track
    + cue created w/ the id, the start and end time taken from the above JavaScript object
    + results: a track w/ individual cues located at the time location of the animal sound file
  + implementation
    + generate buttons in the HTML document
    + excute `getCueById` method when clicked on a button
    + access the start and end time properties of the cue
    + play the sound
  + polyfill for `getCueById`:
    + no available on all browsers yet
    + JavaScript snippet to implement `getCueById`<a name="getCueById"></a>
      + check the type of track: `if (typeof track.getCueById !== "function") {...}`
      + callback function: `track.getCueById = function(d) {...};`
      + access cues: `var cues = track.cues;`
      + iterate on cues: `for (var i=0; i<track.cues.length; i++) { if (cues[i].id === id) { return cues[i]; } }`

+ [Event listeners w/ JSON cue](../Frontend-W3C/3-HTML5AppGame/01d-Multimedia.md#notes-for-142-update-the-document-in-sync-with-a-media-playing)
  + capturing the JSON content of a cue while the video reaches its start time
  + add `cuechange` event listener to `textTrack`: `textTrack.oncuechange = function() {...}`
    + declare variable for active cue: `var cue = this.activeCues[0];`
    + convert text into JSON obj: `var obj = JSON.parse(cue.text);`
    + other actions



## The Web Audio API

+ [Limitations of Standard APIs](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-151-introduction)
  + typical actions for `<audio>` and `<video>` elements: `<audio src="https://.../mooc/LaSueur.mp3">`
    + initiate a network request to stream the content
    + deal w/ decoding/streaming/buffering the incoming data
    + render audio controls
    + update the progress indicator, time, etc.
  + customer player
    + making own controls via the JavaScript API of the `<audio>` and `<video>` elements
    + calling `play()` and `pause()`
    + reading/writing properties such as `currentTime`
    + listening events, such as `ended`, `error`, `timeupdate`, etc.
    + managing a playlist, etc.
  + limitations
    + play multiple sounds or music in perfect sync
    + play non-streamed sounds; games: sounds loaded in memory
    + output directly to the speaker; adding special effects, equalizer, stereo balancing, reverb, etc.
    + any fancy visualizations that dance w/ the music, e.g., waveforms and frequencies
  + solution: [Web Audio API](https://webaudio.github.io/web-audio-api/)

+ [Web Audio concepts](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-151-introduction)
  + canvas used as a graphic context for drawing shapes and handling properties
  + Web Audio API: taking a similar approach, using an `AudioContext` for all its operations
  + audio context: `AudioContext`
    + using Web Audio API to build an "audio routing graph"
    + audio routing graph made of "audio nodes"
      + some nodes types for audio sources
      + built-in nodes for speakers
      + audio effects: delay, reverb, filter, stereo panner, etc.
      + audio analysis: used for creating fancy visualizations of real time signal
      + music synthesis (not covered)
  + [`BaseAudioContext` interface](https://webaudio.github.io/web-audio-api/#BaseAudioContext)
    + not instantiated directly
    + extended by the concrete interfaces `AudioContext` and `OfflineAudioContext`
    + properties: `currentTime`, `sampleRate`, `destination`, `state`, `onstateChange`, `listener`, `audioWorklet`
    + methods: `createAnalyser()`, `createBuffer()`, `createBufferSource()`, `createConstantSource()`, `createChannelMerger()`, `createChannelSplitter()`, `createDelay()`, `createPanner()`, etc.
  + `MediaElementSourceNode`: a special node bridging the streamed audio to the WWW
  + `GainNode`: a node enabling volume control
  + `AudioDestination`: a node corresponding to speaker

+ [Audio graph in devtools](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-151-introduction)
  + Firefox: WebAudio debugger built-in devtools but discontinued in 2019
  + Chrome: w/ extension named "WebAudio Inspector"


+ [Gain node](https://developer.mozilla.org/en-US/docs/Web/API/GainNode)
  + the `GainNode` interface
    + representing a change in volume
    + an AudioNode audio-processing module
    + applied to the input data before its propagation to the output
    + exactly one input and one output w/ the same number of channels
  + `gain` property: corresponding to multiplication applied to the input signal volume
    + value = 1: unchanged volume
    + value < 1: lower the volume
    + value > 1: increasing the global volume, w/ risk of clipping
  + solution to prevent clipping: adding a compressor node

+ [Stereo panner](https://developer.mozilla.org/en-US/docs/Web/API/StereoPannerNode)
  + the `StereoPannerNode` interface
  + representing a simple stereo panner node
  + used to pan an audio stream left or right
  + property `pan`: value $\in [-1, 1]$

+ [Biquad filter](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode)
  + the `BiquadFilterNode` interface
    + representing a simple low-order filter
    + creating via `AudioContext.createBiquadFilterNode()`
    + AudioNode able to represent different kinds of filters, control devices, and graphic equalizers
    + exactly one input and one output
  + properties
    + `frequency`
      + frequency in the current filtering algorithm (Hz); most impactful
      + boosting volume inside the range of frequencies
      + unchanged volume outside the range of frequencies
    + `detune`: detuning of the frequency in cents
    + `Q`
      + Quality factor, a dimensionless parameter describing how underdamped an oscillator or resonator is
      + control the width of the frequency band
      + The greater the Q value, the smaller the frequency band.
    + `gain`
      + the gain used in the current filtering algorithm
      + positive value: corresponding to the boost, in dB, to be applied
      + negative value: attenuation
    + `type`: kind of filtering algorithm, including `lowpass`, `highpass`, `bandpass`, `lowself`, `highself`, `peaking`, `notch`, `allpass`
  + use of `frequency`, `detune` and `Q` depending on type of filtering algorithm
  + demo: [frequency response of various filters](https://webaudioapi.com/samples/frequency-response/)
  + multiple filters often used together

+ [Convolver node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)
  + the `ConvolverNode` interface
    + useful for convolution effects such as reverberation
    + an AudioNode performing a Linear Convolution on a given AudioBuffer
    + often used to achieve a reverb effect
    + exactly one input and one output
  + properties
    + `buffer`: a mono, stereo, or 4-channel AudioBuffer containing impulse response used by the `ConvolverNode` to create the reverb effect
    + `normalize`: a boolean, controlling whether the impulse response from the buffer, scaled by an equal-power normalization
  + effect defined by an impulse response
  + impulse response
    + possibly represented as an audio file, decoded in memory before use
    + able to be recorded from a real acoustic space such as cave
    + able to synthetically generated through a wide variety of techniques

+ [Convolution](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)
  + a mathematical process applied to an audio signal to achieve high-quality linear effect
  + often used to simulate an acoustic space such as a concert hall, cathedral or outdoor amphitheater
  + possibly used for complex filter effcts, example:
    + a muffled sound coming inside from a closet
    + sound underwater
    + sound coming through a telephone
    + playing through a vintage speaker cabinet
  + commonly used in major motion picture and music production

+ [Dynamics compressor node](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode)
  + the `DynamicsCompressorNode` interface
    + providing a compression effect
    + lower the volume of the loudest parts of the signal to help preventing clipping and distortion
    + often used in musical production and game audio
  + properties
    + `threshold`: a k-rate AudioParam representing the decibel value above which the compression will start taking effect
    + `knee`: a k-rate AudioParam containing a decibel value representing the range above the threshold where the curve smoothly transition to the compressed portion
    + `ratio`: a k-rate AudioParam representing the amount of change, in dB, needed in the input for 1 dB change in the output
    + `attack`: a k-rate AudioParam representing the amount of time, in second, required to reduce the gain by 10 dB
    + `release`: a k-rate AudioParam representing the amount of time, in seconds, required to increase the gain by 10 dB
    + `reduction`: the amount of gain reduction currently applied by the compressor to the signal
  + sufficiently adding gain node to compress saturated sound
  + properties of compressor mainly for musicians, not going into detail here

+ [Analyzer node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-155-waveforms)
  + providing real-time frequency and time-doimain analysis information
  + leaving audio stream unchchanged
  + allowing to acqure data about the sound signal played
  + processsing the data via complex computation such as FFT
  + typical operations to perform waveform after DOM ready
    + get audio context: `analyser = audioContext.createAnalyser();`
    + access canvas<a name="canvas"></a> and get properties: `canvas = document.querySelector("#myCanvas"); width = canvas.width; height = canvas.height; canvasContext = canvas.getContext("2d");`
    + call function to build audio graph: `buildAudioGraph();`
    + start animation: `requestAnimationFrame(visualize);`

+ [Basic frequencies visualization](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-156-frequencies)
  + bar chart corresponding to a frequency range
  + frequencies range depending on sample rate of the signal (the audio source) and on the FFT size
  + number of bars = the FFT size / 2
  + the nth bar corresponding to the frequency range $N \times (\text{sampleRate}/\text{fftSize})$. example
    + sample rate: 44100 Hz
    + FFT size: 512
    + 1st bar: $[0, 44100/512) = [0, 86.12)$Hz
    + number of data returned by the analyzer node: fftSize / 2
    + only half of the sample rate
  + height: the strength of the specific frequency bucket

+ [Accurate implementation of volume meter](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-157-volume-meters)
  + the above method inaccurate in terms of real volume meter
  + cwilso approximation
  + SoundSpinning approximation

+ [Applications w/ audio in memory](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-158-sound-samples-loaded-in-memory)
  + no streaming/decoding in real time $\to$ less CPU used
  + possible to play in-memory samples in sync w/ great precision
  + possible to make loops, add effects, change the playback rate, etc.
  + no wait time to start playing

+ The [`AudioBufferSourceNode` object](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode)
  + used as the source of the sound sample in the Web Audio graph
  + handling sound samples
  + used only once
  + properties:
    + `buffer`: the decoded sound sample
    + `loop`: boolean value, sound sample played as an infinite loop
    + `loopStart`: a double value, in seconds, indicating the point in buffer where the loop restarts, default value = 0
    + `loopEnd`: a double value, in seconds, indicating the point in buffer where the playing stops, default value = 0
    + `playbackRate`: the speed factor, used to change the pitch of the sample
    + `detune`: a k-rate AudioParam representing detuning of playback in cents, a logarithmic unit of measure used for musicl intervals

+ [The `BufferLoader` utility](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-159-load-and-play-sound-samples)
  + useful for preloading sound & image assets
  + issue: asynchronously request via Ajax
  + applications w/ multiple sound samples: ensuring loaded and decoded them all before starting
  + loading sound samples and triggering event individually $\to$ unable to ensure all sound samples loaded



## Graphics and Animation

+ [HTML5 canvas](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md)
  + a transparent element useful for drawing and animating
  + adding canvas in HTML: `<canvas id="myCanvas" width="200" height="200"></canvas>`
    + not visible: transparent
    + CSS style border to be visible: `canvas { border: 1px solid black; }`
  + best practice
    + use a function called AFTER the page fully loaded, the DOM ready, and select the canvas
    + get a 2D graph context for this canvas
      + an object used to draw on the canvas and to set global properties
      + syntax: `ctx = canvas.getContext('2d');`
    + draw something
      + `ctx.fillRect(x, y, width, height)`: draw a filled rectangle
      + `ctx.strokeRect(x, y, width, height)`: draw a wireframed rectangle
    + use global variables for the canvas and context objects
      + `ctx.fillStyle = 'color';`: set filled color
      + `ctx.strokeStyle = 'color';`: set wireframe color
      + `ctx.lineWidth = number;`: set framewire line width
      + `ctx.beginPath();`: lift pen to begin a new draw, no line btw the previous ned point and the current starting point
      + useful global properties: `w = canvas.width; h = canvas.height;`
    + typical procedure for function to change the context
      + change any properties of global context: 
        + start by saving the content: `ctx.save();`
        + end by restoring it: `ctx.restore();`
      + properties including color, line, width, coordinate system, etc.
      + the change in the function won't effect anything outside the function
  + coordinate system
    + origin: top left of the canvas
    + default: (0, 0)
    + `ctx.translate(x, y)`: relocate the origin to (x, y) of the canvas
    + useful to have multiple shapes by translating the origin

+ [Animation](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#262-animating)
  + ways to animation
    + `setInterval(func, time)`: execute `func` every `time` ms
    + `setTimeout(func, time)`: execute only once after the delay `time` ms
    + `requestAnimationFrame(func)`: request a new frame of animation in 1/60 seconds
  + best practice: `requestAnimationFrame(func)`
  + typical animation loop procedure
    + clear the canvas
    + draw graphic objects / shapes
    + move graphic objects / shapes
    + repeat previous 3 steps
  + optional steps for animation loop
    + observe the keyboard / mouse / gamepad to change status
    + test collisions: decrease one life if player collides
    + test game state: game over if no life left
    + etc.


## Assets Loading

+ [Background loader](../WebDev/Frontend-W3C/5-JavaScript/03e-HTML5API.md#354-advanced-a-multiple-image-sound-and-music-loader)
  + video games usually required to load assets before starting the game
  + assets
    + images: background image, game logo, sprite sheets, etc
    + sound samples: loaded and decoded
    + streamed music w/ `<audio>` element
      + multiple samples elements probably required
      + pause one and start another when changig music
  + alternatively, change `src` attribute


## Example: Canvas and Animation

+ Example: [simple drawing](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md)

+ Example: [function w/ save and restore context](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md)

+ Example: [monster](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md)

+ Example: [moving monster](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#262-animating)

+ Example: [bouncing balls](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#262-animating)

+ [Aminating multiple objects](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#notes-for-263-animating-multiple-objects)
  + example: [3 bouncing balls and the player](src/02f-example06.html)
  + example: [arrays for bouncing balls](src/02f-example07.html)

+ [Mouse position relative to the canvas](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#264-mouse-interactions)

+ [Moving element w/ mouse pointer](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#265-moving-a-player-with-the-mouse)
  + get mouse position in a canvas: `getMousePos(evt)`
  + the mouse cursor out of canvas: `mousePos === undefined`
  + mouse position within the canvas: `player.x = mousePos.x; player.y = mousePos.y;`

+ [Collision detection - Circle & Rectangle](/WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#266-adding-collision-detection)
  + [circle-Rectangle collision detection](https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection)
  + example: [collision detection btw balls & the player](src/02f-example12.html)


+ [Changing variable dynamically - game completion](../WebDev/Frontend-W3C/5-JavaScript/02f-Interact.md#267-adding-input-fields)
  + using `input` fields to change the init variables
  + example: [game to collide selected color balls](../WebDev/Frontend-W3C/5-JavaScript/src/02f-example13.html)


## Example: Audio

+ Example: [sound sample w/ howler.js](../WebDev/Frontend-W3C/5-JavaScript/03e-HTML5API.md#352-sound-effects-using-howlerjs)

+ Example: [adding music amd sound effects for bouncing ball game](/WebDev/Frontend-W3C/5-JavaScript/03e-HTML5API.md#353-adding-music-and-sound-effects)

+ Example: [asset loader](/WebDev/Frontend-W3C/5-JavaScript/03e-HTML5API.md#354-advanced-a-multiple-image-sound-and-music-loader)



## Example: Video

+ Example: [control w/ external buttons](/WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#333-examples-using-the-javascript-api)

+ Example: [playing multiple videos sequentially](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#333-examples-using-the-javascript-api)

+ Example: [player w/ CSS transformation](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#335-extended-examples)

+ Example: [display events and properties](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#335-extended-examples)

+ Example: [buffering status](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#335-extended-examples)

+ Example: [customized player](../WebDev/Frontend-W3C/5-JavaScript/03c-HTML5API.md#335-extended-examples)


## Example: Track

+ Example: [Status of an HTML track](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-122-the-html-track-element)

+ Example: [button to load tracks](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-123-the-texttrack-object)

+ Example: [Accessing `TextTrack` object](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-123-the-texttrack-object)

+ Example: [display the content of a track](../Frontend-W3C/3-HTML5AppGame/01b-Multimedia.md#notes-for-124-working-with-cues)

+ Example: [clickable transcript](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-131-with-a-clickable-transcript-on-the-side)
  + tasks:
    + read a single subtitle file via buttons
    + display the contents of the transcript file on the right container
    + click on cue to force the video to jump to the corresponding location
    + highlight the current text played
  + implementing procedure
    + not loading all tracks at the same time
      + different browsers deciding when and which track to load
      + click button to enforce the loading of the track if not loaded yet
    + iterate through cues and generate the transcript as a set of `<li> ... </li>`
    + define the `id` attribute of the `<li>` element
      + get `id` when clicking on the cue
      + find the corresponding cue start time
      + make the video jump to the time location
    + add `enter` and `exit` listeners
      + use for highlighting the current cue
      + Firefox no supported yet, using `cuechage` event listener instead

+ Example: [download vtt file w/ Ajax/XHR2](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-131-with-a-clickable-transcript-on-the-side)
  + used prior to the track API available
  + download WebVTT files using Ajax and parse manually

+ Example: [display video description](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-132-captions-descriptions-chapters-and-metadata)
  + `mode` property: `disabled`, `hidden`, or `showing`
    + multiple tracks able to be any state
    + event difference: `hidden` tracks able to fire events while `disabled` track unable to fire events
  + tasks
    + showing the use of the `mode` property
    + listening for cue event to capture the current subtitle/caption
    + changing the mode of a track in video element by toggling on the button

+ Example: [subtitle language](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-133-with-buttons-for-choosing-the-subtitle-language)

+ Example: [display English chapters](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-134-with-a-simple-chapter-navigation-menu)

+ Example: [clickable chapters](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-134-with-a-simple-chapter-navigation-menu)

+ Example: [extract JSON object from WebVTT file](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-135-with-thumbnails-using-json-cues)

+ Example: [chapter menu w/ description of chapter markers](../Frontend-W3C/3-HTML5AppGame/01c-Multimedia.md#notes-for-135-with-thumbnails-using-json-cues)
  + procedure: manually capture the images from the video file
    + click on each chapter link to pause video
    + using a screen capture tool to grape each image corresponding to the beginning of chapter
    + resizing the images approximately 200x400 pixels
  + WebVTT w/ chapter

    ```json
    WEBVTT
    
    chapter-1
    00:00:00.000 --> 00:00:26.000
    {
      "description": "Introduction",
      "image": "introduction.jpg"
    }
    
    chapter-2
    00:00:28.206 --> 00:01:02.000
    {
      "description": "Watch out!",
      "image": "watchOut.jpg"
    }
    ...
    ```

+ Example: [add cues to a track on the fly](../Frontend-W3C/3-HTML5AppGame/01d-Multimedia.md#notes-for-141-creating-tracks-on-the-fly)
  + `addTextTrack` method
    + syntax: `addTextTrack(kind[, label[, language]])`
    + docstring: add a TextTrack to a track element
    + parameters
      + `kind`: str; possible values - `subtitles`, `captions`, `chapters`, etc.
      + `label`: str, optional; description of the track
      + `language`: str, optional; usually using abbreviation from BCP-47, like, 'en', 'fr', 'de', etc.
  + VTTCue constructor
    + enable to create cue class-instances programmatically
    + create a cue instance by using `new` keyword

+ [Example: video tracks w/ JSON cue to sync Google map views](../Frontend-W3C/3-HTML5AppGame/01d-Multimedia.md#notes-for-142-update-the-document-in-sync-with-a-media-playing)
  + a demo by Sam Dutton
  + active cue changed $\to$ the Google map and equivalent to Google street view updated

+ Example: [display wikipedia page and a Google map while a video playing](../Frontend-W3C/3-HTML5AppGame/01d-Multimedia.md#notes-for-142-update-the-document-in-sync-with-a-media-playing)


## Example: the Web Audio API

+ Example: [Build audio routing graph](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-151-introduction)

+ Example: [the `MediaElementSource` node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-152-working-with-streamed-content)

+ Example: [Biquad filter](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)

+ Example: [gain node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)

+ Example: [stereo panner](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)

+ Example: [convolver node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)

+ Example: [audio graph of convolver node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)

+ Example: [compressor node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-153-most-useful-filter-nodes)

+ Example: [audio/video equalizer](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-154-writing-an-equalizer)

+ Example: [Build audio/video graph w/ analyzer node](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-155-waveforms)

+ Example: [animation loop](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-155-waveforms)

+ Example: [frequency visualization](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-156-frequencies)

+ Example: [audio graph of fancy frequency visualization](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-156-frequencies)

+ Example: [volume meter of audio player](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-157-volume-meters)
  + tasks:
    + volume meter: tracing upward/downward w/ the intensity of the music
    + compute the average intensity of frequency ranges
    + draw the average intensity w/ gradient-filled rectangle

+ Example: [volume meters of stereo channels](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-157-volume-meters)
  + stereo channels
    + split the audio signal and create a separate analyser for each output channel
    + add `stereoPanner` node right after the source node
    + add a left/right balance slider to control the `pan` property
    + add [Channel Splitter node](https://developer.mozilla.org/en-US/docs/Web/API/ChannelSplitterNode) to isolate right and left channels
  + audio graph

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
        onclick= "window.open("https://bit.ly/3uBXZfy")"
        src    = "https://bit.ly/3i4pvjn"
        alt    = "Audiograph from previous example"
        title  = "Audiograph from previous example"
      />
    </figure>

+ Example: [`AudioBufferSourceNode` to load and decode sound sample](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-159-load-and-play-sound-samples)

+ Example: [preloading sound samples w/ `BufferLoader`](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-159-load-and-play-sound-samples)

+ Example: [playing 2 sound samples w/ different rates](../Frontend-W3C/3-HTML5AppGame/01e-Multimedia.md#notes-for-159-load-and-play-sound-samples)



