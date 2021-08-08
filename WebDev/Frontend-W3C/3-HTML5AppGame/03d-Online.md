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

<div><ol>
<li value="1">function dropHandler(event) { </li>
<li>&nbsp; &nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp;event.stopPropagation();</li>
<li>&nbsp; &nbsp;// Prevent default behavior, in particular when we drop images or links</li>
<li>&nbsp; &nbsp;event.preventDefault(); </li>
<li> </li>
<li>&nbsp; &nbsp;<strong style="color: red;">// get the dropped files from the clipboard</strong></li>
<li>&nbsp; &nbsp;<strong style="color: red;">var files = event.dataTransfer.files;</strong></li>
<li> </li>
<li>&nbsp; &nbsp;var filenames = "";</li>
<li> </li>
<li>&nbsp; &nbsp;// do something with the files...here we iterate on them and log the filenames</li>
<li>&nbsp; &nbsp;for(var i = 0 ; i &lt; files.length&nbsp;; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;filenames += '\n' + files[i].name; </li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;console.log(files.length + ' file(s) have been dropped:\n' + filenames);</li>
<li>} </li>
</ol></div>

+ _Lines 7-8_ we get the files that have been dropped.
+ _Lines 12-15_ iterate over the collection and build a string which contains the list of file names.
+ _Line 17_ displays this string on the debugging console.

Complete working examples are to be presented later on...


#### Prevent the browser's default behavior

If we drop an image into an HTML page, the browser will open a new tab and display the image. With a .mp3 file, it will open it in a new tab and a default player will start streaming it, etc. We need to prevent this behavior in order to customisethe processing of the dropped files (i.e. display an image thumbnail, add entries to a music playlist, etc.). So, when dragging and dropping images or links, we need to prevent the browser's default behavior.

At the beginning of the `drop` handler in the previous piece of code, you can see the lines of code (_lines 2-5_) that stop the propagation of the drop event and prevent the default behavior of the browser. Normally when we drop an image or an HTTP link onto a web page, the browser will display the image or the web page pointed by the link, in a new tab/window. This is not what we would like in an application using the drag and drop process. These two lines are necessary to prevent the default behavior of the browser:

<div><ol>
<li value="1">// Do not propagate the event</li>
<li>event.stopPropagation();</li>
<li>// Prevent default behavior, in particular when we drop images or links</li>
<li>event.preventDefault(); </li>
</ol></div>

<p style="margin: 10px; padding: 10px;"><strong style="color: red;">Best practice</strong>: add these lines to the <code>drop</code>handler AND to&nbsp;the <code>dragOver</code> handler attached to the drop zone!</p>

... like in this example:

<div><ol>
<li value="1">function dragOverHandler(event) {</li>
<li>&nbsp; &nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp;event.stopPropagation();</li>
<li> </li>
<li>&nbsp; &nbsp;// Prevent default behavior, in particular when we drop images or links</li>
<li>&nbsp; &nbsp;event.preventDefault(); </li>
<li>&nbsp; &nbsp;...</li>
<li>}</li>
<li> </li>
<li>function dropHandler(event) {</li>
<li>&nbsp; &nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp;event.stopPropagation();</li>
<li> </li>
<li>&nbsp; &nbsp;// Prevent default behavior, in particular when we drop images or links</li>
<li>&nbsp; &nbsp;event.preventDefault(); </li>
<li>&nbsp; &nbsp;...</li>
<li>}</li>
</ol></div>

__External resources__

+ Web.dev article: "[Using the HTML5 drag and drop API](https://web.dev/drag-and-drop/)"
+ HTML Goodies article: "[Drag Files Into the Browser From the Desktop with HTML5](https://bit.ly/2UqW41k)"


#### Notes for 3.4.1 Introduction

+ Moving files from desktop and browser w/ the `files` property
  + no `dragstart` handler required
  + files dragged from the desktop
  + browser only copying their contents from the clipboard
  + main work done in the `drop` handler
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
    + not propagating the event<a name="stopPropagation"></a>: `event.stopPropagation();`
    + preventing default behavior, in particular when dropping images or links<a name="preventDefault"></a>: `event.preventDefault();`
  + best practice: add `event.stopPropagation` and `event.preventDefault` to handlers attached to the drop zone
    + the `drop` handler
    + the `dragOver` handler
  + ref: R. Gravelle, [Drag Files Into the Browser From the Desktop with HTML5](https://bit.ly/2UjkWYV), 2012

+ Example: preventing default behavior
  + add to drag over handler<a name="dragover"></a>: `function dragOverHandler(event) {...}`
    + not propagating the event: `event.stopPropagation();`
    + preventing default behavior, in particular when dropping images or links: `event.preventDefault();`
  + add to drop handler<a name="drop"></a>: `function dropHandler(event) {...}`
    + not propagating the event: `event.stopPropagation();`
    + preventing default behavior, in particular when dropping images or links: `event.preventDefault();`


### 3.4.2 Drag and drop files in a drop zone


#### Live coding video: drag and drop files

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2VjRT7R)


#### Moving files to drop zone w/ file details 

__Example: drag and drop files to a drop zone, display file details in a list__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3xodMAV')"
    src    = "https://bit.ly/3wo0EKX"
    alt    = "Example of drag'n'drop of a file"
    title  = "Example of drag'n'drop of a file"
  />
</figure>


Try the example below directly in your browser (just drag and drop files to the greyish drop zone), or [play with it at CodePen](https://codepen.io/w3devcampus/pen/JYjpqV?editors=111):

[Local Demo](src/03d-example01.html)

Complete source code from the example:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp; div {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;height: 150px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;width: 350px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;float: left;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border: 2px solid #666666; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;background-color: #ccc;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;margin-right: 5px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border-radius: 10px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;box-shadow: inset 0 0 3px #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;text-align: center;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;cursor: move;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;.dragged {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;.draggedOver {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;/style&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp; function dragLeaveHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log("drag leave");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Set style of drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.remove('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dragEnterHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log("Drag enter");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Show some visual feedback</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.add('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dragOverHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;//console.log("Drag over a droppable zone");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Prevent default behavior, in particular when we drop images or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.preventDefault(); </li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dropHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log('drop event');</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Prevent default behavior, in particular when we drop images or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.preventDefault(); </li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// reset the visual look of the drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.remove('draggedOver'); </li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// get the files from the clipboard</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var files = event.dataTransfer.files;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var filesLen = files.length; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var filenames = "";</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// iterate on the files, get details using the file API</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Display file names in a list.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;for(var i = 0 ; i &lt; filesLen ; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; filenames += '\n' + files[i].name; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Create a li, set its value to a file name, add it to the ol</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var li = document.createElement('li');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = files[i].name; document.querySelector("#droppedFiles").appendChild(li);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log(files.length + ' file(s) have been dropped:\n' + filenames);</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;&lt;/script&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp;&nbsp;&lt;h2&gt;Drop your files here!&lt;/h2&gt;</li>
<li>&nbsp;&nbsp;&lt;div id="droppableZone" ondragenter="dragEnterHandler(event)" ondrop="dropHandler(event)"&nbsp; &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ondragover="dragOverHandler(event)"&nbsp; &nbsp;ondragleave="dragLeaveHandler(event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;Drop zone</li>
<li>&nbsp; &nbsp; &nbsp;&lt;ol id="droppedFiles"&gt;&lt;/ol&gt;</li>
<li>&nbsp; &lt;/div&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;html&gt;</li>
</ol></div>

Note that:

+ We prevented the browser default behavior in the `drop` and `dragover` handlers Otherwise, if we dropped a media file (an image, an audio of video file), the browser would try to display/play it in a new window/tab. We also stop the  propagation for performance reasons, because when we drag an object it can raise many events within the parents of the drop zone element as well.
+ _Lines 73-74_ create a `<li>` element. Its value is initialized with the file name of the current file in the collection, and added to the `<ol>` list.

In principle, this example is very similar to the "fruit" examples we worked through earlier, except that this time we're working with files. _And when we work with files, it is important to prevent the browser's default behavior._


#### Notes for 3.4.2 Drag and drop files in a drop zone

+ Example: moving files to drop zone w/ filenames
  + tasks
    + prevent the browser default behavior
    + create listed items for the drop zone
  + HTML snippet:
    + drop zone container<a name="dropzone"></a>: `<div id="droppableZone" ondragenter="dragEnterHandler(event)" ondrop="dropHandler(event)" ondragover="dragOverHandler(event)" ondragleave="dragLeaveHandler(event)"> Drop Zone ...</div>`
    + display zone<a name="displayzone"></a>: `<ol id="droppedFiles"></ol>`
  + CSS style<a name="dropdisplaystyle"></a>
    + style for div container: `.div { height: 150px; width: 350px; float: left; ... }`
    + style for dragged item: `.dragged { border: 2px dashed #000; background-color: green; }`
    + style for drop zone w/ mouse over: `.draggedOver { border: 2px dashed #000; background-color: darkgreen; }`
  + JavaScrip snippet
    + add drag leave handler<a name="dragleave"></a>: `function dragLeaveHandler(evt) { console.log("Drag leave"); evt.target.classList.remove('draggedOver'); }`
    + add drag enter handler<a name="dragenter"></a>: `function dragEnterHandler(evt) { console.log("Drag enter"); evt.target.classList.add('draggedOver'); }`
    + add [drag over handler](#dragover)
    + add drop handler and display filename<a name="drop&filename"></a>: `function dropHandler(evt) {...}`
      + log msg: `console.log('drop event');`
      + do not propagate the event: `evt.stopPropagation();`
      + prevent default behavior: `evt.preventDefault();`
      + reset the visual look of drop zone: `evt.target.classList.remove('draggedOver');`
      + get files from the clipboard: `var files = evt.dataTransfer.files; var filesLen = files.length; var filenames = "";`
      + iterate on files and display filenames: `for (var i=0; i<fileLen; i++) {...}`
        + add filename to string: `filenames += '\n' + files[i].name;`
        + create list item: `var li = document.createElement("li");`
        + add item content: `li.textContent = files[i].name;`
        + add the item to display: `document.querySelector("#droppedFiles").appendChild(li);`
      + log msg: `console.log(files.length + 'file(s) have been dropped:\n' + filenames);`


### 3.4.3 Images with thumbnails


#### Read files and display

This time, let's reuse the `readFilesAndDisplayPreview()` method (studied in the W3Cx HTML5 Coding Essentials and Best Practices course). We have reproduced the example here - please review the source code to refresh your memory (click on the JS tab or look at [the example at CodePen](https://codepen.io/w3devcampus/pen/ZbExbM)).

Click the "Choose files" button (an `<input type="file">` element), select one or more images -- and you should see image thumbnails displayed in the open space beneath it:

[Remote Demo at CodePen](https://codepen.io/w3devcampus/pen/ZbExbM)

[Local Demo](src/03d-example03.html)

Source code extract (the part that reads the image file content and displays the thumbnails):

<div><ol>
<li value="1">function readFilesAndDisplayPreview(files) {</li>
<li>&nbsp; &nbsp;// Loop through the FileList and render image files </li>
<li>&nbsp; &nbsp;// as thumbnails.</li>
<li>&nbsp; &nbsp;for (var i = 0, f; f = files[i]; i++) {</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// Only process image files.</li>
<li>&nbsp; &nbsp; &nbsp;if (!f.type.match('image.*')) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;continue;</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;var reader = new FileReader();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;//capture the file information.</li>
<li>&nbsp; &nbsp; &nbsp;reader.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Render thumbnail.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var span = document.createElement('span');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;span.innerHTML = "&lt;img class='thumb' src='" + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;e.target.result + "'/&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document.getElementById('list').insertBefore(span, null);</li>
<li>&nbsp; &nbsp; &nbsp;}; </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;// Read the image file as a data URL. Will trigger </li>
<li>&nbsp; &nbsp; &nbsp;// a call to the onload callback above</li>
<li>&nbsp; &nbsp; &nbsp;// only once the image is completely loaded</li>
<li>&nbsp; &nbsp; &nbsp;reader.readAsDataURL(f);</li>
<li>&nbsp; &nbsp;}</li>
<li> }</li>
</ol></div>

At _line7_, there is a test that will avoid processing non image files. The "!" is the NOT operator in JavaScript. The call to continue at line 8 will make the for loop go to its end and process the next file. See the HTML5 part 1 course about the file API for more details (each file has a `name`, `type`, `lastModificationDate` and `size` attribute. The call to `match(...)` here is a standard way in JavaScript to match a string value with a regular expression).

At _line 19_, we insert the `<img>` element that was created and initialized with the `dataURL` of the image file, into the HTML list with an `id` of "list".

So, let's add this method to our code example, to display file details once dropped, and also add an `<output id="list"></output>` to the HTML of this example.


#### Complete example of drag and drop + thumbnails of images

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2TKZAn5')"
    src    = "https://bit.ly/3xsutv2"
    alt    = "ilmage drag'n'drop with thumbnails"
    title  = "ilmage drag'n'drop with thumbnails"
  />
</figure>


Try it below in your browser (drag'n'drop image files into the drop zone) or play with it at CodePen:

[Remote Demo at CodePen](https://codepen.io/w3devcampus/pen/XmWEMQ)

[Local Demo](src/03d-example02.html)

Complete source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;div {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; height: 150px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; width: 350px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border: 2px solid #666666; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; background-color: #ccc;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; margin-right: 5px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border-radius: 10px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; box-shadow: inset 0 0 3px #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; text-align: center;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cursor: move;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;.dragged {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;.draggedOver {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&lt;/style&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;function dragLeaveHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log("drag leave");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Set style of drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.remove('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;function dragEnterHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log("Drag enter");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Show some visual feedback</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.add('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;function dragOverHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;//console.log("Drag over a droppable zone");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Prevent default behavior, in particular when we drop images or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.preventDefault(); </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;function dropHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log('drop event');</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Prevent default behavior, in particular when we drop images or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.preventDefault(); </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// reset the visual look of the drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; event.target.classList.remove('draggedOver'); </li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// get the files from the clipboard</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var files = event.dataTransfer.files;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var filesLen = files.length; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var filenames = "";</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// iterate on the files, get details using the file API</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Display file names in a list.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;for(var i = 0 ; i &lt; filesLen ; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;filenames += '\n' + files[i].name; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Create a li, set its value to a file name, add it to the ol</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var li = document.createElement('li');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;li.textContent = files[i].name; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document.querySelector("#droppedFiles").appendChild(li);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; console.log(files.length + ' file(s) have been dropped:\n' + filenames);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; readFilesAndDisplayPreview(files);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;} </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;function readFilesAndDisplayPreview(files) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Loop through the FileList and render image files as thumbnails.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;for (var i = 0, f; f = files[i]; i++) {</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Only process image files.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;if (!f.type.match('image.*')) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;continue;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var reader = new FileReader();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;//capture the file information.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; reader.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Render thumbnail.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var span = document.createElement('span');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;span.innerHTML = "&lt;img class='thumb' width='100' src='" + e.target.result + "'/&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document.getElementById('list').insertBefore(span, null);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;};</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Read the image file as a data URL. Will trigger the call to the above callback when</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // the image file is completely loaded </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; reader.readAsDataURL(f);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;&nbsp;} </li>
<li>&nbsp;&nbsp;&lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;h2&gt;Drop your files here!&lt;/h2&gt;</li>
<li> &lt;div id="droppableZone" ondragenter="dragEnterHandler(event)" ondrop="dropHandler(event)" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ondragover="dragOverHandler(event)"&nbsp; &nbsp;ondragleave="dragLeaveHandler(event)"&gt;</li>
<li>&nbsp; &nbsp; Drop zone</li>
<li>&nbsp; &nbsp;&nbsp;&lt;ol id="droppedFiles"&gt;&lt;/ol&gt;</li>
<li> &lt;/div&gt;</li>
<li> &lt;br/&gt;</li>
<li> &lt;output id="list"&gt;&lt;/output&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;html&gt;</li>
</ol></div>

Above, we added the `readFilesAndDisplayPreview()` method detailed earlier. We called it at the end of the `drop` handler (_line 77_), and we added the `<output>` element as a container for the `<img>` elements (constructed by the JavaScript code _lines 94-96_) which will display the thumbnails (_line 114_).


#### Notes for 3.4.3 Images with thumbnails

+ Example: reading the image files and displaying the thumbnails
  + tasks:
    + skip non-image files w/ file type
    + create and initialize the thumbnail
  + read files and display thumbnail<a name="read&thumbnail"></a>: `function readFilesAndDisplayPreview(files) {...}`
  + loop through the file list: `for (var i=0, f; files[i]; i++) {...}`
  + only process image files: `if (!f.type.match("image.*")) { continue; }`
  + create object for files: `var reader = new FileReader();`
  + add load handler for file: `reader.onload = function(e) {...};`
    + create element: `var span = document.createElement('span');`
    + display msg: `span.innerHTML = "<img class='thumb' src='" + e.target.result + "'/>";>`
    + add element to page: `document.getElementBuId('list').insertBefore(span, null);`
  + read image file as a data URL and trigger load event: `reader.readAsDataURL(f);`

+ Example: drag'n'drop image files and displaying thumbnail
  + HTML snippet
    + [drop zone container](#dropzone)
    + [display zone](#displayzone)
  + CSS style for [div, dragged item, and dragged item over drop zone](#dropdisplaystyle)
  + JavaScript snippet
    + add [drag leave handler](#dragleave)
    + add [drag enter handler](#dragenter)
    + add [drag over handler](#dragover)
    + add [drop handler and display filename](#drop&filename) w/ `readFilesAndDisplayPreview(files);`
    + [read files and display thumbnail](#read&thumbnail)


### 3.4.4 Mixing drag and drop and input type=file


#### Input element with file type

Let's go further and also add an `<input type="file">`

The example below allows files to be selected using a file chooser or by drag  and dropping them, like in the screenshot below (the interactive example is a bit further down the page):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('pagehttps://bit.ly/3AGoQLI')"
    src    = "https://bit.ly/2Vn00Rf"
    alt    = "example of file chooser and dir chooser"
    title  = "example of file chooser and dir chooser"
  />
</figure>


In the above screenshot, which is derived from the example detailed later in this page, we selected some files using the first button (which is an `<input type="file" multiple.../>`), then we used the second button (which is an `<input type="file" webkitdirectory>`) to select a directory that contained 11 files. We then dragged and dropped some other images to the drop zone. Each time, thumbnails were displayed. Both methods (file selector or drag and drop) produced the same result.

__Idea: reuse the same code for reading image files and displaying thumbnails__

If you look (again) at the [very first example](https://codepen.io/w3devcampus/pen/ZbExbM) that displayed thumbnails, without drag and drop), you will notice that the event handler we used to track the selected files using `<input type="file"/>` looks like this:

<div><ol>
<li value="1">&lt;script&gt;</li>
<li>&nbsp; &nbsp;function handleFileSelect(evt) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var files = evt.target.files; // FileList object</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// do something with files... why not call readFilesAndDisplayPreview!</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">readFilesAndDisplayPreview</strong><strong style="color: red;">(files);</strong></li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;document.getElementById('files').addEventListener('change', handleFileSelect, false);</li>
<li>&lt;/script&gt;</li>
<li>...</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &nbsp;Choose multiple files :&lt;input type="file" id="files" multiple /&gt;&lt;br/&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

It calls `readFilesAndDisplayPreview()` at line 5! The same function with the same parameters is also used by [the example](https://codepen.io/w3devcampus/pen/XmWEMQ) that used drag and drop that we discussed on a previous page of this course. 

Let's mix both examples: add to our drag'n'drop example an`<input type="file">` element, and the above handler. This will allow us to select files either with drag'n'drop or by using a file selector.

Just for fun, we also added [an experimental "directory chooser"](https://www.youtube.com/watch?v=WaSP-rdQA_c) that is thus far only implemented by Google Chrome (notice, `<input type="file" webkitdirectory>` is __not__ in the HTML5 specification. Drag and drop functionality will work through a file chooser in any modern browser, but the directory chooser will only work with Google Chrome).


#### Complete interactive example with source code

Try it in your browser below (use all three functions: firstly using the file selector, secondly the directory selector, and finally to drag and drop image files into the drop zone), or [play with it at CodePen](https://codepen.io/w3devcampus/pen/BoavPb):

[Local Demo](src/03d-example04.html)

Complete source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp; div {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; height: 150px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; width: 350px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border: 2px solid #666666; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; background-color: #ccc;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; margin-right: 5px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border-radius: 10px;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; box-shadow: inset 0 0 3px #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; text-align: center;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; cursor: move;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;.dragged {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;.draggedOver {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; border: 2px dashed #000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; background-color: green;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp;</li>
<li> &lt;/style&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dragLeaveHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log("drag leave");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Set style of drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.target.classList.remove('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dragEnterHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log("Drag enter");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Show some visual feedback</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.target.classList.add('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dragOverHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;//console.log("Drag over a droppable zone");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Prevent default behavior, in particular when we drop </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// images or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.preventDefault(); </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function dropHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log('drop event');</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Prevent default behavior, in particular when we drop </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// images or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.preventDefault(); </li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// reset the visual look of the drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.target.classList.remove('draggedOver'); </li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// get the files from the clipboard</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var files = event.dataTransfer.files;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var filesLen = files.length; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var filenames = "";</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// iterate on the files, get details using the file API</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Display file names in a list.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;for(var i = 0 ; i &lt; filesLen ; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; filenames += '\n' + files[i].name; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Create a li, set its value to a file name, add it to the ol</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var li = document.createElement('li');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = files[i].name;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document.querySelector("#droppedFiles").appendChild(li);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log(files.length + ' file(s) have been dropped:\n' + filenames);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">readFilesAndDisplayPreview</strong><strong style="color: red;">(files);</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;function readFilesAndDisplayPreview(files) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Loop through the FileList and render image files as </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// thumbnails.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;for (var i = 0, f; f = files[i]; i++) {</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Only process image files.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;if (!f.type.match('image.*')) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;continue;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var reader = new FileReader();</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;//capture the file information.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; reader.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Render thumbnail.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var span = document.createElement('span');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;span.innerHTML = "&lt;img class='thumb' width='100' src='" + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; e.target.result + "'/&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document.getElementById('list').insertBefore(span, null);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;};&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Read the image file as a data URL.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;reader.readAsDataURL(f);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">function handleFileSelect(evt) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong style="color: red;">var files = evt.target.files; // FileList object</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong style="color: red;">// do something with files... why not call </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; // readFilesAndDisplayPreview!</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">readFilesAndDisplayPreview</strong><strong style="color: red;">(files);</strong></li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp;&nbsp;&lt;/script&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;h2&gt;Use one of these input fields for selecting files&lt;/h2&gt;</li>
<li>&lt;p&gt;Beware, the directory choser&nbsp; may overload </li>
<li>your browser memory if there are too many big images in the </li>
<li>directory you choose.&lt;/p&gt;</li>
<li><strong style="color: red;"> Choose multiple files :</strong>&nbsp;<strong style="color: red;">&lt;input type="file" id="files" multiple</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;onchange="handleFileSelect(event)"/&gt;</strong> </li>
<li> &lt;/p&gt;</li>
<li> <strong style="color: red;">&lt;p&gt;Choose a directory (Chrome only): &lt;input type="file" </strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; id="dir" webkitdirectory</strong></li>
<li><strong style="color: red;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; onchange="handleFileSelect(event)"/&gt;</strong></li>
<li> &lt;/p&gt;</li>
<li>&nbsp;</li>
<li> &lt;h2&gt;Drop your files here!&lt;/h2&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;div id="droppableZone" ondragenter="dragEnterHandler(event)" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ondrop="dropHandler(event)" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ondragover="dragOverHandler(event)" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ondragleave="dragLeaveHandler(event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; Drop zone</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&lt;ol id="droppedFiles"&gt;&lt;/ol&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/div&gt;</li>
<li> &lt;br/&gt;</li>
<li> &lt;output id="list"&gt;&lt;/output&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;html&gt;</li>
</ol></div>

The parts that we have added are in bold. As you can see, all methods share the same code for previewing the images.


#### Notes for 3.4.4 Mixing drag and drop and input type=file

+ Handling multiple files
  + selecting file(s) w/ drag and drop
    + syntax:  `<input type="file" multiple ...>`
    + selecting files either w/ drag'n'drop or by using a file selector
    + applied to any modern browser
  + selecting a directory containing multiple files
    + syntax for Chrome: `<input type="file" webkitdirectory>`
    + not in HTML5 spec.
    + only working for file selector

+ Example: selecting image files and directory
  + HTML snippet:
    + input button for choosing multiple files: `<input type="file" id="files" multiple onchange="handleFileSelect(event)"/>`
    + input button for a directory (Chrome only): `<input type="file" id="files" webkitdirectory onchange="handleFileSelect(event)"/>`
    + [drop zone container](#dropzone)
  + CSS style for [div, dragged item, and dragged item over drop zone](#dropdisplaystyle)
  + JavaScript snippet
    + add [drag leave handler](#dragleave)
    + add [drag enter handler](#dragenter)
    + add [drag over handler](#dragover)
    + add [drop handler and display filename](#drop&filename) w/ `readFilesAndDisplayPreview(files);`
    + [read files and display thumbnail](#read&thumbnail)
    + add change handler for selecting directory: `function handleFileSelect(evt) {...}`
      + decalare FileList object: `var files = evt.target.files;`
      + display thumbnails within the directory: `readFilesAndDisplayPreview(files);`


### 3.4.5 Files upload using Ajax/XHR2

This time, let us mash-up a couple of examples. Let's combine the upload of files using XHR2, with progress monitoring (we worked on in the 3.2 lectures) with one of our drag and drop examples. To achieve this, we re-use the method `calleduploadAllFilesUsingAjax()` and add a `<progress>` element to the drag and drop example.

Try [this interactive example at JSBin](https://jsbin.com/conigekoda/edit) (this example does not work on CodePen. We are using a fake remote server and it cancels the connection as soon as we try to connect):

[Local Demo](src/03d-example05.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/2TOjVbd')"
    src    = "https://bit.ly/3qRxzpW"
    alt    = "example that uses drag'n'drop and a progress element for monitoring the ajax upload of the files"
    title  = "example that uses drag'n'drop and a progress element for monitoring the ajax upload of the files"
  />
</figure>


Source code extract (we omitted the CSS):

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;&lt;/style&gt;</li>
<li>&nbsp; &nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp;function dragLeaveHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;console.log("drag leave");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Set style of drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.target.classList.remove('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dragEnterHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;console.log("Drag enter");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Show some visual feedback</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.target.classList.add('draggedOver'); </li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dragOverHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;//console.log("Drag over a droppable zone");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Prevent default behavior, in particular when we drop images </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.preventDefault(); </li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function dropHandler(event) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;console.log('drop event');</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Do not propagate the event</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.stopPropagation();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Prevent default behavior, in particular when we drop images </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// or links</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.preventDefault(); </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// reset the visual look of the drop zone to default</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;event.target.classList.remove('draggedOver'); </li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// get the files from the clipboard</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var files = event.dataTransfer.files;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var filesLen = files.length; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var filenames = "";</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// iterate on the files, get details using the file API</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Display file names in a list.</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;for(var i = 0 ; i &lt; filesLen ; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; filenames += '\n' + files[i].name; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// Create a li, set its value to a file name, add it to the ol</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var li = document.createElement('li');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; li.textContent = files[i].name; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document.querySelector("#droppedFiles").appendChild(li);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;console.log(files.length + ' file(s) have been dropped:\n' </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +&nbsp;filenames);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;uploadAllFilesUsingAjax(files); </li>
<li>&nbsp; &nbsp; &nbsp;} </li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;function uploadAllFilesUsingAjax(files) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;xhr.open('POST', 'upload.html');</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;xhr.upload.onprogress = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; progress.value = e.loaded;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; progress.max = e.total;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;};</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;xhr.onload = function() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;alert('Upload complete!');</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;};</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var form = new FormData();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;for(var i = 0 ; i &lt; files.length ; i++) { </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; form.append('file', files[i]);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// Send the Ajax request</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;xhr.send(form);</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp;&nbsp;&lt;/script&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;h2&gt;Drop your files here!&lt;/h2&gt;</li>
<li> &lt;div id="droppableZone" ondragenter="dragEnterHandler(event)" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ondrop="dropHandler(event)" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ondragover="dragOverHandler(event)"&nbsp; &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ondragleave="dragLeaveHandler(event)"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;Drop zone</li>
<li>&nbsp; &nbsp; &nbsp;&lt;ol id="droppedFiles"&gt;&lt;/ol&gt;</li>
<li> &lt;/div&gt;</li>
<li> &lt;br/&gt;</li>
<li>&nbsp;Uploading progress: &lt;progress id="progress"&gt;&lt;/progress&gt;</li>
<li> &lt;body&gt;</li>
<li> &lt;html&gt;</li>
</ol></div>

We have highlighted the interesting parts in the example!

We build (_line 75_) an object of type `FormData` (this comes from the standard JavaScript DOM API level 2), we fill this object with the file contents (_line 77_), then we send the Ajax request (_line 81_), and monitor the upload progress (_lines 66-69_).

Instead of uploading all the files at once, it might be interesting to upload one file at a time with visual feedback, such as: "uploading file MichaelJackson.jpg.....". We will leave this exercise up to you.


#### Notes for 3.4.5 Files upload using Ajax/XHR2

+ Example: uploading files w/ Ajax/HR2
  + tasks:
    + reuse `calleduploadAllFilesUsingAjax()`
    + add a progress element to the drag and drop
  + HTML snippet:
    + [drop zone container](#dropzone)
    + progress bar: `<progress id="progress"></progress>`
  + JavaScript snippet
    + add [drag leave handler](#dragleave)
    + add [drag enter handler](#dragenter)
    + add [drag over handler](#dragover)
    + add [drop handler and display filename](#drop&filename) w/ `uploadAllFilesUsingAjax(files);`
    + upload files w/ Ajax: `function uploadAllFilesUsingAjax(files) {...}`
      + create XHR2 request: `var xhr = new XMLHttpRequest();`
      + open connection w/ post request: `xhr.open('POST', 'upload.html');`
      + add progress listener for upload: `xhr.upload.onprogress = function(e) { progress.value = e.loaded; progress.max = e.total; };`
      + add upload listener: `xhr.onload = function() { alert('Upload complete!'); }`
      + add file name to drop zone: `var form = new FormData(); for (var i=0; i<files.length; i++) { form.append('file', files[i]); }`
      + send XHR2 request: `xhr.send(form);`


### 3.4.6 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Suggested topics of discussion:

+ Did you know that it was possible to gain control over the process of dragging a file out of a page, and dropping it onto the desktop (for example)?


#### Optional projects:

+ If a user were to drag and drop the same file to a drop zone several times, this would be confusing. Try to modify some of the examples to avoid duplication (i.e.: not uploading the same file twice).
+ Try to modify the example that played a song loaded in memory, using Web Audio, for allowing a song file to be dragged and dropped.
+ Combine these topics with the talents you developed earlier, working with canvas: instead of a progress 'thermometer' to measure XHR2 upload progress, try modifying the appearance of the thumbnail to show the proportion of the graphic file as it is transferred (alternatively, if you have style-sheet skills, you could try this using CSS transitions).




