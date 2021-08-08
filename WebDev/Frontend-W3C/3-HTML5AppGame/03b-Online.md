# Module 3: HTML5 file upload and download section


## 3.2 File API and Ajax / XHR2 requests


### 3.2.1 Ajax and XHR2

We present below a short history of Ajax: an introduction to XMLHttpRequest level 2 (XHR2).

> __Wikipedia definition:__ "Ajax, short for Asynchronous JavaScript and XML), is a group of interrelated Web development techniques used on the client-side to create asynchronous Web applications. With Ajax, Web applications can send data to and retrieve from a server asynchronously (in the background) without interfering with the display and behavior of the existing page. Data can be retrieved using the XMLHttpRequest object. Despite the name, the use of XML is not required (JSON is often used), and the requests do not need to be asynchronous."

Ajax appeared around 2005 with Google Maps, and is now widely used. We are not going to teach you Ajax programming, but instead focus on the relationships between "the new version of Ajax", known as XHR2 (for XmlHttpRequest level 2) and the [File API](https://www.w3.org/TR/FileAPI/) (seen in the W3Cx [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) MOOC). Also, you will discover that the HTML5 `<progress>` element is of great use for monitoring the progress of file uploads (or downloads).

We recommend reading [this article from HTML5Rocks.com](https://www.html5rocks.com/en/tutorials/file/xhr2/) that presents the main features of XHR2.

Briefly, these improvements include:

+ New, easier to use syntax,
+ In-browser encoding/decoding of binary files,
+ Progress monitoring of uploads and downloads.

The following sections of this course present a few examples of file downloads/uploads together with the file API and show how to monitor progress.

The current support of XHR2 is excellent: see related [CanIUse's browser compatibility table](https://caniuse.com/#feat=xhr2).


#### Notes for 3.2.1 Ajax and XHR2

+ Asynchronous JavaScript and XML (Ajax)
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


### 3.2.2 Ajax/XHR2 and binary files

#### Live coding video: downloading files

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3hhbMVq)


#### Ajax and binary files

__Ajax and binary files - downloading files and monitoring progress__

HTTP is a text based protocol, so when you upload/download images, videos or any binary file, they must first be text encoded for transmission, then decoded on-the-fly upon receipt by the server or browser. For a long time, when using Ajax, these binary files had to be decoded "by hand", using JavaScript code. Not recommended!

We won't go into too much detail here, but  all browsers (> 2012) support XHR2. XHR2 adds the option to directly download binary data. With XHR2, you can ask the browser to encode/decode the file you send/receive, natively. To do this, when you use `XMLHttpRequest` to send or receive a file, you must set the `xhr.responseType` as `arrayBuffer`.

Below is a function that loads a sound sample using XMLHttpRequest level 2.

_Note_: 1) the simple and concise syntax, and 2) the use of the new `arrayBuffer` type for the expected response (_line 5_):

<div><ol>
<li value="1">// Load a binary file from a URL as an ArrayBuffer.</li>
<li>function loadSoundFile(url) {</li>
<li>&nbsp; &nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; &nbsp;xhr.open('GET', url, true);<br><br></li>
<li>&nbsp; &nbsp;<strong style="color: red;">xhr</strong><strong style="color: red;">.responseType = 'arraybuffer';<span style="color: #ff0000;"></strong></li>
<li>&nbsp; &nbsp;xhr.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; initSound(this.response); // this.response is an ArrayBuffer.</li>
<li>&nbsp; &nbsp;};<br><br></li>
<li>&nbsp; &nbsp;xhr.send();</li>
<li>}</li>
</ol></div><br>


#### Play downloaded song

__Example: download a binary song file using XHR2 and responseType='arraybuffer', and play it using Web Audio__

