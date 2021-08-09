# Module 1: Advanced HTML5 multimedia section


## 1.2 The Timed Text Track API


### 1.2.1 The Timed Text Track API

#### Contents

In the [W3Cx HTML5 Coding Essentials and Best Practices](https://bit.ly/3we2vSS) course, we saw that `<video>` and `<audio>` elements can have `<track>` elements. A `<track>` can have a `label`, a `kind` (subtitles, captions, chapters, metadata, etc.), a language (`srclang` attribute), a source URL (`src` attribute), etc.

Here is a small example of a video with 3 different tracks ("......" masks the real URL here, as it is too long to fit in this page width!):

<div><ol>
<li value="1">&lt;video id="myVideo" preload="metadata" controls crossOrigin="anonymous"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="https://...../elephants-dream-medium.mp4" type="video/mp4"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="https://<span style="line-height: 25.6px;">...../elephants-dream-medium.webm"</span> type="video/webm"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;<strong>&lt;track label="English subtitles" kind="subtitles" srclang="en" </strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"&gt;</strong></li>
<li><strong>&nbsp; &nbsp;&nbsp;&lt;track label="Deutsch subtitles" kind="subtitles" srclang="de" </strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt" default&gt;</strong></li>
<li><strong>&nbsp; &nbsp;&nbsp;&lt;track label="English chapters" kind="chapters" srclang="en" </strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"&gt;</strong></li>
<li> &lt;/video&gt;</li>
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

<div><ol>
<li value="1">WEBVTT</li>
<li>&nbsp;</li>
<li>1</li>
<li>00:00:15.000 --&gt; 00:00:18.000 align:start</li>
<li>&lt;v Proog&gt;On the left we can see...&lt;/v&gt;</li>
<li>&nbsp;</li>
<li>2</li>
<li>00:00:18.167 --&gt; 00:00:20.083 align:middle</li>
<li>&lt;v Proog&gt;On the right we can see the...&lt;/v&gt;</li>
<li>&nbsp;</li>
<li>3</li>
<li>00:00:20.083 --&gt; 00:00:22.000</li>
<li>&lt;v Proog&gt;...the &lt;c.highlight&gt;head-snarlers&lt;/c&gt;&lt;/v&gt;</li>
<li>&nbsp;</li>
<li>4</li>
<li>00:00:22.000 --&gt; 00:00:24.417 align:end</li>
<li>&lt;v Proog&gt;Everything is safe. Perfectly safe.&lt;/v&gt;</li>
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


#### Notes for 1.2.1 The Timed Text Track API

+ `<track>` element
  + typically within `<video>` and `<audio>` elements
  + attributes
    + `label`
    + `kind`: subtitle, captions, chapters, matadata, etc.
    + `srclang`: language
    + `src`: a source URL
    + `default`: specifying the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate
    + ...
  + example<a name="trackHtml"></a>

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
    + element w/ an `id`, a startTime, and an endTime
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


#### Knowledge check 1.2.1

1. Do the most recent versions of all major browsers provide a menu for choosing the subtitle or the caption track? (Yes/No)

  Ans: No<br>
  Explanation: Unfortunately, support currently varies from one browser to another. Only Safari, IE and Microsoft Edge provide a menu to choose the subtitle or caption track. These missing features can be added, however, using the Timed Text Track API.



### 1.2.2 The HTML track element

#### Live coding video: HTML Track element

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/33TXcvF)


#### Example: `<track>`

