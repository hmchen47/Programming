# Module 1: Advanced HTML5 multimedia section

## 1.5 The Web Audio API

### 1.5.1 Introduction

#### Live coding video: introduction to Web audio

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3ww9mY6)


#### Disadvantages of the Standard APIs

__Shortcomings of the standard APIs that we have discussed so far...__

In Module 2 of the HTML5 Coding Essentials course, you learned how to add an audio or video player to an HTML document, using the `<audio>` and `<video>` elements. 

For example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;audio</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/LaSueur.mp3"</span><span class="pln"> </span><span class="atn">controls</span><span class="tag">&gt;</span></li>
</ol></div><br>

... render like this in your document:

<p class="exampleHTML"><audio id="player" src="https://mainline.i3s.unice.fr/mooc/LaSueur.mp3" loop="loop" controls="controls" crossorigin="anonymous"></audio></p>

Under the hood, this HTML code:

1. initiates a network request to stream the content,
1. deals with decoding/streaming/buffering the incoming data,
1. renders audio controls,
1. updates the progress indicator, time, etc.

You also learned that it's possible to write a custom player: to make your own controls and use the JavaScript API of the `<audio>` and `<video>` elements; to call `play()` and `pause()`; to read/write properties such as `currentTime;` to listen to events (`ended`, `error`, `timeupdate`, etc.); and to manage a playlist, etc.

However, there are many things we still cannot do, including:

+ Play multiple sounds or music in perfect sync,
+ Play non-streamed sounds (this is a requirement for games: sounds must be loaded in memory),
+ Output directly to the speakers; adding special effects, equalizer, stereo balancing, reverb, etc.
+ Any fancy visualizations that dance with the music (e.g. waveforms and frequencies).

The Web Audio API fulfills such missing parts, and much more.

