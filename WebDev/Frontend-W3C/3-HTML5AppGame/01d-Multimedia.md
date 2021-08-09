# Module 1: Advanced HTML5 multimedia section


## 1.4 Creating tracks on the fly, syncing HTML content with a video

### 1.4.1 Creating tracks on the fly

In this lesson, we are going to show:

+ The `addTextTrack` method for adding a `TextTrack` to an html `<track>` element, 
+ The `VTTCue` constructor, for creating cues programmatically, and 
+ the `addCue` method for adding cues on the fly to a `TextTrack` etc.

These methods will allow us to create TextTrack objects and cues on the fly, programatically.

The presented example shows how we can create "__sound sprites__": small sounds that are parts of a mp3 file, and that can be played separately. Each sound will be defined as a cue in a track associated with the `<audio>` element.

#### Segmenting Sound File

__Let's create on the fly a WebVTT file with many cues, in order to cut a big sound file into segments and play them on demand__

[This JsBin demonstration](https://jsbin.com/lodiju/edit?html,js,output), adapted from an original demo by Sam Dutton, uses [a single mp3 file](https://mainline.i3s.unice.fr/mooc/animalSounds.mp3) that contains recorded animal sounds.

[Local Demo](src/01d-example01.html)

Below is the sound file. You can try to play it:

<p><audio src="https://mainline.i3s.unice.fr/mooc/animalSounds.mp3" controls="controls" gt="" audio=""></audio></p>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open("https://bit.ly/3ywzkfL")"
    src    = "https://bit.ly/3ws8Z0z"
    alt    = "Click a button to play an animal sound"
    title  = "Click a button to play an animal sound"
  />
</figure>


__Explanations:__

The demo uses a JavaScript array for defining the different animal sounds in this audio file:

<div style="line-height: 22.4px; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif;"><ol style="margin-top: 1em; margin-bottom: 1em; margin-left: 0px; line-height: 1.4em;">
<li value="1">&nbsp;var&nbsp;sounds&nbsp;=&nbsp;[</li>
<li value="1">&nbsp; &nbsp; {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;id:&nbsp;"purr",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;startTime:&nbsp;0.200,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;endTime:&nbsp;1.800</li>
<li>&nbsp; &nbsp;&nbsp;},</li>
<li>&nbsp; &nbsp; {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;id:&nbsp;"meow",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;startTime:&nbsp;2.300,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;endTime:&nbsp;3.300</li>
<li>&nbsp; &nbsp;&nbsp;},</li>
<li>&nbsp; &nbsp; {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;id:&nbsp;"bark",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;startTime:&nbsp;3.900,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;endTime:&nbsp;4.300</li>
<li>&nbsp; &nbsp;&nbsp;},</li>
<li>&nbsp; &nbsp; {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;id:&nbsp;"baa",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;startTime:&nbsp;5.000,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;endTime:&nbsp;5.800</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; ...</li>
<li>];</li>
</ol></div><br>

The idea is to create a track on the fly, then add cues within this track. Each cue will be created with the id, the start and end time taken from the above JavaScript object. In the end, we will have a track with individual cues located at the time location where an animal sound is in the mp3 file.

Then we generate buttons in the HTML document, and when the user clicks on a button, the `getCueById` method is called, then the start and end time properties of the cue are accessed and the sound is played (using the `currentTime` property of the audio element).

__Polyfill for `getCueById`__: Note that this method is not available on all browsers yet. A simple polyfill is used in the examples presented. If the `getCueById` method is not implemented (this is the case in some browsers), it's easy to use this small polyfill:


<div><ol>
<li value="1">&nbsp;// for browsers that do not implement the getCueById() method</li>
<li></li>
<li>&nbsp;//&nbsp;let's assume we're adding the getCueById function to a TextTrack object</li>
<li>&nbsp;//named "track"</li>
<li>if&nbsp;(typeof&nbsp;track.getCueById&nbsp;!==&nbsp;"function")&nbsp;{</li>
<li>&nbsp; &nbsp;track.getCueById&nbsp;=&nbsp;function(id)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp;var&nbsp;cues&nbsp;=&nbsp;track.cues;</li>
<li>&nbsp; &nbsp; &nbsp;for&nbsp;(var&nbsp;i&nbsp;=&nbsp;0;&nbsp;i&nbsp;!=&nbsp;track.cues.length;&nbsp;++i)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if&nbsp;(cues[i].id&nbsp;===&nbsp;id)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return&nbsp;cues[i];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp;&nbsp;};</li>
<li>&nbsp;}</li>
</ol></div><br>


#### Techniques


To add a `TextTrack` to a track element, use the [`addTextTrack` method](https://www.w3.org/TR/html5/embedded-content-0.html#text-track-api) (of the audio or video element). The function's signature is `addTextTrack(kind[,label[,language]])` where kind is our familiar choice between `subtitles`, `captions`, `chapters`, etc. The optional label is any text you'd like to use describing the track; and the optional language is from our usual list of BCP-47 abbreviations, eg 'de', 'en', 'es', 'fr' (etc).

The VTTCue constructor enables us to create our own cue class-instances programmatically. We create a cue instance by using the new keyword. The constructor function expects three familiar arguments, thus: new `VTTCue(startTime, endTime, id)` - more detail is available from [the MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Video_Text_Tracks_Format) and [the W3C's two applicable groups](https://w3c.github.io/webvtt/#the-vttcue-interface).

To add cue-instances to a TextTrack on-the-fly, use the `track` object's `addCue` method, eg `track.addCue(cue)`. The argument is a _cue instance_ - as above. Note that the track __must__ be a `TextTrack` object because `addCue` does not work with `HTMLTrackElement` Objects.

HTML source code extract:

<div style="line-height: 22.4px; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif;"><ol style="margin-top: 1em; margin-bottom: 1em; margin-left: 0px; line-height: 1.4em;">
<li value="1">...</li>
<li>&lt;h1&gt;Playing&nbsp;audio sprites&nbsp;with&nbsp;the track element&lt;/h1&gt;</li>
<li>&nbsp;&lt;p&gt;A demo&nbsp;by&nbsp;Sam&nbsp;Dutton,&nbsp;adapted&nbsp;for&nbsp;JsBin&nbsp;by&nbsp;M.Buffa&lt;/p&gt;</li>
<li>&nbsp;</li>
<li>&lt;div id="soundButtons"&nbsp;class="isSupported"&gt;&lt;/div&gt;</li>
<li>...</li>
</ol></div><br>

<div style="line-height: 22.4px; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif;"><ol style="margin-top: 1em; margin-bottom: 1em; margin-left: 0px; line-height: 1.4em;">
<li value="1">&nbsp;window.onload&nbsp;=&nbsp;function()&nbsp;{</li>
<li>&nbsp; &nbsp; // Create an audio element programmatically</li>
<li>&nbsp; &nbsp;&nbsp;var&nbsp;audio&nbsp;=&nbsp;newAudio("https://mainline.i3s.unice.fr/mooc/animalSounds.mp3");</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; audio.addEventListener("loadedmetadata",&nbsp;function()&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">// When the audio file has its metadata loaded, we can add </strong></li>
<li><strong style="line-height: 1.4em;">&nbsp; &nbsp; &nbsp; // a new track to it, with mode = hidden. It will fire events</strong></li>
<li><strong style="line-height: 1.4em;">&nbsp; &nbsp; &nbsp; // even if it is hidden</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">var&nbsp;track&nbsp;=&nbsp;audio.addTextTrack("metadata",&nbsp;"sprite track",&nbsp;"en");</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">track</strong><strong style="line-height: 1.4em;">.mode&nbsp;=&nbsp;"hidden";</strong></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// for browsers that do not implement the getCueById() method</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if&nbsp;(typeof&nbsp;track.getCueById&nbsp;!==&nbsp;"function")&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;track.getCueById&nbsp;=&nbsp;function(id)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var&nbsp;cues&nbsp;=&nbsp;track.cues;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;for&nbsp;(var&nbsp;i&nbsp;=&nbsp;0;&nbsp;i&nbsp;!=&nbsp;track.cues.length;&nbsp;++i)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if&nbsp;(cues[i].id&nbsp;===&nbsp;id)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return&nbsp;cues[i];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;};</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;var&nbsp;sounds&nbsp;=&nbsp;[</li>
<li>&nbsp; &nbsp; &nbsp; {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; id:&nbsp;"purr",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; startTime:&nbsp;0.200,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; endTime:&nbsp;1.800</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;},</li>
<li>&nbsp; &nbsp; &nbsp; {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; id:&nbsp;"meow",</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; startTime:&nbsp;2.300,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; endTime:&nbsp;3.300</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;},</li>
<li>&nbsp; &nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp;];</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;for&nbsp;(var&nbsp;i&nbsp;=&nbsp;0;&nbsp;i&nbsp;!==&nbsp;sounds.length;&nbsp;++i)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; // for each animal sound, create a cue with id, start&nbsp;and end time</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var&nbsp;sound&nbsp;=&nbsp;sounds[i];</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">var&nbsp;cue&nbsp;=&nbsp;new&nbsp;VTTCue(sound.startTime,&nbsp;sound.endTime,&nbsp;sound.id);&nbsp;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">cue</strong><strong style="line-height: 1.4em;">.id&nbsp;=&nbsp;sound.id;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">// add it to the track</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">track</strong><strong style="line-height: 1.4em;">.addCue(cue);</strong></li>
<li>&nbsp; &nbsp; &nbsp; // create a button and add it to the HTML document</li>
<li>&nbsp; &nbsp; &nbsp; document.querySelector("#soundButtons").innerHTML&nbsp;+=&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"&lt;button class='playSound' id="&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+&nbsp;sound.id&nbsp;+&nbsp;"&gt;"&nbsp;+sound.id&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+&nbsp;"&lt;/button&gt;";<br>&nbsp; &nbsp;}<br></li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;var&nbsp;endTime;</li>
<li>&nbsp; &nbsp;audio.addEventListener("timeupdate",&nbsp;function(event)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; // When we play a sound, we set the endtime var. </li>
<li>&nbsp; &nbsp; &nbsp; // We need to listen when the audio file is being played,&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; //&nbsp;in order to pause it when endTime is reached.</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if&nbsp;(event.target.currentTime&nbsp;&gt;&nbsp;endTime)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;event.target.pause();</li>
<li>&nbsp; &nbsp;});</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;function&nbsp;playSound(id)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp;// Plays the sound corresponding to the cue with id equal </li>
<li>&nbsp; &nbsp; &nbsp;// to the one passed as a parameter. We set the endTime var</li>
<li>&nbsp; &nbsp; &nbsp;// and position the audio currentTime at the start time </li>
<li>&nbsp; &nbsp; &nbsp;// of the sound</li>
<li>&nbsp; &nbsp; &nbsp;<strong style="line-height: 1.4em;">var&nbsp;cue&nbsp;=&nbsp;track.getCueById(id);</strong></li>
<li>&nbsp; &nbsp; &nbsp;audio.currentTime&nbsp;=&nbsp;cue.startTime;</li>
<li>&nbsp; &nbsp; &nbsp;endTime&nbsp;=&nbsp;cue.endTime;</li>
<li>&nbsp; &nbsp; &nbsp;audio.play();</li>
<li>&nbsp;&nbsp;};</li>
<li>&nbsp; // create listeners for all buttons</li>
<li>&nbsp; var&nbsp;buttons&nbsp;=&nbsp;document.querySelectorAll("button.playSound");<br><br></li>
<li>&nbsp; for(var i=; i &lt; buttons.length; i++) { &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;buttons[i].addEventListener("click",&nbsp;function(e)&nbsp;{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; playSound(this.id);</li>
<li>&nbsp; &nbsp; &nbsp;});</li>
<li>&nbsp; }</li>
<li>&nbsp;});</li>
<li>};</li>
</ol></div>


