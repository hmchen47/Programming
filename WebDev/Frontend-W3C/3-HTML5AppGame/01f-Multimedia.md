# Module 1: Advanced HTML5 multimedia section

## 1.6 Exercises - Module 1 (27 Questions)

### 1.6.1 The Text Track API (1-12)

__Source code useful for answering the questions on this page__

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.mp4"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.webm"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-en.vtt"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"de"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-de.vtt"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en.vtt"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span></li>
</ol></div><br>

JavaScript:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> video</span><span class="pun">,</span><span class="pln"> htmlTracks</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Called when the page has been loaded</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Get the tracks as HTML elements</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;htmlTracks </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"track"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> firstTrack </span><span class="pun">=</span><span class="pln"> htmlTracks</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// do something with this track...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// access properties etc.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>

[Local Code Snippet](src/01f-exercise01.html)


1. Which language do you speak?

  How can we know the type and language of the first track?

  a. We cannot know this information, as it is only available from the `TextTrack` object associated with the HTML `track`.<br>
  b. We use `firstTrack.kind` and `firstTrack.srclang`<br>
  c. We use `firstTrack.lang` and `firstTrack.type`<br>

  Ans: b<br>
  Explanation: The correct properties we can use on an HTML `track` element are `kind` and `srclang`.


2. Are you ready?

  Which property is useful for getting the current HTML track state (loaded, loading, error, etc.)?

  a. `firstTrack.readyState`<br>
  b. `firstTrack.ready`<br>
  c. `firstTrack.loaded`<br>

  Ans: b<br>
  Explanation: The readyState property of an HTML track element will give the current HTML track state. The possible values are:
    + 0 = NONE - the text track's cues have not been obtained,
    + 1 = LOADING - the text track is loading with no errors yet. Further cues can still be added to the track by the parser,
    + 2 = LOADED - the text track has been loaded with no errors,
    + 3 = ERROR - the text track was enabled, but when the user agent attempted to obtain it, something failed. Some or all of the cues are likely missing and will not be obtained.


3. Looking inside...

  Can we use a method or a property of an HTML track element (such as `firstTrack` in the source code example) to read the content of a track file?

  a. No, we can only read track content using a `TextTrack` object obtained, for example, with `firstTrack.track` in the source code given at the beginning of this page.<br>
  b. Yes, use `firstTrack.cues` which contains a list of cues for the track. Iterate over this list to access the individual cues.<br>

  Ans: <span style="color: magenta">a</span>, xb<br>
  Explanation: No, cues can be obtained only from TextTrack objects, and the track should have been loaded in memory.


4. Blood on the tracks
1 point possible (graded)
How can we access a TextTrack object? (2 correct answers)

  a. From the HTML element, using the `track` property we can use the TextTrack object associated with a given HTML track,<br>
  b. Using the DOM API: `document.querySelectorAll("tracks")`<br>
  c. From the video HTML element, by calling the method `video.getTextTracks()`<br>
  d. From the video HTML element, using the textTracks property like this: `var textTracks = video.textTracks`<br>

  Ans: ad, xcd, xab<br>
  Explanation: TextTracks may be accessed using either the `track` property of an HTML track, or the video element's `textTrack` property. The DOM API in the example given will return the list of HTML track elements, not TextTrack objects, and the method `getTextTracks()` does not exist.


5. Please load me

  How do we force the browser to load a particular track?

  a. All tracks are loaded by default by every modern browser. If we wait for the entire page to be loaded using a window.onload listener for example, then all the tracks will also be available.<br>
  b. Set the `mode` property of the TextTrack object associated with this track, to "hidden" or "showing"<br>
  c. Call the load method on the HTML track element: `firstTrack.load()`<br>

  Ans: b<br>
  Explanation: It is possible to force a track to be loaded by setting the `mode` property of the TextTrack object to "showing" or "hidden".<br/>Tracks that are not loaded have their `mode` property set to "disabled".


6. Valid properties

  Which of these are valid cue properties? (4 correct answers)

  a. `id`<br>
  b. `text`<br>
  c. `html`<br>
  d. `length`<br>
  e. `startTime`<br>
  f. `endTime`<br>

  Ans: abef<br>
  Explanation: `id`, `text`, `startTime` and `endTime` are correct.


7. Multiple activities at the same time

  Can cues overlap in time? In other words: can we have more than one cue active at a given point in time? (Yes/No)

  Ans: Yes<br>
  Explanation: Yes, cues may overlap. This is why in a cuechange track event listener, we can't acquire only the "current cue": instead the `TextTrack.activeCues` property contains a list of active cues. In the tracks of examples shown during the course we had no overlapping cues, and so we took the first element in the activeCues list as the current cue.


<hr>

