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

+ [Example: playing downloaded sound](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
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

+ [Example: displaying progress bar](../WebDev/Frontend-W3C/3-HTML5AppGame/03b-Online.md#notes-for-322-ajaxxhr2-and-binary-files)
  + tasks:
    + associate the `value` and `max` attributes of the `<progress>` element w/ progress event
    + reflect the actual proportions of the file downloaded