#### Notes for 1.4.1 Creating tracks on the fly

+ Segmenting sound file
  + sound sprites
    + small sounds as parts of a mp3 file
    + able to be played separately
  + each sound defined as a cue in a track associated w/ the `<audio>` element
  + tasks:
    + create a WebVTT file w/ many cues on the fly
    + cut a big sound file into segments
    + play segments on demand
  + defining the different animal sounds in the audio file <a name="sounds"></a>

    ```js
    var sounds = [
        { id: "purr", startTime: 0.200, endTime: 1.800 },
        { id: "meow", startTime: 2.300, endTime: 3.300 },
        { id: "bark", startTime: 3.900, endTime: 4.300 },
        { id: "baa", startTime: 5.000, endTime: 5.800 }
        ...
    ];
    ```

  + ideas
    + create a track on the fly
    + add cues within the track
    + cue created w/ the id, the start and end time taken from the above JavaScript object
    + results: a track w/ individual cues located at the time location of the animal sound file
  + implementation
    + generate buttons in the HTML document
    + excute `getCueById` method when clicked on a button
    + access the start and end time properties of the cue
    + play the sound
  + polyfill for `getCueById`:
    + no available on all browsers yet
    + JavaScript snippet to implement `getCueById`<a name="getCueById"></a>
      + check the type of track: `if (typeof track.getCueById !== "function") {...}`
      + callback function: `track.getCueById = function(d) {...};`
      + access cues: `var cues = track.cues;`
      + iterate on cues: `for (var i=0; i<track.cues.length; i++) { if (cues[i].id === id) { return cues[i]; } }`

