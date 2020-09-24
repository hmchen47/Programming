# Week 2: HTML5 Multimedia

## 2.4 Webcam, microphone: the getUserMedia API


### 2.4.0 Lecture Notes

+ [The `getUserMedia` API - Webcam access](#241-webcam)
  + useful for controlling a Webcam video stream
  + one component of the WebRTC specification
  + not considered a "real" part of the HTML5 specification
  + dealing with video streams: always used in conjunction with the `<video>` element
  + specification: https://www.w3.org/TR/mediacapture-streams/
  + Webcam usage
    + set the `srcObject` attribute of a `<video>` element to the live video stream object coming out of the Webcam
    + `navigator.getUserMedia(params)` method: get this stream
    + returns an ES6 promise (ES stands for ECMAScript and the scripting language that forms the basis of JavaScript)
  + mandatory to access the page that contains the JavaScript code through `https://`

+ [The `getUserMedia` API - start/stop the Webcam](#242-more-on-getusermedia)
  + `navigator.mediaDevices.getUserMedia({audio: true, video: true})`: 
    + parameters to capture the video and the audio from the current device (default Webcam)
    + return an ES6 promise
  + `then(stream)` method: get the current audio/video stream as parameter if success
  + `video.srcObject = stream;`: set the audio/video stream of the default Webcam to the `srcObject` attribute of the video element
  + `video.play();`: displaying stream in the video player
  + `webcamStream = stream;`: store the stream in a global variable
  + `catch((error)`: catch error event
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
  + [example](#full-example-choose-between-3-different-resolutions)
  + [rear and front camera in smartphone](#selecting-the-front-or-rear-camera-on-smartphones)




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

The main idea is to set the `srcObject` attribute of a `<video>` element to the live video stream object coming out of the Webcam. To get this stream, you'll have to call the `navigator.getUserMedia(params)` method from the getUserMedia API, that returns an [ES6 promise](https://developers.google.com/web/fundamentals/primers/promises) (ES stands for ECMAScript and is the scripting language that forms the basis of JavaScript). Do not panic if you do not know ES6's promises! The syntax is very simple, and you'll learn what you need from the provided examples.

The stream is passed as a parameter to the `then()` method returned by the promise, as in this typical example ([you can try it at JSBin](https://output.jsbin.com/gakikop) - press the "edit in JSBin" button to see the source code) ([Local Example - Webcam](src/2.4.1-example1.html)):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">autoplay</span><span class="tag">&gt;</span><span class="pln">Fallback msg here.</span><span class="tag">&lt;/video&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">navigator</span><span class="pun">.</span><span class="pln">getUserMedia</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // request video and audio stream from the user's webcam</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; navigator</span><span class="pun">.</span><span class="pln">mediaDevices</span><span class="pun">.</span><span class="pln">getUserMedia</span><span class="pun">({</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; audio</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; video</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; })</span>.<span class="pln" style="background-color: #ffffff;">then</span><span class="pun" style="background-color: #ffffff;">((</span><span class="pln" style="background-color: #ffffff;">stream</span><span class="pun" style="background-color: #ffffff;">)</span><span class="pln" style="background-color: #ffffff;"> </span><span class="pun" style="background-color: #ffffff;">=&gt;</span><span class="pln" style="background-color: #ffffff;"> </span><span class="pun" style="background-color: #ffffff;">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; var</span><span class="pln"> video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#myVideo'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">srcObject </span><span class="pun">=</span><span class="pln"> stream</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }).</span><span class="kwd">catch</span><span class="pun">((</span><span class="pln">error</span><span class="pun">)</span><span class="pln"> </span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'navigator.getUserMedia error: '</span><span class="pun">,</span><span class="pln"> error</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Webcam start/stop</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; let webcamStream</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; function</span><span class="pln"> startWebcam</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // request video and audio stream from the user's webcam</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; navigator</span><span class="pun">.</span><span class="pln">mediaDevices</span><span class="pun">.</span><span class="pln">getUserMedia</span><span class="pun">({</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; audio</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; video</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; })</span>.<span class="pln" style="background-color: #ffffff;">then</span><span class="pun" style="background-color: #ffffff;">((</span><span class="pln" style="background-color: #ffffff;">stream</span><span class="pun" style="background-color: #ffffff;">)</span><span class="pln" style="background-color: #ffffff;"> </span><span class="pun" style="background-color: #ffffff;">=&gt;</span><span class="pln" style="background-color: #ffffff;"> </span><span class="pun" style="background-color: #ffffff;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; let video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#video'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">srcObject </span><span class="pun">=</span><span class="pln"> stream</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; webcamStream </span><span class="pun">=</span><span class="pln"> stream</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }).catch((error) =&gt; {</span></li>
<li class="L0" style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; console.log('navigator.getUserMedia error: ', error);</li>
<li class="L0" style="margin-bottom: 0px;">&nbsp; &nbsp; });</li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; }</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; function</span><span class="pln"> stopWebcam</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; webcamStream</span><span class="pun">.</span><span class="pln">getTracks</span><span class="pun">()[</span><span class="lit">0</span><span class="pun">].</span><span class="pln">stop</span><span class="pun">();</span><span class="pln"> </span><span class="com">// audio</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; webcamStream</span><span class="pun">.</span><span class="pln">getTracks</span><span class="pun">()[</span><span class="lit">1</span><span class="pun">].</span><span class="pln">stop</span><span class="pun">();</span><span class="pln"> </span><span class="com">// video</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; }</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;video</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">400</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">400</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"video"</span><span class="pln"> </span><span class="atn">controls</span><span class="tag">&gt;&lt;/video&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">startWebcam</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Start WebCam</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">stopWebcam</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Stop WebCam</span><span class="tag">&lt;/button&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &lt;/p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> vgaConstraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>video</strong></span><strong><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">640</span><span class="pln"> </span><span class="pun">},</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">360</span><span class="pln"> </span><span class="pun">}</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp;}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> hdConstraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;video</strong></span><strong><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> min</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1280</span><span class="pln"> </span><span class="pun">},</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> min</span><span class="pun">:</span><span class="pln"> </span><span class="lit">720</span><span class="pln"> </span><span class="pun">}</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp;}</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> constraints </span><span class="pun">=</span><span class="pln"> hdConstraints</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">navigator</span><span class="pun">.</span><span class="pln">mediaDevices</span><span class="pun">.</span><span class="pln">getUserMedia</span><span class="pun">(</span><span class="pln">constraints</span><span class="pun">)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">.</span><span class="kwd">then</span><span class="pun">((</span><span class="pln">stream</span><span class="pun">)</span><span class="pln"> </span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{...}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"><span class="tag">&nbsp; </span></span><span class="tag"><span class="tag"><span class="tag">&nbsp; </span></span>&lt;title&gt;</span><span class="pln">getUserMedia constraints for choosing resolution</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"><span class="tag">&nbsp; </span>&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag"><span class="tag">&nbsp; </span>&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;h1&gt;</span><span class="pln">Set the camera resolution</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp; </span></span></span>Example adapted from: </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://www.simpl.info/getusermedia/constraints/"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp; </span></span></span>https://www.simpl.info/getusermedia/constraints/</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;/a&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;br&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;p&gt;</span><span class="pln">Click a button to call </span><span class="tag">&lt;code&gt;</span><span class="pln">getUserMedia()</span><span class="tag">&lt;/code&gt;</span><span class="pln"> with appropriate resolution.</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttons"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"qvga"</span><span class="tag">&gt;</span><span class="pln">QVGA</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"vga"</span><span class="tag">&gt;</span><span class="pln">VGA</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"hd"</span><span class="tag">&gt;</span><span class="pln">HD</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;/div&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;p</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"dimensions"</span><span class="tag">&gt;&lt;/p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">autoplay</span><span class="tag">&gt;&lt;/video&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp;</span><span class="tag">&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">var vgaButton</span><span class="pun">,</span><span class="pln"> qvgaButton</span><span class="pun">,</span><span class="pln"> hdButton</span><span class="pun">,</span><span class="pln"> dimensions</span><span class="pun">,</span><span class="pln"> video</span><span class="pun">,</span><span class="pln"> stream</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; vgaButton </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'button#vga'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; qvgaButton </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'button#qvga'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; hdButton </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'button#hd'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; dimensions </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'p#dimensions'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; // Defines event listeners for the buttons that set the resolution</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; qvgaButton</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; getMedia</span><span class="pun">(</span><span class="pln">qvgaConstraints</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> vgaButton</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; getMedia</span><span class="pun">(</span><span class="pln">vgaConstraints</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> hdButton</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; getMedia</span><span class="pun">(</span><span class="pln">hdConstraints</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// Trick: check regularly the size of the video element and display it.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// When getUserMedia is called the video element changes it sizes but for </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// a while its size is zero pixels... or we check every half a second</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> video</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'play'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; setTimeout</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayVideoDimensions</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; },</span><span class="pln"> </span><span class="lit">500</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="com">// The different values for the constraints on resolution</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> qvgaConstraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">320</span><span class="pln"> </span><span class="pun">},</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">180</span><span class="pln"> </span><span class="pun">}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pun">};</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> vgaConstraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">640</span><span class="pln"> </span><span class="pun">},</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">360</span><span class="pln"> </span><span class="pun">}</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pun">};</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> hdConstraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> min</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1280</span><span class="pln"> </span><span class="pun">},</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> min</span><span class="pun">:</span><span class="pln"> </span><span class="lit">720</span><span class="pln"> </span><span class="pun">}</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">};</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// The function that is called when a button has been clicked: it starts the video</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// with the preferred resolution</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getMedia</span><span class="pun">(</span><span class="pln">constraints</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pln"> </span><span class="pun">(!!</span><span class="pln">stream</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">srcObject </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; stream</span><span class="pun">.</span><span class="pln">getTracks</span><span class="pun">()[</span><span class="lit">0</span><span class="pun">].</span><span class="pln">stop</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">navigator</span><span class="pun">.</span><span class="pln">mediaDevices</span><span class="pun">.</span><span class="pln">getUserMedia</span><span class="pun">(</span><span class="pln">constraints</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">.</span><span class="kwd">then</span><span class="pun">((</span><span class="pln">stream</span><span class="pun">)</span><span class="pln"> </span><span class="pun">=&gt;</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">srcObject </span><span class="pun">=</span><span class="pln"> stream</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; window</span><span class="pun">.</span><span class="pln">stream </span><span class="pun">=</span><span class="pln"> stream</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">})</span>.<span class="kwd">catch</span><span class="pun">((</span><span class="pln">error</span><span class="pun">)</span><span class="pln"> </span><span class="pun">=&gt;{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'navigator.getUserMedia error: '</span><span class="pun">,</span><span class="pln"> error</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">});</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// utility function that is called by the setInterval(...) every 0.5s, for</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// displaying the video dimensions</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayVideoDimensions</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; dimensions</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Actual video dimensions: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">videoWidth </span><span class="pun">+</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;'x'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">videoHeight </span><span class="pun">+</span><span class="pln"> </span><span class="str">'px.'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Selecting the front or rear camera on smartphones

Here are some other constraints you can set. In particular, look at the ones for selecting the front or rear camera (smartphones):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="com">// more on video resolution</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">constraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> min</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1024</span><span class="pun">,</span><strong><span class="pln"> ideal</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1280</span></strong><span class="pun">,</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1920</span><span class="pln"> </span><span class="pun">},</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;height</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> min</span><span class="pun">:</span><span class="pln"> </span><span class="lit">776</span><span class="pun">,</span><strong><span class="pln"> ideal</span><span class="pun">:</span><span class="pln"> </span><span class="lit">720</span></strong><span class="pun">,</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1080</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}<br><br></span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="com">// Framerate</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">constraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> frameRate</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> ideal</span><span class="pun">:</span><span class="pln"> </span><span class="lit">10</span><span class="pun">,</span><span class="pln"> max</span><span class="pun">:</span><span class="pln"> </span><span class="lit">15</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="pun">};</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="com">// front and back camera (mobile), some examples</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> front </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'flip-button'</span><span class="pun">).</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> <br>&nbsp; &nbsp; front </span><span class="pun">=</span><span class="pln"> </span><span class="pun">!</span><span class="pln">front</span><span class="pun">;</span><span class="pln"> <br></span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com"><br class="Apple-interchange-newline"><strong>// toggle front and back camera (mobile) by clicking a button</strong></span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">constraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> facingMode</span><span class="pun">:</span><span class="pln"> </span><span class="pun">(</span><span class="pln">front</span><span class="pun">?</span><span class="pln"> </span><span class="str">"user"</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> </span><span class="str">"environment"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="pun">};</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="com">// prefer front camera</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">constraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> audio</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><strong><span class="pln"> video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> facingMode</span><span class="pun">:</span><span class="pln"> </span><span class="str">"user"</span><span class="pln"> </span><span class="pun">}</span></strong><span class="pln"> </span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="com">// require rear camera</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">constraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> audio</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span><strong><span class="pln"> video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> facingMode</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> exact</span><span class="pun">:</span><span class="pln"> </span><span class="str">"environment"</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="pun">}</span></strong><span class="pln"> </span><span class="pun">}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> gotDevices</span><span class="pun">(</span><span class="pln">deviceInfos</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">!==</span><span class="pln"> deviceInfos</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> </span><span class="pun">++</span><span class="pln">i</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; var</span><span class="pln"> deviceInfo </span><span class="pun">=</span><span class="pln"> deviceInfos</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"device with id: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> deviceInfo</span><span class="pun">.</span><span class="pln">deviceId</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // possible values: audioinput, audiooutput, videoinput</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"device with kind: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> deviceInfo</span><span class="pun">.</span><span class="pln">kind</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // 'speaker' or 'camera' for example</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"device with label: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> deviceInfo</span><span class="pun">.</span><span class="pln">label</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; //... should build a menu, test kind/label and set</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // audioSource and videoSource variables</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// ...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> constraints </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; audio</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><strong><span class="pln">deviceId</span><span class="pun">:</span><span class="pln"> audioSource </span></strong><span class="pun">?</span><span class="pln"> </span><span class="pun">{</span><span class="pln">exact</span><span class="pun">:</span><span class="pln"> audioSource</span><span class="pun">}</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">},</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; video</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><strong><span class="pln">deviceId</span><span class="pun">:</span><span class="pln"> videoSource </span></strong><span class="pun">?</span><span class="pln"> </span><span class="pun">{</span><span class="pln">exact</span><span class="pun">:</span><span class="pln"> videoSource</span><span class="pun">}</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">navigator</span><span class="pun">.</span><span class="pln">mediaDevices</span><span class="pun">.</span><span class="pln">getUserMedia</span><span class="pun">(</span><span class="pln">constraints</span><span class="pun">).</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">then</span><span class="pun">(</span><span class="pln">gotStream</span><span class="pun">).</span><span class="kwd">then</span><span class="pun">(</span><span class="pln">gotDevices</span><span class="pun">).</span><span class="kwd">catch</span><span class="pun">(</span><span class="pln">handleError</span><span class="pun">);</span></li>
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


<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> options </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">mimeType</span><span class="pun">:</span><span class="pln"> </span><span class="str">'video/webm; codecs=vp9'</span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">mediaRecorder </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">MediaRecorder</span><span class="pun">(</span><span class="pln">stream</span><span class="pun">,</span><span class="pln"> options</span><span class="pun">);</span></li>
</ol></div>


__2 - Add a "data handler" and call the start() method of the mediaRecorder object__

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> recordedChunks </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span><span class="pln"> </span><span class="com">// will hold the recorded stream</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">mediaRecorder</span><span class="pun">.</span><span class="pln">ondataavailable </span><span class="pun">=</span><span class="pln"> handleDataAvailable</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">mediaRecorder</span><span class="pun">.</span><span class="pln">start</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> handleDataAvailable</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">data</span><span class="pun">.</span><span class="pln">size </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; recordedChunks</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="kwd">event</span><span class="pun">.</span><span class="pln">data</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp;}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// ...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">}</span></li>
</ol></div>


__Explanations:__

+ Line 1: we declare an array of bytes that will hold the recorded stream.
+ Line 2: we declare the callback function that will be called while the stream is being captured. While the Webcam will be used, every xxx seconds, chunks of data will be passed to the `handleDataAvailable` function.
+ Lines 5-10: this function collects the chunk of data that corresponds to a few seconds of video, and stores it in the recordedChunks byte array.


__3 - When you've finished recording, tell the mediaRecorder to stop__

When you're done, you need to call the stop() method of the mediaRecorder object. This will end the periodic execution of the `handleDataAvailable` method, and stop the data capture.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">mediaRecorder</span><span class="pun">.</span><span class="pln">stop</span><span class="pun">();</span></li>
</ol></div>


__4 - Create a blob (binary large object) with the collected data, and use it to set the src attribute of an HTML5 video player__

This piece of code creates a blob with the `recordedChunks` array. Use the `URL.createObjectURL(recordedChunks)` standard method to create another object that can be used as a value to set the src attribute of an HTML5 video element.

Like that, the recorded stream can be played using a standard HTML5 video element.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> play</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> superBuffer </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Blob</span><span class="pun">(</span><span class="pln">recordedChunks</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;videoElement</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">URL</span><span class="pun">.</span><span class="pln">createObjectURL</span><span class="pun">(</span><span class="pln">superBuffer</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__5 - Download the captured stream__

A trick consists in creating, on the fly, an invisible link with a `download` attribute (see Week 1) and a `href` attribute  that points to the blob object containing the recorded stream encoded using a given codec, then generate programmatically a `click` event on the link. This will force the browser to download a file of type `video/webm` to the hard disk.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> download</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> blob </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Blob</span><span class="pun">(</span><span class="pln">recordedChunks</span><span class="pun">,</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">:</span><span class="pln"> </span><span class="str">'video/webm'</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; });</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> url </span><span class="pun">=</span><span class="pln"> URL</span><span class="pun">.</span><span class="pln">createObjectURL</span><span class="pun">(</span><span class="pln">blob</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'a'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">a</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; a</span><span class="pun">.</span><span class="pln">style </span><span class="pun">=</span><span class="pln"> </span><span class="str">'display: none'</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; a</span><span class="pun">.</span><span class="pln">href </span><span class="pun">=</span><span class="pln"> url</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; a</span><span class="pun">.</span><span class="pln">download </span><span class="pun">=</span><span class="pln"> </span><span class="str">'test.webm'</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; a</span><span class="pun">.</span><span class="pln">click</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; window</span><span class="pun">.</span><span class="pln">URL</span><span class="pun">.</span><span class="pln">revokeObjectURL</span><span class="pun">(</span><span class="pln">url</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>




