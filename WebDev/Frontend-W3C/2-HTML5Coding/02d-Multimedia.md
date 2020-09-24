# Week 2: HTML5 Multimedia

## 2.4 Webcam, microphone: the getUserMedia API


## 2.4.0 Lecture Notes

+ The `getUserMedia` API
  + useful for controlling a Webcam video stream
  + one component of the WebRTC specification
  + not considered a "real" part of the HTML5 specification
  + dealing with video streams: always used in conjunction with the `<video>` element
  + [specification](https://www.w3.org/TR/mediacapture-streams/)
  + Webcam usage
    + set the `srcObject` attribute of a `<video>` element to the live video stream object coming out of the Webcam
    + `navigator.getUserMedia(params)` method: get this stream
    + returns an ES6 promise (ES stands for ECMAScript and the scripting language that forms the basis of JavaScript)
  + mandatory to access the page that contains the JavaScript code through `https://`



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






