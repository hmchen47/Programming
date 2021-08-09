# Web Communications


## Overview


+ [Interaction](../WebDev/Frontend-W3C/3-HTML5AppGame/02b-GameProg.md#notes-for-222-elements-and-apis-useful-for-writing-games)
  + user input replying on several APIs
  + DOM API used for keyboard, touch, or mouse inputs
  + GamePad API (working draft)
    + define a low-level interface representing gamepad devices
    + already implemented by some browsers



## Ajax and XHR2

+ [Asynchronous JavaScript and XML (Ajax)](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-321-ajax-and-xhr2)
  + a group of interrelated Web development techniques
  + used on the client-side to create asynchronous Web application
  + Web applications able to send data to and retrieve from a server asynchronously w/o interfering w/ the display and behavior of the existing page
  + data retrieved via the `XMLHttpRequest` object, usually JSON format used than XML
  + the new version of Ajax
    + XmlHttpRequest level 2 (XHR2)
    + improvement
      + easier to use syntax
      + in-browser encoding/decoding of binary files
      + progress monitoring of uploads and downloads



## Transfering Binary Files

+ [Ajax and binary files](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + HTTP: a text based protocol
  + upload/download binary files
    + images, videos, audio and any other binary files
    + encoded to text before transmission
    + decoded on-the-fly upon receipt by the browser or server
  + Ajax: decoded to binary files "by hand" w/ JavaScript code $\to$ not recommended
  + XHR2:
    + supported by all browsers after 2012
    + able to download binary files
    + asking the browser to encode/decode the file to send/receive, natively
    + using `XMLHttpRequest` to send or receive a file
    + set the `xhr.responseType` as `arrayBuffer`

+ [Syntax for downloading file](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + task: download sound sample w/ `XMLHttpRequest` level 2
  + load sound file: `function loadSoundFile(url) {...};`
  + create new connection for XHR2<a name="xhr"></a>: `var xhr = new XMLHttpRequest();`
  + open connect w/ get request: `xhr.open('GET', url, true);`
  + set response type<a name="rspType"></a>: `xhr.responseType = 'arrayBuffer';`
  + add event listener for complete downloading<a name="onload"></a>: `xhr.onload = function(e) { initSound(this.response); };`
  + send request to server<a name="send"></a>: `xhr.send();`

+ Example: [playing downloaded sound](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + tasks:
    + click button to download sound file
    + send Ajax request and call `xhr.onload` callback after file arrived
    + decode mp3 into memory and enable start/stop buttons
    + click button to play and stop sound


## Monitoring Progress

+ [Monitoring w/ `progress` event](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + XHR2 providing `progress` event attributes for monitoring data transfers
  + the `ProgressEvent` interface: 7 events related to uploading/downloading files

    <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 50vw;" cellspacing=0 cellpadding=5 border=1 align="center">
      <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://xhr.spec.whatwg.org/#event-handlers">Uploading/Downloading Events in <code>ProgressEvent</code></a></caption>
      <thead>
      <tr style="font-size: 1.2em; vertical-align:middle;">
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Attribute</th>
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Type</th>
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Explanation</th>
      </thead>
      <tbody>
        <tr><td><code>onloadstart</code></td><td><code title="event-xhr-loadstart">loadstart</code></td><td>When the request starts.</td></tr>
        <tr><td><strong style="color: red;"><code>onprogress</code></strong></td><td><strong style="color: red;"><code title="event-xhr-progress">progress</code></strong></  td><td><strong style="color: red;">While loading and sending data.</strong></td></tr>
        <tr><td><code>onabort</code></td><td><code title="event-xhr-abort">abort</code></td><td>When the request has been aborted, either by invoking   the&nbsp;<code>abort() </code>method or navigating away from the page.</td></tr>
        <tr><td><code>onerror</code></td><td><code title="event-xhr-error">error</code></td><td>When the request has failed.</td></tr>
        <tr><td><code>onload</code></td><td><code title="event-xhr-load">load</code></td><td>When the request has successfully completed.</td></tr>
        <tr><td><code>ontimeout</code></td><td><code title="event-xhr-timeout">timeout</code></td><td>When the author specified timeout has passed  before the request could complete.</td></tr>
        <tr><td><code>onloadend</code></td><td><code title="event-xhr-loadend">loadend</code></td><td>When the request has completed, regardless of   whether or not it was successful.</td></tr>
      </tbody>
    </table><br>

+ [Syntax for download progress](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + create [new connection](#xhr)
  + open connection w/ get request<a name="get"></a>: `xhr.open('GET', url, true);`
  + ...
  + download progress: `xhr.onprogress = function(e) { // do sth. }`
  + [send request](#send)

+ [Syntax for upload progress](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + create [new connection](#xhr)
  + open connection w/ post request<a name="post"></a>: `xhr.open('POST', url, true);`
  + ...
  + upload progress: <code>xhr.<span style="color: #ff0000; font-weight: bold;">upload</span>.onprogress = function(e) { // do sth. }</code>
  + [send request](#send)

+ [Progess values and the total file size](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + properties of `progress` event
    + `loaded`: the number if bytes downloaded and uploaded by the browser so far
    + `total`: the file's size (in bytes)
  + combining `<progress>` element to render an animated animated progress bar

+ [`FormData` object](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-323-uploading-files-and-monitoring-progress)
  + uploading one or more files to an HTTP seerver
  + a container for parts in the multipart data sent by aan XHR2 POST request
  + synatx: `var data = new FormData(form);`
    + `form`: the HTML form
    + `data`: containg all the input field's values
  + adding files: `data.append(name, valuye);`

+ Example: [displaying progress bar](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + tasks:
    + associate the `value` and `max` attributes of the `<progress>` element w/ progress event
    + reflect the actual proportions of the file downloaded

+ [Syntax for uploading file w/ progress bar](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-323-uploading-files-and-monitoring-progress)
  + add listener for upload progress<a name="uploadProgress"></a>: `xhr.upload.onprogress = function(e) {...};`
  + number of bytes uploaded: `progress.value = e.loaded;`
  + total number of bytes in the file: `progress.max = e.total;`

+ Example: [uploading selected file(s)](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-323-uploading-files-and-monitoring-progress)
  + using a `FormData` object for uploading one or more files to an HTTP seerver
  + tasks:
    + callback on selecting file(s)
    + create `FormData` object
    + prepare XHR2 request and send w/ `FormData` object

+ Example: [uploading file w/ progress bar](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-323-uploading-files-and-monitoring-progress)
  + task: add progress bar for the previous example


## Upload Files with HTML Form

+ [Uploading forms and files](../WebDev/Frontend-W3C/3-HTML5AppGame/03e-Online.md)
  + typical tasks
    + submit a form w/ regular input fields
    + benefit from the HTML5 built-in validation
    + upload files
    + monitor the file upload progress w/ a progress bar
  + solutions
    + typical: jQuery plugins
    + alternative: only HTML5 APIs, easy, faster, and lower page weight
  + typical design
    + a regular HTML5 form
    + the input fields for entering a name, address, age, etc.
    + selecting and uploading multiple files
  + approaches
    + serial approach
    + packaged approach

+ Example: [uploading files w/ Ajax/HR2 & DnD](../WebDev/Frontend-W3C/3-HTML5AppGame/03d-Online.md#notes-for-345-files-upload-using-ajaxxhr2)


## Serial Approach for Upload

+ [Serial approach](../WebDev/Frontend-W3C/3-HTML5AppGame/03e-Online.md)
  + uploading the files as soon as selected or dragged and dropped
  + design
    + an Ajax/XHR2
    + a form w/ an `<input type=file multiple>` input field
    + one or more `<progress>` elements for monitoring file uploads
    + form w/ input fields of different types
  + interactions
    + user drag and drop files
    + start being uploaded immediately
    + form only sent all the fields valid
  + example: Gmail's behavior
    + commposing a message and adding an attachment
    + attachments uploaded as soon as selected or dropped into the message window
    + message only sent when the "send" button pressed
    + empty fields w/ `required` attribute &#36;\to&#36; error message &#36;\to&#36; not submitted
    + server-side: join the files asynchronously uploaded w/ the rest of the form's value &#36;\gets&#36; PHP code

+ Example: [server-side PHP code w/ serial approach](../WebDev/Frontend-W3C/3-HTML5AppGame/03e-Online.md#notes-for-353-serial-approach)

## Packaged Approach for Upload


+ [Packaged approach](../WebDev/Frontend-W3C/3-HTML5AppGame/03e-Online.md)
  + send all form content, including files, only when the form is submitted
  + design
    + send all of the form's content at once w/ a single Ajax request &#36;\to&#36; only one progress bar
    + probably using multiple Ajax requests, not starting until the submit button clicked
  + sending everything at the same time using Ajax/JavaScript, including the regular input field conetnt and the selected fields



