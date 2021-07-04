# Module 3: HTML5 file upload and download section


## 3.2 File API and Ajax / XHR2 requests


### 3.2.1 Ajax and XHR2

We present below a short history of Ajax: an introduction to XMLHttpRequest level 2 (XHR2).

> __Wikipedia definition:__ "Ajax, short for Asynchronous JavaScript and XML), is a group of interrelated Web development techniques used on the client-side to create asynchronous Web applications. With Ajax, Web applications can send data to and retrieve from a server asynchronously (in the background) without interfering with the display and behavior of the existing page. Data can be retrieved using the XMLHttpRequest object. Despite the name, the use of XML is not required (JSON is often used), and the requests do not need to be asynchronous."

Ajax appeared around 2005 with Google Maps, and is now widely used. We are not going to teach you Ajax programming, but instead focus on the relationships between "the new version of Ajax", known as XHR2 (for XmlHttpRequest level 2) and the [File API](https://www.w3.org/TR/FileAPI/) (seen in the W3Cx [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) MOOC). Also, you will discover that the HTML5 `<progress>` element is of great use for monitoring the progress of file uploads (or downloads).

We recommend reading [this article from HTML5Rocks.com](https://www.html5rocks.com/en/tutorials/file/xhr2/) that presents the main features of XHR2.

Briefly, these improvements include:

+ New, easier to use syntax,
+ In-browser encoding/decoding of binary files,
+ Progress monitoring of uploads and downloads.

The following sections of this course present a few examples of file downloads/uploads together with the file API and show how to monitor progress.

The current support of XHR2 is excellent: see related [CanIUse's browser compatibility table](https://caniuse.com/#feat=xhr2).


#### Notes for 3.2.1 Ajax and XHR2

+ Asynchronous JavaScript and XML (Ajax)
  + a group of interrelated Web development techniques
  + used on the client-side to create asynchronous Web application
  + Web applications able to send data to and retrieve from a server asynchronously w/o interfering w/ the display and behavior of the existing page
  + data retrieved via the `XMLHttpRequest` object, usually JSON format used than XML
  + the new version of Ajax
    + XmlHttpRequest level 2 (XHR2)
    + improvement
      + easier to use syntax
      + in-browser encoding/decoding of binary files
      + progress monitoring of uploads and downloads


### 3.2.2 Ajax/XHR2 and binary files

#### Live coding video: downloading files

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3hhbMVq)


#### Ajax and binary files

__Ajax and binary files - downloading files and monitoring progress__

HTTP is a text based protocol, so when you upload/download images, videos or any binary file, they must first be text encoded for transmission, then decoded on-the-fly upon receipt by the server or browser. For a long time, when using Ajax, these binary files had to be decoded "by hand", using JavaScript code. Not recommended!

We won't go into too much detail here, but  all browsers (> 2012) support XHR2. XHR2 adds the option to directly download binary data. With XHR2, you can ask the browser to encode/decode the file you send/receive, natively. To do this, when you use `XMLHttpRequest` to send or receive a file, you must set the `xhr.responseType` as `arrayBuffer`.

Below is a function that loads a sound sample using XMLHttpRequest level 2.

_Note_: 1) the simple and concise syntax, and 2) the use of the new `arrayBuffer` type for the expected response (_line 5_):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Load a binary file from a URL as an ArrayBuffer.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadSoundFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);<br><br></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>xhr</strong></span><strong><span class="pun">.</span><span class="pln">responseType </span><span class="pun">=</span><span class="pln"> </span><span class="str">'arraybuffer'</span><span class="pun">;</span><span class="com" style="color: #ff0000;"></span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; initSound</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">response</span><span class="pun">);</span><span class="pln"> </span><span class="com">// this.response is an ArrayBuffer.</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};<br><br></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>


#### Play downloaded song

__Example: download a binary song file using XHR2 and responseType='arraybuffer', and play it using Web Audio__