Try [this example](https://jsbin.com/mecakaz/edit?html,js,console,output) on JSBin:

[Local Demo](src/03b-example01.html)

In this example, instead of reading the file from disk, we download it using XHR2.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2TwBOet')"
    src    = "https://bit.ly/3hyjzgH"
    alt    = "Downloading file with Xhr2"
    title  = "Downloading file with Xhr2"
  />
</figure>


Complete source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp;&lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;title&gt;XHR2 and binary files + Web Audio API&lt;/title&gt;</li>
<li>&nbsp;&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;p&gt;Example of using XHR2&nbsp;and &lt;code&gt;xhr.responseType = 'arraybuffer';&lt;/code&gt; to download a binary sound file</li>
<li> and start playing it on user-click using the Web Audio API.&lt;/p&gt;</li>
<li> </li>
<li> &lt;p&gt;</li>
<li> &lt;h2&gt;Load file using Ajax/XHR2 and the arrayBuffer response type&lt;/h2&gt;</li>
<li> &lt;button <strong style="color: red;">onclick="downloadSoundFile('https://myserver.com/song.mp3');</strong>"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;Download and play example song.</li>
<li>&nbsp;&lt;/button&gt;</li>
<li> &lt;button onclick="playSound()" disabled&gt;Start&lt;/button&gt;</li>
<li> &lt;button onclick="stopSound()" disabled&gt;Stop&lt;/button&gt;</li>
<li>&lt;script&gt;</li>
<li>&nbsp; // WebAudio context</li>
<li>&nbsp; var context = new window.AudioContext();</li>
<li>&nbsp; var source = null;</li>
<li>&nbsp; var audioBuffer = null;</li>
<li>&nbsp;</li>
<li>&nbsp; function stopSound() {</li>
<li>&nbsp; &nbsp;&nbsp;if (source) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;source.stop();</li>
<li>&nbsp; &nbsp; }</li>
<li>&nbsp; }</li>
<li>&nbsp;</li>
<li>&nbsp; function playSound() {</li>
<li>&nbsp; &nbsp;&nbsp;// Build a source node for the audio graph</li>
<li>&nbsp; &nbsp; source = context.createBufferSource();</li>
<li>&nbsp; &nbsp; source.buffer = audioBuffer;</li>
<li>&nbsp; &nbsp; source.loop = false;</li>
<li>&nbsp; &nbsp;&nbsp;// connect to the speakers</li>
<li>&nbsp; &nbsp; source.connect(context.destination);</li>
<li>&nbsp; &nbsp; source.start(0); // Play immediately.</li>
<li>&nbsp; }</li>
<li>&nbsp;</li>
<li>&nbsp; function initSound(audioFile) {</li>
<li>&nbsp; &nbsp;&nbsp;// The audio file may be an mp3 -&nbsp;we must decode it before playing it from memory</li>
<li>&nbsp; &nbsp; context.decodeAudioData(audioFile, function(buffer) {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("Song decoded!");</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// audioBuffer the decoded audio file we're going to work with</li>
<li>&nbsp; &nbsp; &nbsp; audioBuffer = buffer;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// Enable all buttons once the audio file is</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// decoded</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var buttons = document.querySelectorAll('button');</li>
<li>&nbsp; &nbsp; &nbsp; buttons[1].disabled = false; // play</li>
<li>&nbsp; &nbsp; &nbsp; buttons[2].disabled = false; // stop</li>
<li>&nbsp; &nbsp; &nbsp; alert("Binary file has been loaded and decoded, use play / stop buttons!")</li>
<li>&nbsp; &nbsp;&nbsp;}, function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;console.log('Error decoding file', e);</li>
<li>&nbsp; &nbsp;&nbsp;}); </li>
<li>&nbsp; }</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;// Load a binary file from a URL as an ArrayBuffer.</li>
<li>&nbsp; function downloadSoundFile(url) {</li>
<li>&nbsp; &nbsp;&nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; &nbsp; xhr.open('GET', url, true);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; <strong style="color: red;">xhr</strong><strong style="color: red;">.responseType = 'arraybuffer'; // THIS IS NEW WITH HTML5!</strong></li>
<li>&nbsp; &nbsp; xhr.onload = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;console.log("Song downloaded, decoding...");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;initSound(this.response); // this.response is an ArrayBuffer.</li>
<li>&nbsp; &nbsp; };</li>
<li>&nbsp; &nbsp; xhr.onerror = function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("error downloading file");</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; xhr.send();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;console.log("Ajax request sent... wait until it downloads completely");</li>
<li>&nbsp; } </li>
<li>&lt;/script&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

