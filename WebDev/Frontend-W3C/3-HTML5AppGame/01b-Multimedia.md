# Module 1: Advanced HTML5 multimedia section


## 1.2 The Timed Text Track API


### 1.2.1 The Timed Text Track API

#### Contents

In the [W3Cx HTML5 Coding Essentials and Best Practices](https://bit.ly/3we2vSS) course, we saw that `<video>` and `<audio>` elements can have `<track>` elements. A `<track>` can have a `label`, a `kind` (subtitles, captions, chapters, metadata, etc.), a language (`srclang` attribute), a source URL (`src` attribute), etc.

Here is a small example of a video with 3 different tracks ("......" masks the real URL here, as it is too long to fit in this page width!):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://...../elephants-dream-medium.mp4"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun">=</span><span class="atv">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"</span><span class="pln"></span><span class="tag">&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"de"</span><span class="pln"> </span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun">=</span><span class="atv">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt"</span><span class="pln"> </span><span class="atn">default</span><span class="tag">&gt;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun">=</span><span class="atv">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"</span><span class="tag">&gt;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span></li>
</ol></div>

And here is how it renders in your current browser (please play the video and try to show/hide the subtitles/captions):

<video id="myVideo" preload="metadata" controls="controls" crossorigin="anonymous"> 
  <source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.mp4" type="video/mp4"> 
  <source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.webm" type="video/webm"> 
  
  <track kind="subtitles" src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-en.vtt" srclang="en" label="English subtitles"> 
  <track kind="subtitles" src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-de.vtt" srclang="de" label="Deutsch subtitles" default=""> 
  <track kind="chapters" src="https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en.vtt" srclang="en" label="English chapters"> 
</video>

Notice that the support for multiple tracks may differs significantly from one browser to another, in particular if you are using old versions. Here is a quick summary (as in May 2020).

+ Safari provides a menu  you can use to choose which subtitle/caption track to display. If one of the defined text tracks has the default attribute set, then it is loaded by default. Otherwise, the default is off.

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
      onclick= "window.open('https://bit.ly/3v0DqL4')"
      src    = "https://bit.ly/3v0Yxg3"
      alt    = "screenshot of safari menu fr choosing subtitle track"
      title  = "screenshot of safari menu fr choosing subtitle track"
    />
  </figure>

+ Chrome and Opera both provide a subtitle menu and load the text track set that matches the browser language. If none of the available text tracks match the browser’s language, then it loads the track with the default attribute, if there is one. Otherwise, it loads none. Let's say that support is very incomplete (!).
+ Firefox provides also a subtitle menu but will show the first defined text track only if it has default set. It will load all tracks in memory as soon as the page is loaded.

Also there is [a Timed Text Track API in the HTML5/HTML5.1 specification](https://bit.ly/33RJsl8) that enables us to manipulate `<track>` contents from JavaScript. Do you recall that text tracks are associated with WebVTT files? As a quick reminder, let's look at a WebVTT file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="lit">1</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">15.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">18.000</span><span class="pln"> align</span><span class="pun">:</span><span class="pln">start</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Proog</span><span class="pun">&gt;</span><span class="typ">On</span><span class="pln"> the left we can see</span><span class="pun">...&lt;/</span><span class="pln">v</span><span class="pun">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="lit">2</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">18.167</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">20.083</span><span class="pln"> align</span><span class="pun">:</span><span class="pln">middle</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Proog</span><span class="pun">&gt;</span><span class="typ">On</span><span class="pln"> the right we can see the</span><span class="pun">...&lt;/</span><span class="pln">v</span><span class="pun">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">3</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">20.083</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">22.000</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Proog</span><span class="pun">&gt;...</span><span class="pln">the </span><span class="pun">&lt;</span><span class="pln">c</span><span class="pun">.</span><span class="pln">highlight</span><span class="pun">&gt;</span><span class="pln">head</span><span class="pun">-</span><span class="pln">snarlers</span><span class="pun">&lt;</span><span class="str">/c&gt;&lt;/</span><span class="pln">v</span><span class="pun">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">4</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">22.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">24.417</span><span class="pln"> align</span><span class="pun">:</span><span class="kwd">end</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Proog</span><span class="pun">&gt;</span><span class="typ">Everything</span><span class="pln"> </span><span class="kwd">is</span><span class="pln"> safe</span><span class="pun">.</span><span class="pln"> </span><span class="typ">Perfectly</span><span class="pln"> safe</span><span class="pun">.&lt;/</span><span class="pln">v</span><span class="pun">&gt;</span></li>
</ol></div>

The different time segments are called "cues" and each cue has an id (1, 2, 3 and 4 in the above example), a startTime and an endTime, and a text content that can contain HTML tags for styling (`<b>`, etc...) or be associated with a "voice" as in the above example. In this case, the text content is wrapped inside `<v name_of_speaker>...</v>` elements.

It's now time to look at the JavaScript API for manipulating tracks, cues, and events associated with their life cycle. In the following lessons, we will look at different examples which use this API to implement missing features such as:

+ how to  build a menu for choosing the subtitle track language to display,
+ how to display a synchronized description of a video (useful for disabled people, for example),
+ how to display a clickable transcript aside the video (similar to what the edX video player does),
+ how to show chapters,
+ how to use JSON encoded cue contents (useful for showing external resources in the HTML document while a video is playing),
etc.


#### Live coding video: intro to the Timed Text Track API

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2S2MEIa)


#### Knowledge check 1.2.1

1. Do the most recent versions of all major browsers provide a menu for choosing the subtitle or the caption track? (Yes/No)

  Ans: No<br>
  Explanation: Unfortunately, support currently varies from one browser to another. Only Safari, IE and Microsoft Edge provide a menu to choose the subtitle or caption track. These missing features can be added, however, using the Timed Text Track API.


#### Notes for 1.2.1 The Timed Text Track API

+ `<track>` element
  + typically within `<video>` and `<audio>` elements
  + attributes
    + `label`
    + `kind`: subtitle, captions, chapters, matadata, etc.
    + `srclang`: language
    + `src`: a source URL
    + ...
  + example

    ```html
    <video id="myVideo" preload="metadata" controls crossOrigin="anonymous">
        <source src="https://...../elephants-dream-medium.mp4" type="video/mp4">
        <source src="https://...../elephants-dream-medium.webm" type="video/webm">
        <track label="English subtitles" kind="subtitles" srclang="en"
              src="https://...../elephants-dream-subtitles-en.vtt">
        <track label="Deutsch subtitles" kind="subtitles" srclang="de"
              src="https://...../elephants-dream-subtitles-de.vtt" default>
        <track label="English chapters" kind="chapters" srclang="en"
              src="https://...../elephants-dream-chapters-en.vtt">
    </video>
    ```

+ Multiple tracks support
  + supporting for multiple tracks probably different significantly btw browsers (May 2020)
  + Safari
    + providing a menu to choose which subtitle/track to display
    + `default` attribute: loading the text track by default
  + Chrome & Opera
    + providing a subtitle menu
    + loading the text track which matches the browser's language if existed
    + none loaded if no matching
  + Firefox
    + providing a subtitle menu
    + displaying the first defined text track only if the `default` set
    + loading all tracks in memory as page loaded

+ WebVTT text racks
  + [document](https://bit.ly/33RJsl8) in HTML5/HTML5.1 specification
  + enabling to manipulate `<track>` contents from JavaScript
  + cue:
    + element w/ an `id`, a starTime, and an endTime
    + text content: containing HTML tags for styling or associated w/ a "voice"
    + voice element: `<v name_of_speaker> ... </v>`
  + example

    ```s
    WEBVTT

    1
    00:00:15.000 --> 00:00:18.000 align:start
    <v Proog>On the left we can see...</v>

    2
    00:00:18.167 --> 00:00:20.083 align:middle
    <v Proog>On the right we can see the...</v>

    3
    00:00:20.083 --> 00:00:22.000
    <v Proog>...the <c.highlight>head-snarlers</c></v>

    4
    00:00:22.000 --> 00:00:24.417 align:end
    <v Proog>Everything is safe. Perfectly safe.</v>
    remote controller with subtitles button
    ```


### 1.2.2 The HTML track element

#### Live coding video: HTML Track element

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/33TXcvF)


#### Example: `<track>`

Let's go back to our example. Below is the HTML code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag" style="color: #008888;">&lt;video</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">id</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"myVideo"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">preload</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"metadata"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">controls</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">crossOrigin</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"anonymous"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag" style="color: #008888;">&lt;source</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"https://...../elephants-dream-medium.mp4"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">type</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"video/mp4"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag" style="color: #008888;">&lt;source</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">type</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"video/webm"</span><span class="tag" style="color: #008888;">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="tag" style="color: #008888;">&lt;track</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">label</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"English subtitles"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">kind</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"subtitles"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">srclang</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"en"</span><span class="pln"></span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="atn" style="color: #aa0066;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"</span><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag" style="color: #008888;">&lt;track</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">label</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"Deutsch subtitles"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">kind</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"subtitles"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">srclang</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"de"</span><span class="pln"></span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="atn" style="color: #aa0066;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">default</span><span class="tag" style="color: #008888;">&gt;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag" style="color: #008888;">&lt;track</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">label</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"English chapters"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">kind</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"chapters"</span><span class="pln">&nbsp;</span><span class="atn" style="color: #aa0066;">srclang</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"en"</span><span class="pln"></span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="atn" style="color: #aa0066;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun" style="color: #666600;">=</span><span class="atv" style="color: #008800;">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"</span><span class="tag" style="color: #008888;">&gt;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="tag" style="color: #008888;">&lt;/video&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag" style="color: #008888;"></span></li>
<li class="L6" style="margin-bottom: 0px;">&lt;div id="trackStatusesDiv"&gt;</li>
<li class="L6" style="margin-bottom: 0px;">&nbsp; &nbsp; &lt;h3&gt;HTML track descriptions&lt;/h3&gt;</li>
<li class="L6" style="margin-bottom: 0px;">&lt;/div&gt;</li>
</ol></div><br>

This example defines three `<track>` elements. From JavaScript, we can manipulate these elements as "HTML elements" - we will call them the "HTML views" of  tracks.


#### Status of an HTML track


Getting the status of an HTML track

[Example at JSBin that displays the different elements we can get from an HTML track:](https://jsbin.com/kuqevegapi/2/edit?html,css,output)

[Local Demo](src/01b-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3f00BPO')"
    src    = "https://bit.ly/3yojK5G"
    alt    = "An example of JSBin showing html track statuses"
    title  = "An example of JSBin showing html track statuses"
  />
</figure>

Here is the JavaScript source code:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;video</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;htmlTracks</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;trackStatusesDiv</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun" style="color: #666600;">.</span><span class="pln">onload&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666600;">()</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// called when the page has been loaded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#myVideo"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;trackStatusesDiv&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#trackStatusesDiv"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// Get the tracks as HTML elements</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;htmlTracks&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">querySelectorAll</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"track"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// displays their statuses in a div under the video</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;displayTrackStatuses</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTracks</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;displayTrackStatuses</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTracks</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">// displays track info</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">for</span><span class="pun" style="color: #666600;">(</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;i&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">;</span><span class="pln">&nbsp;i&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln">&nbsp;htmlTracks</span><span class="pun" style="color: #666600;">.</span><span class="pln">length</span><span class="pun" style="color: #666600;">;</span><span class="pln">&nbsp;i</span><span class="pun" style="color: #666600;">++)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;currentHtmlTrack&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;htmlTracks</span><span class="pun" style="color: #666600;">[</span><span class="pln">i</span><span class="pun" style="color: #666600;">];</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;label&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;li&gt;label = "</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;currentHtmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">label&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;/li&gt;"</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;kind&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;li&gt;kind = "</span><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;currentHtmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">kind&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;/li&gt;"</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;lang&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;li&gt;lang = "</span><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;currentHtmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">srclang&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;/li&gt;"</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;readyState&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;li&gt;readyState = "</span><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln">&nbsp;currentHtmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">readyState&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;/li&gt;"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;trackStatusesDiv</span><span class="pun" style="color: #666600;">.</span><span class="pln">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;li&gt;&lt;b&gt;Track:"</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;i&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">":&lt;/b&gt;&lt;/li&gt;"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;ul&gt;"</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;label&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;kind&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;lang&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;readyState&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"&lt;/ul&gt;"</span><span class="pun" style="color: #666600;">;</span><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun" style="color: #666600;">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div><br>

The code is rather straightforward:

+ We cannot access any HTML element before the page has been loaded. This is why we do all the work in the `window.onload` listener,
+ _Line 7_: we get a pointer to the div with `id=trackStatusesDiv`, that will be used to display track statuses,
+ _Line 10_: we get all the track elements in the document. They are HTML track elements,
+ _Line 13_: we call a function that will build some HTML to display the track status in the div we got from _line 7_.
+ _Lines 16-29_: we iterate on the HTML tracks, and for each track we get the `label`, the `kind` and the `srclang` attribute values. Notice, at _line 24_, the use of the `readyState` attribute, only used from JavaScript, that will give the current HTML track state.<br>
You can see on the screenshot (or [from the JSBin example](https://jsbin.com/higebo/1/edit?html,css,js,output)) that the German subtitle file has been loaded, and that none of the other tracks have been loaded.


#### Possible values for thw `readyState` attribute

Possible values for the `readyState` attribute of HTML tracks:

+ __0 = NONE__; the text track's cues have not been obtained
+ __1 = LOADING__; the text track is loading with no errors yet. Further cues can still be added to the track by the parser
+ __2 = LOADED__; the text track has been loaded with no errors
+ __3 = ERROR__; the text track was enabled, but when the user agent attempted to obtain it, something failed. Some or all of the cues are likely missing and will not be obtained

Now, it's time to look at the twin brother of an HTML track: the corresponding `TextTrack` object!


#### Knowledge check 1.2.2

1. When playing a video, are all tracks loaded by default?

  a. It depends on the browser<br>
  b. Yes<br>

  Ans: a<br>
  Explanation: In the given example, only the first track with the `default` attribute has been loaded. Try the example on different browsers and you will notice that only the track with the `default` attribute is loaded by the major browsers, when the page is loaded. FireFox will load all tracks, but will display the one with the `default` attribute only if it's the first one.

#### Notes for 1.2.2 The HTML track element

+ Status of an HTML track
  + JavaScript code to display `track` status
  + global variables: `var video, htmlTracks; var trackStatusesDiv;`
  + unable to access any HTML before page loaded: `window.onload = function() {...}`
    + access `<video>` element: `video = document.querySelector("#myVideo");`
    + access status of `<track>` element: `htmlStatusesDiv = document.querySelector("#trackStatusesDiv");`
    + access `<track>` element: `htmlTracks = document.querySelectorAll("track");`
    + display status: `displayTrackStatus(htmlTracks);`
  + display track status: `function displayTrackStatuses(htmlTracks) {...}`
    + iterate through tracks: `for (var i=0; i < htmlTracks.length; i++) {...}`
    + display info: `trackStatusesDiv.innerHTML += "<li><b>Track:" + i + ":</b></li>" + "<url>" + label + kind + lang + readyState + "</ul>"`

+ Values of `readyState` attribute
  + __0 = NONE__: the text track's cues not obtained
  + __1 = LOADING__: the text track loaded w/o errors yet, further cues able to be added to the track by the parser
  + __2 = LOADED__: the text track loaded w/o errors
  + __3 = ERROR__: the text track enabled but accessing failed, likely missing


### 1.2.3 The TextTrack object


#### Live coding video: the TextTrack object

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3ouTZfq)

The object that contains the cues (subtitles or captions or chapter description from the WebVTT file) is not the HTML track itself. It is another object that is associated with it: a `TextTrack` object!

The `TextTrack` JavaScript object has different methods and properties for manipulating track content, and is associated with different events. But before going into detail, let's see how to obtain a TextTrack object.


#### The `TextTrack` object

__Obtaining a `TextTrack` object that corresponds to an HTML track__

__First method: get a `TextTrack` from its associated HTML track__

The HTML track element has a track property which returns the associated `TextTrack` object. Example source code:

<div class="vert vert-1" data-id="block-v1:W3Cx+HTML5.2x+2T2020a+type@html+block@c3042a5fe70246e7883cbab78c032282">
        
<div class="xblock xblock-student_view xblock-student_view-html xmodule_display xmodule_HtmlBlock xblock-initialized" data-course-id="course-v1:W3Cx+HTML5.2x+2T2020a" data-init="XBlockToXModuleShim" data-runtime-class="LmsRuntime" data-runtime-version="1" data-block-type="html" data-usage-id="block-v1:W3Cx+HTML5.2x+2T2020a+type@html+block@c3042a5fe70246e7883cbab78c032282" data-request-token="d420d01cb8d211eb9f4be3e09222ae50" data-graded="False" data-has-score="False">
  
  <style type="text/css"><!--
@import url("/assets/courseware/v1/338ce1f184e47cf356abb3842b8dfe77/asset-v1:W3Cx+HTML5.2x+2T2020a+type@asset+block/syntaxhi.css");
.exampleHTML { border:1px solid black; margin:20px; padding: 20px; }
--></style>
<p>The object that contains the cues (subtitles or captions or chapter description from the WebVTT file) is not the HTML track itself. It is another object that is associated&nbsp;with it: a&nbsp;<span style="font-family: 'courier new', courier;">TextTrack</span>&nbsp;object!</p>
<p>The&nbsp;<span style="font-family: 'courier new', courier;">TextTrack</span> JavaScript object has different methods and properties for manipulating track <g class="gr_ gr_83 gr-alert gr_gramm gr_disable_anim_appear Punctuation only-del replaceWithoutSep" id="83" data-gr-id="83">content,</g> and is associated with different events. But before going into detail, let's see how to obtain a TextTrack object.</p>
<h3>Obtaining a <span style="font-family: courier new, courier;">TextTrack</span> object that corresponds to an HTML track</h3>
<h4>First method: get a&nbsp;<span style="font-family: 'courier new', courier;">TextTrack</span>&nbsp;from its associated HTML track</h4>
<p>The HTML track element has a <span style="font-family: 'courier new', courier;">track</span> property which returns the associated <span style="font-family: 'courier new', courier;">TextTrack</span> object. Example source code:</p>
<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com" style="color: #880000;">// HTML tracks</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;htmlTracks&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">querySelectorAll</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"track"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">// The TextTrack object associated&nbsp;with the first HTML track</span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;textTrack&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;htmlTracks</span><span class="pun" style="color: #666600;">[</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">].</span><span class="pln">track</span><span class="pun" style="color: #666600;">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">var kind = textTrack.kind;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">var label = textTrack.label;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span style="color: #666600;" color="#666600">var lang = textTrack.language;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span style="color: #666600;" color="#666600">// etc.</span></li>
</ol></div>
<p></p>
<p>Note that once we get a&nbsp;<span style="font-family: 'courier new', courier;">TextTrack</span>&nbsp;object, we can manipulate the&nbsp;<span style="font-family: 'courier new', courier;">kind</span>,&nbsp;<span style="font-family: 'courier new', courier;">label</span>,&nbsp;<span style="font-family: 'courier new', courier;">language</span>&nbsp;attributes (be careful, it's not&nbsp;<span style="font-family: 'courier new', courier;"><g class="gr_ gr_103 gr-alert gr_spell gr_disable_anim_appear ContextualSpelling ins-del multiReplace" id="103" data-gr-id="103">srclang</g></span>, like&nbsp;the equivalent attribute name for HTML tracks). Other attributes and methods are described later in this lesson.</p>
<h4>Second method: get <span style="font-family: courier new,courier;">TextTrack</span> from the HTML video element</h4>
<p>The &lt;video&gt; element (and &lt;audio&gt; element too) has a <span style="font-family: courier new, courier;">TextTrack</span> property accessible from JavaScript:</p>
<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;videoElement&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#myVideo"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun" style="color: #666600;"></span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;textTracks&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;videoElement</span><span class="pun" style="color: #666600;">.</span><span class="pln">textTracks</span><span class="pun" style="color: #666600;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// one TextTrack for each HTML track element</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;textTrack&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;textTracks</span><span class="pun" style="color: #666600;">[</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">];</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// corresponds to the first track element</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;kind&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;textTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">kind&nbsp;</span><span class="com" style="color: #880000;">// e.g. "subtitles"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;mode&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;textTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">mode&nbsp;</span><span class="com" style="color: #880000;">// e.g. "disabled", "hidden" or "showing"</span></li>
</ol></div>
<p></p>
<h3>The&nbsp;<span style="font-family: 'courier new', courier;">mode</span>&nbsp;property of <span style="font-family: 'courier new', courier;">TextTrack</span> objects</h3>
<p><span style="font-family: 'courier new', courier;">TextTrack</span> objects have a&nbsp;<span style="font-family: 'courier new', courier;">mode</span>&nbsp;property, that is set to one of:</p>
<ol><ol>
<li><span style="font-family: 'courier new', courier;">"showing"</span>: the track is either already loaded, or is being loaded by the browser. As soon as it is completely loaded, subtitles or captions will be displayed in the video. Other kinds of <g class="gr_ gr_95 gr-alert gr_gramm gr_disable_anim_appear Grammar only-ins doubleReplace replaceWithoutSep" id="95" data-gr-id="95">track</g> will be loaded but will not necessarily show anything visible in the document.&nbsp;<em>All tracks that have mode="showing" will fire events while the video is being played.</em></li>
<li><em><span style="font-style: normal; font-family: 'courier new', courier;">"hidden"</span>: the track is either already loaded, or is being loaded by the browser. All tracks that have mode="hidden" will fire events while the video is being played. Nothing will be visible in the standard video player GUI.</em></li>
<li><span style="font-family: 'courier new', courier;">"disabled"</span>: this is the mode where tracks are not being loaded. If a loaded track has its mode set to "disabled", it will stop firing events, and if it was in&nbsp;<span style="font-family: 'courier new', courier;">mode="showing"</span>&nbsp;the subtitles or captions will stop being displayed in the video player.</li>
</ol></ol>
<h4><span style="font-family: 'courier new', courier;">TextTrack</span> content can only be accessed if a track has been loaded! Use the&nbsp;<span style="font-family: 'courier new', courier;">mode</span>&nbsp;property to force a track to be loaded!</h4>
<p class="exampleHTML" style="border: 1px solid black; margin-top: 20px; margin-right: 20px; margin-left: 20px; padding: 20px; font-size: 16px; line-height: 25.6px;"><span style="color: #ff0000;"><strong>BE CAREFUL: you cannot access&nbsp;a <span style="font-family: 'courier new', courier;">TextTrack</span>&nbsp;content if the corresponding HTML track has not been loaded by the browser!<br><br></strong></span>It is possible to force a track to be loaded by setting&nbsp;the&nbsp;<span style="font-family: 'courier new', courier;">mode</span>&nbsp;property of the&nbsp;TextTrack object&nbsp;to "showing" or "hidden".&nbsp;<br>Tracks that are not loaded have their mode property of "disabled".&nbsp;</p>
<p></p>
<p>Here is an example&nbsp;that will test if a track has been loaded, and if it hasn't, will force it to be loaded by setting its mode to "hidden". We could have used "showing"; in this case, if the file is a subtitle or a caption file, then the subtitles or captions will be displayed on the video as soon as the track has finished loading.</p>
<p><a href="https://jsbin.com/bubeye/1/edit?html,console,output" target="_blank">Try the example at JSBin</a></p>
<p><img style="border: 1px solid; border-width: 1px;" alt="Same example as previous one with two buttons for force loading tracks" src="/assets/courseware/v1/c50e4fc4436d274fd610d65ecd4ee773/asset-v1:W3Cx+HTML5.2x+2T2020a+type@asset+block/forceLoadTracks1.jpg" type="saveimage" target="[object Object]" width="1075" height="955"></p>
<p>Here is what we added to the HTML code:</p>
<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttonLoadFirstTrack"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">forceLoadTrack</span><span class="pun">(</span><span class="lit">0</span><span class="pun">);</span><span class="atv">"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">disabled</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Force load track 0</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttonLoadThirdTrack"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">forceLoadTrack</span><span class="pun">(</span><span class="lit">2</span><span class="pun">);</span><span class="atv">"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">disabled</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Force load track 2</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
</ol></div>
<p></p>
<p>The buttons will call a function named&nbsp;<span style="font-family: 'courier new', courier;">forceLoadTrack(trackNumber)</span>&nbsp;that takes as a parameter the number of the track to get (and force load if necessary).</p>
<p>Here are the additions we made to the JavaScript code from the previous example:</p>
<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;readContent</span><span class="pun" style="color: #666600;">(</span><span class="pln">track</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun" style="color: #666600;">.</span><span class="pln">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"reading content of loaded track..."</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;displayTrackStatuses</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTracks</span><span class="pun" style="color: #666600;">); // update document with new track statuses</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;getTrack</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTrack</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;callback</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp;// TextTrack associated to the htmlTrack</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;textTrack&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;htmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">track</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">&nbsp; &nbsp;if</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">readyState&nbsp;</span><span class="pun" style="color: #666600;">===</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun" style="color: #666600;">.</span><span class="pln">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"text track already loaded"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; &nbsp; // call the callback function, the track is available</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; callback</span><span class="pun" style="color: #666600;">(</span><span class="pln">textTrack</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">}</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">else</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun" style="color: #666600;">.</span><span class="pln">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Forcing the text track to be loaded"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// this will force the track to be loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; textTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">mode&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"hidden"</span><span class="pun" style="color: #666600;">;<br>&nbsp; &nbsp; &nbsp; // loading a track is asynchronous, we must use an event listener</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; htmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">addEventListener</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'load'</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666600;">(</span><span class="pln">e</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// the track is arrived, call the callback function</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;callback</span><span class="pun" style="color: #666600;">(</span><span class="pln">textTrack</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666600;">});</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;forceLoadTrack</span><span class="pun" style="color: #666600;">(</span><span class="pln">n</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // first parameter = track number,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // second = a callback function called when the track is loaded,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // that takes the loaded TextTrack as parameter</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; getTrack</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTracks</span><span class="pun" style="color: #666600;">[</span><span class="pln">n</span><span class="pun" style="color: #666600;">],</span><span class="pln">&nbsp;readContent</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div><br>
<p></p>
<p><strong>Explanations:</strong></p>
<ul>
<ul>
<li><em>Lines 26-31</em>: the function called when a button has been clicked. This function in turn calls the&nbsp;<span style="font-family: 'courier new', courier;">getTrack(trackNumber, callback)</span>&nbsp;function. It passes the&nbsp;<span style="font-family: 'courier new', courier;">readContent</span>&nbsp;callback function as a parameter. This is typical JavaScript asynchronous programming: the&nbsp;<span style="font-family: 'courier new', courier;">getTrack()</span>&nbsp;function may force the browser to load the track and this can take some time (a few seconds), then when the track has downloaded, we ask the&nbsp;<span style="font-family: 'courier new', courier;">getTrack</span>&nbsp;function to call the function we passed (the&nbsp;<span style="font-family: 'courier new', courier;">readContent</span>&nbsp;function, which is known as a&nbsp;<em>callback</em>&nbsp;function), with the loaded track as a parameter.</li>
<li><em>Line 6</em>: the getTrack function. It first checks if the HTML track is already loaded (<em>line 10</em>). If it is, it calls the callback function passed by the caller, with the loaded TextTrack as a parameter. If the TextTrack is not loaded, then it sets its mode to "hidden". This will instruct the browser to load the track. Because that may take some time, we must use a&nbsp;<span style="font-family: 'courier new', courier;">load</span>&nbsp;event listener on the HTML track before calling the callback function.&nbsp;This allows us to be&nbsp;sure that the track is really completely loaded.</li>
<li><em>Lines 1-4</em>: the readContent function is only called with a loaded TextTrack. Here we do nothing special for the moment except that we refresh the different track statuses in the HTML document.</li>
</ul>
</ul>
</div>
</div>

Note that once we get a `TextTrack` object, we can manipulate the kind, label, language attributes (be careful, it's not srclang, like the equivalent attribute name for HTML tracks). Other attributes and methods are described later in this lesson.

__Second method: get TextTrack from the HTML video element__

The `<video>` element (and `<audio>` element too) has a `TextTrack` property accessible from JavaScript:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;videoElement&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;document</span><span class="pun" style="color: #666600;">.</span><span class="pln">querySelector</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"#myVideo"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun" style="color: #666600;"></span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;textTracks&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;videoElement</span><span class="pun" style="color: #666600;">.</span><span class="pln">textTracks</span><span class="pun" style="color: #666600;">;</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// one TextTrack for each HTML track element</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;textTrack&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;textTracks</span><span class="pun" style="color: #666600;">[</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">];</span><span class="pln">&nbsp;</span><span class="com" style="color: #880000;">// corresponds to the first track element</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;kind&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;textTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">kind&nbsp;</span><span class="com" style="color: #880000;">// e.g. "subtitles"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;mode&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;textTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">mode&nbsp;</span><span class="com" style="color: #880000;">// e.g. "disabled", "hidden" or "showing"</span></li>
</ol></div><br>

#### The `mode` property of `TextTrack` objects

`TextTrack` objects have a mode property, that is set to one of:

1. "`showing`": the track is either already loaded, or is being loaded by the browser. As soon as it is completely loaded, subtitles or captions will be displayed in the video. Other kinds of track will be loaded but will not necessarily show anything visible in the document. _All tracks that have mode="showing" will fire events while the video is being played._
2. "`hidden`": the track is either already loaded, or is being loaded by the browser. All tracks that have mode="hidden" will fire events while the video is being played. _Nothing will be visible in the standard video player GUI._
3. "`disabled`": this is the mode where tracks are not being loaded. If a loaded track has its mode set to "disabled", it will stop firing events, and if it was in `mode="showing"` the subtitles or captions will stop being displayed in the video player.


__`TextTrack` content can only be accessed if a track has been loaded! Use the mode property to force a track to be loaded!__

<p class="exampleHTML" style="border: 1px solid black; margin-top: 20px; margin-right: 20px; margin-left: 20px; padding: 20px; font-size: 16px; line-height: 25.6px;"><span style="color: #ff0000;"><strong>BE CAREFUL: you cannot access&nbsp;a <span style="font-family: 'courier new', courier;">TextTrack</span>&nbsp;content if the corresponding HTML track has not been loaded by the browser!<br><br></strong></span>It is possible to force a track to be loaded by setting&nbsp;the&nbsp;<span style="font-family: 'courier new', courier;">mode</span>&nbsp;property of the&nbsp;TextTrack object&nbsp;to "showing" or "hidden".&nbsp;<br>Tracks that are not loaded have their mode property of "disabled".&nbsp;</p>

Here is an example that will test if a track has been loaded, and if it hasn't, will force it to be loaded by setting its mode to "hidden". We could have used "showing"; in this case, if the file is a subtitle or a caption file, then the subtitles or captions will be displayed on the video as soon as the track has finished loading.

[Try the example at JSBin](https://jsbin.com/bubeye/1/edit?html,console,output)

[Local Demo](src/01b-example02.html)


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://reurl.cc/jqbyXM')"
    src    = "https://reurl.cc/V3yMyY"
    alt    = "Same example as previous one with two buttons for force loading tracks"
    title  = "Same example as previous one with two buttons for force loading tracks"
  />
</figure>


Here is what we added to the HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttonLoadFirstTrack"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">forceLoadTrack</span><span class="pun">(</span><span class="lit">0</span><span class="pun">);</span><span class="atv">"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">disabled</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Force load track 0</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttonLoadThirdTrack"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">forceLoadTrack</span><span class="pun">(</span><span class="lit">2</span><span class="pun">);</span><span class="atv">"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">disabled</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Force load track 2</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
</ol></div><br>

The buttons will call a function named `forceLoadTrack(trackNumber)` that takes as a parameter the number of the track to get (and force load if necessary).

Here are the additions we made to the JavaScript code from the previous example:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;readContent</span><span class="pun" style="color: #666600;">(</span><span class="pln">track</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun" style="color: #666600;">.</span><span class="pln">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"reading content of loaded track..."</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;displayTrackStatuses</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTracks</span><span class="pun" style="color: #666600;">); // update document with new track statuses</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;getTrack</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTrack</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;callback</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp;// TextTrack associated to the htmlTrack</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd" style="color: #008888;">var</span><span class="pln">&nbsp;textTrack&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;htmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">track</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">&nbsp; &nbsp;if</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">readyState&nbsp;</span><span class="pun" style="color: #666600;">===</span><span class="pln">&nbsp;</span><span class="lit" style="color: #006666;">2</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun" style="color: #666600;">.</span><span class="pln">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"text track already loaded"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; &nbsp; // call the callback function, the track is available</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; callback</span><span class="pun" style="color: #666600;">(</span><span class="pln">textTrack</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">}</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">else</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun" style="color: #666600;">.</span><span class="pln">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"Forcing the text track to be loaded"</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" style="color: #880000;">// this will force the track to be loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; textTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">mode&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln">&nbsp;</span><span class="str" style="color: #008800;">"hidden"</span><span class="pun" style="color: #666600;">;<br>&nbsp; &nbsp; &nbsp; // loading a track is asynchronous, we must use an event listener</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; htmlTrack</span><span class="pun" style="color: #666600;">.</span><span class="pln">addEventListener</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">'load'</span><span class="pun" style="color: #666600;">,</span><span class="pln">&nbsp;</span><span class="kwd" style="color: #008888;">function</span><span class="pun" style="color: #666600;">(</span><span class="pln">e</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// the track is arrived, call the callback function</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;callback</span><span class="pun" style="color: #666600;">(</span><span class="pln">textTrack</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun" style="color: #666600;">});</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd" style="color: #008888;">function</span><span class="pln">&nbsp;forceLoadTrack</span><span class="pun" style="color: #666600;">(</span><span class="pln">n</span><span class="pun" style="color: #666600;">)</span><span class="pln">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // first parameter = track number,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // second = a callback function called when the track is loaded,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; // that takes the loaded TextTrack as parameter</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; getTrack</span><span class="pun" style="color: #666600;">(</span><span class="pln">htmlTracks</span><span class="pun" style="color: #666600;">[</span><span class="pln">n</span><span class="pun" style="color: #666600;">],</span><span class="pln">&nbsp;readContent</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div><br>

__Explanations:__

+ _Lines 26-31_: the function called when a button has been clicked. This function in turn calls the `getTrack(trackNumber, callback)` function. It passes the `readContent` callback function as a parameter. This is typical JavaScript asynchronous programming: the `getTrack()` function may force the browser to load the track and this can take some time (a few seconds), then when the track has downloaded, we ask the `getTrack` function to call the function we passed (the `readContent` function, which is known as a _callback_ function), with the loaded track as a parameter.
+ _Line 6_: the `getTrack` function. It first checks if the HTML track is already loaded (_line 10_). If it is, it calls the callback function passed by the caller, with the loaded TextTrack as a parameter. If the TextTrack is not loaded, then it sets its mode to "hidden". This will instruct the browser to load the track. Because that may take some time, we must use a `load` event listener on the HTML track before calling the callback function. This allows us to be sure that the track is really completely loaded.
+ _Lines 1-4_: the readContent function is only called with a loaded TextTrack. Here we do nothing special for the moment except that we refresh the different track statuses in the HTML document.


#### Knowledge check 1.2.3

1. When you force load a track, how can you be sure that it's loaded?

  a. You should define a load event listener on the html track element, when the track is loaded, the load event will be fired. Do the rest of your work with the track in this listener (reading its content, etc).<br>
  b. Check the `readyState` property of its HTML track element. If it has a value=2, then the track is loaded.

  Ans: a<br>
  Explanantion: The `readyState` property will not load the track. To load a file, set the `mode` property of its TextTrack object to "hidden" or "showing" and then use a load listener on the html track element, like in the provided example.


#### Notes for 1.2.3 The `TextTrack` object

+ `TextTrack` object
  + containing the cue, not HTML object itself
  + w/ different methods and properties for manipulating track content
  + associated w/ different events

+ Accessing `TextTrack` object
  + obtaining from associated HTML track
    + access HTMl `track` element: `var htmlTracks = document.querySelectorAll("track");`
    + `TextTrack` object associate w/ the 1st HTML track: `var textTrack = htmlTrack[0].track;`
    + get 1st track attributes: `var kind = textTrack.kind; var label = textTrack.label; var lang = textTrack.language; ...`
  + obtaining from the HTML video/audio element
    + access video element: `var videoElement = document.querySelector("#myVideo");`
    + all tracks w/ the video element: `var textTracks = videoElement.textTracks;`
    + access 1st track element: `var textTrack = textTracks[0];`
    + get 1st track attributes: `var kind = textTrack.kind; var mode = textTrack.mode; ...`
  + content existed only if a track loaded

+ The `mode` property of `TextTrack` objects
  + `showing`
    + track already loaded or being loaded by the browser
    + displayed in the video once completely loaded
    + firing event while video played
  + `hidden`
    + track ready loaded or being loaded by the browser
    + firing events while video played
    + nothing visible in the standard video player GUI
  + `disabled`
    + track not loaded
    + stop firing events
  + setting `mode` property as `showing` and `hidden` to force a track to be loaded

+ Example: button to load tracks
  + creating HTML button
    + `<button id="buttonLoadFirstTrack" onclick="forceLoadTrack(0);" disabled> Force load track 0 </button>`
    + callback function to get track (forcing load if necessary): `forceLoadTrack(trackNumber)`
    + get TextTrack object w/ associated HTML `<track>` element: `function getTrack(htmlTrack, callback): {...}`
      + track variable: `var TextTrack = htmlTrack.track;`
      + check track loaded: `if (htmlTrack.readySyaye === 2) {...}`
        + console log: `console.log("text track already loaded");`
        + exec callback function: `callback(textTrack);`
      + track not loaded yet:
        + console log: `console.log("Forcing the text track to be loaded");`
        + force to load track: `textTrack.mode = "hidden";`
        + using an event listener while loading track: `htmlTrack.addEventListener('load', function(e) {callback(textTrack)});`
  + JavaScript to download and display tracks
    + force to load track: `function forceLoadTrack(n) (getTrack(htmlTracks[n], readContent);`
    + read and display track status: `function readContent(track) {...}`
      + console log: `console.log("reading content of loaded track ...");`
      + update page w/ new track: `displayTrackStatuses(htmlTracks)`


### 1.2.4 Working with cues


#### Live Coding Video: accessing the content of a track

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://reurl.cc/DvWK1j)


#### Properties and methods of `TextTrack` object

A `TextTrack` object has different properties and methods

+ `kind`: equivalent to the kind attribute of HTML track elements. Its value is either "subtitles", "caption", "descriptions", "chapters", or "metadata". We will see examples of chapters, descriptions  and metadata tracks in subsequent lessons.
+ `label`: the label of the track, equivalent of the label attribute of HTML track elements.
+ `language`: the language of the text track,  equivalent to the srclang attribute of HTML track elements (be careful: it's not the same spelling!)
+ `mode`: explained earlier. Can have values equal to: "disabled"|"hidden"|"showing". Can force a track to be loaded (by setting the mode to "hidden" or "showing").
+ `cues`: get a list of cues as a TextTrackCueList object. This is the complete content of the WebVTT file!
+ `activeCues`: used in event listeners while the video is playing. Corresponds to the cues located in the current time segment. The start and end times of cues can overlap. In reality this may rarely happen, but this property exists in case it does, returning a  TextTrackCueList object that contains all active tracks at a given time.
+ `addCue(cue)`: add a cue to the list of cues.
+ `removeCue(cue)`: remove a cue from the list of cues.
+ `getCueById(id)`: returns the cue with a given id (not implemented by all browsers - a polyfill is given in the examples from the next lessons).


A `TextTrackCueList` is a collection of cues, each of which has different properties and methods

+ `id`: the cue id as written in the line that starts cues in the WebVTT file.
+ `startTime` and `endTime`: define the time segment for the cue, in seconds, as a floating point value. It is not the formatted String we have in the WebVTT file (see screenshot below),
+ `text`: the cue content.
+ `getCueAsHTML()`: a method that returns an HTML version of the cue content, not as plain text.
+ Others such as align, line, position, size, snapToLines, etc., that correspond to the position of the cue, as specified in the WebVTT file. See the HTML5 course Part 1 about cue positioning.

a webVtt file extract with arrows showing id, startTime, endTime and text


#### Example that displays the content of a track

Here is an example at JSBin that displays the content of a track:

Example that shows the list of cues under the video, for a gicen track

We just changed the content of the readContent(track) method from the example from the previous lesson:

<div class="source-code" style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol class="linenums" style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd" style="color: #000088;">function</span><span class="pln" style="color: #000000;">&nbsp;readContent</span><span class="pun" style="color: #666600;">(</span><span class="pln" style="color: #000000;">track</span><span class="pun" style="color: #666600;">)</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;console</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">log</span><span class="pun" style="color: #666600;">(</span><span class="str" style="color: #008800;">"reading content of loaded track..."</span><span class="pun" style="color: #666600;">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="com" style="color: #880000;">//displayTrackStatuses(htmlTracks);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp;// instead of displaying the track statuses, we display</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp;// in the same div, the track content//</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com" style="color: #880000;">&nbsp; &nbsp;// first, empty the div</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;trackStatusesDiv</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">""</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;// get the list of cues for that track &nbsp;&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd" style="color: #000088;">&nbsp; &nbsp;var</span><span class="pln" style="color: #000000;">&nbsp;cues&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;track</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">cues</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp;// iterate on them</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="kwd" style="color: #000088;">for</span><span class="pun" style="color: #666600;">(</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;i</span><span class="pun" style="color: #666600;">=</span><span class="lit" style="color: #006666;">0</span><span class="pun" style="color: #666600;">;</span><span class="pln" style="color: #000000;">&nbsp;i&nbsp;</span><span class="pun" style="color: #666600;">&lt;</span><span class="pln" style="color: #000000;">&nbsp;cues</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">length</span><span class="pun" style="color: #666600;">;</span><span class="pln" style="color: #000000;">&nbsp;i</span><span class="pun" style="color: #666600;">++)</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">&nbsp; &nbsp; &nbsp; // current cue</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;cue&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;cues</span><span class="pun" style="color: #666600;">[</span><span class="pln" style="color: #000000;">i</span><span class="pun" style="color: #666600;">];</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;id&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;cue</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">id&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">"&lt;br&gt;"</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;timeSegment&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;cue</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">startTime&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">" =&gt; "</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;cue</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">endTime&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">"&lt;br&gt;"</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" style="color: #000088;">var</span><span class="pln" style="color: #000000;">&nbsp;text&nbsp;</span><span class="pun" style="color: #666600;">=</span><span class="pln" style="color: #000000;">&nbsp;cue</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">text&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;</span><span class="str" style="color: #008800;">"&lt;P&gt;"</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp; &nbsp; trackStatusesDiv</span><span class="pun" style="color: #666600;">.</span><span class="pln" style="color: #000000;">innerHTML&nbsp;</span><span class="pun" style="color: #666600;">+=</span><span class="pln" style="color: #000000;">&nbsp;id&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;timeSegment&nbsp;</span><span class="pun" style="color: #666600;">+</span><span class="pln" style="color: #000000;">&nbsp;text</span><span class="pun" style="color: #666600;">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln" style="color: #000000;">&nbsp; &nbsp;</span><span class="pun" style="color: #666600;">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="color: #666600;">}</span></li>
</ol></div><br>

As you can see, the code is simple: you first get the cues for the given TextTrack (it must be loaded; this is the case since we took care of it earlier), then iterate on the list of cues, and use the id, startTime, endTime and text properties of each cue.

This technique will be used in one of the next lessons, and we will show you how to make a clickable transcript on the side of the video - something quite similar to what the edX video player does.

#### Knowledge check 1.2.4

1. What is the name of the TextTrack property that returns the list of all its cues?

  a. `activeCues`<br>
  b. `cues`<br>
  c. `cueList`<br>

  Ans: <br>
  Explanation: 



### 1.2.5 Listening to events



