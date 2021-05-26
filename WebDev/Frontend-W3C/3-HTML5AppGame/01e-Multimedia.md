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
    + create context: `var ctx = window.AudioContext || window.webkitAudioContext; var audioContext;`
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
<li class="L4" style="margin-bottom: 0px;"><span class="pun"><span class="pun" style="line-height: 25.6px;"><span style="color: #000000; line-height: 25.6px;">sourceNode</span>.<span color="#000000" style="color: #000000;">connect</span></span><span class="pun" style="line-height: 25.6px;">(context.destination</span><span class="pun" style="line-height: 25.6px;">); // connect to the speakers</span></span></li>
</ol></div><br>

The `MediaElementSource` node  is built using `context.createMediaElementSource(elem)`, where `elem` is an `<audio>` or a `<video>` element.

Then we connect this source Node to other nodes. If we connect it directly to `context.destination`, the sound goes to the speakers with no additional processing.

In the following lessons, we will see the different nodes that are useful with streamed audio and with the `MediaElementSource` node. Adding them in the audio graph will enable us to change the sound in many different ways.





### 1.5.3 Most useful filter nodes






### 1.5.4 Writing an equalizer






### 1.5.5 Waveforms






### 1.5.6 Frequencies







### 1.5.7 Volume meters






### 1.5.8 Sound samples loaded in memory







### 1.5.9 Load and play sound samples






### 1.5.10 Sound samples and effects






### 1.5.11 Useful third party libraries






### 1.5.12 Discussion and projects







