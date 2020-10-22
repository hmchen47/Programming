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

There are three different methods available for reading a file's content: readAsText, `readAsArrayBuffer` for binary data and also as `readAsDataURL` (the content will be a URL you will use to set the src field of an `<img src=...>`, `<audio>`, `<video>`, and also with all existing methods/properties that accept a URL).

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

<div class="exampleHTML"><label for="file">Choose a text file:</label><input id="file" onchange="readFileContent(this.files)" type="file"><br><br><textarea id="fileContent" rows="15" cols="50"></textarea>
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