+ Example: add cues to a track on the fly
  + `addTextTrack` method
    + syntax: `addTextTrack(kind[, label[, language]])`
    + docstring: add a TextTrack to a track element
    + parameters
      + `kind`: str; possible values - `subtitles`, `captions`, `chapters`, etc.
      + `label`: str, optional; description of the track
      + `language`: str, optional; usually using abbreviation from BCP-47, like, 'en', 'fr', 'de', etc.
  + VTTCue constructor
    + enable to create cue class-instances programmatically
    + create a cue instance by using `new` keyword
  + HTML snippet: `<div id="soundButtons"></div>`
  + JavaScript snippet
    + init page w/ DOM ready: `window.onload = function() {...}`
      + create audio element: `var audio = newAudio("https://.../animalSounds.mp3");`
      + add event listener after metadata loaded: `audio.addEventListener("loadedmetadata", function() {...});`
        + add track info: `var track = audio.addTextTrack("metadata", "sprite track", "en");`
        + assign track mode: `track.mode = "hidden";`
      + implement w/ browser w/o [getCueById](#getCueById)
    + declare [sound array](#sounds)
    + iterate on each sound: `for (var i=0; i !== sounds.length; i++) {...}`
      + create new cue and add value: `var cue = new VTTCue(sound.startTime, sound.endTime, sound.id); cue.id = sound.id;`
      + add cue to track: `track.addCue(cue);`
      + create button adn add to HTML document: `document.querySelector("#soundButtons").innerHTML += "<button class='playSound' id=" + sound.id + ">" + sound.id + "</button>";`
    + declar end time: `var endTime;`
    + add listener for end time: `audio.addEventListener("timeupdate", function(evt) { if (evt.target.currentTime > endTime) evt.target.pause(); })`
    + play sound: `function playSound(id) {...}`
      + declare cue: `var cue = track.getCueById(id);`
      + add start and end times: `audio.currentTime = cue.startTime; endTime = cue.endTime;`
      + play audio: `play.audio();`
    + access all buttons: `var buttons = document.querySelectorAll("button.playSound");`
    + iterate on adding click events: `for (var i=0; i<button.length; i++) { buttons[i].addEventListener("click", function(e) { playSound(this.id); }); }`


### 1.4.2 Update the document in sync with a media playing

Mixing JSON cue content with track and cue events, makes the synchronization of elements in the HTML document (while the video is playing) much easier.

#### Track Event Listeners and JSON Cue

__Example of track event listeners that use JSON cue contents__

Here is a small code extract that shows how we can capture the JSON content of a cue when the video reaches its start time. We do this within a `cuechange` listener attached to a `TextTrack`:

<div><ol>
<li value="1">textTrack.oncuechange = function (){</li>
<li>&nbsp; &nbsp;&nbsp;// "this" is the textTrack that fired the event.</li>
<li>&nbsp; &nbsp; // Let's get the first active cue for this time segment</li>
<li>&nbsp; &nbsp;&nbsp;var cue = this.activeCues[0];&nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;var obj = JSON.parse(cue.text);</li>
<li>&nbsp; &nbsp;&nbsp;// do something</li>
<li>}</li>
</ol></div><br>

Here is a very impressive demo by Sam Dutton that uses JSON cues containing the latitude and longitude of the camera used for filming the video, to synchronize two map views: every time the active cue changes, the Google map and equivalent Google street view are updated. 

<p>WARNING: as this Google service is no longer free of charge, you might see "for development purpose only" messages during the execution of this demo. You'll need a valid Google API key in order to remove these messages.</p>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3vetGwK")"
    src    = "https://bit.ly/3yA1INX"
    alt    = "Video synced with google map and google street map"
    title  = "Video synced with google map and google street map"
  />
</figure>


Example of a cue content from this demonstration:

<div><ol>
<li value="1">{"lat":37.4219276, "lng":-122.088218, "t":1331363000}</li>
</ol></div><br>

Cue events and cue content:

We can acquire a cue DOM object using the techniques we have seen previously, or by using the new HTML5 TextTrack `getCueById()` method. 

<div><ol>
<li value="1">var videoElement = document.querySelector("#myvideo");</li>
<li>var textTracks = videoElement.textTracks; // one for each track element</li>
<li>var textTrack = textTracks[0]; // corresponds to the first track element</li>
<li> </li>
<li><strong>// Get a cue with ID="wikipedia"</strong></li>
<li><strong>var cue = textTrack.getCueById("Wikipedia");&nbsp;</strong></li>
</ol></div><br>

And once we have a cue object, it is possible to add event listeners to it:

<div><ol>
<li value="1">cue.onenter = function(){</li>
<li>&nbsp; &nbsp;// display something, play a sound, update any DOM element...</li>
<li>};</li>
<li> </li>
<li>cue.onexit = function(){</li>
<li>&nbsp; &nbsp;// do something else</li>
<li>};</li>
</ol></div><br>

If the `getCueById` method is not implemented (this is the case in some browsers), we use the @@polyfill presented in the previous section:

<div><ol>
<li value="1">&nbsp;// for browsers that do not implement the getCueById() method</li>
<li> </li>
<li>&nbsp;//&nbsp;let's assume we're adding the getCueById function to a TextTrack object </li>
<li>&nbsp;//named "track"</li>
<li> if (typeof track.getCueById !== "function") {</li>
<li>&nbsp; &nbsp;track.getCueById = function(id) {</li>
<li>&nbsp; &nbsp; &nbsp;var cues = track.cues;</li>
<li>&nbsp; &nbsp; &nbsp;for (var i = 0; i != track.cues.length; ++i) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if (cues[i].id === id) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return cues[i];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; };</li>
<li>&nbsp;}</li>
</ol></div><br>


#### Display Web Page and Google Map While Play Video

__Example that displays a wikipedia page and a google map while a video is playing__

Try [the example at JSBin](https://jsbin.com/gucutiyoyu/2/edit?html,js,output)

[Local Demo](src/01d-example02.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3vetGwK")"
    src    = "https://bit.ly/2RHURBC"
    alt    = "video synced with an iframe that shows external URLs and with a google map"
    title  = "video synced with an iframe that shows external URLs and with a google map"
  />
</figure>


HTML code extract:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Example syncing element of the document with video metadata in webVTT file&lt;/title&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body &gt;</li>
<li>&lt;main&gt; </li>
<li>&lt;video id="myVideo" controls crossorigin="anonymous" &gt;</li>
<li>&nbsp; &nbsp;&lt;source src="https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/mp4"&gt; </li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;&lt;/source&gt;</li>
<li> &lt;track label="urls track" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; src="https://...../SamuraiPizzaCat-metadata.vtt" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; kind="metadata" &gt;</li>
<li>&nbsp;&lt;/track&gt;</li>
<li> &lt;/video&gt;</li>
<li>&nbsp; &nbsp;<strong>&nbsp;</strong><strong>&lt;div id="map"&gt;&lt;/div&gt;</strong></li>
<li> &lt;/main&gt; </li>
<li>&nbsp;</li>
<li> &lt;aside&gt;</li>
<li>&nbsp; &nbsp;&nbsp;<strong>&lt;iframe sandbox="allow-same-origin" id="myIframe" &gt; &lt;/iframe&gt;</strong></li>
<li>&lt;/aside&gt;</li>
<li> &lt;h3&gt;Wikipedia URL: &lt;span id="currentURL"&gt; Non défini &lt;/span&gt;&lt;/h3&gt;</li>
<li>&nbsp;</li>
<li> &lt;script src="https://maps.google.com/maps/api/js?sensor=false"&gt;&lt;/script&gt;</li>
<li>...</li>
</ol></div><br>

JavaScript code:

<div><ol>
<li value="1">window.onload = function() {</li>
<li>&nbsp; &nbsp; var videoElement = document.querySelector("#myVideo");</li>
<li>&nbsp; &nbsp; var myIFrame = document.querySelector("#myIframe");</li>
<li>&nbsp; &nbsp; var currentURLSpan =&nbsp;document.<mark style="background-color: pink;">querySelector</mask>("#currentURL");</li>
<li></li>
<li>&nbsp; &nbsp; var textTracks = videoElement.textTracks; // one for each track element</li>
<li>&nbsp; &nbsp; var textTrack = textTracks[0]; // corresponds to the first track element</li>
<li>&nbsp;&nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; // change mode so we can use the track</li>
<li>&nbsp; &nbsp; textTrack.mode = "hidden";</li>
<li>&nbsp;&nbsp; &nbsp;// Default position on the google map</li>
<li>&nbsp; &nbsp; var centerpos = new google.maps.LatLng(48.579400,7.7519);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; // default options for the google map</li>
<li>&nbsp; &nbsp; var optionsGmaps = {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;center:centerpos,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;navigationControlOptions: {style: </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;google.maps.NavigationControlStyle.SMALL},</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;mapTypeId: google.maps.MapTypeId.ROADMAP,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;zoom: 15</li>
<li>&nbsp; &nbsp; };</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; // Init map object</li>
<li>&nbsp; &nbsp; var map = new google.maps.Map(document.getElementById("map"), </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; optionsGmaps);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; // cue change listener, this is where the synchronization between</li>
<li>&nbsp; &nbsp; // the HTML document and the video is done</li>
<li>&nbsp; &nbsp; textTrack.oncuechange = function (){</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// we assume that we have no overlapping cues</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var cue = this.activeCues[0];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if(cue === undefined) return;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// get cue content as a JavaScript object</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var cueContentJSON = JSON.parse(cue.text);</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// do different things depending on the type of sync (wikipedia, gmap)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;switch(cueContentJSON.type) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;case'WikipediaPage': </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var myURL = cueContentJSON.url;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var myLink = "&lt;a href=\"" + myURL + "\"&gt;" + myURL + "&lt;/a&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<mark style="background-color: pink;">currentURLSpan</mark>.innerHTML = myLink;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myIFrame.src = myURL; // assign url to src property</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;break;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;case 'LongLat':</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; drawPosition(cueContentJSON.long, cueContentJSON.lat);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;break;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;} </li>
<li>&nbsp; &nbsp;};</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;function drawPosition(long, lat) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// Make new object LatLng for Google Maps</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var latlng = new google.maps.LatLng(lat, long);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// Add a marker at position</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var marker = new google.maps.Marker({</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; position: latlng,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; map: map,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; title:"You are here"</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;});</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// center map on longitude and latitude</li>
<li>&nbsp; &nbsp; &nbsp; map.panTo(latlng);</li>
<li>&nbsp; &nbsp;}</li>
<li>};</li>
</ol></div><br>

All the critical work is done by the `cuechange` event listener, _lines 27-50_. We have only the one track, so we set its mode to "hidden" (_line 10_)  in order to be sure that it will be loaded, and that playing the video will fire `cuechange` events on it. The rest is just Google map code and classic DOM manipulation for updating HTML content (a span that will display the current URL, _line 42_).


#### Notes for 1.4.2 Update the document in sync with a media playing

+ Event listeners w/ JSON cue
  + capturing the JSON content of a cue while the video reaches its start time
  + add `cuechange` event listener to `textTrack`: `textTrack.oncuechange = function() {...}`
    + declare variable for active cue: `var cue = this.activeCues[0];`
    + convert text into JSON obj: `var obj = JSON.parse(cue.text);`
    + other actions

+ Example: video tracks w/ JSON cue to sync Google map views
  + a demo by Sam Dutton
  + active cue changed $\to$ the Google map and equivalent to Google street view updated
  + example of cue content: `{"lat":37.4219276, "lng":-122.088218, "t":1331363000}`
  + cue events and cue content
    + access cue DOM object: `var videoElement = document.querySelector("#myvideo");`
    + access 1st track: `var textTracks = videoElement.textTracks; var textTrack = textTracks[0];`
    + get a cue w/ id="wikipedia": `var cue = textTrack.getCueById("Wikipedia");`
  + add event listeners to cue object
    + enter event: `cue.onenter = function() { // display sth, play a sound, update any DOM element... };`
    + exit event: `cue.onexit = function() { // do sth else };`
  + implement [`getCueById`](#getCueById) if not support

+ Example: display wikipedia page and a Google map while a video playing
  + HTML snippet
    + video element: `<video id="myVideo" controls crossorigin="anonymous"> ... </video>`
      + mp4 source: `<source src="https://.../mooc/samuraiPizzacat.mp4" type="video/mp4">...</source>`
      + vtt track: `<track label="urls track" src="https://.../samuraiPizzacat-metadata.vtt" kind="metadata"></track>`
    + map container: `<div id="map"></div>`
    + iframe container: `<aside><iframe sandbox="allow-same-origin" id="myIframe"></frame></aside>`
    + Google map: `<script src="https://maps.google.com/maps/api/js?sensor=false"></script>`
  + JavaScript snippet:
    + init page after DOM ready: `window.onload = function() {...}`
      + access elements: `var videoElement = document.querySelector("#myVideo"); var myIFrame = document.querySelector("#myIframe"); var currentURLSpan = document.querySelector("#currentURL");`
      + access cue: `var textTracks = videoElement.textTrack; var textTrack = textTracks[0];`
      + change mode: `textTrack.mode = "hidden";`
      + set position on google map: `var centerpos = new google.maps.LatLng(48.579400, 7.7519);`
      + set google map options: `var optionsGmaps = { center: centerpos, navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL}, mapTypeId: google.maps.MapTypedId.ROADMAP, zoom: 15 };`
      + init map object: `var map = new google.maps.Map(document.getElementById("map"), optionsGmaps);`
      + add cuechange event listener: `textTrack.oncuechange = function() {...}`
        + access active cue: `var cue = this.activeCues[0];`
        + exist if not available: `if (cue === undefined) return;`
        + convert text to JSON object: `var cueContentJSON = JSON.parse(cue.text);`
        + different actions according to mode: `switch(cueContentJSON.type) {...}`
        + WikipediaPage case: `case "WikipediaPage": var myURL = cueContentJSON.url; var myLink = "<a href=\"" + myURL + "\">" + "</a>"; currentURLSPan.innerHTML = myLink; myIFrame.src = myURL; break;`
        + LngLat case: `drawPosition(cueContentJSON.lng, cueContentJSON.lat); break;`
    + set marker on Google map: `function drawPosition(lng, lat) {...}`
      + create new object for map: `var latlng = new google.maps.LatLng(lat, lng);`
      + add marker at position: `var marker = new google.maps.Marker({ position: latlng, map: map, title: "You are here" });`
      + center map on longitude and latitude: `map.panTo(latlng);`



### 1.4.3 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

__Suggested topics of discussion:__

+ What other examples would need tracks to be created on the fly?
+ What tools can you find on the Web, for updating a document's content in-sync with a video? Are these tools any easier to use than  the techniques presented here?

__Optional projects:__

+ Invent something fun with audio sprites! A small graphic animation with sound effects? A concerto with cats and dogs? Look for example at this example written by a student who followed this course:

  [Demo: animation w/ sounds](https://codepen.io/w3devcampus/pen/jOqyprY)

  [Local Demo](src/01d-example03.html)

+ Create an interactive page that will display information related to the video being played. We showed a simple example with Wikipedia pages and a Google map, but you can do better than that, maybe use OpenStreetMap (that is free)! Be creative :-)