Try [this example](https://jsbin.com/mecakaz/edit?html,js,console,output) on JSBin:

[Local Demo](src/03b-example01.html)

In this example, instead of reading the file from disk, we download it using XHR2.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2TwBOet')"
    src    = "https://bit.ly/3hyjzgH"
    alt    = "Downloading file with Xhr2"
    title  = "Downloading file with Xhr2"
  />
</figure>


Complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">XHR2 and binary files + Web Audio API</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Example of using XHR2&nbsp;and </span><span class="tag">&lt;code&gt;</span><span class="pln">xhr.responseType = 'arraybuffer';</span><span class="tag">&lt;/code&gt;</span><span class="pln"> to download a binary sound file</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> and start playing it on user-click using the Web Audio API.</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h2&gt;</span><span class="pln">Load file using Ajax/XHR2 and the arrayBuffer response type</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">downloadSoundFile</span><span class="pun">(</span><span class="str">'https://myserver.com/song.mp3'</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;Download and play example song.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/button&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">playSound</span><span class="pun">()</span><span class="atv">"</span><span class="pln"> </span><span class="atn">disabled</span><span class="tag">&gt;</span><span class="pln">Start</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">stopSound</span><span class="pun">()</span><span class="atv">"</span><span class="pln"> </span><span class="atn">disabled</span><span class="tag">&gt;</span><span class="pln">Stop</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">&nbsp; // WebAudio context</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">&nbsp; var</span><span class="pln"> context </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> window</span><span class="pun">.</span><span class="typ">AudioContext</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">&nbsp; var</span><span class="pln"> source </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">&nbsp; var</span><span class="pln"> audioBuffer </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">&nbsp; function</span><span class="pln"> stopSound</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">source</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;source</span><span class="pun">.</span><span class="pln">stop</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">&nbsp; function</span><span class="pln"> playSound</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// Build a source node for the audio graph</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; source </span><span class="pun">=</span><span class="pln"> context</span><span class="pun">.</span><span class="pln">createBufferSource</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; source</span><span class="pun">.</span><span class="pln">buffer </span><span class="pun">=</span><span class="pln"> audioBuffer</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; source</span><span class="pun">.</span><span class="pln">loop </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// connect to the speakers</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; source</span><span class="pun">.</span><span class="pln">connect</span><span class="pun">(</span><span class="pln">context</span><span class="pun">.</span><span class="pln">destination</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; source</span><span class="pun">.</span><span class="pln">start</span><span class="pun">(</span><span class="lit">0</span><span class="pun">);</span><span class="pln"> </span><span class="com">// Play immediately.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">&nbsp; function</span><span class="pln"> initSound</span><span class="pun">(</span><span class="pln">audioFile</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// The audio file may be an mp3 -&nbsp;we must decode it before playing it from memory</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; context</span><span class="pun">.</span><span class="pln">decodeAudioData</span><span class="pun">(</span><span class="pln">audioFile</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">buffer</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Song decoded!"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// audioBuffer the decoded audio file we're going to work with</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; audioBuffer </span><span class="pun">=</span><span class="pln"> buffer</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Enable all buttons once the audio file is</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// decoded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> buttons </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">'button'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; buttons</span><span class="pun">[</span><span class="lit">1</span><span class="pun">].</span><span class="pln">disabled </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span><span class="pln"> </span><span class="com">// play</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; buttons</span><span class="pun">[</span><span class="lit">2</span><span class="pun">].</span><span class="pln">disabled </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span><span class="pln"> </span><span class="com">// stop</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; alert</span><span class="pun">(</span><span class="str">"Binary file has been loaded and decoded, use play / stop buttons!"</span><span class="pun">)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'Error decoding file'</span><span class="pun">,</span><span class="pln"> e</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">});</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; }</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Load a binary file from a URL as an ArrayBuffer.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">&nbsp; function</span><span class="pln"> downloadSoundFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>xhr</strong></span><strong><span class="pun">.</span><span class="pln">responseType </span><span class="pun">=</span><span class="pln"> </span><span class="str">'arraybuffer'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// THIS IS NEW WITH HTML5!</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Song downloaded, decoding..."</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;initSound</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">response</span><span class="pun">);</span><span class="pln"> </span><span class="com">// this.response is an ArrayBuffer.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">};</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">onerror </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"error downloading file"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Ajax request sent... wait until it downloads completely"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; }</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

__Explanations:__

+ _Line 12:_ a click on this button will call the `downloadSoundFile` function, passing it the URL of a sample mp3 file.
+ _Lines 58-73:_ this function sends the Ajax request, and when the file has arrived, the `xhr.onload` callback is called (_line 63_).
+ _Lines 39-55:_ The initSound function decodes the mp3 into memory using the `WebAudio` API, and enables the play and stop buttons.
+ When the play button is enabled and clicked (_line 15_) it calls the `playSound` function. This builds a minimal Web Audio graph with a `BufferSource` node that contains the decoded sound (_lines 31-32_), connects it to the speakers (_line 35_), and then plays it.


#### Monitoring uploads and downloads

__Monitoring uploads or downloads using a `progress` event__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/2TwBOet')"
    src    = "https://bit.ly/3xkcnLY"
    alt    = "downloading progression using a progress element"
    title  = "downloading progression using a progress element"
  />
</figure>


__1 - Declare a `progress` event handler__

XHR2 now provides `progress` event attributes for monitoring data transfers. Previous implementations of XmlHttpRequest didn't tell us anything about how much data has been sent or received. The [ProgressEvent](https://www.w3.org/TR/progress-events/) interface adds 7 events relating to uploading or downloading files.

<table>
  <thead>
    <tr><th style="background-color: #0066ff;">attribute</th><th style="background-color: #0066ff;">type</th><th style="background-color: #0066ff;  ">Explanation</th></tr>
  </thead>
  <tbody>
    <tr><td><code>onloadstart</code></td><td><code title="event-xhr-loadstart">loadstart</code></td><td>When the request starts.</td></tr>
    <tr><td><strong><code>onprogress</code></strong></td><td><strong><code title="event-xhr-progress">progress</code></strong></  td><td><strong>While loading and sending data.</strong></td></tr>
    <tr><td><code>onabort</code></td><td><code title="event-xhr-abort">abort</code></td><td>When the request has been aborted, either by invoking   the&nbsp;<code>abort() </code>method or navigating away from the page.</td></tr>
    <tr><td><code>onerror</code></td><td><code title="event-xhr-error">error</code></td><td>When the request has failed.</td></tr>
    <tr><td><code>onload</code></td><td><code title="event-xhr-load">load</code></td><td>When the request has successfully completed.</td></tr>
    <tr><td><code>ontimeout</code></td><td><code title="event-xhr-timeout">timeout</code></td><td>When the author specified timeout has passed  before the request could complete.</td></tr>
    <tr><td><code>onloadend</code></td><td><code title="event-xhr-loadend">loadend</code></td><td>When the request has completed, regardless of   whether or not it was successful.</td></tr>
  </tbody>
</table><br>

The syntax for declaring progress event handlers is slightly different depending on the type of operation: a download (using the GET HTTP method), or an upload (using POST).


__Syntax for download:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">xhr</span><span class="pun">.</span><span class="pln">onprogress </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="com">// do something</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
</ol></div><br>

Note that an alternative syntax such as `xhr.addEventListener('progress', callback, false)` also works.

__Syntax for upload:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'POST'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">xhr</span><span class="pun">.</span><span class="pln" style="color: #ff0000;">upload</span><span class="pun">.</span><span class="pln">onprogress </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="com">// do something</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
</ol></div><br>

Notice that the only difference is the "upload" added after the name of the request object: with GET we use `xhr.onprogress` and with POST we use <span style="font-family: 'courier new', courier;">xhr.<span style="color: #ff0000;">upload</span>.onprogress</span>.

Note that an alternative syntax such as <span style="font-family: 'courier new', courier;">xhr.<span style="color: #ff0000;">upload</span>.addEventListener('progress', callback, false)</span> also works.

__2 - Get progress values (how many bytes have been downloaded) and the total file size__

The event `e` passed to the `onprogress` callback has two pertinent properties:

1. `loaded` which corresponds to the number of bytes that have been downloaded or uploaded by the browser, so far, and
2. `total` which contains the file's size (in bytes).

Combining these with a `<progress>` element, makes it very easy to render an animated progress bar. Here is a source code extract that does this for a download operation:

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;progress</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"downloadProgress"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">0</span><span class="tag">&gt;&lt;/progress&gt;</span></li>
</ol></div><br>

JavaScript:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// progress element</span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> progress </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#downloadProgress'</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> downloadSoundFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;">&nbsp; ...</li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">onprogress </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>progress</strong></span><strong><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">loaded</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>progress</strong></span><strong><span class="pun">.</span><span class="pln">max </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">total</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
</ol></div><br>

__Explanations:__ by setting the `value` and `max` attributes of the `<progress>` element with the current number of bytes downloaded by the browser and the total size of the file (_lines 10-11_), it will reflect the actual proportions of the file downloaded/still to come.

For example, with a file that is 10,000 bytes long, if the current number of bytes downloaded is 1000, then `<progress value=1000 max=10000>` will look like this: 

And a current download of 2000 bytes will define `<progress value=2000 max=10000>` and will look like this:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/2TwBOet" ismap target="_blank">
    <img style="margin: 0.1em;" height=50
      src   = "https://bit.ly/3xiQ1ds"
      alt   = "progress bar 10%"
      title = "progress bar 10%"
    >
    <img style="margin: 0.1em;" height=50
      src   = "https://bit.ly/3dIH2KX"
      alt   = "progress bar 20%"
      title = "progress bar 20%"
    >
  </a>
</div>


__Complete example: monitoring the download of a song file__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/2TwBOet')"
    src    = "https://bit.ly/3hNZ6or"
    alt    = "monitoring download"
    title  = "monitoring download"
  />
</figure>


 This is a variant of the previous example that uses the `progress` event and a `<progress>` HTML5 element to display an animated progression bar while the download is going on.

[Try it on JSBin](https://jsbin.com/nuxanaf/edit?html,output) - look at the code, which includes the previous source code extract.

[Local Demo](src/03b-example02.html)


#### Notes for 3.2.2 Ajax/XHR2 and binary files

+ Ajax and binary files
  + HTTP: a text based protocol
  + upload/download binary files
    + images, videos, audio and any other binary files
    + encoded to text before transmission
    + decoded on-the-fly upon receipt by the browser or server
  + Ajax: decoded to binary files "by hand" w/ JavaScript code $\to$ not recommended
  + XHR2:
    + supported by all browsers after 2012
    + able to download binary files
    + asking the browser to encode/decode the file to send/receive, natively
    + using `XMLHttpRequest` to send or receive a file
    + set the `xhr.responseType` as `arrayBuffer`

+ Syntax for downloading file
  + task: download sound sample w/ `XMLHttpRequest` level 2
  + load sound file: `function loadSoundFile(url) {...};`
  + create new connection for XHR2<a name="xhr"></a>: `var xhr = new XMLHttpRequest();`
  + open connect w/ get request: `xhr.open('GET', url, true);`
  + set response type<a name="rspType"></a>: `xhr.responseType = 'arrayBuffer';`
  + add event listener for complete downloading<a name="onload"></a>: `xhr.onload = function(e) { initSound(this.response); };`
  + send request to server<a name="send"></a>: `xhr.send();`

+ Example: playing downloaded sound
  + task:
    + click button to download sound file
    + send Ajax request and call `xhr.onload` callback after file arrived
    + decode mp3 into memory and enable start/stop buttons
    + click button to play and stop sound
  + HTML snippet
    + button to trigger download: `<button onclick="downloadSoundFile('http://.../song.mp3');"> Download ant play example sound. </button>`
    + start to play: `<button onclick="playSound()" disabled>Start</button>`
    + stop to play: `<button onclick=""stopSound()" disabled>Stop</button>`
  + JavaScript snippet
    + declare variables for WebAudio: `var context = new window.AudioContext(); var source = url; var audioBuffer = null;`
    + stop playing sound: `function stopSound() { if (source) source.stop(); }`
    + start to play sound: `function starSound() {...}`
      + create a source node and set properties: `source = context.createBufferSource(); source.buffer = audioBuffer; source.loop = false;`
      + connect source to speaker: `source.connect(context.destination);`
      + play sound immediately: `source.start(0);`
    + init sound sample: `function initSound(audioFile) {...}`
      + decode mp3 file: `context.deccodeAudioData(audioFile, function(e) {...} function(e) { console.log('Error decoding file', e); });`
      + log msg: `console.log("Sound decoded!");`
      + set variable: `audioBuffer = buffer;`
      + enable buttons once decoded: `var buttons = document.querySelectorAll('button'); button[1].disabled = false; button[2].disabled = false;`
      + display msg: `alert("Binary file has been loaded and decoded, use play / stop buttons!");`
    + download sound file: `function downloadSoundFile(url) {...}`
      + create [new connection](#xhr) for XHR2
      + open connection: `function loadSoundFile(url) {...}`
      + set response type: `xhr.responseType = 'arraybuffer';`
      + add listener for download: `xhr.onload = function(e) { console.log("Song downloaded, decoding..."); initSound(this.response;); }`
      + add listener for error: `xhr.onerror = function(e) { console.log("error downloading file"); }`
      + [send request](#send)
      + log msg: `console.log("Ajax request sent... wait until it downloads completely!");`

+ Monitoring w/ `progress` event
  + XHR2 providing `progress` event attributes for monitoring data transfers
  + the `ProgressEvent` interface: 7 events related to uploading/downloading files

    <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 50vw;" cellspacing=0 cellpadding=5 border=1 align="center">
      <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://xhr.spec.whatwg.org/#event-handlers">Uploading/Downloading Events in <code>ProgressEvent</code></a></caption>
      <thead>
      <tr style="font-size: 1.2em; vertical-align:middle;">
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Attribute</th>
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Type</th>
        <th scope=row style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Explanation</th>
      </thead>
      <tbody>
        <tr><td><code>onloadstart</code></td><td><code title="event-xhr-loadstart">loadstart</code></td><td>When the request starts.</td></tr>
        <tr><td><strong><code>onprogress</code></strong></td><td><strong><code title="event-xhr-progress">progress</code></strong></  td><td><strong>While loading and sending data.</strong></td></tr>
        <tr><td><code>onabort</code></td><td><code title="event-xhr-abort">abort</code></td><td>When the request has been aborted, either by invoking   the&nbsp;<code>abort() </code>method or navigating away from the page.</td></tr>
        <tr><td><code>onerror</code></td><td><code title="event-xhr-error">error</code></td><td>When the request has failed.</td></tr>
        <tr><td><code>onload</code></td><td><code title="event-xhr-load">load</code></td><td>When the request has successfully completed.</td></tr>
        <tr><td><code>ontimeout</code></td><td><code title="event-xhr-timeout">timeout</code></td><td>When the author specified timeout has passed  before the request could complete.</td></tr>
        <tr><td><code>onloadend</code></td><td><code title="event-xhr-loadend">loadend</code></td><td>When the request has completed, regardless of   whether or not it was successful.</td></tr>
      </tbody>
    </table><br>

+ Syntax for download progress
  + create [new connection](#xhr)
  + open connection w/ get request<a name="get"></a>: `xhr.open('GET', url, true);`
  + ...
  + download progress: `xhr.onprogress = function(e) { // do sth. }`
  + [send request](#send)

+ Syntax for upload progress
  + create [new connection](#xhr)
  + open connection w/ post request<a name="post"></a>: `xhr.open('POST', url, true);`
  + ...
  + upload progress: <code>xhr.<span style="color: #ff0000; font-weight: bold;">upload</span>.onprogress = function(e) { // do sth. }</code>
  + [send request](#send)

+ Progess values and the total file size
  + properties of `progress` event
    + `loaded`: the number if bytes downloaded and uploaded by the browser so far
    + `total`: the file's size (in bytes)
  + combining `<progress>` element to render an animated animated progress bar

+ Example: displaying progress bar
  + tasks:
    + associate the `value` and `max` attributes of the `<progress>` element w/ progress event
    + reflect the actual proportions of the file downloaded
  + HTML snippet: `<progress id="downloadProgress" value=0></progress>`
  + JavaScript snippet
    + access element: `var progress = document.querySelector('#downloadProgress');`
    + download binary file: `function downloadSoundFile(url) {...}`
    + create [new connection](#xhr)
    + open connection w/ [get request](#get)
    + ...
    + add progress event: `xhr.onprogress = function(e) { progress.value = e.loaded; progress.max = e.total; }`
    + [send request](#send)


### 3.2.3 Uploading files and monitoring progress


#### Live coding video: uploading files using Ajax XHR2

<a href="https://edx-video.net/W3CHTM52/W3CHTM52T415-V002400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript Download](https://bit.ly/3hzgooX)


#### Uploading files with `FormData` object

Here is an example that uses a `FormData` object for uploading one or more files to an HTTP server.

Notice that the URL of the server is fake, so the request will fail. However, the simulation takes time, and it is interesting to see how it works.

Later on, we will show full examples of real working code with server-side PHP source, during the “File API, drag and drop and XHR2” lecture.

Try [the example on JSBin](https://jsbin.com/pidusap/edit):

[Local Demo](src/03b-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yjWfdi')"
    src    = "https://bit.ly/3695WPQ"
    alt    = "file upload example 1"
    title  = "file upload example 1"
  />
</figure>


Source code of the example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">File upload with XMLHttpRequest level 2 and HTML5</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h1&gt;</span><span class="pln">Example of XHR2&nbsp;file upload</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; Choose a file and wait a little until it is uploaded (on a fake &nbsp; </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; server). A message should pop up once the file is uploaded 100%.</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/p&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> fileInput </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#file'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> fileInput</span><span class="pun">.</span><span class="pln">onchange </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'POST'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'upload.html'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// With FormData, </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // POST is mandatory</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>xhr</strong></span><strong><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>alert</strong></span><strong><span class="pun">(</span><span class="str">'Upload complete !'</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;<strong>};</strong></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">var</span><span class="pln"> form </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FormData</span><span class="pun">();</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>form</strong></span><strong><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">'file'</span><span class="pun">,</span><span class="pln"> fileInput</span><span class="pun">.</span><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// send the request</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">(</span><span class="pln">form</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

__Explanations:__

+ _Line 18_: callback called when the user selects a file.
+ _Lines 19-20_: preparation of the XHR2 request.
+ _Lines 27-30_: a `FormData` object is created (this will contain the (MIME) multipart form-data which will be sent by the `POST` request).
+ _Line 30_: the request is sent, with the `FormData` object passed as a parameter (all data is sent).
+ _Line 23_: when the file is completely uploaded, the `onload` listener is called and an alert message is displayed.


#### Monitor the upload progress

Here is a more user-friendly example. It is basically the same, but this time, we'll monitor the progress of the upload using a method similar to that used for monitoring file downloads:

+ We use a `<progress>` element and its two attributes `value` and `max`.
+ We also bind an event handler to the `progress` event that an `XMLHttpRequest` will trigger. The event has two properties: `loaded` and `total` that respectively correspond to the number of bytes that have been uploaded, and to the total number of bytes we need to upload (i.e., the file size).

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3yjWfdi')"
    src    = "https://bit.ly/2SQACCq"
    alt    = "file upload with progress bar"
    title  = "file upload with progress bar"
  />
</figure>


Here is the code of such an event listener:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">xhr</span><span class="pun">.</span><span class="pln" style="color: #ff0000;">upload</span><span class="pun">.</span><span class="pln">onprogress </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; progress.value =&nbsp;e</span><span class="pun">.</span><span class="pln">loaded<span style="color: #666600;" color="#666600">; //</span></span><span class="com">&nbsp;number of bytes uploaded</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; progress.max = e</span><span class="pun">.</span><span class="pln">total</span><span class="pun">;<span style="color: #000000;" color="#000000">&nbsp; &nbsp; //</span></span><span class="com">&nbsp;total number of bytes in the file</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>

Try [the example on JSBin](https://jsbin.com/qedaja/edit?html,output):

[Local Demo](src/03b-example04.html)

Code from this example (nearly the same as previous example's code):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">HTML5 file upload with monitoring</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h1&gt;</span><span class="pln">Example of XHR2 file upload, with progress bar</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">Choose a file and wait a little until it is uploaded (on a fake server).</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;br/&gt;&lt;br</span><span class="tag">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;progress</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"progress" value=0</span><span class="tag">&gt;&lt;/progress&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> fileInput </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#file'</span><span class="pun">),</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>progress </strong></span><strong><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#progress'</span><span class="pun">);</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;fileInput</span><span class="pun">.</span><span class="pln">onchange </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'POST'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'upload.html'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>xhr</strong></span><strong><span class="pun">.</span><span class="pln">upload</span><span class="pun">.</span><span class="pln">onprogress </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong>progress</strong></span><strong><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">loaded</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;<strong>progress</strong></span><strong><span class="pun">.</span><span class="pln">max </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">total</span><span class="pun">;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="pun">};</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;alert</span><span class="pun">(</span><span class="str">'Upload complete!'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> form </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FormData</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;form</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">'file'</span><span class="pun">,</span><span class="pln"> fileInput</span><span class="pun">.</span><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">(</span><span class="pln">form</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>

The only difference between these two worked-examples is the `onprogress` listener which updates the progress bar's `value` and `max` attributes.


#### Notes for 3.2.3 Uploading files and monitoring progress

+ Syntax for uploading file w/ progress bar
  + add listener for upload progress<a name="uploadProgress>: `xhr.upload.onprogress = function(e) {...};`
  + number of bytes uploaded: `progress.value = e.loaded;`
  + total number of bytes in the file: `progress.max = e.total;`

+ Example: uploading a selecting file
  + tasks:
    + callback on selecting a file
    + create `FormData` object
    + prepare XHR2 request and send w/ `FormData` object
  + HTML snippet: `<input id="file" type="file" />`
  + JavaScript snippet:
    + access input element: `var fileInput = document.querySelector('#file');`
    + add listener for change: `fileInput.onchange = function() {...}`
    + create [new connection](#xhr)
    + open connection w/ post request and FormData: `xhr.open('POST', 'upload.html');`
    + alert msg after uploaded<a name="upComplete"></a>: `xhr.onload = function() { alert('Upload complete!'); }`
    + create new data form and store file within<a name="form"></a>: `var form = new FormData(); form.append('file', fileInput.files[0]);`
    + send request w/ form<a name="sendForm"></a>: `xhr.send(form);`

+ Example: uploading file w/ progress bar
  + task: add progress bar for the previous example
  + HTML snippet:
    + input fields: `<input id="file" type="file" />`
    + progress bar: `<progress id="progress" value=0></progress>`
  + JavaScript snippet
    + access input field and progree bar: `var fileInput = document.querySelector("#file"); progress = document.querySelector("#progree");`
    + add input change listener: `fileInput.onchange = function() {...}`
    + create [XHR2 request](#xhr)
    + open connection: `xhr.open('POST', 'upload.html');`
    + add listener for [upload progress](#uploadProgress)
    + [alert msg after uploaded](#upComplete)
    + create [new object and store file](#form)
    + send [request w/ form](#sendForm)






