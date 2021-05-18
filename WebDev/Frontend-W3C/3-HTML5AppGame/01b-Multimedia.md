# Module 1: Advanced HTML5 multimedia section


## 1.2 The Timed Text Track API


### 1.2.1 The Timed Text Track API

#### Contents

In the [W3Cx HTML5 Coding Essentials and Best Practices](https://bit.ly/3we2vSS) course, we saw that `<video>` and `<audio>` elements can have `<track>` elements. A `<track>` can have a `label`, a `kind` (subtitles, captions, chapters, metadata, etc.), a language (`srclang` attribute), a source URL (`src` attribute), etc.

Here is a small example of a video with 3 different tracks ("......" masks the real URL here, as it is too long to fit in this page width!):

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

```
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

```html
<video id="myVideo" preload="metadata" controls crossOrigin="anonymous">
    <source src="https://...../elephants-dream-medium.mp4" type="video/mp4">
    <source src="https://...../elephants-dream-medium.webm" type="video/webm">
    <track label="English subtitles" kind="subtitles" srclang="en"
           src="https://...../elephants-dream-subtitles-en.vtt" >
    <track label="Deutsch subtitles" kind="subtitles" srclang="de"
           src="https://...../elephants-dream-subtitles-de.vtt" default>
    <track label="English chapters" kind="chapters" srclang="en"
           src="https://...../elephants-dream-chapters-en.vtt">
 </video>
<div id="trackStatusesDiv">
    <h3>HTML track descriptions</h3>
</div>
```

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

```js
var video, htmlTracks;
var trackStatusesDiv;
 
window.onload = function() {
   // called when the page has been loaded
   video = document.querySelector("#myVideo");
   trackStatusesDiv = document.querySelector("#trackStatusesDiv");
   // Get the tracks as HTML elements
   htmlTracks = document.querySelectorAll("track");
   // displays their statuses in a div under the video
   displayTrackStatuses(htmlTracks);
};
 
function displayTrackStatuses(htmlTracks) {
   // displays track info
   for(var i = 0; i < htmlTracks.length; i++) {
     var currentHtmlTrack = htmlTracks[i];
     var label = "<li>label = " + currentHtmlTrack.label + "</li>";
     var kind = "<li>kind = "   + currentHtmlTrack.kind + "</li>";
     var lang = "<li>lang = "   + currentHtmlTrack.srclang + "</li>";
     var readyState = "<li>readyState = " 
                             + currentHtmlTrack.readyState + "</li>"
     trackStatusesDiv.innerHTML += "<li><b>Track:" + i + ":</b></li>"
               + "<ul>" + label + kind + lang + readyState + "</ul>";
  }
}
```

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





### 1.2.4 Working with cues





### 1.2.5 Listening to events



