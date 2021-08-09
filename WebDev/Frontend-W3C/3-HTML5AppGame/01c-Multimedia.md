# Module 1: Advanced HTML5 multimedia section


## 1.3 Advanced features for audio and video players


### 1.3.1 With a clickable transcript on the side

#### Live coding video: a player with a clickable transcript

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001000_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2S50M3w)


#### Clickable transcript of a video presentation

Foreword about the set of five examples presented in this section: the code of the examples is larger than usual, but each example integrates blocks of code already presented and detailed in the previous lessons.

__Example #1: create an accessible player with a clickable transcript of the video presentation__

It might be interesting to read the content of a track before playing the video. This is what the edX video player does: it reads a single subtitle file and displays it as a transcript on the right. In the transcript, you can click on a sentence to make the video jump to the corresponding location. We will learn how to do this using the track API.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2QzbheZ")"
    src    = "https://bit.ly/3wnyEHw"
    alt    = "edX video player with clickable transcript on the right"
    title  = "edX video player with clickable transcript on the right"
  />
</figure>


#### Reading WebVTT file


__Read the WebVTT file at once using the track API and make a clickable transcript__

Here we decided to code something similar, except that we will offer a choice of track/subtitle language. Our example offers English or German subtitles, and also another track that contains the chapter descriptions (more on that later). Using a button to select a language (track), the appropriate  transcript is displayed on the right. Like the edX player, we can click on any sentence in order to force the video to jump to the corresponding location. While the video is playing, the current text is highlighted.

Some important things here:

1. Browsers do not load all the tracks at the same time, and the way they decide when and which track to load differs from one browser to another. So, when we click on a button to choose the track to display, we need to _enforce the loading of the track, if it has not been loaded yet_.
2. When a track file is loaded, then we iterate on the different cues and generate the transcript as a set of `<li>...</li>` elements. One `<li>` per cue/sentence.
3. We define the `id` attribute of the `<li>` to be the same as the cue.id value. In this way, when we click on a `<li>` we can get its `id` and find the corresponding cue start time, and make the video jump to that time location.
4. We add an `enter` and an `exit` listener to each cue. These will be useful for highlighting the current cue. Note that these listeners are not yet supported by FireFox (you can use a `cuechange` event listener on a TextTrack instead - the source code for FireFox is commented in the example).

Try [this example at JSBin](https://jsbin.com/sodihux/1/edit?html,css,js,output):

[Local Demo](src/01c-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2QzbheZ")"
    src    = "https://bit.ly/33Wezw5"
    alt    = "video player with clickable transcript"
    title  = "video player with clickable transcript"
  />
</figure>


HTML code:

<div><ol>
<li value="1">&lt;section id="all"&gt;</li>
<li> &lt;button disabled id="buttonEnglish" </li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;onclick="loadTranscript('en');</strong>"&gt;</li>
<li>&nbsp; &nbsp; Display English transcript</li>
<li>&nbsp;&lt;/button&gt;</li>
<li> &lt;button disabled id="buttonDeutsch" </li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;onclick="loadTranscript('de');</strong>"&gt;</li>
<li>&nbsp; &nbsp; Display Deutsch transcript</li>
<li>&lt;/button&gt;</li>
<li> &lt;/p&gt;</li>
<li> &lt;video id="myVideo" preload="metadata" controls crossOrigin="anonymous"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;source src="https://...../elephants-dream-medium.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/mp4"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;source src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track label="English subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind="subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang="en" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt" &gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track label="Deutsch subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind="subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang="de" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>default</strong>&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track label="English chapters" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind="chapters" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang="en" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"&gt;</li>
<li>&lt;/video&gt;</li>
<li><strong>&lt;div id="transcript"&gt;&lt;/div&gt;</strong></li>
<li>&lt;/section&gt;</li>
</ol></div><br>

CSS code:

<div><ol>
<li value="1">#all {</li>
<li>&nbsp; &nbsp;background-color: lightgrey;</li>
<li>&nbsp; &nbsp;border-radius:10px;</li>
<li>&nbsp; &nbsp;padding: 20px;</li>
<li>&nbsp; &nbsp;border:1px solid;</li>
<li>&nbsp; &nbsp;display:inline-block;</li>
<li>&nbsp; &nbsp;margin:30px;</li>
<li>&nbsp; &nbsp;width:90%;</li>
<li>}</li>
<li>&nbsp;</li>
<li>.cues {</li>
<li>&nbsp; &nbsp;color:blue;</li>
<li>}</li>
<li>&nbsp;</li>
<li>.cues:hover {</li>
<li>&nbsp; &nbsp;text-decoration: underline;</li>
<li>}</li>
<li>&nbsp;</li>
<li>.cues.current {</li>
<li>&nbsp; &nbsp;color:black;</li>
<li>&nbsp; &nbsp;font-weight: bold;</li>
<li>}</li>
<li>&nbsp;</li>
<li>#myVideo {</li>
<li>&nbsp; &nbsp;display: block;</li>
<li>&nbsp; &nbsp;float : left;</li>
<li>&nbsp; &nbsp;margin-right:&nbsp;<span style="color: #006666;" color="#006666">3%;</span></li>
<li>&nbsp; &nbsp;width: 66%;</li>
<li>&nbsp; &nbsp;background-color: black;</li>
<li>&nbsp; &nbsp;position: relative;</li>
<li>}</li>
<li>&nbsp;</li>
<li>#transcript {</li>
<li>&nbsp; &nbsp;padding: 10px;</li>
<li>&nbsp; &nbsp;border:1px solid;</li>
<li>&nbsp; &nbsp;float: left;</li>
<li>&nbsp; &nbsp;max-height: 225px;</li>
<li>&nbsp; &nbsp;overflow: auto;</li>
<li>&nbsp; &nbsp;width: 25%;</li>
<li>&nbsp; &nbsp;margin: 0;</li>
<li>&nbsp; &nbsp;font-size: 14px;</li>
<li>&nbsp; &nbsp;list-style: none;</li>
<li>}</li>
</ol></div><br>

JavaScript code:

