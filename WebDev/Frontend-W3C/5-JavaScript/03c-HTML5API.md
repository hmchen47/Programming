# Module 3: Playing with HTML5 APIs

## 3.3 HTML5 multimedia and JavaScript API

### 3.3.1 Playing audio and video streams

These examples are adapted from the ones in the W3Cx [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) course, which covers multimedia in depth. The [HTML5 advanced course](https://www.edx.org/course/html5-apps-and-games) also gives further examples covering topics such as making a video player with chapter navigation, clickable transcript, audio EQ, etc.


#### The `<video>` element

The `<video>` element of HTML5 is one of the two "Flash killers" (the other being the `<canvas>` element). It was designed to replace horrible things like embedded Flash objects that we used to encounter not so long ago.

The new way of doing things is a lot better... (please open this [live example at JS Bin](https://jsbin.com/kimayesazo/edit?html,output)).

[JS Bin Demo](https://jsbin.com/kimayesazo/edit?html,output)

[Local Demo](src/03c-example01.html)

The source code of this example shows the typical usage of the `<video>` element:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag" style="color: #008888;">&lt;video</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">width</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"320"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">height</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"240"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">controls</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"controls"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag" style="color: #008888;">&lt;source</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"movie.mp4"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">type</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"video/mp4"</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag" style="color: #008888;">&lt;source</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"movie.ogg"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">type</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"video/ogg"</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Your browser does not support the&nbsp;</span><span class="tag" style="color: #008888;">&lt;video&gt;</span><span class="pln">&nbsp;element.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;">&lt;/video&gt;</span></li>
</ol></div>

Please note that:

+ The `controls` attribute indicates that a control panel with play/stop/volume/progress widgets should be displayed;
+ Usually the browser  will use the first format it recognizes  (in this case, the browser checks whether `mp4` is supported, and if not, it will check for the `ogg` format, and so on). Some browsers may use a different heuristic and choose a "preferred" format.
+ The `<video>` element is a DOM member, so  CSS styling can be applied, as well as manipulation using the DOM API.

__You will learn more about the different attributes of the `<video>` element later on in the course.__

__Restriction: you cannot embed a YouTube or a Daily Motion video using the `<video>` element__

Help! `<video src="my youtube video URL"></video>` does not work! 

<div style="border: 2px solid red; margin: 10px; padding: 10px;">
<p><span style="color: #ff0000;"><strong>BEWARE</strong></span>:&nbsp;<em>you cannot directly embed videos from most of the popular social Web sites such as YouTube, Dailymotion, Vimeo, etc.&nbsp;<span style="line-height: 1.6;">For commercial&nbsp;reasons, and because advertising is automatically &nbsp;added to the&nbsp;videos, these Web sites do not allow "regular" embedding of their videos.</span></em></p>
</div>

While they use HTML5 to render their videos, these hosting sites (YouTube, etc.) use rather complex techniques in order to prevent you from using them with the `<video>` element. Instead, you often need to embed an `<iframe>` that will render the HTML5 videos in your Web site, and of course, the advertising that comes along with them.

Usually you have an "embed" button close to the videos that prompts you with some HTML code that you can copy and paste for embedding.


__An example using YouTube:__

Here is the HTML code you need to copy and paste in order to embed a video (in this case, a tutorial that tells you how to embed a YouTube video):

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag" style="color: #008888;">&lt;iframe</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">width</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"560"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">height</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"315"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"https://www.youtube.com/embed/ZH1XOsv8Oyo"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">frameborder</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"0"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #AA0066;">allowfullscreen</span><span class="tag" style="color: #008888;">&gt;&lt;/iframe&gt;</span></li>
</ol></div>

Below is the YouTube video embedded in this page using the above code: it's HTML5 but it's not a `<video>` element directly inserted in the HTML of this page - it's an `<iframe>`.

<p><iframe src="https://www.youtube.com/embed/ZH1XOsv8Oyo" allowfullscreen="" width="560" height="315" frameborder="0"></iframe></p>


#### The `<audio>` element

##### Introduction

HTML5 audio is composed of several layers:

+ [__The `<audio>` element__](https://www.w3.org/wiki/HTML/Elements/audio) is useful for embedding an audio player into a Web page. It is dedicated for <u>streamed audio</u>. It is very similar to the `<video>` element, both in its use and in its API.
+ [__The "Web Audio API"__](https://www.w3.org/TR/webaudio/) is designed for musical applications and for adding sound effects to games. This pure JavaScript API supports manipulation of sound samples (loops, etc.), music synthesis and sound generation (oscillators, etc.). It also comes with a set of predefined sound processing modules (reverb, delay, etc.).

<div style="border: 1px solid red; padding: 10px;">This course focuses on the&nbsp;<span style="font-family: 'courier new', courier;">&lt;audio&gt;</span>&nbsp;element. Please check for&nbsp; <a href="https://www.w3.org/TR/webaudio/" target="_blank">the Web Audio API</a>&nbsp;and other advanced parts of HTML5 in W3Cx's <a href="https://www.edx.org/course/html5-apps-and-games" target="_blank">HTML5 Apps and Games</a> course.</div>

The attributes, event set and JavaScript API of the `<audio>` element are just a "reduced" version of the ones from the `<video>` element, and here we will only address their differences and peculiarities.


##### The `<audio>` element - basic usage

The most simple basic example

[Online example from JS Bin](https://jsbin.com/xojobirowo/edit?html,output)

[JS Bin Demo](https://jsbin.com/xojobirowo/edit?html,output)

[Local Demo](src/03c-example02.html)

<p>Press play to stream the neigh&nbsp;of a&nbsp;horse: &nbsp;&nbsp;<audio controls="controls">
 <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg" type="audio/ogg">
  <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3" type="audio/mp3">
  Your browser does not support the audio element.
</audio></p>

As you can see, the code is very similar to the basic `<video>` element usage.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; &lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;title&gt;</span><span class="pln">Draw a monster in a canvas</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"><span class="tag">&nbsp;&nbsp; </span>&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;audio</span><span class="pln"> </span><span class="atn">controls</span><span class="pun">=</span><span class="atv">"controls" crossorigin="anonymous"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg"</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"audio/ogg"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"audio/mp3"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>Your browser does not support the audio element.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>Download the audio/video in</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">”https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg”</span><span class="tag">&gt;</span><span class="pln">OGG</span><span class="tag">&lt;/a&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>or</span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">”https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3”</span><span class="tag">&gt;</span><span class="pln">MP3</span><span class="tag">&lt;/a&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"><span class="tag">&nbsp;&nbsp; </span></span><span class="pln"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag">&nbsp;&nbsp; </span></span></span>format.</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;/audio&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

In this example, just as for the `<video>` element, we used the `controls` attribute in order to render the play/stop, time, volume and progress widgets.

Notice the other similarities: between the `<audio>...</audio>` tags, we added a text message that is displayed if the Web browser doesn't support the `<audio>` element, and we used several `<source>...</source>` elements that link to different audio formats for the same file. The browser will use the first format it recognizes.

_Lines 8-12_:  we suggest downloading the audio files if the browser does not support the `<audio>` element. This is also a best practice!


#### Notes for 3.3.1 Playing audio and video streams

+ `<video>` element
  + one of the two "Flash  killer" (`<canvas>` as the other)
  + a DOM member $\implies$ CSS styling applied and maipulating w/ the DOM API
  + unable to embedded a YouTube and Daily Motion video
  + typical usage

    ```html
    <video width="320" height="240" controls="controls">
      <source src="movie.mp4" type="video/mp4" />
      <source src="movie.ogg" type="video/ogg" />
      Your browser does not support the <video> element.
    </video>
    ```

    + `control` attribute: displaying a control panel w/ play/stop/volume/progress widget
    + browser using the 1st format recognized but some browsers probably choose a "preferred" format
  
  + example using YouTube: `<iframe width="560" height="315" src="https://www.youtube.com/embed/ZH1XOsv8Oyo" frameborder="0" allowfullscreen></iframe>`

+ Audio 
  + `<audio>` element
    + useful for embedding an audio player into a Web page
    + dedicated for _streamed audio_
    + a DOM member $\implies$ VSS styling applied and manipulating w/ the DOM API
    + attributes: a reduced version of `<video>` element
    + typical usage

      ```html
      <audio controls="controls" crossorigin="anonymous">
         <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg" type="audio/ogg" />
         <source src="https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3" type="audio/mp3" />
         Your browser does not support the audio element.
         Download the audio/video in
         <a href=”https://mainline.i3s.unice.fr/mooc/week2p1/horse.ogg”>OGG</a>
         or<a href=”https://mainline.i3s.unice.fr/mooc/week2p1/horse.mp3”>MP3</a> format.
      </audio>
      ```

      + `control` attribute: render the play/stop, time, volume and progress widgets
      + adding text message of the Wen browser not supporting the `<audio>` element
      + `<source>...</source>` element: link to different audio formats for the same file
      + browser using the 1st format recognized
  + Wen Audio API
    + designed for musical applications and for adding sound effects to games
    + manipulation of sund samples (loops. etc.), music synthesis and sound generation (oscillators, etc.)
    + w/ a set of predefined sound processing modules (reverb, delay, etc.)


#### Knowledge check 3.3.1

1. The `<video>` element is like any other HTML element: I can style it using CSS and interact programmatically with it using the JavaScript DOM API. (True/False)

  Ans: True<br>
  Explanation: Indeed, the `<video>` element is, like other HTML elements, a first class citizen of the DOM and can be styled using CSS or manipulated using the JavaScript DOM API.


### 3.3.2 Audio and video player JavaScript API


#### Live coding video: the video element JavaScript API

<a href="https://edx-video.net/W3CJSIXX2016-V003400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/2gz2casf)

Source code of the example from the video:

[CodePen Demo](https://codepen.io/w3devcampus/pen/WOvVPQ?editors=0011)

[Local Demo](src/03c-example03.html)


#### Audio and video player JavaScript API


##### Control `<audio>` and `<video>` elements from JavaScript

The `<video>` element has methods, properties/attributes and events that can be manipulated with JavaScript. Using the DOM API it's possible to manipulate an audio or video element as a JavaScript object that has:

+ __Methods__ for controlling its behavior, such as `play()`, `pause()`, etc.;
+ __Properties__ (duration, current position, etc.), either in read/write mode (such as volume), or in read-only mode (such as encoding, duration, etc.);
+ __Events__ generated during the life cycle of the element that can be processed using JavaScript callbacks. It is also possible to send events to control the video player.

Like any HTML element, the `<video>` element can be manipulated/created using the DOM JavaScript API. Here is an example of programmatically creating a `<video>` element:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="kwd">var</span><span class="pln">&nbsp;video&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">);</span></li>
<li class="L1"><span class="pln">video</span><span class="pun">.</span><span class="pln">src&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">'video.mp4'</span><span class="pun">;</span></li>
<li class="L2"><span class="pln">video</span><span class="pun">.</span><span class="pln">controls&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L3"><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">video</span><span class="pun">);</span></li>
</ol></div>

This will create a complete video player for the file "video.mp4", with control buttons, and will add it to the `<body>` element of the page.

##### JavaScript API of the `<audio>` and `<video>` elements

__Methods, properties and events__

The JavaScript API gives you powerful tools to manipulate the `<video>` element, as the video object provides many properties, methods and events.

The complete list of <u>events</u> can be found at in this [specification page](https://html.spec.whatwg.org/multipage/media.html#mediaevents), and numerous examples of each event can be found on many Web sites [such as this one](https://www.htmlgoodies.com/html5/tutorials/HTML5-Development-Class-Media-Events-3883356.htm#fbid=rRDjiexm8vR).

The complete list of <u>properties</u> can be found at [the W3C HTML5 Video Events and API page](https://www.w3.org/2010/05/video/mediaevents.html). This page is interesting for Web developers because it shows an interactive view of the different values and events changing over time while the video is playing within the page.

__Click the picture to see it running online (or try the [direct link](https://www.w3.org/2010/05/video/mediaevents.html)), then play with the different buttons and look at the table of events and properties that will change in real time. The displayed names show the properties, events, and methods from the API.__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://www.w3.org/2010/05/video/mediaevents.html')"
    src    ="https://tinyurl.com/14n0mvdk"
    alt    ="JavaScript API gives you powerful tools to manipulate the <video> element"
    title  ="JavaScript API gives you powerful tools to manipulate the <video> element"
  />
</figure>

Here is a table that shows the most interesting methods, properties and events provided by the `<video>` element API
We provide this as a quick reminder - keep in mind that the complete list is much longer!

<table style="max-width: 100%; border-collapse: collapse; border-spacing: 0px; table-layout: auto border: 2px solid #0f0505; background-color: transparent; margin: 0 auto; width: 50vw;" dir="ltr" rules="all" frame="box" cellpadding="10" border="2">
<tbody>
<tr>
<td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Methods</strong></span></td>
<td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Properties</strong></span></td>
<td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Events</strong></span></td>
</tr>
<tr><td><strong><span style="font-family: 'courier new', courier, monospace;">play()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">currentSrc</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">play</span></strong></td></tr>
<tr><td><strong><span style="font-family: 'courier new', courier, monospace;">pause()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">currentTime</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">pause</span></strong></td></tr>
<tr><td><strong><span style="font-family: 'courier new', courier, monospace;">load()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">startTime (readonly)</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">progress</span></strong></td></tr>
<tr><td><strong>canPlayType()</strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">videoWidth</span></strong></td><td><strong>error</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">videoHeight</span></strong></td><td><strong>timeupdate</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">duration (readonly)</span></strong></td><td><strong>ended</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">ended (readonly)</span></strong></td><td><strong>abort</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">error</span></strong></td><td><strong>empty</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">paused (readonly)</span></strong></td><td><strong>emptied</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">muted</span></strong></td><td><strong>waiting</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">seeking</span></strong></td><td><strong>loadedmetadata</strong></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">volume</span></strong></td><td></td></tr>
<tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">height</span></strong></td><td></td></tr>
<tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;">width</span></strong></p></td><td></td></tr>
<tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;" face="courier new, courier, monospace">seekable (readonly)</span></strong></p>
</td><td></td></tr>
<tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;">played (readonly)</span></strong></p>
</td><td></td></tr>
</tbody>
</table>

Now let's take a look at a set of examples demonstrating how to use the most important of these properties, methods, and events...


#### Notes for 3.3.2 Audio and video player JavaScript API

+ Control `<audio>` & `<video>` elements
  + elements w/ methods, properties/attributes and events to manipulate w/ JS
  + the DOM API
    + methods: controlling behavior, such as `play()`, `pause()`, etc.
    + properties:
      + read/write: volume, current time, etc.
      + read-only mode: encoding, duration, etc.
    + events: 
      + generated during the life cycle of the element
      + processed using JS callback
      + possible to trigger event to control the player
  + example: creating a video player w/ control buttons

    ```js
    var video = document.createElement('video');
    video.src = 'video.mp4';
    video.controls = true;
    document.body.appendChild(video);
    ```

+ JavaScript API for `<video>` and `<audio>` elements
  + powerful tools to manipulate element
  + reference: [HTML5 Video Events and API](https://www.w3.org/2010/05/video/mediaevents.html)
  + [event list](https://html.spec.whatwg.org/multipage/media.html#mediaevents)
    + network state: `loadstart`, `progress`, `suspend`, `abort`, `error`, `emptied`, `stalled`
    + ready state: `loadedmetadata`, `loadeddata`, `canplay`, `canplaythrough`, `playing`, `waiting`
    + searching: `seeking`, `seeked`, `ended`
    + playing: `durationchange`, `timeupdate`, `play`, `pause`, `ratechange`
    + element: `resize`, `volumechange`
  + most interested methods, properties and events for `<video>` element

    <table style="max-width: 100%; border-collapse: collapse; border-spacing: 0px; table-layout: auto border: 2px solid #0f0505; background-color: transparent; margin: 0 auto; width: 50vw;" dir="ltr" rules="all" frame="box" cellpadding="10" border="2">
    <tbody>
    <tr>
    <td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Methods</strong></span></td>
    <td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Properties</strong></span></td>
    <td style="text-align: center; background-color: cadetblue; width: 10%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Events</strong></span></td>
    </tr>
    <tr><td><strong><span style="font-family: 'courier new', courier, monospace;">play()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">currentSrc</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">play</span></strong></td></tr>
    <tr><td><strong><span style="font-family: 'courier new', courier, monospace;">pause()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">currentTime</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">pause</span></strong></td></tr>
    <tr><td><strong><span style="font-family: 'courier new', courier, monospace;">load()</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">startTime (readonly)</span></strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">progress</span></strong></td></tr>
    <tr><td><strong>canPlayType()</strong></td><td><strong><span style="font-family: 'courier new', courier, monospace;">videoWidth</span></strong></td><td><strong>error</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">videoHeight</span></strong></td><td><strong>timeupdate</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">duration (readonly)</span></strong></td><td><strong>ended</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">ended (readonly)</span></strong></td><td><strong>abort</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">error</span></strong></td><td><strong>empty</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">paused (readonly)</span></strong></td><td><strong>emptied</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">muted</span></strong></td><td><strong>waiting</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">seeking</span></strong></td><td><strong>loadedmetadata</strong></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">volume</span></strong></td><td></td></tr>
    <tr><td></td><td><strong><span style="font-family: 'courier new', courier, monospace;">height</span></strong></td><td></td></tr>
    <tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;">width</span></strong></p></td><td></td></tr>
    <tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;" face="courier new, courier, monospace">seekable (readonly)</span></strong></p>
    </td><td></td></tr>
    <tr><td></td><td><p style="margin: 0px 0px 10px;"><strong><span style="font-family: 'courier new', courier, monospace;">played (readonly)</span></strong></p>
    </td><td></td></tr>
    </tbody>
    </table>


#### Knowledge check 3.3.2

The W3C specification about the JavaScript API associated to `<audio>` and `<video>` elements, proposes an interactive demonstration of the different properties/methods/events; it's a must see for all Web developers interested in multimedia. Try it and guess what properties indicate the length of the video in seconds and the name of a valid event that is sent while the video is being played...

  a. `duration` and `timeupdate`<br/>
  b. `currentTime` and `play`<br/>

  Ans: <br>
  Explanation






### Reference Tables


<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 60vw;" cellspacing=0 cellpadding=5 border=1 align="center">
  <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://html.spec.whatwg.org/multipage/media.html#mediaevents">Events summary for Media Elements</a></caption>
  <thead>
  <tr style="font-size: 1.2em; vertical-align:middle">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Event name</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Interface</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Fired when</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Preconditions</th>
  </tr>
  </thead>
  <tbody>
    <tr><td><code>loadstart</code></dfn></td><td><code id="mediaevents:event"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent begins looking for <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data">media data</a>, as part of the <a href="https://html.spec.whatwg.org/multipage/media.html#concept-media-load-algorithm" id="mediaevents:concept-media-load-algorithm">resource selection algorithm</a>.
    </td><td><code id="mediaevents:dom-media-networkstate"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code> equals <code id="mediaevents:dom-media-network_loading"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_loading">NETWORK_LOADING</a></code>
    </td></tr>
    <tr><td><code>progress</code></td><td><code id="mediaevents:event-2"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent is fetching <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-2">media data</a>.
    </td><td><code id="mediaevents:dom-media-networkstate-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code> equals <code id="mediaevents:dom-media-network_loading-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_loading">NETWORK_LOADING</a></code>
    </td></tr>
    <tr><td><code>suspend</code></td><td><code id="mediaevents:event-3"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent is intentionally not currently fetching <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-3">media data</a>.
    </td><td><code id="mediaevents:dom-media-networkstate-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code> equals <code id="mediaevents:dom-media-network_idle"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_idle">NETWORK_IDLE</a></code>
    </td></tr>
    <tr><td><code>abort</code></td><td><code id="mediaevents:event-4"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent stops fetching the <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-4">media data</a> before it is completely
    downloaded, but not due to an error.
    </td><td><code id="mediaevents:dom-media-error"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-error">error</a></code> is an object with the code <code id="mediaevents:dom-mediaerror-media_err_aborted"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-mediaerror-media_err_aborted">MEDIA_ERR_ABORTED</a></code>. <code id="mediaevents:dom-media-networkstate-4"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code> equals either <code id="mediaevents:dom-media-network_empty"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_empty">NETWORK_EMPTY</a></code> or <code id="mediaevents:dom-media-network_idle-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_idle">NETWORK_IDLE</a></code>, depending on when the download was aborted.
    </td></tr>
    <tr><td><code>error</code></td><td><code id="mediaevents:event-5"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>An error occurs while fetching the <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-5">media data</a> or the type of the resource
    is not supported media format.
    </td><td><code id="mediaevents:dom-media-error-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-error">error</a></code> is an object with the code <code id="mediaevents:dom-mediaerror-media_err_network"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-mediaerror-media_err_network">MEDIA_ERR_NETWORK</a></code> or higher. <code id="mediaevents:dom-media-networkstate-5"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code> equals either <code id="mediaevents:dom-media-network_empty-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_empty">NETWORK_EMPTY</a></code> or <code id="mediaevents:dom-media-network_idle-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_idle">NETWORK_IDLE</a></code>, depending on when the download was aborted.
    </td></tr>
    <tr><td><code>emptied</code></td><td><code id="mediaevents:event-6"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>A <a href="https://html.spec.whatwg.org/multipage/media.html#media-element" id="mediaevents:media-element-2">media element</a> whose <code id="mediaevents:dom-media-networkstate-6"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code>
    was previously not in the <code id="mediaevents:dom-media-network_empty-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_empty">NETWORK_EMPTY</a></code> state has
    just switched to that state (either because of a fatal error during load that's about to be
    reported, or because the <code id="mediaevents:dom-media-load"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-load">load()</a></code> method was invoked while
    the <a href="https://html.spec.whatwg.org/multipage/media.html#concept-media-load-algorithm" id="mediaevents:concept-media-load-algorithm-2">resource selection algorithm</a> was already
    running).
    </td><td><code id="mediaevents:dom-media-networkstate-7"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code> is <code id="mediaevents:dom-media-network_empty-4"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_empty">NETWORK_EMPTY</a></code>; all the IDL attributes are in their
    initial states.
    </td></tr>
    <tr><td><code>stalled</code></td><td><code id="mediaevents:event-7"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent is trying to fetch <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-6">media data</a>, but data is unexpectedly not
    forthcoming.
    </td><td><code id="mediaevents:dom-media-networkstate-8"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-networkstate">networkState</a></code> is <code id="mediaevents:dom-media-network_loading-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-network_loading">NETWORK_LOADING</a></code>.
    </td></tr>
  </tbody><tbody>
  <tr><td><code>loadedmetadata</code></td><td><code id="mediaevents:event-8"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent has just determined the duration and dimensions of the <a href="https://html.spec.whatwg.org/multipage/media.html#media-resource" id="mediaevents:media-resource">media
    resource</a> and <a href="https://html.spec.whatwg.org/multipage/media.html#the-text-tracks-are-ready" id="mediaevents:the-text-tracks-are-ready">the text tracks are ready</a>.
    </td><td><code id="mediaevents:dom-media-readystate"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> is newly equal to <code id="mediaevents:dom-media-have_metadata"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_metadata">HAVE_METADATA</a></code> or greater for the first time.
    </td></tr>
    <tr><td><code>loadeddata</code></td><td><code id="mediaevents:event-9"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent can render the <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-7">media data</a> at the <a href="https://html.spec.whatwg.org/multipage/media.html#current-playback-position" id="mediaevents:current-playback-position">current playback
    position</a> for the first time.
    </td><td><code id="mediaevents:dom-media-readystate-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> newly increased to <code id="mediaevents:dom-media-have_current_data"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_current_data">HAVE_CURRENT_DATA</a></code> or greater for the first time.
    </td></tr>
    <tr><td><code>canplay</code></td><td><code id="mediaevents:event-10"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent can resume playback of the <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-8">media data</a>, but estimates that if
    playback were to be started now, the <a href="https://html.spec.whatwg.org/multipage/media.html#media-resource" id="mediaevents:media-resource-2">media resource</a> could not be rendered at the
    current playback rate up to its end without having to stop for further buffering of content.
    </td><td><code id="mediaevents:dom-media-readystate-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> newly increased to <code id="mediaevents:dom-media-have_future_data"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_future_data">HAVE_FUTURE_DATA</a></code> or greater.
    </td></tr>
    <tr><td><code>canplaythrough</code></td><td><code id="mediaevents:event-11"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The user agent estimates that if playback were to be started now, the <a href="https://html.spec.whatwg.org/multipage/media.html#media-resource" id="mediaevents:media-resource-3">media
    resource</a> could be rendered at the current playback rate all the way to its end without
    having to stop for further buffering.
    </td><td><code id="mediaevents:dom-media-readystate-4"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> is newly equal to <code id="mediaevents:dom-media-have_enough_data"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_enough_data">HAVE_ENOUGH_DATA</a></code>.
    </td></tr>
    <tr><td><code>playing</code></td><td><code id="mediaevents:event-12"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>Playback is ready to start after having been paused or delayed due to lack of <a href="https://html.spec.whatwg.org/multipage/media.html#media-data" id="mediaevents:media-data-9">media
    data</a>.
    </td><td><code id="mediaevents:dom-media-readystate-5"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> is newly equal to or greater than
    <code id="mediaevents:dom-media-have_future_data-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_future_data">HAVE_FUTURE_DATA</a></code> and <code id="mediaevents:dom-media-paused"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-paused">paused</a></code> is false, or <code id="mediaevents:dom-media-paused-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-paused">paused</a></code> is newly false and <code id="mediaevents:dom-media-readystate-6"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> is equal to or greater than <code id="mediaevents:dom-media-have_future_data-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_future_data">HAVE_FUTURE_DATA</a></code>. Even if this event fires, the
    element might still not be <a href="https://html.spec.whatwg.org/multipage/media.html#potentially-playing" id="mediaevents:potentially-playing">potentially playing</a>, e.g. if the element is
    <a href="https://html.spec.whatwg.org/multipage/media.html#paused-for-user-interaction" id="mediaevents:paused-for-user-interaction">paused for user interaction</a> or <a href="https://html.spec.whatwg.org/multipage/media.html#paused-for-in-band-content" id="mediaevents:paused-for-in-band-content">paused for in-band content</a>.
    </td></tr>
    <tr><td><code>waiting</code></td><td><code id="mediaevents:event-13"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>Playback has stopped because the next frame is not available, but the user agent expects
    that frame to become available in due course.
    </td><td><code id="mediaevents:dom-media-readystate-7"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> is equal to or less than <code id="mediaevents:dom-media-have_current_data-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_current_data">HAVE_CURRENT_DATA</a></code>, and <code id="mediaevents:dom-media-paused-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-paused">paused</a></code> is false. Either <code id="mediaevents:dom-media-seeking"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-seeking">seeking</a></code> is true, or the <a href="https://html.spec.whatwg.org/multipage/media.html#current-playback-position" id="mediaevents:current-playback-position-2">current playback position</a>
    is not contained in any of the ranges in <code id="mediaevents:dom-media-buffered"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-buffered">buffered</a></code>. It
    is possible for playback to stop for other reasons without <code id="mediaevents:dom-media-paused-4"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-paused">paused</a></code> being false, but those reasons do not fire this event
    (and when those situations resolve, a separate <code id="mediaevents:event-media-playing"><a href="https://html.spec.whatwg.org/multipage/media.html#event-media-playing">playing</a></code>
    event is not fired either): e.g., <a href="https://html.spec.whatwg.org/multipage/media.html#ended-playback" id="mediaevents:ended-playback">playback has ended</a>, or
    playback <a href="https://html.spec.whatwg.org/multipage/media.html#stopped-due-to-errors" id="mediaevents:stopped-due-to-errors">stopped due to errors</a>, or the element has <a href="https://html.spec.whatwg.org/multipage/media.html#paused-for-user-interaction" id="mediaevents:paused-for-user-interaction-2">paused for user
    interaction</a> or <a href="https://html.spec.whatwg.org/multipage/media.html#paused-for-in-band-content" id="mediaevents:paused-for-in-band-content-2">paused for in-band content</a>.
    </td></tr>
  </tbody><tbody>
    <tr><td><code>seeking</code></td><td><code id="mediaevents:event-14"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The <code id="mediaevents:dom-media-seeking-2"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-seeking">seeking</a></code> IDL attribute changed to true, and the user agent has started seeking to a new position.
    </td><td>
    </td></tr>
    <tr><td><code>seeked</code></td><td><code id="mediaevents:event-15"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The <code id="mediaevents:dom-media-seeking-3"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-seeking">seeking</a></code> IDL attribute changed to false after the <a href="https://html.spec.whatwg.org/multipage/media.html#current-playback-position" id="mediaevents:current-playback-position-3">current playback position</a> was changed.
    </td><td>
    </td></tr>
    <tr><td><code>ended</code></td><td><code id="mediaevents:event-16"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>Playback has stopped because the end of the <a href="https://html.spec.whatwg.org/multipage/media.html#media-resource" id="mediaevents:media-resource-4">media resource</a> was reached.
    </td><td><code id="mediaevents:dom-media-currenttime"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-currenttime">currentTime</a></code> equals the end of the <a href="https://html.spec.whatwg.org/multipage/media.html#media-resource" id="mediaevents:media-resource-5">media
    resource</a>; <code id="mediaevents:dom-media-ended"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-ended">ended</a></code> is true.
    </td></tr>
  </tbody><tbody>
    <tr><td><code>durationchange</code></td><td><code id="mediaevents:event-17"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The <code id="mediaevents:dom-media-duration"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-duration">duration</a></code> attribute has just been updated.
    </td><td>
    </td></tr>
    <tr><td><code>timeupdate</code></td><td><code id="mediaevents:event-18"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The <a href="https://html.spec.whatwg.org/multipage/media.html#current-playback-position" id="mediaevents:current-playback-position-4">current playback position</a> changed as part of normal playback or in an especially interesting way, for example discontinuously.
    </td><td>
    </td></tr>
    <tr><td><code>play</code></td><td><code id="mediaevents:event-19"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The element is no longer paused. Fired after the <code id="mediaevents:dom-media-play"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-play">play()</a></code>
    method has returned, or when the <code id="mediaevents:attr-media-autoplay"><a href="https://html.spec.whatwg.org/multipage/media.html#attr-media-autoplay">autoplay</a></code> attribute
    has caused playback to begin.
    </td><td><code id="mediaevents:dom-media-paused-5"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-paused">paused</a></code> is newly false.
    </td></tr>
    <tr><td><code>pause</code></td><td><code id="mediaevents:event-20"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>The element has been paused. Fired after the <code id="mediaevents:dom-media-pause"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-pause">pause()</a></code>
    method has returned.
    </td><td><code><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-paused">paused</a></code> is newly true.
    </td></tr>
    <tr><td><code>ratechange</code></td><td><code id="mediaevents:event-21"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>Either the <code id="mediaevents:dom-media-defaultplaybackrate"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-defaultplaybackrate">defaultPlaybackRate</a></code> or the
    <code id="mediaevents:dom-media-playbackrate"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-playbackrate">playbackRate</a></code> attribute has just been updated.
    </td><td>
    </td></tr>
  </tbody><tbody>
    <tr><td><code>resize</code>
    </td><td><code><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>One or both of the <code id="mediaevents:dom-video-videowidth"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-video-videowidth">videoWidth</a></code> and <code id="mediaevents:dom-video-videoheight"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-video-videoheight">videoHeight</a></code> attributes have just been updated.
    </td><td><a href="https://html.spec.whatwg.org/multipage/media.html#media-element" id="mediaevents:media-element-3">Media element</a> is a <code id="mediaevents:the-video-element"><a href="https://html.spec.whatwg.org/multipage/media.html#the-video-element">video</a></code> element; <code id="mediaevents:dom-media-readystate-8"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-readystate">readyState</a></code> is not <code id="mediaevents:dom-media-have_nothing"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-have_nothing">HAVE_NOTHING</a></code>
    </td></tr>
    <tr><td><code>volumechange</code></td><td><code id="mediaevents:event-23"><a data-x-internal="event" href="https://dom.spec.whatwg.org/#interface-event">Event</a></code>
    </td><td>Either the <code id="mediaevents:dom-media-volume"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-volume">volume</a></code> attribute or the <code id="mediaevents:dom-media-muted"><a href="https://html.spec.whatwg.org/multipage/media.html#dom-media-muted">muted</a></code> attribute has changed. Fired after the relevant
    attribute's setter has returned.
    </td><td>
  </td></tr></tbody>
</table>

