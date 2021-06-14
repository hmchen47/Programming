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

<p class="exampleHTML"><audio src="https://mainline.i3s.unice.fr/mooc/animalSounds.mp3" controls="controls" gt="" audio=""></audio></p>

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

<div class="source-code" style="line-height: 22.4px; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif;"><ol class="linenums" style="margin-top: 1em; margin-bottom: 1em; margin-left: 0px; line-height: 1.4em;">
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;" value="1"><span class="pln" >&nbsp;</span><span class="kwd" >var</span><span class="pln" >&nbsp;sounds&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="pun" >[</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;" value="1"><span class="pun" >&nbsp; &nbsp; {</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;id</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="str" >"purr"</span><span class="pun" >,</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;startTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >0.200</span><span class="pun" >,</span></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;endTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >1.800</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;&nbsp;</span><span class="pun" >},</span><span class="pln" ></span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; {</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;id</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="str" >"meow"</span><span class="pun" >,</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;startTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >2.300</span><span class="pun" >,</span></li>
<li class="L7" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;endTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >3.300</span></li>
<li class="L8" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;&nbsp;</span><span class="pun" >},</span><span class="pln" ></span></li>
<li class="L8" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; {</span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;id</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="str" >"bark"</span><span class="pun" >,</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;startTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >3.900</span><span class="pun" >,</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;endTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >4.300</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;&nbsp;</span><span class="pun" >},</span><span class="pln" ></span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; {</span></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;id</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="str" >"baa"</span><span class="pun" >,</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;startTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >5.000</span><span class="pun" >,</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp;endTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >5.800</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;&nbsp;</span><span class="pun" >}</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; ...</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" ></span>];</li>
</ol></div><br>

The idea is to create a track on the fly, then add cues within this track. Each cue will be created with the id, the start and end time taken from the above JavaScript object. In the end, we will have a track with individual cues located at the time location where an animal sound is in the mp3 file.

Then we generate buttons in the HTML document, and when the user clicks on a button, the `getCueById` method is called, then the start and end time properties of the cue are accessed and the sound is played (using the `currentTime` property of the audio element).

__Polyfill for `getCueById`__: Note that this method is not available on all browsers yet. A simple polyfill is used in the examples presented. If the `getCueById` method is not implemented (this is the case in some browsers), it's easy to use this small polyfill:


<div class="source-code" style="line-height: 25.6px;"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">&nbsp;// for browsers that do not implement the getCueById() method</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;//&nbsp;let's assume we're adding the getCueById function to a TextTrack object</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;//named "track"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">if</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="kwd">typeof</span><span class="pln">&nbsp;track</span><span class="pun">.</span><span class="pln">getCueById&nbsp;</span><span class="pun">!==</span><span class="pln">&nbsp;</span><span class="str">"function"</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;track</span><span class="pun">.</span><span class="pln">getCueById&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">id</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln">&nbsp;cues&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;track</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="kwd">var</span><span class="pln">&nbsp;i&nbsp;</span><span class="pun">=</span><span class="pln">&nbsp;</span><span class="lit">0</span><span class="pun">;</span><span class="pln">&nbsp;i&nbsp;</span><span class="pun">!=</span><span class="pln">&nbsp;track</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln">&nbsp;</span><span class="pun">++</span><span class="pln">i</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln">&nbsp;</span><span class="pun">(</span><span class="pln">cues</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">id&nbsp;</span><span class="pun">===</span><span class="pln">&nbsp;id</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln">&nbsp;cues</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp;}</span></li>
</ol></div><br>


#### Techniques