__Source code for the next questions (8 and 9)__

HTML (same code as the one at the top of this page):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.mp4"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.webm"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-en.vtt"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"de"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-de.vtt"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en.vtt"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span></li>
</ol></div><br>

JavaScript:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> video</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> firstTrack </span><span class="pun">=</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[<span style="color: #006666;">0</span></span><span class="pun">];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; readContent</span><span class="pun">(</span><span class="pln">firstTrack</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> readContent</span><span class="pun">(</span><span class="pln">track</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"adding cue change listener to loaded track..."</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; track</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">"cuechange"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">activeCues</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">cue </span><span class="pun">!==</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln"> </span><span class="str">"cue change: text = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> cue</span><span class="pun">.</span><span class="pln">text</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">});</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;video</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div><br>

[Local Exercise Code](src/01f-exercise02.html)


8. Fire or not fire!

  What does the above code do?

  a. It works in most browsers, but not FireFox<br>
  b. It reports no errors, but no event is fired<br>
  c. In the console it displays the English subtitles in sync<br>

  Ans: <span style="color: magenta">b</span>, xc<br>
  Explanation: The code is not best practice: verify that the track is loaded before working with it, accessing its content, etc. The first track does not have the default attribute, therefore it is not active nor hidden, it is disabled. It exists, but as it is not showing or hidden (and even not loaded, with some browsers), it will not fire any events while the video is playing. Try [this JSBin](https://jsbin.com/visegax/edit?html,js,console,output) with different browsers.


9. And like this?

  Ok, let's change line 5 to: `var firstTrack = video.textTracks[1]`. Now, what happens?

  a. In modern browsers (excluding FireFox), it displays the German subtitles in sync over the video and in the console<br>
  b. It reports no errors, but no event is fired<br>

  Ans: a<br>
  Explanation: The code is not best practice: verify that the track is loaded before working with it, accessing its content, etc. The first track does not have the default attribute, therefore it is not active nor hidden, it is disabled. It exists, but as it is not showing or hidden (and even not loaded, with some browsers), it will not fire any events while the video is playing. Try [this JSBin](https://jsbin.com/visegax/edit?html,js,console,output) with different browsers.


<hr>

Source code for the next questions (10 and 11)

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">1</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">00.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">26.000</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"description"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Introduction"</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"image"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"introduction.jpg"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">2</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">28.206</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">02.000</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"description"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Watch out!"</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"image"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"watchOut.jpg"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;">...</li>
</ol></div><br>

JavaScript:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Track is the TextTrack corresponding to the webVTT file.&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">//&nbsp;</span>We suppose it's been loaded</li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayChapters</span><span class="pun">(</span><span class="pln">track</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Get the list of cues for this track</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cues </span><span class="pun">=</span><span class="pln"> track</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Iterate on cues</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> len </span><span class="pun">=</span><span class="pln"> cues</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> len</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // current cue</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> cues</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Get the current cue as a JavaScript object</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cueObject </span><span class="pun">=</span><span style="color: #ff0000;"><strong><span class="pln"> AAA</span></strong></span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> description </span><span class="pun">=</span><strong><span class="pln"> BBB</span></strong><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

10. JSON and JavaScript objects

  Replace the AAA placeholder (above) with the correct code (the number of letters is not significant, and do not include the ; statement terminator)

  Ans: `JSON.parse(cue.text)` or `JSON.parse(cue.text);`<br>
  Explanation: The cue is read as a JSON encoded string. In order to turn it into a JavaScript object, you must use `JSON.parse(cue.text)`


11. Give me a description please!

  What would you code (above) instead of the BBB placeholder? (the number of letters is not significant, and do not include the ; statement terminator)

  Ans: `cueObject.description`<br>
  Explanation: Once the cue content has been decoded, it can be used as a normal JavaScript object. To access the description use `cueObject.description`



12. Give me more tracks and cues!

  Which of these are valid methods and constructors in the Timed Text Track API, for creating cues and tracks programmatically? (3 correct answers)

  a. The `Cue` constructor: `var cue = new Cue(startTime, endTime, id);`<br>
  b. The `VTTCue` constructor: `ar cue = new VTTCue(startTime, endTime, id);`<br>
  c. The `Track` constructor: `var textTrack = new Track(kind, label, language);`<br>
  d. The `addTrack` method of a video or audio element: `video.addTrack(kind, label, language);`<br>
  e. The `addTextTrack` method of a video or audio element: `video.addTextTrack(kind, label, language);`<br>
  f. The `addCue` method you can use from a TextTrack: `track.addCue(cue);`<br>

  Ans: bef<br>
  Explanation: Only the `VTTCue` constructor, and the `addTextTrack` method and `addCue` methods, are valid.




