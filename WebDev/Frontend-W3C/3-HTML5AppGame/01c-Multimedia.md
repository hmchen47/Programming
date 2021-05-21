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
    onclick= "window.open("https://bit.ly/2QzbheZ")"
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
    onclick= "window.open("https://bit.ly/2QzbheZ")"
    src    = "https://bit.ly/33Wezw5"
    alt    = "video player with clickable transcript"
    title  = "video player with clickable transcript"
  />
</figure>


HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">&lt;section id="all"&gt;</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">disabled</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttonEnglish"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">loadTranscript</span><span class="pun">(</span><span class="str">'en'</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Display English transcript</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/button&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">disabled</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttonDeutsch"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">loadTranscript</span><span class="pun">(</span><span class="str">'de'</span><span class="pun">);</span></strong><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Display Deutsch transcript</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://...../elephants-dream-medium.mp4"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"de"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>default</strong></span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"transcript"</span><span class="tag">&gt;&lt;/div&gt;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;">&lt;/section&gt;</li>
</ol></div><br>

CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">#all {</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightgrey</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">-</span><span class="pln">radius</span><span class="pun">:</span><span class="lit">10px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;padding</span><span class="pun">:</span><span class="pln"> </span><span class="lit">20px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;display</span><span class="pun">:</span><span class="kwd">inline</span><span class="pun">-</span><span class="pln">block</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;margin</span><span class="pun">:</span><span class="lit">30px</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;width</span><span class="pun">:</span><span class="lit">90</span><span class="pun">%;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">.</span><span class="pln">cues </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln">blue</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">.</span><span class="pln">cues</span><span class="pun">:</span><span class="pln">hover </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;text</span><span class="pun">-</span><span class="pln">decoration</span><span class="pun">:</span><span class="pln"> underline</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">.</span><span class="pln">cues</span><span class="pun">.</span><span class="pln">current </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln">black</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;font</span><span class="pun">-</span><span class="pln">weight</span><span class="pun">:</span><span class="pln"> bold</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">#myVideo {</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;display</span><span class="pun">:</span><span class="pln"> block</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">float</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> left</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;margin</span><span class="pun">-</span><span class="pln">right</span><span class="pun">:</span><span class="pln">&nbsp;<span style="color: #006666;" color="#006666">3</span></span><span class="pun">%;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">66</span><span class="pun">%;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> black</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;position</span><span class="pun">:</span><span class="pln"> relative</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">#transcript {</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;padding</span><span class="pun">:</span><span class="pln"> </span><span class="lit">10px</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">float</span><span class="pun">:</span><span class="pln"> left</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;max</span><span class="pun">-</span><span class="pln">height</span><span class="pun">:</span><span class="pln"> </span><span class="lit">225px</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;overflow</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">auto</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">25</span><span class="pun">%;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;margin</span><span class="pun">:</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;font</span><span class="pun">-</span><span class="pln">size</span><span class="pun">:</span><span class="pln"> </span><span class="lit">14px</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;list</span><span class="pun">-</span><span class="pln">style</span><span class="pun">:</span><span class="pln"> none</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> video</span><span class="pun">,</span><span class="pln"> transcriptDiv</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">// TextTracks, html tracks, urls of tracks</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> tracks</span><span class="pun">,</span><span class="pln"> trackElems</span><span class="pun">,</span><span class="pln"> tracksURLs </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> buttonEnglish</span><span class="pun">,</span><span class="pln"> buttonDeutsch</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"init"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// when the page is loaded, get the different DOM nodes</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// we're going to work with</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp;video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transcriptDiv </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#transcript"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// The tracks as HTML elements</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;trackElems </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"track"</span><span class="pun">);<br></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Get the URLs of the vtt files</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> trackElems</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> currentTrackElem </span><span class="pun">=</span><span class="pln"> trackElems</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; tracksURLs</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> currentTrackElem</span><span class="pun">.</span><span class="pln">src</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;buttonEnglish </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#buttonEnglish"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;buttonDeutsch </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#buttonDeutsch"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// we enable the buttons&nbsp;only in this load callback, </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp;// we cannot click before the video is in the DOM</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;buttonEnglish</span><span class="pun">.</span><span class="pln">disabled </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;buttonDeutsch</span><span class="pun">.</span><span class="pln">disabled </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// The tracks as TextTrack JS objects</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;tracks </span><span class="pun">=</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadTranscript</span><span class="pun">(</span><span class="pln">lang</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; // Called when a button is clicked</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// clear current transcript</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; clearTranscriptDiv</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// set all track modes to disabled. We will only activate the</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// one whose content will be displayed as transcript</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; disableAllTracks</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Locate the track with language = lang</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> tracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="com">// current track</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> track </span><span class="pun">=</span><span class="pln"> tracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> trackAsHtmlElem </span><span class="pun">=</span><span class="pln"> trackElems</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; // Only subtitles/captions are ok for this example...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">((</span><span class="pln">track</span><span class="pun">.</span><span class="pln">language </span><span class="pun">===</span><span class="pln"> lang</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="pun">(</span><span class="pln">track</span><span class="pun">.</span><span class="pln">kind </span><span class="pun">!==</span><span class="pln"> </span><span class="str">"chapters"</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;track</span><span class="pun">.</span><span class="pln">mode</span><span class="pun">=</span><span class="str">"showing"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">trackAsHtmlElem</span><span class="pun">.</span><span class="pln">readyState </span><span class="pun">===</span><span class="pln"> </span><span class="lit">2</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="com">// the track has already been loaded</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayCues</span><span class="pun">(</span><span class="pln">track</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; displayCuesAfterTrackLoaded</span><span class="pun">(</span><span class="pln">trackAsHtmlElem</span><span class="pun">,</span><span class="pln"> track</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp;/* Fallback for FireFox that still does not implement cue enter and exit events<br></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;track.addEventListener("cuechange", function(e) {</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var cue = this.activeCues[0];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console.log("cue change");</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;var transcriptText = document.getElementById(cue.id);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transcriptText.classList.add("current");</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;});</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; */</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayCuesAfterTrackLoaded</span><span class="pun">(</span><span class="pln">trackElem</span><span class="pun">,</span><span class="pln"> track</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Create a listener that will only be called once the track has</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// been loaded. We cannot display the transcript before </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp; // the track is loaded</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;trackElem</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'load'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"track loaded"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; displayCues</span><span class="pun">(</span><span class="pln">track</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">});</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> disableAllTracks</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> tracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp;</span>// the track mode is important: disabled tracks do not fire events</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;tracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">"disabled"</span><span class="pun">;&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayCues</span><span class="pun">(</span><span class="pln">track</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// displays the transcript of a TextTrack</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cues </span><span class="pun">=</span><span class="pln"> track</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">//&nbsp;iterate on all cues of the current track</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> len </span><span class="pun">=</span><span class="pln"> cues</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> len</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; // current cue, also add enter and exit listeners to it</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> cues</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; addCueListeners</span><span class="pun">(</span><span class="pln">cue</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; // Test if the cue content is a voice &lt;v speaker&gt;....&lt;/v&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> voices </span><span class="pun">=</span><span class="pln"> getVoices</span><span class="pun">(</span><span class="pln">cue</span><span class="pun">.</span><span class="pln">text</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> transText</span><span class="pun">=</span><span class="str">""</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">voices</span><span class="pun">.</span><span class="pln">length </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> j </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> j </span><span class="pun">&lt;</span><span class="pln"> voices</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> j</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span><span class="com">// how many voices?</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; transText </span><span class="pun">+=</span><span class="pln"> voices</span><span class="pun">[</span><span class="pln">j</span><span class="pun">].</span><span class="pln">voice </span><span class="pun">+</span><span class="pln"> </span><span class="str">': '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> removeHTML</span><span class="pun">(</span><span class="pln">voices</span><span class="pun">[</span><span class="pln">j</span><span class="pun">].</span><span class="pln">text</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transText </span><span class="pun">=</span><span class="pln"> cue</span><span class="pun">.</span><span class="pln">text</span><span class="pun">;</span><span class="pln"> </span><span class="com">// not a voice text</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> clickableTransText </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;li class='cues' id="</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> cue</span><span class="pun">.</span><span class="pln">id </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> </span><span class="str">" onclick='jumpTo("</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+&nbsp;</span><span class="pln">cue</span><span class="pun">.</span><span class="pln">startTime </span><span class="pun">+</span><span class="pln"> </span><span class="str">");'"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&gt;"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> transText </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/li&gt;"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; addToTranscriptDiv</span><span class="pun">(</span><span class="pln">clickableTransText</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getVoices</span><span class="pun">(</span><span class="pln">speech</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// takes a text content and check if there are voices</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> voices </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span><span class="pln"> </span><span class="com">// inside</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> pos </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&lt;v'</span><span class="pun">);</span><span class="pln"> </span><span class="com">// voices are like &lt;v Michel&gt; ....</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="pln">pos </span><span class="pun">!=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; endVoice </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&gt;'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> voice </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="pln">pos </span><span class="pun">+</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> endVoice</span><span class="pun">).</span><span class="pln">trim</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> endSpeech </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&lt;/v&gt;'</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> text </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="pln">endVoice </span><span class="pun">+</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> endSpeech</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; voices</span><span class="pun">.</span><span class="pln">push</span><span class="pun">({</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="str">'voice'</span><span class="pun">:</span><span class="pln"> voice</span><span class="pun">,</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="str">'text'</span><span class="pun">:</span><span class="pln"> text</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">});</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; speech </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="pln">endSpeech </span><span class="pun">+</span><span class="pln"> </span><span class="lit">4</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; pos </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&lt;v'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> voices</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> removeHTML</span><span class="pun">(</span><span class="pln">text</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> div </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'div'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; div</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> text</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> div</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">||</span><span class="pln"> div</span><span class="pun">.</span><span class="pln">innerText </span><span class="pun">||</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> jumpTo</span><span class="pun">(</span><span class="pln">time</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; // Make the video jump at the time position + force play </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; // if it was not playing</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; video</span><span class="pun">.</span><span class="pln">currentTime </span><span class="pun">=</span><span class="pln"> time</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; video</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> clearTranscriptDiv</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; transcriptDiv</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> addToTranscriptDiv</span><span class="pun">(</span><span class="pln">htmlText</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; transcriptDiv</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> htmlText</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> addCueListeners</span><span class="pun">(</span><span class="pln">cue</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; cue</span><span class="pun">.</span><span class="pln">onenter </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp;// Highlight current cue transcript by adding the </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp;// cue.current CSS class</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'enter id='</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">id</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> transcriptText </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">id</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;transcriptText</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="str">"current"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> cue</span><span class="pun">.</span><span class="pln">onexit </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'exit id='</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> cue</span><span class="pun">.</span><span class="pln">id</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> transcriptText </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">id</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;transcriptText</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">remove</span><span class="pun">(</span><span class="str">"current"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">} // end of addCueListeners...</span></li>
</ol></div><br>


#### Loading WebVTT file using Ajax/XHR2 

__Load a WebVTT file using Ajax/XHR2 and parse it manually__

This is an old example written in 2012 at a time when the track API was not supported by browsers. It downloads WebVTT files using Ajax and parses it "by hand". Notice the complexity of the code, compared to the previous example that uses the track API instead. We give this example as is. Sometimes, bypassing all APIs can be a valuable solution, especially when support for the track API is sporadic, as was the case in 2012...

Here is an [example at JSBin](https://jsbin.com/vedelequso/edit?html,js,output) that displays the values of the cues in the different tracks:

[Local Demo](src/01c-example02.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/2QzbheZ")"
    src    = "https://bit.ly/3bAOJBZ"
    alt    = "screenshot of JsBin example: video on top and two buttons 'english' and 'german' at bottom for extracting the track contents in english or german"
    title  = "screenshot of JsBin example: video on top and two buttons 'english' and 'german' at bottom for extracting the track contents in english or german"
  />
</figure>


This example, adapted from an example from (now offline) dev.opera.com, uses some JavaScript code that takes a WebVTT subtitle (or caption) file as an argument, parses it, and displays the text on screen, in an element with an `id` of transcript.

Extract from HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span style="color: #000088;" color="#000088">...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://..../elephants-dream-medium.mp4"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://..../elephants-dream-medium.webm"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun">=</span><span class="atv">"https://..../elephants-dream-subtitles-en.vtt"</span><span class="pln"> </span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"de"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun">=</span><span class="atv">"https://..../elephants-dream-subtitles-de.vtt"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun">=</span><span class="atv">"https://..../elephants-dream-chapters-en.vtt"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp;...</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;h3&gt;</span><span class="pln">Video Transcript</span><span class="tag">&lt;/h3&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">loadTranscript</span><span class="pun">(</span><span class="str">'en'</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">English</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">loadTranscript</span><span class="pun">(</span><span class="str">'de'</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Deutsch</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/div&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"transcript"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;">...</li>
</ol></div><br>

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Transcript.js, by dev.opera.com</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadTranscript</span><span class="pun">(</span><span class="pln">lang</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> url </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://mainline.i3s.unice.fr/mooc/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp;'elephants-dream-subtitles-'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> lang </span><span class="pun">+</span><span class="pln"> </span><span class="str">'.vtt'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// Will download using Ajax + extract subtitles/captions&nbsp; &nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;loadTranscriptFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">);&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadTranscriptFile</span><span class="pun">(</span><span class="pln">webvttFileUrl</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Using Ajax/XHR2 (explained in detail in Module 3)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> reqTrans </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;reqTrans</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> webvttFileUrl</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// callback, called only once the response is ready</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;reqTrans</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> pattern </span><span class="pun">=</span><span class="pln"> </span><span class="str">/^([0-9]+)$/</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> patternTimecode </span><span class="pun">=</span><span class="pln"> </span><span class="str">/^([0-9]{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3}) --\&gt; ([0-9]</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{2}:[0-9]{2}:[0-9]{2}[,.]{1}[0-9]{3})(.*)$/</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> content </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">response</span><span class="pun">;</span><span class="pln"> </span><span class="com">// content of the webVTT file</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> lines </span><span class="pun">=</span><span class="pln"> content</span><span class="pun">.</span><span class="pln">split</span><span class="pun">(</span><span class="str">/\r?\n/</span><span class="pun">); // Get an array of text lines</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> transcript </span><span class="pun">=</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="pln">i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> lines</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> identifier </span><span class="pun">=</span><span class="pln"> pattern</span><span class="pun">.</span><span class="kwd">exec</span><span class="pun">(</span><span class="pln">lines</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// is there an id for this line, if it is, go to next line</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">identifier</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;i</span><span class="pun">++;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> timecode </span><span class="pun">=</span><span class="pln"> patternTimecode</span><span class="pun">.</span><span class="kwd">exec</span><span class="pun">(</span><span class="pln">lines</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]);&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">// is the current line a</span>&nbsp;timecode?</li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">timecode </span><span class="pun">&amp;&amp;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> lines</span><span class="pun">.</span><span class="pln">length</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ &nbsp; &nbsp; &nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;<span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>// if it is go to next line&nbsp;&nbsp; &nbsp;&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; i</span><span class="pun">++;</span></li>
<li class="L7" style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span class="pun">// it can only be a text&nbsp;</span>line now</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> text </span><span class="pun">=</span><span class="pln"> lines</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]; &nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>// is the text multiline?</li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="pln">lines</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]</span><span class="pln"> </span><span class="pun">!==</span><span class="pln"> </span><span class="str">''</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> lines</span><span class="pun">.</span><span class="pln">length</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ &nbsp;&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;text </span><span class="pun">=</span><span class="pln"> text </span><span class="pun">+</span><span class="pln"> </span><span class="str">'\n'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> lines</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;i</span><span class="pun">++;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> transText </span><span class="pun">=</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> voices </span><span class="pun">=</span><span class="pln"> getVoices</span><span class="pun">(</span><span class="pln">text</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;// is the extracted text multi voices ?&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">voices</span><span class="pun">.</span><span class="pln">length </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>// how many voices ?</li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> j </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> j </span><span class="pun">&lt;</span><span class="pln"> voices</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> j</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transText </span><span class="pun">+=</span><span class="pln"> voices</span><span class="pun">[</span><span class="pln">j</span><span class="pun">].</span><span class="pln">voice </span><span class="pun">+</span><span class="pln"> </span><span class="str">': '</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> removeHTML</span><span class="pun">(</span><span class="pln">voices</span><span class="pun">[</span><span class="pln">j</span><span class="pun">].</span><span class="pln">text</span><span class="pun">)</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> </span><span class="str">'&lt;br /&gt;'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}&nbsp;</span><span class="kwd">else</span><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>// not a voice text</li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transText </span><span class="pun">=</span><span class="pln"> removeHTML</span><span class="pun">(</span><span class="pln">text</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">'&lt;br /&gt;'</span><span class="pun">;&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;transcript </span><span class="pun">+=</span><span class="pln"> transText</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> oTrans </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'transcript'</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;oTrans</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> transcript</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;reqTrans</span><span class="pun">.</span><span class="pln">send</span><span class="pun">(); // send the Ajax request</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> getVoices</span><span class="pun">(</span><span class="pln">speech</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ &nbsp;// takes a text content and check if there are voices&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> voices </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[]; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// inside</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> pos </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&lt;v'</span><span class="pun">); // voices are like &lt;v Michel&gt; ....</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="pln">pos </span><span class="pun">!=</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; endVoice </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&gt;'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> voice </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="pln">pos </span><span class="pun">+</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> endVoice</span><span class="pun">).</span><span class="pln">trim</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> endSpeech </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&lt;/v&gt;'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> text </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="pln">endVoice </span><span class="pun">+</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> endSpeech</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; voices</span><span class="pun">.</span><span class="pln">push</span><span class="pun">({</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">'voice'</span><span class="pun">:</span><span class="pln"> voice</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="str">'text'</span><span class="pun">:</span><span class="pln"> text</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">});</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; speech </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="pln">endSpeech </span><span class="pun">+</span><span class="pln"> </span><span class="lit">4</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; pos </span><span class="pun">=</span><span class="pln"> speech</span><span class="pun">.</span><span class="pln">indexOf</span><span class="pun">(</span><span class="str">'&lt;v'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">return</span><span class="pln"> voices</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> removeHTML</span><span class="pun">(</span><span class="pln">text</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> div </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'div'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; div</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> text</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="kwd">return</span><span class="pln"> div</span><span class="pun">.</span><span class="pln">textContent </span><span class="pun">||</span><span class="pln"> div</span><span class="pun">.</span><span class="pln">innerText </span><span class="pun">||</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
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
    + button to load English transcript: `<button disabled id="buttonEnglish" onclick="loadTranscript('en')>Display English transcript</button>`
    + button to load German transcript: `<button disabled id="buttonGerman" onclick="loadTranscript('de')>Display Deutsch transcript</button>`
    + video container w/ various video sources and tracks
  + CSS style snippet
    + cues color: `.cues {color: blue; }`
    + mouse hover cues: `.cues.hover{ text-decoration: underline; }`
    + current cue: `.cues.current{ color: black; font-weight: bold; }`
    + Video container: `#myVideo{ display: block; float: left; margin-right: 3%; width: 66%; background-color: black; position: relative; }`
    + transcript container: `#transcript{ paddin: 10px; border: 1px solid; float: left; max-height: 225px; overflow: auto; width: 25%; margin: 0; font-size: 14px; list-style: none; }`
  + Javascript snippet
    + declare global variables: `var video, transcriptDiv; var tracks, trackElems, trackURLs = []; var buttonEnglish, buttonDeutsch;`
    + actions after page loaded: `window.onload = function() {...}`
      + console msg: `console.log("init");`
      + video container: `video = document.querySelector("#myVideo");`
      + transcript container: `transcriptDiv = document.querySelector("#transcript");`
      + all tracks: `trackElems = document.querySelectorAll("track);`
      + get all URLs of vtt files: `for (var i=0; i<trackElms.length; i++) {...}`
        + current track: `var currentTrackElem = trackElems[i];
        + URL of current track: `tracksURLs[i] = currentTrackElem.src;`
      + English button: `buttonEnglish = document.querySelector("#buttonEnglish");`
      + Deutsch button: `buttonDeutsch = document.querySelector("#buttonDeutsch");`
      + disable buttons: `buttonEnglish.disabled = true; buttonDeutsch.disabled = true;`
      + access tracks: `tracks = video.textTracks;`
    + download transcript once button clicked: `function loadTranscript(lang) {...}`
      + empty transcript container: `clearTranscriptDiv();`
      + set all track mode disabled: `disableAllTracks();`
      + iterate through all languages: `for (var i=0; i<tracks.length; i++) {...}`
        + access current track and element: `var track = tracks[i]; var trackAsHtmlElem = trackElems[i];`
        + existence of language and kind of track id ok: `if ((track.language === lang) && (track.kind !== "chapter")) {...}`
        + change track mode: `track.mode = "showing";`
        + display track: `displayCues(track);`
        + checktrack status: `if (trackAsHtml.readyState ==== 2) {...}`
        + call display function if ok: `displayCues(track);`
        + call to download and display track: `displayCuesTrackLoaded(trackAsHtmlElem, track);`
        + add event listener for FireFox (no enter/exit events): `track.addEventListener("cuechange", function(e) {...})`
          + current cue: `var cue = this.activeCues[0];`
          + log msg: `console.log("cue change");`
          + get cue: `var transcriptText = document.getElementById(cue.id);`
          + change display style: `transcriptText.classList.add("current");`
    + download and display transcript: `function displayCuesAfterTrackLoaded(trackElem, track) {...}`
      + add event listener: `trackElem.addEventListener('load', dunction(e) {...})`
      + log msg: `console.log("track loaded");`
      + call function to display cues: `displayCues(track);`
    + disable all tracks: `function disableAllTracks() {...}`
      + iterate through all tracks: `for (var i=0; i<tracks.length; i++) {...}`
      + disable current track: `tracks[i].mode = "disabled";`
    + display all cues of current track: `function displayCues(track) {...}`
      + get all cues: `var cues = track.cues;`
      + iterate on all cues: `for (var i=0; i<cues.length; i++) {...} (...)`
        + get current cue andcall function to add event listener: `var cue = cues[i]; addCueListeners(cue);`
        + call function to get all cues w/ voice `<v speaker>...</v>`: `var voices = getVoices(cue.text);`
        + declare transcript text variable: `var transText = "";`
        + voice existed: `if (voices.length >0) {...}`
          + existed: `for (var j=0; j<voices.length;j++) {transText += voices[j].voice + ": " + removeHTML(voices[j].text) });`
          + non-existed: `transText = cue.text;`
        + declare clickable contents: `var clickableTransText = "<li class='cues' id=" + cue.id + "onclick="jumpTo(" + cue+startTime + ");" + ">" + transText + "</li>";`
        + add to transcript container: `addToTranscriptDiv(clickableTransText);`
    + extract info for speaker and text: `function getVoices(speech) {...}`
      + declare variables: `var voices = []; var pos = speech.indexOf('<');`
      + iterate until `pos` not existed: `while(pos ~= -1) {...}`
        + get various info: `endVoice = speech.indexOf('>'); var voice = speech.substring(pos + 2, endVoice).trim(); var endSpeech = speech.indexOf('</v>'); var text = speech.substring(endVoice + 1, endSpeech);`
        + append current voice: `voice.push({ 'voice': voice, 'text': text});`
        + move the position: `speech = speech.substring(endSpeech + 4); pos = speech.indexOf('<'));`
      + return all voices obtained: `return voices;`
    + write HTML `div` element: `function removeHTML(text) {...}`
      + access `div` element: `var div = document.createElement('div');`
      + write given text: `div.innerHTML = text;`
      + return required info: `return div.textContent || div.innerText || ";`
    + jump to a given time  to play video: `function jumpTo(time) { video.currentTime = time; video.play(); }`
    + clear transcript container: `function clearTranscriptDiv() { transcriptDiv.innerHTML = ""; }`
    + add cue to transcript container: `function addToTranscriptDiv(htmlText) { transcriptDiv.innerHTML += htmlText; }`
    + add listener to a cue: `function addCueListeners(cue) {...}`
      + callback function for enter event: `cue.onenter = function() {...};`
        + log msg: `console.log('enter id =' + this.id);`
        + access transcript element: `vat transcriptText = document.getElementById(this.id);`
        + add highlighted style: `transcriptText.classList.add("current");`
      + callback function for exit event: `function cue.onexit = function() {...};`
        + log msg: `console.log('exit id=' + cue.id);`
        + access transcript element: `var transcriptText = document.getElementById(this.id);`
        + remove highlighted style: `transcriptText.classList.remove("current");`

+ Example: download vtt file w/ Ajax/XHR2
  + used prior to the track API available
  + download WebVTT files using Ajax and parse manually
  + HTML snippet
    + video element: `<video preload="metadata" controls> ... </video>`
    + button for English: `<button onclick="loadTranscript('en');>English</button>`
    + button for Deutsch: `<button onclick="loadTranscript('de');>Deutsch</button>`
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
      + extract start time of the next line: `i++; var timecode = patternTimecode.exec(line[i]);`
      + check start time: `if (timecode && i > lines.length) {...}`
        + get cue from the next line: `i++; var text = lines[i];`
        + move to the next text line: `while (lines[i] !== " && i < lines.length) { text = text + '\n' + lines[i]; i++; }`
        + extract the voice: `var transText = "; var voices = getVoices(text);`
        + iterate for multiple voices and add to the transcript text: `if (voices.length > 0) { for (var j = 0; j<voices.length; j++) { transText += voices.length; j++) { transText += voices.voice + ':' + removeHTML(voices[i].text) + '<br>'} } }`
        + not voice text: `else {transText = removeHTML(text) + '<br>'; }`
      + append to transcript text: `transText += transText;`
      + send the Ajax request: `reqTrans.send();`
    + extract voice from cues (same as the previous example): `function getVoices(speech) {...}`
    + remove HTML (same as the previous example): `function removeHTML(text) {...}`


### 1.3.2 Captions, descriptions, chapters, and metadata

__Example #2: showing video description while playing, listening to events, changing the mode of a track__

Each track has a `mode` property (and a `mode` attribute) that can be: "_disabled_", "_hidden_" or "_showing_". More than one track at a time can be in any of these states.  The difference between "_hidden_" and "_disabled_" is that hidden tracks can fire events (more on that at the end of the first example) whereas disabled tracks do not fire events.

[Here is an example at JSBin](https://jsbin.com/bixoru/1/edit?html,css,js,output) that shows the use of the mode property, and how to listen for cue events in order to capture the current subtitle/caption from JavaScript. You can change the mode of each track in the video element by clicking on its button. This will toggle the mode of that track. All tracks with mode="showing" or mode="hidden" will have the content of their cues displayed in real time in a small area below the video.

In the screen-capture below, we have a WebVTT file displaying a scene's captions and descriptions.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open("https://bit.ly/3oCbhrn")"
    src    = "https://bit.ly/3uiXJCp"
    alt    = "Example that shows how to toggle track modes and listen to events"
    title  = "Example that shows how to toggle track modes and listen to events"
  />
</figure>


Extract from HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;">...</li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;">...</li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; poster</span><span class="pln"> </span><span class="pun">=</span><span class="atv">"https://...../sintel.jpg"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; controls</span><span class="pun">=</span><span class="atv">"controls"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; width</span><span class="pun">=</span><span class="atv">"640"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"272"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/sintel.mp4"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px; background-color: #ffffff;">.....</span>/sintel.webm"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/sintel-captions.vtt"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"captions"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">=</span><span class="atv">"English Captions"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;default</span></strong><span class="tag">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px; background-color: #ffffff;">.....</span>/sintel-descriptions.vtt"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"descriptions"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">=</span><span class="atv">"Audio Descriptions"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/sintel-chapters.vtt"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">=</span><span class="atv">"Chapter Markers"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px; background-color: #ffffff;">.....</span>/sintel-thumbs.vtt"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">=</span><span class="atv">"Preview Thumbs"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;/video&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"currentTrackStatuses"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"subtitlesCaptions"</span><span class="tag">&gt;&lt;/div&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/p&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">clearSubtitlesCaptions</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; Clear subtitles/captions log</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;/button&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Click one of these buttons to toggle the mode of each track:</span><span class="tag">&lt;/p&gt;<br><br></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">toggleTrack</span><span class="pun">(</span><span class="lit">0</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;Toggle english caption track mode</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;br&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">toggleTrack</span><span class="pun">(</span><span class="lit">1</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;Toggle audio description track mode</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;br&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">toggleTrack</span><span class="pun">(</span><span class="lit">2</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;Toggle chapter track mode</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;br&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">toggleTrack</span><span class="pun">(</span><span class="lit">3</span><span class="pun">);</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;Toggle preview thumbnail track modes</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br>


JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> tracks</span><span class="pun">,</span><span class="pln"> video</span><span class="pun">,</span><span class="pln"> statusDiv</span><span class="pun">,</span><span class="pln"> subtitlesCaptionsDiv</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<span style="line-height: 25.6px;">statusDiv</span>&nbsp;</span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#currentTrackStatuses"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln" style="line-height: 1.6;">&nbsp; &nbsp;subtitlesCaptionsDiv </span><span class="pun" style="line-height: 1.6;">=</span><span class="pln" style="line-height: 1.6;"> document</span><span class="pun" style="line-height: 1.6;">.</span><span class="pln" style="line-height: 1.6;">querySelector</span><span class="pun" style="line-height: 1.6;">(</span><span class="str" style="line-height: 1.6;">"#subtitlesCaptions"</span><span class="pun" style="line-height: 1.6;">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;tracks </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"track"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'loadedmetadata'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"metadata loaded"</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// defines cue listeners for the active track; we can do this only after the video metadata have been loaded</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">&lt;</span><span class="pln">tracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> tracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">track</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">t</span><span class="pun">.</span><span class="pln">mode </span><span class="pun">===</span><span class="pln"> </span><span class="str">"showing"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; t</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'cuechange'</span><span class="pun">,</span><span class="pln"> logCue</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp;</span>// display in a div the list of tracks and their status/mode value</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;displayTrackStatus</span><span class="pun">(); &nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">});</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayTrackStatus</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // display the status / mode value of each track. </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // In red if disabled, in green if showing</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">&lt;</span><span class="pln">tracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> tracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">track</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> mode </span><span class="pun">=</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">mode</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">mode </span><span class="pun">===</span><span class="pln"> </span><span class="str">"disabled"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;span style='color:red'&gt;"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">mode </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/span&gt;"</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="kwd">if</span><span class="pun">(</span><span class="pln">mode </span><span class="pun">===</span><span class="pln"> </span><span class="str">"showing"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;span style='color:green'&gt;"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">mode </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/span&gt;"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;appendToScrollableDiv</span><span class="pun">(</span><span class="pln">statusDiv</span><span class="pun">,</span><span class="pln"> </span><span class="str">"track "&nbsp;</span><span class="pun">+&nbsp;</span><span class="pln">i&nbsp;</span><span class="pun">+&nbsp;</span><span class="str">": "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">label </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +</span><span class="pln"> </span><span class="str">" "&nbsp;</span><span class="pun">+&nbsp;</span><span class="pln">t</span><span class="pun">.</span><span class="pln">kind</span><span class="pun">+</span><span class="str">" in "</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +&nbsp;</span><span class="pln">mode&nbsp;</span><span class="pun">+&nbsp;</span><span class="str">" mode"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;">}</li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> appendToScrollableDiv</span><span class="pun">(</span><span class="pln">div</span><span class="pun">,</span><span class="pln"> text</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// we've got two scrollable divs. This function </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// appends text to the div passed as a parameter</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// The div is scrollable (thanks to CSS overflow:auto)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> inner </span><span class="pun">=</span><span class="pln"> div</span><span class="pun">.</span><span class="pln">innerHTML</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;div</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> inner </span><span class="pun">+</span><span class="pln"> text </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;br/&gt;"</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Make it display the last line appended</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;div</span><span class="pun">.</span><span class="pln">scrollTop </span><span class="pun">=</span><span class="pln"> div</span><span class="pun">.</span><span class="pln">scrollHeight</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> clearDiv</span><span class="pun">(</span><span class="pln">div</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;div</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> clearSubtitlesCaptions</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;clearDiv</span><span class="pun">(</span><span class="pln">subtitlesCaptionsDiv</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> toggleTrack</span><span class="pun">(</span><span class="pln">i</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// toggles the mode of track i, removes the cue listener </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// if its mode becomes "disabled"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// adds a cue listener if its mode was "disabled" </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// and becomes "hidden"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> tracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">track</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp;switch</span><span class="pln"> </span><span class="pun">(</span><span class="pln">t</span><span class="pun">.</span><span class="pln">mode</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">case</span><span class="pln"> </span><span class="str">"disabled"</span><span class="pun">:</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'cuechange'</span><span class="pun">,</span><span class="pln"> logCue</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t</span><span class="pun">.</span><span class="pln">mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">"hidden"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">case</span><span class="pln"> </span><span class="str">"hidden"</span><span class="pun">:</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t</span><span class="pun">.</span><span class="pln">mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">"showing"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">case</span><span class="pln"> </span><span class="str">"showing"</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t</span><span class="pun">.</span><span class="pln">removeEventListener</span><span class="pun">(</span><span class="str">'cuechange'</span><span class="pun">,</span><span class="pln"> logCue</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;t</span><span class="pun">.</span><span class="pln">mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">"disabled"</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // updates the status</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; clearDiv</span><span class="pun">(</span><span class="pln">statusDiv</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; displayTrackStatus</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; appendToScrollableDiv</span><span class="pun">(</span><span class="pln">statusDiv</span><span class="pun">,</span><span class="str">"&lt;br&gt;"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">label</span><span class="pun">+</span><span class="str">" are now "</span><span class="pln"> </span><span class="pun">+</span><span class="pln">t</span><span class="pun">.</span><span class="pln">mode</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> logCue</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// callback for the cue event</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">activeCues </span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">activeCues</span><span class="pun">.</span><span class="pln">length</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">activeCues</span><span class="pun">[</span><span class="lit">0</span><span class="pun">].</span><span class="pln">text</span><span class="pun">; // text of current cue</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; appendToScrollableDiv</span><span class="pun">(</span><span class="pln">subtitlesCaptionsDiv</span><span class="pun">,</span><span class="pln"> </span><span class="str">"Active "</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +&nbsp;</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">kind&nbsp;</span><span class="pun">+&nbsp;</span><span class="str">" changed to: "&nbsp;</span><span class="pun">+&nbsp;</span><span class="pln">t</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div><br>






### 1.3.3 With buttons for choosing the subtitle language






### 1.3.4 With a simple chapter navigation menu






### 1.3.5 With thumbnails, using JSON cues






### 1.3.6 Discussion and project






