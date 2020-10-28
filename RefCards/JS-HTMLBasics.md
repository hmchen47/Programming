# JavaScript Basic HTML APIs

## Web Storage APIs

### Web Storage API

+ [Web Storage API](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#621-the-web-storage-api)
  + similar to HTTP session cookies
  + two related mechanisms for storing structured data on the client side
    + `sessionStorage`:
      + erased when the tab/browser closed
      + tab specific and scoped to the lifetime of the tab
      + useful for storing small amounts of session specific information
      + used with caution: synchronous and blocking the main thread
      + limited to about 5MB and containing only strings
      + not accessible from web workers or service workers
      + data never transferred to the server
      + storage limit larger than a cookie
    + `localStorage`:
      + data remained until deleted
      + avoided due to synchronous to block the main thread
      + limited to about 5MB and containing only strings
      + not accessible from web workers or service workers
      + stored data w/o expiration date
      + get cleared only through JavaScript, or clearing the Browser cache / Locally Stored Data
      + storage limit: the maximum among the three
  + main difference: data longevity
  + key-value store for `localStorage`
    + a simple key-value store
    + the keys and values: strings
    + only one store per domain
    + same applied to `sessionStorage` 
    + functionality exposed through the globally available `localStorage` object
  + [example: save & restore form contents on the fly](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#622-example-1)

+ [Example for local storage API](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#example-that-shows-all-the-methods-of-the-local-storage-api-in-action)
  + HTML button to activate the JS function: `<button onclick="resetStore()">reset store (erase all key/value pairs)</button>`
  + retrieve all data: `function getCountValue() { document.querySelector("#counter").innerHTML = localStorage.count; }`
  + view all stored data
  + reset all stored data: `function resetStore() { localStorage.clear(); document.querySelector('#list').innerHTML=""; }`
  + add/remove some data to local storage

+ [Example to save/restore states](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#624-example-2)
  + save initial preferences
  + load preferences



### Cookie

+ [Cookies & Web Storage](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#differences-with-cookies)
  + main difference: size limit
  + cookie:
    + a popular way to store key-value pairs
    + cookies limited to a few KBytes
    + generate additional HTTP request traffic: request a Web page, an image, a stylesheet, a JavaScript file, etc.
    + not used for storage
    + sent with every HTTP request
    + storing anything more than a small amount of data
    + significantly increasing the size of every web request
    + limited to only strings
  + Web Storage: a more powerful technique than cookies
    + Web Storage extended to several MBytes
    + objects managed no longer carried on the network and HTTP
    + easily accessible (read, change and delete) from JavaScript
    + using the Web Storage API

+ [sessionStorage key/values vs cookies](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#sessionstorage-keyvalues-instead-of-cookies)
  + store session-based data in a manner more powerful than cookies
  + `sessionStorage` object working in exactly the same way as `localStorage`
  + lifetime limited to a single browser session (lifetime of your tab/window)
  + `sessionStorage` advantage: being scoped to a given browser tab (or similar execution context)
  + Cookies' security drawback
    + two tabs open to the same site $\to$ share the same cookies
    + storing information about a given operation using cookies in one tab
    + probably leaking the information to the other side
    + confusing if performing different tasks in each
  + `sessionStorage` data scoped and not leak across tabs


### Set & Get Web Storage

+ [getItem and setItem methods](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#gettingsetting-values-using-the-getitemkey-and-setitemkey-value-methods)
  + using `var value = getItem(key)` to retrieve a key's value and `setItem(key, value)` to set it
  + a counter counting the number of times a given user loaded the application
  + spaces acceptable: `localStorage.setItem("Instructor's name", "Michel");` and `var name = localStorage.getItem("Instructor's name");`
  + not acceptable: `var name = localStorage.Instructor's name; will not work!`
  + syntax to set/get `localStorage` values within loop or iterator


### Delete & Reset Web Storage

+ [removeItem and clear methods](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#deleting-a-key-with-removeitemkey-or-all-keys-with-clear)
  + `removeItem(key)`: delete a key
  + `localStorage.clear()`:
    + reset the entire store
    + rare occasion to clear the entire store by the user in production software
    + a common operation needed during development
      + bugs may store faulty data the persistence of which can break your application
      + the way to store data may evolve over time
      + test the experience of the user when first using the application
  + one way of reseting the entire store
    + add a user interface button that calls `clear()` when clicked
    + remember to remove it when you ship
  + recommended approach: simply open the dev. tool's console and type `localStorage.clear()`

+ [Example for generic functions](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#625-example-3)
  + calling `init()` function when the page loaded
  + adding input listeners:
    + taking an input field as parameter and attaching an `oninput` listener to it
    + saving the field's content each time a value entered
  + restore the last saved value for each input field, if present.
    + get the list of input fields: `document.querySelectorAll("input");`
    + iterate through the list: `for(var i= 0; i < listOfInputsInForm.length; i++) {...}`
    + get `id` of input fields as the key in `localStorage` for the previous data saved for this field: `var fieldToRestore = listOfInputsInForm[i]; var id = fieldToRestore.id;`
    + restore by setting the value of the input field if not undefined: `if(savedValue !== undefined) { fieldToRestore.value = savedValue; }`


### Size of Web Storage

+ [Size of Web storage](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#626-size-limitations-etc)
  + related mechanism w/ user agents (browsers) according to Web storage specification
    + limiting the total amount of space allowed for storage areas
    + allowing the user to grant more space to a site, when reaching quotas
    + allowing users to see how much space each domain is using
    + giving at least 5Mb per origin
  + local storage required for saving/loading data on demand in many cases
  + more complex solutions:
    + processing transaction: require more available space than local storage
    + e.g., IndexedDB, a No SQL database
  + limit amount of data to prevent from storing anything anything huge
  + storage not necessarily permanent
  + serious applications
    + synchronizing existing data with the server on a regular basis
    + avoid data loss when using the same service from multiple devices at once


### JavaScript Object Notation (JSON)

+ [JSON to structure key-value pairs](../WebDev/Frontend-W3C/2-HTML5Coding/06b-BasicAPIs.md#626-size-limitations-etc)
  + `JSON.stringify()` and `JSON.parse() methods`: manipulate minimal record format to store complex data
  + JSON (JavaScript Object Notation)
    + a lightweight data-interchange format
    + easy for machines to parse and generate.
    + a text format completely programming language independent
    + providing a great way of encoding and decoding data
    + a really good match for JavaScript
    + careful not to use circular data structures or non-serializable objects
    + straightforward plugging yo support local store in vast majority of cases
    + two structures:
      + a collection of name/value pairs
      + an ordered list of values
  + typical usage:
    + `locaStorage.key = JSON.stringify(object);`
    + `localStorage.setItem(key, JSON.stringify(object));`
  + example:
    + store the object as a JSON String: `localStorage.setItem('testObject', JSON.stringify(personObject));`
    + retrieve the object from storage: `retrievedObject = JSON.parse(localStorage.getItem('testObject'));`



## File APIs


### File APIs

+ [Interface of HTML5 File API specification](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#634-blob-and-file) 
  + __FileList__ interface: the files property
  + __File__ interface: useful for getting details about a file
  + __Blob__ interface: read binary data (only) accessed slice by slice (as chunks of data, each one being a "Blob")
  + __FileReader__ interface: reading file content

+ [File API](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#631-introduction)
  + features for accessing file metadata (name, size, type) from client-side JavaScript
  + methods for reading file contents directly in the browser
  + particularly interesting for displaying preview of images before uploading them
  + much more interesting: developing Web applications work with local files w/o the need for a server
  + [File API Specification](https://www.w3.org/TR/FileAPI/)
  + example: loading image files for preview


### File Metadata

+ [File metadata](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#633-reading-file-metadata)
  + metadata: name, size, type and last modification date
  + select one or more files: `<input type="file" id="input" ... />`
    + rendered as a "select files" or "browse files" button
    + file chooser dialog popped-up to select one file
    + do nothing in the client-side before HTML5 die to no access from JavaScript
  + File API 
    + define a file property on the DOM node corresponding to the `<input type="file".../>` input field
    + property as an array
    + the metadata related to `selectedFile` variable: `selectedFile.name, selectedFile.size, selectedFile.type, selectedFile.lastModifiedDate`
  + example: read file metadata from `<input type="file" id="input" onchange="displayFirstSelectedFileMetadata();"/>`
  + example: display metadata of multiple files w/ a filter on the file type
    + select several images: `<input type="file" accept="image/*" multiple onchange="filesProcess(this.files)" name="selection"/>`
    + `accept="image/*"` attribute: a filter restricting selection to images only
    + `filesProcess(...)` function: passing as parameter the list of selected files for the current element (`this.files`)
    + `for` loop builds all the rows that compose the table, adding HTML code to the selection string variable
      + prepare the HTML code for building a `<table>` with the results
      + build table and headings: `var selection = "<table><tr><th>Name</th><th>Bytes</th><th>MIME Type</th> <th>Last modified date</th></tr>";`
      + build rows iteratively
      + closing table: `selection += "</table>";`
    + table added to the page: `document.getElementById("result").innerHTML = selection;`
      + table appears on the page dynamically
      + use the innerHTML attribute of the DOM element corresponding to the `<div id="result">` in order to insert the table as its child in the DOM tree


### Bolb Object

+ [Blob object](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#the-blob-object)
  + a structure representing binary data available as read-only
  + two properties, namely: size and type
  + retrieving the size in bytes of the data handled by the Blob and their MIME type


### File Object

+ [File object](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#the-file-object)
  + useful for manipulating files
  + inherit the properties and methods of `Blob` objects
  + two additional properties
    + name: the file name
    + lastModifiedDate: the date of the last modification of the file

+ [Procedure to read file contents](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#635-reading-file-content)
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
    + called only when the file content loaded
    + the content: `e.target.result`
    + called only when the file content available: `reader.onload = function(e) {...}`
    + event `e` as a unique parameter
    + `e.target.result` = the file content


### Text Files

+ [Read text file](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#636-read-file-content-as-text)
  + read a single file's content
    + start reading the file asynchronously: `reader.readAsText(files[0]);`
    + call the `onload` callback when the file is read
    + called when the file content is loaded: `reader.onload = function(e) {...}`
      + the file content: `e.target.result`
      + display content in the `textarea` with `id="fileContent"`: `document.getElementById("fileContent").value= e.target.result;`
  + read multiple files
    + select multiple files: `<input type="file" id="files" multiple onchange="readFilesAndDisplayAsText(this.files);"/><br/>`
    + `onload` listener to print the name of the file...
    + iterate to read files
  
+ [Character encoding for text file](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#about-character-encoding)
  + optionally indicate the encoding of the file going to read
  + default: UTF-8
  + e.g., `reader.readAsText(file, 'UTF-8'); reader.readAsText(file, 'ISO-8859-1');`


### Binary Files

+ [Read binary file](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#637-read-file-content-as-binary)
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
      + once the file entirely read, the `onload` callback asynchronously called by the browser
    + executed the `onload` callback when the file content is loaded in memory
    + pass the file content to the `initSound(e.target.result);` function to play


### dataURL method

+ [Read file as dataURL](../WebDev/Frontend-W3C/2-HTML5Coding/06c-BasicAPIs.md#638-read-file-content-as-dataurl)
  + data URL: a URL including type and content at the same time
  + useful for in-lining images or videos in the HTML of a Web page
  + mobile devices: speed up the loading of the page by reducing the number of HTTP requests
  + example: the red square w/ dataURL
    + dataURL: `data:image/png;base64,iVBOR...`
    + `src` attribute of an image element `<img src="data:image/png....">` with the data URL: `<img src="data:image/png;base64,iVBORw..." alt="Red square" width=50 height=50/>`
  + dataURL format
    + enabling file content to be stored in a base64 format (as a string)
    + adding the MIME type specification of the content
    + able to store a file as a URL readable with modern browsers
    + commonly used on the Web
    + especially for mobile applications, in-lining images reducing the number of HTTP requests and making the Web page load faster
    + [Image to Data URI converter](https://ezgif.com/image-to-datauri)
    + able to encode any type of file as dataURL
    + most frequently used with media files (images, audio, video)
  + example: read images as data URL & display
    + starts the reading of the file `f`: `reader.readAsDataURL(f);`
    + when `f` read, the `onload` callback called: `reader.onload = function(e) {...}`
      + render thumbnail
      + `e.target.result` = the image content as a data URL
      + create a span with CSS `class="thumb"` for nicer layout: `var span = document.createElement('span');`
      + add an `<img src=...>` in the span, with src= the dataURL of the image: `span.innerHTML = "<img class='thumb' src='" + e.target.result + "' alt='a picture'/>";`
      + insert the span in the `<output id="list"></output>`:  `document.getElementById('list').insertBefore(span, null);`
  + example: read local image file and use it with drawImage in a canvas
    + create an image object to draw an image on a canvas: `var img = new Image();`
    + `e.target.result` as the dataURL
    + set the `src` attribute of the image object: `img.src= e.target.result`
    + asynchronously call the `onload` callback: `img.onload = function(e) { ctx.drawImage(img, 0, 0, 400, 400); }`





## Geolocaltion APIs






