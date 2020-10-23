# Week 6: HTML5 Basic APIs


## 6.3 The File API


### 6.3.0 Lecture Notes

+ [File API](#631-introduction)
  + features for accessing file metadata (name, size, type) from client-side JavaScript
  + methods for reading file contents directly in the browser
  + particularly interesting for displaying preview of images before uploading them
  + much more interesting: developing Web applications work with local files w/o the need for a server
  + [File API Specification](https://www.w3.org/TR/FileAPI/)
  + example: loading image files for preview

    ```html
    <input type="file" multiple onchange="readImagesAndPreview(this.files);">
    <p>
    <div id="thumbnails"></div>
    <script>
      var container = document.getElementById("thumbnails");
      function readImagesAndPreview(files) {
        for(var i=0; i < files.length; i++) {
            var f = files[i];

            var reader = new FileReader();

            reader.onload = function(e) {
              var img = document.createElement("img");
              img.src = e.target.result;
              img.width = 100;

              container.appendChild(img);
          }

          reader.readAsDataURL(f);
        }
      }
    </script>
    ```

+ [File metadata](#633-reading-file-metadata)
  + metadata: name, size, type and last modification date
  + select one or more files: `<input type="file" id="input" ... />`
    + rendered as a "select files" or "browse files" button
    + file chooser dialog popped-up to select one file
    + do nothing in the client-side before HTML5 die to no access from JavaScript
  + File API
    + define a files property on the DOM node corresponding to the `<input type="file".../>` input field
    + property as an array
    + the metadata related to `selectedFile` variable: `selectedFile.name, selectedFile.size, selectedFile.type, selectedFile.lastModifiedDate`
  + example: read file metadata from `<input type="file" id="input" onchange="displayFirstSelectedFileMetadata();"/>`

    ```js
    function displayFirstSelectedFileMetadata() {
        var selectedFile = document.getElementById('input').files[0];
        document.querySelector("#singleName").innerHTML = selectedFile.name;
        document.querySelector("#singleSize").innerHTML = selectedFile.size + " bytes";
        document.querySelector("#singleType").innerHTML = selectedFile.type;
        document.querySelector("#singleDate").innerHTML = selectedFile.lastModifiedDate;
    }
    ```

  + example: display metadata of multiple files w/ a filter on the file type
    + select several images: `<input type="file" accept="image/*" multiple onchange="filesProcess(this.files)" name="selection"/>`
    + `accept="image/*"` attribute: a filter restricting selection to images only
    + `filesProcess(...)` function: passing as parameter the list of selected files for the current element (`this.files`)
    + `for` loop builds all the rows that compose the table, adding HTML code to the selection string variable
      + prepare the HTML code for building a `<table>` with the results
      + build table and headings: `var selection = "<table><tr><th>Name</th><th>Bytes</th><th>MIME Type</th> <th>Last modified date</th></tr>";`
      + build rows in iteration:

        ```js
        selection += "<tr><td>"+file.name+"</td><td style=\"text-align:right\">"
                    +file.size+"</td><td>"
                    +file.type+"</td><td> "+file.lastModifiedDate+"</td></tr>";
        ```

      + closing table: `selection += "</table>";`
    + table added to the page: `document.getElementById("result").innerHTML = selection;`
      + table appears on the page dynamically
      + use the innerHTML attribute of the DOM element corresponding to the `<div id="result">` in order to insert the table as its child in the DOM tree

+ [Interface of HTML5 File API specification](#634-blob-and-file)
  + FileList interface: the files property
  + File interface: useful for getting details about a file
  + Blob interface: read binary data (only) accessed slice by slice (as chunks of data, each one being a "Blob")
  + FileReader interface: reading file content

+ [Blob object](#the-blob-object)
  + a structure representing binary data available as read-only
  + two properties, namely: size and type
  + retrieving the size in bytes of the data handled by the Blob and their MIME type

+ [File object](#the-file-object)
  + useful for manipulating files
  + inherit the properties and methods of `Blob` objects
  + two additional properties
    + name: the file name
    + lastModifiedDate: the date of the last modification of the file

+ [Procedure to read file contents](#635-reading-file-content)
  + create a FileReader object
    + several methods for reading file content, each taken from the `FileReader` interface
    + create a FileReader object: `var reader = new FileReader();`
  + call a method of the FileReader object for reading the file content
    + three different methods available for reading a file's content: `readAsText`, `readAsArrayBuffer` and `readAsDataURL`
    + `readAsArrayBuffer` for binary data
    + `readAsDataURL`
      + content as a URL used to set the `src` field of an `<img src=...>`, `<audio>`, `<video>`
      + all existing methods/properties that accept a URL
    + start reading the file asynchronously: `reader.readAsText(f);`
    + executed by the browser in the background
    + `reader.onload `callback only when the file is read entirely
  + get the file content in an `onload` callback
    + called only when the file content is loaded
    + the content: `e.target.result`
    + called only when the file content is available: `reader.onload = function(e) {...}`
    + event `e` as a unique parameter
    + `e.target.result` = the file content

+ [Read text file](#636-read-file-content-as-text)
  + read a single file's content
    + start reading the file asynchronously: `reader.readAsText(files[0]);`
    + call the `onload` callback when the file is read
    + called when the file content is loaded: `reader.onload = function(e) {...}`
      + the file content: `e.target.result`
      + display content in the `textarea` with `id="fileContent"`: `document.getElementById("fileContent").value= e.target.result;`
  + read multiple files
    + select multiple files: `<input type="file" id="files" multiple onchange="readFilesAndDisplayAsText(this.files);"/><br/>`
    + `onload` listener to print the name of thev file...

      ```js
      function addOnLoadListener(reader, name) {
          // Add an onload listener that will be able to print the name of the
          // file...
          reader.onload = function(e) {
              filesContent.value += "###### READING FILE " + name + " ######";
              filesContent.value += e.target.result;
          };
      }
      ```

    + iterate to read files

      ```js
      function readFilesAndDisplayAsText(files) {
          console.log("dans read files");
          // Loop through the FileList
          for (var i = 0, f; f = files[i]; i++) {
              var reader = new FileReader();
              // Add an onload listener to the reader
              addOnLoadListener(reader, f.name);
              // start reading, will call the listener later, when the file f is read
              reader.readAsText(f);
          }
      }
      ```

+ [Character encoding for text file](#about-character-encoding)
  + optionally indicate the encoding of the file going to read
  + default: UTF-8
  + e.g., `reader.readAsText(file, 'UTF-8'); reader.readAsText(file, 'ISO-8859-1');`

+ [Read binary file](#637-read-file-content-as-binary)
  + rarely used, except for loading "raw" binary data
  + HTML page for specific binary files
    + image files or drawing in a canvas: using the `<img src= tag>`
    + audio files: using the `<audio>` elements
    + video files: using the `<video>` elements
  + image, drawing, audio, and video files: referable to use the `readAsDataURL` method
  + `readAsArrayBuffer` method used for purposes
    + reading audio samples that should be loaded in memory 
    + played using the WebAudio API
    + loading textures that you will use with WebGL for 3D animations
  + WebAudio API
    + useful for reading audio sound samples from memory (no streaming)
    + designed for music application and games
  + example: read audio file and play w/ WebAudio API
    + read a local audio file and play directly in the Browser
    + user selects file and read it as an `ArrayBuffer` and pass to the API: `var fileInput = document.querySelector('input[type="file"]');`
    + define a change listener: `fileInput.addEventListener('change', function(e) {...}`
      + after choosing a file, the listener executed
      + start the reading of the file content, as a binary file: `reader.readAsArrayBuffer(this.files[0]);`
      + once the file will be entirely read, the `onload` callback asynchronously called by the browser
    + executed the `onload` callback when the file content is loaded in memory
    + pass the file content to the `initSound(e.target.result);` function to play

+ [Read file as dataURL](#638-read-file-content-as-dataurl)
  + data URL: a URL including type and content at the same time
  + useful for in-lining images or videos in the HTML of a Web page
  + mobile devices: speed up the loading of the page by reducing the number of HTTP requests
  + the red circle
    + dataURL: `data:image/png;base64,iVBOR...`
    + `src` attribute of an image element `<img src="data:image/png....">` with the data URL: `<img src="data:image/png;base64,iVBORw..." alt="Red square" width=50 height=50/>`
  + dataURL format
    + enabling file content to be stored in a base64 format (as a string)
    + adding the MIME type specification of the content
    + able to store a file as a URL readable with modern browsers
    + commonly used on the Web
    + especially for mobile applications, inlining images reducing the number of HTTP requests and making the Web page load faster
    + [Image to Data URI converter](https://ezgif.com/image-to-datauri)
    + able to encode any type of file as dataURL
    + most frequently used with media files (images, audio, video)
  + example: read images as data URL & display
    + starts the reading of the file `f`: `reader.readAsDataURL(f);`
    + when `f` read, the `onload` callback called: `reader.onload = function(e) {...}`
      + render thumbnail
      + `e.target.result` = the image content as a data URL
      + create a span with CSS `class="thumb"`, for nicer layout": `var span = document.createElement('span');`
      + Add an img src=... in the span, with src= the dataURL of the image: `span.innerHTML = "<img class='thumb' src='" + e.target.result + "' alt='a picture'/>";`
      + Insert the span in the `<output id="list"></output>`:  `document.getElementById('list').insertBefore(span, null);`
  + example: read local image file and use it with drawImage in a canvas
    + create an image object to draw an image on a canvas: `var img = new Image();`
    + `e.target.result` as the dataURL
    + set the `src` attribute of the image object: `img.src= e.target.result`
    + asynchronously call the `onload` callback: `img.onload = function(e) { ctx.drawImage(img, 0, 0, 400, 400); }`
    + 






### 6.3.1 Introduction

The objective of this chapter is to provide an overview of the File API.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2xpgmdq')"
    src    ="https://tinyurl.com/y6k8n294"
    alt    ="sound sample editor serverless"
    title  ="sound sample editor serverless"
  />
</figure>


Before HTML5, file management was limited to multipart forms and to Ajax for sending/requesting files to/from a remote Web server.

Possible actions were limited, both for the developer and the user. However, HTML5 now comes with an API called "File"  that holds features for accessing file metadata (name, size, type) from client-side JavaScript. The API also has methods for reading file contents directly in the browser. This is particularly interesting for displaying preview of images before uploading them, or - and this is much more interesting - for developing Web applications that work with local files without the need for a server.

Imagine a multimedia player that accesses (in read-only) your file system, reads your audio and video files, etc., such as the [Remo Music player](https://tinyurl.com/ya9fuqb2) below, or an application that edits the audio content of local mp3 files, for example, the [HYA-WAVE sound editor](https://wav.hya.io/#/fx) (screenshot above).

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2xpgmdq" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y5m6fw8g"
      alt  ="audio player that plays local files"
      title="audio player that plays local files"
    >
    <img style="margin: 0.1em;" height=300
      src  ="https://tinyurl.com/y3n3q6et"
      alt  ="polarr photo editor uses the File API"
      title="polarr photo editor uses the File API"
    >
  </a>
</div>


#### External resources

+ From W3C's specification: [File API](https://www.w3.org/TR/FileAPI/)
+ An article from Web.dev: [Read files in JavaScript](https://web.dev/read-files/)
+ MDN's Web Docs: [Using files from web applications](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications)


### 6.3.2 Working with local files

#### Live Coding Video: Working with local files

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V002200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y6gmkl7c)


#### Source code of the example shown in the video

[Example on JSBin](https://jsbin.com/nituko/1/edit?html,output) ([Local Example - Image Files](src/6.3.2-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y4r7br7l')"
    src    ="https://tinyurl.com/y4ttpl6m" 
    alt    ="image previews"
    title  ="image previews"
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of using readAsDataURL</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">multiple</span><span class="pln"> </span><span class="atn">onchange</span><span class="pun">=</span><span class="atv">"</span><span class="pln">readImagesAndPreview</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">files</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"thumbnails"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> container </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"thumbnails"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> readImagesAndPreview</span><span class="pun">(</span><span class="pln">files</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> files</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> f </span><span class="pun">=</span><span class="pln"> files</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> reader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FileReader</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;reader</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> img </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">"img"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; img</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; img</span><span class="pun">.</span><span class="pln">width </span><span class="pun">=</span><span class="pln"> </span><span class="lit">100</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; container</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">img</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;reader</span><span class="pun">.</span><span class="pln">readAsDataURL</span><span class="pun">(</span><span class="pln">f</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag">&lt;/script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


### 6.3.3 Reading file metadata

Imagine you have an input field like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="typ">Select</span><span class="pln"> one </span><span class="kwd">or</span><span class="pln"> more files</span><span class="pun">:</span><span class="pln"> </span><span class="pun">&lt;</span><span class="pln">input type</span><span class="pun">=</span><span class="str">"file"</span><span class="pln"> id</span><span class="pun">=</span><span class="str">"input"</span><span class="pun">/&gt;</span></li>
</ol></div>

This renders as a "select files" or "browse files" button. If you select one file in the file chooser dialog that has popped up, before HTML5 you couldn't do anything with it in the client-side: no access from JavaScript. With the File API, you can read what we call "file metadata": name, size, type and last modification date.

Look at the the code below: the file API defines a files property on the DOM node corresponding to the `<input type="file".../>` input field. This property is an array.

In the example below, we get in the `selectedFile` variable, the metadata related to the first selected file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">var selectedFile </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'input'</span><span class="pun">).</span><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// do something with selectedFile.name, selectedFile.size, selectedFile.type</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">//&nbsp;</span><span style="color: #880000; line-height: 25.6000003814697px;">selectedFile.lastModifiedDate</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">...</span></li>
</ol></div>


#### Examples

__Example #1: read metadata of the first selected file__

[Here is a complete example on JSBin](https://jsbin.com/terocu/edit?html,output) that uses the code above to get details about the first selected file. Please try it below on your browser (click on the button and choose one file): ([Local Example - Metadata](src/6.3.3-example1.html))

<div class="exampleHTML">
<script>// <![CDATA[
function displayFirstSelectedFileMetadata() {
      var selectedFile = document.getElementById('input1').files[0];
      document.querySelector("#singleName").innerHTML = selectedFile.name;
      document.querySelector("#singleSize").innerHTML = selectedFile.size + "  bytes";
      document.querySelector("#singleType").innerHTML = selectedFile.type;
      document.querySelector("#singleDate").innerHTML = selectedFile.lastModifiedDate;
    }
// ]]></script>
Select one or more files: <input id="input1" onchange="displayFirstSelectedFileMetadata();" type="file">
<ul>
<li>File name: <span id="singleName"></span></li>
<li>File size: <span id="singleSize"></span></li>
<li>File type: <span id="singleType"></span></li>
<li>File last modification date: <span id="singleDate"></span></li>
</ul>
</div>

Complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">utf-8</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;title&gt;</span><span class="pln">Reading file metadata</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">function</span><strong><span class="pln"> displayFirstSelectedFileMetadata</span><span class="pun">()</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> selectedFile </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'input'</span><span class="pun">).</span><strong><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span></strong><span class="pun"><strong>]</strong>;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#singleName"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><strong><span class="pln"> selectedFile</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#singleSize"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><strong><span class="pln"> selectedFile</span><span class="pun">.</span><span class="pln">size </span></strong><span class="pun">+</span><span class="pln"> </span><span class="str">" bytes"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#singleType"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><strong><span class="pln"> selectedFile</span><span class="pun">.</span><span class="pln">type</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#singleDate"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=&nbsp;</span><strong><span class="pln">selectedFile</span><span class="pun">.</span><span class="pln">lastModifiedDate</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Select one or more files: </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"input"</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>onchange</strong></span><strong><span class="pun">=</span><span class="atv">"</span><span class="pln">displayFirstSelectedFileMetadata</span><span class="pun">();</span></strong><span class="atv">"</span><span class="tag">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;ul&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li&gt;</span><span class="pln">File name: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"singleName"</span><span class="tag">&gt;&lt;/span&gt;&lt;/li&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li&gt;</span><span class="pln">File size: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"singleSize"</span><span class="tag">&gt;&lt;/span&gt;&lt;/li&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li&gt;</span><span class="pln">File type: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"singleType"</span><span class="tag">&gt;&lt;/span&gt;&lt;/li&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;li&gt;</span><span class="pln">File last modification date: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"singleDate"</span><span class="tag">&gt;&lt;/span&gt;&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/ul&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;">&lt;/body&gt;</li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


__Example #2: display metadata of multiple files, use a filter on the file type__

This example is a bit more complicated, as it will display details about all files selected (not only the first) and allows only images to be selected, using the accept attribute of the input field: `<input type="file" accept="image/*".../>`.

[Example on JSBin](https://jsbin.com/deboja/edit?html,output), or try it in your browser: click on the button, and select multiple image files. Notice that in the file selector, files that are not images will be greyed and non selectable. ([Local Example - Filter](src/6.3.3-example2.html))

<div class="exampleHTML">Select several images: <input name="selection" onchange="filesProcess2(this.files)" accept="image/*" multiple="multiple" type="file">
<div id="result2">...</div>
<p>
<script>// <![CDATA[
function filesProcess2(files) {    
    selection = "<table><tr><th>Name</th><th>Bytes</th><th>MIME Type</th><th>Last modified date</th></tr>";

    for (i=0; i<files.length ;i++){
      file = files[i];      
        selection += "<tr><td>"+file.name+"</td><td style=\"text-align:right\">"
			+ file.size + "</td><td>"
			+ file.type + "</td><td> "+file.lastModifiedDate+"</td></tr>";
     }
      selection += "</table>";

     document.getElementById("result2").innerHTML = selection;
   }
// ]]></script>
</p>
</div>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="typ">Select</span><span class="pln"> several images</span><span class="pun">:</span><span class="pln"> </span><span class="pun">&lt;</span><span class="pln">input type</span><span class="pun">=</span><span class="str">"file"</span><strong><span class="pln"> accept</span><span class="pun">=</span><span class="str">"image/*"</span></strong><span class="pln"><strong> multiple</strong> <strong>onchange</strong></span><strong><span class="pun">=</span><span class="str">"filesProcess(this.files)"</span></strong><span class="pln"> name</span><span class="pun">=</span><span class="str">"selection"</span><span class="pun">/&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">&lt;p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">div id</span><span class="pun">=</span><span class="str">"result"</span><span class="pun">&gt;...&lt;/</span><span class="pln">div</span><span class="pun">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">&lt;script&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> filesProcess</span><span class="pun">(</span><span class="pln">files</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; var selection </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;table&gt;&lt;tr&gt;&lt;th&gt;Name&lt;/th&gt;&lt;th&gt;Bytes&lt;/th&gt;&lt;th&gt;MIME Type&lt;/th&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;th&gt;Last modified date&lt;/th&gt;&lt;/tr&gt;"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="pln">i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">&lt;</span><span class="pln">files</span><span class="pun">.</span><span class="pln">length </span><span class="pun">;</span><span class="pln">i</span><span class="pun">++){</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; file </span><span class="pun">=</span><span class="pln"> files</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; selection </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"&lt;tr&gt;&lt;td&gt;"</span><span class="pun">+</span><span class="pln">file</span><span class="pun">.</span><span class="pln">name</span><span class="pun">+</span><span class="str">"&lt;/td&gt;&lt;td style=\"text-align:right\"&gt;"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">+</span><span class="pln">file</span><span class="pun">.</span><span class="pln">size</span><span class="pun">+</span><span class="str">"&lt;/td&gt;&lt;td&gt;"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">+</span><span class="pln">file</span><span class="pun">.</span><span class="pln">type</span><span class="pun">+</span><span class="str">"&lt;/td&gt;&lt;td&gt; "</span><span class="pun">+</span><span class="pln">file</span><span class="pun">.</span><span class="pln">lastModifiedDate</span><span class="pun">+</span><span class="str">"&lt;/td&gt;&lt;/tr&gt;"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; selection </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"&lt;/table&gt;"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"result"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> selection</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&lt;/</span><span class="pln">script</span><span class="pun">&gt;</span></li>
</ol></div>

__Explanations:__

+ _Line 1_: we used the multiple attribute to allow the selection of multiple files in the file chooser (using shift or control keys). The `accept="image/*"`  attribute is a filter that restricts selection to images only. Finally, the `onchange` listener will call the `filesProcess(...)` function, passing as parameter the list of selected files for the current element (`this.files`).
+ _Lines 7 and 12_: we prepare the HTML code for building a `<table>` with the results.
+ _Line 10_: this `for` loop builds all the rows that compose the table, adding HTML code to the `selection` string variable. At the end of the loop, this variable contains all the HTML code that corresponds to the table of results.
+ _Line 18_: the table is added to the page. We use the `innerHTML` attribute of the DOM element corresponding to the `<div id="result">` in order to insert the table as its child in the DOM tree. As such, the table appears on the page dynamically.


### 6.3.4 Blob and File

The [HTML5 File API specification](https://www.w3.org/TR/FileAPI/) introduces several interfaces:

+ the [__FileList__](https://www.w3.org/TR/FileAPI/#filelist-section) interface (we already met it: the `files` property is a `FileList`,
+ the [__File__](https://www.w3.org/TR/FileAPI/#file-section) interface that is useful for getting details about a file (the `file` variable in the `for` loop of the last example illustrates this),
+ the [__Blob__](https://www.w3.org/TR/FileAPI/#blob-section) interface helps read binary data (only) that is accessed slice by slice (as chunks of data, each one being a "Blob"),
+ and the [__FileReader__](https://www.w3.org/TR/FileAPI/#APIASynch) interface for reading file content (we will see how to use it in the next section of the course).

We will not use all of these interfaces, but let's explain the difference between `Blob` and `File`, as most of the methods exposed by the `FileReader` interface take indiscriminately a Blob or a File as parameter.


#### The Blob object

__An object of type Blob is a structure that represents binary data available as read-only.__ Most of the time, you will only encounter these objects when you handle files.

Blob objects have two properties, namely: `size` and `type`, which respectively retrieve the size in bytes of the data handled by the Blob and their MIME type.


#### The File object

__File objects are useful for manipulating... files!__ They inherit the properties and methods of Blob objects, and have two additional properties that are `name`, for the file name, and `lastModifiedDate` to get the date of the last modification of the file (in the form of a JavaScript Date object, obviously) .

Most of the time, we will work with `File` objects. `Blob` objects will have real interest when you download binary files using Ajax (see example below).

__Advanced:__ If you are interested in seeing how `Blob` objects can be used, [here is an example "as is" that shows how to download an image using Xhr2](https://jsbin.com/jefitop/1/edit?html,output) (Xml Http Request version 2). The examples uses a `<progress>` element to show the download progress, and uses `xhr.responseType = 'blob';` to indicate that the file we are going to download is a binary file (a blob). Try the example, then comment the line with responseType='blob'. In this case, you will notice that the image file is not properly decoded by the browser and is not displayed in the page. We explain Xhr2 in the [W3C HTML5 Apps and Games course](https://www.edx.org/course/html5-apps-and-games). ([Local Example - Bolb](src/6.3.4-example1.html))



### 6.3.5 Reading file content

In order to read the content of a file, different steps required. Let's see how to do it.


#### Typical use is made of three steps


__Step #1: create a FileReader object__

The file API proposes several methods for reading file content, each taken from the `FileReader` interface. Here is how you create a `FileReader` object:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> reader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FileReader</span><span class="pun">();</span></li>
</ol></div>


__Steps #2 and #3: first call a method of the FileReader object for reading the file content, then get the file content in an onload callback__

There are three different methods available for reading a file's content: `readAsText`, `readAsArrayBuffer` for binary data and also as `readAsDataURL` (the content will be a URL you will use to set the `src` field of an `<img src=...>`, `<audio>`, `<video>`, and also with all existing methods/properties that accept a URL).

All these methods take as a unique parameter a File object (for example, a file chosen by a user after clicking on a `<input type=file>` input field). Below, we use, as an example, the `readAsText` method:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> readFileContent</span><span class="pun">(</span><span class="pln">f</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// <strong>Executed last:</strong> called only when the file content is loaded, e.target.result is</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// The content</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>reader</strong></span><strong><span class="pun">.</span><span class="pln">onload </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> content </span><span class="pun">=</span><strong><span class="pln"> e</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// do something with the file content</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"File "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> f</span><span class="pun">.</span><span class="pln">name </span><span class="pun">+</span><span class="pln"> </span><span class="str">" content is: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> content</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// <strong>Executed first:</strong> start reading the file asynchronously, will call the </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// reader.onload callback&nbsp;only when the file is read entirely</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;reader</strong></span><strong><span class="pun">.</span><span class="pln">readAsText</span><span class="pun">(</span><span class="pln">f</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

The above code shows how a file can be read as text. The function is called, for example by clicking on the button corresponding to a `<input type="file" id="file"  onchange="readFileContent(this.files)"/>`, and by choosing a file.

+ _Line 12_ is executed first, and asks the `Reader` object to read the file f as text. As this takes some time, it's an asynchronous operation that will be executed by the browser in the background. When the file is read, the `reader.onload` callback function is called.
+ _Line 4_ is executed after line 12, and is called only when the file content is available. This callback takes an event `e` as a unique parameter, and `e.target.result` is the file content.

Try a variation of the above code in your browser, that displays the file content in a text area. This example is detailed further in the course. Click and select a text file below:

<div style="border: 1px solid; margin: 20px; padding: 20px;"><label for="file">Choose a text file:</label><input id="file" onchange="readFileContent(this.files)" type="file"><br><br><textarea id="fileContent" rows="5" cols="50"></textarea>
<p></p>
<p> 
<script>// <![CDATA[
function readFileContent(files) {
    console.log("In readFileContent");
    // Loop through the FileList and render image files as thumbnails.

      var reader = new FileReader();
 
      // Called when the file content is loaded, e.target.result is
      // The content
      reader.onload = function(e) {   
        // display content in the textarea with id="fileContent"
        document.getElementById("fileContent").value= e.target.result;
      };   
 
      // Read in the tfile as text
      console.log("Reading file:" + files[0].name);
      
      // Start reading asynchronously the file
      reader.readAsText(files[0]);
    }
// ]]></script>
</p>
</div>

In the following next pages, we look at different examples that read file contents as text, dataURL and binary.


### 6.3.6 Read file content as text

Let's start by reading a pure text file


#### Examples


__Example #1: read a single file's content__

[Example at JSBin](https://jsbin.com/xewemi/edit?html,output), or try it below in your browser: ([Local Example - Read Text File](src/6.3.6-example1.html))

<div style="border: 1px solid; margin: 20px; padding: 20px;">Choose a text file :<input id="file" onchange="readFileContent(this.files)" type="file"><br>
<p></p>
<p><textarea id="fileContent" rows="5" cols="50"></textarea>
<script>// <![CDATA[
function readFileContent(files) {
    console.log("In readFileContent");
    // Loop through the FileList and render image files as thumbnails.

      var reader = new FileReader();
 
      // Called when the file content is loaded, e.target.result is
      // The content
      reader.onload = function(e) {   
        // display content in the textarea with id="fileContent"
        document.getElementById("fileContent").value= e.target.result;
      };   
 
      // Read in the tfile as text
      console.log("Reading file:" + files[0].name);
      
      // Start reading asynchronously the file
      reader.readAsText(files[0]);
    }
// ]]></script>
</p>
</div>

Complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of use of FileReader with a text file</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&lt;label for="files"&gt;Choose a text file:&lt;/label&gt;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"file"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">onchange</span><span class="pun">=</span><span class="atv">"</span><span class="pln">readFileContent</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">files</span><span class="pun">)</span><span class="atv">"</span></strong><span class="tag">/&gt;&lt;br/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;textarea</span><span class="pln"> </span><span class="atn">rows</span><span class="pun">=</span><span class="atv">15</span><span class="pln"> </span><span class="atn">cols</span><span class="pun">=</span><span class="atv">50</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"fileContent"</span><span class="tag">&gt;&lt;/textarea&gt;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> readFileContent</span><span class="pun">(</span><span class="pln">files</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"In readFileContent"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> reader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FileReader</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// <strong>Executed last</strong>: called when the file content is loaded, <strong>e.target.result</strong> is</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// The content</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; reader</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// display content in the textarea with id="fileContent"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"fileContent"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">=</span><strong><span class="pln"> e</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">};</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Reading file:"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">].</span><span class="pln">name</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// <strong>Executed first:</strong> start reading the file asynchronously , will call the onload</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // callback when the file is read</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>reader</strong></span><strong><span class="pun">.</span><span class="pln">readAsText</span><span class="pun">(</span><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

This example is the one at the end of the previous page. This time, we show the complete source code above. Remember that the instruction at line 29 is executed first, then when the file is read, the browser will call asynchronously the onload callback at line 20.


__Example #2: a variation of the previous one, using multiple files__

[Example on JSBin](https://jsbin.com/zaheyu/edit?html,output), or try it below in your browser. ([Local Example - Multiple Files](src/6.3.6-example2.html))

This time, please select multiple text files (using shift for multiple selection):

<div style="border: 1px solid; margin: 20px; padding: 20px;"><label for="files1">Choose multiple text files:</label><input id="files1" onchange="readFilesAndDisplayAsText1(this.files);" multiple="multiple" type="file"><br>
<p></p>
<p><textarea id="filesContent1" rows="5" cols="50"></textarea>
<script>// <![CDATA[
var filesContent = document.getElementById("filesContent1");
  
  function readFilesAndDisplayAsText1(files) {
    console.log("dans read files");
    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {
 
      var reader = new FileReader();      
 
      // Add an onload listener to the reader
      addOnLoadListener(reader, f.name);
      // start reading, will call the listener later, when the file f is read
      reader.readAsText(f);
      
    }
  }
 
  function addOnLoadListener(reader, name) {
    // Add an onload listener that will be able to print the name of the
    // file...
    reader.onload = function(e) {  
        filesContent.value += "###### READING FILE " + name + " ######";
        filesContent.value += e.target.result;
      };
  }
// ]]></script>
</p>
</div>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of use of FileReader with a text file</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&lt;label for="files"&gt;Choose multiple text files:&lt;/label&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"files"</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp;multiple</span><span class="pln"> </span><span class="atn">onchange</span><span class="pun">=</span><span class="atv">"</span><span class="pln">readFilesAndDisplayAsText</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">files</span><span class="pun">);</span><span class="atv">"</span><span class="tag">/&gt;&lt;br/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;textarea</span><span class="pln"> </span><span class="atn">rows</span><span class="pun">=</span><span class="atv">30</span><span class="pln"> </span><span class="atn">cols</span><span class="pun">=</span><span class="atv">50</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"filesContent"</span><span class="tag">&gt;&lt;/textarea&gt;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> filesContent </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"filesContent"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> readFilesAndDisplayAsText</span><span class="pun">(</span><span class="pln">files</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"dans read files"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Loop through the FileList</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> f</span><span class="pun">;</span><span class="pln"> f </span><span class="pun">=</span><span class="pln"> files</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> reader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FileReader</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// Add an onload listener to the reader</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;addOnLoadListener</span><span class="pun">(</span><span class="pln">reader</span><span class="pun">,</span><span class="pln"> f</span><span class="pun">.</span><span class="pln">name</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// start reading, will call the listener later, when the file f is read</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;reader</span><span class="pun">.</span><span class="pln">readAsText</span><span class="pun">(</span><span class="pln">f</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> addOnLoadListener</span><span class="pun">(</span><span class="pln">reader</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Add an onload listener that will be able to print the name of the</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// file...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;reader</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;filesContent</span><span class="pun">.</span><span class="pln">value </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"###### READING FILE "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> name </span><span class="pun">+</span><span class="pln"> </span><span class="str">" ######"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;filesContent</span><span class="pun">.</span><span class="pln">value </span><span class="pun">+=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


__Explanations:__

This example is similar to the previous one, except that this time we read multiple files.

+ _Line 20_: this is the `for` loop that will iterate on the `files` object passed as parameter by the `onchange` listener declaration at _line 10_.
+ _Line 25_: instead of declaring the `onload` listener with a `reader.onload =...` directly in the loop, this time we preferred to write a separate function that will do this. This technique is useful when you want the listener to work with extra variables computed in the loop (in our case, the `name` of the file).


#### About character encoding

Note that you can optionally indicate the encoding of the file you are going to read (default is UTF-8):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">reader</span><span class="pun">.</span><span class="pln">readAsText</span><span class="pun">(</span><span class="pln">file</span><span class="pun">,</span><span class="pln"> </span><span class="str">'UTF-8'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">reader</span><span class="pun">.</span><span class="pln">readAsText</span><span class="pun">(</span><span class="pln">file</span><span class="pun">,</span><span class="pln"> </span><span class="str">'ISO-8859-1'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">...</span></li>
</ol></div>


### 6.3.7 Read file content as binary

This method is rarely used, except for loading "raw" binary data. For images you would like to see in your HTML page using the `<img src= tag>` or for drawing in a canvas, or for audio and video files that you would like to play using the `<audio>` or `<video>` elements, it would be preferable to use the readAsDataURL method presented on the next page of the course.

`readAsArrayBuffer` is often used for purposes such as reading audio samples that should be loaded in memory and played using the WebAudio API, or for loading textures that you will use with WebGL for 3D animations.


#### Example: read a local audio file and play it with the WebAudio API

The WebAudio API is useful for reading audio sound samples from memory (no streaming), and has been designed for music application and games. This example shows how a local audio file can be read and played directly in the browser, without the need for a server!

[Example on JSBin](https://jsbin.com/xepexuy/1/edit?html,output) (does not work on IE, as it does not support the WebAudio API). We could not embed it here on the edX platform as it prevents code that uses Ajax to run in its pages. ([Local Example - Audio File](src/6.3.7-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y4yldqdq')"
    src    ="https://tinyurl.com/y2arv2ez"
    alt    ="local audio player"
    title  ="local audio player"
  />
</figure>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// User selects file. Read it as an ArrayBuffer and pass&nbsp;to the API.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> fileInput </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'input[type="file"]'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">fileInput</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'change'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> reader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FileReader</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;reader</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; initSound</span><span class="pun">(</span><span class="pln">e</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="com">// THIS IS THE INTERESTING PART!</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>reader</strong></span><strong><span class="pun">.</span><span class="pln">readAsArrayBuffer</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
</ol></div>


__Explanations:__

+ _Line 2_: we get a pointer to the file selector, the variable `fileInput`.
+ _Line 4_: we define a `change` listener. In this example, we use an anonymous function directly included in the listener definition (the listener is the `function(e) {...}`).
+ _Line 11_: when a user chooses a file, the listener will be executed. Line 11 will start the reading of the file content, as a binary file (this is what `readAsArrayBuffer` means: read as binary!). Once the file will be entirely read, the onload callback will be asynchronously called by the browser.
+ _Line 7_ is the `onload` callback, executed when the file content is loaded in memory. We pass the file content to the `initSound` function (see JSBin example for complete source code) that uses WebAudio to decode it (it may be a compressed file - an mp3 for example - and WebAudio works only with uncompressed audio formats in memory), and to play it.


### 6.3.8 Read file content as dataURL

What is a data URL?

A data URL is a URL that includes type and content at the same time. It is useful, for example,  for in-lining images or videos in the HTML of a Web page (on mobile devices, this may speed up the loading of the page by reducing the number of HTTP requests).

Here is an example of a red square, as a data URL. Copy and paste it in the address bar of your browser, and you should see the red square:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">data</span><span class="pun">:</span><span class="pln">image</span><span class="pun">/</span><span class="pln">png</span><span class="pun">;</span><span class="pln">base64</span><span class="pun">,</span><span class="pln">iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4</span><span class="com">//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==</span></li>
</ol></div>

This data URL in a browser address bar should look like this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3vycf73')"
    src    ="https://tinyurl.com/y5mea3zx"
    alt    ="data url in address bar shows a red circle"
    title  ="data url in address bar shows a red circle"
  />
</figure>


If we set the src attribute of an image element `<img src="data:image/png....">` with the data URL of the above screenshot, it will work exactly as if you used a URL that started with https://

In your browser, you will see a small red circle rendered by this source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atv">AAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atv">9TXL0Y4OHwAAAABJRU5ErkJggg=="</span><span class="pln"> </span><span class="atn">alt</span><span class="pun">=</span><span class="atv">"Red square"</span><span class="pln">&nbsp;width=50 height=50</span><span class="tag">/&gt;</span></li>
</ol></div>

And here is the result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 2vw;"
    onclick="window.open('https://tinyurl.com/y3vycf73')"
    src    ="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=="
    alt    ="Red square"
    title  ="Red square"
  />
</figure>


This `dataURL` format enables file content to be stored in a base64 format (as a string), and adds the MIME type specification of the content. The dataURL can therefore store a file as a URL readable with modern browsers. It is becoming more commonly used on the Web, especially for mobile applications, as inlining images reduces the number of HTTP requests and makes the Web page load faster.

You will find lots of Web sites and tools for generating dataURL from files, such as [Image to Data URI converter](https://ezgif.com/image-to-datauri) (screenshot below):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3vycf73')"
    src    ="https://tinyurl.com/y4kdb9mp"
    alt    ="Online service that converts uploaded images to data uris... we see an image and its ascii encoded data uri version."
    title  ="Online service that converts uploaded images to data uris... we see an image and its ascii encoded data uri version."
  />
</figure>


With the above example, you can copy and paste the characters on the left and use them with an `<img src="...">`. Just set the src attribute with it!

Notice that you can encode any type of file as dataURL, but this format is most frequently used with media files (images, audio, video).

Example of HTML5 logo embedded in a document without any real image, just a dataURL and CSS:

[Try it at JSBin](https://jsbin.com/zaheyu/edit?html,output) ([Local Example - Text File](src/6.3.8-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3vycf73')"
    src    ="https://tinyurl.com/yyqatka8"
    alt    ="Screenshot of JsBin example that shows the HTML5 logo inserted before a div using CSS"
    title  ="Screenshot of JsBin example that shows the HTML5 logo inserted before a div using CSS"
  />
</figure>



#### Examples


__Example #1: read images as data URL and display previews in the page__

This first example is useful for forms that allow the user to select one or more pictures. Before sending the form, you might want to get a preview of the pictures in the HTML page. The `reader.readAsDataUrl` method is used for that.

[Example on JSBin](https://jsbin.com/laseye/edit?html,output) or try it below in your browser: ([Local Example - data URL for Image](src/6.3.8-example2.html))

<div class="exampleHTML"><label for="files1">Choose multiple images files:</label> <input id="files1" onchange="readFilesAndDisplayPreview1(this.files);" multiple="multiple" type="file"><br>
<p></p>
<p>Preview of selected images:</p>
<output id="list1"></output>
<script>// <![CDATA[
function readFilesAndDisplayPreview1(files) {
    // Loop through the FileList and render image files as thumbnails.
    for (var i = 0, f; f = files[i]; i++) {

      // Only process image files.
      if (!f.type.match('image.*')) {
        continue;
      }

      var reader = new FileReader();

      //capture the file information.
      reader.onload = function(e) {
          // Render thumbnail. e.target.result = the image content 
          // as a data URL
        
          // create the span with CSS class="thumb", for nicer layout
          var span = document.createElement('span');
          // Add an <img src=...> in the span, with src= the dataURL of
          // the image
          span.innerHTML = "<img class='thumb' src='" + e.target.result + "' alt='a picture'/>";
          // Insert the span in the output id=list
          document.getElementById('list1').insertBefore(span, null);
        };
      
      // Read in the image file as a data URL.
      reader.readAsDataURL(f);
    }
  }
// ]]></script>
</div>


Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"files"</span><span class="tag">&gt;</span><span class="pln">Choose multiple files:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"files"</span><span class="pln"> </span><span class="atn">multiple</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><strong><span class="atn">onchange</span><span class="pun">=</span><span class="atv">"</span><span class="pln">readFilesAndDisplayPreview</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">files</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">/&gt;&lt;br/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Preview of selected images:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"list"</span><span class="tag">&gt;&lt;/output&gt;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; function readFilesAndDisplayPreview(files) {</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // Loop through the FileList and render image files as thumbnails.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; for (var i = 0, f; f = files[i]; i++) {</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // Only process image files.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; if (!f.type.match('image.*')) {</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; continue;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; var reader = new FileReader();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; //capture the file information.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; reader.onload = function(e) {</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; // Render thumbnail. e.target.result = the image content </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; // as a data URL</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;// create a&nbsp;span with CSS class="thumb", for nicer layout</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;var span = document.createElement('span');</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;// Add an </span><span class="tag">img</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">...</span><span class="pln">&nbsp;in the span, with src= the dataURL of</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;// the image</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;span.innerHTML = "</span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">'thumb'</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">'" + </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="atv">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;e.target.result + "'</span><span class="pln"> </span><span class="atn">alt</span><span class="pun">=</span><span class="atv">'a picture'</span><span class="tag">/&gt;</span><span class="pln">";</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;// Insert the span in the output id=list</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;document.getElementById('list').insertBefore(span, null);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>// Read in the image file as a data URL.</strong></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>reader.readAsDataURL(f);</strong></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> }</span></li>
</ol></div>


__Explanations:__

+ _Line 35_: starts the reading of the file `f`. When `f` is read, the `onload` callback will be called.
+ _Lines 25-31_: we build, using the DOM API, a `<span class="thumb">`...`</span>` and inside we add an `<img src=the data url>` element with its `src` attribute equal to the `url` of the image that has been read (the image content as dataURL is in `e.target.result`). Finally, at _line 31_, we insert the span in the document before the current children of the `<output id="list">` element (declared at _line 5_).


__Example #2: read a single local image file and use it with drawImage in a canvas__

[Try it on JSBin](https://jsbin.com/miciqu/edit?html,output) ([Local Example - drawImage](src/6.3.8-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y3vycf73')"
    src    ="https://tinyurl.com/yy8tqvav"
    alt    ="read image as dataURL and draw inside a canvas. Jsbin screenshot"
    title  ="read image as dataURL and draw inside a canvas. Jsbin screenshot"
  />
</figure>


Errata: the above screenshot says "choose multiple files", but the example only works with a single file.

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawImage</span><span class="pun">(</span><span class="pln">imageFile</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> reader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FileReader</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">//capture the file information.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>reader</strong></span><strong><span class="pun">.</span><span class="pln">onload </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// For drawing an image on a canvas we</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// need an image object</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> img </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Image</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Even if the file has been read, decoding</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// the dataURL format may take some time</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// so we need to use the regular way of</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// working with images: onload callback &nbsp; &nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// that will be called after setting the src attribute</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>img</strong></span><strong><span class="pun">.</span><span class="pln">onload </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// draw the image!</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">drawImage</span><span class="pun">(</span><span class="pln">img</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">400</span><span class="pun">,</span><span class="pln"> </span><span class="lit">400</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// e.target.result is the dataURL, so we set the</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// src if the image with it. This will call </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; // asynchonously&nbsp;</span>the onload callback</li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; img</span><span class="pun">.</span><span class="pln">src</span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">result</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// Read in the image file as a data URL.</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>reader</strong></span><strong><span class="pun">.</span><span class="pln">readAsDataURL</span><span class="pun">(</span><span class="pln">imageFile</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> readFileAndDraw</span><span class="pun">(</span><span class="pln">files</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; drawImage</span><span class="pun">(</span><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div>


__Explanations:__

Remember how we worked with images on a canvas. We had to create an empty image object (_line 8_), set the src attribute of the image object (line 23), then use an image.onload callback (line 15), and we could only draw from inside the callback (_line 17_). This time, it's exactly the same, except that the URL comes from `e.target.result` in the `reader.onload` callback (_line 23_).


__Example #3 (advanced): an instagram-like photo filter application__

Another very impressive example, has been developed by @GeorgianaB, a student of the first iteration of this course (see her [other creations/examples](https://codepen.io/giana/)). This Web application reads local image files, draws them into a canvas element and proposes different filters. This example is given "as is" for those of you who would like to go further. Just click on the link (or on the image below) and look at the source code.

[Try this example online on gitHub](https://gianablantin.github.io/CanvasFilters/).



### 6.3.9 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ The course demonstrated how to play an audio file from memory using the Web Audio API (not covered in this course). It was a good way to show how local binary files could be read using `readAsArrayBuffer`. But do you know that we could have used `readAsDataURL` and set the file content to an `<audio>`  element's source? In this case we could have streamed it from the client hard disk!
+ Have you tried "chrome applications" or HTML5 applications from the Windows store? Try some! A lot of them work with local files and rely on the File API. Share the best applications you find in the forum!


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy):__ Add a way to select an image file in your form and display a preview as a thumbnail. Additional task: write a local audio/video player that streams audio/video files from the local hard disk.
+ __Project 2 (a bit harder):__ Add a way to select a pattern (an image) and use it with one of your canvas animations - i.e., apply a pattern on a monster, or a background image you read from disk.


