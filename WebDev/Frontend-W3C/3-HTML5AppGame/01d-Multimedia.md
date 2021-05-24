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

Below is the sound file. You can try to play it:

<p class="exampleHTML"><audio src="https://mainline.i3s.unice.fr/mooc/animalSounds.mp3" controls="controls" gt="" audio=""></audio></p>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
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


To add a TextTrack to a track element, use the [`addTextTrack` method](https://www.w3.org/TR/html5/embedded-content-0.html#text-track-api) (of the audio or video element). The function's signature is `addTextTrack(kind[,label[,language]])` where kind is our familiar choice between `subtitles`, `captions`, `chapters`, etc. The optional label is any text you'd like to use describing the track; and the optional language is from our usual list of BCP-47 abbreviations, eg 'de', 'en', 'es', 'fr' (etc).

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







### 1.4.2 Update the document in sync with a media playing






### 1.4.3 Discussion and projects








