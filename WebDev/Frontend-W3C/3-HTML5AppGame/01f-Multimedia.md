# Module 1: Advanced HTML5 multimedia section

## 1.6 Exercises - Module 1 (27 Questions)

### 1.6.1 The Text Track API (1-12)

__Source code useful for answering the questions on this page__

HTML:

<div><ol>
<li value="1">&lt;video id="myVideo" preload="metadata" controls crossOrigin="anonymous"&gt;</li>
<li> &lt;source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; type="video/mp4"&gt;</li>
<li> &lt;source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.webm" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li> &lt;track label="English subtitles" kind="subtitles" srclang="en"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-en.vtt" &gt;</li>
<li> &lt;track label="Deutsch subtitles" kind="subtitles" srclang="de"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-de.vtt"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;default&gt;</li>
<li> &lt;track label="English chapters" kind="chapters" srclang="en"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;src="https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en.vtt"&gt;</li>
<li> &lt;/video&gt;</li>
</ol></div><br>

JavaScript:

<div><ol>
<li value="1">var video, htmlTracks;</li>
<li>&nbsp;</li>
<li>window.onload = function() {</li>
<li>&nbsp; &nbsp;// Called when the page has been loaded</li>
<li>&nbsp; &nbsp;video = document.querySelector("#myVideo");</li>
<li> </li>
<li>&nbsp; &nbsp;// Get the tracks as HTML elements</li>
<li>&nbsp; &nbsp;htmlTracks = document.querySelectorAll("track");</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;var firstTrack = htmlTracks[0];</li>
<li>&nbsp;</li>
<li>&nbsp; &nbsp;// do something with this track...</li>
<li>&nbsp; &nbsp;// access properties etc.</li>
<li>};</li>
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

  Ans: <span style="color: magenta">a, xb<br>
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

<div><ol>
<li value="1">&lt;video id="myVideo" preload="metadata" controls crossOrigin="anonymous"&gt;</li>
<li> &lt;source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; type="video/mp4"&gt;</li>
<li> &lt;source src="https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.webm" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li> &lt;track label="English subtitles" kind="subtitles" srclang="en"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-en.vtt" &gt;</li>
<li> &lt;track label="Deutsch subtitles" kind="subtitles" srclang="de"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;src="https://mainline.i3s.unice.fr/mooc/elephants-dream-subtitles-de.vtt"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;default&gt;</li>
<li> &lt;track label="English chapters" kind="chapters" srclang="en"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;src="https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en.vtt"&gt;</li>
<li> &lt;/video&gt;</li>
</ol></div><br>

JavaScript:

<div><ol>
<li value="1">var video;</li>
<li>&nbsp;</li>
<li>window.onload = function() {</li>
<li>&nbsp; video = document.querySelector("#myVideo");</li>
<li>&nbsp;&nbsp;var firstTrack = video.textTracks[<span style="color: #006666;">0</span>];</li>
<li>&nbsp; readContent(firstTrack);</li>
<li>};</li>
<li>&nbsp;</li>
<li>function readContent(track) {</li>
<li>&nbsp; console.log("adding cue change listener to loaded track..."); </li>
<li>&nbsp; track.addEventListener("cuechange", function(e) {</li>
<li>&nbsp; &nbsp; &nbsp;var cue = this.activeCues[0];</li>
<li>&nbsp; &nbsp; &nbsp;if(cue !== undefined)</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; console.log( "cue change: text = " + cue.text);</li>
<li>&nbsp; &nbsp; &nbsp;});</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;video.play();</li>
<li>}</li>
<li>&nbsp;</li>
</ol></div><br>

[Local Exercise Code](src/01f-exercise02.html)


8. Fire or not fire!

  What does the above code do?

  a. It works in most browsers, but not FireFox<br>
  b. It reports no errors, but no event is fired<br>
  c. In the console it displays the English subtitles in sync<br>

  Ans: <span style="color: magenta">b, xc<br>
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

JavaScript:

