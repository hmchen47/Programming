# Module 3: HTML5 file upload and download section


## 3.4 Drag and drop files


### 3.4.1 Introduction

In these lectures, we will learn how to _drag and drop_ files between the browser and the desktop. The process shares similarities with the methods for _dragging and dropping_ elements within an HTML document, but it's even simpler!


#### Moving files from desktop to browser

__Drag and drop files from the desktop to the browser: the `files` property of the clipboard__

The principle is the same as in the examples from the previous section (drag and drop basics), except that we do not need to worry about a `dragstart` handler. __Files will be dragged from the desktop, so the browser only has to copy their content from the clipboard__ and make it available in our JavaScript code.

Indeed, __the main work will be done in the drop handler__, where we will use the `files` property of the `dataTransfer` object (aka the clipboard). This is where the browser will copy the files that have been dragged from the desktop.

This `files` object is the same one we saw in the chapter about the File API in the "HTML5 part 1" course: it is a collection of `file` objects >(sort of file descriptors). From each `file` object, we will be able to extract the name of the file, its type, size, last modification date, read it, etc.

In this source code extract we have a `drop` handler that works on files which have been dragged and dropped from the desktop to a drop zone associated with this handler with an `ondrop=dropHandler(event);` attribute:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> dropHandler</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Do not propagate the event</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">stopPropagation</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Prevent default behavior, in particular when we drop images or links</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// get the dropped files from the clipboard</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">var</span><span class="pln"> files </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">event</span><span class="pun">.</span><span class="pln">dataTransfer</span><span class="pun">.</span><span class="pln">files</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> filenames </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// do something with the files...here we iterate on them and log the filenames</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> files.length&nbsp;</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;filenames </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'\n'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> files</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">name</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">files</span><span class="pun">.</span><span class="pln">length </span><span class="pun">+</span><span class="pln"> </span><span class="str">' file(s) have been dropped:\n'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> filenames</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
</ol></div>

+ _Lines 7-8_ we get the files that have been dropped.
+ _Lines 12-15_ iterate over the collection and build a string which contains the list of file names.
+ _Line 17_ displays this string on the debugging console.

Complete working examples are to be presented later on...


#### Prevent the browser's default behavior

If we drop an image into an HTML page, the browser will open a new tab and display the image. With a .mp3 file, it will open it in a new tab and a default player will start streaming it, etc. We need to prevent this behavior in order to customisethe processing of the dropped files (i.e. display an image thumbnail, add entries to a music playlist, etc.). So, when dragging and dropping images or links, we need to prevent the browser's default behavior.

At the beginning of the `drop` handler in the previous piece of code, you can see the lines of code (_lines 2-5_) that stop the propagation of the drop event and prevent the default behavior of the browser. Normally when we drop an image or an HTTP link onto a web page, the browser will display the image or the web page pointed by the link, in a new tab/window. This is not what we would like in an application using the drag and drop process. These two lines are necessary to prevent the default behavior of the browser:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Do not propagate the event</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">event</span><span class="pun">.</span><span class="pln">stopPropagation</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Prevent default behavior, in particular when we drop images or links</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span><span class="pln"> </span></li>
</ol></div>

<p style="margin: 10px; padding: 10px;"><strong>Best practice</strong>: add these lines to the <code>drop</code>handler AND to&nbsp;the <code>dragOver</code> handler attached to the drop zone!</p>

... like in this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> dragOverHandler</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Do not propagate the event</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">stopPropagation</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Prevent default behavior, in particular when we drop images or links</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> dropHandler</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Do not propagate the event</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">stopPropagation</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Prevent default behavior, in particular when we drop images or links</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">preventDefault</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__External resources__

+ Web.dev article: "[Using the HTML5 drag and drop API](https://web.dev/drag-and-drop/)"
+ HTML Goodies article: "[Drag Files Into the Browser From the Desktop with HTML5](https://bit.ly/2UqW41k)"


#### Notes for 3.4.1 Introduction

+ Moving files from desktop and browser w/ the `files` property
  + no `dragstart` handler required
  + files dragged from the desktop
  + browser only copying their contents from the clipboard
  + main work done in the drop handler
  + `files` property of the `dataTransfer` object used to copy the dragged files from the desktop
  + `files` object: a collection of `file` objects
  + `file` object able to extract the name of the file, type, size, last modificaton date, read it, etc.

+ Example: handling the drop event for dragged files
  + add drop handler: `function dropHandler(evt) {...}`
  + stop propagating event: `evt.stopPropagation();`
  + prevent default behavior: `evt.preventDefault();`
  + get the dropped files from the clipboard: `var files = evt.dataTransfer.files;`
  + init filename: `var filename = "";`
  + iterate to add filenames into string: `for (var i=0; i<files.length; i++) { filenames += '\n' + files[i].name; }`
  + log msg to display filenames: `console.log(files.length + 'file(s) have been dropped:\n' + filenames);`

+ Prevent browser's deafult behavior
  + default behavior
    + dropping an image into an HTML page $\to$ open a new tab and display the image
    + dropping a mp3 file $\to$ open a new tab and start streaming the audio w/ a default player
  + two functions to prevent the default behavior of the browser
    + not propagating the event: `event.stopPropagation();`
    + preventing default behavior, in particular when droopping images or links: `event.preventDefault();`
  + best practice: add `eventPropagation` and `event.preventDefault` to handlers attached to the drop zone
    + the `stop` handler
    + the `dragOver` handler
  + ref: R. Gravelle, [Drag Files Into the Browser From the Desktop with HTML5](https://www.htmlgoodies.com/html5/drag-files-into-the-browser-from-the-desktop-with-html5/), 2012

+ Example: preventing default behavior
  + add to drag over handler: `function dragOverHandler(event) {...}`
    + not propagating the event: `event.stopPropagation();`
    + preventing default behavior, in particular when droopping images or links: `event.preventDefault();`
  + add to drop handler: `function dropHandler(event) {...}`
    + not propagating the event: `event.stopPropagation();`
    + preventing default behavior, in particular when droopping images or links: `event.preventDefault();`







