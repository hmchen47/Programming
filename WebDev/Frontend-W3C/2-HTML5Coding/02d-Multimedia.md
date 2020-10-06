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
<li style="margin-bottom: 0px;" value="1"><span>&lt;video</span><span> </span><span>id</span><span>=</span><span>"myVideo"</span><span> </span><span>autoplay</span><span>&gt;</span><span>Fallback msg here.</span><span>&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;script&gt;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; if</span><span> </span><span>(</span><span>navigator</span><span>.</span><span>getUserMedia</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; // request video and audio stream from the user's webcam</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; navigator</span><span>.</span><span>mediaDevices</span><span>.</span><span>getUserMedia</span><span>({</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; audio</span><span>:</span><span> </span><span>true</span><span>,</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; video</span><span>:</span><span> </span><span>true</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; })</span>.<span style="background-color: #ffffff;">then</span><span style="background-color: #ffffff;">((</span><span style="background-color: #ffffff;">stream</span><span style="background-color: #ffffff;">)</span><span style="background-color: #ffffff;"> </span><span style="background-color: #ffffff;">=&gt;</span><span style="background-color: #ffffff;"> </span><span style="background-color: #ffffff;">{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; var</span><span> video </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'#myVideo'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; video</span><span>.</span><span>srcObject </span><span>=</span><span> stream</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; video</span><span>.</span><span>play</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; }).</span><span>catch</span><span>((</span><span>error</span><span>)</span><span> </span><span>=&gt;</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; console</span><span>.</span><span>log</span><span>(</span><span>'navigator.getUserMedia error: '</span><span>,</span><span> error</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; });</span><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/script&gt;</span></li>
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
<li style="margin-bottom: 0px;" value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>&lt;title&gt;</span><span>Webcam start/stop</span><span>&lt;/title&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>&lt;script&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; let webcamStream</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; function</span><span> startWebcam</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; // request video and audio stream from the user's webcam</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; navigator</span><span>.</span><span>mediaDevices</span><span>.</span><span>getUserMedia</span><span>({</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; audio</span><span>:</span><span> </span><span>true</span><span>,</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; video</span><span>:</span><span> </span><span>true</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; })</span>.<span style="background-color: #ffffff;">then</span><span style="background-color: #ffffff;">((</span><span style="background-color: #ffffff;">stream</span><span style="background-color: #ffffff;">)</span><span style="background-color: #ffffff;"> </span><span style="background-color: #ffffff;">=&gt;</span><span style="background-color: #ffffff;"> </span><span style="background-color: #ffffff;">{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; let video </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'#video'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; video</span><span>.</span><span>srcObject </span><span>=</span><span> stream</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; video</span><span>.</span><span>play</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; webcamStream </span><span>=</span><span> stream</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; }).catch((error) =&gt; {</span></li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; console.log('navigator.getUserMedia error: ', error);</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; });</li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; function</span><span> stopWebcam</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; webcamStream</span><span>.</span><span>getTracks</span><span>()[</span><span>0</span><span>].</span><span>stop</span><span>();</span><span> </span><span>// audio</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; webcamStream</span><span>.</span><span>getTracks</span><span>()[</span><span>1</span><span>].</span><span>stop</span><span>();</span><span> </span><span>// video</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; }</span><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>&lt;/script&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;body</span><span> </span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &lt;video</span><span> </span><span>width</span><span>=</span><span>400</span><span> </span><span>height</span><span>=</span><span>400</span><span> </span><span>id</span><span>=</span><span>"video"</span><span> </span><span>controls</span><span>&gt;&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &lt;p&gt;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>startWebcam</span><span>();</span><span>"</span><span>&gt;</span><span>Start WebCam</span><span>&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>stopWebcam</span><span>();</span><span>"</span><span>&gt;</span><span>Stop WebCam</span><span>&lt;/button&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/html&gt;</span></li>
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
<li style="margin-bottom: 0px;" value="1"><span>var</span><span> vgaConstraints </span><span>=</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;<strong>video</strong></span><strong><span>:</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; width</span><span>:</span><span> </span><span>{</span><span> max</span><span>:</span><span> </span><span>640</span><span> </span><span>},</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; height</span><span>:</span><span> </span><span>{</span><span> max</span><span>:</span><span> </span><span>360</span><span> </span><span>}</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span></span><span>&nbsp; &nbsp;}</span></strong></li>
<li style="margin-bottom: 0px;"><span>};</span></li>
<li style="margin-bottom: 0px;"><span>var</span><span> hdConstraints </span><span>=</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; <strong>&nbsp;video</strong></span><strong><span>:</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; width</span><span>:</span><span> </span><span>{</span><span> min</span><span>:</span><span> </span><span>1280</span><span> </span><span>},</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; height</span><span>:</span><span> </span><span>{</span><span> min</span><span>:</span><span> </span><span>720</span><span> </span><span>}</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span></span><span>&nbsp; &nbsp;}</span></strong></li>
<li style="margin-bottom: 0px;"><span>};</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>let</span><span> constraints </span><span>=</span><span> hdConstraints</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>navigator</span><span>.</span><span>mediaDevices</span><span>.</span><span>getUserMedia</span><span>(</span><span>constraints</span><span>)</span></li>
<li style="margin-bottom: 0px;"><span>.</span><span>then</span><span>((</span><span>stream</span><span>)</span><span> </span><span>=&gt;</span><span> </span><span>{...}</span></li>
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
<li style="margin-bottom: 0px;" value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span>&lt;title&gt;</span><span>getUserMedia constraints for choosing resolution</span><span>&lt;/title&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span>&lt;body</span><span> </span><span>onload</span><span>=</span><span>"</span><span>init</span><span>();</span><span>"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;h1&gt;</span><span>Set the camera resolution</span><span>&lt;/h1&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span>Example adapted from: </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://www.simpl.info/getusermedia/constraints/"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span>https://www.simpl.info/getusermedia/constraints/</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;/a&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;br&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;p&gt;</span><span>Click a button to call </span><span>&lt;code&gt;</span><span>getUserMedia()</span><span>&lt;/code&gt;</span><span> with appropriate resolution.</span><span>&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;div</span><span> </span><span>id</span><span>=</span><span>"buttons"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;button</span><span> </span><span>id</span><span>=</span><span>"qvga"</span><span>&gt;</span><span>QVGA</span><span>&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;button</span><span> </span><span>id</span><span>=</span><span>"vga"</span><span>&gt;</span><span>VGA</span><span>&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;button</span><span> </span><span>id</span><span>=</span><span>"hd"</span><span>&gt;</span><span>HD</span><span>&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;/div&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;p</span><span> </span><span>id</span><span>=</span><span>"dimensions"</span><span>&gt;&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;video</span><span> </span><span>autoplay</span><span>&gt;&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span><span>&lt;/body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/html&gt;</span></li>
</ol></div>


JavaScript code:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>var vgaButton</span><span>,</span><span> qvgaButton</span><span>,</span><span> hdButton</span><span>,</span><span> dimensions</span><span>,</span><span> video</span><span>,</span><span> stream</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>function</span><span> init</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; vgaButton </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'button#vga'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; qvgaButton </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'button#qvga'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; hdButton </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'button#hd'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; dimensions </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'p#dimensions'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; video </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'video'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; // Defines event listeners for the buttons that set the resolution</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; qvgaButton</span><span>.</span><span>onclick </span><span>=</span><span> </span><span>function</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; getMedia</span><span>(</span><span>qvgaConstraints</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>};</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> vgaButton</span><span>.</span><span>onclick </span><span>=</span><span> </span><span>function</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; getMedia</span><span>(</span><span>vgaConstraints</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>};</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> hdButton</span><span>.</span><span>onclick </span><span>=</span><span> </span><span>function</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; getMedia</span><span>(</span><span>hdConstraints</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>};</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// Trick: check regularly the size of the video element and display it.</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// When getUserMedia is called the video element changes it sizes but for </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// a while its size is zero pixels... or we check every half a second</span></li>
<li style="margin-bottom: 0px;"><span> video</span><span>.</span><span>addEventListener</span><span>(</span><span>'play'</span><span>,</span><span> </span><span>function</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; setTimeout</span><span>(</span><span>function</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayVideoDimensions</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; &nbsp; },</span><span> </span><span>500</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; });</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><strong><span>// The different values for the constraints on resolution</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>var</span><span> qvgaConstraints </span><span>=</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; video</span><span>:</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; width</span><span>:</span><span> </span><span>{</span><span> max</span><span>:</span><span> </span><span>320</span><span> </span><span>},</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; height</span><span>:</span><span> </span><span>{</span><span> max</span><span>:</span><span> </span><span>180</span><span> </span><span>}</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span></span><span>&nbsp; &nbsp; }</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>};</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp;</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>var</span><span> vgaConstraints </span><span>=</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; video</span><span>:</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; width</span><span>:</span><span> </span><span>{</span><span> max</span><span>:</span><span> </span><span>640</span><span> </span><span>},</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; height</span><span>:</span><span> </span><span>{</span><span> max</span><span>:</span><span> </span><span>360</span><span> </span><span>}</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span></span><span>&nbsp; &nbsp; }</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>};</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp;</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>var</span><span> hdConstraints </span><span>=</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; video</span><span>:</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; width</span><span>:</span><span> </span><span>{</span><span> min</span><span>:</span><span> </span><span>1280</span><span> </span><span>},</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>&nbsp; &nbsp; &nbsp; &nbsp; height</span><span>:</span><span> </span><span>{</span><span> min</span><span>:</span><span> </span><span>720</span><span> </span><span>}</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span></span><span>&nbsp; &nbsp; }</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>};</span></strong></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>// The function that is called when a button has been clicked: it starts the video</span></li>
<li style="margin-bottom: 0px;"><span>// with the preferred resolution</span></li>
<li style="margin-bottom: 0px;"><span>function</span><span> getMedia</span><span>(</span><span>constraints</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; if</span><span> </span><span>(!!</span><span>stream</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; video</span><span>.</span><span>srcObject </span><span>=</span><span> </span><span>null</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; stream</span><span>.</span><span>getTracks</span><span>()[</span><span>0</span><span>].</span><span>stop</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>navigator</span><span>.</span><span>mediaDevices</span><span>.</span><span>getUserMedia</span><span>(</span><span>constraints</span><span>)</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>.</span><span>then</span><span>((</span><span>stream</span><span>)</span><span> </span><span>=&gt;</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; video</span><span>.</span><span>srcObject </span><span>=</span><span> stream</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; video</span><span>.</span><span>play</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; window</span><span>.</span><span>stream </span><span>=</span><span> stream</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>})</span>.<span>catch</span><span>((</span><span>error</span><span>)</span><span> </span><span>=&gt;{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; console</span><span>.</span><span>log</span><span>(</span><span>'navigator.getUserMedia error: '</span><span>,</span><span> error</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>});</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>// utility function that is called by the setInterval(...) every 0.5s, for</span></li>
<li style="margin-bottom: 0px;"><span>// displaying the video dimensions</span></li>
<li style="margin-bottom: 0px;"><span>function</span><span> displayVideoDimensions</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; dimensions</span><span>.</span><span>innerHTML </span><span>=</span><span> </span><span>'Actual video dimensions: '</span><span> </span><span>+</span><span> video</span><span>.</span><span>videoWidth </span><span>+</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;'x'</span><span> </span><span>+</span><span> video</span><span>.</span><span>videoHeight </span><span>+</span><span> </span><span>'px.'</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
</ol></div>


#### Selecting the front or rear camera on smartphones

Here are some other constraints you can set. In particular, look at the ones for selecting the front or rear camera (smartphones):

<div><ol>
<li style="margin-bottom: 0px;" value="1"><strong><span>// more on video resolution</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>constraints </span><span>=</span><span> </span><span>{</span></strong></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; video</span><span>:</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; width</span><span>:</span><span> </span><span>{</span><span> min</span><span>:</span><span> </span><span>1024</span><span>,</span><strong><span> ideal</span><span>:</span><span> </span><span>1280</span></strong><span>,</span><span> max</span><span>:</span><span> </span><span>1920</span><span> </span><span>},</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;height</span><span>:</span><span> </span><span>{</span><span> min</span><span>:</span><span> </span><span>776</span><span>,</span><strong><span> ideal</span><span>:</span><span> </span><span>720</span></strong><span>,</span><span> max</span><span>:</span><span> </span><span>1080</span><span> </span><span>}</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span>}<br><br></span></li>
<li style="margin-bottom: 0px;"><strong><span>// Framerate</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>constraints </span><span>=</span><span> </span><span>{</span><span> video</span><span>:</span><span> </span><span>{</span><span> frameRate</span><span>:</span><span> </span><span>{</span><span> ideal</span><span>:</span><span> </span><span>10</span><span>,</span><span> max</span><span>:</span><span> </span><span>15</span><span> </span><span>}</span><span> </span><span>}</span><span> </span><span>};</span></strong></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><strong><span>// front and back camera (mobile), some examples</span></strong></li>
<li style="margin-bottom: 0px;"><strong><span>var</span><span> front </span><span>=</span><span> </span><span>false</span><span>;</span></strong></li>
<li style="margin-bottom: 0px;"><span></span></li>
<li style="margin-bottom: 0px;"><span>document</span><span>.</span><span>getElementById</span><span>(</span><span>'flip-button'</span><span>).</span><span>onclick </span><span>=</span><span> </span><span>function</span><span>()</span><span> </span><span>{</span><span> <br>&nbsp; &nbsp; front </span><span>=</span><span> </span><span>!</span><span>front</span><span>;</span><span> <br></span><span>};</span></li>
<li style="margin-bottom: 0px;"><span><br><strong>// toggle front and back camera (mobile) by clicking a button</strong></span></li>
<li style="margin-bottom: 0px;"><strong><span>constraints </span><span>=</span><span> </span><span>{</span><span> video</span><span>:</span><span> </span><span>{</span><span> facingMode</span><span>:</span><span> </span><span>(</span><span>front</span><span>?</span><span> </span><span>"user"</span><span> </span><span>:</span><span> </span><span>"environment"</span><span>)</span><span> </span><span>}</span><span> </span><span>};</span></strong></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><strong><span>// prefer front camera</span></strong></li>
<li style="margin-bottom: 0px;"><span>constraints </span><span>=</span><span> </span><span>{</span><span> audio</span><span>:</span><span> </span><span>true</span><span>,</span><strong><span> video</span><span>:</span><span> </span><span>{</span><span> facingMode</span><span>:</span><span> </span><span>"user"</span><span> </span><span>}</span></strong><span> </span><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><strong><span>// require rear camera</span></strong></li>
<li style="margin-bottom: 0px;"><span>constraints </span><span>=</span><span> </span><span>{</span><span> audio</span><span>:</span><span> </span><span>true</span><span>,</span><strong><span> video</span><span>:</span><span> </span><span>{</span><span> facingMode</span><span>:</span><span> </span><span>{</span><span> exact</span><span>:</span><span> </span><span>"environment"</span><span> </span><span>}</span><span> </span><span>}</span></strong><span> </span><span>}</span></li>
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
<li style="margin-bottom: 0px;" value="1"><span>function</span><span> gotDevices</span><span>(</span><span>deviceInfos</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; for</span><span> </span><span>(</span><span>var</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>!==</span><span> deviceInfos</span><span>.</span><span>length</span><span>;</span><span> </span><span>++</span><span>i</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; &nbsp; var</span><span> deviceInfo </span><span>=</span><span> deviceInfos</span><span>[</span><span>i</span><span>];</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; console</span><span>.</span><span>log</span><span>(</span><span>"device with id: "</span><span> </span><span>+</span><span> deviceInfo</span><span>.</span><span>deviceId</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; &nbsp; // possible values: audioinput, audiooutput, videoinput</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; console</span><span>.</span><span>log</span><span>(</span><span>"device with kind: "</span><span> </span><span>+</span><span> deviceInfo</span><span>.</span><span>kind</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; &nbsp; // 'speaker' or 'camera' for example</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; console</span><span>.</span><span>log</span><span>(</span><span>"device with label: "</span><span> </span><span>+</span><span> deviceInfo</span><span>.</span><span>label</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; &nbsp; //... should build a menu, test kind/label and set</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; &nbsp; &nbsp; // audioSource and videoSource variables</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>// ...</span></li>
<li style="margin-bottom: 0px;"><span>var</span><span> constraints </span><span>=</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; audio</span><span>:</span><span> </span><span>{</span><strong><span>deviceId</span><span>:</span><span> audioSource </span></strong><span>?</span><span> </span><span>{</span><span>exact</span><span>:</span><span> audioSource</span><span>}</span><span> </span><span>:</span><span> </span><span>undefined</span><span>},</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; video</span><span>:</span><span> </span><span>{</span><strong><span>deviceId</span><span>:</span><span> videoSource </span></strong><span>?</span><span> </span><span>{</span><span>exact</span><span>:</span><span> videoSource</span><span>}</span><span> </span><span>:</span><span> </span><span>undefined</span><span>}</span></li>
<li style="margin-bottom: 0px;"><span>};</span></li>
<li style="margin-bottom: 0px;"><span></span></li>
<li style="margin-bottom: 0px;"><span>navigator</span><span>.</span><span>mediaDevices</span><span>.</span><span>getUserMedia</span><span>(</span><span>constraints</span><span>).</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>then</span><span>(</span><span>gotStream</span><span>).</span><span>then</span><span>(</span><span>gotDevices</span><span>).</span><span>catch</span><span>(</span><span>handleError</span><span>);</span></li>
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
<li style="margin-bottom: 0px;" value="1"><span>var</span><span> options </span><span>=</span><span> </span><span>{</span><span>mimeType</span><span>:</span><span> </span><span>'video/webm; codecs=vp9'</span><span>};</span></li>
<li style="margin-bottom: 0px;"><span>mediaRecorder </span><span>=</span><span> </span><span>new</span><span> </span><span>MediaRecorder</span><span>(</span><span>stream</span><span>,</span><span> options</span><span>);</span></li>
</ol></div>

... where streams is typically the object returned by the call to getUserMedia (see previous examples).


__2 - Add a "data handler" and call the `start()` method of the mediaRecorder object__

Source code extract:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>var</span><span> recordedChunks </span><span>=</span><span> </span><span>[];</span><span> </span><span>// will hold the recorded stream</span></li>
<li style="margin-bottom: 0px;"><span>mediaRecorder</span><span>.</span><span>ondataavailable </span><span>=</span><span> handleDataAvailable</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>mediaRecorder</span><span>.</span><span>start</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>function</span><span> handleDataAvailable</span><span>(</span><span>event</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp;if</span><span> </span><span>(</span><span>event</span><span>.</span><span>data</span><span>.</span><span>size </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; recordedChunks</span><span>.</span><span>push</span><span>(</span><span>event</span><span>.</span><span>data</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp;}</span><span> </span><span>else</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp;// ...</span></li>
<li style="margin-bottom: 0px;"><span></span><span>}</span></li>
</ol></div>


Explanations:

+ _Line 1_: we declare an array of bytes that will hold the recorded stream.
+ _Line 2_: we declare the callback function that will be called while the stream is being captured. While the Webcam will be used, every xxx seconds, chunks of data will be passed to the `handleDataAvailable` function.
+ _Lines 5-10_: this function collects the chunk of data that corresponds to a few seconds of video, and stores it in the recordedChunks byte array.


__3 - When you've finished recording, tell the mediaRecorder to stop__

When you're done, you need to call the `stop()` method of the mediaRecorder object. This will end the periodic execution of the `handleDataAvailable` method, and stop the data capture.

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>mediaRecorder</span><span>.</span><span>stop</span><span>();</span></li>
</ol></div>


__4 - Create a blob (binary large object) with the collected data, and use it to set the `src` attribute of an HTML5 video player__

This piece of code creates a blob with the `recordedChunks` array. Use the `URL.createObjectURL(recordedChunks)` standard method to create another object that can be used as a value to set the `src` attribute of an HTML5 video element.

Like that, the recorded stream can be played using a standard HTML5 video element.

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>function</span><span> play</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp;var</span><span> superBuffer </span><span>=</span><span> </span><span>new</span><span> </span><span>Blob</span><span>(</span><span>recordedChunks</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;videoElement</span><span>.</span><span>src </span><span>=</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window</span><span>.</span><span>URL</span><span>.</span><span>createObjectURL</span><span>(</span><span>superBuffer</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
</ol></div>


__5 - Download the captured stream__

A trick consists in creating, on the fly, an invisible link with a `download` attribute (see Week 1) and a `href` attribute  that points to the blob object containing the recorded stream encoded using a given codec, then generate programmatically a `click` event on the link. This will force the browser to download a file of type `video/webm` to the hard disk.

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>function</span><span> download</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; var</span><span> blob </span><span>=</span><span> </span><span>new</span><span> </span><span>Blob</span><span>(</span><span>recordedChunks</span><span>,</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; type</span><span>:</span><span> </span><span>'video/webm'</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; });</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; var</span><span> url </span><span>=</span><span> URL</span><span>.</span><span>createObjectURL</span><span>(</span><span>blob</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span><span>&nbsp; &nbsp; var</span><span> a </span><span>=</span><span> document</span><span>.</span><span>createElement</span><span>(</span><span>'a'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; document</span><span>.</span><span>body</span><span>.</span><span>appendChild</span><span>(</span><span>a</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; a</span><span>.</span><span>style </span><span>=</span><span> </span><span>'display: none'</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; a</span><span>.</span><span>href </span><span>=</span><span> url</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; a</span><span>.</span><span>download </span><span>=</span><span> </span><span>'test.webm'</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; a</span><span>.</span><span>click</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; window</span><span>.</span><span>URL</span><span>.</span><span>revokeObjectURL</span><span>(</span><span>url</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
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



