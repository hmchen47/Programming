# JavaScript Basic HTML APIs


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


### Modifying HTML document

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



### Modifying CSS style

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





## Reacting events

+ [Interaction w/ events](../WebDev/Frontend-W3C/5-JavaScript/01f-JSIntro.md#notes-for-165-adding-interactivity-with-events)
  + possible actions able to react to
    + user interactions (keyboard, mouse, gamepad)
    + changes in the lifecycle of document, e.g., pages loading or resizing, screen rotation on a mobile device
    + notified after compeltion of a long process; e.g. loading a large image or source track from the network






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

### Geolocation APIs


+ [Geolocation API](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#641-introduction)
  + implemented by most modern Web browsers
  + using different means to get the current location: GPS, GSM/3G triangulation, Wifi, IP address, etc.
  + mobile phones:
    + prompt the user to activate the GPS and ask for a particular mean among those available
    + track the current position when it changes
    + useful for writing a navigation application
    + useful for tracking in real time the position of different participants
    + application involving several persons at the same time (using WebSockets, for example)
  + typical usage

    ```js
    navigator.geolocation.getCurrentPosition(showPosition, onError);

    function showPosition(position) {
        console.log("latitude is: " + position.coords.latitude);
        console.log("longitude is: " + position.coords.longitude);
    }

    function onError(err) {
        console.log("Could not get the position");
    }
    ```

  + example: get location
    + check if the Web browser supports the `geolocation` API by testing the variable `navigator.geolocation`:
      + `navigator.geolocation.getCurrentPosition(showPosition)` passing a callback function as a parameter
      + when a current position available, the callback function called asynchronously
      + the input parameter of this callback function = the current position

      ```js
      function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            displayCoords.innerHTML="Geolocation API not supported by your browser.";
        }
      }
      ```

    + position objects w/ a `coords` property: the longitude and the latitude

      ```js
      function showPosition(position) {
        displayCoords.innerHTML="Latitude: " + position.coords.latitude +
                               "<br />Longitude: " + position.coords.longitude;
      }
      ```

  + [Geolocation API Specification](https://www.w3.org/TR/geolocation-API/)
  + [Geolocation API - WDN](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)

+ [coords object properties](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#642-the-coords-object-properties)
  + __latitude:__ the latitude of the position
  + __longitude:__ the longitude of the position
  + __altitude:__ the altitude of the position
  + __accuracy:__ the accuracy of the measure of the longitude and latitude (in meters)
  + __altitudeAccuracy:__ the accuracy of the measure of the altitude (in meters)
  + __heading:__ giving the orientation relative to north, in degrees
  + __speed:__ current speed in meters/second

+ [Geolocation error codes](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#643-geolocation-error-codes)
  + `navigator.geolocation.getCurrentPosition` method possible to pass a second parameter in case of errror
  + example: error handler
    + get location: `navigator.geolocation.getCurrentPosition(showPosition, errorPosition);`
    + error handling

      ```js 
      function errorPosition(error) {
        var info = "Error during geolocation: ";
        switch(error.code) {
          case error.TIMEOUT:
              info += "Timeout !";
              break;
          case error.PERMISSION_DENIED:
              info += "Permission denied, geolocation could not be obtained...";
              break;
          case error.POSITION_UNAVAILABLE:
              info += "Location could not be obtained though the available means...";
              break;
          case error.UNKNOWN_ERROR:
              info += "Unknown error";
              break;
        }
        displayCoords.innerHTML = info;
      }
      ```

+ [Tracking position](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#644-tracking-a-position) 
  + syntax: `watchPosition(onSuccess, onError)`
    + get the callback function only when the current position changes
    + return an `id` to use the `clearWatch(id)` method to stop the current tracking
  + track the current position
  + typical usage:
    + get an id of the current tracking: `var watchPosId = navigator.geolocation.watchPosition(showPosition);`
    + stop the tracking: `navigator.geolocation.clearWatch(watchPosId);`


### Tracking Position

+ [Properties of the coords object for real time tracking](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#options-available-when-using-the-geolocation-api-in-particular-real-time-tracking)
  + __enableHighAccuracy:__ 
    + a boolean (true/false) indicating to the device wish to obtain its most accurate readings
    + using the GPS
    + probably making a difference, depending on your hardware, GPS availability, etc.
  + __maximumAge:__
    + the maximum amount of time (in milliseconds) the position  in the cache
    + appropriate as the device may cache readings to save power and/or bandwidth
  + __timeout:__
    + the maximum time (in milliseconds)
    + prepared to allow the device to try to obtain a Geo location
    + after this timeout, call the `onError` callback

+ [Example: tracking position](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#example-of-use)
  + ask to turn GPS on, if available: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {enableHighAccuracy:true});`
  + the position cached for 10 mins useful when in tunnels: `maximumAge = 10 mins` 
  + when the device tries to get a position, if it does not succeed, then go on error immediately: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:600000, timeout:0});`
  + position will never come from the cache (maximumAge: 0), and if after 0.1s the position could not be computed, then go on error: `navigator.geolocation.getCurrentPosition(onSuccess, onError, {maximumAge:0, timeout:100});`
  + ask for GPS, cache for 30s, 27s before going on error: `watchId=navigator.geolocation.watchPosition(onSuccess, onError, {enableHighAccuracy:true, maximumAge:30000, timeout:27000});`


### 

+ [Get a map centered on given longitude and latitude](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#645-geolocation-and-maps)
  + rendering a map with the [Leaflet API for OpenStreetMaps](https://leafletjs.com/reference-1.6.0.html)
  + required files to use the Leaflet API :
    + `<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css">`
    + `<script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>`
  + container to display the interactive map: `<div id="map"></div>`
  + using the [Geolocation API](https://www.w3.org/TR/geolocation-API/) to get the current position: `navigator.geolocation.getCurrentPosition(success, error);`
  + successfully get the location: `function success(position) {...}`
    + get the longitude and latitude properties from the location: `latitude = position.coords.latitude, longitude = position.coords.longitude;`
    + instance map using leaflet w/ `id='map'`: `map = L.map('map').setView([latitude, longitude], 13);`
    + tile layer using key API at cloudmade.com
    + marker using leaflet: `marker = L.marker([latitude, longitude]).addTo(map);`
    + popup in leaflet: `marker.bindPopup('<p>Your location</p>').openPopup();`
  + get current position fail: `alert('Get current position fail. Please access codepen to get geolocation.');`



### Reverse Geocoding

+ [Reverse Geocoding](../WebDev/Frontend-W3C/2-HTML5Coding/06d-BasicAPIs.md#646-reverse-geocoding)
  + Web services:
    + used to get an address from longitude and latitude
    + mostly free of charge, but ask to register an API key and enter your credit card number
    + if too many requests, you will be charged
    + examples:
      + the [Google Reverse Geocoding JavaScript API](https://tinyurl.com/pdlpfjc)
      + Leaflet plugin (an extension to Leaflet) based on the Gisgraphy (free open source framework)
  + example: get address from longitude & latitude
    + access Google API: `<script src="https://maps.googleapis.com/maps/api/js?key=PUT_HERE_YOUR_API_KEY&v=3.exp&sensor=false">`
    + using the google apis: `var infowindow = new google.maps.InfoWindow();`
    + initializing JS after page loaded: `function init() {...}`
      + linking w/ html elements: `displayCoords=document.getElementById("msg"); myAddress = document.getElementById("address");`
      + access Google map: `geocoder = new google.maps.Geocoder();`
      + displaying something before click button: `geocoder = new google.maps.Geocoder();`
      + parameters for Google map: `var mapOptions = { zoom: 8, center: latlng, mapTypeId: 'roadmap' }`
      + get initial map: `map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);`
    + button clicked: `navigator.geolocation.getCurrentPosition(showPosition);`
    + show position as available: `function showPosition(position) {...}`
      + insert HTML code: `displayCoords.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;`
      + display map: `showOnGoogleMap(new google.maps.LatLng(position.coords.latitude, position.coords.longitude));`
    + ask google geocoder for an address: `function showOnGoogleMap(latlng) {...}`
      + the reverse geocoder sends back an array of "guesses", i.e. not just one address object, but several
      + each entry in this array has several properties such as street, city, etc.
      + using the "formatted_address" one here
      + probably interesting to get the detailed properties in other applications like a form with street, city, zip code etc.
      + the reverse geocoder: `geocoder.geocode({'latLng': latlng},reverseGeocoderSuccess);`
    + process the map: `function reverseGeocoderSuccess(results, status) {...}`
      + display marker if success: `status == google.maps.GeocoderStatus.OK`
      + showing warning message: `alert('Geocoder failed due to: ' + status);`






