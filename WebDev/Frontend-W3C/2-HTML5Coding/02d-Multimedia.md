# Week 2: HTML5 Multimedia

## 2.4 Webcam, microphone: the getUserMedia API


### 2.4.0 Lecture Notes

+ [The `getUserMedia` API - Webcam access](#241-webcam)
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

+ [The `getUserMedia` API - start/stop the Webcam](#242-more-on-getusermedia)
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

+ [Accessing the microphone](#243-using-the-microphone)
  + `navigator.getUserMedia({audio:true}, onSuccess, onError)`: capture the microphone input
  + `navigator.getUserMedia({video:true, audio:true}, onSuccess, onError)`: access the video and audio simultaneously
  + [WebRTC](https://www.w3.org/TR/webrtc/): a W3C specification for P2P audio/video/data Real Time Communication


+ [Webcam resolutions](#244-webcam-resolution)
  + "constraint" object: 
    + As constraints applied to an existing local video stream using the "change constraints" API, where it may cause the video engine to reconfigure the device or codec for that particular stream.
    + As constraints applied to an incoming video stream using the "change constrains" API on a MediaStreamTrack, where it serves to inform the video engine about the desirable properties of the video track, which may lead to the video engine choosing to reencode the video and/or signal a remote video source that it wishes certain constraints to be put in place.
  + [example: different resolutions](#full-example-choose-between-3-different-resolutions)
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

  + [rear and front camera in smartphone](#selecting-the-front-or-rear-camera-on-smartphones)

    ```js
    document.getElementById('flip-button').onclick = function() {
        front = !front;
    };

    // toggle front and back camera (mobile) by clicking a button
    constraints = { video: { facingMode: (front? "user" : "environment") } };
    ```

+ [The MediaRecorder API](#245-the-mediarecorder-api): [usage procedure](#five-steps-are-needed-to-use-the-mediarecorder-object)
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



### 2.4.1 Webcam

#### Introduction to the getUserMedia API

The [getUserMedia API](https://www.w3.org/TR/mediacapture-streams/) is useful for controlling a Webcam video stream. This chapter presents the most interesting parts, related to the `<video>` and `<audio>` elements.

While this API is one component of the [WebRTC specification](https://www.w3.org/TR/webrtc/) and therefore not considered a "real" part of the HTML5 specification, we still consider it relevant to the "multimedia" part of this course. The getUserMedia API, when dealing with video streams, is always used in conjunction with the `<video>` element.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y3aztar7')"
    src    ="https://tinyurl.com/y5xy54qv"
    alt    ="screenshot of a webcam display in a web page"
    title  ="screenshot of a webcam display in a web page"
  />
</figure>


#### Typical use of the getUserMedia API with a Webcam

The main idea is to set the `srcObject` attribute of a `<video>` element to the live video stream object coming out of the Webcam. To get this stream, you'll have to call the `navigator.getUserMedia(params)` method from the getUserMedia API, that returns an [ES6 promise](https://tinyurl.com/y4atxcjf) (ES stands for ECMAScript and is the scripting language that forms the basis of JavaScript). Do not panic if you do not know ES6's promises! The syntax is very simple, and you'll learn what you need from the provided examples.

The stream is passed as a parameter to the `then()` method returned by the promise, as in this typical example ([you can try it at JSBin](https://output.jsbin.com/gakikop) - press the "edit in JSBin" button to see the source code) ([Local Example - Webcam](src/2.4.1-example1.html)):

<div><ol>
<li value="1">&lt;video id="myVideo" autoplay&gt;Fallback msg here.&lt;/video&gt;</li>
<li>&lt;script&gt;</li>
<li>&nbsp; if (navigator.getUserMedia) {</li>
<li>&nbsp; &nbsp; // request video and audio stream from the user's webcam</li>
<li>&nbsp; &nbsp; navigator.mediaDevices.getUserMedia({</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; audio: true,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; video: true</li>
<li>&nbsp; &nbsp; }).<span style="background-color: #ffffff;">then((stream) =&gt; {</span></li>
<li>&nbsp; &nbsp; &nbsp; var video = document.querySelector('#myVideo');</li>
<li>&nbsp; &nbsp; &nbsp; video.srcObject = stream;</li>
<li>&nbsp; &nbsp; &nbsp; video.play();</li>
<li>&nbsp; &nbsp; }).catch((error) =&gt; {</li>
<li>&nbsp; &nbsp; &nbsp; console.log('navigator.getUserMedia error: ', error);</li>
<li>&nbsp; &nbsp; }); </li>
<li> }</li>
<li>&lt;/script&gt;</li>
</ol></div>

<p style="border: 1px solid; padding: 10px; margin: 10px; text-align: center;"><span style="color: #ff0000;"><strong>HTTPS is mandatory:</strong></span> for getUserMedia to work, it is mandatory to access the page that contains the JavaScript code through <span style="font-family: courier new, courier;">https://</span>. Otherwise you will get an error message. Note that all examples on JSBin use <span style="font-family: courier new, courier;">https://jsbin.com/</span>....</p>

Support of stream is [very good in all modern browsers](https://caniuse.com/#feat=stream), including mobile ones.


#### Knowledge check 2.5.1

1. What is getUserMedia?<br/>
  a. A JavaScript API that can be used to redirect the Webcam video stream to a video element<br/>
  b. An API which only works with WebRTC for audio conferencing<br/>
  c. An upcoming API that is not available yet on browsers, but can be emulated by the video element<br/>

  Ans: a<br/>
  Explanation: getUserMedia is part of the WebRTC specification, but it's related to the `<video>` element too. Indeed, it can be used to redirect the Webcam video stream to a `<video>` element. If this element has the autoplay attribute, it will display the video stream as soon as it is available.


### 2.4.2 More on getUserMedia

Let's see some more examples of what we can do with the getUserMedia API: start/stop the Webcam, take a screenshot from the current video stream from the Webcam, and apply CSS effects in real time. Below, we give links to some cool examples available on the Web.

#### How to stop/release the Webcam

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y6xzkams')"
    src    ="https://tinyurl.com/y5cs88ya"
    alt    ="start and stop the Webcam"
    title  ="start and stop the Webcam"
  />
</figure>

[Online version at JSBin](https://output.jsbin.com/hafigop) ([Local Example - video controls](src/2.4.2-example1.html))

In order to stop the Webcam and make the hardware "unlock it", you need to call the `stop()` method of the video stream.

Modified version of the previous example:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Webcam start/stop&lt;/title&gt;</li>
<li> &lt;script&gt;</li>
<li>&nbsp; let webcamStream;</li>
<li>&nbsp;</li>
<li>&nbsp; function startWebcam() {</li>
<li>&nbsp; &nbsp; // request video and audio stream from the user's webcam</li>
<li>&nbsp; &nbsp; navigator.mediaDevices.getUserMedia({</li>
<li>&nbsp; &nbsp; &nbsp; audio: true,</li>
<li>&nbsp; &nbsp; &nbsp; video: true</li>
<li>&nbsp; &nbsp; }).<span style="background-color: #ffffff;">then((stream) =&gt; {</span></li>
<li>&nbsp; &nbsp; &nbsp; let video = document.querySelector('#video');</li>
<li>&nbsp; &nbsp; &nbsp; video.srcObject = stream;</li>
<li>&nbsp; &nbsp; &nbsp; video.play();</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; webcamStream = stream;</li>
<li>&nbsp; &nbsp; }).catch((error) =&gt; {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log('navigator.getUserMedia error: ', error);</li>
<li>&nbsp; &nbsp; });</li>
<li>&nbsp; }</li>
<li>&nbsp;</li>
<li>&nbsp; function stopWebcam() {</li>
<li>&nbsp; &nbsp; webcamStream.getTracks()[0].stop(); // audio</li>
<li>&nbsp; &nbsp; webcamStream.getTracks()[1].stop(); // video</li>
<li>&nbsp; } </li>
<li> &lt;/script&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body &gt;</li>
<li>&nbsp; &lt;video width=400 height=400 id="video" controls&gt;&lt;/video&gt;</li>
<li>&nbsp; &lt;p&gt;</li>
<li>&nbsp; &lt;button onclick="startWebcam();"&gt;Start WebCam&lt;/button&gt;</li>
<li>&nbsp; &lt;button onclick="stopWebcam();"&gt;Stop WebCam&lt;/button&gt; </li>
<li>&nbsp; &lt;/p&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

__Explanations__:

+ _Lines 11-13_: we call `navigator.getUserMedia`. The parameters indicate that we want to capture the video and the audio from the current device (default Webcam). The call to `getUserMedia` returns an ES6 promise: the then(stream) method that follows.
+ _Line 14_: the `then(stream)` method is called in case of success and gets the current audio/video stream as parameter. This is passed by the browser to your JavaScript code. 
+ _Lines 15-19_: The line 16 sets the audio/video stream of the default Webcam to the `srcObject` attribute of the video element, while line 18 starts displaying it in the video player (there can be more than one Webcam, we'll see how to select one in particular next). Line 19 stores the stream in a global variable so that we can use it from another function (for stopping/starting the Webcam...)
+ _Lines 19-23_ define the `catch` method called in case of error (it could be that the Webcam cannot be accessed, or authorizations have not been granted).
+ _Lines 25-27_: a function for stopping the Webcam. We use the global variable `webcamStream` here, that has been initialized when we started using the Webcam in line 19. We have to stop separately the audio and the video streams.


#### Other examples that mix what we've seen in previous chapters, but this time with a live video stream

__Applying CSS effects on a video element with a live webcam__

Try this example that shows how to use the getUserMedia API. Note the CSS effects (click on the video to cycle from one effect to another). This works in Chrome/Firefox/Opera: see the [online version at JSBin](https://output.jsbin.com/jerayag). ([Local Example - Webcam w/ CSS](src/2.4.2-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y6xzkams')"
    src    ="https://tinyurl.com/yy2jzhuh"
    alt    ="css filter effects on live stream"
    title  ="css filter effects on live stream"
  />
</figure>



#### Taking a snapshot from the live Webcam stream

The trick is to copy and paste the current image from the video stream into a `<canvas>` element. Check out the [online version at JSBin](https://output.jsbin.com/debekod) (click on the "edit in JSBin" link on top left of the running Web app. to see the complete source code). ([Local Example - Webcam Snapshot](src/2.4.2-example3.html))

We will look at this example in greater detail in the next course section (related to the `<canvas>` element). For the time being, just play with the example. Also note that the source code extract visible in the following screenshot corresponds to an old version, so we recommend that you look at the complete source code in the JSBin running example.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y6xzkams')"
    src    ="https://tinyurl.com/y3claauz"
    alt    ="take screenshot of live video stream"
    title  ="take screenshot of live video stream"
  />
</figure>


#### Impressive demonstrations available on the Web

+ [WebCam pixelization! Fun!](https://codepen.io/dlueth/pen/zBhwv)
+ A MUST TRY: [Paul Neave's WebGL Camera Effects](http://neave.com/webcam/html5/)


### 2.4.3 Using the microphone

Instead of using the getUserMedia API with: `navigator.getUserMedia({video:true}, onSuccess, onError)`, it is also possible to use `{audio:true}` for the first parameter. In this case, only the microphone input will be captured. Notice that `{video:true, audio:true}` is also accepted, if you write a video conferencing system and need to capture both the audio and the video (this is often the case when writing WebRTC applications). The [WebRTC](https://www.w3.org/TR/webrtc/) is another W3C specification for P2P audio/video/data Real Time Communication.

Apart from videoconferencing, microphone input will be used for music Web apps, from the [WebAudio API](https://www.w3.org/TR/webaudio/). This API focuses on real time sound processing and music synthesis. This API is covered in the advanced W3Cx HTML5 course ([HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games)).

Do try some nice WebRTC applications like [Jitsi](https://jitsi.org/). Also check out the [WebAudio demonstrations](https://webaudiodemos.appspot.com/) written by Chris Wilson, esp. the one called "Input effects".

Below is an [example of real time audio processing of the microphone](https://webaudiodemos.appspot.com/input/index.html) input using getUserMedia and WebAudio APIs:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yxq32gur')"
    src    ="https://tinyurl.com/y56hekwa"
    alt    ="webaudio live processing"
    title  ="webaudio live processing"
  />
</figure>


### 2.4.4 Webcam resolution

It is possible to set "hints" for the preferred cam/resolution during video capture. This is done by using a ["constraint" object](https://tinyurl.com/y5teklb4) that is passed as a parameter to the `getUserMedia(...)` method. It's just the same object we passed in the basic example: `navigator.getUserMedia({video:true}, success, error)` except that this time this object is a little more complex.

For more information, this [article on MDN about the getUserMedia API](https://tinyurl.com/q8dses4) gives great examples on how to set the camera resolution and/or to choose the front or back camera when using a mobile phone.  

Typical use: check out this source code extract below, also [available online at JSBin](https://output.jsbin.com/howodaw). ([Local Example - Camera Resultion](src/2.4.4-example1.html))

<div><ol>
<li value="1">var vgaConstraints = {</li>
<li>&nbsp; &nbsp;<strong>video</strong><strong>: {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; width: { max: 640 },</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; height: { max: 360 }</strong></li>
<li><strong>&nbsp; &nbsp;}</strong></li>
<li>};</li>
<li>var hdConstraints = {</li>
<li>&nbsp; <strong>&nbsp;video</strong><strong>: {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; width: { min: 1280 },</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; height: { min: 720 }</strong></li>
<li><strong>&nbsp; &nbsp;}</strong></li>
<li>};</li>
<li>&nbsp;</li>
<li>let constraints = hdConstraints;</li>
<li>navigator.mediaDevices.getUserMedia(constraints)</li>
<li>.then((stream) =&gt; {...}</li>
</ol></div>


#### How to check which resolutions are supported by a browser?

Use this [Web app that systematically tests a set of "preferred resolutions"](https://webrtchacks.github.io/WebRTC-Camera-Resolution/) and compared them to the actual resolutions returned by the browser. Remember that the requested resolution is a hint, and there is no real guarantee that your configuration will allow it.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yya4venl')"
    src    ="https://tinyurl.com/y54hxx4a"
    alt    ="Webapp for checking supported resolutions"
    title  ="Webapp for checking supported resolutions"
  />
</figure>


#### Full example: choose between 3 different resolutions

[Online example at JSBin](https://output.jsbin.com/howodaw), with some browsers the QVGA resolution might not be supported. ([Local Example - Resolutions](src.2.4.4-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yya4venl')"
    src    ="https://tinyurl.com/y4mvemxb"
    alt    ="Set cam resolution, example shows three buttons, you click and it captures the video webcam stream in a different resolution each time"
    title  ="Set cam resolution, example shows three buttons, you click and it captures the video webcam stream in a different resolution each time"
  />
</figure>


HTML code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp; &nbsp; &lt;meta charset="utf-8"/&gt;</li>
<li>&nbsp; &nbsp; &lt;title&gt;getUserMedia constraints for choosing resolution&lt;/title&gt;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body onload="init();"&gt;</li>
<li>&nbsp; &nbsp; &lt;h1&gt;Set the camera resolution&lt;/h1&gt;</li>
<li>&nbsp; &nbsp; &nbsp; Example adapted from: </li>
<li>&nbsp; &nbsp; &lt;a href="https://www.simpl.info/getusermedia/constraints/"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; https://www.simpl.info/getusermedia/constraints/</li>
<li>&nbsp; &nbsp; &lt;/a&gt;</li>
<li>&nbsp; &lt;br&gt;</li>
<li>&nbsp; &lt;p&gt;Click a button to call &lt;code&gt;getUserMedia()&lt;/code&gt; with appropriate resolution.&lt;/p&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &lt;div id="buttons"&gt;</li>
<li>&nbsp; &nbsp; &lt;button id="qvga"&gt;QVGA&lt;/button&gt;</li>
<li>&nbsp; &nbsp; &lt;button id="vga"&gt;VGA&lt;/button&gt;</li>
<li>&nbsp; &nbsp; &lt;button id="hd"&gt;HD&lt;/button&gt;</li>
<li>&nbsp; &lt;/div&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &lt;p id="dimensions"&gt;&lt;/p&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &lt;video autoplay&gt;&lt;/video&gt;</li>
<li> </li>
<li>&nbsp;&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


JavaScript code:

<div><ol>
<li value="1">var vgaButton, qvgaButton, hdButton, dimensions, video, stream;</li>
<li>&nbsp;</li>
<li>function init() {</li>
<li>&nbsp; &nbsp; vgaButton = document.querySelector('button#vga');</li>
<li>&nbsp; &nbsp; qvgaButton = document.querySelector('button#qvga');</li>
<li>&nbsp; &nbsp; hdButton = document.querySelector('button#hd');</li>
<li>&nbsp; &nbsp; dimensions = document.querySelector('p#dimensions');</li>
<li>&nbsp; &nbsp; video = document.querySelector('video');</li>
<li> </li>
<li> </li>
<li>&nbsp; &nbsp; // Defines event listeners for the buttons that set the resolution</li>
<li>&nbsp; &nbsp; qvgaButton.onclick = function() {</li>
<li>&nbsp; &nbsp; getMedia(qvgaConstraints);</li>
<li> };</li>
<li> </li>
<li> vgaButton.onclick = function() {</li>
<li>&nbsp; &nbsp; getMedia(vgaConstraints);</li>
<li> };</li>
<li> </li>
<li> hdButton.onclick = function() {</li>
<li>&nbsp; &nbsp; getMedia(hdConstraints);</li>
<li> };</li>
<li>&nbsp;</li>
<li> // Trick: check regularly the size of the video element and display it.</li>
<li> // When getUserMedia is called the video element changes it sizes but for </li>
<li> // a while its size is zero pixels... or we check every half a second</li>
<li> video.addEventListener('play', function() {</li>
<li>&nbsp; &nbsp; setTimeout(function() {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayVideoDimensions();</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; }, 500);</li>
<li>&nbsp; &nbsp; });</li>
<li>}</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li><strong>// The different values for the constraints on resolution</strong></li>
<li><strong>var qvgaConstraints = {</strong></li>
<li><strong>&nbsp; &nbsp; video: {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; width: { max: 320 },</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; height: { max: 180 }</strong></li>
<li><strong>&nbsp; &nbsp; }</strong></li>
<li><strong>};</strong></li>
<li><strong>&nbsp;</strong></li>
<li><strong>var vgaConstraints = {</strong></li>
<li><strong>&nbsp; &nbsp; video: {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; width: { max: 640 },</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; height: { max: 360 }</strong></li>
<li><strong>&nbsp; &nbsp; }</strong></li>
<li><strong>};</strong></li>
<li><strong>&nbsp;</strong></li>
<li><strong>var hdConstraints = {</strong></li>
<li><strong>&nbsp; &nbsp; video: {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; width: { min: 1280 },</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; height: { min: 720 }</strong></li>
<li><strong>&nbsp; &nbsp; }</strong></li>
<li><strong>};</strong></li>
<li>&nbsp;</li>
<li>// The function that is called when a button has been clicked: it starts the video</li>
<li>// with the preferred resolution</li>
<li>function getMedia(constraints) {</li>
<li>&nbsp; &nbsp; if (!!stream) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; video.srcObject = null;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; stream.getTracks()[0].stop();</li>
<li>&nbsp; &nbsp; }</li>
<li> </li>
<li>navigator.mediaDevices.getUserMedia(constraints)</li>
<li> .then((stream) =&gt; {</li>
<li>&nbsp; &nbsp; video.srcObject = stream;</li>
<li>&nbsp; &nbsp; video.play();</li>
<li>&nbsp; &nbsp; window.stream = stream;</li>
<li> }).catch((error) =&gt;{</li>
<li>&nbsp; &nbsp; console.log('navigator.getUserMedia error: ', error);</li>
<li> });</li>
<li>&nbsp;</li>
<li>// utility function that is called by the setInterval(...) every 0.5s, for</li>
<li>// displaying the video dimensions</li>
<li>function displayVideoDimensions() {</li>
<li>&nbsp; &nbsp; dimensions.innerHTML = 'Actual video dimensions: ' + video.videoWidth +</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;'x' + video.videoHeight + 'px.';</li>
<li>}</li>
</ol></div>


#### Selecting the front or rear camera on smartphones

Here are some other constraints you can set. In particular, look at the ones for selecting the front or rear camera (smartphones):

<div><ol>
<li value="1"><strong>// more on video resolution</strong></li>
<li><strong>constraints = {</strong></li>
<li>&nbsp; &nbsp; video: {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; width: { min: 1024,<strong> ideal: 1280</strong>, max: 1920 },</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;height: { min: 776,<strong> ideal: 720</strong>, max: 1080 }</li>
<li>&nbsp; &nbsp; }</li>
<li>}<br><br></li>
<li><strong>// Framerate</strong></li>
<li><strong>constraints = { video: { frameRate: { ideal: 10, max: 15 } } };</strong></li>
<li>&nbsp;</li>
<li><strong>// front and back camera (mobile), some examples</strong></li>
<li><strong>var front = false;</strong></li>
<li></li>
<li>document.getElementById('flip-button').onclick = function() { <br>&nbsp; &nbsp; front = !front; <br>};</li>
<li><br><strong>// toggle front and back camera (mobile) by clicking a button</strong></li>
<li><strong>constraints = { video: { facingMode: (front? "user" : "environment") } };</strong></li>
<li>&nbsp;</li>
<li><strong>// prefer front camera</strong></li>
<li>constraints = { audio: true,<strong> video: { facingMode: "user" }</strong> }</li>
<li>&nbsp;</li>
<li><strong>// require rear camera</strong></li>
<li>constraints = { audio: true,<strong> video: { facingMode: { exact: "environment" } }</strong> }</li>
</ol></div>


#### Select input/output for audio and video streams

Resource: [WebRTC samples: Select sources & outputs](https://webrtc.github.io/samples/src/content/devices/input-output/)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yya4venl')"
    src    ="https://tinyurl.com/y2t3cufd"
    alt    ="webapp for selecting audio and video input/output"
    title  ="webapp for selecting audio and video input/output"
  />
</figure>


Source code extract:

<div><ol>
<li value="1">function gotDevices(deviceInfos) {</li>
<li>&nbsp; &nbsp; for (var i = 0; i !== deviceInfos.length; ++i) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; var deviceInfo = deviceInfos[i];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log("device with id: " + deviceInfo.deviceId);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // possible values: audioinput, audiooutput, videoinput</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log("device with kind: " + deviceInfo.kind);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // 'speaker' or 'camera' for example</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log("device with label: " + deviceInfo.label);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; //... should build a menu, test kind/label and set</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; // audioSource and videoSource variables</li>
<li>&nbsp; &nbsp; }</li>
<li>}</li>
<li>// ...</li>
<li>var constraints = {</li>
<li>&nbsp; &nbsp; audio: {<strong>deviceId: audioSource </strong>? {exact: audioSource} : undefined},</li>
<li>&nbsp; &nbsp; video: {<strong>deviceId: videoSource </strong>? {exact: videoSource} : undefined}</li>
<li>};</li>
<li></li>
<li>navigator.mediaDevices.getUserMedia(constraints).</li>
<li> then(gotStream).then(gotDevices).catch(handleError);</li>
</ol></div>


### 2.4.5 The MediaRecorder API

Let's start by playing with an example: record, replay and download the video stream captured using a Webcam. You can [try this example on JSBin](https://output.jsbin.com/cogozom). ([Local Example - Recording](src/2.4.5-example1.html))

Click "start recording", then press the play button on the video element on the right of the app. You can also click the "download" button to download a .webm file, playable offline with a media player such as [VLC](https://www.videolan.org/).

Screenshot that shows on the left the webcam video stream, and on the right the same stream recorded and playable in a HTML video element

#### Five steps are needed to use the mediaRecorder object

__1 - Create a mediaRecorder from a stream__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yykzd3po')"
    src    ="https://tinyurl.com/y4gznu76"
    alt    ="Source code extract:"
    title  ="Source code extract:"
  />
</figure>


<div><ol>
<li value="1">var options = {mimeType: 'video/webm; codecs=vp9'};</li>
<li>mediaRecorder = new MediaRecorder(stream, options);</li>
</ol></div>

... where streams is typically the object returned by the call to getUserMedia (see previous examples).


__2 - Add a "data handler" and call the `start()` method of the mediaRecorder object__

Source code extract:

<div><ol>
<li value="1">var recordedChunks = []; // will hold the recorded stream</li>
<li>mediaRecorder.ondataavailable = handleDataAvailable;</li>
<li>mediaRecorder.start();</li>
<li>&nbsp;</li>
<li>function handleDataAvailable(event) {</li>
<li>&nbsp; &nbsp;if (event.data.size &gt; 0) {</li>
<li>&nbsp; &nbsp; &nbsp; recordedChunks.push(event.data);</li>
<li>&nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp;// ...</li>
<li>}</li>
</ol></div>


Explanations:

+ _Line 1_: we declare an array of bytes that will hold the recorded stream.
+ _Line 2_: we declare the callback function that will be called while the stream is being captured. While the Webcam will be used, every xxx seconds, chunks of data will be passed to the `handleDataAvailable` function.
+ _Lines 5-10_: this function collects the chunk of data that corresponds to a few seconds of video, and stores it in the recordedChunks byte array.


__3 - When you've finished recording, tell the mediaRecorder to stop__

When you're done, you need to call the `stop()` method of the mediaRecorder object. This will end the periodic execution of the `handleDataAvailable` method, and stop the data capture.

<div><ol>
<li value="1">mediaRecorder.stop();</li>
</ol></div>


__4 - Create a blob (binary large object) with the collected data, and use it to set the `src` attribute of an HTML5 video player__

This piece of code creates a blob with the `recordedChunks` array. Use the `URL.createObjectURL(recordedChunks)` standard method to create another object that can be used as a value to set the `src` attribute of an HTML5 video element.

Like that, the recorded stream can be played using a standard HTML5 video element.

<div><ol>
<li value="1">function play() {</li>
<li>&nbsp; &nbsp;var superBuffer = new Blob(recordedChunks);</li>
<li>&nbsp; &nbsp;videoElement.src =</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window.URL.createObjectURL(superBuffer);</li>
<li>}</li>
</ol></div>


__5 - Download the captured stream__

A trick consists in creating, on the fly, an invisible link with a `download` attribute (see Week 1) and a `href` attribute  that points to the blob object containing the recorded stream encoded using a given codec, then generate programmatically a `click` event on the link. This will force the browser to download a file of type `video/webm` to the hard disk.

<div><ol>
<li value="1">function download() {</li>
<li>&nbsp; &nbsp; var blob = new Blob(recordedChunks, {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; type: 'video/webm'</li>
<li>&nbsp; &nbsp; });</li>
<li>&nbsp; &nbsp; var url = URL.createObjectURL(blob);</li>
<li>&nbsp; &nbsp; var a = document.createElement('a');</li>
<li>&nbsp; &nbsp; document.body.appendChild(a);</li>
<li>&nbsp; &nbsp; a.style = 'display: none';</li>
<li>&nbsp; &nbsp; a.href = url;</li>
<li>&nbsp; &nbsp; a.download = 'test.webm';</li>
<li>&nbsp; &nbsp; a.click();</li>
<li>&nbsp; &nbsp; window.URL.revokeObjectURL(url);</li>
<li>}</li>
</ol></div>


### 2.4.6 Discussion and project

Here is the discussion forum dedicated to this part of the course. You can post your comments and share your creations here, and of course ask questions.


#### Suggested topics

+ Do you know applications that use getUserMedia (webcam, mic)? If so, please share!
+ Are you concerned about privacy? Implementations are secure so far, but are you scared that there could be some security holes?
+ Do you plan to use getUserMedia for your Web sites and/or Web applications? Getting a screenshot directly in a form by activating the webcam is cool, but do you plan to use it (support is very good in all modern browsers, mobile or desktop)?


#### Optional project

Write a small PhotoBooth app for taking selfies, and optionally save them using the download attribute or some tricks for saving them to disk automatically.

+ Example written by Fjordcarver, a student who previously followed this MOOC course , available [on JSBin](https://output.jsbin.com/bucevej). It uses the HTML5 canvas element for the small thumbnails below the webcam video. We'll study this element in Week 3.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy6kpxpr')"
    src    ="https://courses.edx.org/assets/courseware/v1/97023394fa7d27a62f537045d932894b/asset-v1:W3Cx+HTML5.1x+2T2020+type@asset+block/photobooth.jpg"
    alt    ="a simple photobooth webapp"
    title  ="a simple photobooth webapp"
  />
</figure>