__Explanations:__

+ _Line 12:_ a click on this button will call the `downloadSoundFile` function, passing it the URL of a sample mp3 file.
+ _Lines 58-73:_ this function sends the Ajax request, and when the file has arrived, the `xhr.onload` callback is called (_line 63_).
+ _Lines 39-55:_ The initSound function decodes the mp3 into memory using the `WebAudio` API, and enables the play and stop buttons.
+ When the play button is enabled and clicked (_line 15_) it calls the `playSound` function. This builds a minimal Web Audio graph with a `BufferSource` node that contains the decoded sound (_lines 31-32_), connects it to the speakers (_line 35_), and then plays it.


#### Monitoring uploads and downloads

__Monitoring uploads or downloads using a `progress` event__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/2TwBOet')"
    src    = "https://bit.ly/3xkcnLY"
    alt    = "downloading progression using a progress element"
    title  = "downloading progression using a progress element"
  />
</figure>


__1 - Declare a `progress` event handler__

XHR2 now provides `progress` event attributes for monitoring data transfers. Previous implementations of XmlHttpRequest didn't tell us anything about how much data has been sent or received. The [ProgressEvent](https://www.w3.org/TR/progress-events/) interface adds 7 events relating to uploading or downloading files.

<table>
  <thead>
    <tr><th style="background-color: #0066ff;">attribute</th><th style="background-color: #0066ff;">type</th><th style="background-color: #0066ff;  ">Explanation</th></tr>
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

The syntax for declaring progress event handlers is slightly different depending on the type of operation: a download (using the GET HTTP method), or an upload (using POST).


__Syntax for download:__

<div><ol>
<li value="1">var xhr = new XMLHttpRequest();</li>
<li> xhr.open('GET', url, true);</li>
<li>...</li>
<li><strong style="color: red;">xhr.onprogress = function(e) {</strong></li>
<li> <strong style="color: red;">// do something</strong></li>
<li><strong style="color: red;">}</strong></li>
<li>&nbsp;</li>
<li>xhr.send();</li>
</ol></div><br>

Note that an alternative syntax such as `xhr.addEventListener('progress', callback, false)` also works.

__Syntax for upload:__

<div><ol>
<li value="1">var xhr = new XMLHttpRequest();</li>
<li> xhr.open('POST', url, true);</li>
<li>...</li>
<li><strong style="color: red;">xhr.<span style="color: #ff0000;">upload.onprogress = function(e) {</strong></li>
<li> <strong style="color: red;">// do something</strong></li>
<li><strong style="color: red;">}</strong></li>
<li>&nbsp;</li>
<li>xhr.send();</li>
</ol></div><br>

Notice that the only difference is the "upload" added after the name of the request object: with GET we use `xhr.onprogress` and with POST we use <span style="font-family: 'courier new', courier;">xhr.<span style="color: #ff0000;">upload.onprogress.

Note that an alternative syntax such as <span style="font-family: 'courier new', courier;">xhr.<span style="color: #ff0000;">upload.addEventListener('progress', callback, false) also works.

__2 - Get progress values (how many bytes have been downloaded) and the total file size__

The event `e` passed to the `onprogress` callback has two pertinent properties:

1. `loaded` which corresponds to the number of bytes that have been downloaded or uploaded by the browser, so far, and
2. `total` which contains the file's size (in bytes).

Combining these with a `<progress>` element, makes it very easy to render an animated progress bar. Here is a source code extract that does this for a download operation:

HTML:

<div><ol>
<li value="1">&lt;progress id="downloadProgress" value=0&gt;&lt;/progress&gt;</li>
</ol></div><br>

