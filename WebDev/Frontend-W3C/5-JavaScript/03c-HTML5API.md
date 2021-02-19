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

+ Video and `<video>` element
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

    + `controls` attribute: displaying a control panel w/ play/stop/volume/progress widget
    + browser using the 1st format recognized but some browsers probably choose a "preferred" format
  
  + example using YouTube: `<iframe width="560" height="315" src="https://www.youtube.com/embed/ZH1XOsv8Oyo" frameborder="0" allowfullscreen></iframe>`

+ Audio 
  + `<audio>` element
    + useful for embedding an audio player into a Web page
    + dedicated for _streamed audio_
    + a DOM member $\implies$CVSS styling applied and manipulating w/ the DOM API
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
  + Web Audio API
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

    <table style="max-width: 100%; border-collapse: collapse; border-spacing: 0px; table-layout: auto border: 2px solid #0f0505; background-color: transparent; margin: 0 auto; width: 60vw;" dir="ltr" rules="all" frame="box" cellpadding="10" border="2">
    <tbody>
    <tr>
    <td style="text-align: center; background-color: cadetblue; width: 5%;"><span style="font-family: 'courier new', courier, monospace; font-size: medium;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">Methods</strong></span></td>
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

1. The W3C specification about the JavaScript API associated to `<audio>` and `<video>` elements, proposes an interactive demonstration of the different properties/methods/events; it's a must see for all Web developers interested in multimedia. Try it and guess what properties indicate the length of the video in seconds and the name of a valid event that is sent while the video is being played...

  a. `duration` and `timeupdate`<br/>
  b. `currentTime` and `play`<br/>

  Ans: a<br>
  Explanation: If you try the intereactive demonstration, and play the example video, you will see that the `duration` property indicates the total length of the video. You will also see that the `timeupdate` event is emitted regularly while the video is being played?


### 3.3.3 Examples using the JavaScript API

The JavaScript API is useful for implementing playlists, making custom user interfaces and many other interesting things. The "enhanced HTML5 multimedia players" presented later on in the course rely heavily on this API.

#### Control w/ external buttons

__Example #1: how to use external buttons to control a player's behavior__

This example shows the first steps towards writing a custom video player. It shows basic usage of the JavaScript API for adding custom buttons to play/pause the video or to go back to the beginning by setting the currentTime property to zero.