<div><ol>
<li value="1">// Track is the TextTrack corresponding to the webVTT file.&nbsp;</li>
<li>//&nbsp;We suppose it's been loaded</li>
<li>function displayChapters(track) {</li>
<li>&nbsp;&nbsp;// Get the list of cues for this track</li>
<li>&nbsp;&nbsp;var cues = track.cues;</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;// Iterate on cues</li>
<li>&nbsp;&nbsp;for(var i=0, len = cues.length; i &lt; len; i++) {</li>
<li>&nbsp; &nbsp; // current cue</li>
<li>&nbsp; &nbsp;&nbsp;var cue = cues[i];</li>
<li> </li>
<li>&nbsp; &nbsp;&nbsp;// Get the current cue as a JavaScript object</li>
<li>&nbsp; &nbsp;&nbsp;var cueObject =<span style="color: #ff0000;"><strong> AAA</strong></span>;</li>
<li>&nbsp; &nbsp;&nbsp;var description =<strong> BBB</strong>;</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp;&nbsp;}</li>
<li>}</li>
</ol></div><br>

10. JSON and JavaScript objects

  Replace the __AAA__ placeholder (above) with the correct code (the number of letters is not significant, and do not include the ; statement terminator)

  Ans: `JSON.parse(cue.text)` or `JSON.parse(cue.text);`<br>
  Explanation: The cue is read as a JSON encoded string. In order to turn it into a JavaScript object, you must use `JSON.parse(cue.text)`


11. Give me a description please!

  What would you code (above) instead of the __BBB__ placeholder? (the number of letters is not significant, and do not include the ; statement terminator)

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


### 1.6.2 The Web Audio API (13-27)

13. Can you do it?

  What is NOT POSSIBLE using only an `<audio>` or a `<video>` element (without using WebAudio): (3 correct answers.)

  a. Streaming audio or video content<br>
  b. Making fancy visualizations which dance with the music<br>
  c. Making custom play, stop, pause buttons, using JavaScript and methods from the API of these elements<br>
  d. Managing a playlist, using JavaScript and events from the API of these elements<br>
  e. Adding sound effects such as reverberation, filters, etc.<br>
  f. Playing multiple audio or video files in _perfect synchronization_<br>
  
  Ans: bef<br>
  Explanation: With the standard `<audio>` and `<video>` elements, it's not possible to process the signal for adding sound effects or fancy visualizations. It's also not possible to play multiple multimedia files in perfect sync, owing to the streamed nature of these elements.


14. Canvas and Web Audio

  What do the HTML5 canvas API and the WebAudio API have in common?

  a. They use a "context" object for calling methods and accessing properties<br>
  b. They have nothing in common<br>
  
  Ans: a<br>
  Explanation: The canvas uses a graphic context for drawing shapes and handling properties such as colors and line widths.<br>The `WebAudio` API takes a similar approach, using an `AudioContext` for all its operations.


<hr>

__Source code for the next questions (15 and 16)__

HTML:

<div><ol>
<li value="1"> &lt;audio src="https://mainline.i3s.unice.fr/mooc/drums.mp3" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;id="player" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;controls </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;loop </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;crossorigin="anonymous"&gt;</li>
<li>&lt;/audio&gt;</li>
</ol></div><br>

JavaScript:

<div><ol>
<li value="1">var audioContext;</li>
<li>var player;</li>
<li>&nbsp;</li>
<li>window.onload = function() {</li>
<li>&nbsp;&nbsp;// get the AudioContext</li>
<li>&nbsp; audioContext = new AudioContext();</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;// the audio element</li>
<li>&nbsp; player = document.querySelector('#player');</li>
<li>&nbsp;</li>
<li>&nbsp; buildAudioGraph();</li>
<li>};</li>
<li>&nbsp;</li>
<li>function buildAudioGraph() {</li>
<li>&nbsp;&nbsp;// create source node with the audio element stream</li>
<li>&nbsp;&nbsp;var source = audioContext.<strong>AAA</strong>(player);</li>
<li> </li>
<li>&nbsp;&nbsp;// connect source node to the speaker</li>
<li>&nbsp; source.connect(<strong>BBB</strong>);</li>
<li>}</li>
</ol></div><br>

15. Use the source, Luke!

  Replace the __AAA__ placeholder (above) with the correct code
  
  Ans: `createMediaElementSource`<br>
  Explanation: The correct way to create a source node that corresponds to the audio stream of an audio or video element is to use the `audioContext.createMediaElementSource(elem)` method. In the above example the correct answer is: `audioContext.createMediaElementSource(player);`