In this course, we do not cover the whole [Web Audio API specification](https://webaudio.github.io/web-audio-api/). Instead, we focus on the parts of the API that can be useful for writing enhanced multimedia players (that work with streamed audio or video), and on parts that are useful for games (i.e. parts that work with small sound samples loaded in memory). There is the API that specializes in music synthesis and scheduling notes, that we will not study oin this course.

Here's a screenshot from one example we will study: an audio player with animated waveform and volume meters that 'dance' with the music:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/34cszld")"
    src    = "https://bit.ly/2St4DY8"
    alt    = "A fancy audio player with multiple visualizations"
    title  = "A fancy audio player with multiple visualizations"
  />
</figure>


#### Web Audio concepts

__The audio context__

The canvas used a graphic context for drawing shapes and handling properties such as colors and line widths.

The Web Audio API takes a similar approach, using an AudioContext for all its operations. 

Using this context, the first thing we do when using this API is to build an "audio routing graph" made of "audio nodes" which are linked together (most of the time in the course, we are going to call it the "audio graph"). Some node types are for "audio sources", another built-in node is for the speakers, and many other types exist, that correspond to audio effects (delay, reverb, filter, stereo panner, etc.), audio analysis (useful for creating fancy visualizations of the real time signal). Others, which are specialized for music synthesis, are not studied in this course.

The AudioContext also exposes various properties, such as `sampleRate`, `currentTime` (in seconds, from the start of `AudioContext` creation), `destination`, and the methods for creating each of the various audio nodes.

The easiest way to understand this principle is to look at a [first example at JSBin](https://jsbin.com/gaduqojeke/edit?html,js).

[Local Demo](src/01e-example01.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/34cszld")"
    src    = "https://bit.ly/3ukFWdI"
    alt    = "A fancy audio player with multiple visualizations"
    title  = "A fancy audio player with multiple visualizations"
  />
</figure>


This example is detailed in the next lesson. For the moment, all you need to know is that it routes the signal from an `<audio>` element using a special node that bridges the "streamed audio" world  to the Web Audio World, called a `MediaElementSourceNode`, then this node is connected to a `GainNode` which enables volume control. This node is then connected to the speakers. We can look at the audio graph of this application using a recent version of FireFox. This browser is the only one (@@as at November 2015) to provide a view of the audio graph, which is very useful for debugging:

__Use the Audio Chrome extension to see the WebAudio graph in devtools__

For a long time, FireFox had a very good WebAudio debugger built in its devtools, but it has been discontinued in 2019. Meanwhile you can use a Google Chrome extension named  "WebAudio Inspector" (or "Audion").  You can install it from the [Chrome Web Store](https://bit.ly/3yEgH9C).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open("https://bit.ly/34cszld")"
    src    = "https://bit.ly/2QOQDYp"
    alt    = "Chrome WebAudio Inspector extension"
    title  = "Chrome WebAudio Inspector extension"
  />
</figure>

Once installed, open a Web page that contains some WebAudio code ([this one for example](https://output.jsbin.com/gaduqojeke)), open the Developer Tools (function key F12, then the gear-wheel), and locate the “Web Audio” (Editor) option. Once enabled, return to Developer Tools and open the Web Audio tab. Then reload the target webpage so that all Web audio activity can be monitored by the tool. You can click on the WebAudio graph nodes to see their properties' values.

Note that JSBin examples should be opened in standalone mode (not in editor mode).

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/34cszld" ismap target="_blank">
    <img style="margin: 0.1em;" height=180
      src   = "https://bit.ly/3bTUpqV"
      alt   = "WebAudio Inspector tab"
      title = "WebAudio Inspector tab"
    >
    <img style="margin: 0.1em;" height=180
      src   = "https://bit.ly/3wr3mzy"
      alt   = "How to go in JsBin standalone mode: click the black arrow on top right of the output tab"
      title = "How to go in JsBin standalone mode: click the black arrow on top right of the output tab"
    >
  </a>
</div>


Audio nodes are linked via their inputs and outputs, forming a chain that starts with one or more sources, goes through one or more nodes, then ends up at a destination (although you don't have to provide a destination if you just want to visualize some audio data, for example).

The `AudioDestination` node above corresponds to the speakers. In this example, the signal goes from left to right: from the `MediaElementSourceNode` (we will see in the code that it's the audio stream from an `<audio>` element), to a Gain node (and by adjusting the gain property we can set the volume of the sound that outputs from this node), then to the speakers.

#### Build Audio Routing Graph

__Typical code to build an audio routing graph (the one used in the above example)__

HTML code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;audio</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/drums.mp3"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; id</span><span class="pun">=</span><span class="atv">"gainExample"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; controls</span><span class="pln"> </span><span class="atn">loop</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/audio&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;br&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;label for="gainSlider"&gt;</span><span class="pln">Gain</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"1"</span><span class="pln"> </span><span class="atn">step</span><span class="pun">=</span><span class="atv">"0.01"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"1"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"gainSlider"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
</ol></div><br>

JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// This line is a trick to initialize the AudioContext</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// that will work on all recent browsers</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">webkitAudioContext</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> audioContext</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> gainExemple</span><span class="pun">,</span><span class="pln"> gainSlider</span><span class="pun">,</span><span class="pln"> gainNode</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// get the AudioContext</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; audioContext </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> ctx</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// the audio element</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; player&nbsp;</span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#gainExample'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;">&nbsp; player.onplay = () =&gt; {</li>
<li class="L2"><span color="#666600" style="color: #666600;">&nbsp; &nbsp; &nbsp;audioContext.resume();</span></li>
<li class="L2"><span color="#666600" style="color: #666600;">&nbsp; }</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; gainSlider </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#gainSlider'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>buildAudioGraph</strong></span><strong><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// input listener on the gain slider</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; gainSlider</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">){</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; gainNode</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; };</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> buildAudioGraph</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// create source and gain node</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> gainMediaElementSource </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(player</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; gainNode </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createGain</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><strong><span class="com">// connect nodes together</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; gainMediaElementSource</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">gainNode</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; gainNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div><br>

__Explanations:__

Here we applied a commonly used technique:

+ As soon as the page is loaded: initialize the audio context (_line 11_). Here we use a trick so that the code works on all browsers: Chrome, FF, Opera, Safari, Edge. The trick at _line 3_ is required for Safari, as it still needs the WebKit prefixed version of the AudioContext constructor.
+ Then we build a graph (_line 20_).
+ The build graph function first builds the nodes, then connects them to build the audio graph. Notice the use of `audioContext.destination` for the speakers (_line 35_). This is a built-in node. Also, the `MediaElementSource` node "gainexample" which is the HTML's audio element.

#### Example of bigger graphs

Web Audio nodes are implemented natively in the browser. The Web Audio framework has been designed to handle a very large number of nodes. It's common to encounter applications with several dozens of nodes: some, such as this [Vocoder application](https://webaudiodemos.appspot.com/Vocoder/index.html#), use hundreds of nodes (the picture below has been taken while the WebAudio debugger was still included in FireFox, you should get similar results with the Chrome WebAudio Inspector extension).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open("https://bit.ly/34cszld")"
    src    = "https://bit.ly/34gs3my"
    alt    = "audio graph of the vocoder app is made of hundreds of nodes"
    title  = "audio graph of the vocoder app is made of hundreds of nodes"
  />
</figure>



#### Notes for 1.5.1 Introduction

+ Limitations of Standard APIs
  + typical actions for `<audio>` and `<video>` elements: `<audio src="https://.../mooc/LaSueur,mp3">`
    + initiate a network request to stream the content
    + deal w/ decoding/streaming/buffering the incoming data
    + render audio controls
    + update the progress indicator, time, etc.
  + customer player
    + making own controls via the JavaScript API of the `<audio>` and `<video>` elements
    + calling `play()` and `pause()`
    + reading/writing properties such as `currentTime`
    + listen events, such as `ended`, `error`, `timeupdate`, etc.
    + managing a playlist, etc.
  + limitations
    + play multiple sounds or music in perfect sync
    + play non-streamed sounds; games: sounds loaded in memory
    + output directly to the speaker; adding special effects, equalizer, stereo balancing, reverb, etc.
    + any fancy visualizations that dance w/ the music, e.g., waveforms and frequencies
  + solution: [Web Audio API](https://webaudio.github.io/web-audio-api/)

+ Web Audio concepts
  + canvas used as a graphic context for drawing shapes and handling properties
  + Web Audio API: taking a similar approach, using an AudioContext for all its operations
  + audio context: `AudioContext`
    + using Web Audio API to build an "audio routing graph"
    + audio routing graph made of "audio nodes"
      + some nodes types for audio sources
      + built-in nodes for speakers
      + audio effects: delay, reverb, filter, stereo panner, etc.
      + audio analysis: used for creating fancy visualizations of real time signal
      + music synthesis (not covered)
  + `BaseAudioContext` [interface](https://webaudio.github.io/web-audio-api/#BaseAudioContext)
    + not instantiated directly
    + extended by the concrete interfaces `AudioContext` and `OfflineAudioContext`
    + properties: `currentTime`, `sampleRate`, `destination`, `state`, `onstateChange`, `listener`, `audioWorklet`
    + methods: `createAnalyser()`, `createBuffer()`, `createBufferSource()`, `createConstantSource()`, `createChannelMerger()`, `createChannelSplitter()`, `createDelay()`, `createPanner()`, etc.
  + `MediaElementSourceNode`: a special node bridging the streamed audio to the WWW
  + `GainNode`: a node enabling volume control
  + `AudioDestination`: a node corresponding to speaker

+ Audio graph in devtools
  + Firefox: WebAudio debugger built-in devtools but discontinued in 2019
  + Chrome: w/ extension named "WenAudio Inspector"

+ Example: Build audio routing graph
  + HTML snippet:
    + audio element: `<audio src="https://.../drums.mp3" id="gainExample" controls loop crossorigin="anonymous"></audio>`
    + gain slider: `<label for="gainSlider">Gain</label><input type="range" min=0 max=1 step"0.01" value=1 id=gainSlider/>`
  + JavaScript snippet
    + create context<a name="audioCtx"></a>: `var ctx = window.AudioContext || window.webkitAudioContext; var audioContext;`
    + access elements: `var gainExample, gainSlider, gainNode;`
    + init page after DOM ready: `window.onload = function() {...}`
      + get Audio Context: `audioContext = new ctx;`
      + get audio element: `player = document.querySelector('#gainExample');`
      + callback for audio play: `player.onplay = () => { audioContext.resume(); }`
      + access gain slider: `gainSlider = document.querySelector('#gainSlider");`
      + call to build audio graph: `buildAudioGraph();`
      + callback for gain slider: `gainSlider.oninput = function(evt) { gainNode.gain.value = evt.target.value; }`
    + build audio graph: `function buildAudioGraph() {...}`
      + create source and gain node: `var gainMediaElementSource = audioContext.createMediaElementSource(player); gainNode = audioContext.createGain();`
      + connect nodes: `gainMediaElementSource.connect(gainNode); gainNode.connect(audioContext.destination);`


#### Knowledge check 1.5.1

1. The WebAudio API has a modular approach: you build an audio graph made of different nodes connected together, each node being a source or corresponding to a sound effect. The signal follows all the routes in this graph, from the sources to the final destination (which is usually the speakers). Can WebAudio handle big graphs made of hundred of nodes?

  a. It depends on the power of the device, but on modern computers or mobile devices it should be able to handle hundreds of nodes. It has been designed with support for large graphs in mind.<br>
  b. No, you shouldn't create audio graphs with more than a few nodes.<br>

  Ans: a<br>
  Explanation: Web Audio has been designed to work with huge graphs.

### 1.5.2 Working with streamed content

#### Live coding video: working with streamed content

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/2RJV8Uw)


#### The MediaSourceElement node

In the previous lesson, we encountered the MediaElementSource node that is used for routing the sound from a `<video>` or `<audio>` element stream. The above video shows how to make a simple example step by step, and how to setup FireFox for debugging Web Audio applications and visualize the audio graph.

Typical use:

[Example at JSBin](https://jsbin.com/mifaqa/edit?html,js,output)

[Local Demo](src/01e-example02.html)

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;audio</span><span class="pln"> </span><strong><span class="atn">id</span><span class="pun">=</span><span class="atv">"player"</span></strong><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="pln"> </span><span class="atn">loop</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Your browser does not support the audio tag.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/audio&gt;</span></li>
</ol></div><br>

JavaScript:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">webkitAudioContext</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> context </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> ctx</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> mediaElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.querySelector</span><span class="pun">(</span><span class="str">'<strong>#player</strong>'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> sourceNode </span><span class="pun">=</span><span class="pln"> context</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">mediaElement</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun"><span class="pun" style="line-height: 25.6px;"><span style="line-height: 25.6px;">sourceNode</span>.<span>connect</span></span><span class="pun" style="line-height: 25.6px;">(context.destination</span><span class="pun" style="line-height: 25.6px;">); // connect to the speakers</span></span></li>
</ol></div><br>

The `MediaElementSource` node  is built using `context.createMediaElementSource(elem)`, where `elem` is an `<audio>` or a `<video>` element.

Then we connect this source Node to other nodes. If we connect it directly to `context.destination`, the sound goes to the speakers with no additional processing.

In the following lessons, we will see the different nodes that are useful with streamed audio and with the `MediaElementSource` node. Adding them in the audio graph will enable us to change the sound in many different ways.


#### Notes for 1.5.2 Working with streamed content

+ Example: the MediaSourceElement` node
  + HTML snippet
    + audio element<a name="audioElem"></a>: `<audio id="player" controls crossorigin="anonymous" loop>...</audio>`
    + source element<a name="guitarElem"></a>: `<source src="https://.../guitarRiff1.mp3">`
    + exception message: `Your browser does not support the audio tag.`
  + JavaScript snippet
    + create [audio context](#audioCtx)
    + access player element: `var mediaElement = document.querySelector('#player');`
    + create source node: `var sourceNode = context.createMediaElementSource(mediaElement);`
    + connect source node to speaker: `sourceNode.connect(context.destination);`
  + using `context.createMediaElementSource(elem)` to build the `MediaElementSource` node
  + `elem`: an `<audio>` or `<video>` element
  + connecting source node to destination node directly w/o additional processing


### 1.5.3 Most useful filter nodes


All definitions come from the [Mozilla Developer Network (MDN) pages](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) giving details about the Web Audio API. 

Let's study the most useful filter nodes: gain, stereo panner, filter, convolver (reverb).

#### Gain node

Useful for setting volume... see the [Gain node's documentation](https://developer.mozilla.org/en-US/docs/Web/API/GainNode).

> Definition: "The `GainNode` interface represents a change in volume. It is an AudioNode audio-processing module that causes a given gain to be applied to the input data before its propagation to the output. A `GainNode` always has exactly one input and one output, both with the same number of channels."

[Example at JSBin](https://jsbin.com/davebu/edit?html,js,console,output), or try it in your browser:

[Local Demo](src/01e-example03.html)

<p class="exampleHTML"><audio id="gainExample" src="https://mainline.i3s.unice.fr/mooc/drums.mp3" loop="loop" controls="controls" crossorigin="anonymous"></audio>&nbsp;<br> <label>Gain</label> <input id="gainSlider" min="0" max="1" step="0.01" value="1" type="range"></p>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">/* Gain Node */</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> gainExample </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#gainExample'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> gainSlider </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#gainSlider'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> gainMediaElementSource </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">gainExample</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> gainNode </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createGain</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">gainMediaElementSource</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">gainNode</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">gainNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">gainSlider</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">){</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gainNode</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>

The `gain` property (_line 13_ in the above code) corresponds to the multiplication we apply to the input signal volume. A value of 1 will keep the volume unchanged. A value < 1 will lower the volume (0 will mute the signal), and a value > 1 will increase the global volume, with a risk of clipping. With gain values > 1, we usually add a compressor node to the signal chain to prevent clipping. You will see an example of this when we discuss the compressor node.


#### Stereo panner

See the [Stereo Panner node's documentation](https://developer.mozilla.org/en-US/docs/Web/API/StereoPannerNode).

> Definition: "The `StereoPannerNode` interface of the Web Audio API represents a simple stereo panner node that can be used to pan an audio stream left or right. The pan property takes a value between -1 (full left pan) and 1 (full right pan)."

[Example at JSBin](https://jsbin.com/jarimu/edit?html,js,output), or try it in your browser:

[Local Demo](src/01e-example04.html)

<p class="exampleHTML"><audio id="pannerPlayer" src="https://mainline.i3s.unice.fr/mooc/drums.mp3" loop="loop" controls="controls" crossorigin="anonymous"></audio> <br> <label for="pannerSlider">Balance</label> <input id="pannerSlider" min="-1" max="1" step="0.1" value="0" type="range"></p>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// the audio element</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> playerPanner </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#pannerPlayer'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> pannerSlider </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#pannerSlider'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// create nodes</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> source </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">playerPanner</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> pannerNode </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createStereoPanner</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// connect nodes together</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> source</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">pannerNode</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> pannerNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// input listener on the gain slider</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> pannerSlider</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">){</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; pannerNode</span><span class="pun">.</span><span class="pln">pan</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span><span class="pln"> </span></li>
</ol></div><br>

#### Biquad filter

> Definition: "The `BiquadFilterNode` interface represents a simple low-order filter, and is created using the `AudioContext.createBiquadFilter()` method. It is an AudioNode that can represent different kinds of filters, tone control devices, and graphic equalizers. A `BiquadFilterNode` always has exactly one input and one output."

See also the [Biquad Filter node's documentation](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode).

[Example at JSBin](https://jsbin.com/tuvaxar/edit?html,js,output), or try it in your browser, with a lowpass filter, only the frequency slider will have a noticeable effect:

[Local Demo](src/01e-example05.html)

<p class="exampleHTML"><audio id="biquadExample" src="https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3" loop="loop" controls="controls" crossorigin="anonymous"></audio> <br> <label>Frequency</label> <input id="biquadFilterFrequencySlider" min="0" max="22050" step="1" value="350" type="range"> <label>Detune</label> <input id="biquadFilterDetuneSlider" min="0" max="100" step="1" value="0" type="range"> <label>Q</label> <input id="biquadFilterQSlider" min="0.0001" max="1000" step="0.01" value="1" type="range"> <label>Type</label><select id="biquadFilterTypeSelector">
<option selected="selected" value="lowpass">lowpass</option>
<option value="highpass">highpass</option>
<option value="bandpass">bandpass</option>
<option value="lowshelf">lowshelf</option>
<option value="highshelf">highshelf</option>
<option value="peaking">peaking</option>
<option value="notch">notch</option>
<option value="allpass">allpass</option>
</select></p>

The most useful slider is the frequency slider (that changes the `frequency` value property of the node). The meaning of the different properties (`frequency`, `detune` and `Q`) differs depending on the `type` of the filter you use (click on the dropdown menu to see the different types available). Look at [this documentation](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode) for details on the different filters and how the `frequency`, `detune` and `Q` properties are used with each of these filter types.

Here is [a nice graphic application](https://webaudioapi.com/samples/frequency-response/) that shows the frequency responses to the various filters, you can choose the type of filters and play with the different property values using sliders:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3wCeY2L")"
    src    = "https://bit.ly/3uh4dSd"
    alt    = "Frequency responses for various filters. Screenshot of a nice application that visualizes that"
    title  = "Frequency responses for various filters. Screenshot of a nice application that visualizes that"
  />
</figure>


Multiple filters are often used together. We will make a multi band equalizer in a next lesson, and use six filters with `type=peaking`. 

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> <g class="gr_ gr_195 gr-alert gr_spell gr_run_anim ContextualSpelling ins-del multiReplace" id="195" data-gr-id="195">ctx</g> </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">webkitAudioContext</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> audioContext </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> <g class="gr_ gr_196 gr-alert gr_spell gr_run_anim ContextualSpelling ins-del multiReplace" id="196" data-gr-id="196">ctx</g></span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">/* BiquadFilterNode */</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> biquadExample </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#biquadExample'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> biquadFilterFrequencySlider </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#biquadFilterFrequencySlider'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> biquadFilterDetuneSlider </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#biquadFilterDetuneSlider'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> biquadFilterQSlider </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#biquadFilterQSlider'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> biquadFilterTypeSelector </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#biquadFilterTypeSelector'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> biquadExampleMediaElementSource </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">biquadExample</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> filterNode </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createBiquadFilter</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">biquadExampleMediaElementSource</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">filterNode</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">filterNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">biquadFilterFrequencySlider</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">){</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;filterNode</span><span class="pun">.</span><span class="pln">frequency</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> parseFloat</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">biquadFilterDetuneSlider</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">){</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;filterNode</span><span class="pun">.</span><span class="pln">detune</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> parseFloat</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">biquadFilterQSlider</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">){</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;filterNode</span><span class="pun">.</span><span class="pln">Q</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> parseFloat</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">biquadFilterTypeSelector</span><span class="pun">.</span><span class="pln">onchange </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">){</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; filterNode</span><span class="pun">.</span><span class="pln">type </span><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span>;</li>
</ol></div><br>

#### Convolver Node

__Convolver node: useful for convolution effects such as reverberation__

> Definition: "The `ConvolverNode` interface is an AudioNode that performs a Linear Convolution on a given AudioBuffer, __often used to achieve a reverb effect__. A ConvolverNode always has exactly one input and one output."

See the [Convolver node's documentation](https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode).

[Example at JSBin](https://jsbin.com/belide/edit?html,js,console,output), THIS EXAMPLE DOES NOT WORK IN YOUR BROWSER as the edX platforms disables Ajax loading in its HTML pages. Try it at JSBin!

[Local Demo](src/01e-example06.html)

<p class="exampleHTML"><audio id="convolverPlayer" src="https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3" loop="loop" controls="controls" crossorigin="anonymous"></audio> <br> <label for="convolverSlider">Reverb (Dry/Wet)</label> <input id="convolverSlider" min="0" max="1" step="0.1" value="0" type="range"></p>

> [From Wikipedia:](https://en.wikipedia.org/wiki/Convolution) a convolution is a mathematical process which can be applied to an audio signal to achieve many interesting high-quality linear effects. Very often, the effect is used to simulate an acoustic space such as a concert hall, cathedral, or outdoor amphitheater. It can also be used for complex filter effects, like a muffled sound coming from inside a closet, sound underwater, sound coming through a telephone, or playing through a vintage speaker cabinet. This technique is very commonly used in major motion picture and music production and is considered to be extremely versatile and of high quality.

E__ach unique effect is defined by an impulse response.__ An impulse response can be represented as an audio file and can be recorded from a real acoustic space such as a cave, or can be synthetically generated through a wide variety of techniques. We can find many high quality impulses on the Web (for example @@TJS OK? [here](https://www.kvraudio.com/forum/viewtopic.php?p=2102159)). The impulse used in the example is the one recorded at the opera: La Scala Opera of Milan, in Italy. It's a .wav file.

Try [this demo](https://webaudioapi.com/samples/room-effects/) to see the difference between different impulse files!

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3wCeY2L")"
    src    = "https://bit.ly/3fj5fsz"
    alt    = "screenshot of a webapp that enable to switch between different impulse files"
    title  = "screenshot of a webapp that enable to switch between different impulse files"
  />
</figure>


So before building the audio graph, we need to download the impulse. For this, we use an Ajax request (this will be detailed during Module 3), but for the moment, just take this function as it is... The Web Audio API requires that impulse files should be decoded in memory before use. Accordingly, once the requested file has downloaded, we call the `decodeAudioData` method. Once the impulse is decoded, we can build the graph. So typical use is as follows:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> impulseURL </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://mainline.i3s.unice.fr/mooc/Scala-Milan-Opera-Hall.wav"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">var decodedImpulse;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> loadImpulse</span><span class="pun">(</span><span class="pln">impulseURL</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// we only get here&nbsp;once the impulse has finished</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// loading and is decoded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;buildAudioGraphConvolver</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">});</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadImpulse</span><span class="pun">(</span><span class="pln">url</span><span class="pun">,</span><span class="pln"> callback</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ajaxRequest </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ajaxRequest</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ajaxRequest</span><span class="pun">.</span><span class="pln">responseType </span><span class="pun">=</span><span class="pln"> </span><span class="str">'arraybuffer'</span><span class="pun">; // for binary transfer</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ajaxRequest</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; // The impulse has been loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> impulseData </span><span class="pun">=</span><span class="pln"> ajaxRequest</span><span class="pun">.</span><span class="pln">response</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; // let's decode it.</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; audioContext</span><span class="pun">.</span><span class="pln">decodeAudioData</span><span class="pun">(</span><span class="pln">impulseData</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// The impulse has been decoded</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;decodedImpulse </span><span class="pun">=</span><span class="pln"> buffer</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// Let's call the callback function, we're done!</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;callback</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">});</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ajaxRequest</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Error with loading&nbsp;audio data"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">err</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ajaxRequest</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Now let's consider the function which builds the graph. In order to set the quantity of reverb we would like to apply, we need two separate routes for the signal:

1. One "dry" route where we directly connect the audio source to the destination,
1. One "wet" route where we connect the audio source to the convolver node (that will add a reverb effect), then to the destination,
1. At the end of both routes, before the destination, we add a gain node, so that we can specify the quantity of dry and wet signal we're going to send to the speakers.

The audio graph will look like this (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3wCeY2L")"
    src    = "https://bit.ly/3yOQNQS"
    alt    = "audio graph of the previous example"
    title  = "audio graph of the previous example"
  />
</figure>


And here is the function which builds the graph:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> buildAudioGraphConvolver</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// create&nbsp;the nodes</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> source </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">playerConvolver</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>convolverNode </strong></span><strong><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createConvolver</span><span class="pun">();</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pun">&nbsp; // Set the buffer property of the convolver node with the decoded impulse</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; convolverNode</span><span class="pun">.</span><span class="pln">buffer </span><span class="pun">=</span><span class="pln"> decodedImpulse</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; convolverGain </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createGain</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; convolverGain</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; directGain </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createGain</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; directGain</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// direct/dry route source -&gt; directGain -&gt; destination</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; source</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">directGain</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; directGain</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// wet route with convolver: source -&gt; convolver </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// -&gt; convolverGain -&gt; destination</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; source</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">convolverNode</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; convolverNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">convolverGain</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; convolverGain</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Note that at line 6 we use the decoded impulse. We could not have done this before the impulse was loaded and decoded.


#### The Dynamics Compressor node

> Definition: "The `DynamicsCompressorNode` interface provides a compression effect, which lowers the volume of the loudest parts of the signal in order to help prevent clipping and distortion that can occur when multiple sounds are played and multiplexed together at once. This is often used in musical production and game audio."

It's usually a good idea to insert a compressor in your audio graph to give a louder, richer and fuller sound, and to prevent clipping. See the [Dynamics Compressor node's documentation](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode).

[Example you can try on JSBin](https://jsbin.com/momixok/edit?html,js,console,output) or try it here in your browser:

[Local Demo](src/01e-example07.html)

<p class="exampleHTML"><audio id="compressorExample" src="https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3" loop="loop" controls="controls" crossorigin="anonymous"></audio> <br> <label for="gainSlider1">Gain</label> <input id="gainSlider1" min="0" max="10" step="0.01" value="8" type="range"> <button id="compressorButton">Turn compressor On</button></p>

In this example we set the gain to a very high value that will make a saturated sound. To prevent clipping, it is sufficient to add a compressor right at the end of the graph! Here we use the compressor with all default settings.

NB: This course does not go into detail about the different properties of the compressor node, as they are largely for musicians with the purpose of enabling the user to set subtle effects such as release, attack, etc.

Audio graph with the compressor activated (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3wCeY2L")"
    src    = "https://bit.ly/3fN9iMG"
    alt    = "Audio graph of the previous example"
    title  = "Audio graph of the previous example"
  />
</figure>


Extract of the HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;audio</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; id</span><span class="pun">=</span><span class="atv">"compressorExample"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">loop</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;&lt;/audio&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"gainSlider1"</span><span class="tag">&gt;</span><span class="pln">Gain</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"10"</span><span class="pln"> </span><span class="atn">step</span><span class="pun">=</span><span class="atv">"0.01"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; <strong>value</strong></span><strong><span class="pun">=</span><span class="atv">"8"</span></strong><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"gainSlider1"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"compressorButton"</span><span class="tag">&gt;</span><span class="pln">Turn compressor On</span><span class="tag">&lt;/button&gt;</span></li>
</ol></div><br>

JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// This line is a trick to initialize the AudioContext</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// that will work on all recent browsers</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">webkitAudioContext</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> audioContext</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> compressorExemple</span><span class="pun">,</span><span class="pln"> gainSlider1</span><span class="pun">,</span><span class="pln"> gainNode1</span><span class="pun">,</span><span class="pln"> compressorNode</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> compressorButton</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> compressorOn </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// get the AudioContext</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; audioContext </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> ctx</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// the audio element</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; compressorExemple </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#compressorExample'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; gainSlider1 </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#gainSlider1'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// button for turning on/off the compressor</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; compressorButton </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#compressorButton'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; buildAudioGraph</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// input listener on the gain slider</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; gainSlider1</span><span class="pun">.</span><span class="pln">oninput </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; gainNode1</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> evt</span><span class="pun">.</span><span class="pln">target</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; compressorButton</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">compressorOn</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// disconnect the compressor and make a </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// direct route from gain to destination</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; compressorNode</span><span class="pun">.</span><span class="pln">disconnect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gainNode1</span><span class="pun">.</span><span class="pln">disconnect</span><span class="pun">(</span><span class="pln">compressorNode</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gainNode1</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; compressorButton</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Turn compressor: On"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><strong><span class="com">// compressor was off, we connect the gain to the compressor </span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// and the compressor to the destination</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gainNode1</span><span class="pun">.</span><span class="pln">disconnect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gainNode1</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">compressorNode</span><span class="pun">);</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; compressorNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; compressorButton</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">=</span><span class="str">"Turn compressor: Off"</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;compressorOn </span><span class="pun">=</span><span class="pln"> </span><span class="pun">!</span><span class="pln">compressorOn</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> buildAudioGraph</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// create source and gain node</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> gainMediaElementSource </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">compressorExemple</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gainNode1 </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createGain</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gainNode1</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> parseFloat</span><span class="pun">(</span><span class="pln">gainSlider1</span><span class="pun">.</span><span class="pln">value</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// do not connect it yet</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;compressorNode </strong></span><strong><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createDynamicsCompressor</span><span class="pun">();</span><span class="pln">&nbsp;</span><span class="com">// connect nodes together</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gainMediaElementSource</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">gainNode1</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gainNode1</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>


__Explanations:__

There is nothing special here compared to the other examples in this section, except that we have used a new method `disconnect` (_line 32_ and _line 38_), which is available on all types of nodes (except `ctx.destination`)  to modify the graph on the fly. When the button is clicked, we remove or add a compressor in the audio graph (_lines 28-42_) and to achieve this, we disconnect and reconnect some of the nodes.


#### Notes for 1.5.3 Most useful filter nodes

+ [Gain node](https://developer.mozilla.org/en-US/docs/Web/API/GainNode)
  + the `GainNode` interface
    + representing a change in volume
    + an AudioNode audio-processing module
    + applied to the input data before its propagation to the output
    + exactly one input and one output w/ the same number of channels
  + `gain` property: corresponding to multiplication applied to the input signal volume
    + value = 1: unchanged volume
    + value < 1: lower the volume
    + value > 1: increasing the global volume, w/ risk of clipping
  + solution to prevent clipping: adding a compressor node

+ Example: gain node
  + access elements: `var gainExample = document.querySelector('#gainExample'); var gainSlider = document.querySelector('#gainSlider');`
  + create gain node: `var gainMediaElementSource = audioContext.createMediaElementSource(gainExample); var gainNode = audioContext.createGain();`
  + create connection btw gain node and destination: `gainMediaElementSource.connect(gainNode); gainNode.connect(audioContext.destination);`
  + add listener for gain node: `gainSlide.oninput = function(evt) { gainNode.gain.value = evt.target.value; };`

+ [Stereo panner](https://developer.mozilla.org/en-US/docs/Web/API/StereoPannerNode)
  + the `StereoPannerNode` interface
  + representing a simple stereo panner node
  + used to pan an audio stream left or right
  + property `pan`: value $\in [-1, 1]$

+ Example: stereo panner
  + access elements: `playerPanner = document.querySelector('#pannerPlayer'); pannerSlide = document.querySelector('#pannerSlide');`
  + create stereo node: `var source = audioContext.createMediaElementSource(playerPanner); pannerNode = audioContext.createStereoPanner();`
  + connect stereo to destination: `source.connect(pannerNode); pannerNode.connect(audioContext.destination);`
  + add listener on pan slider: `pannerSlider.oninput = function(evt) { pannerNode.pan.value = evt.target.value; };`

+ [Biquad filter](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode)
  + the `BiquadFilterNode` interface
    + representing a simple low-order filter
    + creating via `AudioContext.createBiquadFilterNode()`
    + AudioNode able to represent different kinds of filters, control devices, and graphic equalizers
    + exactly one input and one output
  + properties
    + `frequency`
      + frequency in the current filtering algorithm (Hz); most impactful
      + boosting volume inside the range of frequencies
      + unchanged volume outside the range of frequencies
    + `detune`: detuning of the frequency in cents
    + `Q`
      + Quality factor, a dimensionless parameter describing how underdamped an oscillator or resonator is
      + control the width of the frequency band
      + The greater the Q value, the smaller the frequency band.
    + `gain`
      + the gain used in the current filtering algorithm
      + positive value: corresponding to the boost, in dB, to be applied
      + negative value: attentuation
    + `type`: kind of filtering algorithm, including `lowpass`, `highpass`, `bandpass`, `lowself`, `highself`, `peaking`, `notch`, `allpass`
  + use of `frequency`, `detune` and `Q` depnding on type of filtering algorithm
  + demo: [frequency response of various filters](https://webaudioapi.com/samples/frequency-response/)
  + multiple filtersoften used together

+ Example: Biquad filter
  + create Audio context: `var ctx = window.AudioContext || window.webkitAuddioContext; var audioContext = new ctx();`
  + access element for sliders: `var biquadExample = document.querySelector('#biquadExample'); var biquadFilterFrequencySlider = document.querySelector('#biquadFilterFrequencySlider'); var biquadFilterDetuneSlide = document.querySelector(#biquadFilterDetuneSlider'); var biquadFilterQSilder = document.querySelector('#biquadFilterQSlider'); var biquadFilterTypeSelector = document.querySelector('#biquadFilterTypeSelector');`
  + create source node: `var biquadExampleMediaElementSource = audioContext.createMediaElementSource(biquadExample);`
  + create filter node: `var filterNode = audioContext.createBiquadFilter();`
  + connect source, filter and destination: `biquadExampleMediaElementSource.connect(filterNode); filterNode.connect(audioContext.destination);`
  + add event for frequency slider: `biquadFilterFrequencySlider.oninput = function(evt) { fileterNode.frequency.value = parseFloat(evt.target.value); };`
  + add event for detune slider: `biquadFilterDetuneSlider.oninput = function(evt) { filterNode.detune.value = parseFloat(evt.target.value); };`
  + add event for Q slider: `biquadFilterQSlider.oninput = function(evt) { filterNode.Q.value = parseFloat(evt.target.value); };`
  + add event for type selector: `biquadFilterTypeSelector.onchange = function(evt) { flterNode.type = evt.target.value; };`

+ Convolver node
  + the `ConvolverNode` interface
    + useful for convolution effects such as reverberation
    + an AudioNode performing a Linear Convolution on a given AudioBuffer
    + often used to achieve a reverb effect
    + exactly one input and one output
  + properties
    + `buffer`: a mono, stereo, or 4-channel AudioBuffer containing impulse response used by the `ConvolverNode` to create the reverb effect
    + `normalize`: a boolean, controlling whether the impulse response from the buffer, scaled by an equal-power normalization
  + effect defined by an impulse response
  + impulse response
    + possibly represented as an audio file, decoded in memory before use
    + able to be recorded from a real acoustic space such as cave
    + able to synthestically generated through a wide variety of techniques

+ Convolution
  + a mathematical process applied to an audio signal to achieve high-quality linear effect
  + often used to simulate an acoustic space such as a concert hall, cathedral or outdoor amphitheater
  + possibly used for complex filter effcts, example:
    + a muffled sound coming inside from a closet
    + sound underwater
    + sound coming through a telephone
    + playing through a vintage speaker cabinet
  + commonly used in major motion picture and music production

+ Example: convolver node
  + declare variabel for impulse: `var impulseURL = "https://.../mooc/Scala-Milan-Opera-Hall.wav"; var decodedImpulse;`
  + call to load and convolve impulse: `loadImpulse(impulseURL, function() { buildAudioGraphConvolve(); });`
  + load and convolve impulse: `function loadImpulse(url, callback) {...}`
    + set Ajax connection: `ajaxRequest = new XMLHttpRequest(); ajaxRequest.open('GET', url, true); ajaxRequest.responseType = 'arraybuffer';`
    + add listener for AJAX request: `ajaxRequest.onload = function {...}`
      + access impulse data: `var impulseData = ajaxRequest.response;
      + decode impuse data: `audioContext.decodeAudioData(impulseData, function(buffer) { decodedImpulse = buffer; callback(); });`
    + add listener for AJAX error: `ajaxRequest.onerror = function(e) { console.log("Error with loading audio data" + e.err); };`
  + send convolved data: `ajaxRequest.send();`

+ Example: audio graph of convolver node
  + two separate routes for different quantity of reverb
    + `dry` route directly connecting the audio source to the destination
    + `wet` route connecting the audio source to the convolver node
    + add gain nodes on both routes
  + build Audio Graph Convolver: `function buildAudioGraphConvolver() {...}`
    + create nodes: `var source = audioContext.createMediaElementSource(playerConvolver); convolverNode = audioContext.createConvolver();`
    + set buffer property of convolver node: `convolverNode.buffer = decodedImpulse;`
    + create gain node for wet route: `convolverGain = audioContext.createGain(); convolverGain.gain.value = 0;`
    + create gain node for dry route: `directGain = audioContext.createGain(); directGain.gain.value = 1;`
    + connect dry route: `source.connect(directGain); directGain.connect(audioContext.destination);`
    + connect wet route: `source,connect(convolverNode); convolverNode.connect(convolverGain); convolverGain.connect(audioContext.destination);`

+ [Dynamics compressor node](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode)
  + the `DynamicsCompressorNode` interface
    + providing a compression effect
    + lower the volume of the loudest parts of the signal to help preventing clipping and distortion
    + often used in musical production and game audio
  + properties
    + `threshold`: a k-rate AudioParam representing the decibel value above which the compression will start taking effect
    + `knee`: a k-rate AudioParam containing a decibel value representing the range above the threshold where the curve smoothly transition tot the compressed portion
    + `ratio`: a k-rate AudioParam representing the amount of change, in dB, needed in the input for 1 dB change in the output
    + `attack`: a k-rate AudioParam representing the amount of time, in second, required to reduce the gain by 10 dB
    + `release`: a k-rate AudioParam representing the amount of time, in seconds, required to increase the gain by 10 dB
    + `reduction`: the amount of gain reduction currently applied by the compressor to the signal
  + sufficiently adding gain node to compress saturated sound
  + properties of compressor mainly for musians, not going into detail here

+ Example: compressor node
  + HTML snippet
    + [audio element](#audioElem)
    + gain slider: `<label for="gainSlider1">Gain</label><input type="range" min=0 max=10 step="0.01" value=8 id="gainSlider1" />`
    + toggle button for compressor: `<button id="compressorButton">Turn compressor On</button>`
  + JavaScript snippet
    + create sudio context: `var ctx = window.AudioContext || widow.webkitAudioContext; var audioContext;`
    + delcalre variables for compressor: `var compressorExample, gainSlider1, gainNode1, compressorNode; var compressorButton; var compressorOn = false;`
    + init page fater DOM ready: `window.onload = fucntion() {...};`
      + get AudioContext: `audioContext = new ctx();`
      + access elements: `compressorExample = document.querySelector('#compressorExample'); gainSlider1 = document.querySelector('#gainSlider1'); compressorButton = document.querySelector('#compressorButton');`
      + call to build audio graph: `buildAudioGraph();`
      + add event for gain slider: `gainSlider1.oninpu = function(evt) { gainNode1.gain.value = evt.target.value; };`
        + toggle conpressor button: `compressorButton.onclick = function(evt) {...};`
          + On: `if (compressorOn) { compressorNode.disconnect(audioContext.destination); gainNode1.deconnect(compressorNode)}; gainNode1.connect(audioContext.destination); compressorButton.innerHTML = "Turn compresssor: On";`
          + Off: `else { gainNode1.disconnect(audioContext.destination); gainNode1.connect(compressorNode); compressorNode.connect(audioContext.destination); compressorButton.innerHTML = "Turn ciompressor: Off" }`
        + toggle status: `compressorOn = !compressorOn;`
    + build audio graph: `function buildAudioGraph() {...}`
      + crate nodes: `var gainMediaElementSource = audioContext.createMediaElementSource(compressorExample); gainNode1 = audioContexxt.createGain(); gainNode1.gain.value = parseFloat(gainSlider1.value); compressorNode = audioContext.createDynamicCompressor();`
      + connect nodes: `gainMediaElementSource.connect(gainNode1); gainNode1.connect(audioContext.destination);`


### 1.5.4 Writing an equalizer

#### Audio Equalizer

__Example #1: an audio equalizer with an `<audio>` element__

[Example at JSBin](https://jsbin.com/loquwih/edit?html,css,js,output), here is a screenshot:

[Local Demo](src/01e-example08.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3oXBelg")"
    src    = "https://bit.ly/3upIW8N"
    alt    = "an audio player with an equalizer"
    title  = "an audio player with an equalizer"
  />
</figure>


This example uses six `BiquadFilter` nodes with `type="peaking"`.

If you read [the description of this filter type](https://developer.mozilla.org/en-US/docs/Web/API/BiquadFilterNode): _"Frequencies inside the range get a boost or an attenuation; frequencies outside it are unchanged."_ This is exactly what we need to write a multi band equalizer! We're going to use several sliders, each of which boosts one range of frequency values.

The definition says that:

+ the `frequency` property value of a filter will indicate the middle of the frequency range getting a boost or an attenuation, each slider corresponds to a filter whose frequency will be set to 60Hz, 170Hz, 350Hz, 1000Hz, 3500Hz, or 10000Hz.
+ the `gain` property value of a filter corresponds to the boost, in dB, to be applied; if negative, it will be an attenuation. We will code the sliders' event listeners to change the gain value of the corresponding filter.
+ the `Q` property values control the width of the frequency band. The greater the Q value, the smaller the frequency band. We'll ignore it for the purposes of this example.

HTML code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;h2&gt;</span><span class="pln">Equalizer made with the Web Audio API</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"eq"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;audio</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"player"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="pln"> </span><span class="atn">loop</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/drums.mp3"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span style="color: #000000; line-height: 1.6;">&nbsp; &nbsp; &nbsp;Your browser does not support the audio tag.</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;/audio&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;<br></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;label&gt;</span><span class="pln">60Hz</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">step</span><span class="pun">=</span><span class="atv">"1"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"-30"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"30"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">changeGain</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;/input&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"gain0"</span><span class="tag">&gt;</span><span class="pln">0 dB</span><span class="tag">&lt;/output&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;label&gt;</span><span class="pln">170Hz</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; value</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">step</span><span class="pun">=</span><span class="atv">"1"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"-30"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"30"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">changeGain</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;/input&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"gain1"</span><span class="tag">&gt;</span><span class="pln">0 dB</span><span class="tag">&lt;/output&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;label&gt;</span><span class="pln">350Hz</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">step</span><span class="pun">=</span><span class="atv">"1"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"-30"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"30"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">changeGain</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;/input&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"gain2"</span><span class="tag">&gt;</span><span class="pln">0 dB</span><span class="tag">&lt;/output&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/div&gt;</span></li>
</ol></div><br>

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">//Builds an equalizer with multiple <g class="gr_ gr_63 gr-alert gr_spell gr_run_anim ContextualSpelling ins-del multiReplace" id="63" data-gr-id="63">biquad</g> filters</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">webkitAudioContext</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> context </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> ctx</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> mediaElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'player'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> sourceNode </span><span class="pun">=</span><span class="pln"> context</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">mediaElement</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// Creates the equalizer,&nbsp;comprised of&nbsp;a set of biquad filters</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> filters </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Set filters</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">60</span><span class="pun">,</span><span class="pln"> </span><span class="lit">170</span><span class="pun">,</span><span class="pln"> </span><span class="lit">350</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3500</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10000</span><span class="pun">].</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">freq</span><span class="pun">,</span><span class="pln"> i</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> eq </span><span class="pun">=</span><span class="pln"> context</span><span class="pun">.</span><span class="pln">createBiquadFilter</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;eq</span><span class="pun">.</span><span class="pln">frequency</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> freq</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;eq</span><span class="pun">.</span><span class="pln">type </span><span class="pun">=</span><span class="pln"> </span><span class="str">"peaking"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;eq</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;filters</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="pln">eq</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">});</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// Connects filters in&nbsp;sequence</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> sourceNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">filters</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> filters</span><span class="pun">.</span><span class="pln">length </span><span class="pun">-</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;filters</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">filters</span><span class="pun">[</span><span class="pln">i</span><span class="pun">+</span><span class="lit">1</span><span class="pun">]);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// Connects the last filter to the speakers</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">filters</span><span class="pun">[</span><span class="pln">filters</span><span class="pun">.</span><span class="pln">length </span><span class="pun">-</span><span class="pln"> </span><span class="lit">1</span><span class="pun">].</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">context</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">// Event listener called by the sliders</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> changeGain</span><span class="pun">(</span><span class="pln">sliderVal</span><span class="pun">,</span><span class="pln">nbFilter</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> value </span><span class="pun">=</span><span class="pln"> parseFloat</span><span class="pun">(</span><span class="pln">sliderVal</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; filters</span><span class="pun">[</span><span class="pln">nbFilter</span><span class="pun">].</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> value</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Updates output labels</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> output </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#gain"</span><span class="pun">+</span><span class="pln">nbFilter</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; output</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> value </span><span class="pun">+</span><span class="pln"> </span><span class="str">" dB"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>


Here is the final audio graph (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3oXBelg")"
    src    = "https://bit.ly/3oUOgA3"
    alt    = "audio graph of the previous example"
    title  = "audio graph of the previous example"
  />
</figure>


#### Video Equalizer

__Example #2: equalizer with a `<video>` element__

We cloned the previous example and simply changed the `<audio>...</audio>` part of the HTML code by:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"player"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"320"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"240"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/elephants-dream-medium.mp4"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div><br>

And the example works in the same way, but this time with a video. Try moving the sliders to change the sound!

[Example at JSBin](https://jsbin.com/kukupot/edit?html,css,js,output):

[Local Demo](src/01e-example09.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3oXBelg")"
    src    = "https://bit.ly/34CEhpP"
    alt    = "same example as previously but with a video above the equalizer"
    title  = "same example as previously but with a video above the equalizer"
  />
</figure>


#### Notes for 1.5.4 Writing an equalizer

+ Example: audio/video equalizer
  + HTML snippet
    + audio element: `<audio id="player" controls crossorigin="anonymous" loop><source src="https://.../drums.mp3"></audio>`
    + 60Hz gain slider: `<div class="controls"><label>60Hz</label><input type="range" value=0 step=1 min=-30 max=30 oninput="changeGain(this.value, 0);"></input><output id="gain0()">0 dB</output></div>`
    + 170Hz gain slider: `<div class="controls"><label>170Hz</label><input type="range" value=0 step=1 min=-30 max=30 oninput="changeGain(this.value, 0);"></input><output id="gain1()">0 dB</output></div>`
    + ...
  + JavaScript snippet
    + create [audio context](#audioCtx)
    + access palyer element: `var mediaElement = document.getElementById('player');`
    + create source node: `var sourceNode = context.createMediaElementSource(mediaElement);`
    + create filters: `var filters = []; [60, 170, 350, 1000, 3500, 10000].forEach(function(freq, i) {...});`
      + create filter node: `var eq = context.createBiquadFilter();`
      + set various properties: `eq,frequency.value = freq; eq.type = "peaking"; eq.gain.value = 0; filters.push(eq);`
      + append created node to filters: `filters.push(eq);`
    + connect filters in sequence: `sourceNode.connect(filters[0]); for (var i=0; i<filters.length-1; i++) { filters[i].connect(filters[i+1]); }`
    + connect last filter to destination: `filters[filters.length-1].connect(context.destination);`
    + add event listeners for sliders: `function changeGain(sliderVal, nbFilter) {...}`
      + assign gain value to filter: `var value = parseFloat(sliderVal); filters[nbFilter].gain.value = value;`
      + update output label: `var output = document.querySelector('#gain"+nbFilter); output.value = value + " dB";`
  + HTML video element: `<video id="player" width=320 height=240 controls crossOrigin="anonymous"><source src="https://.../elephant-dream-medium.mp4">`


### 1.5.5 Waveforms

#### Live video coding: animating a waveform

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V001400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3usRdJ6)

Do try on and study the code in the [JSBin example](https://jsbin.com/sequtas/edit) created during the Live Coding Video

WebAudio offers an Analyser node that provides real-time frequency and time-domain analysis information. It leaves the audio stream unchanged from the input to the output, but allows us to acquire data about the sound signal being played. This data is easy for us to process since complex computations such as Fast Fourier Transforms are being executed, behind the scenes.


#### Audio Waveform Visualization

__Example #1: audio player with waveform visualization__

[Example at JSBin](https://jsbin.com/sufatup/edit?html,js,output)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3c1Lh3z")"
    src    = "https://bit.ly/3ft2ZPn"
    alt    = "Audio player with waveform visualization"
    title  = "Audio player with waveform visualization"
  />
</figure>


__Do things in order!__

First, select the audio context and the canvas context, then build the audio graph, and finally run the animation loop.

Typical operations to perform once the HTML page is loaded:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// get the audio context</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;audioContext</span><span class="pun">=</span><span class="pln"> ...</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// get the canvas, its graphic context...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;width </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;height </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;canvasContext </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// Build the audio graph with an analyser node at the end</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;buildAudioGraph</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// starts the animation at 60 frames/s</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;requestAnimationFrame</span><span class="pun">(</span><span class="pln">visualize</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div>


__Step #1: build the audio graph with an analyser node at the end__

If we want to visualize the sound that is coming out of the speakers, we have to put an analyser node at almost the end of the sound graph. Example #1 shows a typical use: an `<audio>` element, a `MediaElementElementSource` node connected to an `Analyser` node, and the analyser node connected to the speakers (`audioContext.destination`). The visualization is a graphic animation that uses the `requestAnimationFrame` API presented in teh W3C HTML5 Coding Essentials and Best Practices course (Module 4).

__Typical code for building the audio graph:__

HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;audio</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"player"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">loop</span><span class="pln"> </span><span class="atn">crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/audio&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">300</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">100</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
</ol></div><br>

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> buildAudioGraph</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> mediaElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'player'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> sourceNode </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">mediaElement</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="com">// Create an analyser node</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;analyser </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createAnalyser</span><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="com">//&nbsp;set visualizer options, for lower precision change 1024 to 512,</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="com">&nbsp; &nbsp;// 256, 128, 64 etc. bufferLength will be equal to fftSize/2</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;analyser</span><span class="pun">.</span><span class="pln">fftSize </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1024</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;bufferLength </span><span class="pun">=</span><span class="pln"> analyser</span><span class="pun">.</span><span class="pln">frequencyBinCount</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;dataArray </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Uint8Array</span><span class="pun">(</span><span class="pln">bufferLength</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln"> </span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;sourceNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">analyser</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;analyser</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

With the exception of _lines 8-12_, where we set the analyser options (explained later), we build the following graph (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open("https://bit.ly/3c1Lh3z")"
    src    = "https://bit.ly/3oYy0Oz"
    alt    = "Audio graph with analyser node and properties"
    title  = "Audio graph with analyser node and properties"
  />
</figure>



__Step #2: write the animation loop__

The visualization itself depends on the options which we set for the analyser node. In this case we set the FFT size to 1024 (FFT is a kind of accuracy setting: the bigger the value, the more accurate the analysis will be. 1024 is common for visualizing waveforms, while lower values are preferred for visualizing frequencies). Here is what we set in this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> analyser</span><span class="pun">.</span><span class="pln">fftSize </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1024</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> bufferLength </span><span class="pun">=</span><span class="pln"> analyser</span><span class="pun">.</span><span class="pln">frequencyBinCount</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> dataArray </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Uint8Array</span><span class="pun">(</span><span class="pln">bufferLength</span><span class="pun">);</span></li>
</ol></div><br>

+ _Line 2_: we set the size of the FFT,
+ _Line 3_: this is the byte array that will contain the data we want to visualize. Its length is equal to `fftSize/2`.

When we build the graph, these parameters are set - effectively as constants, to control the analysis during play-back.

Here is the code that is run 60 times per second to draw the waveform:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> visualize</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// 1 - clear the canvas</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// like this: canvasContext.clearRect(0, 0, width, height);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Or use rgba fill to give a slight blur effect</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'rgba(0, 0, 0, 0.5)'</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="com">// 2 - Get the analyser data - for waveforms we need time domain data</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; analyser</span><span class="pun">.</span><span class="pln">getByteTimeDomainData</span><span class="pun">(</span><span class="pln">dataArray</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; // 3 - draws the waveform</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">lineWidth </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> </span><span class="str">'lightBlue'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// the waveform is in one single path, first let's</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// clear any previous path that could be in the buffer</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">beginPath</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> sliceWidth </span><span class="pun">=</span><span class="pln"> width </span><span class="pun">/</span><span class="pln"> bufferLength</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> bufferLength</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // dataArray values are between 0 and 255,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; //&nbsp;normalize v, now between 0 and 1</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> v </span><span class="pun">=</span><span class="pln"> dataArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> 255</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // y will be in [0, canvas height], in pixels</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> v </span><span class="pun">*</span><span class="pln"> height</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">i </span><span class="pun">===</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; canvasContext</span><span class="pun">.</span><span class="pln">moveTo</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; canvasContext</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; x </span><span class="pun">+=</span><span class="pln"> sliceWidth</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">lineTo</span><span class="pun">(</span><span class="pln">canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">/</span><span class="lit">2</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// draw the path at once</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// once again call the visualize function at 60 frames/s</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">visualize</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
</ol></div><br>

__Explanations:__

+ _Lines 9-10_: we ask for the time domain analysis data. The call to `getByteTimeDomainData(dataArray)` will fill the array with values corresponding to the waveform to draw. The returned values are between 0 and 255. See the [specification for details](https://webaudio.github.io/web-audio-api/#widl-AnalyserNode-getByteTimeDomainData-void-Uint8Array-array) about what they represent exactly in terms of audio processing.

Below are other examples that draw waveforms.


#### Video Waveform Visualization

__Example #2: video player with waveform visualization__

Using a `<video>` element is very similar to using an `<audio>` element. We have made no changes to the JavaScript code here; we Just changed "audio" to "video" in the HTML code. 

[Example at JSBin](https://jsbin.com/fuyejuz/edit?html,js,console,output):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3c1Lh3z")"
    src    = "https://bit.ly/3vtyQ8r"
    alt    = "a video player with real time waveform visualization"
    title  = "a video player with real time waveform visualization"
  />
</figure>



#### Graphic Equalizer

__Example #3: both previous examples, this time with the graphic equalizer__

Adding the graphic equalizer to the graph changes nothing, we visualize the sound that goes to the speakers. Try lowering the slider values - you should see the waveform changing.

[Example at JSBin - Audio Player](https://jsbin.com/qijujuz/edit?html,js,output)

[Example at JSBin - Video Player](https://jsbin.com/jafoboh/edit?js,console,output)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3c1Lh3z" ismap target="_blank">
    <img style="margin: 0.1em;" width=200
      src   = "https://bit.ly/3fPgLuS"
      alt   = "audio player + equalizer + visualization"
      title = "audio player + equalizer + visualization"
    >
    <img style="margin: 0.1em;" width=200
      src   = "https://bit.ly/3vvLJP5"
      alt   = "Video player + equalizer + waveform visualization"
      title = "Video player + equalizer + waveform visualization"
    >
  </a>
</div>






### 1.5.6 Frequencies







### 1.5.7 Volume meters






### 1.5.8 Sound samples loaded in memory







### 1.5.9 Load and play sound samples






### 1.5.10 Sound samples and effects






### 1.5.11 Useful third party libraries






### 1.5.12 Discussion and projects







