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

The Web Audio API takes a similar approach, using an `AudioContext` for all its operations. 

Using this context, the first thing we do when using this API is to build an "audio routing graph" made of "audio nodes" which are linked together (most of the time in the course, we are going to call it the "audio graph"). Some node types are for "audio sources", another built-in node is for the speakers, and many other types exist, that correspond to audio effects (delay, reverb, filter, stereo panner, etc.), audio analysis (useful for creating fancy visualizations of the real time signal). Others, which are specialized for music synthesis, are not studied in this course.

The `AudioContext` also exposes various properties, such as `sampleRate`, `currentTime` (in seconds, from the start of `AudioContext` creation), `destination`, and the methods for creating each of the various audio nodes.

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

+ As soon as the page is loaded: initialize the audio context (_line 11_). Here we use a trick so that the code works on all browsers: Chrome, FF, Opera, Safari, Edge. The trick at _line 3_ is required for Safari, as it still needs the WebKit prefixed version of the `AudioContext` constructor.
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
  + typical actions for `<audio>` and `<video>` elements: `<audio src="https://.../mooc/LaSueur.mp3">`
    + initiate a network request to stream the content
    + deal w/ decoding/streaming/buffering the incoming data
    + render audio controls
    + update the progress indicator, time, etc.
  + customer player
    + making own controls via the JavaScript API of the `<audio>` and `<video>` elements
    + calling `play()` and `pause()`
    + reading/writing properties such as `currentTime`
    + listening events, such as `ended`, `error`, `timeupdate`, etc.
    + managing a playlist, etc.
  + limitations
    + play multiple sounds or music in perfect sync
    + play non-streamed sounds; games: sounds loaded in memory
    + output directly to the speaker; adding special effects, equalizer, stereo balancing, reverb, etc.
    + any fancy visualizations that dance w/ the music, e.g., waveforms and frequencies
  + solution: [Web Audio API](https://webaudio.github.io/web-audio-api/)

+ Web Audio concepts
  + canvas used as a graphic context for drawing shapes and handling properties
  + Web Audio API: taking a similar approach, using an `AudioContext` for all its operations
  + audio context: `AudioContext`
    + using Web Audio API to build an "audio routing graph"
    + audio routing graph made of "audio nodes"
      + some nodes types for audio sources
      + built-in nodes for speakers
      + audio effects: delay, reverb, filter, stereo panner, etc.
      + audio analysis: used for creating fancy visualizations of real time signal
      + music synthesis (not covered)
  + [`BaseAudioContext` interface](https://webaudio.github.io/web-audio-api/#BaseAudioContext)
    + not instantiated directly
    + extended by the concrete interfaces `AudioContext` and `OfflineAudioContext`
    + properties: `currentTime`, `sampleRate`, `destination`, `state`, `onstateChange`, `listener`, `audioWorklet`
    + methods: `createAnalyser()`, `createBuffer()`, `createBufferSource()`, `createConstantSource()`, `createChannelMerger()`, `createChannelSplitter()`, `createDelay()`, `createPanner()`, etc.
  + `MediaElementSourceNode`: a special node bridging the streamed audio to the WWW
  + `GainNode`: a node enabling volume control
  + `AudioDestination`: a node corresponding to speaker

+ Audio graph in devtools
  + Firefox: WebAudio debugger built-in devtools but discontinued in 2019
  + Chrome: w/ extension named "WebAudio Inspector"

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


#### The MediaElementSource node

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

+ Example: the `MediaElementSource` node
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

__Each unique effect is defined by an impulse response.__ An impulse response can be represented as an audio file and can be recorded from a real acoustic space such as a cave, or can be synthetically generated through a wide variety of techniques. We can find many high quality impulses on the Web (for example @@TJS OK? [here](https://www.kvraudio.com/forum/viewtopic.php?p=2102159)). The impulse used in the example is the one recorded at the opera: La Scala Opera of Milan, in Italy. It's a .wav file.

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
  + add listener for gain node: `gainSlider.oninput = function(evt) { gainNode.gain.value = evt.target.value; };`

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
  + multiple filters often used together

+ Example: Biquad filter
  + create Audio context: `var ctx = window.AudioContext || window.webkitAudioContext; var audioContext = new ctx();`
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
      + access impulse data: `var impulseData = ajaxRequest.response;`
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
    + `knee`: a k-rate AudioParam containing a decibel value representing the range above the threshold where the curve smoothly transition to the compressed portion
    + `ratio`: a k-rate AudioParam representing the amount of change, in dB, needed in the input for 1 dB change in the output
    + `attack`: a k-rate AudioParam representing the amount of time, in second, required to reduce the gain by 10 dB
    + `release`: a k-rate AudioParam representing the amount of time, in seconds, required to increase the gain by 10 dB
    + `reduction`: the amount of gain reduction currently applied by the compressor to the signal
  + sufficiently adding gain node to compress saturated sound
  + properties of compressor mainly for musicians, not going into detail here

+ Example: compressor node
  + HTML snippet
    + [audio element](#audioElem)
    + gain slider: `<label for="gainSlider1">Gain</label><input type="range" min=0 max=10 step="0.01" value=8 id="gainSlider1" />`
    + toggle button for compressor: `<button id="compressorButton">Turn compressor On</button>`
  + JavaScript snippet
    + create audio context: `var ctx = window.AudioContext || widow.webkitAudioContext; var audioContext;`
    + delcare variables for compressor: `var compressorExample, gainSlider1, gainNode1, compressorNode; var compressorButton; var compressorOn = false;`sa
    + init page after DOM ready: `window.onload = function() {...};`
      + get AudioContext: `audioContext = new ctx();`
      + access elements: `compressorExample = document.querySelector('#compressorExample'); gainSlider1 = document.querySelector('#gainSlider1'); compressorButton = document.querySelector('#compressorButton');`
      + call to build audio graph: `buildAudioGraph();`
      + add event for gain slider: `gainSlider1.oninput = function(evt) { gainNode1.gain.value = evt.target.value; };`
      + toggle conpressor button: `compressorButton.onclick = function(evt) {...};`
        + On: `if (compressorOn) { compressorNode.disconnect(audioContext.destination); gainNode1.connect(compressorNode); gainNode1.connect(audioContext.destination); compressorButton.innerHTML = "Turn compressor: On"; }`
        + Off: `else { gainNode1.disconnect(audioContext.destination); gainNode1.connect(compressorNode); compressorNode.connect(audioContext.destination); compressorButton.innerHTML = "Turn compressor: Off" }`
      + toggle status: `compressorOn = !compressorOn;`
    + build audio graph: `function buildAudioGraph() {...}`
      + crate nodes: `var gainMediaElementSource = audioContext.createMediaElementSource(compressorExample); gainNode1 = audioContext.createGain(); gainNode1.gain.value = parseFloat(gainSlider1.value); compressorNode = audioContext.createDynamicCompressor();`
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
    + 60Hz gain slider: `<div class="controls"><label>60Hz</label><input type="range" value=0 step=1 min=-30 max=30 oninput="changeGain(this.value, 0);"></input><output id="gain0">0 dB</output></div>`
    + 170Hz gain slider: `<div class="controls"><label>170Hz</label><input type="range" value=0 step=1 min=-30 max=30 oninput="changeGain(this.value, 1);"></input><output id="gain1">0 dB</output></div>`
    + ...
  + JavaScript snippet
    + create [audio context](#audioCtx)
    + access palyer element<a name="playerElem"></a>: `var mediaElement = document.getElementById('player');`
    + create source node<a name="srcNode"></a>: `var sourceNode = context.createMediaElementSource(mediaElement);`
    + create filters<a name="eqiualizer"></a>: `var filters = []; [60, 170, 350, 1000, 3500, 10000].forEach(function(freq, i) {...});`
      + create filter node: `var eq = context.createBiquadFilter();`
      + set various properties: `eq.frequency.value = freq; eq.type = "peaking"; eq.gain.value = 0; filters.push(eq);`
      + append created node to filters: `filters.push(eq);`
    + connect filters in sequence<a name="sequence"></a>: `sourceNode.connect(filters[0]); for (var i=0; i<filters.length-1; i++) { filters[i].connect(filters[i+1]); }`
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

[Local Demo](src/01e-example10.html)

WebAudio offers an Analyser node that provides real-time frequency and time-domain analysis information. It leaves the audio stream unchanged from the input to the output, but allows us to acquire data about the sound signal being played. This data is easy for us to process since complex computations such as Fast Fourier Transforms are being executed, behind the scenes.


#### Audio Waveform Visualization

__Example #1: audio player with waveform visualization__

[Example at JSBin](https://jsbin.com/sufatup/edit?html,js,output)

[Local Ddemo](src/01e-exampl11.html)

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

[Local Demo](src/01e-example12.html)

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

[Example at JSBin - Audio Player](https://jsbin.com/qijujuz/edit?html,js,output) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Local Demo - Audio Player](src/01e-example13.html)

[Example at JSBin - Video Player](https://jsbin.com/jafoboh/edit?js,console,output) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Local Demo - Video Player](src/01e-example14.html)

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


#### Notes for 1.5.5 Waveforms

+ analyzer node
  + providing real-time frequency and time-doimain analysis information
  + leaving audio stream unchchanged
  + allowing to acqure data about the sound signal played
  + processsing the data vai complex computation such as FFT
  + typical operations to perform waveform after DOM ready
    + get audio context: `audioContext = audioContext.createAnalyser();`
    + access canvas<a name="canvas"></a> and get properties: `canvas = document.querySelector("#myCanvas"); width = canvas.width; height = canvas.height; canvasContext = canvas.getContext("2d");`
    + call function to build audio graph: `buildAudioGraph();`
    + start animation: `requestAnimationFrame(visualize);`

+ Build audio/video graph w/ analyzer node
  + HTML snippet
    + audio element: `<audio src="https://.../guitaRifff1.mp3" id="player" controls loop crossorigin="anonymous"></audio>`
    + video element: `<video src="https://.../guitaRifff1.mp3" id="player" controls loop crossorigin="anonymous"></video>`
    + graph convas: `<canvas id="myCanvas" with=300 height=100></canvas>`
  + JavaScript snippet: `function buildAudioGraph() {...}`
    + access player: `var mediaElement = document.getElementById('player');`
    + create [source node](#srcNode)
    + create analyzer node<a name="analyser"></a>: `analyser = audioContext.createAnalyser();`
    + set visualizer options<a name="fftSettings"></a>: `analyser.fftSize = 1024; bufferLength = analyser.frequencyBinCount; datArray = new Unit8Array(bufferLength);`
      + `bufferLength`: the size of the FFT
      + `dataArray`: the byte array containing the data to visualize w/ size = `fftSize/2`
    + build audio graph: `sourceNode.connect(analszer); analyser.connect(audioContext.destination);`

+ Create animation loop: `function visualize() {...}`
  + create the canvas: `canvasContext.fillStyle = 'rgba(0, 0, 0, 0.5)'; canvasContext.fillRect(0, 0, width, height);`
  + get analyzer data - time-domain data: `analyser.getByteTimeDomainData(dataArray);`
  + draw the waveform: `canvasContext.lineWidth = 2; canvasContext.strokeStyle = 'lightBlue';`
  + clean the previous path: `canvasContext.beginPath();`
  + declare variables: `var sliceWidth = width/bufferLength; var x = 0;`
  + iterate on all data in buffer: `for (var i=0; i<bufferLength; i++) {...}}`
    + normalize data and rescale height: `var v = dataArray[i]/255; var y = v * height;`
    + plot 1st point: `if (i === 0) {canvasContext.moveTo(x, y);}`
    + plot the following points: `else {canvasContext.lineTo(x, y);}`
    + move to next data: `x += sliceWidth;`
  + draw horizontal line: `canvasContext.lineTo(canvas.width, canvas.length/2); canvasContext.stroke();`
  + call the visualize function at 60 frames/sec: `requestAnimationFrame(visualize);`



### 1.5.6 Frequencies


#### First typical example

[Example at JSBin](https://jsbin.com/wenuvub/edit?js,output):

[Local Demo](src/01e-example15.html)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/2R2ZKVt" ismap target="_blank">
    <img style="margin: 0.1em;" height=130
      src   = "https://bit.ly/3yNjehZ"
      alt   = "audio player with frequency visualisations with red bars"
      title = "audio player with frequency visualisations with red bars"
    >
    <img style="margin: 0.1em;" height=130
      src   = "https://bit.ly/3yRlqoS"
      alt   = "frequency viualisation this time fftsize = 64"
      title = "frequency viualisation this time fftsize = 64"
    >
  </a>
</div>


This time, instead of a waveform we want to visualize an animated bar chart. Each bar will correspond to a frequency range and 'dance' in concert with the music being played.

+ The frequency range depends upon the sample rate of the signal (the audio source) and on the FFT size. While the sound is being played, the values change and the bar chart is animated.
+ The number of bars is equal to the FFT size / 2 (left screenshot with size = 512, right screenshot with size = 64).
+ In the example above, the `Nth` bar (from left to right) corresponds to the frequency range `N * (samplerate/fftSize)`. If we have a sample rate equal to 44100 Hz and a FFT size equal to 512, then the first bar represents frequencies between 0 and 44100/512 = 86.12Hz. etc. As the amount of data returned by the analyser node is half the fft size, we will only be able to plot the frequency-range to half the sample rate. You will see that this is generally enough as frequencies in the second half of the sample rate are not relevant.
+ The height of each bar shows the strength of that specific frequency bucket. It's just a representation of how much of each frequency is present in the signal (i.e. how "loud" the frequency is).

You do __not__ have to master the signal processing 'plumbing' summarised above - just plot the reported values!

Enough said! Let's study some extracts from the source code. 

This code is very similar to the first example given at the top of this page. We've set the FFT size to a lower value, and rewritten the animation loop to plot frequency bars instead of a waveform:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> buildAudioGraph</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;">&nbsp; ...</li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Create an analyser node</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyser </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createAnalyser</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="com">// Try changing to lower values: 512, 256, 128, 64...</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="com">&nbsp; // Lower values are good for frequency visualizations, </span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="com">&nbsp; // try 128, 64 etc.?&nbsp;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; analyser</span><span class="pun">.</span><span class="pln">fftSize </span><span class="pun">=</span><span class="pln"> </span><span class="lit">256</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;...</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

This time, when building the audio graph, we have used a smaller FFT size. Values between 64 and 512 are very common here. Try them in the JSBin example! Apart from the lines in bold, this function is exactly the same as in the first example.

The new visualization code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> visualize</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// clear the canvas</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> width</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="com">// Get the analyser data</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; analyser</span><span class="pun">.</span><span class="pln">getByteFrequencyData</span><span class="pun">(</span><span class="pln">dataArray</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> barWidth </span><span class="pun">=</span><span class="pln"> width </span><span class="pun">/</span><span class="pln"> bufferLength</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> barHeight</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// values go from 0 to 255 and the canvas heigt is 100. Let's rescale</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// before drawing. This is the scale factor</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; heightScale </span><span class="pun">=</span><span class="pln"> height</span><span class="pun">/</span><span class="lit">128</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> bufferLength</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // between 0 and 255</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; barHeight </span><span class="pun">=</span><span class="pln"> dataArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // The color is red but lighter or darker depending on the value</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pln" style="line-height: 1.6;">canvasContext</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">fillStyle </span><span class="pun" style="line-height: 1.6;">=</span><span class="pln" style="line-height: 1.6;"> </span><span class="str" style="line-height: 1.6;">'rgb('</span><span class="pln" style="line-height: 1.6;"> </span><span class="pun" style="line-height: 1.6;">+</span><span class="pln" style="line-height: 1.6;"> </span><span class="pun" style="line-height: 1.6;">(</span><span class="pln" style="line-height: 1.6;">barHeight</span><span class="pun" style="line-height: 1.6;">+</span><span class="lit" style="line-height: 1.6;">100</span><span class="pun" style="line-height: 1.6;">)</span><span class="pln" style="line-height: 1.6;"> </span><span class="pun" style="line-height: 1.6;">+</span><span class="pln" style="line-height: 1.6;"> </span><span class="str" style="line-height: 1.6;">',50,50)'</span><span class="pun" style="line-height: 1.6;">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun" style="line-height: 1.6;">&nbsp; &nbsp; // scale from [0, 255] to the canvas height [0, height] pixels</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; barHeight </span><span class="pun">*=</span><span class="pln"> heightScale</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // draw the bar</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">-</span><span class="pln">barHeight</span><span class="pun">/</span><span class="lit">2</span><span class="pun">,</span><span class="pln"> barWidth</span><span class="pun">,</span><span class="pln"> barHeight</span><span class="pun">/</span><span class="lit">2</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// 1 is the number of pixels between bars -&nbsp;you can change it</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; x </span><span class="pun">+=</span><span class="pln"> barWidth </span><span class="pun">+</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// once again call the visualize function at 60 frames/s</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">visualize</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

__Explanations:__

+ _Line 6_: this is different to code which draws a waveform! We ask for byteFrequencyData (vs byteTimeDomainData earlier) and it returns an array of fftSize/2 values between 0 and 255.
+ _Lines 16-29_: we iterate on the value. The x position of each bar is incremented at each iteration (_line 28_) adding a small interval of 1 pixel between bars (you can try different values here). The width of each bar is computed at line 8.
+ _Line 14_: we compute a scale factor to be able to display the values (ranging from 0 to 255) in direct proportion to the height of the canvas. This scale factor is used in _line 23_, when we compute the height of the bars we are going to draw.


#### Fancy Frequency Visualization

__Other examples: achieving more impressive frequency visualization__

[Example at JSBin](https://jsbin.com/muzifi/edit?html,css,js,output) with a different look for the visualization: please read the source code and try to understand how the drawing of the frequency is done.

[Local Demo](src/01e-example16.html)


[Last example at JSBin](https://jsbin.com/fekorej/edit?html,js,output) with this time the graphic equalizer, a master volume (gain) and a stereo panner node just before the visualizer node:

[Local Demo](src/01e-example17.html)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/2R2ZKVt" ismap target="_blank">
    <img style="margin: 0.1em;" width=250
      src   = "https://bit.ly/3p0CHaq"
      alt   = "Same example as before but with symmetric and colored frequency visualisations"
      title = "Same example as before but with symmetric and colored frequency visualisations"
    >
    <img style="margin: 0.1em;" width=250
      src   = "https://bit.ly/3vAQvLd"
      alt   = "Previous example with a master volume (gain node) and the equalizer + a stereoPanner node"
      title = "Previous example with a master volume (gain node) and the equalizer + a stereoPanner node"
    >
  </a>
</div>

And here is the audio graph for this example (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 45vw;"
    onclick= "window.open("https://bit.ly/2R2ZKVt")"
    src    = "https://bit.ly/3wVRqGD"
    alt    = "audio graph from above example"
    title  = "audio graph from above example"
  />
</figure>

Source code from this example's the buildAudioGraph function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> buildAudioGraph</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> mediaElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'player'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> sourceNode </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">mediaElement</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Create an analyser node</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyser </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createAnalyser</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// Try changing for lower values: 512, 256, 128, 64...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyser</span><span class="pun">.</span><span class="pln">fftSize </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1024</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferLength </span><span class="pun">=</span><span class="pln"> analyser</span><span class="pun">.</span><span class="pln">frequencyBinCount</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; dataArray </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Uint8Array</span><span class="pun">(</span><span class="pln">bufferLength</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Create the equalizer, which comprises a set of biquad filters</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Set filters</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">[</span><span class="lit">60</span><span class="pun">,</span><span class="pln"> </span><span class="lit">170</span><span class="pun">,</span><span class="pln"> </span><span class="lit">350</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1000</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3500</span><span class="pun">,</span><span class="pln"> </span><span class="lit">10000</span><span class="pun">].</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">freq</span><span class="pun">,</span><span class="pln"> i</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> eq </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createBiquadFilter</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;eq</span><span class="pun">.</span><span class="pln">frequency</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> freq</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;eq</span><span class="pun">.</span><span class="pln">type </span><span class="pun">=</span><span class="pln"> </span><span class="str">"peaking"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;eq</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;filters</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="pln">eq</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">});</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Connect filters in&nbsp;sequence</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;sourceNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">filters</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> filters</span><span class="pun">.</span><span class="pln">length </span><span class="pun">-</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;filters</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">filters</span><span class="pun">[</span><span class="pln">i</span><span class="pun">+</span><span class="lit">1</span><span class="pun">]);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Master volume is a gain node</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;masterGain </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createGain</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;masterGain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Connect the last filter to the speakers</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;filters</span><span class="pun">[</span><span class="pln">filters</span><span class="pun">.</span><span class="pln">length </span><span class="pun">-</span><span class="pln"> </span><span class="lit">1</span><span class="pun">].</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">masterGain</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;</strong></span><strong><span class="com">// for stereo balancing, split the signal</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;stereoPanner </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createStereoPanner</span><span class="pun">();</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;</span><span class="com">// connect master volume output to the stereo panner</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;masterGain</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">stereoPanner</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Connect the stereo panner to analyser and analyser to destination</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;stereoPanner</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">analyser</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;analyser</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Notes for 1.5.6 Frequencies

+ Basic frequencies visualization
  + bar chart corresponding to a frequency range
  + frequencies range dependning on sample rate of the signal (the audio source) and on the FFT size
  + number of bars = the FFT size / 2
  + the nth bar corresponding to the frequency range $N \times (\text{samplerate}/text{fftSize})$. example
    + sameple rate: 44100 Hz
    + FFT size: 512
    + 1st bar: $[0, 44100/512) = [0, 86,12)$Hz
    + number of data returned by the analyzer node: fftSize / 2
    + only half of the sample rate
  + height: the stength of the specific freqnecy bucket

+ Example: frequency visualization `function visualize() {...}`
  + clear the canvas: `canvasContext.clearRect(0, 0, width, height);`
  + get analyser data on frequency domain: `analyser.getByteFrequencyData(dataArray);`
  + declare variables: `var barWidth = width / bufferLength; var barHeight; var x = 0; heightScale = height/128;`
  + iterate on buffer: `for (var i=0; i<bufferLength; i++) {...}`
    + set bar height: `barHeight = dataArray[i];`
    + set bar color w/ red from lighter to darker: `canvasContext.fillStyle = 'rgb(' + (barHeight + 100) + ',50, 50);`
    + rescale to canvas height: `barHeight += heightScale;`
    + draw the bar: `canvasContext.fillRect(x, height-barHeight/2, barWidth, barHeight/2);`
    + create the gap btw bars: `x += barWidth + 1;`
  + call animation loop: `requestAnimationFrame(visualize);`

+ Example: audio graph of fancy frequency visualization - `function buildAudioGraph() {...}`
  + access elements: `var mediaElement = document.getElementById('player'); var sourceNode = audioContext.createMediaElementSource(mediaElement);`
  + create analyser node: `analyser = audioContext.createAnalyser();`
  + set [visualization option](#fftSettings)
  + create [filters](#equalizer)
  + connect [filters in sequence](#sequence)
  + set master volume in gain node: `masterGain = audioContext.createGain(); masterGain.value = 1;`
  + connecct laster filter to gain node: `filters[filters.length - 1].connect(masterGain);`
  + create stereo balancing and connect to gain and stereo nodes: `stereoPanner = audioContext.createStereoPanner(); masterGain.connect(stereoPanner);`
  + connect stereo panner to analyser to destination<a name="stereoAnalyserDest"></a>: `stereoPlanner.connect(analyser); analyser.connect(audioContext.destination);`


### 1.5.7 Volume meters

<p style="margin: 10px; border: 1px solid black; padding: 5px;"><span style="color: #ff0000;"><strong>Important note:</strong></span> the volume meter implementations below use rough approximations and cannot be taken as the most accurate way to compute an exact volume. See at the end of the page for some extra explanations, as well as links to better (and more complex) implementations.&nbsp;</p>


#### Volume Meter of Audio Player

__Example #1: add a single volume meter to the audio player__

[Try it at JSBin](https://jsbin.com/kuciset/edit?html,css,js,output):

[Local Demo](src/01e-example18.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3uBXZfy")"
    src    = "https://bit.ly/3vDdsxw"
    alt    = "Single volume meter that dances with the music"
    title  = "Single volume meter that dances with the music"
  />
</figure>


In order to have a "volume meter" which traces upward/downward with the intensity of the music, we will compute the average intensity of our frequency ranges, and draw this value using a nice gradient-filled rectangle.

Here are the two functions we will call from the animation loop:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawVolumeMeter</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>analyser</strong></span><strong><span class="pun">.</span><span class="pln">getByteFrequencyData</span><span class="pun">(</span><span class="pln">dataArray</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> average </span><span class="pun">=</span><span class="pln"> getAverageVolume</span><span class="pun">(</span><span class="pln">dataArray</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// set the fill style to a nice gradient</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">gradient</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// draw the vertical meter</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln">height</span><span class="pun">-</span><span class="pln">average</span><span class="pun">,</span><span class="lit">25</span><span class="pun">,</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">restore</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getAverageVolume</span><span class="pun">(</span><span class="pln">array</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> values </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> average</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> length </span><span class="pun">=</span><span class="pln"> array</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// get all the frequency amplitudes</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; values </span><span class="pun">+=</span><span class="pln"> array</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; average </span><span class="pun">=</span><span class="pln"> values </span><span class="pun">/</span><span class="pln"> length</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> average</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div><br>

Note that we are measuring intensity (_line 4_) and once the frequency analysis data is copied into the dataarray, we call the `getAverageVolume` function (_line 5_) to compute the average value which we will draw as the volume meter.

This is how we create the gradient:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="com">// create a vertical gradient of the height of the canvas</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> gradient </span><span class="pun">=</span><span class="pln"> canvasContext</span><span class="pun">.</span><span class="pln">createLinearGradient</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> height</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> gradient</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="str">'#000000'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> gradient</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.75</span><span class="pun">,</span><span class="str">'#ff0000'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> gradient</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0.25</span><span class="pun">,</span><span class="str">'#ffff00'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> gradient</span><span class="pun">.</span><span class="pln">addColorStop</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="str">'#ffffff'</span><span class="pun">);</span></li>
</ol></div><br>

And here is what the new animation loop looks like (for the sake of clarity, we have moved the code that draws the signal waveform to a separate function):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> visualize</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; clearCanvas</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; drawVolumeMeter</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; drawWaveform</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// call again the visualize function at 60 frames/s</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; requestAnimationFrame</span><span class="pun">(</span><span class="pln">visualize</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;">}</li>
</ol></div><br>

Notice that we used the best practices seen in week 3 of the HTML5 part 1 course: we saved and restored the context in all functions that change something in the canvas context (see function `drawVolumeMeter` and `drawWaveForm` in the source code).


#### Volume Meters for Stereo Channels

__Example #2: draw two volume meters, one for each stereo channel__

This time, let's split the audio signal and create a separate analyser for each output channel. We retain the analyser node that is being used to draw the waveform, as this works on the stereo signal (and is connected to the destination in order to hear full audio).

We added a `stereoPanner` node right after the source and a left/right balance slider to control its `pan` property. Use this slider to see how the left and right volume meter react.

In order to isolate the left and the right channel (for creating individual volume meters), we used a new node called a Channel Splitter node. From this node, we created two routes, each going to a separate analyser (_lines 46 and 47_ of the example below)

+ See the [ChannelSplitterNode's documentation](https://developer.mozilla.org/en-US/docs/Web/API/ChannelSplitterNode). Notice that there is also a [ChannelMergerNode](https://developer.mozilla.org/en-US/docs/Web/API/ChannelMergerNode) for merging multiple routes into a single stereo signal.

Use the connect method with extra parameters to connect the different outputs of the channel splitter node:

+ `connect(node, 0, 0)` to connect the left output channel to another node,
+ `connect(node, 1, 0)` to connect the right output channel to another node,

[Example at JSBin](https://jsbin.com/qezevew/edit?html,css,js,output):

[Loacal Demo](src/01e-example19.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3uBXZfy")"
    src    = "https://bit.ly/2St4DY8"
    alt    = "Example with stereo volume meters"
    title  = "Example with stereo volume meters"
  />
</figure>

This is the audio graph we've built (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open("https://bit.ly/3uBXZfy")"
    src    = "https://bit.ly/3i4pvjn"
    alt    = "Audiograph from previous example"
    title  = "Audiograph from previous example"
  />
</figure>


As you can see there are two routes: the one on top sends the output signal to the speakers and uses an analyser node to animate the waveform, meanwhile the one at the bottom splits the signal and send its left and right parts to separate analyser nodes which draw the two volume meters. Just before the split, we added a stereoPanner to enable adjustment of the left/right balance with a slider.

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> buildAudioGraph</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> mediaElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'player'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> sourceNode </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createMediaElementSource</span><span class="pun">(</span><span class="pln">mediaElement</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong>&nbsp;</strong></span><strong>// connect the source node to a stereo panner</strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; stereoPanner </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createStereoPanner</span><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; sourceNode</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">stereoPanner</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"></li>
<li class="L6" style="margin-bottom: 0px;">&nbsp; // Create an analyser node for the waveform</li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyser </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createAnalyser</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">//&nbsp;Use FFT value adapted to waveform drawing</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyser</span><span class="pun">.</span><span class="pln">fftSize </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1024</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferLength </span><span class="pun">=</span><span class="pln"> analyser</span><span class="pun">.</span><span class="pln">frequencyBinCount</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; dataArray </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Uint8Array</span><span class="pun">(</span><span class="pln">bufferLength</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Connect the stereo panner to the analyser</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; stereoPanner</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">analyser</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// and the analyser to the destination</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyser</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">audioContext</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;&nbsp;</span><span class="com">// End of route 1. &nbsp;W</span>e start another route from the</strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong>&nbsp; // stereoPanner node, with two analysers for the meters</strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// Two analysers for the stereo volume meters</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; // Here we use a small FFT value as we're gonna work with</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; // frequency analysis data</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyserLeft </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createAnalyser</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyserLeft</span><span class="pun">.</span><span class="pln">fftSize </span><span class="pun">=</span><span class="pln"> </span><span class="lit">256</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferLengthLeft </span><span class="pun">=</span><span class="pln"> analyserLeft</span><span class="pun">.</span><span class="pln">frequencyBinCount</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; dataArrayLeft </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Uint8Array</span><span class="pun">(</span><span class="pln">bufferLengthLeft</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyserRight </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createAnalyser</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyserRight</span><span class="pun">.</span><span class="pln">fftSize </span><span class="pun">=</span><span class="pln"> </span><span class="lit">256</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferLengthRight </span><span class="pun">=</span><span class="pln"> analyserRight</span><span class="pun">.</span><span class="pln">frequencyBinCount</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; dataArrayRight </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Uint8Array</span><span class="pun">(</span><span class="pln">bufferLengthRight</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;<strong> // Split the signal</strong></span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; splitter </span><span class="pun">=</span><span class="pln"> audioContext</span><span class="pun">.</span><span class="pln">createChannelSplitter</span><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Connect the stereo panner&nbsp;to the splitter node</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; stereoPanner</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">splitter</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Connect each&nbsp;of the outputs from the splitter to</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// the analysers</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; splitter</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">analyserLeft</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; splitter</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">analyserRight</span><span class="pun">,</span><span class="lit">1</span><span class="pun">,</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// No need to connect these analysers to something, the sound</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// is already connected through the route that goes through</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// the analyser used for the waveform</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

And here is the new function for drawing the two volume meters:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> drawVolumeMeters</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">save</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// set the fill style to a nice gradient</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillStyle</span><span class="pun">=</span><span class="pln">gradient</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// left channel</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyserLeft</span><span class="pun">.</span><span class="pln">getByteFrequencyData</span><span class="pun">(</span><span class="pln">dataArrayLeft</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> averageLeft </span><span class="pun">=</span><span class="pln"> getAverageVolume</span><span class="pun">(</span><span class="pln">dataArrayLeft</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// draw the vertical meter for left channel</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln">height</span><span class="pun">-</span><span class="pln">averageLeft</span><span class="pun">,</span><span class="lit">25</span><span class="pun">,</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// right channel</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; analyserRight</span><span class="pun">.</span><span class="pln">getByteFrequencyData</span><span class="pun">(</span><span class="pln">dataArrayRight</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> averageRight </span><span class="pun">=</span><span class="pln"> getAverageVolume</span><span class="pun">(</span><span class="pln">dataArrayRight</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// draw the vertical meter for left channel</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; canvasContext</span><span class="pun">.</span><span class="pln">fillRect</span><span class="pun">(</span><span class="lit">26</span><span class="pun">,</span><span class="pln">height</span><span class="pun">-</span><span class="pln">averageRight</span><span class="pun">,</span><span class="lit">25</span><span class="pun">,</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pln" style="line-height: 1.6;">canvasContext</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">restore</span><span class="pun" style="line-height: 1.6;">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

The code is very similar to the previous one. We draw two rectangles side-by-side, corresponding to the two analyser nodes - instead of the single display in the previous example.

#### Extra explanations and resources

Indeed, the proposed examples are ok for making things "dancing in music" but rather inaccurate if you are looking for a real volume meter. Results may also change if you modify the size of the fft in the analyser node properties. There are accurate implementations of volume meters in WebAudio (see this [volume meter example](https://github.com/cwilso/volume-meter)) but they use nodes that were out of the scope for this course. Also, a student from this course named "SoundSpinning" proposed also another approximation that gives more stable results. Read below:

*** _SoundSpinning:_ "The only half close way I found for the meter levels is to use `getFloatTimeDomainData` data from the analyser, which seems to give a normalized array between -1 and 1. Then just plot the actual wave level values as we loop in the canvas rendering. This is still not great, since the canvas works at 60Hz while (most of the times) audio sampling is 44.1kHz, but it is closer. This also keeps the same levels no matter what `FFTsize` you apply."

Here is a [codepen with my proposed meters](https://codepen.io/Sound_Spinning/pen/RwPKgOK). ***

[Local Demo](src/01e-example20.html)


#### Notes for 1.5.7 Volume meters

+ Example: volume meter of audio player
  + tasks:
    + volume meter: tracing upward/downward w/ the intensity of the music
    + compute the average intensity of frequency ranges
    + draw the average intensity w/ gradient-filled rectangle
  + draw volume meter: `function drawVolumeMeter() {...}`
    + save canvas ctx: `canvasContext.save();`
    + get analyser data and their average: `analyser.getByteFrequencyData(dataArray); var average = getAverageVolume(dataAnalysis);`
    + set fill style: `canvasContext.fillStyle = gradient;`
    + draw the vertical meter: `canvasContext.fillRect(0, height-average, 25, height);`
    + restore ctx: `canvasContext.restore();`
  + get average volume: `function getAverageVolume(array) {...}`
    + declare variable: `var values = 0; var average; var length = array.length;`
    + get all the frequency amplitude: `for (avr i=0; i<length; i++) {values += array[i]; }`
    + get average value: `average = values/length; return average;`
  + create gradient: `gradient = canvasContext.createLinearGradient(0, 0, 0, height); gradient.addColorStop(1, '#000000'); gradient.addColorStop(0.75, '#ff0000'); gradient.addColorStop(0.25, '#ffff00'); gradient.addColorStop(0, '#ffffff');`
  + draw visualization: `function visualize() {...}`
    + empty canvas: `clearCanvas();`
    + draw waveform and volume meter: `drawVolumeMeter(); drawWaveform();`
    + call animation loop: `requestAnimationFrame(visualize);`

+ Example: volume meters of stereo channels
  + stereo channels
    + split the audio signal and create a separate analyser for each output channel
    + add `stereoPanner` node right after the source node
    + add a left/right balance slider to control the `pan` property
    + add [Channel Splitter node](https://developer.mozilla.org/en-US/docs/Web/API/ChannelSplitterNode) to isolate right and left channels
  + audio graph

    <figure style="margin: 0.5em; text-align: center;">
      <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
        onclick= "window.open("https://bit.ly/3uBXZfy")"
        src    = "https://bit.ly/3i4pvjn"
        alt    = "Audiograph from previous example"
        title  = "Audiograph from previous example"
      />
    </figure>
  
  + build audio graph: `function buildAudioGraph() {...}`
    + access [player element](#playerElem)
    + create [source node](#srcNode)
    + connect source node to stereo node: `stereoPanner = audioContext.createStereoPanner(); sourceNode.connect(stereoPanner);`
    + create [analyzer node](#analyser)
    + set [visualizer options](#fftSettings)
    + connect [stereo panner to analyser to destination](#stereoAnalyserDest)
    + set left channel: `analyserLeft.fftSize = 256; bufferLengthLeft = analyserLeft.frequencyBinCount; dataArrayLeft = new Unit8Array(bufferLengthLeft);`
    + set right channel: `analyserRight.fftSize = 256; bufferLengthRight = analyserRight.frequencyBinCount; dataArrayRight = new Unit8Array(bufferLengthRight);`
    + create and connect splitter node: `splitter = audioContext.createChannelSplitter(); stereoPanner.connect(splitter);`
    + connect splitter to left/right analyser: `splitter.connect(analyserLeft, 0, 0); splitter.connect(analyserRight. 0. 0);`
  + draw volume meters: `function drawVolumeMeters() {...}`
    + save canvas ctx: `canvasContext.save();`
    + set fill style: `canvasContext.fillStyle = gradient;`
    + compute left channel data: `analyserLeft.getByteFrequencyData(dataArrayLeft); var averageLeft = getAverageVolume(dataArray);`
    + draw vertical meter for left channel: `canvasContext.fillRect(0, height-averageLeft, 25 height);`
    + compute right channel data: `analyserRight.getByteFrequencyData(dataArrayRight); var averageRight = getAverageVolume(dataArray);`
    + draw vertical meter for right channel: `canvasContext.fillRect(26, height-averageRight, 25 height);`
    + restore canvas ctx: `canvasContext.restore();`

+ Accurate implementation of volume meter
  + the above method inaccurate in terms of real volume meter
  + cwilso approximation
    + [simple volume meter](https://github.com/cwilso/volume-meter)
    + `var meter = createAudioMeter(audioContext,clipLevel,averaging,clipLag);`
  + SoundSpinning approximation
    + using `getFloatTimeDomainData` from analyser w/ nmormalized array valued btw -1 and 1
    + still not accurate but closer, e.g., 60kHz on canvas as audio smapling on 44.1kHz


### 1.5.8 Sound samples loaded in memory

For some applications, it may be necessary to load sound samples into memory and uncompress them before they can be used.

+ No streaming/decoding in real time means less CPU is used,
+ With all samples loaded in memory, it's possible to play them in sync with great precision,
+ It's possible to make loops, add effects, change the playback rate, etc.
+ And of course, if they are in memory and uncompressed, there is no wait time for them to start playing: they are ready to be used immediately!

These features are useful in video games: where a library of sounds may need to ready to be played. By changing the playback rate or the effects, many different sounds can be created, even with a limited number of samples (for instance, an explosion played at different speed, with different effects).


#### Examples

__Let's try some demos!__

Here is a first [example at JSBin](https://jsbin.com/gojuxo/edit?html,js,console,output): click on the different buttons. Only two minimal sound samples are used in this example: [shot1.mp3](https://mainline.i3s.unice.fr/mooc/shoot1.mp3) and [shot2.mp3](https://mainline.i3s.unice.fr/mooc/shoot2.mp3). You can download many free sound samples like these from the freesound.org Web site.

[Local Demo](src/01e-example21.html)

Here is how the WebAudio graph looks like (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open("https://bit.ly/2TurtPU")"
    src    = "https://bit.ly/3i4Lc2G"
    alt    = "Screenshot with buttons that play sound samples many times with different pitch, volume, interval of times"
    title  = "Screenshot with buttons that play sound samples many times with different pitch, volume, interval of times"
  />
</figure>

Music applications such as Digital Audio Workstations (GarageBand-like apps) will need to play/record/loop music tracks in memory.

[Try this impressive DAW](https://remixxer.com/app/) that uses free sound samples from freesound.org! Each instrument is a small audio file that contains all the notes played on a real instrument. When you play a song (midi file) the app will play-along, selecting the same musical note from the corresponding instrument audio sample. This is all done with Web Audio and samples loaded in memory:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open("https://bit.ly/2TurtPU")"
    src    = "https://bit.ly/3c3alXF"
    alt    = "The remixer DAW workstation, a typical screenshot of a DAW with tracks, mix table etc."
    title  = "The remixer DAW workstation, a typical screenshot of a DAW with tracks, mix table etc."
  />
</figure>


The author of this course wrote a multitrack audio player: it loads different mp3 files corresponding to different instruments and play/loop them in sync.

[You can try](https://mainline.i3s.unice.fr/) it or get [the sources on GitHub](https://github.com/squallooo/MT5). The documentation is in the help menu.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/2TurtPU")"
    src    = "https://bit.ly/34yYNrc"
    alt    = "Screenshot of MT5 a multitrack player"
    title  = "Screenshot of MT5 a multitrack player"
  />
</figure>

Try also this small demonstration that uses the [Howler.js](https://goldfirestudios.com/blog/104/howler.js-Modern-Web-Audio-Javascript-Library) library for loading sound samples in memory and playing them using WebAudio (we'll discuss this library later). Click on the main window and notice how fast the sound effects are played. Click as fast as you can!

[Try the explosion demo at JSBin](https://jsbin.com/gefezu/edit):

[Local Demo](src/01e-example22.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/2TurtPU")"
    src    = "https://bit.ly/34MxZE9"
    alt    = "Screenshot of an example that plays sound in memory. It's an explosion framework based on a particle system"
    title  = "Screenshot of an example that plays sound in memory. It's an explosion framework based on a particle system"
  />
</figure>


#### Notes for 1.5.8 Sound samples loaded in memory

+ Applications w/ audio im memory
  + no streaming/decoding in real time $\to$ less CPU used
  + possible to play in-memory samples in sync w/ great precision
  + possible to make loops, add effects, change the playback rate, etc.
  + no wait time to start playing



### 1.5.9 Load and play sound samples

Use an `AudioBufferSourceNode` as the source of the sound sample in the Web Audio graph.

There is a special node in Web Audio for handling sound samples, called an [`AudioBufferSourceNode`](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode).

This node has different properties:

+ `buffer`: the decoded sound sample.
+ `loop`: should the sample be played as an infinite loop - when the sample has played to its end, it is re-started from the beginning. (default is True), it also depends on the two next properties.
+ `loopStart`: a double value indicating, in seconds, in the buffer sample playing must restart. Its default value is 0.
+ `loopEnd`: a double value indicating, in seconds, at what point in the buffer sample playing must stop (and eventually loop again). Its default value is 0.
+ `playbackRate`: the speed factor at which the audio asset will be played. Since no pitch correction is applied on the output, this can be used to change the pitch of the sample.
+ `detune`: not relevant for this course.


#### Loading and decoding a sound sample

__Before use, a sound sample must be loaded using Ajax, decoded, and set to the `buffer` property of an `AudioBufferSourceNode`.__

Try the [example at JSBin](https://jsbin.com/botagas/edit?html,js,console,output):

[Local Demo](src/01e-example23.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3uPRR3P")"
    src    = "https://bit.ly/3pckbMc"
    alt    = "example that loads and play a unique sound"
    title  = "example that loads and play a unique sound"
  />
</figure>


In this example, as soon as the page is loaded, we send an Ajax request to a remote server in order to get the file shoot2.mp3. When the file is loaded, we decode it. Then we enable the button (before the sample was not available, and thus could not be played). Now you can click on the button to make the noise.

Notice in the code that each time we click on the button, we rebuild the audio graph.

<p class="exampleHTML" style="color: red; text-align: center;"><strong>This is because AudioBufferSourceNodes can be used only once!&nbsp;<br></strong><br>But don't worry, Web Audio is optimized for handling thousands of nodes...</p>

HTML code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"playButton"</span><span class="pln"> </span><span class="atn">disabled</span><span class="pun">=</span><span class="atv">true</span><span class="tag">&gt;</span><span class="pln">Play sound</span><span class="tag">&lt;/button&gt;</span></li>
</ol></div><br>

JavaScript source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> <g class="gr_ gr_136 gr-alert gr_spell gr_run_anim ContextualSpelling ins-del multiReplace" id="136" data-gr-id="136">ctx</g></span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> soundURL </span><span class="pun">=</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">'https://mainline.i3s.unice.fr/mooc/shoot2.mp3'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> decodedSound</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// The page has been loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="com">// To make it work even on browsers like Safari, that still</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// do not recognize the non prefixed version of AudioContext</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> audioContext </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">webkitAudioContext</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;ctx </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> audioContext</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;loadSoundUsingAjax</span><span class="pun">(</span><span class="pln">soundURL</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// By default the button is disabled, it will be</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// clickable only when the sound sample will be loaded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;playButton</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; playSound</span><span class="pun">(</span><span class="pln">decodedSound</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadSoundUsingAjax</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> request </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Important: we're loading binary data</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">responseType </span><span class="pun">=</span><span class="pln"> </span><span class="str">'arraybuffer'</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Decode asynchronously</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;request</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Sound loaded"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Let's decode it. This is also asynchronous</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; ctx</span><span class="pun">.</span><span class="pln">decodeAudioData</span><span class="pun">(</span><span class="pln">request</span><span class="pun">.</span><span class="pln">response</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; function</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ // success</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Sound decoded"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;decodedSound </span><span class="pun">=</span><span class="pln"> buffer</span><span class="pun">; &nbsp; &nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// we enable the button</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;playButton</span><span class="pun">.</span><span class="pln">disabled </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ // error</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"error"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; ); // end of decodeAudioData callback</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}; &nbsp; // end of the onload callback</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Send the request. When the file will be loaded,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// the request.onload callback will be called (above)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; request</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> playSound</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">){</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pun">&nbsp; &nbsp; // builds the audio graph, then start playing the source</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> bufferSource </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createBufferSource</span><span class="pun">();</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; bufferSource</span><span class="pun">.</span><span class="pln">buffer </span><span class="pun">=</span><span class="pln"> buffer</span><span class="pun">;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; bufferSource</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; bufferSource</span><span class="pun">.</span><span class="pln">start</span><span class="pun">(); // remember, you can start() a source only once!</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
</ol></div><br>

__Explanations:__

+ When the page is loaded, we first call the `loadSoundUsingAjax` function for loading and decoding the sound sample (_line 16_), then we define a click listener for the play button. Loading and decoding the sound can take some time, so it's an asynchronous process. This means that the call to `loadSoundUsingAjax` will return while the downloading and decoding is still in progress. We can define a click listener on the button anyway, as it is disabled by default (see the HTML code). Once the sample has been loaded and decoded, only then will the button be enabled (_line 42_).
+ The `loadSoundUsingAjax` function will first create an `XmlHttpRequest` using the "new version of Ajax called XhR2" (described in detail during week 3). First we create the request (_lines 26-30_): notice the use of '`arrayBuffer`' as a `responseType` for the request. This has been introduced by Xhr2 and is necessary for binary file transfer. Then the request is sent (_line 52_).
+ Ajax is an asynchronous process: once the browser receives the requested file, the `request.onload` callback will be called (it is defined at _line 33_), and we can decode the file (an mp3, the content of which must be uncompressed in memory). This is done by calling `ctx.decodeAudioData(file, successCallback, errorCallback)`.  When the file is decoded, the success callback is called (_lines 38-43_). We store the decoded buffer in the variable decodedSound, and we enable the button.
+ Now, when someone clicks on the button, the `playSound` function will be called (_lines 55-61_). This function builds a simple audio graph: it creates an `AudioBufferSourceNode` (_line 57_), sets its buffer property with the decoded sample, connects this source to the speakers (_line 59_) and plays the sound. <span style="color: pink;">Source nodes can only be used once (a "fire and forget" philosophy), so to play the sound again, we have to rebuild a source node and connect that to the destination. This seems strange when you learn Web Audio, but don't worry - it's a very fast operation, even with hundreds of nodes.</span>


#### The `BufferLoader` Utility

__Loading and decoding multiple sounds: the `BufferLoader` utility__

__The problem: AJax requests are asynchronous__

The asynchronous aspect of Ajax has always been problematic for beginners. For example, if our applications use multiple sound samples and we need to be sure that all of them are loaded and decoded, using the code we presented in the earlier example will not work as is. We cannot call:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">loadSoundSample</span><span class="pun">(</span><span class="pln">urlOfSound1</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">loadSoundSample</span><span class="pun">(</span><span class="pln">urlOfSound2</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">loadSoundSample</span><span class="pun">(</span><span class="pln">urlOfSound3</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">etc</span><span class="pun">...</span></li>
</ol></div><br>

... because we will never know exactly when all the sounds have finished being loaded and decoded. All these calls will run operations in the background yet return instantly.


#### Preloading Sound and Image Assets

__The BufferLoader utility object: useful for preloading sound and image assets__

There are different approaches for dealing with this problem. During the HTML5 Coding Essentials and Best Practices course, we presented utility functions for loading multiple images. Here we use the same approach and have packaged the code into an object called the BufferedLoader.

[Example at JSBin](https://jsbin.com/javoger/edit?html,js,console,output) that uses the BufferLoader utility:

[Local Demo](src/01e-example24.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3uPRR3P")"
    src    = "https://bit.ly/3wPR5VC"
    alt    = "Example that loads two sounds and create two buttons for playing them"
    title  = "Example that loads two sounds and create two buttons for playing them"
  />
</figure>


HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"shot1Normal"</span><span class="pln"> </span><span class="atn">disabled</span><span class="pun">=</span><span class="atv">true</span><span class="tag">&gt;</span><span class="pln">Shot 1</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"shot2Normal"</span><span class="pln"> </span><span class="atn">disabled</span><span class="pun">=</span><span class="atv">true</span><span class="tag">&gt;</span><span class="pln">Shot 2</span><span class="tag">&lt;/button&gt;</span></li>
</ol></div><br>


JavaScript code extract (does not contain the BufferLoader utility code):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> listOfSoundSamplesURLs </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">'https://mainline.i3s.unice.fr/mooc/shoot1.mp3'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">'https://mainline.i3s.unice.fr/mooc/shoot2.mp3'</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// To make it work even on browsers like Safari, that still</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="com">// do not recognize the non prefixed version of AudioContext</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">&nbsp; var</span><span class="pln"> audioContext </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">webkitAudioContext</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; ctx </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> audioContext</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; loadAllSoundSamples</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> playSampleNormal</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">){</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; // builds the audio graph and play</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> bufferSource </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createBufferSource</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferSource</span><span class="pun">.</span><span class="pln">buffer </span><span class="pun">=</span><span class="pln"> buffer</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferSource</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferSource</span><span class="pun">.</span><span class="pln">start</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> onSamplesDecoded</span><span class="pun">(</span><span class="pln">buffers</span><span class="pun">){</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"all samples loaded and decoded"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// enables the buttons</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;shot1Normal</span><span class="pun">.</span><span class="pln">disabled</span><span class="pun">=</span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;shot2Normal</span><span class="pun">.</span><span class="pln">disabled</span><span class="pun">=</span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// creates the click listeners on the buttons</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;shot1Normal</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; playSampleNormal</span><span class="pun">(</span><span class="pln">buffers</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;shot2Normal</span><span class="pun">.</span><span class="pln">onclick </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; playSampleNormal</span><span class="pun">(</span><span class="pln">buffers</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadAllSoundSamples</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// onSamplesDecoded will be called when all samples </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// have been loaded and decoded, and the decoded sample will</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// be its only parameter (see function above)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferLoader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">BufferLoader</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">,&nbsp;</span><span class="pln" style="line-height: 1.6;">listOfSoundSamplesURLs</span><span class="pun" style="line-height: 1.6;">,</span><span style="color: #000000; line-height: 1.6; background-color: #ffffff;">onSamplesDecoded</span>);</li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// starts loading and decoding the files</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; bufferLoader</span><span class="pun">.</span><span class="pln">load</span><span class="pun">();</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

After the call to `loadAllSoundSamples()` (_line 13_), when all the sound sample files have been loaded and decoded, a callback will be initiated to `onSamplesDecoded(decodedSamples)`, located at _line 25_. The array of decoded samples is the  parameter of the `onSamplesDecoded` function.

The `BufferLoader` utility object is created at _line 45_ and takes as parameters: 1) the audio context, 2) an array listing the URLs of the different audio files to be loaded and decoded, and 3) the callback function which is to be called once all the files have been loaded and decoded. This callback function should accept an array as its parameter: the array of decoded sound files.

To study the source of the `BufferLoaded` object, look at the JavaScript tab in [the example at JSBin](https://jsbin.com/gegita/edit?html,js,console,output). 

[Local Demo](src/01e-example25.html)


####  Example: Two Sound Samples

__Playing the two sound samples at various playback rates, repeatedly__

This is a variant of the previous example (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension).

[Example at JSBin](https://jsbin.com/zebokeg/edit?html,js,console,output):

[Local Demo](src/01e-example26.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open("https://bit.ly/3uPRR3P")"
    src    = "https://bit.ly/3vJ9nHZ"
    alt    = "Audio Graph used in the previous example source node -> gain -> compressor -> destination"
    title  = "Audio Graph used in the previous example source node -> gain -> compressor -> destination"
  />
</figure>


In this example, we added a function (borrowed and adapted from this [article on HTML5Rocks](https://www.html5rocks.com/en/tutorials/webaudio/games/)):

+ `makeSource(buffer)`

Here is the source code of this function:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> makeSource</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// build graph source -&gt; gain -&gt; compressor -&gt; speakers</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// We use a compressor at the end to cut the part of the signal</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// that would make peaks</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// create the nodes</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> source </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createBufferSource</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> compressor </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createDynamicsCompressor</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> gain </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">createGain</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// set their properties</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Not all shots&nbsp;will have the same volume</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;gain</span><span class="pun">.</span><span class="pln">gain</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0.2</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;source</span><span class="pun">.</span><span class="pln">buffer </span><span class="pun">=</span><span class="pln"> buffer</span><span class="pun">;<br></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Build the graph</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;source</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">gain</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; gain</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">compressor</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; compressor</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">ctx</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">return</span><span class="pln"> source</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

And this is the function that plays different sounds in a row, eventually creating random time intervals between them and random pitch variations:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> playSampleRepeated</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">,</span><span class="pln"> rounds</span><span class="pun">,</span><span class="pln"> interval</span><span class="pun">,</span><span class="pln"> random</span><span class="pun">,</span><span class="pln"> random2</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">typeof</span><span class="pln"> random </span><span class="pun">==</span><span class="pln"> </span><span class="str">'undefined'</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; random </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">typeof</span><span class="pln"> random2 </span><span class="pun">==</span><span class="pln"> </span><span class="str">'undefined'</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; random2 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> time </span><span class="pun">=</span><span class="pln"> ctx</span><span class="pun">.</span><span class="pln">currentTime</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Make multiple sources using the same buffer and play in quick succession.</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> rounds</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> source </span><span class="pun">=</span><span class="pln"> makeSource</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; source</span><span class="pun">.</span><span class="pln">playbackRate</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> random2</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; source</span><span class="pun">.</span><span class="pln">start</span><span class="pun">(</span><span class="pln">time </span><span class="pun">+</span><span class="pln"> i </span><span class="pun">*</span><span class="pln"> interval </span><span class="pun">+</span><span class="pln"> </span><span class="typ">Math</span><span class="pun">.</span><span class="pln">random</span><span class="pun">()</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> random</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

__Explanations:__

+ _Lines 11-15_: we make a loop for building multiple routes in the graph. The number of routes corresponds to the number of times that we want the same buffer to be played. Note that the random2 parameter enables us to randomize the playback rate of the source node that corresponds to the pitch of the sound. 
+ _Line 14_: this is where the sound is being played. Instead of calling source.start(), we call source.start(delay), this tells the Web Audio scheduler to play the sound after a certain time. 
+ The makeSource function builds a graph from one decoded sample to the speakers. A gain is added that is also randomized in order to generate shot sounds with different volumes (between 0.2 and 1.2 in the example). A compressor node is added in order to limit the max intensity of the signal in case the gain makes it peak.


#### Notes for 1.5.9 Load and play sound samples

+ The [`AudioBufferSourceNode` object](https://developer.mozilla.org/en-US/docs/Web/API/AudioBufferSourceNode)
  + used as the source of the sound sample in the Web Audio graph
  + handling sound samples
  + used only once
  + properties:
    + `buffer`: the decoded sound sample
    + `loop`: boolean value, sound sample played as an infinite loop
    + `loopStart`: a double value, in seconds, indicating the point in buffer where the loop restarts, default value = 0
    + `loopEnd`: a double value, in seconds, indicating the point in buffer where the playing stops, default value = 0
    + `playbackRate`: the speed factor, used to change the pitch of the sample
    + `detune`: a k-rate AudioParam representing detuning of playback in cents, a logarithmic unit of measure used for musicl intervals

+ Example: `AudioBufferSourceNode` to load and decoding sound sample
  + HTML snippet: `<button id="playButton" disabled=true>Play sound</buton>`
  + Javascript snippet:
    + declare global variables: `var ctx; var soundURL = 'https://.../shoot2.mp3'; vadr decodedSound;`
    + init after DOM ready: `window.onload = function int() {...}`
      + create audio ctx: `var audioContext = window.AudioContext || window.webkitAudioContext; ctx = new audioContext();`
      + call to load and decode sound w/ Ajax: `loadSoundUsingAjax(soundURL);`
      + add listener to play sound: `playButton.onclick = function(evt) { playSound(deciodedSound); };`
    + load and decode sound w/ Ajax: `function loadSoundUsingAjax(url) {...}`
      + open connecction: `var request = new XMLHttpRequest(); request.open('GET', url, true); request.responsType = 'arraybuffer';`
      + decode asynchronously: `reuest.onload = function () {...}`
        + log msg: `console.log("Sound loaded");`
        + decode sound: `ctx.decodeAudioData(request.response. function(buffer) {//success}, function(e) {//errror} );`
          + success: `console.log("Sound decoded"); decodedSound = buffer; playButton.disabled = false;`
          + error: `console.log("error");`
      + send the request: `request.send();`
    + play sound<a name="playSound"></a>: `function playSound(buffer) {...}`
      + build audio graph: `var bufferSource = ctx.createBufferSource(); bufferSource.buffer = buffer; bufferSource.connect(ctx.destiunation);`
      + start to play the sound: `bufferSource.start();`

+ The `BufferLoader` utility
  + usful for preloading and sound and image assets
  + issue: assynchronlously request via Ajax
  + applications w/ multiple sound samples: ensuring loaded and decoded them all before starting
  + loading sound samples and triggering event individually $\to$ unable to ensure all sound samples loaded

+ Example: preloading sound samples w/ `BufferLoader`
  + HTML snippet - buttons: `<button id="shot1Normal" disabled=true>Shot 1</button><button id="shot2Normal" disabled=true>Shot 2</button>`
  + JavaScript snippet:
    + set sound assets: `var listOfSoundSamplesURLs = ['https://.../shot1.mp3', 'https://.../shot2.mp3'];`
    + init page after DOM ready: `window.onload = function init() {...};`
      + create [audio context](#audioCtx)
      + call to load lal sound samples: `loadAllSoundSamples();`
    + build [audio graph and play](#playSound)
    + decode samples: `function onSamplesDecoded(buffers) {...}`
      + log msg: `console.log("all samples loaded and decoded");`
      + enable buttons: `shot1Normal.disalbed = false; shot2Normal.disabled = false;`
      + add click listener on button 1: `shot1Normal.onclick = function(evt) { playSampleNormal(buffers[0]); };`
      + add click listener on button 2: `shot2Normal.onclick = function(evt) { playSampleNormal(buffers[1]); };`
    + load all sound samles: `fucntion loadAllSoundSamples() {...}`
      + create loader w/ callback `onSamplesDecoded`: `bufferLoader = new BufferLoader(ctx, listOfSoundSamplesURLs, onSampllesDecoded);`
      + start loading adn decoding smaples: `bufferLoader.load();`

+ Example: playing 2 sound samples w/ different rates
  + audio graph: source $\to$ gain $\to$ compressor $\to$ speakers
  + make source: `function makeSource(buffer) {...}`
    + create nodes: `var source = ctx.createBufferSource(); var compressor = ctx.createDynamicsCompressor(); cvar gain = ctx.createGain();`
    + set gain node property: `gain.gain.value = 0.2 + Math.random();`
    + assign sound samplle: `source.buffer = buffer;`
    + connect nodes: `soource.connect(gain); gain.connect(compressor); compressor.connect(ctx.destiantion);`
    + return the head of graph: `return source;`
  + play different sound samples repeatedly: `function playSampleRepeated(buffer, rounds, interval, random, random2) {...}`
    + set random values if not defined: `if (typeof random == 'undefined') {random = 0; }; if (typeof random2 == 'undefined' ) {random2 = 0; }`
    + get current time: `var time = ctx.currentTime;`
    + use a sound sample as multiple sound sources and play: `for (var i=0; i<sounds; i++) {...}`
      + assign sound sample: `var source = makeSource(buffer);`
      + assign playing rate: `source.playbackRate.value = 1 + Math.random() * random2;`
      + assign the start time: `source.start(time + i * interval + Math.random() * random);`



#### Knowledge check 1.5.9

1. Video games often need to play sound samples in rapid sequence, with different effects, pitch, etc. What best practice has been presented in the course?

  a. They should be loaded and decoded, before being used.<br>
  b. All sound samples must be loaded before being used.<br>

  Ans: a<br>
  Explanation: Indeed, all sound samples must be decoded and loaded into memory before playing with them. Due to the asynchronous nature of Ajax and of the decoding process, this operation can be tricky when you need to download and decode multiple sound samples before starting your application. This is why we recommend the BufferLoader utility.



### 1.5.10 Sound samples and effects

Any of the effects that discussed during these lectures (gain, stereo panner, reverb, compressor, equalizer, analyser node for visualization, etc.) may be added to the audio graphs that we have built in our sound sample examples.

Below, we have mixed the code from two previous examples:

[This one at JSBin](https://jsbin.com/vejocav/edit?html,css,js,output):

[Local Demo](src/01e-example27.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3uOirdC")"
    src    = "https://bit.ly/2St4DY8"
    alt    = "audio player with volume meters and waveform"
    title  = "audio player with volume meters and waveform"
  />
</figure>


And [this one at JSBin](https://jsbin.com/nazega/edit?html,js,console,output) (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

[Local Demo](src/01e-example28.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3uOirdC")"
    src    = "https://bit.ly/2RbHpWk"
    alt    = "multiple sound samples played at different intervals and rates"
    title  = "multiple sound samples played at different intervals and rates"
  />
</figure>

And here is the result ([try it at JSBin](https://jsbin.com/coraso/edit?html,js,console,output)):

[Local Demo](src/01e-example29.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open("https://bit.ly/3uOirdC")"
    src    = "https://bit.ly/3g0Ty98"
    alt    = "Sound samples and 2D visualization"
    title  = "Sound samples and 2D visualization"
  />
</figure>

Here is the audio graph of this example (picture taken with the now discontinued FireFox WebAudio debugger, you should get similar results with the Chrome WebAudio Inspector extension):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3uOirdC")"
    src    = "https://bit.ly/3g0nDp7"
    alt    = "audio graph of the previous example"
    title  = "audio graph of the previous example"
  />
</figure>

Look at the source code on JSBin, it's a quick merge of the two previous examples.



### 1.5.11 Useful third party libraries

It's best practice to know the Web Audio API itself. Many of the examples demonstrated during this course may be hard to write using high-level libraries. However, if you don't have too many custom needs, such libraries can make your life simpler! Also, some libraries use sound synthesis that we did not cover in the course and are fun to use - for example, adding 8-bit sounds to your HTML5 game!

Many JavaScript libraries have been built on top of WebAudio. We recommend the following:

+ HowlerJS: useful for loading and playing sound sample in video games. Can handle audio sprites (multiple sounds in a single audio file), loops, spatialization. Very simple to use. Try this [very simple example](https://jsbin.com/wuteqo/edit?html,js,output) we prepared for you at JsBin that uses HowlerJS!
+ [Webaudiox](https://blog.jetienne.com/blog/2014/02/27/webaudiox-jsfx/), and in particular a helper built with this library, jsfx for adding 8-bit procedural sounds to video games, without the need to load audio files. [Try the demo](https://jeromeetienne.github.io/webaudiox/examples/jsfx.html)! There is also a [sound generator](https://egonelbre.com/project/jsfx/) you can try. When you find a sound you like, just copy and paste the parameter values into your code.
+ For writing musical applications, take a look at [ToneJS](https://github.com/Tonejs/Tone.js)!


#### Notes for 1.5.11 Useful third party libraries

+ Useful 3rd party libraries
  + [HowlerJS](https://howlerjs.com/)
  + [Webaudiox](https://blog.jetienne.com/blog/2014/02/27/webaudiox-jsfx/)
  + [ToneJS](https://github.com/Tonejs/Tone.js)


### 1.5.12 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics of discussion

+ Prior to this week, did you know that all the things presented in this course could be accomplished in a Web application? 
+ Which interesting tools / libraries have you found for using WebAudio?
+ Do you have any experience with audio processing? If so, please post a message in the forum as we need help designing a good sounding distortion effect/amp simulator for guitar!

#### Optional projects

+ We would like to see the best audio visualizations possible! Drawing wave forms and frequency bars is so common!... Please show us some psychedelic animations or use something like this: 

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3papfkv" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3yUiFmp"
      alt   = "vu meter analogicvu meter"
      title = "vu meter analogicvu meter"
    >
    <img style="margin: 0.1em;" height=150
      src   = "https://bit.ly/3wT3gkq"
      alt   = "vu meter analogicvu meter"
      title = "vu meter analogicvu meter"
    >
  </a>
</div>


By the way, look at this, too. It uses the techniques we saw for drawing volume meters: it animates different shapes and colors that follow the beat of the music.

And here is an impressive music visualization example written by a student of this course.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick= "window.open("https://bit.ly/3papfkv")"
    src    = "https://bit.ly/3yURVlM"
    alt    = "audio visualization example"
    title  = "audio visualization example"
  />
</figure>

+ And... we would like to see the ultimate audio or video player, with great effects: reverb, equalizer, stereo, compressor, etc.
+ __Make a graphic equalizer__: take the code from the example given in the course, mix it with the one from [the application that draws the frequency response of a single filter](https://webaudioapi.com/samples/frequency-response/), and make a multi-band graphic equalizer, perhaps inspired by this one:

  <figure style="margin: 0.5em; text-align: center;">
    <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
      onclick= "window.open("https://bit.ly/3papfkv")"
      src    = "https://bit.ly/3g0YIlw"
      alt    = "graphic equalizer"
      title  = "graphic equalizer"
    />
  </figure>

+ __Sound sample project:__ try to make a small multi track player (load the files in memory like sound samples). You can get free multi track audio files [on this Web site](https://www.cambridge-mt.com/ms-mtk.htm) (or find real multi track songs by famous artists - many have been ripped from the Guitar Hero or Rock Band games and are available as Moog files on the Web).
+ __Audio samples:__ prepare a set of audio samples for the video game you will develop during Week 2. Register on [freesound.org](https://freesound.org/), download the sounds, prepare a small app that uses the BufferLoader utility that we presented in the course, add buttons to the page to play them, and why not add some effects, too?





