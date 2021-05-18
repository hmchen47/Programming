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


#### Live coding video: the TextTrack object

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V000700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3ouTZfq)

The object that contains the cues (subtitles or captions or chapter description from the WebVTT file) is not the HTML track itself. It is another object that is associated with it: a `TextTrack` object!

The `TextTrack` JavaScript object has different methods and properties for manipulating track content, and is associated with different events. But before going into detail, let's see how to obtain a TextTrack object.


#### The `TextTrack` object

__Obtaining a TextTrack object that corresponds to an HTML track__

__First method: get a TextTrack from its associated HTML track__

The HTML track element has a track property which returns the associated TextTrack object. Example source code:

```js
// HTML tracks
var htmlTracks = document.querySelectorAll("track");

// The TextTrack object associated with the first HTML track
var textTrack = htmlTracks[0].track;
var kind = textTrack.kind;
var label = textTrack.label;
var lang = textTrack.language;
// etc.
```

Note that once we get a TextTrack object, we can manipulate the kind, label, language attributes (be careful, it's not srclang, like the equivalent attribute name for HTML tracks). Other attributes and methods are described later in this lesson.

Second method: get TextTrack from the HTML video element
The <video> element (and <audio> element too) has a TextTrack property accessible from JavaScript:

```js
var videoElement = document.querySelector("#myVideo");
var textTracks = videoElement.textTracks; // one TextTrack for each HTML track element
var textTrack = textTracks[0]; // corresponds to the first track element
var kind = textTrack.kind // e.g. "subtitles"
var mode = textTrack.mode // e.g. "disabled", "hidden" or "showing"
```

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
    onclick= "window.open('https://bit.ly/3fnnewM')"
    src    = "https://bit.ly/3hyvU63"
    alt    = "Same example as previous one with two buttons for force loading tracks"
    title  = "Same example as previous one with two buttons for force loading tracks"
  />
</figure>


Here is what we added to the HTML code:

```js
<button id="buttonLoadFirstTrack"
        onclick="forceLoadTrack(0);"
        disabled>
   Force load track 0
</button>
<button id="buttonLoadThirdTrack"
        onclick="forceLoadTrack(2);"
        disabled>
   Force load track 2
</button>
```

The buttons will call a function named `forceLoadTrack(trackNumber)` that takes as a parameter the number of the track to get (and force load if necessary).

Here are the additions we made to the JavaScript code from the previous example:

```js
function readContent(track) {
   console.log("reading content of loaded track...");
   displayTrackStatuses(htmlTracks); // update document with new track statuses
}
 
function getTrack(htmlTrack, callback) {
   // TextTrack associated to the htmlTrack
   var textTrack = htmlTrack.track;
   if(htmlTrack.readyState === 2) {
      console.log("text track already loaded");
      // call the callback function, the track is available
      callback(textTrack);
   } else {
      console.log("Forcing the text track to be loaded");
 
      // this will force the track to be loaded
      textTrack.mode = "hidden";
      // loading a track is asynchronous, we must use an event listener
      htmlTrack.addEventListener('load', function(e) {
         // the track is arrived, call the callback function
         callback(textTrack);
      });
   }
}
function forceLoadTrack(n) {
    // first parameter = track number,
    // second = a callback function called when the track is loaded,
    // that takes the loaded TextTrack as parameter
    getTrack(htmlTracks[n], readContent);
}
```

__Explanations:__

+ _Lines 26-31_: the function called when a button has been clicked. This function in turn calls the `getTrack(trackNumber, callback)` function. It passes the `readContent` callback function as a parameter. This is typical JavaScript asynchronous programming: the `getTrack()` function may force the browser to load the track and this can take some time (a few seconds), then when the track has downloaded, we ask the `getTrack` function to call the function we passed (the `readContent` function, which is known as a _callback_ function), with the loaded track as a parameter.
+ _Line 6_: the `getTrack` function. It first checks if the HTML track is already loaded (_line 10_). If it is, it calls the callback function passed by the caller, with the loaded TextTrack as a parameter. If the TextTrack is not loaded, then it sets its mode to "hidden". This will instruct the browser to load the track. Because that may take some time, we must use a `load` event listener on the HTML track before calling the callback function. This allows us to be sure that the track is really completely loaded.
+ _Lines 1-4_: the readContent function is only called with a loaded TextTrack. Here we do nothing special for the moment except that we refresh the different track statuses in the HTML document.


#### Knowledge check 1.2.3

1. When you force load a track, how can you be sure that it's loaded?

  a. You should define a load event listener on the html track element, when the track is loaded, the load event will be fired. Do the rest of your work with the track in this listener (reading its content, etc).<br>
  b. Check the readyState property of its HTML track element. If it has a value=2, then the track is loaded.

  Ans: 


### 1.2.4 Working with cues





### 1.2.5 Listening to events