16. Show me where to go!

  What would you code (above) instead of the __BBB__ placeholder?
  
  Ans: `audioContext.destination`<br>
  Explanation: The speakers node is predefined: if the variable that corresponds to the audio context is named `audioContext`, then the speakers are the `audioContext.destination` object/node.


17. Left or right?

What is the name of the node used to adjust the left/right channel balance?

  a. 2DSpatialNode<br>
  b. StereoPanner<br>
  c. ChannelSplitter<br>
  
  Ans: b<br>
  Explanation: The StereoPanner node is used to implement a left/right controller. See for example: [This example at JSBin](http://jsbin.com/zojona/edit?html,js,output)


18. Too much gain?

The gain node is useful for changing the volume of a signal in the audio routing graph. Can it have values above 1? (Yes/No)
  
  Ans: Yes<br>
  Explanation: Yes, gain nodes can have any value >= 0. If a gain is too high the signal can peak and be distorted.


19. What? A plastic pipe?

  What is a compressor node useful for?

  a. It lowers the volume of the loudest parts of the signal in order to help prevent clipping and distortion<br>
  b. It compresses the signal and produces a muffled sound as if it were coming from the other end of a plastic pipe<br>
  
  Ans: a<br>
  Explanation: The `DynamicsCompressorNode` interface provides a compression effect, which lowers the volume of the loudest parts of the signal in order to help prevent clipping and distortion that might occur when multiple sounds are played and multiplexed together at once. This is often used in musical production and game audio.<br>It's usually a good idea to insert a compressor near the end of your audio graph to give a louder, richer and fuller sound, and prevent clipping.


20. Impulse what?

  The convolver node uses an impulse response as the value of its buffer property. It's often an audio file. What is it and how do we use it?
  
  a. An impulse response can be recorded as an audio file, from a real acoustic space such as a cave or an opera. We find many impulse responses on the Web. It should be loaded in memory and decoded using the decodeAudioData method of the audio context.<br>
  b. It is a set of parameters, the file we load is just a binary file with encoded parameters.<br>
  
  Ans: a<br>
  Explanation:
    + An impulse response can be represented as an audio file and can be recorded from a real acoustic space such as a cave, or can be synthetically generated through a wide variety of techniques. We can find many high quality impulse files on the Web. In the course we used a .wav file that corresponds to the impulse response of La Scala Opera, Milan, Italy.
    + So before building the audio graph, we need to download the impulse. For this, we used an Ajax request. The `WebAudio` API also requires that impulse files should be decoded in memory before use. For this reason, once the requested file has arrived we call the `decodeAudioData` method. Once the impulse is decoded, we can build the graph.


<hr>

__Source code for the next 4 questions (21, 22, 23 and 24)__

HTML:

<div><ol>
<li value="1">&lt;audio src="https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3"</li>
<li> id="player" controls loop crossorigin="anonymous"&gt;</li>
<li>&lt;/audio&gt;</li>
<li>&lt;canvas id="myCanvas" width=300 height=100&gt;&lt;/canvas&gt;</li>
</ol></div><br>

JavaScript:

<div><ol>
<li value="1">function buildAudioGraph() {</li>
<li>&nbsp; &nbsp;var mediaElement = document.getElementById('player');</li>
<li>&nbsp; &nbsp;var sourceNode = audioContext.createMediaElementSource(mediaElement);</li>
<li> </li>
<li><strong>&nbsp; &nbsp;// Create an analyser node</strong></li>
<li><strong>&nbsp; &nbsp;analyser = audioContext.createAnalyser();</strong></li>
<li><strong> </strong></li>
<li><strong>&nbsp; &nbsp;// Set visualizer options, for lower precision change 1024 to 512,</strong></li>
<li><strong>&nbsp; &nbsp;// 256, 128, 64 etc.</strong></li>
<li><strong>&nbsp; &nbsp;analyser.fftSize = 1024;</strong></li>
<li><strong>&nbsp; &nbsp;bufferLength = analyser.frequencyBinCount;</strong></li>
<li><strong>&nbsp; &nbsp;dataArray = new Uint8Array(bufferLength);</strong></li>
<li><strong> </strong></li>
<li>&nbsp; &nbsp;sourceNode.connect(analyser);</li>
<li>&nbsp; &nbsp;analyser.connect(audioContext.destination);</li>
<li>}</li>
</ol></div><br>

And here is an extract of the code that does a real time animated visualization of the signal:

<div><ol>
<li value="1">function visualize() {</li>
<li>&nbsp; &nbsp;// 1 - Clear the canvas</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;// 2 - Get the analyser data</li>
<li>&nbsp; analyser.<strong>AAA</strong>(dataArray);</li>
<li> </li>
<li>&nbsp; // 3 - Draws the visualization...</li>
<li>&nbsp;</li>
<li>&nbsp; // dataArray values are between ? and ?,</li>
<li>&nbsp;</li>
<li>&nbsp; // Once again call the visualize function at 60 frames/s</li>
<li>&nbsp; requestAnimationFrame(visualize);</li>
<li>}</li>
</ol></div><br>

21. Number of data to draw?

  We created an analyser node in the `buildAudioGraph` function. We set the FFT size to 1024, at _line 10_. What will be the size of the buffer containing the __frequency__ analysis data (in other words, what will be the length of the `dataArray` object)?

  a. 512<br>
  b. 1024<br>
  
  Ans: a<br>
  Explanation: The number of data returned is equal to the FFT size/2. In this example, 512.


22. Value range?

  What is the range of the values in the `dataArray` (_line 9_ in the visualize() function)?

  a. It depends on the size of the `fftSize` property of the analyser<br>
  b. All values are between 0 and 255<br>
  c. All values are between -128 and +128<br>
  
  Ans: b<br>
  Explanation: All values are between 0 and 255. Usually you will adjust these values to fit between 0 and the height of the canvas you use to draw the visualization, in pixels.


23. Visualize waveforms

  Instead of the __AAA__ placeholder at _line 5_ of the visualize function, which method would you call to visualize a waveform?
  
  Ans: `getByteTimeDomainData`<br>
  Explanation: For visualizing waveforms, we need time domain data. So we call the `analyser.getByteTimeDomainData(dataArray)` method. The correct answer is `getByteTimeDomainData`.


24. Visualize frequencies

  Instead of the __AAA__ placeholder at _line 5_ of the visualize function, which method would you call to visualize frequencies?
  
  Ans: `getByteFrequencyData`<br>
  Explanation: For visualizing frequencies, we need frequency data. We should call the `analyser.getByteFrequencyData(dataArray)` method. The correct answer is `getByteFrequencyData`.


25. Separate these channels, please!

  What is the difference between the stereoPanner and the channelSplitter nodes?

  a. The stereoPanner is for adjusting the stereo. It has only one input and one output. The channelSplitter node has one input but can have more than one output, for example for separating the left and right channels in the audio graph.<br>
  b. They do the same thing: adjust the stereo balance between the left and right channels.<br>
  
  Ans: a<br>
  Explanation: The `ChannelSplitterNode` interface, often used in conjunction with its opposite, `ChannelMergerNode`, separates the different channels of an audio source into a set of mono outputs. This is useful for accessing each channel separately.


26. Multiple sound samples

  Video games often need to play sound samples in rapid sequence, with different effects, pitch, etc. In the course material, what has been presented as a best practice?

  a. All sound samples should be loaded and decoded before use<br>
  b. All sound samples must be loaded before being used<br>
  
  Ans: a<br>
  Explanation: Indeed, all sound samples must be decoded and loaded into memory before playing with them. Due to the asynchronous nature of both Ajax and the decoding process, this operation can be tricky when you need to download and decode multiple sound samples before starting your application. This is why we have recommended, the BufferLoader utility.


27. Security belt please!

  When we played with sound samples of rifle shots, why did we use a compressor node? (2 correct answers.)

  a. Just in case....<br>
  b. Because a sound might be clipped if the gain value is higher than 1 (if we used a gain node with each sound)<br>
  c. Because when playing multiple sounds, when these sounds are merged into one before being sent to the speakers, the result might be clipped<br>
  
  Ans: bc<br>
  Explanation: Indeed, using a compressor node is always a good way of ensuring that the signal will not clip and produce crackles and a distorted sound.