[Try it online](https://jsbin.com/dayuko/1/edit?html,css,output), and look at the source code. ([Local Demo](src/03c-example04.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/1s4oij0v')"
    src    ="https://tinyurl.com/hxxjdjrp"
    alt    ="Snapshot of a video player"
    title  ="Snapshot of a video player"
  />
</figure>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="tag">&lt;video</span><span class="pln">&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"vid"</span><span class="pln">&nbsp;</span><span class="atn">controls</span><span class="tag">&gt;</span></li>
<li class="L4"><span class="pln"></span><span class="tag">&lt;source</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">https://html5doctor.com/demos/video-canvas-magic/video.webm</span><span class="pln"></span></li>
<li class="L4"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">video/webm</span><span class="tag">&gt;</span><span class="pln"></span></li>
<li class="L5">...</li>
<li class="L7"><span class="tag">&lt;/video&gt;</span><span class="pln"></span></li>
<li class="L8"><span class="tag">&lt;p&gt;</span><span class="pln">Example of custom controls:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L9"><span class="tag">&lt;button</span><span class="pln">&nbsp;</span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">playVideo</span><span class="pun">();</span><span class="atv">"</span><span class="pln">&nbsp;</span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">cursor</span><span class="pun">:</span><span class="pln">&nbsp;pointer</span><span class="pun">;</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Play</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L0"><span class="pln">&nbsp;</span></li>
<li class="L1"><span class="tag">&lt;button</span><span class="pln">&nbsp;</span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">pauseVideo</span><span class="pun">();</span><span class="atv">"</span><span class="pln">&nbsp;</span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">cursor</span><span class="pun">:</span><span class="pln">&nbsp;pointer</span><span class="pun">;</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Pause</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L2"><span class="pln">&nbsp;</span></li>
<li class="L3"><span class="tag">&lt;button</span><span class="pln">&nbsp;</span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">rewindVideo</span><span class="pun">();</span><span class="atv">"</span><span class="pln">&nbsp;</span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">cursor</span><span class="pun">:</span><span class="pln">&nbsp;pointer</span><span class="pun">;</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;Back to beginning</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L5"><span class="pln"></span><span class="tag">&lt;script&gt;</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp; var vid&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#vid"</span><span class="pun">);</span></li>
<li class="L7"><span class="pln"></span></li>
<li class="L8"><span class="kwd">&nbsp; &nbsp; function</span><span class="pln">&nbsp;playVideo</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;vid</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L0"><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L1"><span class="kwd">&nbsp; &nbsp; function</span><span class="pln">&nbsp;pauseVideo</span><span class="pun">() {</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;vid</span><span class="pun">.</span><span class="pln">pause</span><span class="pun">();</span></li>
<li class="L3"><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L4"><span class="pln"></span></li>
<li class="L5"><span class="kwd">&nbsp; &nbsp; function</span><span class="pln">&nbsp;rewindVideo</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;vid</span><span class="pun">.</span><span class="pln">currentTime&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L7"><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L8"><span class="tag">&lt;/script&gt;</span></li>
</ol></div>

+ _Lines 7, 9 and 11_: we add a click listener to each button, in order to call a JavaScript function when the button is clicked.
+ _Line 14_: using the DOM API we get the JavaScript object that corresponds to the video element we inserted in the HTML document. This line is outside a function, it will be executed when the page loads.
+ _Lines 17 and 20_: we call methods from the API for playing/pausing the video.
+ _Line 24_: we modify the `currentTime` property in order to rewind the video. Note that `vid.load()` also rewinds the video, shows the poster image again, but also pauses the video. By using `currentTime=0` the playback does not stop. 


#### Sequential play multiple videos

__Example #2: how to detect the end of a video and start a new one__

This example listens for the `ended` event, and calls a callback function when the video has finished.

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="tag">&lt;video</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"video.ogv"</span><span class="pln">&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="tag">&gt;</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp; video not supported</span></li>
<li class="L2"><span class="tag">&lt;/video&gt;</span></li>
<li class="L3"><span class="pln"></span></li>
<li class="L4"><span class="tag">&lt;script</span><span class="pln">&nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">'text/javascript'</span><span class="tag">&gt;</span></li>
<li class="L5"><span class="pln">&nbsp; var vid = document</span><span class="pun">.querySelector</span><span class="pun">(</span><span class="str">'#myVideo'</span><span class="pun">);</span></li>
<li class="L5"><span class="pln">&nbsp; vid.addEventListener</span><span class="pun">(</span><span class="str">'ended'</span><span class="pun">,&nbsp;</span><span class="pun"><span style="color: #000000; line-height: 23.2727279663086px; background-color: #ffffff;">playN</span><span style="color: #000000; line-height: 23.2727279663086px; background-color: #ffffff;">extVideo</span>,&nbsp;</span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5"><span class="pun"></span></li>
<li class="L6"><span class="kwd">&nbsp; function</span><span class="pln">&nbsp;playNextVideo</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Whatever you want to do after the event (play another video, </span></li>
<li class="L7"><span class="com">&nbsp; &nbsp; &nbsp;// for example), change the src attribute,&nbsp;</span>of the video element, etc.</li>
<li class="L9"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0"><span class="tag">&lt;/script&gt;</span></li>
</ol></div>

#### Managing playlists

__Example #3: how to manage playlists (application of the above technique)__

This example detects the end of a video then loads the next video, changes the `src` attribute of the video element and plays the video (see the online [example](https://jsbin.com/ridujix/1/edit?html,output)). ([Local Demo](src/03c-example05.html))

To try this example: use the progress cursor to go near the end of the first video that is being played and see how it continues with the next video. 

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="dec">&lt;!doctype html&gt;</span></li>
<li class="L1"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2"><span class="tag">&lt;head&gt;</span></li>
<li class="L3"><span class="pln"></span><span class="tag">&lt;title&gt;</span><span class="pln">Sequential Movies</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4"><span class="pln"></span><span class="tag">&lt;script&gt;</span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;myVideo</span><span class="pun">;</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;currentVideo&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;sources&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="pun">[</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">"https://html5doctor.com/demos/video-canvas-magic/video.mp4"</span><span class="pun">,</span></li>
<li class="L9"><span class="pln"></span><span class="str">&nbsp;"https://ia600204.us.archive.org/9/items/AnimatedMechanicalArtPiecesAtMit/P1120973_512kb.mp4"</span><span class="pln"></span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp;</span><span class="pun">];</span></li>
<li class="L1"><span class="pln"></span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Set the src of the video to the next URL in the playlist</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp;</span><span class="com">// If at the end, we start again from beginning (the modulo</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp;</span><span class="com">// source.length does this)</span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln">&nbsp;loadNextVideo</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp; &nbsp; myVideo</span><span class="pun">.</span><span class="pln">src&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;sources</span><span class="pun">[</span><span class="pln">currentVideo&nbsp;</span><span class="pun">%</span><span class="pln">&nbsp;sources</span><span class="pun">.</span><span class="pln">length</span><span class="pun">]</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp; myVideo</span><span class="pun">.</span><span class="pln">load</span><span class="pun">();</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; currentVideo</span><span class="pun">++;</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0"><span class="pln"></span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp;</span><span class="com">//&nbsp;callback that loads and plays the next video</span></li>
<li class="L2"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln">&nbsp;loadAndplayNextVideo</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"playing "</span><span class="pln">&nbsp;</span><span class="pun">+</span><span class="pln">&nbsp;sources</span><span class="pun">[</span><span class="pun"><span class="pln" style="line-height: 23.2727279663086px; background-color: #ffffff;">currentVideo&nbsp;</span><span class="pun" style="line-height: 23.2727279663086px; background-color: #ffffff;">%</span><span class="pln" style="line-height: 23.2727279663086px; background-color: #ffffff;">&nbsp;sources</span><span class="pun" style="line-height: 23.2727279663086px; background-color: #ffffff;">.</span><span class="pln" style="line-height: 23.2727279663086px; background-color: #ffffff;">length</span>])</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp; &nbsp; loadNextVideo</span><span class="pun">();</span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp; &nbsp; myVideo</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L5"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L8"><span class="pln"></span></li>
<li class="L9"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Called when the page is loaded</span></li>
<li class="L0"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln">&nbsp;init</span><span class="pun">(){</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// get the video element using the DOM api</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp; &nbsp; myVideo&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L3"><span class="pln"></span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Define a callback function called each time a video ends</span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp; &nbsp; myVideo</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'ended'</span><span class="pun">,</span><span class="pln">&nbsp;loadAndplayNextVideo</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L6"><span class="pln"></span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Load the first video when the page is loaded.</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; loadNextVideo</span><span class="pun">();</span></li>
<li class="L9"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0"><span class="tag">&lt;/script&gt;</span></li>
<li class="L1"><span class="tag">&lt;/head&gt;</span></li>
<li class="L2"><span class="tag">&lt;body</span><span class="pln">&nbsp;</span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;video</span><span class="pln">&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln">&nbsp;</span><span class="atn">controls</span><span class="tag">&gt;</span>&lt;/video&gt;</li>
<li class="L6"><span class="tag">&lt;/body&gt;</span></li>
<li class="L7"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

+ _Line 8_: the JavaScript array that contains the URLs of the videos in the playlist. In this example, we've only got two of them, but if the array is larger the example will still work.
+ _Line 42_: When the page is loaded, an `init()` function is called.
+ _Lines 32 - 38_: we used the DOM to get the JavaScript object corresponding to the video element, then defined a listener for the ended event. Each time a video ends, the `loadAndPlayNextVideo()` callback will be called. As the video element has no src attribute by default, we also preload the first video (call to `loadNextVideo()` at line 38).
+ _Lines 16 - 20_: the `loadNextVideo()` function uses a variable called `currentVideo` that corresponds to the index of the current video. By setting `myVideo.src = sources [currentVideo % sources.length]`, we set the src of the video element to sources[0], then to sources[1], and as we increment the `currentVideo` index each time (_line 19_). If it becomes greater than 1, the modulo (the "%" symbol is the modulo in JavaScript) will make it "loop" between 0 and the number of videos in the playlist. In other words, when the last video ends, it starts back at the first one.


#### Notes for 3.3.3 Examples using the JavaScript API

+ Examples for Media API
  + [control w/ external buttons](src/03c-example04.html)
    + video and source element

      ```js
      <video id="vid" controls>
      <source src=https://html5doctor.com/demos/video-canvas-magic/video.webm
              type=video/webm>
      ...
      </video>
      ```

    + play button: `<button onclick="playVideo();" style="cursor: pointer;">Play</button>`
    + pause button: `<button onclick="pauseVideo();" style="cursor: pointer;">Pause</button>`
    + rewind button: `<button onclick="rewindVideo();" style="cursor: pointer;">Back to beginning</button>`
    + accessing video element: `var vid = document.querySelector("#vid");`
    + play JS code: `function playVideo() { vid.play(); }`
    + pause JS code: `function pauseVideo() { vid.pause(); }`
    + rewind JS code: `function rewindVideo() { vid.currentTime = 0; }`
  + playing multiple videos sequentially
    + add event listener for video end: `vid.addEventListener('ended', playNextVideo, false);`
    + action for playing next video: `function playNextVideo(e) {...}`
  + [managing playlists](src/03c-example05.html)
    + video element: `<video id="myVideo" controls></video>`
    + initializing JS after page loaded: `function init() {...}`
      + access video element: `myVideo = document.querySelector("#myVideo");`
      + add video end listener: `myVideo.addEventListener('ended', loadAndplayNextVideo, false);`
      + load the first video first time, not playing until play clicked in control panel: `loadNextVideo();`
    + array of videos: `var sources = ["video1.mp4", "video2.mp4"];`
    + loading the next video to play repeatedly: `function loadNextVideo() { myVideo.src = sources[currentVideo % sources.length] myVideo.load();currentVideo++; }`
    + load and play next video (callback): `function loadAndplayNextVideo() { console.log("playing " + sources[currentVideo % sources.length]) loadNextVideo(); myVideo.play(); }`


### 3.3.4 Using the Webcam

It's very easy to use the `getUserMedia` API for accessing the WebCam. 

Here is a version that should work on any recent browser except Apple Safari (which still does not support this API). Note that for security reasons you must host your HTML/CSS/JS page on an HTTPS server for `getUserMedia` to work.

<span style="color: brown; font-weight: bold;">For security reason, these examples cannot run in the course web pages. Click on "Edit on CodePen" to run them.</span>

__First version that uses callbacks (success/error, see the JS code):__

[CodePen Demo](https://codepen.io/w3devcampus/pen/OpYNBE)

[Local Demo](src/03c-example06.html)


__Second version that uses a new JavaScript syntax called "promises":__

This is another way of saying, "Please, browser, try to give me access to the WebCam, __THEN__ when the Webcam is ready, please tell me so that I can display its stream in a `<video>` element". 

[CodePen Demo](https://codepen.io/w3devcampus/pen/EWzKrK)

[Local Demo](src/03c-example07.html)


#### Notes for 3.3.4 Using the Webcam

+ Accessing Webcam
  + using `getUserMedia` API for accessing the WebCam
  + example: [callback function](src/03c-example06.html)
    + video element: `<video width=200 height=200 id="video" controls autoplay>`
    + preferred camera resolution: `var constraints = { audio: true, video: { width: 1280, height: 720 } };`
    + callback function

      ```js
      navigator.mediaDevices.getUserMedia(constraints)
      .then(function(mediaStream) {
        var video = document.querySelector('video');
        video.srcObject = mediaStream;
        video.onloadedmetadata = function(e) {
          video.play();
        };
      })
      .catch(function(err) { console.log(err.name + ": " + err.message); });
      ```

  + example: [promises - after DOM ready](src/03c-example07.html)
    + init after DOM ready: `window.onload = init;`
    + raise error message:

      ```js
      function init() {
        navigator.mediaDevices.getUserMedia({audio: true,video: true})
          .then(function (stream) {
              var video = document.querySelector('#video');
              video.srcObject = stream;
              video.play();
          })
          .catch(function(err) {
              alert("something went wrong: " + err)
        });
      }
      ```

#### Knowledge check 3.3.3

1. What is `getUserMedia`?

  a. A JavaScript API that can be used to redirect the webcam video stream to a video element<br>
  b. An API which only works with WebRTC for audio conferencing<br>
  c. An upcoming API that is not available yet on browsers, but can be emulated by the video element<br>
  
  Ans: a<br>
  Explanation: `getUserMedia` is part of the `WebRTC` specification, but it's related to the `<video>` element too. Indeed, it can be used to redirect the webcam video stream to a `<video>` element. If this element has the autoplay attribute, it will display the video stream as soon as it is available.


### 3.3.5 Extended examples

In this section, we propose a few examples that use more JavaScript and more complex CSS manipulation. They might be a little hard to understand if you are a JavaScript beginner, but don't be afraid to try and test them, look at the code, etc.

Some examples are given "as is", such as the custom video player that uses SVG (at the end of the page); if you are interested, you may view the code. 

#### Player with CSS transformation

__Example #1: a player showing the use of every type of CSS3 transformation__

Please see this example online, originally written by [Chris Heilmann](https://christianheilmann.com/), and tuned by us ;).

[JS Bin Demo](https://jsbin.com/vaqulep/edit?html,css,output)

[Local Demo](src/03c-example08.html)

Don't forget to click the JavaScript and CSS tabs in JS Bin in order to display the JavaScript code that creates the buttons on the right of the video, and the CSS that processes the different clicks and applies CSS3 transforms.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/1uobo1ta')"
    src    ="https://tinyurl.com/2p6zs9ns"
    alt    ="Snapshoot of HTML5 video w/ CSS transformation"
    title  ="Snapshoot of HTML5 video w/ CSS transformation"
  />
</figure>

This example shows a lot:

+ It uses the HTML5 elements `<nav>`, `<footer>`, `<header>`.
+ It shows the use of CSS3 2D transformations (scale, translate, and rotate).
+ It shows how to handle DOM events using JavaScript and how to modify CSS properties of the `<video>` element from JavaScript.


#### Display events and properties

__Example #2: how to track all possible events and manipulate many properties__

This example also shows how to handle failures. See the code and play with this example online.

[JS Bin Demo](https://jsbin.com/becaref/3/edit?html,output)

[Local Demo](src/03c-example09.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/1uobo1ta')"
    src    ="https://tinyurl.com/ie7k1cq6"
    alt    ="Snapshoot of HTML5 video w/ time elasped"
    title  ="Snapshoot of HTML5 video w/ time elasped"
  />
</figure>


Here is an example of a piece of code for handling errors during video playback:

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="pun">...</span></li>
<li class="L1"><span class="pln"></span></li>
<li class="L2"><span class="pln">vid</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'error'</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span><span class="pln"></span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp; logEvent</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">,</span><span class="str">'red'</span><span class="pun">);</span><span class="pln"></span></li>
<li class="L2"><span class="pun">},</span><span class="pln">&nbsp;</span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L3"><span class="pln"></span></li>
<li class="L4"><span class="pun">...</span></li>
<li class="L5"><span class="pln"></span></li>
<li class="L6"><span class="kwd">function</span><span class="pln">&nbsp;logEvent</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">,</span><span class="pln">&nbsp;color</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L6"><span class="kwd">&nbsp; &nbsp; switch</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">.</span><span class="pln">type</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">...</span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln">&nbsp;</span><span class="str">'error'</span><span class="pun">:</span><span class="pln"></span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;error&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">).</span><span class="pln">error</span><span class="pun">;</span></li>
<li class="L2"><span class="pln"></span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">switch</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">error</span><span class="pun">.</span><span class="pln">code</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln">&nbsp;error</span><span class="pun">.</span><span class="pln">MEDIA_ERR_ABORTED</span><span class="pun">:</span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span class="pun">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"fetching aborted at the user's request"</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln">&nbsp;error</span><span class="pun">.</span><span class="pln">MEDIA_ERR_NETWORK</span><span class="pun">:</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span class="pun">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"a network error caused the browser to stop fetching the media"</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln">&nbsp;error</span><span class="pun">.</span><span class="pln">MEDIA_ERR_DECODE</span><span class="pun">:</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span class="pun">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"an error occurred while decoding the media"</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln">&nbsp;error</span><span class="pun">.</span><span class="pln">MEDIA_ERR_SRC_NOT_SUPPORTED</span><span class="pun">:</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span class="pun">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"the media indicated by the src</span></li>
<li class="L4"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; attribute was not suitable"</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">default</span><span class="pun">:</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span class="pun">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="str">"an error occurred"</span><span class="pun">;</span><span class="pln"></span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1"><span class="pln">&nbsp;</span><span class="pun">...</span></li>
<li class="L1">}</li>
</ol></div>


#### Buffering status

__Example #3: how to display a percentage of buffering when using a slow connection__

See the example online here too.

[JS Bin Demo](https://jsbin.com/xororol/3/edit?html,output)

[Local Demo](src/03c-example10.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/1uobo1ta')"
    src    ="https://tinyurl.com/2mxcvzx3"
    alt    ="how to display the percentage of buffering"
    title  ="how to display the percentage of buffering"
  />
</figure>


Note that on mobile phones, the video does not start until the user presses the play control or clicks on the video picture. Using the "`canplaythrough`" event is a trick to call a function that starts the video player as soon as the page is loaded on desktop. This event is not supported by mobile devices, so if you try this example on a mobile, the video will not start automatically.

As explained by the [Apple Developer Web site](http://developer.apple.com/):  "The `buffered` property is a `TimeRanges` object: an array of start and stop times, not a single value. Consider what happens if the person watching the media uses the time scrubber to jump forward to a point in the movie that hasn’t loaded yet—the movie stops loading and jumps forward to the new point in time, then starts buffering again from there. So the `buffered` property can contain an array of discontinuous ranges. The example simply seeks the end of the array and reads the last value, so it actually shows the percentage into the movie duration for which there is data. "

<div class="source-code"><ol class="linenums">
<li class="L0" value="1"><span class="dec">&lt;!doctype html&gt;</span></li>
<li class="L1"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2"><span class="tag">&nbsp; &lt;head&gt;</span></li>
<li class="L3"><span class="tag">&nbsp; &nbsp; &lt;title&gt;</span><span class="pln">JavaScript Progress Monitor</span><span class="tag">&lt;/title&gt;</span><span class="pln"></span></li>
<li class="L4"><span class="pln">&nbsp;&nbsp;&nbsp; &lt;meta charset="utf-8"/&gt;<br></span></li>
<li class="L5"><span class="tag">&nbsp; &nbsp; &lt;script</span><span class="tag">&gt;</span></li>
<li class="L6"><span class="kwd">&nbsp; &nbsp; &nbsp; function</span><span class="pln">&nbsp;getPercentProg</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;myVideo&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">getElementsByTagName</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">)[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;endBuf&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;myVideo</span><span class="pun">.</span><span class="pln">buffered</span><span class="pun">.</span><span class="pln">end</span><span class="pun">(</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;soFar&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;parseInt</span><span class="pun">(((</span><span class="pln">endBuf&nbsp;</span><span class="pun">/</span><span class="pln">&nbsp;myVideo</span><span class="pun">.</span><span class="pln">duration</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">*</span><span class="pln">&nbsp;</span><span class="lit">100</span><span class="pun">));</span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"loadStatus"</span><span class="pun">).</span><span class="pln">innerHTML&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;soFar&nbsp;</span><span class="pun">+</span><span class="pln">&nbsp;</span><span class="str">'%'</span><span class="pun">;</span></li>
<li class="L1"><span class="pun">&nbsp; &nbsp; &nbsp; }</span></li>
<li class="L2"><span class="pln"></span></li>
<li class="L3"><span class="com">&nbsp; &nbsp; &nbsp; // Will be called as soon as the page is ready on desktop computer,</span></li>
<li class="L4"><span class="com">&nbsp; &nbsp; &nbsp; // Only when a user clicks on play control or image on mobile</span></li>
<li class="L5"><span class="kwd">&nbsp; &nbsp; &nbsp; function</span><span class="pln">&nbsp;myAutoPlay</span><span class="pun">()</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L5"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;myVideo&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">getElementsByTagName</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">)[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVideo</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L9"><span class="pun">&nbsp; &nbsp; &nbsp; }</span></li>
<li class="L9"><span class="kwd"></span></li>
<li class="L9"><span class="kwd">&nbsp; &nbsp; &nbsp; function</span><span class="pln">&nbsp;addMyListeners</span><span class="pun">(){</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;myVideo&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;document</span><span class="pun">.</span><span class="pln">getElementsByTagName</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">)[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L4"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVideo</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'progress'</span><span class="pun">,</span><span class="pln">&nbsp;getPercentProg</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5"><span class="pln"></span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Calls autoplay only if the device is adapted</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVideo</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'canplaythrough'</span><span class="pun">,</span><span class="pln">&nbsp;myAutoPlay</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="kwd">false</span><span class="pun">);</span><span class="pln"></span></li>
<li class="L8"><span class="pun">&nbsp; &nbsp; &nbsp; }</span></li>
<li class="L9"><span class="tag">&nbsp; &lt;/script&gt;</span></li>
<li class="L0"><span class="tag">&lt;/head&gt;</span></li>
<li class="L0"><span class="tag">&lt;body</span><span class="pln">&nbsp;</span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">addMyListeners</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L0"><span class="tag">&nbsp; &nbsp; &lt;h1&gt;</span><span class="pln">Check progression of buffering before playing a movie. Useful withy</span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; slow&nbsp;</span><span class="pln">connexion (3G, etc.)</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L6"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;div&gt;</span></li>
<li class="L7"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;video</span><span class="pln">&nbsp;</span><span class="atn">controls</span><span class="tag">&gt;</span></li>
<li class="L8"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">https://html5doctor.com/demos/video-canvas-magic/video.webm</span><span class="pln"></span></li>
<li class="L8"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">video/webm</span><span class="tag">&gt;</span><span class="pln"></span></li>
<li class="L9"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">https://html5doctor.com/demos/video-canvas-magic/video.ogg</span><span class="pln">&nbsp;&nbsp;</span></li>
<li class="L9"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">video/ogg</span><span class="tag">&gt;</span><span class="pln"></span></li>
<li class="L0"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">https://html5doctor.com/demos/video-canvas-magic/video.mp4</span><span class="pln"></span></li>
<li class="L0"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">video/mp4</span><span class="tag">&gt;</span><span class="pln"></span></li>
<li class="L1"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/video&gt;</span></li>
<li class="L2"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;p</span><span class="pln">&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"loadStatus"</span><span class="tag">&gt;</span><span class="pln">Buffering...</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L3"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L4"><span class="tag">&lt;/body&gt;</span></li>
<li class="L5"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


#### Control with SVG element

__Example #4: how to use SVG elements as external controllers__

This is the ultimate way of doing a real custom player: redesign your own controls using SVG shapes! This example (try it [online](https://www.w3.org/2010/Talks/0430-www2010-plh/video-player.xhtml)) is given "as is" for those of you who may be curious.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/1uobo1ta')"
    src    ="https://tinyurl.com/my4r5nli"
    alt    ="Snapshot of HTML5/SVG video player"
    title  ="Snapshot of HTML5/SVG video player"
  />
</figure>

#### Customized video player

__Example #5: a custom video player written by a previous student__

This is more an example than a tutorial. Maurice, a student who followed the precursor version of this MOOC, had the assignment to write a custom video player with playlist, video thumbnails, custom play/pause/next/previous/volume controls, and present it in a Web page that used a nice layout based on the new structuring elements seen during Week 1.

Here is the online example on JS Bin, by Maurice Buiten. We recommend that you look at the source code.

[JS Bin Demo](https://jsbin.com/noqubut/4/edit?html,js,output)

[Local Demo](src/03c-example11.html)


Screenshot:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/1uobo1ta')"
    src    ="https://tinyurl.com/1ia3vzr4"
    alt    ="a custom video player in a nice presented html page"
    title  ="a custom video player in a nice presented html page"
  />
</figure>


#### Notes for 3.3.5 Extended examples

+ Examples:
  + [player w/ CSS transformation](src/03c-example08.html)
    + elements in HTML: `nav`, `video`, `header` and `footer`
      + `<video>` element within `<div>` w/ `id = 'stage'`
      + a `<div>` element w/ `id = 'controls'` to display the buttones for transformation
      + the buttons created by JS code
    + global variables for DOM elements by `getEleemntById()` and `getElementByTagName()`: `stage`, `v` (video), and `controls`
    + array for possible setting for transformation ans set default one: `var properties = ['transform', 'WebkitTransform', 'MozTransform', 'msTransform', 'OTransform'], prop = properties[0];`
    + find the properties browser support:

      ```js
      for (var i=0,j=properties.length;i<j;i++) {
        if (typeof stage.style[properties[i]] !== 'undefined') {
          prop = properties[i];
          break;
        }
      }
      ```

    + create control buttons w/ `controls.innerHTML`: `controls.innerHTML =  '<button class="play">play</button>'+ '<div id="change">' + '<button class="zoomin">+</button>' + '<button class="zoomout">-</button>' + ...`
    + add event listener and switch to related cases: `controls.addEventListener('click', function(e) {...}`
      + identify which button clicked: `t = e.target; if(t.nodeName.toLowerCase() === 'button'){ switch(t.className) {...}}`
      + play/pause button toggle btw play and pause: `case 'play': if(v.paused) { v.play(); t.innerHTML = 'pause'; } else { v.pause(); t.innerHTML = 'play'; } break;`
      + zoom in/out buttons:  `case 'zoomin': zoom = zoom + 0.1; v.style[prop] = 'scale('+zoom+') rotate('+rotate+'deg)'; break;`
      + rotate right/left buttons: `case 'rotateleft': rotate = rotate + 5; v.style[prop] = 'rotate('+rotate+'deg) scale('+zoom+')'; break;`
      + shitf buttons: `case 'left': v.style.left = (parseInt(v.style.left,10) - 5) + 'px'; break;`
      + reset buttons: `case 'reset': zoom = 1; rotate = 0; v.style.top = 0 + 'px'; v.style.left = 0 + 'px'; v.style[prop]='rotate('+rotate+'deg) scale('+zoom+')'; break;`
    + error handling for default: `e.preventDefault();`
  + [display events and properties](src/03c-example09.html)
    + control the display of notes: `<div id="notes"></div>`
    + the event logs: `<div id="eventslog"></div>`
    + add event listener: `vid.addEventListener('loadstart', function(evt) { logEvent(evt,'#000099'); }, false); ...`
    + toggle notes in JS: `function toggleNotes() {...}`
      + access element: `var notes = document.getElementsByClassName('note');`
      + variable to control display: `var isShowing = parseInt(window.getComputedStyle(notes[0],null).getPropertyValue("opacity"));`
      + loop through the notes: `for (var i = 0; i < notes.length; i++) { notes[i].style.opacity = isShowing ? 0 : 1; }`
      + toggle text to "Show Notes" or "Hide Notes": `document.getElementById('notes').className = isShowing ? 'off' : 'on';`
    + callback triggered by the event listener: `function logEvent(evt, color) {...}`
      + current event info: `log.innerHTML = evt.type; log.style.color = color;`
      + create container for the log and check the displaying status: `var note = document.createElement("span"); note.setAttribute('class', 'note'); note.style.opacity = document.getElementById('notes').className == 'on' ? '1' : '0';`
      + add note description of each event with switch cases: `switch (evt.type) { case 'loadstart': note.innerHTML = "begin loading media data"; break; ...; case 'error': ...}`
      + error handler w/ `case 'error'`: `var error = document.querySelector('video').error; switch (error.code) {...}`
        + media error: `case error.MEDIA_ERR_ABORTED: note.innerHTML = "fetching aborted at the user's request"; break;`
        + network error: `case error.MEDIA_ERR_NETWORK: note.innerHTML = "a network error caused the browser to stop fetching the media";  break;`
        + deccoding error: `case error.MEDIA_ERR_DECODE: note.innerHTML = "an error occurred while decoding the media";  break;`
        + unsupport error: `case error.MEDIA_ERR_SRC_NOT_SUPPORTED: note.innerHTML = "the media indicated by the src attribute was not suitable";  break;`
        + unspecified error: `default: note.innerHTML = "an error occurred"; break;`
      + create log and append to event log: `log.appendChild(note); var eventslog = document.getElementById('eventslog'); eventslog.insertBefore(log, eventslog.firstChild);`
  + [buffering status](src/03c-example10.html)
    + `canplaythrough` event: a trick to call a function that starts the video player as soon as the page is loaded on desktop
    + `buffered` property:
      + a `TimeRanges` object
      + an array of start and stop times, not a single value
      + able to contain an array of discountinuous ranges, e.g., jump to a certain point of video and play
    + contaimner to display the status: `<p id="loadStatus">MOVIE LOADING...</p>`
    + addd event listener for `<video>` element: `function addMyListeners(){ ...}`
      + listening `progress` event: `myVideo.addEventListener('progress', getPercentProg, false);`
      + listening `canplaythrough` event: `myVideo.addEventListener('canplaythrough', myAutoPlay, false);`
    + callback to calculate rthe percentage of video loaded: `function getPercentProg() {...}`
      + access `<video>` element: `var myVideo = document.getElementsByTagName('video')[0];`
      + video loaded so far in time unit: `var endBuf = myVideo.buffered.end(0);`
      + calculate the percentage of video loaded: `var soFar = parseInt(((endBuf / myVideo.duration) * 100));`
      + display the percentag: `document.getElementById("loadStatus").innerHTML =  soFar + '%';`
    + callback to play video: ` function myAutoPlay() {...}`
      + access `<video>` element: `var myVideo = document.getElementsByTagName('video')[0];`
      + play video: `myVideo.play();`
  + [customized player](src/03c-example11.html)
    + structure design w/ `<main>`, `<section>`, `<aside>`, `<article>`, `<header>`, `<footer>`
    + video player, buttons, and thumbnails within `<div class="player">` container inside `<section>`
      + video player: `<video id="myVideo" preload width="640" height="360"> <source src="https://mainline.i3s.unice.fr/mooc/mi5.mp4" /> </video>`
      + buttons container: `<div> ... </div>`
      + play button: `<button type="button" id="pl">Play</button>`
      + previous clip button: `<button type="button" id="pr">Previous</button>`
      + slider for video progress: `<input id="slide" type="range" value="0" />`
      + next clip button: `<button type="button" id="nx">Next</button>`
      + volume buttons: `<button type="button"> <span id="volDown">- &nbsp; </span>Vol<span id="volUp"> &nbsp; +</span></button>`
      + container for thumbernails: `<div class="thumbs"> <img id="vid1" src="http://i.imgur.com/y6RTkIi.gif" width="128" height="72" alt="video 1"> ...`
    + add global variables to access various elements and array of sources of video clips
    + add event listeners
      + play button: `pl.addEventListener("click", playPause, false);`
      + preious clip: `pr.addEventListener("click", prevVid, false);`
      + click to pause/play video: `seek.addEventListener("mousedown", function () { myVid.pause(); pl.innerHTML = "Play"; }); seek.addEventListener("mouseup", function () { myVid.play(); pl.innerHTML = "Pause"; });`
      + video progress slider event: `seek.addEventListener("input", vidSeek, false);`
      + timeupdate event: `myVid.addEventListener("timeupdate", vidTime, false);`
      + video end: `myVid.addEventListener("ended", nextVid, false);`
      + next video button: `nx.addEventListener("click", nextVid, false);`
      + volume up button: `volDown.addEventListener("mousedown", volChangeDown, false);`
      + volume down button: `volUp.addEventListener("mousedown", volChangeUp, false);`
      + clip 1 thumbernail: `vid1.addEventListener("click", vidChoice1);`
      + clip 2 thumbernail: `vid2.addEventListener("click", vidChoice2);`
      + clip 3 thumbernail: `vid3.addEventListener("click", vidChoice3);`
    + [callback function](src/js/03c-example11.js)


### 3.3.6 Discussion and projects

Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ This might be useful: find [free videos](https://download.blender.org/peach/bigbuckbunny_movies/)
+ Hosting videos is complicated when you want to use them with CodePen or JsBin, do you have some tips to share with others? For this course, we run our own private HTTP server... We are speaking about files that can be used with the `<video>` element directly, not on YouTube, DailyMotion, etc.
+ What tool do you use for encoding your audio and video files?


#### Optional projects

##### Project #1: a custom video player

Here are a few ideas to play with the material learned in this section. Your classmates and the team who prepared the course will be happy to look at them and give feedback. Please post URLs of your work in this discussion forum. These projects are optional, meaning that they won't be graded.

Try to write a video  player with a few custom buttons for play/stop/etc. When your custom player is done, please add a way to play several videos one after another (what we call a playlist), etc.

Examples that can help you, created by students of earlier versions of this MOOC:

+ [A custom player with nice CSS and buttons](https://jsbin.com/mayugik/1/edit?html,css,output)
+ [Custom players with a small playlist composed of three songs by Queen](https://jsbin.com/vefiniq/7/edit?html,output)
+ [AWESOME custom player created by GeorgianaB, with playlist, progress bar, CSS3 animations, etc.](https://codepen.io/w3devcampus/pen/reQbow)


##### Project #2: a video quiz!

Create a quiz based on videos - here is a proposed story telling:

+ a video is playing, then it stops at a given time, and you display a question such as: "who is this actor?" followed by some radio buttons + a proposal (see what we do with quizzes in this course): "Leonardo Di Caprio" or "Harisson Ford"?
+ Once the question is answered, you display "Correct" or "Incorrect"
+ Then the video continues....
+ When the video ends, please show the final score. 

_A few hints:_

1. Use an array with stop times, for example `let stopTimes = [5, 10, 20]`. This will mean "the video should stop at currentTime = 5, currentTime = 10, currentTime = 20". 
2. You will use a `timeupdate` event listener on the video, like in the example from the live coding video, and the `pause`, `play` and `stop` methods from the video element JavaScript API. And also an `ended` event listener for detecting the end of the video.
3. Start from one of the example in the course (the one from the live coding video): try to make the video stop at 5s ,for example, and then display a question, and a "continue" button. When the button is pressed, the video goes on and stops a bit further, etc.
4. When this works (the video plays, then stops, you click, it continues, etc.), try to turn the displayed sentence into a quiz: add HTML radio buttons, and when you click the continue button, you will validate the answer, show "correct" or "incorrect", and maybe increment the score.
5. Feel free to add any feature(s) you'd like.

As always, do not forget to post the URL of your work in the forum so that we can enjoy your creation. Michel will inevitably give you his advice(s), and also tell you that you are the best ;))


<hr>

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