To add a `TextTrack` to a track element, use the [`addTextTrack` method](https://www.w3.org/TR/html5/embedded-content-0.html#text-track-api) (of the audio or video element). The function's signature is `addTextTrack(kind[,label[,language]])` where kind is our familiar choice between `subtitles`, `captions`, `chapters`, etc. The optional label is any text you'd like to use describing the track; and the optional language is from our usual list of BCP-47 abbreviations, eg 'de', 'en', 'es', 'fr' (etc).

The VTTCue constructor enables us to create our own cue class-instances programmatically. We create a cue instance by using the new keyword. The constructor function expects three familiar arguments, thus: new `VTTCue(startTime, endTime, id)` - more detail is available from [the MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Video_Text_Tracks_Format) and [the W3C's two applicable groups](https://w3c.github.io/webvtt/#the-vttcue-interface).

To add cue-instances to a TextTrack on-the-fly, use the `track` object's `addCue` method, eg `track.addCue(cue)`. The argument is a _cue instance_ - as above. Note that the track __must__ be a `TextTrack` object because `addCue` does not work with `HTMLTrackElement` Objects.

HTML source code extract:

<div class="source-code" style="line-height: 22.4px; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif;"><ol class="linenums" style="margin-top: 1em; margin-bottom: 1em; margin-left: 0px; line-height: 1.4em;">
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;" value="1"><span class="pun" >...</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="str" >&lt;h1&gt;</span><span class="typ" >Playing</span><span class="pln" >&nbsp;audio sprites&nbsp;</span><span class="kwd" >with</span><span class="pln" >&nbsp;the track element</span><span class="pun" >&lt;/</span><span class="pln" >h1</span><span class="pun" >&gt;</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span><span class="str" >&lt;p&gt;</span><span class="pln" >A demo&nbsp;</span><span class="kwd" >by</span><span class="pln" >&nbsp;</span><span class="typ" >Sam</span><span class="pln" >&nbsp;</span><span class="typ" >Dutton</span><span class="pun" >,</span><span class="pln" >&nbsp;adapted&nbsp;</span><span class="kwd" >for</span><span class="pln" >&nbsp;</span><span class="typ" >JsBin</span><span class="pln" >&nbsp;</span><span class="kwd" >by</span><span class="pln" >&nbsp;M</span><span class="pun" >.</span><span class="typ" >Buffa</span><span class="pun" >&lt;/</span><span class="pln" >p</span><span class="pun" >&gt;</span></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&lt;</span><span class="pln" >div id</span><span class="pun" >=</span><span class="str" >"soundButtons"</span><span class="pln" >&nbsp;</span><span class="kwd" >class</span><span class="pun" >=</span><span class="str" >"isSupported"</span><span class="pun" >&gt;&lt;/</span><span class="pln" >div</span><span class="pun" >&gt;</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >...</span></li>
</ol></div><br>

<div class="source-code" style="line-height: 22.4px; font-family: 'Open Sans', Verdana, Geneva, sans-serif, sans-serif;"><ol class="linenums" style="margin-top: 1em; margin-bottom: 1em; margin-left: 0px; line-height: 1.4em;">
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;" value="1">&nbsp;<span class="pln" >window</span><span class="pun" >.</span><span class="pln" >onload&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="kwd" >function</span><span class="pun" >()</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; // Create an audio element programmatically</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;&nbsp;</span><span class="kwd" >var</span><span class="pln" >&nbsp;audio&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="kwd" >new</span><span class="pln" ></span><span class="typ" >Audio</span><span class="pun" >(</span><span class="str" >"https://mainline.i3s.unice.fr/mooc/animalSounds.mp3"</span><span class="pun" >);</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; audio</span><span class="pun" >.</span><span class="pln" >addEventListener</span><span class="pun" >(</span><span class="str" >"loadedmetadata"</span><span class="pun" >,</span><span class="pln" >&nbsp;</span><span class="kwd" >function</span><span class="pun" >()</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">// When the audio file has its metadata loaded, we can add </strong></span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" ><strong style="line-height: 1.4em;">&nbsp; &nbsp; &nbsp; // a new track to it, with mode = hidden. It will fire events</strong></span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><strong style="line-height: 1.4em;"><span class="pun" >&nbsp; &nbsp; &nbsp; // even if it is hidden</span></strong></li>
<li class="L7" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><strong style="line-height: 1.4em;"><span class="kwd" >var</span><span class="pln" >&nbsp;track&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;audio</span><span class="pun" >.</span><span class="pln" >addTextTrack</span><span class="pun" >(</span><span class="str" >"metadata"</span><span class="pun" >,</span><span class="pln" >&nbsp;</span><span class="str" >"sprite track"</span><span class="pun" >,</span><span class="pln" >&nbsp;</span><span class="str" >"en"</span><span class="pun" >);</span></strong></li>
<li class="L8" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">track</strong></span><strong style="line-height: 1.4em;"><span class="pun" >.</span><span class="pln" >mode&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="str" >"hidden"</span><span class="pun" >;</span></strong></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com" >// for browsers that do not implement the getCueById() method</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" >if</span><span class="pln" >&nbsp;</span><span class="pun" >(</span><span class="kwd" >typeof</span><span class="pln" >&nbsp;track</span><span class="pun" >.</span><span class="pln" >getCueById&nbsp;</span><span class="pun" >!==</span><span class="pln" >&nbsp;</span><span class="str" >"function"</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;track</span><span class="pun" >.</span><span class="pln" >getCueById&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="kwd" >function</span><span class="pun" >(</span><span class="pln" >id</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" >var</span><span class="pln" >&nbsp;cues&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;track</span><span class="pun" >.</span><span class="pln" >cues</span><span class="pun" >;</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" >for</span><span class="pln" >&nbsp;</span><span class="pun" >(</span><span class="kwd" >var</span><span class="pln" >&nbsp;i&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="lit" >0</span><span class="pun" >;</span><span class="pln" >&nbsp;i&nbsp;</span><span class="pun" >!=</span><span class="pln" >&nbsp;track</span><span class="pun" >.</span><span class="pln" >cues</span><span class="pun" >.</span><span class="pln" >length</span><span class="pun" >;</span><span class="pln" >&nbsp;</span><span class="pun" >++</span><span class="pln" >i</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd" >if</span><span class="pln" >&nbsp;</span><span class="pun" >(</span><span class="pln" >cues</span><span class="pun" >[</span><span class="pln" >i</span><span class="pun" >].</span><span class="pln" >id&nbsp;</span><span class="pun" >===</span><span class="pln" >&nbsp;id</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd" >return</span><span class="pln" >&nbsp;cues</span><span class="pun" >[</span><span class="pln" >i</span><span class="pun" >];</span></li>
<li class="L7" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun" >}</span></li>
<li class="L8" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun" >}</span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun" >};</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp;}</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="kwd" >&nbsp; &nbsp;var</span><span class="pln" >&nbsp;sounds&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="pun" >[</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; {</span></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; id</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="str" >"purr"</span><span class="pun" >,</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; startTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >0.200</span><span class="pun" >,</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; endTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >1.800</span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun" >},</span><span class="pln" ></span></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; {</span></li>
<li class="L7" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; id</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="str" >"meow"</span><span class="pun" >,</span></li>
<li class="L8" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; startTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >2.300</span><span class="pun" >,</span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; endTime</span><span class="pun" >:</span><span class="pln" >&nbsp;</span><span class="lit" >3.300</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun" >},</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; ...</li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;">&nbsp; &nbsp;];</li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="kwd" >&nbsp; &nbsp;for</span><span class="pln" >&nbsp;</span><span class="pun" >(</span><span class="kwd" >var</span><span class="pln" >&nbsp;i&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="lit" >0</span><span class="pun" >;</span><span class="pln" >&nbsp;i&nbsp;</span><span class="pun" >!==</span><span class="pln" >&nbsp;sounds</span><span class="pun" >.</span><span class="pln" >length</span><span class="pun" >;</span><span class="pln" >&nbsp;</span><span class="pun" >++</span><span class="pln" >i</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; // for each animal sound, create a cue with id, start&nbsp;and end time</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" >var</span><span class="pln" >&nbsp;sound&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;sounds</span><span class="pun" >[</span><span class="pln" >i</span><span class="pun" >];</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><strong style="line-height: 1.4em;"><span class="kwd" >var</span><span class="pln" >&nbsp;cue&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;</span><span class="kwd" >new</span><span class="pln" >&nbsp;</span><span class="typ" >VTTCue</span><span class="pun" >(</span><span class="pln" >sound</span><span class="pun" >.</span><span class="pln" >startTime</span><span class="pun" >,</span><span class="pln" >&nbsp;sound</span><span class="pun" >.</span><span class="pln" >endTime</span><span class="pun" >,</span><span class="pln" >&nbsp;sound</span><span class="pun" >.</span><span class="pln" >id</span><span class="pun" >);</span><span class="pln" >&nbsp;</span></strong></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">cue</strong></span><strong style="line-height: 1.4em;"><span class="pun" >.</span><span class="pln" >id&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;sound</span><span class="pun" >.</span><span class="pln" >id</span><span class="pun" >;</span></strong></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">// add it to the track</strong></span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;<strong style="line-height: 1.4em;">track</strong></span><strong style="line-height: 1.4em;"><span class="pun" >.</span><span class="pln" >addCue</span><span class="pun" >(</span><span class="pln" >cue</span><span class="pun" >);</span></strong></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; // create a button and add it to the HTML document</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; document</span><span class="pun" >.</span><span class="pln" >querySelector</span><span class="pun" >(</span><span class="str" >"#soundButtons"</span><span class="pun" >).</span><span class="pln" >innerHTML&nbsp;</span><span class="pun" >+=</span><span class="pln" >&nbsp;</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="str" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"&lt;button class='playSound' id="</span><span class="pln" >&nbsp;</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+&nbsp;</span><span class="pln" >sound</span><span class="pun" >.</span><span class="pln" >id&nbsp;</span><span class="pun" >+</span><span class="pln" >&nbsp;</span><span class="str" >"&gt;"</span><span class="pln" >&nbsp;</span><span class="pun" >+</span><span class="pln" >sound</span><span class="pun" >.</span><span class="pln" >id&nbsp;</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln" >&nbsp;</span><span class="str" >"&lt;/button&gt;"</span><span class="pun" >;<br><span class="pln" >&nbsp; &nbsp;</span><span class="pun" >}</span><br></span></li>
<li class="L7" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span></li>
<li class="L8" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;</span><span class="kwd" >var</span><span class="pln" >&nbsp;endTime</span><span class="pun" >;</span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;audio</span><span class="pun" >.</span><span class="pln" >addEventListener</span><span class="pun" >(</span><span class="str" >"timeupdate"</span><span class="pun" >,</span><span class="pln" >&nbsp;</span><span class="kwd" >function</span><span class="pun" >(</span><span class="kwd" >event</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; // When we play a sound, we set the endtime var. </span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; // We need to listen when the audio file is being played,&nbsp;</span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp; //&nbsp;in order to pause it when endTime is reached.</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd" >if</span><span class="pln" >&nbsp;</span><span class="pun" >(</span><span class="kwd" >event</span><span class="pun" >.</span><span class="pln" >target</span><span class="pun" >.</span><span class="pln" >currentTime&nbsp;</span><span class="pun" >&gt;</span><span class="pln" >&nbsp;endTime</span><span class="pun" >)</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd" >event</span><span class="pun" >.</span><span class="pln" >target</span><span class="pun" >.</span><span class="pln" >pause</span><span class="pun" >();</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;</span><span class="pun" >});</span></li>
<li class="L3" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp;</span><span class="kwd" >function</span><span class="pln" >&nbsp;playSound</span><span class="pun" >(</span><span class="pln" >id</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp;// Plays the sound corresponding to the cue with id equal </span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp;// to the one passed as a parameter. We set the endTime var</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp;// and position the audio currentTime at the start time </span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >&nbsp; &nbsp; &nbsp;// of the sound</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;</span><strong style="line-height: 1.4em;"><span class="kwd" >var</span><span class="pln" >&nbsp;cue&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;track</span><span class="pun" >.</span><span class="pln" >getCueById</span><span class="pun" >(</span><span class="pln" >id</span><span class="pun" >);</span></strong></li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;audio</span><span class="pun" >.</span><span class="pln" >currentTime&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;cue</span><span class="pun" >.</span><span class="pln" >startTime</span><span class="pun" >;</span></li>
<li class="L7" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;endTime&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;cue</span><span class="pun" >.</span><span class="pln" >endTime</span><span class="pun" >;</span></li>
<li class="L8" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;audio</span><span class="pun" >.</span><span class="pln" >play</span><span class="pun" >();</span></li>
<li class="L9" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;&nbsp;</span><span class="pun" >};</span></li>
<li class="L0" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; // create listeners for all buttons</span></li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; </span><span class="kwd" >var</span><span class="pln" >&nbsp;buttons&nbsp;</span><span class="pun" >=</span><span class="pln" >&nbsp;document</span><span class="pun" >.</span><span class="pln" >querySelectorAll</span><span class="pun" >(</span><span class="str" >"button.playSound"</span><span class="pun" >);<br><br></span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; for(var i=; i &lt; buttons.length; i++) { &nbsp; &nbsp;</span></li>
<li class="L4" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp;buttons</span><span class="pun" >[</span><span class="pln" >i</span><span class="pun" >].</span><span class="pln" >addEventListener</span><span class="pun" >(</span><span class="str" >"click"</span><span class="pun" >,</span><span class="pln" >&nbsp;</span><span class="kwd" >function</span><span class="pun" >(</span><span class="pln" >e</span><span class="pun" >)</span><span class="pln" >&nbsp;</span><span class="pun" >{</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp; &nbsp; &nbsp; &nbsp; playSound</span><span class="pun" >(</span><span class="kwd" >this</span><span class="pun" >.</span><span class="pln" >id</span><span class="pun" >);</span></li>
<li class="L5" style="line-height: 1.4em; margin-bottom: 0px;">&nbsp; &nbsp; &nbsp;});</li>
<li class="L6" style="line-height: 1.4em; margin-bottom: 0px;">&nbsp; }</li>
<li class="L1" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pln" >&nbsp;</span><span class="pun" >});</span></li>
<li class="L2" style="line-height: 1.4em; margin-bottom: 0px;"><span class="pun" >};</span></li>
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
  + HTML snippet: `<div id="soundButtons" class="isSupported"></div>`
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">textTrack</span><span class="pun">.</span><span class="pln">oncuechange </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// "this" is the textTrack that fired the event.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // Let's get the first active cue for this time segment</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">activeCues</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> obj </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">parse</span><span class="pun">(</span><span class="pln">cue</span><span class="pun">.</span><span class="pln">text</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// do something</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

Here is a very impressive demo by Sam Dutton that uses JSON cues containing the latitude and longitude of the camera used for filming the video, to synchronize two map views: every time the active cue changes, the Google map and equivalent Google street view are updated. 

<p class="exampleHTML">WARNING: as this Google service is no longer free of charge, you might see "for development purpose only" messages during the execution of this demo. You'll need a valid Google API key in order to remove these messages.</p>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3vetGwK")"
    src    = "https://bit.ly/3yA1INX"
    alt    = "Video synced with google map and google street map"
    title  = "Video synced with google map and google street map"
  />
</figure>


Example of a cue content from this demonstration:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">{</span><span class="str">"lat"</span><span class="pun">:</span><span class="lit">37.4219276</span><span class="pun">,</span><span class="pln"> </span><span class="str">"lng"</span><span class="pun">:-</span><span class="lit">122.088218</span><span class="pun">,</span><span class="pln"> </span><span class="str">"t"</span><span class="pun">:</span><span class="lit">1331363000</span><span class="pun">}</span></li>
</ol></div><br>

Cue events and cue content:

We can acquire a cue DOM object using the techniques we have seen previously, or by using the new HTML5 TextTrack `getCueById()` method. 

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> videoElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myvideo"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> textTracks </span><span class="pun">=</span><span class="pln"> videoElement</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">;</span><span class="pln"> </span><span class="com">// one for each track element</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> textTrack </span><span class="pun">=</span><span class="pln"> textTracks</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span><span class="pln"> </span><span class="com">// corresponds to the first track element</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><strong>// Get a cue with ID="wikipedia"</strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> textTrack</span><span class="pun">.</span><span class="pln">getCueById</span><span class="pun">(</span><span class="str">"Wikipedia"</span><span class="pun">);</span><span class="pln">&nbsp;</span></strong></li>
</ol></div><br>

And once we have a cue object, it is possible to add event listeners to it:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">cue</span><span class="pun">.</span><span class="pln">onenter </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// display something, play a sound, update any DOM element...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">cue</span><span class="pun">.</span><span class="pln">onexit </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// do something else</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
</ol></div><br>

If the `getCueById` method is not implemented (this is the case in some browsers), we use the @@polyfill presented in the previous section:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">&nbsp;// for browsers that do not implement the getCueById() method</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;//&nbsp;let's assume we're adding the getCueById function to a TextTrack object </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;//named "track"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">typeof</span><span class="pln"> track</span><span class="pun">.</span><span class="pln">getCueById </span><span class="pun">!==</span><span class="pln"> </span><span class="str">"function"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;track</span><span class="pun">.</span><span class="pln">getCueById </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">id</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cues </span><span class="pun">=</span><span class="pln"> track</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">!=</span><span class="pln"> track</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> </span><span class="pun">++</span><span class="pln">i</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">cues</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">id </span><span class="pun">===</span><span class="pln"> id</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> cues</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp;}</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example syncing element of the document with video metadata in webVTT file</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;main&gt;</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;</span><span class="tag">&lt;/source&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"urls track"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"https://...../SamuraiPizzaCat-metadata.vtt"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/track&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>&nbsp;</strong></span><strong><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"map"</span><span class="tag">&gt;&lt;/div&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/main&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;aside&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="tag">&lt;iframe</span><span class="pln"> </span><span class="atn">sandbox</span><span class="pun">=</span><span class="atv">"allow-same-origin"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myIframe"</span><span class="pln"> </span><span class="tag">&gt;</span><span class="pln"> </span><span class="tag">&lt;/iframe&gt;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/aside&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h3&gt;</span><span class="pln">Wikipedia URL: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"currentURL"</span><span class="tag">&gt;</span><span class="pln"> Non défini </span><span class="tag">&lt;/span&gt;&lt;/h3&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://maps.google.com/maps/api/js?sensor=false"</span><span class="tag">&gt;&lt;/script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">...</span></li>
</ol></div><br>

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> videoElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> myIFrame </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pun"><span style="line-height: 25.6px;">querySelector</span>("</span><span class="str">#myIframe"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;">&nbsp; &nbsp; var currentURLSpan =&nbsp;<span class="pln">document</span><span class="pun">.</span><span class="pun"><span style="line-height: 25.6px;"><mark style="background-color: pink;">querySelector</mask></span>(</span><span class="str">"#currentURL"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> textTracks </span><span class="pun">=</span><span class="pln"> videoElement</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">;</span><span class="pln"> </span><span class="com">// one for each track element</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> textTrack </span><span class="pun">=</span><span class="pln"> textTracks</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span><span class="pln"> </span><span class="com">// corresponds to the first track element</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">&nbsp;</span><span class="pln">&nbsp;</span>&nbsp;</li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // change mode so we can use the track</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pln">textTrack</span><span class="pun">.</span><span class="pln">mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">"hidden"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span><span class="pln">&nbsp; &nbsp;</span><span class="com">// Default position on the google map</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> centerpos </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">LatLng</span><span class="pun">(</span><span class="lit">48.579400</span><span class="pun">,</span><span class="lit">7.7519</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // default options for the google map</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> optionsGmaps </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;center</span><span class="pun">:</span><span class="pln">centerpos</span><span class="pun">,</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;navigationControlOptions</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln">style</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">NavigationControlStyle</span><span class="pun">.</span><span class="pln">SMALL</span><span class="pun">},</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;mapTypeId</span><span class="pun">:</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">MapTypeId</span><span class="pun">.</span><span class="pln">ROADMAP</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;zoom</span><span class="pun">:</span><span class="pln"> </span><span class="lit">15</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; };</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; // Init map object</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> map </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">Map</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"map"</span><span class="pun">),</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; optionsGmaps</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // cue change listener, this is where the synchronization between</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // the HTML document and the video is done</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; textTrack</span><span class="pun">.</span><span class="pln">oncuechange </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(){</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp;// we assume that we have no overlapping cues</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">activeCues</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">cue </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">return</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;// get cue content as a JavaScript object</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cueContentJSON </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">parse</span><span class="pun">(</span><span class="pln">cue</span><span class="pun">.</span><span class="pln">text</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;// do different things depending on the type of sync (wikipedia, gmap)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">switch</span><span class="pun">(</span><span class="pln">cueContentJSON</span><span class="pun">.</span><span class="pln">type</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="str">'WikipediaPage'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> myURL </span><span class="pun">=</span><span class="pln"> cueContentJSON</span><span class="pun">.</span><span class="pln">url</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> myLink </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;a href=\""</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> myURL </span><span class="pun">+</span><span class="pln"> </span><span class="str">"\"&gt;"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> myURL </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/a&gt;"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun"><span style="color: #3c3c3c; line-height: 25.6px;"><mark style="background-color: pink;">currentURLSpan</mark></span>.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> myLink</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myIFrame</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> myURL</span><span class="pun">;</span><span class="pln"> </span><span class="com">// assign url to src property</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">case</span><span class="pln"> </span><span class="str">'LongLat'</span><span class="pun">:</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; drawPosition</span><span class="pun">(</span><span class="pln">cueContentJSON</span><span class="pun">.</span><span class="kwd">long</span><span class="pun">,</span><span class="pln"> cueContentJSON</span><span class="pun">.</span><span class="pln">lat</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">function</span><span class="pln"> drawPosition</span><span class="pun">(</span><span class="kwd">long</span><span class="pun">,</span><span class="pln"> lat</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Make new object LatLng for Google Maps</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> latlng </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">LatLng</span><span class="pun">(</span><span class="pln">lat</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">long</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// Add a marker at position</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> marker </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> google</span><span class="pun">.</span><span class="pln">maps</span><span class="pun">.</span><span class="typ">Marker</span><span class="pun">({</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; position</span><span class="pun">:</span><span class="pln"> latlng</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; map</span><span class="pun">:</span><span class="pln"> map</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; title</span><span class="pun">:</span><span class="str">"You are here"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">});</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// center map on longitude and latitude</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; map</span><span class="pun">.</span><span class="pln">panTo</span><span class="pun">(</span><span class="pln">latlng</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">};</span></li>
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