Let's go back to our example. Below is the HTML code:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">&lt;video</span>&nbsp;<span style="color: #aa0066;">id</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"myVideo"</span>&nbsp;<span style="color: #aa0066;">preload</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"metadata"</span>&nbsp;<span style="color: #aa0066;">controls</span>&nbsp;<span style="color: #aa0066;">crossOrigin</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"anonymous"</span><span style="color: #008888;">&gt;</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">&lt;source</span>&nbsp;<span style="color: #aa0066;">src</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"https://...../elephants-dream-medium.mp4"</span>&nbsp;<span style="color: #aa0066;">type</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"video/mp4"</span><span style="color: #008888;">&gt;</span></li>
<li>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">&lt;source</span>&nbsp;<span style="color: #aa0066;">src</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm"</span>&nbsp;<span style="color: #aa0066;">type</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"video/webm"</span><span style="color: #008888;">&gt;</span></li>
<li>&nbsp; &nbsp;&nbsp;<strong><span style="color: #008888;">&lt;track</span>&nbsp;<span style="color: #aa0066;">label</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"English subtitles"</span>&nbsp;<span style="color: #aa0066;">kind</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"subtitles"</span>&nbsp;<span style="color: #aa0066;">srclang</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"en"</span></strong></li>
<li><strong><span style="color: #aa0066;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"</span>&nbsp;<span style="color: #008888;">&gt;</span></strong></li>
<li><strong>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">&lt;track</span>&nbsp;<span style="color: #aa0066;">label</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"Deutsch subtitles"</span>&nbsp;<span style="color: #aa0066;">kind</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"subtitles"</span>&nbsp;<span style="color: #aa0066;">srclang</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"de"</span></strong></li>
<li><strong><span style="color: #aa0066;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt"</span>&nbsp;<span style="color: #aa0066;">default</span><span style="color: #008888;">&gt;</span></strong></li>
<li><strong>&nbsp; &nbsp;&nbsp;<span style="color: #008888;">&lt;track</span>&nbsp;<span style="color: #aa0066;">label</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"English chapters"</span>&nbsp;<span style="color: #aa0066;">kind</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"chapters"</span>&nbsp;<span style="color: #aa0066;">srclang</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"en"</span></strong></li>
<li><strong><span style="color: #aa0066;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span style="color: #bb6600;">=</span><span style="color: #008800;">"https://<span style="font-weight: normal; line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"</span><span style="color: #008888;">&gt;</span></strong></li>
<li>&nbsp;<span style="color: #008888;">&lt;/video&gt;</span></li>
<li><span style="color: #008888;"></span></li>
<li>&lt;div id="trackStatusesDiv"&gt;</li>
<li>&nbsp; &nbsp; &lt;h3&gt;HTML track descriptions&lt;/h3&gt;</li>
<li>&lt;/div&gt;</li>
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

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">var</span>&nbsp;video<span style="color: #bb6600;">,</span>&nbsp;htmlTracks<span style="color: #bb6600;">;</span></li>
<li><span style="color: #008888;">var</span>&nbsp;trackStatusesDiv<span style="color: #bb6600;">;</span></li>
<li>&nbsp;</li>
<li>window<span style="color: #bb6600;">.</span>onload&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">()</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// called when the page has been loaded</span></li>
<li><span>&nbsp; &nbsp;video&nbsp;</span><span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelector<span style="color: #bb6600;">(</span><span style="color: #008800;">"#myVideo"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;trackStatusesDiv&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelector<span style="color: #bb6600;">(</span><span style="color: #008800;">"#trackStatusesDiv"</span><span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// Get the tracks as HTML elements</span></li>
<li>&nbsp; &nbsp;htmlTracks&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelectorAll<span style="color: #bb6600;">(</span><span style="color: #008800;">"track"</span><span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// displays their statuses in a div under the video</span></li>
<li>&nbsp; &nbsp;displayTrackStatuses<span style="color: #bb6600;">(</span>htmlTracks<span style="color: #bb6600;">);</span></li>
<li><span style="color: #bb6600;">};</span></li>
<li>&nbsp;</li>
<li><span style="color: #008888;">function</span>&nbsp;displayTrackStatuses<span style="color: #bb6600;">(</span>htmlTracks<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// displays track info</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">(</span><span style="color: #008888;">var</span>&nbsp;i&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #006666;">0</span><span style="color: #bb6600;">;</span>&nbsp;i&nbsp;<span style="color: #bb6600;">&lt;</span>&nbsp;htmlTracks<span style="color: #bb6600;">.</span>length<span style="color: #bb6600;">;</span>&nbsp;i<span style="color: #bb6600;">++)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;currentHtmlTrack&nbsp;<span style="color: #bb6600;">=</span>&nbsp;htmlTracks<span style="color: #bb6600;">[</span>i<span style="color: #bb6600;">];</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;label&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">"&lt;li&gt;label = "</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;currentHtmlTrack<span style="color: #bb6600;">.</span>label&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;/li&gt;"</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;kind&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">"&lt;li&gt;kind = "</span>&nbsp; &nbsp;<span style="color: #bb6600;">+</span>&nbsp;currentHtmlTrack<span style="color: #bb6600;">.</span>kind&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;/li&gt;"</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;lang&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">"&lt;li&gt;lang = "</span>&nbsp; &nbsp;<span style="color: #bb6600;">+</span>&nbsp;currentHtmlTrack<span style="color: #bb6600;">.</span>srclang&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;/li&gt;"</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;readyState&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">"&lt;li&gt;readyState = "</span>&nbsp;</li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span>&nbsp;currentHtmlTrack<span style="color: #bb6600;">.</span>readyState&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;/li&gt;"</span></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;trackStatusesDiv<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">+=</span>&nbsp;<span style="color: #008800;">"&lt;li&gt;&lt;b&gt;Track:"</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;i&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">":&lt;/b&gt;&lt;/li&gt;"</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;ul&gt;"</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;label&nbsp;<span style="color: #bb6600;">+</span>&nbsp;kind&nbsp;<span style="color: #bb6600;">+</span>&nbsp;lang&nbsp;<span style="color: #bb6600;">+</span>&nbsp;readyState&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;/ul&gt;"</span><span style="color: #bb6600;">;</li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">}</span></li>
<li><span style="color: #bb6600;">}</span></li>
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
    + display info: `trackStatusesDiv.innerHTML += "<li><b>Track:" + i + ":</b></li>" + "<ul>" + label + kind + lang + readyState + "</ul>"`

+ Values of `readyState` attribute
  + __0 = NONE__: the text track's cues not obtained
  + __1 = LOADING__: the text track loaded w/o errors yet, further cues able to be added to the track by the parser
  + __2 = LOADED__: the text track loaded w/o errors
  + __3 = ERROR__: the text track enabled but accessing failed, likely missing


#### Knowledge check 1.2.2

1. When playing a video, are all tracks loaded by default?

  a. It depends on the browser<br>
  b. Yes<br>

  Ans: a<br>
  Explanation: In the given example, only the first track with the `default` attribute has been loaded. Try the example on different browsers and you will notice that only the track with the `default` attribute is loaded by the major browsers, when the page is loaded. FireFox will load all tracks, but will display the one with the `default` attribute only if it's the first one.


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

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #880000;">// HTML tracks</span></li>
<li><span style="color: #008888;">var</span>&nbsp;htmlTracks&nbsp;<span style="color: #bb6600;">=</span>&nbsp;document<span style="color: #bb6600;">.</span>querySelectorAll<span style="color: #bb6600;">(</span><span style="color: #008800;">"track"</span><span style="color: #bb6600;">);</span></li>
<li><span>&nbsp;</span></li>
<li><span>&nbsp;</span></li>
<li><span style="color: #880000;">// The TextTrack object associated&nbsp;with the first HTML track</span></li>
<li><strong><span style="color: #008888;">var</span><span>&nbsp;textTrack&nbsp;</span><span style="color: #bb6600;">=</span><span>&nbsp;htmlTracks</span><span style="color: #bb6600;">[</span><span style="color: #006666;">0</span><span style="color: #bb6600;">].</span><span>track</span><span style="color: #bb6600;">;</span></strong></li>
<li><span style="color: #bb6600;">var kind = textTrack.kind;</span></li>
<li><span style="color: #bb6600;">var label = textTrack.label;</span></li>
<li><span style="color: #bb6600;" color="#bb6600">var lang = textTrack.language;</span></li>
<li><span style="color: #bb6600;" color="#bb6600">// etc.</span></li>
</ol></div>


Note that once we get a `TextTrack` object, we can manipulate the kind, label, language attributes (be careful, it's not srclang, like the equivalent attribute name for HTML tracks). Other attributes and methods are described later in this lesson.

__Second method: get TextTrack from the HTML video element__

The `<video>` element (and `<audio>` element too) has a `TextTrack` property accessible from JavaScript:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">var</span><span>&nbsp;videoElement&nbsp;</span><span style="color: #bb6600;">=</span><span>&nbsp;document</span><span style="color: #bb6600;">.</span><span>querySelector</span><span style="color: #bb6600;">(</span><span style="color: #008800;">"#myVideo"</span><span style="color: #bb6600;">);</span></li>
<li value="1"><span style="color: #bb6600;"></span></li>
<li><strong><span style="color: #008888;">var</span><span>&nbsp;textTracks&nbsp;</span><span style="color: #bb6600;">=</span><span>&nbsp;videoElement</span><span style="color: #bb6600;">.</span><span>textTracks</span><span style="color: #bb6600;">;</span><span>&nbsp;</span><span style="color: #880000;">// one TextTrack for each HTML track element</span></strong></li>
<li><span style="color: #008888;">var</span><span>&nbsp;textTrack&nbsp;</span><span style="color: #bb6600;">=</span><span>&nbsp;textTracks</span><span style="color: #bb6600;">[</span><span style="color: #006666;">0</span><span style="color: #bb6600;">];</span><span>&nbsp;</span><span style="color: #880000;">// corresponds to the first track element</span></li>
<li><span style="color: #008888;">var</span><span>&nbsp;kind&nbsp;</span><span style="color: #bb6600;">=</span><span>&nbsp;textTrack</span><span style="color: #bb6600;">.</span><span>kind&nbsp;</span><span style="color: #880000;">// e.g. "subtitles"</span></li>
<li><span style="color: #008888;">var</span><span>&nbsp;mode&nbsp;</span><span style="color: #bb6600;">=</span><span>&nbsp;textTrack</span><span style="color: #bb6600;">.</span><span>mode&nbsp;</span><span style="color: #880000;">// e.g. "disabled", "hidden" or "showing"</span></li>
</ol></div><br>

#### The `mode` property of `TextTrack` objects

`TextTrack` objects have a mode property, that is set to one of:

1. "`showing`": the track is either already loaded, or is being loaded by the browser. As soon as it is completely loaded, subtitles or captions will be displayed in the video. Other kinds of track will be loaded but will not necessarily show anything visible in the document. _All tracks that have mode="showing" will fire events while the video is being played._
2. "`hidden`": the track is either already loaded, or is being loaded by the browser. All tracks that have mode="hidden" will fire events while the video is being played. _Nothing will be visible in the standard video player GUI._
3. "`disabled`": this is the mode where tracks are not being loaded. If a loaded track has its mode set to "disabled", it will stop firing events, and if it was in `mode="showing"` the subtitles or captions will stop being displayed in the video player.


__`TextTrack` content can only be accessed if a track has been loaded! Use the mode property to force a track to be loaded!__

<p style="border: 1px solid black; margin-top: 20px; margin-right: 20px; margin-left: 20px; padding: 20px; font-size: 16px; line-height: 25.6px;"><span style="color: #ff0000;"><strong>BE CAREFUL: you cannot access&nbsp;a <span style="font-family: 'courier new', courier;">TextTrack</span>&nbsp;content if the corresponding HTML track has not been loaded by the browser!<br><br></strong></span>It is possible to force a track to be loaded by setting&nbsp;the&nbsp;<span style="font-family: 'courier new', courier;">mode</span>&nbsp;property of the&nbsp;TextTrack object&nbsp;to "showing" or "hidden".&nbsp;<br>Tracks that are not loaded have their mode property of "disabled".&nbsp;</p>

Here is an example that will test if a track has been loaded, and if it hasn't, will force it to be loaded by setting its mode to "hidden". We could have used "showing"; in this case, if the file is a subtitle or a caption file, then the subtitles or captions will be displayed on the video as soon as the track has finished loading.

[Try the example at JSBin](https://jsbin.com/bubeye/1/edit?html,console,output)

[Local Demo](src/01b-example02.html)


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open('https://bit.ly/3fnnewM')"
    src    = "https://bit.ly/3hyvU63"
    alt    = "Same example as previous one with two buttons for force loading tracks"
    title  = "Same example as previous one with two buttons for force loading tracks"
  />
</figure>


Here is what we added to the HTML code:

<div><ol>
<li value="1">&lt;button id="buttonLoadFirstTrack"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;onclick="forceLoadTrack(0);"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;disabled&gt;</li>
<li>&nbsp; &nbsp;Force load track 0</li>
<li>&lt;/button&gt;</li>
<li>&lt;button id="buttonLoadThirdTrack"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;onclick="forceLoadTrack(2);"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;disabled&gt;</li>
<li>&nbsp; &nbsp;Force load track 2</li>
<li>&lt;/button&gt;</li>
</ol></div><br>

The buttons will call a function named `forceLoadTrack(trackNumber)` that takes as a parameter the number of the track to get (and force load if necessary).

Here are the additions we made to the JavaScript code from the previous example:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">function</span>&nbsp;readContent<span style="color: #bb6600;">(</span>track<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">"reading content of loaded track..."</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;displayTrackStatuses<span style="color: #bb6600;">(</span>htmlTracks<span style="color: #bb6600;">); // update document with new track statuses</span></li>
<li><span style="color: #bb6600;">}</li>
<li>&nbsp;</li>
<li><span style="color: #008888;">function</span>&nbsp;getTrack<span style="color: #bb6600;">(</span>htmlTrack<span style="color: #bb6600;">,</span>&nbsp;callback<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp;// TextTrack associated to the htmlTrack</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;textTrack&nbsp;<span style="color: #bb6600;">=</span>&nbsp;htmlTrack<span style="color: #bb6600;">.</span>track<span style="color: #bb6600;">;</span></li>
<li><span style="color: #bb6600;"></span></li>
<li><span style="color: #008888;">&nbsp; &nbsp;if</span><span style="color: #bb6600;">(</span>htmlTrack<span style="color: #bb6600;">.</span>readyState&nbsp;<span style="color: #bb6600;">===</span>&nbsp;<span style="color: #006666;">2</span><span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp; console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">"text track already loaded"</span><span style="color: #bb6600;">);</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; &nbsp; // call the callback function, the track is available</span></li>
<li>&nbsp; &nbsp; &nbsp; callback<span style="color: #bb6600;">(</span>textTrack<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">}</span>&nbsp;<span style="color: #008888;">else</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp; console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">"Forcing the text track to be loaded"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// this will force the track to be loaded</span></li>
<li>&nbsp; &nbsp; &nbsp; textTrack<span style="color: #bb6600;">.</span>mode&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">"hidden"</span><span style="color: #bb6600;">;<br>&nbsp; &nbsp; &nbsp; // loading a track is asynchronous, we must use an event listener</span></li>
<li>&nbsp; &nbsp; &nbsp; htmlTrack<span style="color: #bb6600;">.</span>addEventListener<span style="color: #bb6600;">(</span><span style="color: #008800;">'load'</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(</span>e<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// the track is arrived, call the callback function</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;callback<span style="color: #bb6600;">(</span>textTrack<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #bb6600;">});</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">}</span></li>
<li><span style="color: #bb6600;">}</span></li>
<li><span style="color: #008888;"></span></li>
<li><span style="color: #008888;">function</span>&nbsp;forceLoadTrack<span style="color: #bb6600;">(</span>n<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; // first parameter = track number,</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; // second = a callback function called when the track is loaded,</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; // that takes the loaded TextTrack as parameter</span></li>
<li>&nbsp; &nbsp; getTrack<span style="color: #bb6600;">(</span>htmlTracks<span style="color: #bb6600;">[</span>n<span style="color: #bb6600;">],</span>&nbsp;readContent<span style="color: #bb6600;">);</span></li>
<li><span style="color: #bb6600;">}</span></li>
</ol></div><br>

__Explanations:__

+ _Lines 26-31_: the function called when a button has been clicked. This function in turn calls the `getTrack(trackNumber, callback)` function. It passes the `readContent` callback function as a parameter. This is typical JavaScript asynchronous programming: the `getTrack()` function may force the browser to load the track and this can take some time (a few seconds), then when the track has downloaded, we ask the `getTrack` function to call the function we passed (the `readContent` function, which is known as a _callback_ function), with the loaded track as a parameter.
+ _Line 6_: the `getTrack` function. It first checks if the HTML track is already loaded (_line 10_). If it is, it calls the callback function passed by the caller, with the loaded TextTrack as a parameter. If the TextTrack is not loaded, then it sets its mode to "hidden". This will instruct the browser to load the track. Because that may take some time, we must use a `load` event listener on the HTML track before calling the callback function. This allows us to be sure that the track is really completely loaded.
+ _Lines 1-4_: the readContent function is only called with a loaded TextTrack. Here we do nothing special for the moment except that we refresh the different track statuses in the HTML document.

#### Notes for 1.2.3 The `TextTrack` object

+ `TextTrack` object
  + containing the cue, not HTML object itself
  + w/ different methods and properties for manipulating track content
  + associated w/ different events

+ Accessing `TextTrack` object
  + obtaining from associated HTML track
    + access HTMl `track` element: `var htmlTracks = document.querySelectorAll("track");`
    + `TextTrack` object associated w/ the 1st HTML track: `var textTrack = htmlTrack[0].track;`
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
  + HTML snippet
    + creating HTML button: `<button id="buttonLoadFirstTrack" onclick="forceLoadTrack(0);" disabled> Force load track 0 </button>`
    + callback function to get track (forcing load if necessary): `forceLoadTrack(trackNumber);`
    + get TextTrack object w/ associated HTML `<track>` element: `function getTrack(htmlTrack, callback): {...}`
      + declare variable: `var TextTrack = htmlTrack.track;`
      + check track loaded: `if (htmlTrack.readyState === 2) {...}`
        + console log: `console.log("text track already loaded");`
        + exec callback function: `callback(textTrack);`
      + track not loaded yet:
        + console log: `console.log("Forcing the text track to be loaded");`
        + force to load track: `textTrack.mode = "hidden";`
        + use listener while loading track: `htmlTrack.addEventListener('load', function(e) {callback(textTrack);});`
  + JavaScript snippet
    + force to load track: `function forceLoadTrack(n) {getTrack(htmlTracks[n], readContent;}`
    + read and display track status: `function readContent(track) {...}`
      + console log: `console.log("reading content of loaded track ...");`
      + update page w/ new track: `displayTrackStatuses(htmlTracks);`


#### Knowledge check 1.2.3

1. When you force load a track, how can you be sure that it's loaded?

  a. You should define a load event listener on the html track element, when the track is loaded, the load event will be fired. Do the rest of your work with the track in this listener (reading its content, etc).<br>
  b. Check the `readyState` property of its HTML track element. If it has a value=2, then the track is loaded.

  Ans: a<br>
  Explanantion: The `readyState` property will not load the track. To load a file, set the `mode` property of its TextTrack object to "hidden" or "showing" and then use a load listener on the html track element, like in the provided example.



### 1.2.4 Working with cues


#### Live Coding Video: accessing the content of a track

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://reurl.cc/DvWK1j)


#### Properties and methods of `TextTrack` object

A `TextTrack` object has different properties and methods

+ `kind`: equivalent to the `kind` attribute of HTML track elements. Its value is either "subtitles", "caption", "descriptions", "chapters", or "metadata". We will see examples of chapters, descriptions  and metadata tracks in subsequent lessons.
+ `label`: the label of the track, equivalent of the `label` attribute of HTML `track` elements.
+ `language`: the language of the text track, equivalent to the `srclang` attribute of HTML `track` elements (be careful: it's not the same spelling!)
+ `mode`: explained earlier. Can have values equal to: "disabled"|"hidden"|"showing". Can force a track to be loaded (by setting the mode to "hidden" or "showing").
+ `cues`: get a list of cues as a `TextTrackCueList` object. This is the complete content of the WebVTT file!
+ `activeCues`: used in event listeners while the video is playing. Corresponds to the cues located in the current time segment. The start and end times of cues can overlap. In reality this may rarely happen, but this property exists in case it does, returning a  `TextTrackCueList` object that contains all active tracks at a given time.
+ `addCue(cue)`: add a cue to the list of cues.
+ `removeCue(cue)`: remove a cue from the list of cues.
+ `getCueById(id)`: returns the cue with a given `id` (not implemented by all browsers - a polyfill is given in the examples from the next lessons).


#### Properties and methods of TextTrackCueList object

__A `TextTrackCueList` is a collection of cues, each of which has different properties and methods__

+ `id`: the cue id as written in the line that starts cues in the WebVTT file.
+ `startTime` and `endTime`: define the time segment for the cue, in seconds, as a floating point value. It is not the formatted String we have in the WebVTT file (see screenshot below),
+ `text`: the cue content.
+ `getCueAsHTML()`: a method that returns an HTML version of the cue content, not as plain text.
+ Others such as `align`, `line`, `position`, `size`, `snapToLines`, etc., that correspond to the position of the cue, as specified in the WebVTT file. See the HTML5 course Part 1 about cue positioning.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3u8AKda')"
    src    = "https://bit.ly/3eYLZjM"
    alt    = "a webVtt file extract with arrows showing id, startTime, endTime and text"
    title  = "a webVtt file extract with arrows showing id, startTime, endTime and text"
  />
</figure>



#### Example that displays the content of a track

Here is [an example at JSBin](https://jsbin.com/teruhay/1/edit?html,css,js,output) that displays the content of a track:

[Local Demo](src/01b-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3u8AKda)"
    src    = "https://bit.ly/3f1jhiv"
    alt    = "Example that shows the list of cues under the video, for a given track"
    title  = "Example that shows the list of cues under the video, for a given track"
  />
</figure>


We just changed the content of the `readContent(track)` method from the example from the previous lesson:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">function</span>&nbsp;readContent<span style="color: #bb6600;">(</span>track<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">"reading content of loaded track..."</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">//displayTrackStatuses(htmlTracks);</span></li>
<li><span style="color: #880000;">&nbsp; &nbsp;// instead of displaying the track statuses, we display</span></li>
<li><span style="color: #880000;">&nbsp; &nbsp;// in the same div, the track content//</span></li>
<li><span style="color: #880000;">&nbsp; &nbsp;// first, empty the div</span></li>
<li>&nbsp; &nbsp;trackStatusesDiv<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">""</span><span style="color: #bb6600;">;</span></li>
<li><span style="color: #bb6600;"></span></li>
<li>&nbsp; &nbsp;// get the list of cues for that track &nbsp;&nbsp;</li>
<li><span style="color: #008888;">&nbsp; &nbsp;var</span>&nbsp;cues&nbsp;<span style="color: #bb6600;">=</span>&nbsp;track<span style="color: #bb6600;">.</span>cues<span style="color: #bb6600;">;</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp;// iterate on them</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">(</span><span style="color: #008888;">var</span>&nbsp;i<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">;</span>&nbsp;i&nbsp;<span style="color: #bb6600;">&lt;</span>&nbsp;cues<span style="color: #bb6600;">.</span>length<span style="color: #bb6600;">;</span>&nbsp;i<span style="color: #bb6600;">++)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; &nbsp; // current cue</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;cue&nbsp;<span style="color: #bb6600;">=</span>&nbsp;cues<span style="color: #bb6600;">[</span>i<span style="color: #bb6600;">];</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;id&nbsp;<span style="color: #bb6600;">=</span>&nbsp;cue<span style="color: #bb6600;">.</span>id&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;br&gt;"</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;timeSegment&nbsp;<span style="color: #bb6600;">=</span>&nbsp;cue<span style="color: #bb6600;">.</span>startTime&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">" =&gt; "</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;cue<span style="color: #bb6600;">.</span>endTime&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;br&gt;"</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;text&nbsp;<span style="color: #bb6600;">=</span>&nbsp;cue<span style="color: #bb6600;">.</span>text&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;P&gt;"</span></li>
<li>&nbsp; &nbsp; &nbsp; trackStatusesDiv<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">+=</span>&nbsp;id&nbsp;<span style="color: #bb6600;">+</span>&nbsp;timeSegment&nbsp;<span style="color: #bb6600;">+</span>&nbsp;text<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">}</span></li>
<li><span style="color: #bb6600;">}</span></li>
</ol></div><br>

As you can see, the code is simple: you first get the cues for the given TextTrack (it must be loaded; this is the case since we took care of it earlier), then iterate on the list of cues, and use the `id`, `startTime`, `endTime` and `text` properties of each cue.

This technique will be used in one of the next lessons, and we will show you how to make a clickable transcript on the side of the video - something quite similar to what the edX video player does.


#### Notes for 1.2.4 Working with cues

+ Properties & methods of `TextTrack` object
  + properties
    + `kind`
      + equivalent to `kind` attribute of HTML track elements
      + possible values: `"subtitles"`, `"caption"`, `"description"`, `"chapters"`, or `"metadata"`
    + `label`: the label of the track
    + `language`: the language of the text track
    + `mode`: values - "disabled"|"hidden"|"showing"
    + `cues`
      + a list of cues as a `TextTrackCueList` object
      + the complete content of the WebVTT file
    + `activeCues`
      + used in event listeners while video playing
      + corresponding to the cues located in the current time segment
      + start and end time possibly overlapped but rare
      + used for overcoming overlapped instead of only th e"current cue"
      + returning a `TextTrackCueList` object
  + methods
    + `addCue(cue)`: add a cue to the list of cues
    + `removeCue(id)`: return a cue from the list of cues
    + `getCueById(id)`: return the cue w/ a given `id`

+ Properties & methods of `TexTrackCueList` object
  + object: a collection of cues
  + `ld`: the cue id as written in the starting line of the WebVTT file
  + `startTime` and `endTime`:
    + define the time segment for the cue, in second
    + floating point value
    + not formatted String in the WebVTT file

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open('https://bit.ly/3u8AKda')"
      src    = "https://bit.ly/3eYLZjM"
      alt    = "a webVtt file extract with arrows showing id, startTime, endTime and text"
      title  = "a webVtt file extract with arrows showing id, startTime, endTime and text"
    />
  </figure>

+ Example: display the content of a track
  + function to dispay content of a track: `function readContent(track) {...}`
  + console log: `console.log("reading content of loaded track...");`
  + empty displayed msg: `trackStatusesDiv.innerHTML = "";`
  + assign variable for cues: `var cues = track.cues;`
  + iterate through all cues in the track: `for (var i=0; i < cues.length; i++) {...}`
    + set various variables w/ contents of cue: `var cue = cues[i]; var id = cue.id + "<br>"; var timeSegment = cue.startTime + " => " + "<br>"; var text = cue.text + "<p>";`
    + display the message: `trackStatusesDiv.innerHTML += id + timeSegment + text;`


#### Knowledge check 1.2.4

1. What is the name of the `TextTrack` property that returns the list of all its cues?

  a. `activeCues`<br>
  b. `cues`<br>
  c. `cueList`<br>

  Ans: c<br>
  Explanation: The `cues` property of a `TextTrack` returns the list of cues as a `TextTrackCueList` object. This is the complete content of the WebVTT file!



### 1.2.5 Listening to events

#### Live coding video: track and cue events

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3f3jW2K)

#### Cue events

Instead of reading the whole content of a track at once, like in the previous example, it might be interesting to process the track content cue by cue, while the video is being played. For example, you choose which track you want - say, German subtitles - and you want to display the subtitles in sync with the video, below the video, with your own style and animations... Or you display the entire set of subtitles to the side of the video and you want to highlight the current one... For this, you can listen for different sorts of events.

The two types of cue event are:

1. `enter` and `exit` events fired for cues.
2. `cuechange` events fired for `TextTrack` objects (good support).


#### Changing cue event

__Example of `cuechange` listener on `TextTrack`__

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #880000;">// track is a loaded TextTrack</span></li>
<li>track<span style="color: #bb6600;">.</span>addEventListener<span style="color: #bb6600;">(</span><span style="color: #008800;">"cuechange"</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(</span>e<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;cue&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>activeCues<span style="color: #bb6600;">[</span><span style="color: #006666;">0</span><span style="color: #bb6600;">];</span></li>
<li>&nbsp; &nbsp;console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">"cue change"</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// do something with the current cue</span></li>
<li>&nbsp;<span style="color: #bb6600;">});</span></li>
</ol></div>
<br>

In the above example, let's assume that we have no overlapping cues for the current time segment. The above code listens for cue change events: when the video is being played, the time counter increases. And when this time counter value reaches time segments defined by one or more cues, the callback is called. The list of cues that are in the current time segments are in `this.activeCues;` where `this` represents the track that fired the event.

In the following lessons, we show how to deal with overlapping cues (cases where we have more than one active cue).


#### Enter and exit cue events

Example of `enter` and `exit` event listeners on a track's cues

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #880000;">&nbsp;// iterate on all cues of the current track</span></li>
<li>&nbsp;var cues = track.cues;</li>
<li>&nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">(</span><span style="color: #008888;">var</span>&nbsp;i<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">,</span>&nbsp;len&nbsp;<span style="color: #bb6600;">=</span>&nbsp;cues<span style="color: #bb6600;">.</span>length<span style="color: #bb6600;">;</span>&nbsp;i&nbsp;<span style="color: #bb6600;">&lt;</span>&nbsp;len<span style="color: #bb6600;">;</span>&nbsp;i<span style="color: #bb6600;">++)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// current cue, also add enter and exit listeners to it</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;cue&nbsp;<span style="color: #bb6600;">=</span>&nbsp;cues<span style="color: #bb6600;">[</span>i<span style="color: #bb6600;">];</span></li>
<li>&nbsp; &nbsp;addCueListeners<span style="color: #bb6600;">(</span>cue<span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">...</span></li>
<li>&nbsp;}</li>
<li>&nbsp;</li>
<li><span style="color: #008888;">function</span>&nbsp;addCueListeners<span style="color: #bb6600;">(</span>cue<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; cue<span style="color: #bb6600;">.</span>onenter&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(){</li>
<li>&nbsp; &nbsp; console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">'enter cue id='</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>id<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; // do something</li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">};</span></li>
<li></li>
<li>&nbsp; cue<span style="color: #bb6600;">.</span>onexit&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(){</span></li>
<li>&nbsp; &nbsp; console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">'exit cue id='</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;cue<span style="color: #bb6600;">.</span>id<span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp; &nbsp;// do something else</li>
<li>&nbsp;&nbsp;<span style="color: #bb6600;">};</span></li>
<li><span style="color: #bb6600;">}</span>&nbsp;<span style="color: #880000;">// end of addCueListeners...</span></li>
</ol></div><br>


#### Example: Cue events

__Showing real examples of event listeners__

Here is an [example at JSBin](https://bit.ly/3wesDwM) that shows how to listen for cuechange events:

[Local Demo](src/01b-example04.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3oIkFK9')"
    src    = "https://bit.ly/3hEPQEo"
    alt    = "example that displays cue contents with cuechange even listeners"
    title  = "example that displays cue contents with cuechange even listeners"
  />
</figure>


Source code extract:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">function</span>&nbsp;readContent<span style="color: #bb6600;">(</span>track<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">"adding cue change listener to loaded track..."</span><span style="color: #bb6600;">);</span></li>
<li>&nbsp; &nbsp;trackStatusesDiv<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">""</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp;<strong>// add a cue change listener to the TextTrack</strong></li>
<li><strong>&nbsp; &nbsp;track<span style="color: #bb6600;">.</span>addEventListener<span style="color: #bb6600;">(</span><span style="color: #008800;">"cuechange"</span><span style="color: #bb6600;">,</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(</span>e<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;cue&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>activeCues<span style="color: #bb6600;">[</span><span style="color: #006666;">0</span><span style="color: #bb6600;">];</span></strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">if</span><span style="color: #bb6600;">(</span>cue&nbsp;<span style="color: #bb6600;">!==</span>&nbsp;<span style="color: #008888;">undefined</span><span style="color: #bb6600;">)</span></strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;trackStatusesDiv<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">+=</span>&nbsp;<span style="color: #008800;">"cue change: text = "</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;cue<span style="color: #bb6600;">.</span>text&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;br&gt;"</span><span style="color: #bb6600;">;</span></strong></li>
<li><strong>&nbsp; &nbsp;<span style="color: #bb6600;">});</span></strong></li>
<li></li>
<li>&nbsp; &nbsp;video<span style="color: #bb6600;">.</span>play<span style="color: #bb6600;">();</span></li>
<li><span style="color: #bb6600;">}</span></li>
</ol></div><br>

And [here](https://bit.ly/3f2oy9u) is another modified version of this example at JSBin, that shows how to use enter and exit events on cues:

[Local Demo](src/01b-example05.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3oIkFK9')"
    src    = "https://bit.ly/3eZ0Cnc"
    alt    = "Example that displays message in enter and exit cue listeners of the selected track"
    title  = "Example that displays message in enter and exit cue listeners of the selected track"
  />
</figure>


Source code extract:

<div style="padding-left: 30px; padding-right: 30px; border: 1px solid black; line-height: 25.6px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;"><ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px;">
<li value="1"><span style="color: #008888;">function</span>&nbsp;readContent<span style="color: #bb6600;">(</span>track<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;console<span style="color: #bb6600;">.</span>log<span style="color: #bb6600;">(</span><span style="color: #008800;">"adding enter and exit listeners to all cues of this track"</span><span style="color: #bb6600;">);</span></li>
<li></li>
<li>&nbsp; &nbsp;trackStatusesDiv<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008800;">""</span><span style="color: #bb6600;">;</span></li>
<li></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// get the list of cues for that track</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">var</span>&nbsp;cues&nbsp;<span style="color: #bb6600;">=</span>&nbsp;track<span style="color: #bb6600;">.</span>cues<span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;<span style="color: #880000;">// iterate on them</span></li>
<li>&nbsp; &nbsp;<span style="color: #008888;">for</span><span style="color: #bb6600;">(</span><span style="color: #008888;">var</span>&nbsp;i<span style="color: #bb6600;">=</span><span style="color: #006666;">0</span><span style="color: #bb6600;">;</span>&nbsp;i&nbsp;<span style="color: #bb6600;">&lt;</span>&nbsp;cues<span style="color: #bb6600;">.</span>length<span style="color: #bb6600;">;</span>&nbsp;i<span style="color: #bb6600;">++)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #880000;">// current cue</span></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #008888;">var</span>&nbsp;cue&nbsp;<span style="color: #bb6600;">=</span>&nbsp;cues<span style="color: #bb6600;">[</span>i<span style="color: #bb6600;">]; &nbsp;&nbsp;</span></li>
<li>&nbsp; &nbsp; &nbsp;<strong>&nbsp;addCueListeners</strong><strong><span style="color: #bb6600;">(</span>cue<span style="color: #bb6600;">);</span></strong></li>
<li>&nbsp;<span style="color: #bb6600;">}</span></li>
<li></li>
<li>video<span style="color: #bb6600;">.</span>play<span style="color: #bb6600;">();</span></li>
<li><span style="color: #bb6600;">}</span></li>
<li>&nbsp;</li>
<li><span style="color: #008888;">function</span>&nbsp;addCueListeners<span style="color: #bb6600;">(</span>cue<span style="color: #bb6600;">)</span>&nbsp;<span style="color: #bb6600;">{</span></li>
<li>&nbsp; &nbsp;cue<span style="color: #bb6600;">.</span>onenter&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(){</li>
<li><span>&nbsp; &nbsp; &nbsp; trackStatusesDiv</span><span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">+=</span>&nbsp;<span style="color: #008800;">'entered cue id='</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>id&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">" "</span></li>
<li><span style="color: #bb6600;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span>&nbsp;this<span style="color: #bb6600;">.</span>text&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;br&gt;"</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">};</span></li>
<li>&nbsp; &nbsp;cue<span style="color: #bb6600;">.</span>onexit&nbsp;<span style="color: #bb6600;">=</span>&nbsp;<span style="color: #008888;">function</span><span style="color: #bb6600;">(){</span></li>
<li>&nbsp; &nbsp; &nbsp; trackStatusesDiv<span style="color: #bb6600;">.</span>innerHTML&nbsp;<span style="color: #bb6600;">+=</span>&nbsp;<span style="color: #008800;">'exited cue id='</span>&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008888;">this</span><span style="color: #bb6600;">.</span>id&nbsp;<span style="color: #bb6600;">+</span>&nbsp;<span style="color: #008800;">"&lt;br&gt;"</span><span style="color: #bb6600;">;</span></li>
<li>&nbsp; &nbsp;<span style="color: #bb6600;">};</span></li>
<li><span style="color: #bb6600;">}</span>&nbsp;<span style="color: #880000;">// end of addCueListeners...</span></li>
</ol></ol></div><br>


#### Notes for 1.2.5 Listening to events

+ Cue events:  types of events
  + `enter` and `exit` events fired for cues
  + `cuechange` events fired for `TextTrack` objects

+ Cue change event
  + event listener: `track.addEventListener("cueChange", function(e) {...});`
    + access 1st active cue: `var cue = this.activeCues[i];`
    + console log: `console.log("cue change");`
  + assumption: no overlapped cues for the current time segment
  + video played $\to$ time counter increasing
  + `this.activeCue`: the list of cues in the current time segments, `this` representing the track firing the event

+ Cue enter and exit events
  + set variable for cues: `var cues = track.cues;`
  + iterate on all cues of the current track: `for (var i=0, len=cue.length; i < len; i++) {...}`
    + get current cue: `var cue = cues[i];`
    + exec function to add event listener: `addCueListeners(cue);`
  + event listener: `function addCueListeners(cue) {...}`
    + cue enter event: `cue.onenter = function(){ // do something };`
    + cue exit event: `cue.onexit = function(){ // do something else };`

+ Example: cue change events
  + [HTML snippet](#trackHtml)
  + display cue contents: `function readContent(track) {...}`
  + console log: `console.log("adding cue change listener to loaded track...");`
  + empty msg: `trackStatusesDiv.innerHTML = "";`
  + add cue change event listener: `track.addEventListener("cuechange", function(e){...});`
    + access $i$th active cues: `var cue = this.activeCues[0];`
    + check the existence of cue: `if (cue !== undefined) {...}`
    + append info if cue existed: `trackStatusesDiv.innerHTML += "cue change: text = " + cue.text + "<br>"";`
  + play video: `video.play();`
  + `default` attribute:
    + `var firstTrack = video.textTracks[0];`: no default attribute $\to$ not active nor hidden, but disabled $\to$ no track loaded $\to$ no even fired
    + `var firstTrack = video.textTracks[1];`: default attribute enabled $\to$ active $\to$ Deutsch track loaded $\to$ even fired as expected

+ Example: cue enter and exit events
  + dispay msg: `function readContent(track) {...}`
    + log msg: `console.log("adding enter and exit listeners to all cues of this track");`
    + empty msg container: `trackStatusesDiv.innerHTML = "";`
    + gte list of cues: `var cues = track.cues;`
    + iterate through all cues: `for (var i=0; i<cues.length; i++) {...}`
      + access 1st cue: `var cue = cues[i];`
      + add event listener: `addCueListeners(cue);`
    + play video: `play.video();`
  + add event listeners: `function addCueListeners(cue) {...}`
    + cue enter event: `cue.onenter = function() { trackStatusesDiv.innerHTML += 'entered cue id=' + this.id + " " + this.text + "<br>"; }`
    + cue exit event: `cue.onexit = function() { trackStatusesDiv.innerHTML += 'existed cue id=' + this.id + "<br>"; }`


#### Knowledge check 1.2.5

1. What conditions are necessary for a video to fire events on a particular track?

  a. The track must be loaded and the `mode` property of its `TextTrack` object must be "hidden" or "showing". Of course you have to define event listeners too in order to do something interesting.<br>
  b. No particular conditions, just add event listeners and you'll be good.

  Ans: a<br>
  Explanation: In order to fire events, a track must have been loaded and its `mode` set to "showing" or "hidden".



