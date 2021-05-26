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
    + audio element: `<audio id="player" controls crossorigin="anonymous" loop>...</audio>`
    + source element: `<source src="https://.../guitarRiff1.mp3">`
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

Definition: "The `ConvolverNode` interface is an AudioNode that performs a Linear Convolution on a given AudioBuffer, __often used to achieve a reverb effect__. A ConvolverNode always has exactly one input and one output."

See the [Convolver node's documentation](https://developer.mozilla.org/en-US/docs/Web/API/ConvolverNode).

[Example at JSBin](https://jsbin.com/belide/edit?html,js,console,output), THIS EXAMPLE DOES NOT WORK IN YOUR BROWSER as the edX platforms disables Ajax loading in its HTML pages. Try it at JSBin!

<p class="exampleHTML"><audio id="convolverPlayer" src="https://mainline.i3s.unice.fr/mooc/guitarRiff1.mp3" loop="loop" controls="controls" crossorigin="anonymous"></audio> <br> <label for="convolverSlider">Reverb (Dry/Wet)</label> <input id="convolverSlider" min="0" max="1" step="0.1" value="0" type="range"></p>

> [From Wikipedia:](https://en.wikipedia.org/wiki/Convolution) a convolution is a mathematical process which can be applied to an audio signal to achieve many interesting high-quality linear effects. Very often, the effect is used to simulate an acoustic space such as a concert hall, cathedral, or outdoor amphitheater. It can also be used for complex filter effects, like a muffled sound coming from inside a closet, sound underwater, sound coming through a telephone, or playing through a vintage speaker cabinet. This technique is very commonly used in major motion picture and music production and is considered to be extremely versatile and of high quality.

Each unique effect is defined by an impulse response. An impulse response can be represented as an audio file and can be recorded from a real acoustic space such as a cave, or can be synthetically generated through a wide variety of techniques. We can find many high quality impulses on the Web (for example @@TJS OK? here). The impulse used in the example is the one recorded at the opera: La Scala Opera of Milan, in Italy. It's a .wav file.

Try [this demo](https://webaudioapi.com/samples/room-effects/) to see the difference between different impulse files!

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3wCeY2L")"
    src    = "https://bit.ly/3fj5fsz"
    alt    = "screenshot of a webapp that enable to switch between different impulse files"
    title  = "screenshot of a webapp that enable to switch between different impulse files"
  />
</figure>


So before building the audio graph, we need to download the impulse. For this, we use an Ajax request (this will be detailed during Module 3), but for the moment, just take this function as it is... The Web Audio API requires that impulse files should be decoded in memory before use. Accordingly, once the requested file has downloaded, we call the decodeAudioData method. Once the impulse is decoded, we can build the graph. So typical use is as follows:

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

> Definition: "The DynamicsCompressorNode interface provides a compression effect, which lowers the volume of the loudest parts of the signal in order to help prevent clipping and distortion that can occur when multiple sounds are played and multiplexed together at once. This is often used in musical production and game audio."

It's usually a good idea to insert a compressor in your audio graph to give a louder, richer and fuller sound, and to prevent clipping. See the [Dynamics Compressor node's documentation](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode).

[Example you can try on JSBin](https://jsbin.com/momixok/edit?html,js,console,output) or try it here in your browser:

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





### 1.5.4 Writing an equalizer






### 1.5.5 Waveforms






### 1.5.6 Frequencies







### 1.5.7 Volume meters






### 1.5.8 Sound samples loaded in memory







### 1.5.9 Load and play sound samples






### 1.5.10 Sound samples and effects






### 1.5.11 Useful third party libraries






### 1.5.12 Discussion and projects