<div><ol>
<li value="1">var video, transcriptDiv;</li>
<li>// TextTracks, html tracks, urls of tracks</li>
<li>var tracks, trackElems, tracksURLs = [];&nbsp;</li>
<li>var buttonEnglish, buttonDeutsch;</li>
<li>&nbsp;</li>
<li>window.onload = function() {</li>
<li>&nbsp; &nbsp;console.log("init");</li>
<li>&nbsp; &nbsp;// when the page is loaded, get the different DOM nodes</li>
<li>&nbsp; &nbsp;// we're going to work with</li>
<li>&nbsp;&nbsp;&nbsp;video = document.querySelector("#myVideo");</li>
<li>&nbsp; &nbsp;transcriptDiv = document.querySelector("#transcript");</li>
<li> </li>
<li>&nbsp; &nbsp;// The tracks as HTML elements</li>
<li>&nbsp; &nbsp;trackElems = document.querySelectorAll("track");<br></li>
<li></li>
<li>&nbsp; &nbsp;// Get the URLs of the vtt files</li>
<li>&nbsp; &nbsp;for(var i = 0; i &lt; trackElems.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var currentTrackElem = trackElems[i];</li>
<li>&nbsp; &nbsp; &nbsp; tracksURLs[i] = currentTrackElem.src;</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;buttonEnglish = document.querySelector("#buttonEnglish");</li>
<li>&nbsp; &nbsp;buttonDeutsch = document.querySelector("#buttonDeutsch");</li>
<li> </li>
<li>&nbsp; &nbsp;// we enable the buttons&nbsp;only in this load callback, </li>
<li>&nbsp; &nbsp;// we cannot click before the video is in the DOM</li>
<li>&nbsp; &nbsp;buttonEnglish.disabled = false;</li>
<li>&nbsp; &nbsp;buttonDeutsch.disabled = false;</li>
<li> </li>
<li>&nbsp; &nbsp;// The tracks as TextTrack JS objects</li>
<li>&nbsp; &nbsp;tracks = video.textTracks;</li>
<li>};</li>
<li>&nbsp;</li>
<li>function loadTranscript(lang) {</li>
<li>&nbsp; // Called when a button is clicked</li>
<li></li>
<li>&nbsp;&nbsp;// clear current transcript</li>
<li>&nbsp; clearTranscriptDiv();</li>
<li> </li>
<li>&nbsp;&nbsp;// set all track modes to disabled. We will only activate the</li>
<li>&nbsp;&nbsp;// one whose content will be displayed as transcript</li>
<li>&nbsp; disableAllTracks();</li>
<li> </li>
<li>&nbsp;&nbsp;// Locate the track with language = lang</li>
<li>&nbsp;&nbsp;for(var i = 0; i &lt; tracks.length; i++) {</li>
<li>&nbsp; &nbsp;&nbsp;// current track</li>
<li>&nbsp; &nbsp;&nbsp;var track = tracks[i];</li>
<li>&nbsp; &nbsp;&nbsp;var trackAsHtmlElem = trackElems[i];</li>
<li> </li>
<li>&nbsp; &nbsp; // Only subtitles/captions are ok for this example...</li>
<li>&nbsp; &nbsp;&nbsp;if((track.language === lang) &amp;&amp; (track.kind !== "chapters")) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;track.mode="showing";</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if(trackAsHtmlElem.readyState === 2) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // the track has already been loaded</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayCues(track);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayCuesAfterTrackLoaded(trackAsHtmlElem, track);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;/* Fallback for FireFox that still does not implement cue enter and exit events<br></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;track.addEventListener("cuechange", function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var cue = this.activeCues[0];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log("cue change");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var transcriptText = document.getElementById(cue.id);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transcriptText.classList.add("current");</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;});</li>
<li>&nbsp; &nbsp; &nbsp; */</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;} </li>
<li>}</li>
<li> </li>
<li>function displayCuesAfterTrackLoaded(trackElem, track) {</li>
<li>&nbsp;&nbsp;// Create a listener that will only be called once the track has</li>
<li>&nbsp;&nbsp;// been loaded. We cannot display the transcript before </li>
<li>&nbsp; // the track is loaded</li>
<li>&nbsp; &nbsp;trackElem.addEventListener('load', function(e) {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("track loaded");</li>
<li>&nbsp; &nbsp; &nbsp; displayCues(track);</li>
<li>&nbsp; &nbsp;});</li>
<li>}</li>
<li></li>
<li>function disableAllTracks() {</li>
<li>&nbsp;&nbsp;for(var i = 0; i &lt; tracks.length; i++) </li>
<li>&nbsp; &nbsp; &nbsp;// the track mode is important: disabled tracks do not fire events</li>
<li>&nbsp; &nbsp; &nbsp;tracks[i].mode = "disabled";&nbsp;</li>
<li>}</li>
<li>&nbsp;</li>
<li>function displayCues(track) {&nbsp;</li>
<li>&nbsp; &nbsp;// displays the transcript of a TextTrack</li>
<li>&nbsp; &nbsp;var cues = track.cues;</li>
<li> </li>
<li>&nbsp; &nbsp;//&nbsp;iterate on all cues of the current track</li>
<li>&nbsp; &nbsp;for(var i=0, len = cues.length; i &lt; len; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; // current cue, also add enter and exit listeners to it</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var cue = cues[i];</li>
<li>&nbsp; &nbsp; &nbsp; addCueListeners(cue);</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; // Test if the cue content is a voice &lt;v speaker&gt;....&lt;/v&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var voices = getVoices(cue.text);</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var transText="";</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if (voices.length &gt; 0) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;for (var j = 0; j &lt; voices.length; j++) { // how many voices?</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; transText += voices[j].voice + ': ' + removeHTML(voices[j].text);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;} else </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transText = cue.text; // not a voice text</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var clickableTransText = "&lt;li class='cues' id=" + cue.id </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ " onclick='jumpTo(" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+&nbsp;cue.startTime + ");'" + "&gt;" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ transText + "&lt;/li&gt;";</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; addToTranscriptDiv(clickableTransText);</li>
<li>&nbsp; &nbsp;}</li>
<li>}</li>
<li>&nbsp;</li>
<li>function getVoices(speech) {&nbsp;</li>
<li>&nbsp; &nbsp;// takes a text content and check if there are voices</li>
<li>&nbsp; &nbsp;var voices = []; // inside</li>
<li>&nbsp; &nbsp;var pos = speech.indexOf('&lt;v'); // voices are like &lt;v Michel&gt; ....</li>
<li>&nbsp; &nbsp;while (pos != -1) {</li>
<li>&nbsp; &nbsp; &nbsp; endVoice = speech.indexOf('&gt;');</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var voice = speech.substring(pos + 2, endVoice).trim();</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var endSpeech = speech.indexOf('&lt;/v&gt;');</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var text = speech.substring(endVoice + 1, endSpeech);</li>
<li>&nbsp; &nbsp; &nbsp; voices.push({</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;'voice': voice,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;'text': text</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;});</li>
<li>&nbsp; &nbsp; &nbsp; speech = speech.substring(endSpeech + 4);</li>
<li>&nbsp; &nbsp; &nbsp; pos = speech.indexOf('&lt;v');</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;return voices;</li>
<li>}</li>
<li>&nbsp;</li>
<li>function removeHTML(text) {</li>
<li>&nbsp;&nbsp;var div = document.createElement('div');</li>
<li>&nbsp; div.innerHTML = text;</li>
<li>&nbsp;&nbsp;return div.textContent || div.innerText || '';</li>
<li>}</li>
<li></li>
<li>function jumpTo(time) {</li>
<li>&nbsp; // Make the video jump at the time position + force play </li>
<li>&nbsp; // if it was not playing</li>
<li>&nbsp; video.currentTime = time;</li>
<li>&nbsp; video.play();</li>
<li>}</li>
<li>&nbsp;</li>
<li>function clearTranscriptDiv() {</li>
<li>&nbsp; transcriptDiv.innerHTML = "";</li>
<li>}</li>
<li>&nbsp;</li>
<li>function addToTranscriptDiv(htmlText) {</li>
<li>&nbsp; transcriptDiv.innerHTML += htmlText;</li>
<li>}</li>
<li>&nbsp;</li>
<li>function addCueListeners(cue) {</li>
<li>&nbsp; cue.onenter = function(){</li>
<li>&nbsp; &nbsp; &nbsp;// Highlight current cue transcript by adding the </li>
<li>&nbsp; &nbsp; &nbsp;// cue.current CSS class</li>
<li>&nbsp; &nbsp; &nbsp;console.log('enter id=' + this.id);</li>
<li>&nbsp; &nbsp; &nbsp;var transcriptText = document.getElementById(this.id);</li>
<li>&nbsp; &nbsp; &nbsp;transcriptText.classList.add("current");</li>
<li> };</li>
<li>&nbsp;</li>
<li> cue.onexit = function(){</li>
<li>&nbsp; &nbsp;console.log('exit id=' + cue.id);</li>
<li>&nbsp; &nbsp;var transcriptText = document.getElementById(this.id); </li>
<li>&nbsp; &nbsp;transcriptText.classList.remove("current");</li>
<li> };</li>
<li></li>
<li>} // end of addCueListeners...</li>
</ol></div><br>


#### Loading WebVTT file using Ajax/XHR2 

__Load a WebVTT file using Ajax/XHR2 and parse it manually__

This is an old example written in 2012 at a time when the track API was not supported by browsers. It downloads WebVTT files using Ajax and parses it "by hand". Notice the complexity of the code, compared to the previous example that uses the track API instead. We give this example as is. Sometimes, bypassing all APIs can be a valuable solution, especially when support for the track API is sporadic, as was the case in 2012...

Here is an [example at JSBin](https://jsbin.com/vedelequso/edit?html,js,output) that displays the values of the cues in the different tracks:

[Local Demo](src/01c-example02.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2QzbheZ")"
    src    = "https://bit.ly/3bAOJBZ"
    alt    = "screenshot of JsBin example: video on top and two buttons 'english' and 'german' at bottom for extracting the track contents in english or german"
    title  = "screenshot of JsBin example: video on top and two buttons 'english' and 'german' at bottom for extracting the track contents in english or german"
  />
</figure>


This example, adapted from an example from (now offline) dev.opera.com, uses some JavaScript code that takes a WebVTT subtitle (or caption) file as an argument, parses it, and displays the text on screen, in an element with an `id` of transcript.

Extract from HTML code:

<div><ol>
<li value="1"><span style="color: #008888;">...</li>
<li> &lt;video preload="metadata" controls &gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="https://..../elephants-dream-medium.mp4" type="video/mp4"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="https://..../elephants-dream-medium.webm" type="video/webm"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track label="English subtitles" kind="subtitles" srclang="en" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://..../elephants-dream-subtitles-en.vtt" default&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track label="Deutsch subtitles" kind="subtitles" srclang="de" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://..../elephants-dream-subtitles-de.vtt"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track label="English chapters" kind="chapters" srclang="en" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://..../elephants-dream-chapters-en.vtt"&gt; </li>
<li> &lt;/video&gt;</li>
<li>&nbsp;...</li>
<li>&nbsp; &nbsp;&lt;h3&gt;Video Transcript&lt;/h3&gt;</li>
<li>&nbsp; &nbsp;&lt;button onclick="loadTranscript('en');"&gt;English&lt;/button&gt;</li>
<li>&nbsp; &nbsp;&lt;button onclick="loadTranscript('de');"&gt;Deutsch&lt;/button&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;/div&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;div id="transcript"&gt;&lt;/div&gt;</li>
<li>...</li>
</ol></div><br>

JavaScript code:

<div><ol>
<li value="1">// Transcript.js, by dev.opera.com</li>
<li>function loadTranscript(lang) {</li>
<li>&nbsp; &nbsp;var url = "https://mainline.i3s.unice.fr/mooc/" + </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;'elephants-dream-subtitles-' + lang + '.vtt';</li>
<li> </li>
<li>&nbsp; &nbsp;// Will download using Ajax + extract subtitles/captions&nbsp; &nbsp;</li>
<li>&nbsp; &nbsp;loadTranscriptFile(url);&nbsp;</li>
<li>}</li>
<li>&nbsp;</li>
<li>function loadTranscriptFile(webvttFileUrl) {</li>
<li>&nbsp; &nbsp;// Using Ajax/XHR2 (explained in detail in Module 3)</li>
<li>&nbsp; &nbsp;var reqTrans = new XMLHttpRequest();</li>
<li> </li>
<li>&nbsp; &nbsp;reqTrans.open('GET', webvttFileUrl);</li>
<li> </li>
<li>&nbsp; &nbsp;// callback, called only once the response is ready</li>
<li>&nbsp; &nbsp;reqTrans.onload = function(e) {&nbsp;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var pattern = /^([0-9]+)$/;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var patternTimecode = /^([0-9]{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3}) --\&gt; ([0-9]</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3})(.*)$/;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var content = this.response; // content of the webVTT file</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var lines = content.split(/\r?\n/); // Get an array of text lines</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var transcript = '';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;for (i = 0; i &lt; lines.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var identifier = pattern.exec(lines[i]);</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// is there an id for this line, if it is, go to next line</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if (identifier) {&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;i++;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var timecode = patternTimecode.exec(lines[i]);&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// is the current line a&nbsp;timecode?</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if (timecode &amp;&amp; i &lt; lines.length) { &nbsp; &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// if it is go to next line&nbsp;&nbsp; &nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; i++;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// it can only be a text&nbsp;line now</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var text = lines[i]; &nbsp;</li>
<li> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// is the text multiline?</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;while (lines[i] !== '' &amp;&amp; i &lt; lines.length) { &nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;text = text + '\n' + lines[i];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;i++;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var transText = '';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;var voices = getVoices(text);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// is the extracted text multi voices ?&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;if (voices.length &gt; 0) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// how many voices ?</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;for (var j = 0; j &lt; voices.length; j++) {&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transText += voices[j].voice + ': ' </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ removeHTML(voices[j].text) </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ '&lt;br /&gt;';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}&nbsp;else&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// not a voice text</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transText = removeHTML(text) + '&lt;br /&gt;';&nbsp;</li>
<li></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transcript += transText;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;var oTrans = document.getElementById('transcript');</li>
<li>&nbsp; &nbsp; &nbsp;oTrans.innerHTML = transcript;</li>
<li>&nbsp; &nbsp;}</li>
<li> };</li>
<li>&nbsp;reqTrans.send(); // send the Ajax request</li>
<li>}</li>
<li>&nbsp;</li>
<li>function getVoices(speech) { &nbsp;// takes a text content and check if there are voices&nbsp;</li>
<li>&nbsp;&nbsp;var voices = []; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// inside</li>
<li>&nbsp;&nbsp;var pos = speech.indexOf('&lt;v'); // voices are like &lt;v Michel&gt; ....</li>
<li> </li>
<li>&nbsp;&nbsp;while (pos != -1) {</li>
<li>&nbsp; &nbsp; endVoice = speech.indexOf('&gt;');</li>
<li>&nbsp; &nbsp;&nbsp;var voice = speech.substring(pos + 2, endVoice).trim();</li>
<li>&nbsp; &nbsp;&nbsp;var endSpeech = speech.indexOf('&lt;/v&gt;');</li>
<li>&nbsp; &nbsp;&nbsp;var text = speech.substring(endVoice + 1, endSpeech);</li>
<li>&nbsp; &nbsp; voices.push({</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;'voice': voice,</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;'text': text</li>
<li>&nbsp; &nbsp;&nbsp;});</li>
<li>&nbsp; &nbsp; speech = speech.substring(endSpeech + 4);</li>
<li>&nbsp; &nbsp; pos = speech.indexOf('&lt;v');</li>
<li>&nbsp;&nbsp;}</li>
<li>&nbsp;&nbsp;return voices;</li>
<li>}</li>
<li>&nbsp;</li>
<li>function removeHTML(text) {</li>
<li>&nbsp;&nbsp;var div = document.createElement('div');</li>
<li>&nbsp; div.innerHTML = text;</li>
<li>&nbsp; return div.textContent || div.innerText || '';</li>
<li>}</li>
</ol></div>


#### Notes for 1.3.1 With a clickable transcript on the side

+ Example: clickable transcript
  + tasks:
    + read a single subtitle file via buttons
    + display the contents of the transcript file on the right container
    + click on cue to force the video to jump to the corresponding location
    + highlight the current text played
  + implementing procedure
    + not loading all tracks at the same time
      + different browsers deciding when and which track to load
      + click button to enforce the loading of the track if not loaded yet
    + iterate through cues and generate the transcript as a set of `<li> ... </li>`
    + define the `id` attribute of the `<li>` element
      + get `id` when clicking on the cue
      + find the corresponding cue start time
      + make the video jump to the time location
    + add `enter` and `exit` listeners
      + use for highlighting the current cue
      + Firefox no supported yet, using `cuechage` event listener instead
  + HTML snippet
    + video element<a name="videoElmt"></a>: `<video preload="metadata" controls crossOrigin="anonymous"> ... </video>`
      + MP4 video source: `<source src="https://.../elephants-dream-medium.mp4" type="video/mp4">`
      + Webm video source: `<source src="https://.../elephats-dream-medium.webm" type="video/webm">`
      + English subtitle track: `<track label="Englih subtitle" kind=subtitles srclang=en src="https://.../elephats-dream-subtitles-en.vtt">`
      + Deutsch subtitle track: `<track label="Deutsch subtitle" kind=subtitles srclang=de src="https://.../elephats-dream-subtitles-de.vtt">`
      + English capters track: `<track label="English chapters" kind=chapters srclang=en src="https://.../elephats-dream-chapters-en.vtt">`
    + button to load English transcript<a name="buttonEn"></a>: `<button disabled id="buttonEnglish" onclick="loadTranscript('en');">Display English transcript</button>`
    + button to load German transcript<a name="buttonDe"></a>: `<button disabled id="buttonDeutsch " onclick="loadTranscript('de');">Display Deutsch transcript</button>`
    + video container w/ various video sources and tracks
  + CSS style snippet<a name="css"></a>
    + cues color: `.cues {color: blue; }`
    + mouse hover cues: `.cues.hover{ text-decoration: underline; }`
    + current cue: `.cues.current{ color: black; font-weight: bold; }`
    + video container: `#myVideo{ display: block; float: left; margin-right: 3%; width: 66%; background-color: black; position: relative; }`
    + transcript container: `#transcript{ padding: 10px; border: 1px solid; float: left; max-height: 225px; overflow: auto; width: 25%; margin: 0; font-size: 14px; list-style: none; }`
  + Javascript snippet
    + declare global variables: `var video, transcriptDiv; var tracks, trackElems, trackURLs = []; var buttonEnglish, buttonDeutsch;`
    + actions after page loaded<a name="pageLoad"></a>: `window.onload = function() {...}`
      + console msg: `console.log("init");`
      + video container: `video = document.querySelector("#myVideo");`
      + transcript container: `transcriptDiv = document.querySelector("#transcript");`
      + all tracks: `trackElems = document.querySelectorAll("track);`
      + get all URLs of vtt files: `for (var i=0; i<trackElms.length; i++) {...}`
        + current track: `var currentTrackElem = trackElems[i];`
        + URL of current track: `tracksURLs[i] = currentTrackElem.src;`
      + English button: `buttonEnglish = document.querySelector("#buttonEnglish");`
      + Deutsch button: `buttonDeutsch = document.querySelector("#buttonDeutsch");`
      + disable buttons: `buttonEnglish.disabled = true; buttonDeutsch.disabled = true;`
      + access tracks: `tracks = video.textTracks;`
    + download transcript once button clicked<a name="buttonClick"></a>: `function loadTranscript(lang) {...}`
      + empty transcript container: `clearTranscriptDiv();`
      + set all track mode disabled: `disableAllTracks();`
      + iterate through all languages: `for (var i=0; i<tracks.length; i++) {...}`
        + access current track and element: `var track = tracks[i]; var trackAsHtmlElem = trackElems[i];`
        + existence of language and kind of track id: `if ((track.language === lang) && (track.kind !== "chapter")) {...}`
        + change track mode: `track.mode = "showing";`
        + display track: `displayCues(track);`
        + check track status: `if (trackAsHtml.readyState === 2) {...}`
        + call to display function if ok: `displayCues(track);`
        + call to download and display track: `displayCuesTrackLoaded(trackAsHtmlElem, track);`
        + add event listener for FireFox (no enter/exit events): `track.addEventListener("cuechange", function(e) {...})`
          + current cue: `var cue = this.activeCues[0];`
          + log msg: `console.log("cue change");`
          + get cue: `var transcriptText = document.getElementById(cue.id);`
          + change display style: `transcriptText.classList.add("current");`
    + download and display transcript<a name="downDisplay"></a>: `function displayCuesAfterTrackLoaded(trackElem, track) {...}`
      + add event listener: `trackElem.addEventListener('load', function(e) {...})`
      + log msg: `console.log("track loaded");`
      + call function to display cues: `displayCues(track);`
    + disable all tracks: `function disableAllTracks() {...}`
      + iterate through all tracks: `for (var i=0; i<tracks.length; i++) {...}`
      + disable current track: `tracks[i].mode = "disabled";`
    + display all cues of current track: `function displayCues(track) {...}`
      + get all cues: `var cues = track.cues;`
      + iterate on all cues: `for (var i=0; i<cues.length; i++) {...}`
        + get current cue and call function to add event listener: `var cue = cues[i]; addCueListeners(cue);`
        + call function to get all cues w/ voice `<v speaker>...</v>`: `var voices = getVoices(cue.text);`
        + declare transcript text variable: `var transText = "";`
        + voice existed: `if (voices.length >0) {...}`
          + existed: `for (var j=0; j<voices.length;j++) {transText += voices[j].voice + ": " + removeHTML(voices[j].text) });`
          + non-existed: `transText = cue.text;`
        + declare clickable contents: `var clickableTransText = "<li class='cues' id=" + cue.id + "onclick="jumpTo(" + cue.startTime + ");" + ">" + transText + "</li>";`
        + add to transcript container: `addToTranscriptDiv(clickableTransText);`
    + extract info for speaker and text<a name="extractInfo"></a>: `function getVoices(speech) {...}`
      + declare variables: `var voices = []; var pos = speech.indexOf('<');`
      + iterate until `pos` not existed: `while(pos != -1) {...}`
        + get various info: `endVoice = speech.indexOf('>'); var voice = speech.substring(pos + 2, endVoice).trim(); var endSpeech = speech.indexOf('</v>'); var text = speech.substring(endVoice + 1, endSpeech);`
        + append current voice: `voice.push({ 'voice': voice, 'text': text});`
        + move the position: `speech = speech.substring(endSpeech + 4); pos = speech.indexOf('<'));`
      + return all voices obtained: `return voices;`
    + remove HTML `div` element<a name="removeHTML"></a>: `function removeHTML(text) {...}`
      + access `div` element: `var div = document.createElement('div');`
      + write given text: `div.innerHTML = text;`
      + return required info: `return div.textContent || div.innerText || '';`
    + jump to a given time to play video<a name="jumpStart"></a>: `function jumpTo(time) { video.currentTime = time; video.play(); }`
    + clear transcript container: `function clearTranscriptDiv() { transcriptDiv.innerHTML = ""; }`
    + add cue to transcript container: `function addToTranscriptDiv(htmlText) { transcriptDiv.innerHTML += htmlText; }`
    + add listener to a cue<a name="addCueListener"></a>: `function addCueListeners(cue) {...}`
      + callback function for enter event: `cue.onenter = function() {...};`
        + log msg: `console.log('enter id =' + this.id);`
        + access transcript element: `vat transcriptText = document.getElementById(this.id);`
        + add highlighted style: `transcriptText.classList.add("current");`
      + callback function for exit event: `cue.onexit = function() {...};`
        + log msg: `console.log('exit id=' + cue.id);`
        + access transcript element: `var transcriptText = document.getElementById(this.id);`
        + remove highlighted style: `transcriptText.classList.remove("current");`

+ Example: download vtt file w/ Ajax/XHR2
  + used prior to the track API available
  + download WebVTT files using Ajax and parse manually
  + HTML snippet
    + [video element](#videoElmt)
    + [button for English](#buttonEn)
    + [buttone for German](#buttonDe)
  + JavaScript snippet:
    + download transcript: `function loadTranscript(lang) {...}`
      + parse URL: `var url = 'https://mainline.i3s.unice.fr/mooc/" + 'elephants-dream-subtitles-' + lang + '.vtt';`
      + download transcript: `loadTranscriptFile(url);`
    + download transcript w/ Ajax/XHR2: `function loadTranscriptFile(webvttFileUrl) {...}`
      + using Ajax/XHR2: `var reqTrans = new XMLHttpRequest(); reqTrans.open('GET', webvttFileUrl);`
      + callback once loaded: `reqTrans.onload = function (e) {...}`
        + regexp patterns: `var pattern = /^([0-9]+)$/; var patternTimecode = /^([0-9]{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3}) --\> ([0-9]{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3})(.*)$/;`
        + declare for conetnt of the webVTT: `var content = this.response;`
        + get an array of text lines: `var lines = content.split(/\r?\n/);`
        + declare transcript: `var transcript = "";`
      + iterate all lines within callback: `for (var i=0; i<lines.length; i++) {...}`
      + extract identifier from the line and check existence for each iteration: `var identifier = pattern.exec(lines[i]); if (identifier) {...}`
      + extract start time of the next line: `i++; var timecode = patternTimecode.exec(lines[i]);`
      + check start time: `if (timecode && i > lines.length) {...}`
        + get cue from the next line: `i++; var text = lines[i];`
        + move to the next text line: `while (lines[i] !== '' && i < lines.length) { text = text + '\n' + lines[i]; i++; }`
        + extract the voice: `var transText = ''; var voices = getVoices(text);`
        + iterate for multiple voices and add to the transcript text: `if (voices.length > 0) { for (var j = 0; j<voices.length; j++) { transText += voices.voice + ':' + removeHTML(voices[i].text) + '<br>'} } }`
        + not voice text: `else {transText = removeHTML(text) + '<br>'; }`
      + append to transcript text: `transcript += transText;`
      + send the Ajax request: `reqTrans.send();`
    + [extract voice](#extractInfo) from cues
    + [remove HTML](#removeHTML)


### 1.3.2 Captions, descriptions, chapters, and metadata


#### Display Video Description

__Example #2: showing video description while playing, listening to events, changing the mode of a track__

Each track has a `mode` property (and a `mode` attribute) that can be: "_disabled_", "_hidden_" or "_showing_". More than one track at a time can be in any of these states.  The difference between "_hidden_" and "_disabled_" is that hidden tracks can fire events (more on that at the end of the first example) whereas disabled tracks do not fire events.

[Here is an example at JSBin](https://jsbin.com/bixoru/1/edit?html,css,js,output) that shows the use of the `mode` property, and how to listen for cue events in order to capture the current subtitle/caption from JavaScript. You can change the mode of each track in the video element by clicking on its button. This will toggle the mode of that track. All tracks with `mode="showing"` or `mode="hidden"` will have the content of their cues displayed in real time in a small area below the video.

[Local Demo](src/01c-example02.html)

In the screen-capture below, we have a WebVTT file displaying a scene's captions and descriptions.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3oCbhrn")"
    src    = "https://bit.ly/3uiXJCp"
    alt    = "Example that shows how to toggle track modes and listen to events"
    title  = "Example that shows how to toggle track modes and listen to events"
  />
</figure>


Extract from HTML code:

<div><ol>
<li value="1">&lt;html lang="en"&gt;</li>
<li>...</li>
<li>&lt;body onload="init();"&gt;</li>
<li>...</li>
<li>&lt;p&gt;</li>
<li>&nbsp; &lt;video id="myVideo" preload="metadata" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; poster ="https://...../sintel.jpg" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; crossorigin="anonymous" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; controls="controls" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; width="640" height="272"&gt;</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="https://<span style="line-height: 25.6px;">.....</span>/sintel.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type="video/mp4" /&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="https://<span style="line-height: 25.6px;>...../sintel.webm" </span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type="video/webm" /&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track src="https://<span style="line-height: 25.6px;">.....</span>/sintel-captions.vtt" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="captions" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label="English Captions" </li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;default</strong>/&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track src="https://<span style="line-height: 25.6px;">.....</span>/sintel-descriptions.vtt" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="descriptions" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label="Audio Descriptions" /&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track src="https://<span style="line-height: 25.6px;">.....</span>/sintel-chapters.vtt" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="chapters" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label="Chapter Markers" /&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track src="https://<span style="line-height: 25.6px;">.....</span>/sintel-thumbs.vtt" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="metadata" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label="Preview Thumbs" /&gt;</li>
<li>&nbsp; &lt;/video&gt;</li>
<li>&lt;/p&gt;</li>
<li></li>
<li>&lt;p&gt;</li>
<li>&nbsp; &nbsp;&lt;div id="currentTrackStatuses"&gt;&lt;/div&gt;</li>
<li>&lt;p&gt;</li>
<li>&lt;p&gt;</li>
<li>&nbsp; &nbsp;&lt;div id="subtitlesCaptions"&gt;&lt;/div&gt;</li>
<li>&lt;/p&gt;</li>
<li></li>
<li>&lt;p&gt;</li>
<li>&nbsp; &nbsp;&lt;button onclick="clearSubtitlesCaptions();"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; Clear subtitles/captions log</li>
<li>&nbsp; &nbsp;&lt;/button&gt;</li>
<li>&lt;/p&gt;</li>
<li>&nbsp;</li>
<li> &lt;p&gt;Click one of these buttons to toggle the mode of each track:&lt;/p&gt;<br></li>
<li> &lt;button onclick="toggleTrack(0);"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;Toggle english caption track mode</li>
<li>&nbsp;&lt;/button&gt;</li>
<li>&nbsp;&lt;br&gt;</li>
<li> &lt;button onclick="toggleTrack(1);"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;Toggle audio description track mode</li>
<li>&lt;/button&gt;</li>
<li>&lt;br&gt;</li>
<li> &lt;button onclick="toggleTrack(2);"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;Toggle chapter track mode</li>
<li>&lt;/button&gt;</li>
<li>&lt;br&gt;</li>
<li>&lt;button onclick="toggleTrack(3);"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;Toggle preview thumbnail track modes</li>
<li>&lt;/button&gt;</li>
<li>&nbsp;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div><br>


JavaScript code:

<div><ol>
<li value="1">var tracks, video, statusDiv, subtitlesCaptionsDiv;</li>
<li>&nbsp;</li>
<li>function init() { </li>
<li>&nbsp; &nbsp;video = document.querySelector("#myVideo");</li>
<li>&nbsp; &nbsp;<span style="line-height: 25.6px;">statusDiv&nbsp;</span>= document.querySelector("#currentTrackStatuses");</li>
<li><span style="line-height: 1.6;">&nbsp; &nbsp;subtitlesCaptionsDiv </span><span style="line-height: 1.6;">=</span><span style="line-height: 1.6;"> document</span><span style="line-height: 1.6;">.</span><span style="line-height: 1.6;">querySelector</span><span style="line-height: 1.6;">(</span><span style="line-height: 1.6;">"#subtitlesCaptions"</span><span style="line-height: 1.6;">);</span></li>
<li>&nbsp; &nbsp;tracks = document.querySelectorAll("track");</li>
<li> </li>
<li>&nbsp; &nbsp;video.addEventListener('loadedmetadata', function() {</li>
<li>&nbsp; &nbsp; &nbsp; console.log("metadata loaded");</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// defines cue listeners for the active track; we can do this only after the video metadata have been loaded</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;for(var i=0; i&lt;tracks.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var t = tracks[i].track;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if(t.mode === "showing") {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; t.addEventListener('cuechange', logCue, false);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;// display in a div the list of tracks and their status/mode value</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;displayTrackStatus(); &nbsp;</li>
<li>&nbsp; &nbsp;&nbsp;});</li>
<li>}</li>
<li>&nbsp;</li>
<li>function displayTrackStatus() {</li>
<li>&nbsp; &nbsp; // display the status / mode value of each track. </li>
<li>&nbsp; &nbsp; // In red if disabled, in green if showing</li>
<li>&nbsp; &nbsp;&nbsp;for(var i=0; i&lt;tracks.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var t = tracks[i].track;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;var mode = t.mode;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if(mode === "disabled") {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mode = "&lt;span style='color:red'&gt;" + t.mode + "&lt;/span&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;} else if(mode === "showing") {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mode = "&lt;span style='color:green'&gt;" + t.mode + "&lt;/span&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;appendToScrollableDiv(statusDiv, "track "&nbsp;+&nbsp;i&nbsp;+&nbsp;": " + t.label </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + " "&nbsp;+&nbsp;t.kind+" in "</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +&nbsp;mode&nbsp;+&nbsp;" mode");</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>}</li>
<li>function appendToScrollableDiv(div, text) {</li>
<li>&nbsp; &nbsp;// we've got two scrollable divs. This function </li>
<li>&nbsp; &nbsp;// appends text to the div passed as a parameter</li>
<li>&nbsp; &nbsp;// The div is scrollable (thanks to CSS overflow:auto)</li>
<li>&nbsp; &nbsp;var inner = div.innerHTML;</li>
<li>&nbsp; &nbsp;div.innerHTML = inner + text + "&lt;br/&gt;";</li>
<li>&nbsp; &nbsp;// Make it display the last line appended</li>
<li>&nbsp; &nbsp;div.scrollTop = div.scrollHeight;</li>
<li> }</li>
<li>&nbsp;</li>
<li>function clearDiv(div) {</li>
<li>&nbsp; &nbsp;div.innerHTML = '';</li>
<li>}</li>
<li>&nbsp;</li>
<li>function clearSubtitlesCaptions() {</li>
<li>&nbsp; &nbsp;clearDiv(subtitlesCaptionsDiv);</li>
<li>}</li>
<li> </li>
<li>function toggleTrack(i) {</li>
<li>&nbsp; &nbsp;// toggles the mode of track i, removes the cue listener </li>
<li>&nbsp; &nbsp;// if its mode becomes "disabled"</li>
<li>&nbsp; &nbsp;// adds a cue listener if its mode was "disabled" </li>
<li>&nbsp; &nbsp;// and becomes "hidden"</li>
<li>&nbsp; &nbsp;var t = tracks[i].track;</li>
<li>&nbsp; &nbsp;switch (t.mode) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;case "disabled":</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t.addEventListener('cuechange', logCue, false);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t.mode = "hidden";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;break;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;case "hidden":</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t.mode = "showing";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;break;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;case "showing": </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t.removeEventListener('cuechange', logCue, false);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t.mode = "disabled";</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;break;</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; // updates the status</li>
<li>&nbsp; &nbsp; clearDiv(statusDiv);</li>
<li>&nbsp; &nbsp; displayTrackStatus();</li>
<li>&nbsp; &nbsp; appendToScrollableDiv(statusDiv,"&lt;br&gt;" + t.label+" are now " +t.mode);</li>
<li>}</li>
<li>&nbsp;</li>
<li>function logCue() {</li>
<li>&nbsp; &nbsp;// callback for the cue event</li>
<li>&nbsp; &nbsp;if(this.activeCues &amp;&amp; this.activeCues.length) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var t = this.activeCues[0].text; // text of current cue</li>
<li>&nbsp; &nbsp; &nbsp; appendToScrollableDiv(subtitlesCaptionsDiv, "Active "</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +&nbsp;this.kind&nbsp;+&nbsp;" changed to: "&nbsp;+&nbsp;t);</li>
<li>&nbsp; &nbsp;}</li>
<li> }</li>
</ol></div><br>


#### Notes for 1.3.2 Captions, descriptions, chapters, and metadata

+ Example: display video description
  + `mode` property: `disabled`, `hidden`, or `showing`
    + multiple tracks able to be any state
    + event difference: `hidden` tracks able to fire events while `disabled` track unable to fire events
  + tasks
    + showing the use of the `mode` property
    + listening for cue event to capture the current subtitle/caption
    + changing the mode of a track in video element by toggling on the button
  + HTML snippet
    + init page after loading: `<body onload="init();">`
    + video element: `<video id="#myVideo" preload="metadata" poster="https://.../sintel.jpg" crossorigin="anonymous" width=640 height=272>...</video>`
      + MP4 video source: `<source src="https://.../sintel.mp4" type="video/mp4">`
      + Webm video source: `<source src="https://.../sintel.webm" type="video/webm">`
      + English caption: `<track src="https://.../sintel-cpations.vtt" kind=captions label="English Captions" default/>`
      + audio descriptions:" `<track src="https://.../sintel-descriptions.vtt" kind=descriptions label="Audio Descriptions">`
      + chapter markers: `<track src="https://.../sintel-chapters.vtt" kind=chapters label="Chapter Markers">`
      + thumbnail preview: `<track src="https://.../sintel-thumbs.vtt" kind=metadata label="Preview Thumbs">`
    + clear subtitles: `<button onclick="clearSubtitlesCaptions();">Clear subtitles/captions log</button>`
    + button for English: `<button onclcik="toggleTracks(0);">Toggle english caption track mode</button>`
    + button for audio: `<button onclick="toggleTracks(1);">Toggle audio description track mode</button>`
    + button for chapter: `<button onclick="toggleTracks(2);">Toggle chapter caption track mode</button>`
    + button for preview: `<button onclick="toggleTracks(3);">Toggle preview thumbnail track mode</button>`
    + containers for track status & subtitle captions: `<p><div id="currentTrackStatuses"></div></p> <p><div id="subtitlesCaptions"></div></p>`
  + Javascript snippet
    + declar global variables: `var tracks, video, statusDiv, subtitlesCaptionsDiv;`
    + init page while page loaded: `function init() {...}`
      + access video, status, subtitle and tracks elements: `video = document.querySelector("#myVideo"); statusDiv = document.querySelector("currentTrackStatuses"); subtitlesCaptionsDiv = document.querySelector("#subtitleCations"); tracks = document.querySelectorAll("track");`
      + add event listener: `video.addEventListener('loadedmetadata', function() {...});`
        + log msg: `console.log("metadata loaded");`
        + iterate to add event listeners for all cues: `for (var i=0; i<tracks.length; i++) { var t = tracks[i].track; if (t.mode === "showing") { t.addEventListener("cuechange", logCue, false) } }`
        + display the tracks and their status/mode value: `displayTrackStatus();`
    + disply status of tracks: `function displayTrackStatus() {...}`
      + display the status / mode value of each track w/ color red if disable and color green if showing
      + iterate on all tracks: `for (var i=0; i<tracks.length; i++) {...}`
        + declare variables: `var t = tracks[i].length; var mode = t.mode;`
        + disabled mode: `if (mode === "disabled") { mode = "<span style='color: red'>" + t.mode + ""; }`
        + showing mode: `else if (mode === "showing") { mode = "<span style='color: green'>" + t.mode + "</span>" }`
        + append to container: `appendToScrollableDiv(statusDiv, "track" + i + ": " + t.label + " " + t.kind + " in " + mode + " mode");`
    + append to container: `function appendToScrollableDiv(div, text) {...}`
      + two scrollable divs
      + append text to the div passed as a parameter
      + declare variables: `var inner = div.innerHTML; div.innerHTML = inner + text + "<br/>";`
      + append to the text: `div.scrollTop = div.scrollHeight;`
    + empty div container: `function clearDiv(div) { div.innerHTML = ''; }`
    + empty subtitle container: `function clearSubstitutesCaptions() { clearDiv(subtitlesCaptionsDiv); }`
    + toggle track mode: `function toggleTrack(i) {...}`
      + declare variable: `var t = tracks[i].track;`
      + deal w/ different modes: `switch (t.mode) {...}`
        + disabled mode: `case "disabled": t.addEventListener('cuechange', logCue, false); t.mode='hidden'; break;`
        + hidden mode: `case "hidden": t.mode="showing"; break;`
        + showing mode: `case "showing": t.removeEventListener('curchange', logCue, false); t.mode="disabled"; break;`
      + update status: `clearDiv(statusDiv); displayTrackStatus(); appendToScrollableDiv(statusDiv, "<br>" + t.label + " are now " + t.mode);`
    + callback for current event: `function logCue() {...}`
      + check active cue existed: `if (this.activeCues && this.activeCues.length) {...}`
      + access current cue: `var t = this.activeCues[0].text;`
      + append text to subtitles/captions: `appendToScrollableDiv(subtitlesCaptionsDiv, "Active" + this.kind + " changed to:" + t);`


### 1.3.3 With buttons for choosing the subtitle language


#### Buttons for choosing the `subtitle` language

__Example #3: adding buttons for choosing the subtitle/caption track__

You might have noticed that with some browsers, before 2018, the standard implementation of the video element did not let the user choose the subtitle language. Now, recent browsers offers a menu to choose the track to display. 

However, before it was available, it was easy to implement this feature using the Track API.

Here is a [simple example at JSBin](https://jsbin.com/balowuq/1/edit?html,css,js,output): we added two buttons below the video to enable/disable subtitles/captions and let you choose which track you prefer.

[Local Demo](src/01c-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3hLYBMV')"
    src    = "https://bit.ly/3yytDhu"
    alt    = "Buttons for choosing the track/language under a standard video player"
    title  = "Buttons for choosing the track/language under a standard video player"
  />
</figure>


HTML code:

<div><ol>
<li value="1">...</li>
<li>&lt;body onload="init()"&gt;</li>
<li>&nbsp;...</li>
<li> &lt;video id="myVideo" preload="metadata" controls crossOrigin="anonymous" &gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;source src="https://...../elephants-dream-medium.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/mp4"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;source src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track&nbsp;&nbsp;label="English subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;srclang="en"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://<span style="line-height: 25.6px;">.....</span> /elephants-dream-subtitles-en.vtt" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>default</strong>&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track&nbsp;&nbsp;label="Deutsch subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;srclang="de"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://...../elephants-dream-subtitles-de.vtt"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track&nbsp;&nbsp;label="English chapters" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="chapters" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;srclang="en"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src="https://...../elephants-dream-chapters-en.vtt"&gt;</li>
<li> &lt;/video&gt;</li>
<li> &lt;h3&gt;Current track: &lt;span id="currentLang"&gt;&lt;/span&gt;&lt;/h3&gt;</li>
<li> &lt;div id="langButtonDiv"&gt;&lt;/div&gt; </li>
<li> &lt;/section&gt;</li>
<li>...</li>
</ol></div><br>


JavaScript code:

<div><ol>
<li value="1">var langButtonDiv, currentLangSpan, video;</li>
<li>&nbsp;</li>
<li>function init() {</li>
<li>&nbsp; &nbsp;langButtonDiv = document.querySelector("#langButtonDiv");</li>
<li>&nbsp; &nbsp;currentLangSpan = document.querySelector("#currentLang");</li>
<li>&nbsp; &nbsp;video = document.querySelector("#myVideo");</li>
<li></li>
<li>&nbsp; &nbsp;console.log("Number of tracks = " </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ video.textTracks.length);</li>
<li>&nbsp; &nbsp;// Updates the display of the current track activated</li>
<li>&nbsp; &nbsp;currentLangSpan.innerHTML = activeTrack();</li>
<li>&nbsp; &nbsp;// Build the buttons for choosing a track</li>
<li>&nbsp; &nbsp;buildButtons();</li>
<li>}</li>
<li>&nbsp;</li>
<li>function activeTrack() {</li>
<li>&nbsp; &nbsp;for (var i = 0; i &lt; video.textTracks.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;if(video.textTracks[i].mode === 'showing') {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return video.textTracks[i].label + " (" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; + video.textTracks[i].language + ")";</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;return "no subtitles/caption selected";</li>
<li>}</li>
<li>&nbsp;</li>
<li>function buildButtons() {</li>
<li>&nbsp; &nbsp;if (video.textTracks) { // if the video contains track elements</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;// For each track, create a button</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;for (var i = 0; i &lt; video.textTracks.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// We create buttons only for the caption and subtitle tracks</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var track = video.textTracks[i];</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if((track.kind !== "subtitles") &amp;&amp; (track.kind !== "captions")) </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; continue;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// create a button for track number i&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;createButton(video.textTracks[i]);&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp;}</li>
<li>}</li>
<li> </li>
<li>function createButton(track) {</li>
<li>&nbsp; &nbsp;// Create a button</li>
<li>&nbsp; &nbsp;var b = document.createElement("button");</li>
<li>&nbsp; &nbsp;b.value=track.label;</li>
<li>&nbsp; &nbsp;// use the lang attribute of the button to keep trace of the</li>
<li>&nbsp; &nbsp;// associated track language. Will be useful in the click listener</li>
<li>&nbsp; &nbsp;b.setAttribute("lang", track.language);&nbsp;</li>
<li>&nbsp; &nbsp;b.addEventListener('click', function(e) {</li>
<li>&nbsp; &nbsp; &nbsp;// Check which track is the track with the language we're looking for</li>
<li>&nbsp; &nbsp; &nbsp;// Get the value of the lang attribute of the clicked button</li>
<li>&nbsp; &nbsp; &nbsp;var lang = this.getAttribute('lang');&nbsp;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;for (var i = 0; i &lt; video.textTracks.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;if (video.textTracks[i].language == lang) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; video.textTracks[i].mode = 'showing';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; video.textTracks[i].mode = 'hidden';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;// Updates the span so that it displays the new active track</li>
<li>&nbsp; &nbsp; currentLangSpan.innerHTML = activeTrack();</li>
<li>&nbsp; });</li>
<li>&nbsp; // Creates a label inside the button</li>
<li>&nbsp; b.appendChild(document.createTextNode(track.label));</li>
<li>&nbsp; // Add the button to a div at the end of the HTML document</li>
<li>&nbsp; langButtonDiv.appendChild(b);</li>
<li>}</li>
<li> </li>
</ol></div>

#### External resources

+ If you are interested in building a complete custom video player, MDN offers an online tutorial with further information about [styling and integrating a "CC" button](https://mzl.la/3bOFgab)
+ The MDN documentation on [Web Video Text Tracks Format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (WebVTT)

#### Notes for 1.3.3 With buttons for choosing the subtitle language

+ Example: subtitle language
  + task: choose subtitle/caption track via button
  + HTML snippet
    + page full load: `<body onload="init()">`
    + [video element](#videoElmt)
    + toggle button to select subtitles: `<div id="langButtonDiv"></div>`
  + JavaScript snippet
    + declare variables: `var langButtonDiv, currentLangSpan, video;`
    + init page after fully loaded: `function init() {...}`
      + access elements: `langButtonDiv = document.querySelector("#langButtonDiv"); currentLangButton = document.querySelector("#currentLang"); video = document.querySelector("#myVideo");`
      + log msg: `console.log("Number of tracks = " + video.textTracks.length);`
      + display activated track: `currentLangSpan.innerHTML = activeTrack();`
      + build buttons: `buildButtons();`
    + active track: `function activeTrack() {...}`
      + iterate on tracks: `for (var i=0; i<video.textTracks.length; i++) {...}`
      + showing mode: `if (video.textTrack[i].mode === 'showing') { return video.textTracks[i].label + " (" + video.textTracks[i].language + ")"; }`
      + other mode: `return "no substitle/caption selected";`
    + build buttons: `function buildButtons() {...}`
      + check the existence of track: `if (video.textTracks) {...}`
      + create a button each track: `for (var i=0;i<video.textTracks.length; i++) {...}`
      + access current track: `var track = video.textTracks[i];`
      + skip mode not subtitles and captions: `if ((track.kind !== "subtitles") && (track.kind !== "captions")) continue;`
      + create button: `createButton(video.textTracks[i]);`
    + create button: `function createButton(track) {...}`
      + access element: `var b = document.createElement("button"); b.value = track.label;`
      + set `lang` attribute: `b.setAttribute("lang", track.language);`
      + add event listener: `b.addEventListener('click', function(e)) {...}`
        + get `lang` value: `var lang = this.getAttribute('lang');`
        + iterate tracks: `for (var i=0; i<video.textTracks.length; i++) {...}`
        + same language: `if (video.textTracks[i].language == lang) { video.textTracks[i].mode = 'showing'; }`
        + other language: `else { video.textTracks[i].mode = 'hidden'; }`
        + display the new active track: `currentLangSpan.innerHTML = activeTracl();`
      + create button label and add button to container: `b.appendChild(document.createTextNode(track.label)); langButtonDiv.appendChild(b);`


### 1.3.4 With a simple chapter navigation menu


#### Chapter Navigation Menu

__Example #4: making a simple chapter navigation menu__

We can use WebVTT files to define chapters. The syntax is exactly the same as for subtitles/caption .vtt files. The only difference is in the declaration of the track. Here is how we declared a chapter track in one of the previous examples (in bold in the example below):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bMOhAL')"
    src    = "https://bit.ly/3bQO13s"
    alt    = "Simple chapter navigation"
    title  = "Simple chapter navigation"
  />
</figure>

HTML code:

<div style="line-height: 25.6px;"><ol>
<li value="1">&lt;video&nbsp;id="myVideo"&nbsp;preload="metadata"&nbsp;controls&nbsp;crossOrigin="anonymous"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;source&nbsp;src="https://...../elephants-dream-medium.mp4"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/mp4"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;source&nbsp;src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track&nbsp;label="English subtitles"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind="subtitles"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang="en"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"&nbsp;&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;track&nbsp;label="Deutsch subtitles"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind="subtitles"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang="de"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;default&gt;</li>
<li>&nbsp; &nbsp; <strong>&nbsp;</strong><strong>&lt;track&nbsp;label="English chapters"</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind="<span style="color: #ff0000;">chapters"</span></strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang="en"</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"&gt;</strong></li>
<li>&lt;/video&gt;</li>
</ol></div> <br>

If we try this code in an HTML document, nothing special happens. No magic menu, no extra button!

Currently, no browser takes chapter tracks into account. You could use one of the enhanced video players presented during the HTML5 Part 1 course, but as you will see in this lesson: making your own chapter navigation menu is not complicated.

__Let's start by examining the sample `.vtt` file__

`elephant-dream-chapters-en.vtt`:

<div><ol>
<li value="1">WEBVTT</li>
<li>&nbsp;</li>
<li>chapter-1</li>
<li>00:00:00.000 --&gt; 00:00:26.000</li>
<li>Introduction</li>
<li>&nbsp;</li>
<li>chapter-2</li>
<li>00:00:28.206 --&gt; 00:01:02.000 </li>
<li>Watch out!</li>
<li>&nbsp;</li>
<li>chapter-3</li>
<li>00:01:02.034 --&gt; 00:03:10.000</li>
<li>Let's go</li>
<li>&nbsp;</li>
<li>chapter-4</li>
<li>00:03:10.014 --&gt; 00:05:40.000 </li>
<li>The machine</li>
<li>&nbsp;</li>
<li>chapter-5</li>
<li>00:05:41.208 --&gt; 00:07:26.000 </li>
<li>Close your eyes</li>
<li>&nbsp;</li>
<li>chapter-6</li>
<li>00:07:27.125 --&gt; 00:08:12.000</li>
<li>There's nothing there</li>
<li>&nbsp;</li>
<li>chapter-7</li>
<li>00:08:13.000 --&gt; 00:09:07.500</li>
<li>The Colossus of Rhodes</li>
</ol></div><br>

There are 7 cues (one for each chapter). Each cue id is the word "chapter-" followed by the chapter number, then we have the start and end time of the cue/chapter, and the cue content. In this case: the description of the chapter ("Introduction", "Watch out!", "Let's go", etc...).

Hmm... let's try to open this chapter track with the [example](https://jsbin.com/zeqoleq/1/edit?html,css,js,output) we wrote in a previous lesson - the one that displayed the clickable transcript for subtitles/captions on the right of the video. We need to modify it a little bit:

[Local Demo](src/01c-example04.html)

1. We add a "show English chapters" button with a click event listener similar to this:

  <div><ol style="list-style-type: decimal;">
  <li value="1">&lt;button disabled id="buttonEnglishChapters" <strong>onclick="loadTranscript('en', <span style="color: #ff0000;">'chapters'</span>);"</strong>&gt;</li>
  <li>&nbsp; &nbsp; Display English chapter markers</li>
  <li>&lt;/button&gt;<br></li>
  </ol></div>

2. We modify the `loadTranscript` function from the previous example, so that it matches both the `srclang` and the `kind` attribute of the track.

  Here is a new version: in bold are the source code lines we modified.

  <div><ol style="list-style-type: decimal;">
  <li value="1">function loadTranscript(lang,<span style="color: #ff0000;"> kind</span>) {</li>
  <li>&nbsp; &nbsp;...</li>
  <li> </li>
  <li>&nbsp; &nbsp;// Locate the track with&nbsp;lang and kind that match the parameters</li>
  <li>&nbsp; &nbsp;for(var i = 0; i &lt; tracks.length; i++) {</li>
  <li>&nbsp; &nbsp; &nbsp;&nbsp;...</li>
  <li> </li>
  <li>&nbsp; &nbsp; &nbsp;&nbsp;<strong>if((track.language === lang) &amp;&amp; (track.kind ===<span style="color: #ff0000;"> kind</span>)) {</strong></li>
  <li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// display it contents...</li>
  <li>&nbsp; &nbsp; &nbsp;&nbsp;}</li>
  <li>&nbsp; &nbsp;} </li>
  <li>}</li>
  </ol></div>


#### Clickable Chapters

Simple approach: chapters as clickable text on the right of the video

[Try it on JSBin](https://jsbin.com/rifekik/edit?html,css,js): this version includes the modifications we presented earlier - nothing more. Notice that we kept the existing buttons to display a clickable transcript:

[Local Demo](src/01c-example05.html)

Look at the JavaScript and HTML tab of the JSBin example to see the source code. It's the same as in the clickable transcript example, except for the small changes we explained earlier.

Chapter navigation, illustrated in the video player below, is fairly popular.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3bMOhAL')"
    src    = "https://bit.ly/3fbqfkM"
    alt    = "Example of video player that uses text based chapter navigation"
    title  = "Example of video player that uses text based chapter navigation"
  />
</figure>

In addition to the clickable chapter list, this one displays an enhanced progress bar created using a canvas. The small squares are drawn corresponding to the chapter cues' start and end times. You could modify the code provided, in order to add such an enhanced progress indicator.

However, we will see how we can do better by using JSON objects as cue contents. This will be the topic of the next two lessons!


#### Notes for 1.3.4 With a simple chapter navigation menu

+ VebVTT file and chapters
  + using WebVTT files to define chapters
  + task: display subtitles/caption into `.vtt` files
  + HTML snippet: [video element](#videoElmt)
  + no browser taking chapter track in account
  + example of `.vtt` file <a name="vtt"></a>

    ```vtt
    WEBVTT

    chapter-1
    00:00:00.000 --> 00:00:26.000
    Introduction

    chapter-2
    00:00:28.206 --> 00:01:02.000
    Watch out!
    ...
    ```

    + cue id: `chapter-` + chapter number
    + start and end time of the cue/chapter
    + description of the chapter: `Introduction`, `Watch out!`, etc.

+ Example: display English chapters
  + HTML snipper:
    + display English chapter w/ button: `<button disabled id="buttonEnglishChapters" onclick="loadTranscript('en', , 'chapters');">Display English chapter markers</button>`
  + JavaScript snippet:
    + revise [`loadTranscript`](#buttonClick) w/ `kind` property: `function loadTranscript(lang, kind);`
    + check to display text: `if ((track.language === lang) && (track.kind === kind)) {...}`

+ Example: clickable chapters
  + task: chapters as clickable text
  + same as `dispaly English chapters` example except for chapters


### 1.3.5 With thumbnails, using JSON cues


#### Chapter Menu w/ Image Thumbnails

__Example #5: create a chapter menu with image thumbnails__

Instead of using text (optionally using HTML for styling, multi lines, etc.), it is also possible to use JSON objects as cue values that can be manipulated from JavaScript. JSON means "JavaScript Object Notation". It's an open standard for describing JavaScript objects as plain text.

Here is an example cue from a WebVTT file encoded as JSON instead of plain text. JSON is useful for describing "structured data"', and processing such data from JavaScript is easier than parsing plain text.

<div><ol>
<li value="1">WEBVTT</li>
<li> </li>
<li>Wikipedia</li>
<li>00:01:15.200 --&gt; 00:02:18.800</li>
<li><strong style="color: olive;">{</strong></li>
<li><strong style="color: olive;">&nbsp; &nbsp;"title": "State of Wikipedia",</strong></li>
<li><strong style="color: olive;">&nbsp; &nbsp;"description": "Jimmy Wales talking ...",</strong></li>
<li><strong style="color: olive;">&nbsp; &nbsp;"src": "https://upload.wikimedia.org/...../120px-Wikipedia-logo-v2.svg.png",</strong></li>
<li><strong style="color: olive;">&nbsp; &nbsp;"href": "https://en.wikipedia.org/wiki/Wikipedia"</strong></li>
<li><strong style="color: olive;">}</strong></li>
</ol></div><br>

This JSON object (in bold olive) is a JavaScript object encoded as a text string. If we listen for cue events or if we read a WebVTT file as done in previous examples, we can extract this text content using the `cue.text` property. For example:

<div><ol>
<li value="1">var videoElement = document.querySelector("#myvideo");</li>
<li>var textTracks = videoElement.textTracks; // one for each track element</li>
<li>var textTrack = textTracks[0]; // corresponds to the first track element</li>
<li> </li>
<li>var cues = textTrack.cues;</li>
<li>var cue = cues[0]; // first cue</li>
<li> </li>
<li><strong>// cue.text is in JSON format, with JSON.parse we turn it back </strong></li>
<li><strong>// to a real JavaScript object</strong></li>
<li><strong>var obj = JSON.parse(cue.text);&nbsp;</strong></li>
<li> </li>
<li>var title = obj.title; // "State of Wikipedia"</li>
<li>var description = obj.description; // Jimmy Wales talking...</li>
<li>etc...</li>
</ol></div><br>

This is a powerful way of embedding metadata, especially when used in conjunction with listening for cue and track events.


#### Better Chapter Menu w/ Enriched Chapter Markers

__Improved approach: make a nicer chapter menu by embedding a richer description of chapter markers__

Earlier we saw [an example](https://jsbin.com/jiyodit/edit?html,css,js,output) that could display chapter markers as clickable text on the right of a video.

[Local Demo](src/01c-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9')"
    src    = "https://bit.ly/3bQO13s"
    alt    = "Simple chapter menu in plain text"
    title  = "Simple chapter menu in plain text"
  />
</figure>

This example used only standard plain text content for the cues:

<div><ol>
<li value="1">WEBVTT</li>
<li>&nbsp;</li>
<li>chapter-1</li>
<li>00:00:00.000 --&gt; 00:00:26.000</li>
<li>Introduction</li>
<li>&nbsp;</li>
<li>chapter-2</li>
<li>00:00:28.206 --&gt; 00:01:02.000 </li>
<li>Watch out!</li>
<li>&nbsp;...</li>
</ol></div>

We used this example to manually capture the images from the video that correspond to each of the seven chapters:

+ We clicked on each chapter link on the right, then paused the video,
+ then we used a screen capture tool to grab each image that corresponds to the beginning of chapter,
+ Finally, we resized the images with Photoshop to approximately 200x400 pixels.

(For advanced users: it's possible to semi-automatize this process using the [ffmepg](https://www.ffmpeg.org/) command line tool, see for example [this](https://bit.ly/3fGTbA9) and [that](https://bit.ly/3wtsVQJ)).

Here are the images which correspond to the seven chapters of the video from the previous example:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3bQuyA9" ismap target="_blank">
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3ywRhe8"
      alt   = "chapter 1 thumbnail"
      title = "chapter 1 thumbnail"
    >
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/346FO7c"
      alt   = "chapter 2 thumbnail"
      title = "chapter 2 thumbnail"
    >
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/2QHXVx0"
      alt   = "chapter 3 thumbnail"
      title = "chapter 3 thumbnail"
    >
  </a><a href="url" ismap target="_blank">
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3hIoBJg"
      alt   = "chapter 4 thumbnail"
      title = "chapter 4 thumbnail"
    >
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3fcKhLS"
      alt   = "chapter 5 thumbnail"
      title = "chapter 5 thumbnail"
    >
  </a>
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3vgkHLE"
      alt   = "chapter 6 thumbnail"
      title = "chapter 6 thumbnail"
    >
  </a>
</div>

To associate these images with its chapter description, we will use JSON objects as cue contents:

[elephants-dream-chapters-en-JSON.vtt](https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en-JSON.vtt):

<div><ol>
<li value="1">WEBVTT</li>
<li>&nbsp;</li>
<li>chapter-1</li>
<li>00:00:00.000 --&gt; 00:00:26.000</li>
<li>{</li>
<li> "description": "Introduction",</li>
<li> "image": "introduction.jpg"</li>
<li>}</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li>chapter-2</li>
<li>00:00:28.206 --&gt; 00:01:02.000 </li>
<li>{</li>
<li> "description": "Watch out!",</li>
<li> "image": "watchOut.jpg"</li>
<li>}</li>
<li>...</li>
</ol></div><br>

Before explaining the code, we propose that you [try this example at JSBin](https://jsbin.com/pulefe/1/edit?html,css,js,output) that uses this new `.vtt` file:

[Local Demo](src/01c-example07.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9')"
    src    = "https://bit.ly/3wyNATD"
    alt    = "Video with nice chapter menu that uses thumbnail images"
    title  = "Video with nice chapter menu that uses thumbnail images"
  />
</figure>


HTML code:

<div><ol>
<li value="1">...</li>
<li>&lt;video id="myVideo" preload="metadata" controls crossOrigin="anonymous"&gt;</li>
<li> &lt;source src="https://...../elephants-dream-medium.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/mp4"&gt;</li>
<li> &lt;source src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li> &lt;track label="English subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; kind="subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; srclang="en" src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt" &gt;</li>
<li> &lt;track label="Deutsch subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; kind="subtitles" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; srclang="de" src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt" default&gt;</li>
<li> <strong>&lt;track label="English chapters" </strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="chapters" </strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; srclang="en" src="https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-chapters-en-<span style="color: #ff0000;">JSON.vtt"&gt;</span></strong></li>
<li> &lt;/video&gt; </li>
<li> &lt;h2&gt;Chapter menu&lt;/h2&gt;</li>
<li> <strong>&lt;div id="chapterMenu"&gt;&lt;/div&gt;</strong></li>
<li>&nbsp;...</li>
</ol></div><br>

It's the same code we had in the first example, except that this time we use a new WebVTT file that uses JSON cues to describe each chapter. For the sake of simplicity, we also removed the buttons and all the code for displaying a clickable transcript of the subtitles/captions on the right of the video.

JavaScript code:

<div><ol>
<li value="1">var video, chapterMenuDiv;</li>
<li>var tracks, trackElems, tracksURLs = [];</li>
<li>&nbsp;</li>
<li>window.onload = function() {</li>
<li>&nbsp; &nbsp;console.log("init");</li>
<li>&nbsp; &nbsp;// When the page is loaded</li>
<li>&nbsp; &nbsp;video = document.querySelector("#myVideo");</li>
<li>&nbsp; &nbsp;chapterMenuDiv = document.querySelector("#chapterMenu");</li>
<li> </li>
<li>&nbsp; &nbsp;// Get the tracks as HTML elements</li>
<li>&nbsp; &nbsp;trackElems = document.querySelectorAll("track");</li>
<li>&nbsp; &nbsp;for(var i = 0; i &lt; trackElems.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var currentTrackElem = trackElems[i];</li>
<li>&nbsp; &nbsp; &nbsp; tracksURLs[i] = currentTrackElem.src;</li>
<li>&nbsp; &nbsp;}</li>
<li> </li>
<li>&nbsp; &nbsp;// Get the tracks as JS TextTrack objects</li>
<li>&nbsp; &nbsp;tracks = video.textTracks;</li>
<li> </li>
<li><span style="color: #880000; line-height: 25.6px;">&nbsp; &nbsp;<strong>//&nbsp;Build the chapter navigation menu for the given lang and kind</strong></span></li>
<li><strong>&nbsp; &nbsp;buildChapterMenu('en', 'chapters');</strong></li>
<li>};</li>
<li>&nbsp;</li>
<li>function buildChapterMenu(lang, kind) {</li>
<li>&nbsp;&nbsp;// Locate the track with language = lang and kind="chapters"</li>
<li>&nbsp;&nbsp;for(var i = 0; i &lt; tracks.length; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;// current track</li>
<li>&nbsp; &nbsp; &nbsp;var track = tracks[i];</li>
<li>&nbsp; &nbsp; &nbsp;var trackAsHtmlElem = trackElems[i];</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;if((track.language === lang) &amp;&amp; (track.kind === kind)) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// the track must be active,&nbsp;otherwise it will not load</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; track.mode="showing"; // "hidden" would work too</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;if(trackAsHtmlElem.readyState === 2) {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// the track has already been loaded</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;displayChapterMarkers(track);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;displayChapterMarkersAfterTrackLoaded(trackAsHtmlElem, track);</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; &nbsp;}</li>
<li>&nbsp; &nbsp;} </li>
<li>}</li>
<li>&nbsp;</li>
<li>function&nbsp;<spanline-height: 25.6px;">displayChapterMarkers(track) {</li>
<li>&nbsp; &nbsp;var cues = track.cues;</li>
<li> </li>
<li>&nbsp; &nbsp;// We must not see the cues on the video</li>
<li>&nbsp; &nbsp;track.mode = "hidden";</li>
<li></li>
<li>&nbsp; &nbsp;// Iterate on cues</li>
<li>&nbsp; &nbsp;for(var i=0, len = cues.length; i &lt; len; i++) {</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var cue = cues[i];</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp;<strong>&nbsp;</strong><strong>var cueObject = JSON.parse(cue.text);</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; var description = cueObject.description;</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;&nbsp;var imageFileName = cueObject.image;</strong></li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var imageURL = "https://mainline.i3s.unice.fr/mooc/" + imageFileName;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;//&nbsp;Build the marker. It's a figure with an img and a figcaption inside.</li>
<li>&nbsp; &nbsp; &nbsp; // The img has an onclick listener that will make the video jump</li>
<li>&nbsp; &nbsp; &nbsp; // to the start time of the current cue/chapter</li>
<li>&nbsp; &nbsp; &nbsp;&nbsp;var figure = document.createElement('figure');</li>
<li>&nbsp; &nbsp; &nbsp; figure.classList.add("img");</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; figure.innerHTML = "&lt;img onclick='jumpTo(" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ cue.startTime + ");' class='thumb' src='" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ imageURL&nbsp;+ "'&gt;&lt;figcaption class='desc'&gt;" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+ description + "&lt;/figcaption&gt;&lt;/figure&gt;";</li>
<li>&nbsp; &nbsp; &nbsp; // Add the figure to the chapterMenuDiv</li>
<li>&nbsp; &nbsp; &nbsp; chapterMenuDiv.insertBefore(figure, null);</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li> }</li>
<li>&nbsp;</li>
<li>function displayChapterMarkersAfterTrackLoaded(trackElem, track) {</li>
<li>&nbsp;&nbsp;// Create a listener that will only be called when the track has</li>
<li>&nbsp;&nbsp;// been loaded</li>
<li>&nbsp; trackElem.addEventListener('load', function(e) {</li>
<li>&nbsp; &nbsp; &nbsp;console.log("chapter track loaded");</li>
<li>&nbsp; &nbsp; &nbsp;<span style="line-height: 25.6px;">displayChapterMarkers(track);</span></li>
<li>&nbsp;&nbsp;});</li>
<li>}</li>
<li>&nbsp;</li>
<li>function jumpTo(time) {</li>
<li>&nbsp; video.currentTime = time;</li>
<li>&nbsp; video.play();</li>
<li>}</li>
<li>&nbsp;</li>
</ol></div><br>


__Explanations:__

+ _Lines  4-18_: when the page is loaded, we assemble all of the track HTML elements and their corresponding TextTrack objects.
+ _Line 19_: using that we can build the chapter navigation menu. All is done in the `window.onload` callback, so nothing happens until the DOM is ready.
+ _Lines 24-43_: the `buildChapterMenu` function first locates the chapter track for the given language, then checks if this track has been loaded by the browser. Once it has been confirmed that the track is loaded, the function `displayChapters` is called.
+ _Lines 45-65_: the `displayChapters(track)` function will iterate over all of the cues within the chapter track passed as its parameter. For each cue, the JSON content is re-formatted back into a JavaScript object (_line 55_) and the image filename and description of the chapter/cue are extracted (_lines 56-57_). Then an HTML description for the chapter is built and added to the `div` element with `id=chapterMenu`. Here is the HTML code for one menu marker:

  <div><ol style="list-style-type: decimal;">
  <li value="1">&lt;figure class="<g id="127" data-gr-id="127">img</g>"&gt;</li>
  <li>&nbsp; &nbsp;&lt;img onclick="jumpTo(0);" class="thumb" src="https://...../introduction.jpg"&gt;</li>
  <li>&nbsp; &nbsp;&lt;figcaption class="desc"&gt;</li>
  <li>&nbsp; &nbsp; &nbsp; Introduction</li>
  <li>&nbsp; &nbsp;&lt;/figcaption&gt;</li>
  <li>&lt;/figure&gt;</li>
  </ol></div><br>

Notice that we add a click listener to each thumbnail image. Clicking a chapter thumbnail will cause the video to jump to the chapter time location (the example above is for the first chapter with start time = 0).

We also added CSS classes "img", "thumb" and "desc", which make it easy to style and position the thumbnails using CSS.

CSS source code extract:

<div><ol>
<li value="1">#chapterMenuSection {</li>
<li>&nbsp; &nbsp;background-color: lightgrey;</li>
<li>&nbsp; &nbsp;border-radius:10px;</li>
<li>&nbsp; &nbsp;padding: 20px;</li>
<li>&nbsp; &nbsp;border:1px solid;</li>
<li>&nbsp; &nbsp;display:inline-block;</li>
<li>&nbsp; &nbsp;margin:0px 30px 30px 30px;</li>
<li>&nbsp; &nbsp;width:90%;</li>
<li>}</li>
<li>&nbsp;</li>
<li>figure.img {</li>
<li>&nbsp; margin: 2px;</li>
<li>&nbsp;&nbsp;float: left;</li>
<li>}</li>
<li>&nbsp;</li>
<li>figcaption.desc {</li>
<li>&nbsp; text-align: center;</li>
<li>&nbsp; font-weight: normal;</li>
<li>&nbsp; margin: 2px;</li>
<li>}</li>
<li>&nbsp;</li>
<li>.thumb {</li>
<li>&nbsp; height: 75px;</li>
<li>&nbsp; border: 1px solid #000;</li>
<li>&nbsp; margin: 10px 5px 0 0;</li>
<li>&nbsp; box-shadow: 5px 5px 5px grey;</li>
<li>&nbsp; transition: all 0.5s;</li>
<li>}</li>
<li>&nbsp;</li>
<li>.thumb:hover {</li>
<li>&nbsp; box-shadow: 5px 5px 5px black;</li>
<li>}</li>
</ol></div><br>

A sample menu marker is shown below (it's also animated - hover your mouse over the thumbnail to see its animated shadow):


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9')"
    src    = "https://bit.ly/3ffAvsx"
    alt    = "Introduction"
    title  = "Introduction"
  />
</figure>


#### Chapter Menu w/ Clickable Transcript

__Combining techniques: a clickable transcript and a chapter menu__

This example is the same as the previous one except that we have kept the features that we saw previously: the buttons for displaying a clickable transcript. The code is longer, but it's just a combination of the "clickable transcript" example from the previous lesson, and the code from earlier in this lesson.

[Try it at JSBin](https://jsbin.com/zewemaj/edit?html,js,output)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9")"
    src    = "https://bit.ly/3ucOkfp"
    alt    = "Chapter menu + clickable transcript"
    title  = "Chapter menu + clickable transcript"
  />
</figure>


#### Notes for 1.3.5 With thumbnails, using JSON cues

+ WebVTT file w/ JSON
  + possible to use JSON as cue values
  + able to manipulate JSON from JavaScript
  + able to be extracted JSON object w/ `cue.text`
  + a powerful way of embedding metadata
  + particularly used in conjunction w/ listening for cue and track events

+ Example: extract JSON object from WebVTT file
  + text within curly brackets `{...}` as a JSON object

    ```json
    WEBVTT
    Wikipedia
    00:01:15.200 --> 00:02:18.800
    {
      "title": "State of Wikipedia",
      "description": "Jimmy Wales talking ...",
      "src": "https://upload.wikimedia.org/...../120px-Wikipedia-logo-v2.svg.png",
      "href": "https://en.wikipedia.org/wiki/Wikipedia"
    }
    ```
  
  + JavaScript snippet:
    + declare variables for various elements: `var videoElement = document.querySelector("#myVideo"); var textTracks = videoElement.textTracks; var textTrack = textTracks[0];`
    + declare variables for cues: `var cues = textTrack.cues; var cue = cues[0];`
    + convert JSON text into JSON object: `var obj = JSON.parse(cue.text);`
    + access description: `var description = obj.description;`

+ Example: chapter menu w/ description of chapter markers
  + procedure: manually capture the images from the video file
    + click on each chapter link to pause video
    + using a screen capture tool to grape each image corresponding to the beginning of chapter
    + resizing the images approximately 200x400 pixels
  + WebVTT w/ chapter

    ```json
    WEBVTT
    
    chapter-1
    00:00:00.000 --> 00:00:26.000
    {
      "description": "Introduction",
      "image": "introduction.jpg"
    }
    
    chapter-2
    00:00:28.206 --> 00:01:02.000
    {
      "description": "Watch out!",
      "image": "watchOut.jpg"
    }
    ...
    ```

  + HTML snippet
    + same as [video element](#videoElmt)
    + resvised chapter track w/ JSON: `<track label="English chapters" kind=chapters srclang="https://.../elephants-dream-chapters-en-JSON.vtt">`
    + create chapter container: `<div id="chapterMenu"></div>`
    + no button left but thumbnails created by JavaScript snippet
  + JavaScript snippet
    + declare variables: `var video, chapterMenuDiv; var tracks, trackElems, tracksURLs = [];`
    + init page after DOM ready: `window.onload = function() {...}`
      + same snippet as [page load](#pageLoad)
      + build chapter navigation menu: `buildChapterMenu('en', 'chapters');`
    + create chapter menu: `function buildChapterMenu(lang, kind) {...}`
      + iterate on all tracks: `for (var i=0; i<tracks.length; i++) {...}`
      + declare variables: `var track = tracks[i]; var trackAsHtmlElem = trackElems[i];`
      + check language and kind of the current track: `if ((track.language === lang) && (track.kind === kind)) {...}`
        + almost same as [button click snippet](#buttonClick)
        + display chapter menu: `displayChapterMarkers(track);`
      + other than the same language and kind: `else { displayChapterMarkersAfterTrackLoaded(trackAsHtmlElem, track); }`
    + display chapter menu: `function displayChapterMarkers(track) {...}`
      + declare variable: `var cues = track.cues;`
      + assign invisible value: `track.mode = "hidden";`
      + iterate on cues: `for (var i=0, len = cues.length; i<len; i++) {...}`
        + declare variable for info: `var cue = cues[i];`
        + assign variables related to JSON object: `var cueObject = JSON.parse(cue.text); var description = cueObject.description; var imageFileName = cueObject.image; var imageURL = "https://.../mooc" + imageFileName;`
        + add figure: `var figure = document.createElement('figure'); figure.classList.add('img');`
        + add img element: `figure.innerHTML = "<img onclick='jumpTo(" + cue.startTime + ");' class='thumb' src='" + imageURL + "><figcaption class='desc'>" + description + "</figcaption></figure>";`
        + add figure to chapter menu: `chapterMenuDiv.insertBefore(figure, null);`
    + display chapter markers after track loaded: `function displayChapterMarkersAfterTrackLoaded(trackElem, track) {...}`
      + add listener after track loaded: `trackElem.addEventListener('load', function(e){...});`
      + log msg: `console.log('chapter track loaded');`
      + display chapter menu: `displayChapterMarkers(track);`
    + play video from given start time: `function jumpTo(time) {...}`
      + set start time: `video.currentTime = time;`
      + play video: `play.video();`
  + CSS style
    + chapter menu: `#chapterMenuSection { background-color: lightgrey; border-radius: 10px; padding: 20px; border: 1px solid; display: inline-block; margin: 0px 30px 30px 30px; width: 90% }`
    + image: `figure.img{ margin: 2px; float: left; }`
    + description: `figcaption.desc { text-align: center; font-weight: normal; margin: 2px; }`
    + thumbnail img: `.thumb { height: 75px; border: 1px solid #000; margin: 10px 5px 0 0; box-shadow: 5px 5px 5px grey; transition: all 0.5s; }`
    + thumbnail hover: `.thumb.hover { box-shadow: 5px 5px 5px black; }`


### 1.3.6 Discussion and project

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

__Suggested topics of discussion:__

+ We presented improved video players in the examples, with clickable transcripts, buttons for choosing the subtitles, chapter menus, etc. Which example is your favorite?
+ What other functionalities would you like us to cover in a future course? Small images in the progress bar? Bookmarks? Loop A/B for repeating a given part of a video/audio? Others?


__Optional project:__

+ Make an impressive video player with an attractive menu for choosing between different subtitle files and a nice chapter menu. Be creative! You may use the provided examples as a starting point or build something on your own. Some suggestions: animated menu markers (CSS3 or animated GIFs, or even small video clips), a nice popup menu for choosing the subtitles, a button for hiding/showing a transcript, etc.