JavaScript:

<div><ol>
<li value="1">// progress element</li>
<li><strong style="color: red;">var progress = document.querySelector('#downloadProgress');</strong></li>
<li>&nbsp;</li>
<li>function downloadSoundFile(url) {</li>
<li>&nbsp;&nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; xhr.open('GET', url, true);</li>
<li>&nbsp;</li>
<li>&nbsp; ...</li>
<li>&nbsp; xhr.onprogress = function(e) {</li>
<li>&nbsp; &nbsp; <strong style="color: red;">.value = e.loaded;</strong></li>
<li>&nbsp; &nbsp; <strong style="color: red;">.max = e.total;</strong></li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp; xhr.send();</li>
<li>} </li>
</ol></div><br>

__Explanations:__ by setting the `value` and `max` attributes of the `<progress>` element with the current number of bytes downloaded by the browser and the total size of the file (_lines 10-11_), it will reflect the actual proportions of the file downloaded/still to come.

For example, with a file that is 10,000 bytes long, if the current number of bytes downloaded is 1000, then `<progress value=1000 max=10000>` will look like this: 

And a current download of 2000 bytes will define `<progress value=2000 max=10000>` and will look like this:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/2TwBOet" ismap target="_blank">
    <img style="margin: 0.1em;" height=50
      src   = "https://bit.ly/3xiQ1ds"
      alt   = "progress bar 10%"
      title = "progress bar 10%"
    >
    <img style="margin: 0.1em;" height=50
      src   = "https://bit.ly/3dIH2KX"
      alt   = "progress bar 20%"
      title = "progress bar 20%"
    >
  </a>
</div>


__Complete example: monitoring the download of a song file__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2TwBOet')"
    src    = "https://bit.ly/3hNZ6or"
    alt    = "monitoring download"
    title  = "monitoring download"
  />
</figure>


 This is a variant of the previous example that uses the `progress` event and a `<progress>` HTML5 element to display an animated progression bar while the download is going on.

[Try it on JSBin](https://jsbin.com/nuxanaf/edit?html,output) - look at the code, which includes the previous source code extract.

[Local Demo](src/03b-example02.html)


#### Notes for 3.2.2 Ajax/XHR2 and binary files

+ Ajax and binary files
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

+ Syntax for downloading file
  + task: download sound sample w/ `XMLHttpRequest` level 2
  + load sound file: `function loadSoundFile(url) {...};`
  + create new connection for XHR2<a name="xhr"></a>: `var xhr = new XMLHttpRequest();`
  + open connect w/ get request: `xhr.open('GET', url, true);`
  + set response type<a name="rspType"></a>: `xhr.responseType = 'arrayBuffer';`
  + add event listener for complete downloading<a name="onload"></a>: `xhr.onload = function(e) { initSound(this.response); };`
  + send request to server<a name="send"></a>: `xhr.send();`

+ Example: playing downloaded sound
  + tasks:
    + click button to download sound file
    + send Ajax request and call `xhr.onload` callback after file arrived
    + decode mp3 into memory and enable start/stop buttons
    + click button to play and stop sound
  + HTML snippet
    + button to trigger download: `<button onclick="downloadSoundFile('http://.../song.mp3');"> Download and play example sound. </button>`
    + start to play: `<button onclick="playSound()" disabled>Start</button>`
    + stop to play: `<button onclick=""stopSound()" disabled>Stop</button>`
  + JavaScript snippet
    + declare variables for WebAudio: `var context = new window.AudioContext(); var source = url; var audioBuffer = null;`
    + stop playing sound: `function stopSound() { if (source) source.stop(); }`
    + start to play sound: `function starSound() {...}`
      + create a source node and set properties: `source = context.createBufferSource(); source.buffer = audioBuffer; source.loop = false;`
      + connect source to speaker: `source.connect(context.destination);`
      + play sound immediately: `source.start(0);`
    + init sound sample: `function initSound(audioFile) {...}`
      + decode mp3 file: `context.deccodeAudioData(audioFile, function(buffer) {...}, function(e) { console.log('Error decoding file', e); });`
      + log msg: `console.log("Sound decoded!");`
      + set variable: `audioBuffer = buffer;`
      + enable buttons once decoded: `var buttons = document.querySelectorAll('button'); button[1].disabled = false; button[2].disabled = false;`
      + display msg: `alert("Binary file has been loaded and decoded, use play / stop buttons!");`
    + download sound file: `function downloadSoundFile(url) {...}`
      + create [new connection](#xhr) for XHR2
      + open connection: `function loadSoundFile(url) {...}`
      + set response type: `xhr.responseType = 'arraybuffer';`
      + add listener for download: `xhr.onload = function(e) { console.log("Song downloaded, decoding..."); initSound(this.response); }`
      + add listener for error: `xhr.onerror = function(e) { console.log("error downloading file"); }`
      + [send request](#send)
      + log msg: `console.log("Ajax request sent... wait until it downloads completely!");`

+ Monitoring w/ `progress` event
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

+ Syntax for download progress
  + create [new connection](#xhr)
  + open connection w/ get request<a name="get"></a>: `xhr.open('GET', url, true);`
  + ...
  + download progress: `xhr.onprogress = function(e) { // do sth. }`
  + [send request](#send)

+ Syntax for upload progress
  + create [new connection](#xhr)
  + open connection w/ post request<a name="post"></a>: `xhr.open('POST', url, true);`
  + ...
  + upload progress: <code>xhr.<span style="color: #ff0000; font-weight: bold;">upload.onprogress = function(e) { // do sth. }</code>
  + [send request](#send)

+ Progess values and the total file size
  + properties of `progress` event
    + `loaded`: the number if bytes downloaded and uploaded by the browser so far
    + `total`: the file's size (in bytes)
  + combining `<progress>` element to render an animated animated progress bar

+ Example: displaying progress bar
  + tasks:
    + associate the `value` and `max` attributes of the `<progress>` element w/ progress event
    + reflect the actual proportions of the file downloaded
  + HTML snippet: `<progress id="downloadProgress" value=0></progress>`
  + JavaScript snippet
    + access element: `var progress = document.querySelector('#downloadProgress');`
    + download binary file: `function downloadSoundFile(url) {...}`
    + create [new connection](#xhr)
    + open connection w/ [get request](#get)
    + ...
    + add progress event: `xhr.onprogress = function(e) { progress.value = e.loaded; progress.max = e.total; }`
    + [send request](#send)


### 3.2.3 Uploading files and monitoring progress


#### Live coding video: uploading files using Ajax XHR2

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3hzgooX)


#### Uploading files with `FormData` object

Here is an example that uses a `FormData` object for uploading one or more files to an HTTP server.

Notice that the URL of the server is fake, so the request will fail. However, the simulation takes time, and it is interesting to see how it works.

Later on, we will show full examples of real working code with server-side PHP source, during the “File API, drag and drop and XHR2” lecture.

Try [the example on JSBin](https://jsbin.com/pidusap/edit):

[Local Demo](src/03b-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yjWfdi')"
    src    = "https://bit.ly/3695WPQ"
    alt    = "file upload example 1"
    title  = "file upload example 1"
  />
</figure>


Source code of the example:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;meta charset="utf-8" /&gt;</li>
<li>&nbsp; &nbsp;&lt;title&gt;File upload with XMLHttpRequest level 2 and HTML5&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li>&nbsp;</li>
<li> &lt;body&gt;</li>
<li> &lt;h1&gt;Example of XHR2&nbsp;file upload&lt;/h1&gt;</li>
<li>&nbsp; Choose a file and wait a little until it is uploaded (on a fake &nbsp; </li>
<li>&nbsp; server). A message should pop up once the file is uploaded 100%.</li>
<li> &lt;p&gt;</li>
<li> &lt;input id="file" type="file" /&gt;</li>
<li> &lt;/p&gt;</li>
<li> &lt;script&gt; </li>
<li> var fileInput = document.querySelector('#file');</li>
<li>&nbsp;</li>
<li> fileInput.onchange = function() {</li>
<li>&nbsp; &nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; &nbsp;xhr.open('POST', 'upload.html'); // With FormData, </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // POST is mandatory</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;<strong style="color: red;">xhr</strong><strong style="color: red;">.onload = function() {</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">alert</strong><strong style="color: red;">('Upload complete !');</strong></li>
<li>&nbsp; &nbsp;<strong style="color: red;">};</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;<strong style="color: red;">var form = new FormData();</strong></li>
<li>&nbsp; &nbsp;<strong style="color: red;">form</strong><strong style="color: red;">.append('file', fileInput.files[0]);</strong></li>
<li>&nbsp; &nbsp;// send the request</li>
<li>&nbsp; &nbsp;xhr.send(form);</li>
<li>};</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

__Explanations:__

+ _Line 18_: callback called when the user selects a file.
+ _Lines 19-20_: preparation of the XHR2 request.
+ _Lines 27-30_: a `FormData` object is created (this will contain the (MIME) multipart form-data which will be sent by the `POST` request).
+ _Line 30_: the request is sent, with the `FormData` object passed as a parameter (all data is sent).
+ _Line 23_: when the file is completely uploaded, the `onload` listener is called and an alert message is displayed.


#### Monitor the upload progress

Here is a more user-friendly example. It is basically the same, but this time, we'll monitor the progress of the upload using a method similar to that used for monitoring file downloads:

+ We use a `<progress>` element and its two attributes `value` and `max`.
+ We also bind an event handler to the `progress` event that an `XMLHttpRequest` will trigger. The event has two properties: `loaded` and `total` that respectively correspond to the number of bytes that have been uploaded, and to the total number of bytes we need to upload (i.e., the file size).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yjWfdi')"
    src    = "https://bit.ly/2SQACCq"
    alt    = "file upload with progress bar"
    title  = "file upload with progress bar"
  />
</figure>


Here is the code of such an event listener:

<div><ol>
<li value="1">xhr.<span style="color: #ff0000;">upload.onprogress = function(e) { </li>
<li>&nbsp; progress.value =&nbsp;e.loaded<span style="color: #666600;" color="#666600">; //&nbsp;number of bytes uploaded</li>
<li>&nbsp; progress.max = e.total;<span style="color: #000000;" color="#000000">&nbsp; &nbsp; //&nbsp;total number of bytes in the file</li>
<li>};</li>
</ol></div><br>

Try [the example on JSBin](https://jsbin.com/qedaja/edit?html,output):

[Local Demo](src/03b-example04.html)

Code from this example (nearly the same as previous example's code):

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li> &lt;head&gt;</li>
<li>&nbsp; &nbsp;&lt;meta charset="utf-8" /&gt;</li>
<li>&nbsp; &nbsp;&lt;title&gt;HTML5 file upload with monitoring&lt;/title&gt;</li>
<li> &lt;/head&gt;</li>
<li>&nbsp;</li>
<li> &lt;body&gt;</li>
<li> &lt;h1&gt;Example of XHR2 file upload, with progress bar&lt;/h1&gt;</li>
<li>Choose a file and wait a little until it is uploaded (on a fake server).</li>
<li> &lt;p&gt;</li>
<li> &lt;input id="file" type="file" /&gt;</li>
<li> &lt;br/&gt;&lt;br/&gt;</li>
<li> <strong style="color: red;">&lt;progress id="progress" value=0&gt;&lt;/progress&gt;</strong></li>
<li>&nbsp;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp;var fileInput = document.querySelector('#file'),</li>
<li>&nbsp; &nbsp;<strong style="color: red;">progress </strong><strong style="color: red;">= document.querySelector('#progress');</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;fileInput.onchange = function() {</li>
<li>&nbsp; &nbsp; &nbsp;var xhr = new XMLHttpRequest();</li>
<li>&nbsp; &nbsp; &nbsp;xhr.open('POST', 'upload.html');</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">xhr</strong><strong style="color: red;">.upload.onprogress = function(e) {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">.value = e.loaded;</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong style="color: red;">.max = e.total;</strong></li>
<li>&nbsp; &nbsp; &nbsp;<strong style="color: red;">};</strong></li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;xhr.onload = function() {</li>
<li>&nbsp; &nbsp; &nbsp;alert('Upload complete!');</li>
<li>&nbsp; &nbsp;};</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;var form = new FormData();</li>
<li>&nbsp; &nbsp;form.append('file', fileInput.files[0]);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;xhr.send(form);</li>
<li> };</li>
<li> &lt;/script&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>

The only difference between these two worked-examples is the `onprogress` listener which updates the progress bar's `value` and `max` attributes.


#### Notes for 3.2.3 Uploading files and monitoring progress

+ Syntax for uploading file w/ progress bar
  + add listener for upload progress<a name="uploadProgress"></a>: `xhr.upload.onprogress = function(e) {...};`
  + number of bytes uploaded: `progress.value = e.loaded;`
  + total number of bytes in the file: `progress.max = e.total;`

+ `FormData` object
  + uploading one or more files to an HTTP server
  + a container for parts in the multipart data sent by aan XHR2 POST request
  + syntax: `var data = new FormData(form);`
    + `form`: the HTML form
    + `data`: containing all the input field's values
  + adding files: `data.append(name, value);`

+ Example: uploading selected file(s)
  + tasks:
    + callback on selecting file(s)
    + create `FormData` object
    + prepare XHR2 request and send w/ `FormData` object
  + HTML snippet: `<input id="file" type="file" />`
  + JavaScript snippet:
    + access input element: `var fileInput = document.querySelector('#file');`
    + add listener for change: `fileInput.onchange = function() {...}`
    + create [new connection](#xhr)
    + open connection w/ post request and FormData: `xhr.open('POST', 'upload.html');`
    + alert msg after uploaded<a name="upComplete"></a>: `xhr.onload = function() { alert('Upload complete!'); }`
    + create new data form and store file within<a name="form"></a>: `var form = new FormData(); form.append('file', fileInput.files[0]);`
    + send request w/ form<a name="sendForm"></a>: `xhr.send(form);`

+ Example: uploading file w/ progress bar
  + task: add progress bar for the previous example
  + HTML snippet:
    + input fields: `<input id="file" type="file" />`
    + progress bar: `<progress id="progress" value=0></progress>`
  + JavaScript snippet
    + access input field and progree bar: `var fileInput = document.querySelector("#file"); progress = document.querySelector("#progress");`
    + add input change listener: `fileInput.onchange = function() {...}`
    + create [XHR2 request](#xhr)
    + open connection: `xhr.open('POST', 'upload.html');`
    + add listener for [upload progress](#uploadProgress)
    + [alert msg after uploaded](#upComplete)
    + create [new object and store file](#form)
    + send [request w/ form](#sendForm)


### 3.2.4 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics of discussion:

+ Did you hear about the [Fetch API](https://davidwalsh.name/fetch)? This APIs  is easier to use than XhR2, but monitoring progress is a bit trickier and will require the use of the streams API. Monitoring upload is not yet supported. See for example [this article](https://javascript.info/fetch-progress).
+ Did you note that using XHR2 for monitoring progress is really simple and efficient?  What is your experience? Please share ;)
+ How can we monitor the speed of an upload/download in bytes per second? What would you propose? Did you find any interesting resources on the Web that explain that?


#### Optional projects:

+ If you know how to program server-side code, please make a small app that will upload files, monitor the progress of the upload, save the files server-side, and send back a message containing the URLs of the files. Better: create a Web page that displays links to the uploaded files.
+ Try to write an `assetLoader` function that will download a set of images and sound (maybe using the BufferUtility seen during Module 1), but this time with a progress bar. This could be useful for a game, or for a Web app that needs to load resources before starting.


