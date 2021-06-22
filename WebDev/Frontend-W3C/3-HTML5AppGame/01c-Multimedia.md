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
    onclick= "window.open('https://bit.ly/2QzbheZ")"
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
    onclick= "window.open('https://bit.ly/2QzbheZ")"
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
    onclick= "window.open('https://bit.ly/2QzbheZ")"
    src    = "https://bit.ly/3bAOJBZ"
    alt    = "screenshot of JsBin example: video on top and two buttons 'english' and 'german' at bottom for extracting the track contents in english or german"
    title  = "screenshot of JsBin example: video on top and two buttons 'english' and 'german' at bottom for extracting the track contents in english or german"
  />
</figure>


This example, adapted from an example from (now offline) dev.opera.com, uses some JavaScript code that takes a WebVTT subtitle (or caption) file as an argument, parses it, and displays the text on screen, in an element with an `id` of transcript.

Extract from HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span style="color: #008888;">...</span></li>
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
    + video element<a name="videoElmt"></a>: `<video preload="metadata" controls crossOrigin="anonymous"> ... </video>`
      + MP4 video source: `<source src="https://.../elephants-dream-medium.mp4" type="video/mp4">`
      + Webm video source: `<source src="https://.../elephats-dream-medium.webm" type="video/webm">`
      + English subtitle track: `<track label="Englih subtitle" kind=subtitles srclang=en src="https://.../elephats-dream-subtitles-en.vtt">`
      + Deutsch subtitle track: `<track label="Deutsch subtitle" kind=subtitles srclang=de src="https://.../elephats-dream-subtitles-de.vtt">`
      + English capters track: `<track label="English chapters" kind=chapters srclang=en src="https://.../elephats-dream-chapters-en.vtt">`
    + button to load English transcript<a name="buttonEn"></a>: `<button disabled id="buttonEnglish" onclick="loadTranscript('en');">Display English transcript</button>`
    + button to load German transcript<a name="buttonDe"></a>: `<button disabled id="buttonDeutsch " onclick="loadTranscript('de');">Display Deutsch transcript</button>`
    + video container w/ various video sources and tracks
  + CSS style snippet<a name="css"></a>
    + cues color: `.cues {color: blue; }`
    + mouse hover cues: `.cues.hover{ text-decoration: underline; }`
    + current cue: `.cues.current{ color: black; font-weight: bold; }`
    + video container: `#myVideo{ display: block; float: left; margin-right: 3%; width: 66%; background-color: black; position: relative; }`
    + transcript container: `#transcript{ padding: 10px; border: 1px solid; float: left; max-height: 225px; overflow: auto; width: 25%; margin: 0; font-size: 14px; list-style: none; }`
  + Javascript snippet
    + declare global variables: `var video, transcriptDiv; var tracks, trackElems, trackURLs = []; var buttonEnglish, buttonDeutsch;`
    + actions after page loaded<a name="pageLoad"></a>: `window.onload = function() {...}`
      + console msg: `console.log("init");`
      + video container: `video = document.querySelector("#myVideo");`
      + transcript container: `transcriptDiv = document.querySelector("#transcript");`
      + all tracks: `trackElems = document.querySelectorAll("track);`
      + get all URLs of vtt files: `for (var i=0; i<trackElms.length; i++) {...}`
        + current track: `var currentTrackElem = trackElems[i];`
        + URL of current track: `tracksURLs[i] = currentTrackElem.src;`
      + English button: `buttonEnglish = document.querySelector("#buttonEnglish");`
      + Deutsch button: `buttonDeutsch = document.querySelector("#buttonDeutsch");`
      + disable buttons: `buttonEnglish.disabled = true; buttonDeutsch.disabled = true;`
      + access tracks: `tracks = video.textTracks;`
    + download transcript once button clicked<a name="buttonClick"></a>: `function loadTranscript(lang) {...}`
      + empty transcript container: `clearTranscriptDiv();`
      + set all track mode disabled: `disableAllTracks();`
      + iterate through all languages: `for (var i=0; i<tracks.length; i++) {...}`
        + access current track and element: `var track = tracks[i]; var trackAsHtmlElem = trackElems[i];`
        + existence of language and kind of track id: `if ((track.language === lang) && (track.kind !== "chapter")) {...}`
        + change track mode: `track.mode = "showing";`
        + display track: `displayCues(track);`
        + check track status: `if (trackAsHtml.readyState === 2) {...}`
        + call to display function if ok: `displayCues(track);`
        + call to download and display track: `displayCuesTrackLoaded(trackAsHtmlElem, track);`
        + add event listener for FireFox (no enter/exit events): `track.addEventListener("cuechange", function(e) {...})`
          + current cue: `var cue = this.activeCues[0];`
          + log msg: `console.log("cue change");`
          + get cue: `var transcriptText = document.getElementById(cue.id);`
          + change display style: `transcriptText.classList.add("current");`
    + download and display transcript<a name="downDisplay"></a>: `function displayCuesAfterTrackLoaded(trackElem, track) {...}`
      + add event listener: `trackElem.addEventListener('load', function(e) {...})`
      + log msg: `console.log("track loaded");`
      + call function to display cues: `displayCues(track);`
    + disable all tracks: `function disableAllTracks() {...}`
      + iterate through all tracks: `for (var i=0; i<tracks.length; i++) {...}`
      + disable current track: `tracks[i].mode = "disabled";`
    + display all cues of current track: `function displayCues(track) {...}`
      + get all cues: `var cues = track.cues;`
      + iterate on all cues: `for (var i=0; i<cues.length; i++) {...}`
        + get current cue and call function to add event listener: `var cue = cues[i]; addCueListeners(cue);`
        + call function to get all cues w/ voice `<v speaker>...</v>`: `var voices = getVoices(cue.text);`
        + declare transcript text variable: `var transText = "";`
        + voice existed: `if (voices.length >0) {...}`
          + existed: `for (var j=0; j<voices.length;j++) {transText += voices[j].voice + ": " + removeHTML(voices[j].text) });`
          + non-existed: `transText = cue.text;`
        + declare clickable contents: `var clickableTransText = "<li class='cues' id=" + cue.id + "onclick="jumpTo(" + cue.startTime + ");" + ">" + transText + "</li>";`
        + add to transcript container: `addToTranscriptDiv(clickableTransText);`
    + extract info for speaker and text<a name="extractInfo"></a>: `function getVoices(speech) {...}`
      + declare variables: `var voices = []; var pos = speech.indexOf('<');`
      + iterate until `pos` not existed: `while(pos != -1) {...}`
        + get various info: `endVoice = speech.indexOf('>'); var voice = speech.substring(pos + 2, endVoice).trim(); var endSpeech = speech.indexOf('</v>'); var text = speech.substring(endVoice + 1, endSpeech);`
        + append current voice: `voice.push({ 'voice': voice, 'text': text});`
        + move the position: `speech = speech.substring(endSpeech + 4); pos = speech.indexOf('<'));`
      + return all voices obtained: `return voices;`
    + remove HTML `div` element<a name="removeHTML"></a>: `function removeHTML(text) {...}`
      + access `div` element: `var div = document.createElement('div');`
      + write given text: `div.innerHTML = text;`
      + return required info: `return div.textContent || div.innerText || '';`
    + jump to a given time to play video<a name="jumpStart"></a>: `function jumpTo(time) { video.currentTime = time; video.play(); }`
    + clear transcript container: `function clearTranscriptDiv() { transcriptDiv.innerHTML = ""; }`
    + add cue to transcript container: `function addToTranscriptDiv(htmlText) { transcriptDiv.innerHTML += htmlText; }`
    + add listener to a cue<a name="addCueListener"></a>: `function addCueListeners(cue) {...}`
      + callback function for enter event: `cue.onenter = function() {...};`
        + log msg: `console.log('enter id =' + this.id);`
        + access transcript element: `vat transcriptText = document.getElementById(this.id);`
        + add highlighted style: `transcriptText.classList.add("current");`
      + callback function for exit event: `cue.onexit = function() {...};`
        + log msg: `console.log('exit id=' + cue.id);`
        + access transcript element: `var transcriptText = document.getElementById(this.id);`
        + remove highlighted style: `transcriptText.classList.remove("current");`

+ Example: download vtt file w/ Ajax/XHR2
  + used prior to the track API available
  + download WebVTT files using Ajax and parse manually
  + HTML snippet
    + [video element](#videoElmt)
    + [button for English](#buttonEn)
    + [buttone for German](#buttonDe)
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
      + extract start time of the next line: `i++; var timecode = patternTimecode.exec(lines[i]);`
      + check start time: `if (timecode && i > lines.length) {...}`
        + get cue from the next line: `i++; var text = lines[i];`
        + move to the next text line: `while (lines[i] !== '' && i < lines.length) { text = text + '\n' + lines[i]; i++; }`
        + extract the voice: `var transText = ''; var voices = getVoices(text);`
        + iterate for multiple voices and add to the transcript text: `if (voices.length > 0) { for (var j = 0; j<voices.length; j++) { transText += voices.voice + ':' + removeHTML(voices[i].text) + '<br>'} } }`
        + not voice text: `else {transText = removeHTML(text) + '<br>'; }`
      + append to transcript text: `transcript += transText;`
      + send the Ajax request: `reqTrans.send();`
    + [extract voice](#extractInfo) from cues
    + [remove HTML](#removeHTML)


### 1.3.2 Captions, descriptions, chapters, and metadata


#### Display Video Description

__Example #2: showing video description while playing, listening to events, changing the mode of a track__

Each track has a `mode` property (and a `mode` attribute) that can be: "_disabled_", "_hidden_" or "_showing_". More than one track at a time can be in any of these states.  The difference between "_hidden_" and "_disabled_" is that hidden tracks can fire events (more on that at the end of the first example) whereas disabled tracks do not fire events.

[Here is an example at JSBin](https://jsbin.com/bixoru/1/edit?html,css,js,output) that shows the use of the `mode` property, and how to listen for cue events in order to capture the current subtitle/caption from JavaScript. You can change the mode of each track in the video element by clicking on its button. This will toggle the mode of that track. All tracks with `mode="showing"` or `mode="hidden"` will have the content of their cues displayed in real time in a small area below the video.

[Local Demo](src/01c-example02.html)

In the screen-capture below, we have a WebVTT file displaying a scene's captions and descriptions.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3oCbhrn")"
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
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;>.....</span>/sintel.webm"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/sintel-captions.vtt"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"captions"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">=</span><span class="atv">"English Captions"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;default</span></strong><span class="tag">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;>.....</span>/sintel-descriptions.vtt"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"descriptions"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">=</span><span class="atv">"Audio Descriptions"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/sintel-chapters.vtt"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;label</span><span class="pun">=</span><span class="atv">"Chapter Markers"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;>.....</span>/sintel-thumbs.vtt"</span><span class="pln"> </span></li>
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
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">Click one of these buttons to toggle the mode of each track:</span><span class="tag">&lt;/p&gt;<br></span></li>
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


#### Notes for 1.3.2 Captions, descriptions, chapters, and metadata

+ Example: display video description
  + `mode` property: `disabled`, `hidden`, or `showing`
    + multiple tracks able to be any state
    + event difference: `hidden` tracks able to fire events while `disabled` track unable to fire events
  + tasks
    + showing the use of the `mode` property
    + listening for cue event to capture the current subtitle/caption
    + changing the mode of a track in video element by toggling on the button
  + HTML snippet
    + init page after loading: `<body onload="init();">`
    + video element: `<video id="#myVideo" preload="metadata" poster="https://.../sintel.jpg" crossorigin="anonymous" width=640 height=272>...</video>`
      + MP4 video source: `<source src="https://.../sintel.mp4" type="video/mp4">`
      + Webm video source: `<source src="https://.../sintel.webm" type="video/webm">`
      + English caption: `<track src="https://.../sintel-cpations.vtt" kind=captions label="English Captions" default/>`
      + audio descriptions:" `<track src="https://.../sintel-descriptions.vtt" kind=descriptions label="Audio Descriptions">`
      + chapter markers: `<track src="https://.../sintel-chapters.vtt" kind=chapters label="Chapter Markers">`
      + thumbnail preview: `<track src="https://.../sintel-thumbs.vtt" kind=metadata label="Preview Thumbs">`
    + clear subtitles: `<button onclick="clearSubtitlesCaptions();">Clear subtitles/captions log</button>`
    + button for English: `<button onclcik="toggleTracks(0);">Toggle english caption track mode</button>`
    + button for audio: `<button onclick="toggleTracks(1);">Toggle audio description track mode</button>`
    + button for chapter: `<button onclick="toggleTracks(2);">Toggle chapter caption track mode</button>`
    + button for preview: `<button onclick="toggleTracks(3);">Toggle preview thumbnail track mode</button>`
    + containers for track status & subtitle captions: `<p><div id="currentTrackStatuses"></div></p> <p><div id="subtitlesCaptions"></div></p>`
  + Javascript snippet
    + declar global variables: `var tracks, video, statusDiv, subtitlesCaptionsDiv;`
    + init page while page loaded: `function init() {...}`
      + access video, status, subtitle and tracks elements: `video = document.querySelector("#myVideo"); statusDiv = document.querySelector("currentTrackStatuses"); subtitlesCaptionsDiv = document.querySelector("#subtitleCations"); tracks = document.querySelectorAll("track");`
      + add event listener: `video.addEventListener('loadedmetadata', function() {...});`
        + log msg: `console.log("metadata loaded");`
        + iterate to add event listeners for all cues: `for (var i=0; i<tracks.length; i++) { var t = tracks[i].track; if (t.mode === "showing") { t.addEventListener("cuechange", logCue, false) } }`
        + display the tracks and their status/mode value: `displayTrackStatus();`
    + disply status of tracks: `function displayTrackStatus() {...}`
      + display the status / mode value of each track w/ color red if disable and color green if showing
      + iterate on all tracks: `for (var i=0; i<tracks.length; i++) {...}`
        + declare variables: `var t = tracks[i].length; var mode = t.mode;`
        + disabled mode: `if (mode === "disabled") { mode = "<span style='color: red'>" + t.mode + "</span>"; }`
        + showing mode: `else if (mode === "showing") { mode = "<span style='color: green'>" + t.mode + "</span>" }`
        + append to container: `appendToScrollableDiv(statusDiv, "track" + i + ": " + t.label + " " + t.kind + " in " + mode + " mode");`
    + append to container: `function appendToScrollableDiv(div, text) {...}`
      + two scrollable divs
      + append text to the div passed as a parameter
      + declare variables: `var inner = div.innerHTML; div.innerHTML = inner + text + "<br/>";`
      + append to the text: `div.scrollTop = div.scrollHeight;`
    + empty div container: `function clearDiv(div) { div.innerHTML = ''; }`
    + empty subtitle container: `function clearSubstitutesCaptions() { clearDiv(subtitlesCaptionsDiv); }`
    + toggle track mode: `function toggleTrack(i) {...}`
      + declare variable: `var t = tracks[i].track;`
      + deal w/ different modes: `switch (t.mode) {...}`
        + disabled mode: `case "disabled": t.addEventListener('cuechange', logCue, false); t.mode='hidden'; break;`
        + hidden mode: `case "hidden": t.mode="showing"; break;`
        + showing mode: `case "showing": t.removeEventListener('curchange', logCue, false); t.mode="disabled"; break;`
      + update status: `clearDiv(statusDiv); displayTrackStatus(); appendToScrollableDiv(statusDiv, "<br>" + t.label + " are now " + t.mode);`
    + callback for current event: `function logCue() {...}`
      + check active cue existed: `if (this.activeCues && this.activeCues.length) {...}`
      + access current cue: `var t = this.activeCues[0].text;`
      + append text to subtitles/captions: `appendToScrollableDiv(subtitlesCaptionsDiv, "Active" + this.kind + " changed to:" + t);`


### 1.3.3 With buttons for choosing the subtitle language


#### Buttons for choosing the `subtitle` language

__Example #3: adding buttons for choosing the subtitle/caption track__

You might have noticed that with some browsers, before 2018, the standard implementation of the video element did not let the user choose the subtitle language. Now, recent browsers offers a menu to choose the track to display. 

However, before it was available, it was easy to implement this feature using the Track API.

Here is a [simple example at JSBin](https://jsbin.com/balowuq/1/edit?html,css,js,output): we added two buttons below the video to enable/disable subtitles/captions and let you choose which track you prefer.

[Local Demo](src/01c-example03.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick= "window.open('https://bit.ly/3hLYBMV')"
    src    = "https://bit.ly/3yytDhu"
    alt    = "Buttons for choosing the track/language under a standard video player"
    title  = "Buttons for choosing the track/language under a standard video player"
  />
</figure>


HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">()</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://...../elephants-dream-medium.mp4"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln">&nbsp;&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;srclang</span><span class="pun">=</span><span class="atv">"en"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>default</strong></span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp;&lt;track</span><span class="pln">&nbsp;&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;srclang</span><span class="pun">=</span><span class="atv">"de"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;src</span><span class="pun">=</span><span class="atv">"https://...../elephants-dream-subtitles-de.vtt"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp;&lt;track</span><span class="pln">&nbsp;&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;srclang</span><span class="pun">=</span><span class="atv">"en"</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://...../elephants-dream-chapters-en.vtt"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h3&gt;</span><span class="pln">Current track: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"currentLang"</span><span class="tag">&gt;&lt;/span&gt;&lt;/h3&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"langButtonDiv"</span><span class="tag">&gt;&lt;/div&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/section&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;">...</li>
</ol></div><br>


JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> langButtonDiv</span><span class="pun">,</span><span class="pln"> currentLangSpan</span><span class="pun">,</span><span class="pln"> video</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;langButtonDiv </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#langButtonDiv"</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;currentLangSpan </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#currentLang"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Number of tracks = "</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Updates the display of the current track activated</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;currentLangSpan</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> activeTrack</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Build the buttons for choosing a track</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;buildButtons</span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;">}</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> activeTrack</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">mode </span><span class="pun">===</span><span class="pln"> </span><span class="str">'showing'</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">label </span><span class="pun">+</span><span class="pln"> </span><span class="str">" ("</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">language </span><span class="pun">+</span><span class="pln"> </span><span class="str">")"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">return</span><span class="pln"> </span><span class="str">"no subtitles/caption selected"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> buildButtons</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ // if the video contains track elements</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// For each track, create a button</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// We create buttons only for the caption and subtitle tracks</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> track </span><span class="pun">=</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">((</span><span class="pln">track</span><span class="pun">.</span><span class="pln">kind </span><span class="pun">!==</span><span class="pln"> </span><span class="str">"subtitles"</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="pun">(</span><span class="pln">track</span><span class="pun">.</span><span class="pln">kind </span><span class="pun">!==</span><span class="pln"> </span><span class="str">"captions"</span><span class="pun">))</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; continue</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// create a button for track number i&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;createButton</span><span class="pun">(</span><span class="pln">video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]);&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> createButton</span><span class="pun">(</span><span class="pln">track</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;// Create a button</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">"button"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;b</span><span class="pun">.</span><span class="pln">value</span><span class="pun">=</span><span class="pln">track</span><span class="pun">.</span><span class="pln">label</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;</span>// use the lang attribute of the button to keep trace of the</li>
<li class="L2" style="margin-bottom: 0px;">&nbsp; &nbsp;// associated track language. Will be useful in the click listener</li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;b</span><span class="pun">.</span><span class="pln">setAttribute</span><span class="pun">(</span><span class="str">"lang"</span><span class="pun">,</span><span class="pln"> track</span><span class="pun">.</span><span class="pln">language</span><span class="pun">);&nbsp;</span><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;b</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'click'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Check which track is the track with the language we're</span><span class="pln"> </span><span class="com">looking for</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp;</span>// Get the value of the lang attribute of the clicked button</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> lang </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">getAttribute</span><span class="pun">(</span><span class="str">'lang'</span><span class="pun">);&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">language </span><span class="pun">==</span><span class="pln"> lang</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">'showing'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">].</span><span class="pln">mode </span><span class="pun">=</span><span class="pln"> </span><span class="str">'hidden'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// Updates the span so that it displays the new active track</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; currentLangSpan</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> activeTrack</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="pun">});</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; // Creates a label inside the button</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; b</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">document</span><span class="pun">.</span><span class="pln">createTextNode</span><span class="pun">(</span><span class="pln">track</span><span class="pun">.</span><span class="pln">label</span><span class="pun">));</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&nbsp; // Add the button to a div at the end of the HTML document</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; langButtonDiv</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">b</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
</ol></div>

#### External resources

+ If you are interested in building a complete custom video player, MDN offers an online tutorial with further information about [styling and integrating a "CC" button](https://mzl.la/3bOFgab)
+ The MDN documentation on [Web Video Text Tracks Format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (WebVTT)

#### Notes for 1.3.3 With buttons for choosing the subtitle language

+ Example: subtitle language
  + task: choose subtitle/caption track via button
  + HTML snippet
    + page full load: `<body onload="init()">`
    + [video element](#videoElmt)
    + toggle button to select subtitles: `<div id="langButtonDiv"></div>`
  + JavaScript snippet
    + declare variables: `var langButtonDiv, currentLangSpan, video;`
    + init page after fully loaded: `function init() {...}`
      + access elements: `langButtonDiv = document.querySelector("#langButtonDiv"); currentLangButton = document.querySelector("#currentLang"); video = document.querySelector("#myVideo");`
      + log msg: `console.log("Number of tracks = " + video.textTracks.length);`
      + display activated track: `currentLangSpan.innerHTML = activeTrack();`
      + build buttons: `buildButtons();`
    + active track: `function activeTrack() {...}`
      + iterate on tracks: `for (var i=0; i<video.textTracks.length; i++) {...}`
      + showing mode: `if (video.textTrack[i].mode === 'showing') { return video.textTracks[i].label + " (" + video.textTracks[i].language + ")"; }`
      + other mode: `return "no substitle/caption selected";`
    + build buttons: `function buildButtons() {...}`
      + check the existence of track: `if (video.textTracks) {...}`
      + create a button each track: `for (var i=0;i<video.textTracks.length; i++) {...}`
      + access current track: `var track = video.textTracks[i];`
      + skip mode not subtitles and captions: `if ((track.kind !== "subtitles") && (track.kind !== "captions")) continue;`
      + create button: `createButton(video.textTracks[i]);`
    + create button: `function createButton(track) {...}`
      + access element: `var b = document.createElement("button"); b.value = track.label;`
      + set `lang` attribute: `b.setAttribute("lang", track.language);`
      + add event listener: `b.addEventListener('click', function(e)) {...}`
        + get `lang` value: `var lang = this.getAttribute('lang');`
        + iterate tracks: `for (var i=0; i<video.textTracks.length; i++) {...}`
        + same language: `if (video.textTracks[i].language == lang) { video.textTracks[i].mode = 'showing'; }`
        + other language: `else { video.textTracks[i].mode = 'hidden'; }`
        + display the new active track: `currentLangSpan.innerHTML = activeTracl();`
      + create button label and add button to container: `b.appendChild(document.createTextNode(track.label)); langButtonDiv.appendChild(b);`


### 1.3.4 With a simple chapter navigation menu


#### Chapter Navigation Menu

__Example #4: making a simple chapter navigation menu__

We can use WebVTT files to define chapters. The syntax is exactly the same as for subtitles/caption .vtt files. The only difference is in the declaration of the track. Here is how we declared a chapter track in one of the previous examples (in bold in the example below):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bMOhAL')"
    src    = "https://bit.ly/3bQO13s"
    alt    = "Simple chapter navigation"
    title  = "Simple chapter navigation"
  />
</figure>

HTML code:

<div class="source-code" style="line-height: 25.6px;"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln">&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln">&nbsp;</span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln">&nbsp;</span><span class="atn">controls</span><span class="pln">&nbsp;</span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://...../elephants-dream-medium.mp4"</span><span class="pln"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;>.....</span>/elephants-dream-medium.webm"</span><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln">&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"</span><span class="pln">&nbsp;</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln">&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"de"</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;>.....</span>/elephants-dream-subtitles-de.vtt"</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;default</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>&nbsp;</strong></span><strong><span class="tag">&lt;track</span><span class="pln">&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"></span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"<span style="color: #ff0000;">chapters</span>"</span><span class="pln"></span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"></span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-chapters-en.vtt"</span><span class="tag">&gt;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div> <br>

If we try this code in an HTML document, nothing special happens. No magic menu, no extra button!

Currently, no browser takes chapter tracks into account. You could use one of the enhanced video players presented during the HTML5 Part 1 course, but as you will see in this lesson: making your own chapter navigation menu is not complicated.

__Let's start by examining the sample `.vtt` file__

`elephant-dream-chapters-en.vtt`:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">1</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">00.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">26.000</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">Introduction</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">2</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">28.206</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">02.000</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="typ">Watch</span><span class="pln"> </span><span class="kwd">out</span><span class="pun">!</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">3</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">02.034</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">03</span><span class="pun">:</span><span class="lit">10.000</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="typ">Let</span><span class="str">'s go</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">chapter-4</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">00:03:10.014 --&gt; 00:05:40.000 </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="str">The machine</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="str">chapter-5</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="str">00:05:41.208 --&gt; 00:07:26.000 </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">Close your eyes</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">chapter-6</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">00:07:27.125 --&gt; 00:08:12.000</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">There'</span><span class="pln">s nothing there</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">7</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">08</span><span class="pun">:</span><span class="lit">13.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">09</span><span class="pun">:</span><span class="lit">07.500</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="typ">The</span><span class="pln"> </span><span class="typ">Colossus</span><span class="pln"> of </span><span class="typ">Rhodes</span></li>
</ol></div><br>

There are 7 cues (one for each chapter). Each cue id is the word "chapter-" followed by the chapter number, then we have the start and end time of the cue/chapter, and the cue content. In this case: the description of the chapter ("Introduction", "Watch out!", "Let's go", etc...).

Hmm... let's try to open this chapter track with the [example](https://jsbin.com/zeqoleq/1/edit?html,css,js,output) we wrote in a previous lesson - the one that displayed the clickable transcript for subtitles/captions on the right of the video. We need to modify it a little bit:

[Local Demo](src/01c-example04.html)

1. We add a "show English chapters" button with a click event listener similar to this:

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">disabled</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"buttonEnglishChapters"</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">loadTranscript</span><span class="pun">(</span><span class="str">'en'</span><span class="pun">,</span><span class="pln"> </span><span class="str" style="color: #ff0000;">'chapters'</span><span class="pun">);</span><span class="atv">"</span></strong><span class="tag">&gt;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Display English chapter markers</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;<br></span></li>
  </ol></div>

2. We modify the `loadTranscript` function from the previous example, so that it matches both the `srclang` and the `kind` attribute of the track.

  Here is a new version: in bold are the source code lines we modified.

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> loadTranscript</span><span class="pun">(</span><span class="pln">lang</span><span class="pun">,</span><span class="pln" style="color: #ff0000;"> kind</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;...</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Locate the track with&nbsp;lang and kind that match the parameters</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> tracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;...</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><strong><span class="kwd">if</span><span class="pun">((</span><span class="pln">track</span><span class="pun">.</span><span class="pln">language </span><span class="pun">===</span><span class="pln"> lang</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="pun">(</span><span class="pln">track</span><span class="pun">.</span><span class="pln">kind </span><span class="pun">===</span><span class="pln" style="color: #ff0000;"> kind</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></strong></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// display it contents...</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
  </ol></div>


#### Clickable Chapters

Simple approach: chapters as clickable text on the right of the video

[Try it on JSBin](https://jsbin.com/rifekik/edit?html,css,js): this version includes the modifications we presented earlier - nothing more. Notice that we kept the existing buttons to display a clickable transcript:

[Local Demo](src/01c-example05.html)

Look at the JavaScript and HTML tab of the JSBin example to see the source code. It's the same as in the clickable transcript example, except for the small changes we explained earlier.

Chapter navigation, illustrated in the video player below, is fairly popular.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick= "window.open('https://bit.ly/3bMOhAL')"
    src    = "https://bit.ly/3fbqfkM"
    alt    = "Example of video player that uses text based chapter navigation"
    title  = "Example of video player that uses text based chapter navigation"
  />
</figure>

In addition to the clickable chapter list, this one displays an enhanced progress bar created using a canvas. The small squares are drawn corresponding to the chapter cues' start and end times. You could modify the code provided, in order to add such an enhanced progress indicator.

However, we will see how we can do better by using JSON objects as cue contents. This will be the topic of the next two lessons!


#### Notes for 1.3.4 With a simple chapter navigation menu

+ VebVTT file and chapters
  + using WebVTT files to define chapters
  + task: display subtitles/caption into `.vtt` files
  + HTML snippet: [video element](#videoElmt)
  + no browser taking chapter track in account
  + example of `.vtt` file <a name="vtt"></a>

    ```vtt
    WEBVTT

    chapter-1
    00:00:00.000 --> 00:00:26.000
    Introduction

    chapter-2
    00:00:28.206 --> 00:01:02.000
    Watch out!
    ...
    ```

    + cue id: `chapter-` + chapter number
    + start and end time of the cue/chapter
    + description of the chapter: `Introduction`, `Watch out!`, etc.

+ Example: display English chapters
  + HTML snipper:
    + display English chapter w/ button: `<button disabled id="buttonEnglishChapters" onclick="loadTranscript('en', , 'chapters');">Display English chapter markers</button>`
  + JavaScript snippet:
    + revise [`loadTranscript`](#buttonClick) w/ `kind` property: `function loadTranscript(lang, kind);`
    + check to display text: `if ((track.language === lang) && (track.kind === kind)) {...}`

+ Example: clickable chapters
  + task: chapters as clickable text
  + same as `dispaly English chapters` example except for chapters


### 1.3.5 With thumbnails, using JSON cues


#### Chapter Menu w/ Image Thumbnails

__Example #5: create a chapter menu with image thumbnails__

Instead of using text (optionally using HTML for styling, multi lines, etc.), it is also possible to use JSON objects as cue values that can be manipulated from JavaScript. JSON means "JavaScript Object Notation". It's an open standard for describing JavaScript objects as plain text.

Here is an example cue from a WebVTT file encoded as JSON instead of plain text. JSON is useful for describing "structured data"', and processing such data from JavaScript is easier than parsing plain text.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="typ">Wikipedia</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">15.200</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">02</span><span class="pun">:</span><span class="lit">18.800</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong style="color: olive;">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong style="color: olive;">&nbsp; &nbsp;"title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"State of Wikipedia"</span><span class="pun">,</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong style="color: olive;">&nbsp; &nbsp;"description"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Jimmy Wales talking ..."</span><span class="pun">,</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong style="color: olive;">&nbsp; &nbsp;"src"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://upload.wikimedia.org/...../120px-Wikipedia-logo-v2.svg.png"</span><span class="pun">,</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong style="color: olive;">&nbsp; &nbsp;"href"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://en.wikipedia.org/wiki/Wikipedia"</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong style="color: olive;">}</span></strong></li>
</ol></div><br>

This JSON object (in bold olive) is a JavaScript object encoded as a text string. If we listen for cue events or if we read a WebVTT file as done in previous examples, we can extract this text content using the `cue.text` property. For example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> videoElement </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myvideo"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> textTracks </span><span class="pun">=</span><span class="pln"> videoElement</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">;</span><span class="pln"> </span><span class="com">// one for each track element</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> textTrack </span><span class="pun">=</span><span class="pln"> textTracks</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span><span class="pln"> </span><span class="com">// corresponds to the first track element</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> cues </span><span class="pun">=</span><span class="pln"> textTrack</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> cues</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span><span class="pln"> </span><span class="com">// first cue</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="kwd">// cue.text is in JSON format, with JSON.parse we turn it back </span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="kwd">// to a real JavaScript object</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> obj </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">parse</span><span class="pun">(</span><span class="pln">cue</span><span class="pun">.</span><span class="pln">text</span><span class="pun">);</span><span class="pln">&nbsp;</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> title </span><span class="pun">=</span><span class="pln"> obj</span><span class="pun">.</span><span class="pln">title</span><span class="pun">;</span><span class="pln"> </span><span class="com">// "State of Wikipedia"</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> description </span><span class="pun">=</span><span class="pln"> obj</span><span class="pun">.</span><span class="pln">description</span><span class="pun">;</span><span class="pln"> </span><span class="com">// Jimmy Wales talking...</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">etc</span><span class="pun">...</span></li>
</ol></div><br>

This is a powerful way of embedding metadata, especially when used in conjunction with listening for cue and track events.


#### Better Chapter Menu w/ Enriched Chapter Markers

__Improved approach: make a nicer chapter menu by embedding a richer description of chapter markers__

Earlier we saw [an example](https://jsbin.com/jiyodit/edit?html,css,js,output) that could display chapter markers as clickable text on the right of a video.

[Local Demo](src/01c-example06.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9')"
    src    = "https://bit.ly/3bQO13s"
    alt    = "Simple chapter menu in plain text"
    title  = "Simple chapter menu in plain text"
  />
</figure>

This example used only standard plain text content for the cues:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">1</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">00.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">26.000</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">Introduction</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">chapter</span><span class="pun">-</span><span class="lit">2</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">28.206</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">02.000</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="typ">Watch</span><span class="pln"> </span><span class="kwd">out</span><span class="pun">!</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span>...</li>
</ol></div>

We used this example to manually capture the images from the video that correspond to each of the seven chapters:

+ We clicked on each chapter link on the right, then paused the video,
+ then we used a screen capture tool to grab each image that corresponds to the beginning of chapter,
+ Finally, we resized the images with Photoshop to approximately 200x400 pixels.

(For advanced users: it's possible to semi-automatize this process using the [ffmepg](https://www.ffmpeg.org/) command line tool, see for example [this](https://bit.ly/3fGTbA9) and [that](https://bit.ly/3wtsVQJ)).

Here are the images which correspond to the seven chapters of the video from the previous example:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://bit.ly/3bQuyA9" ismap target="_blank">
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3ywRhe8"
      alt   = "chapter 1 thumbnail"
      title = "chapter 1 thumbnail"
    >
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/346FO7c"
      alt   = "chapter 2 thumbnail"
      title = "chapter 2 thumbnail"
    >
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/2QHXVx0"
      alt   = "chapter 3 thumbnail"
      title = "chapter 3 thumbnail"
    >
  </a><a href="url" ismap target="_blank">
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3hIoBJg"
      alt   = "chapter 4 thumbnail"
      title = "chapter 4 thumbnail"
    >
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3fcKhLS"
      alt   = "chapter 5 thumbnail"
      title = "chapter 5 thumbnail"
    >
  </a>
    <img style="margin: 0.1em;" height=100
      src   = "https://bit.ly/3vgkHLE"
      alt   = "chapter 6 thumbnail"
      title = "chapter 6 thumbnail"
    >
  </a>
</div>

To associate these images with its chapter description, we will use JSON objects as cue contents:

[elephants-dream-chapters-en-JSON.vtt](https://mainline.i3s.unice.fr/mooc/elephants-dream-chapters-en-JSON.vtt):

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

Before explaining the code, we propose that you [try this example at JSBin](https://jsbin.com/pulefe/1/edit?html,css,js,output) that uses this new `.vtt` file:

[Local Demo](src/01c-example07.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9')"
    src    = "https://bit.ly/3wyNATD"
    alt    = "Video with nice chapter menu that uses thumbnail images"
    title  = "Video with nice chapter menu that uses thumbnail images"
  />
</figure>


HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="pln"> </span><span class="atn">controls</span><span class="pln"> </span><span class="atn">crossOrigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://...../elephants-dream-medium.mp4"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-medium.webm"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English subtitles"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-en.vtt"</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Deutsch subtitles"</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"de"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-subtitles-de.vtt"</span><span class="pln"> </span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English chapters"</span><span class="pln"> </span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"chapters"</span><span class="pln"> </span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="line-height: 25.6px;">.....</span>/elephants-dream-chapters-en-<span style="color: #ff0000;">JSON</span>.vtt"</span><span class="tag">&gt;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/video&gt;</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h2&gt;</span><span class="pln">Chapter menu</span><span class="tag">&lt;/h2&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"chapterMenu"</span><span class="tag">&gt;&lt;/div&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;...</span></li>
</ol></div><br>

It's the same code we had in the first example, except that this time we use a new WebVTT file that uses JSON cues to describe each chapter. For the sake of simplicity, we also removed the buttons and all the code for displaying a clickable transcript of the subtitles/captions on the right of the video.

JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> video</span><span class="pun">,</span><span class="pln"> chapterMenuDiv</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> tracks</span><span class="pun">,</span><span class="pln"> trackElems</span><span class="pun">,</span><span class="pln"> tracksURLs </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">window</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"init"</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// When the page is loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;chapterMenuDiv </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#chapterMenu"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Get the tracks as HTML elements</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;trackElems </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelectorAll</span><span class="pun">(</span><span class="str">"track"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> trackElems</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> currentTrackElem </span><span class="pun">=</span><span class="pln"> trackElems</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; tracksURLs</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> currentTrackElem</span><span class="pun">.</span><span class="pln">src</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Get the tracks as JS TextTrack objects</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;tracks </span><span class="pun">=</span><span class="pln"> video</span><span class="pun">.</span><span class="pln">textTracks</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"><span style="color: #880000; line-height: 25.6px;">&nbsp; &nbsp;<strong>//&nbsp;Build the chapter navigation menu for the given lang and kind</strong></span></span></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp;buildChapterMenu</span><span class="pun">(</span><span class="str">'en'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'chapters'</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> buildChapterMenu</span><span class="pun">(</span><span class="pln">lang</span><span class="pun">,</span><span class="pln"> kind</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Locate the track with language = lang and kind="chapters"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> tracks</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="com">// current track</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> track </span><span class="pun">=</span><span class="pln"> tracks</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> trackAsHtmlElem </span><span class="pun">=</span><span class="pln"> trackElems</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">if</span><span class="pun">((</span><span class="pln">track</span><span class="pun">.</span><span class="pln">language </span><span class="pun">===</span><span class="pln"> lang</span><span class="pun">)</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="pun">(</span><span class="pln">track</span><span class="pun">.</span><span class="pln">kind </span><span class="pun">===</span><span class="pln"> kind</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">// the track must be active,&nbsp;otherwise it will not load</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; track</span><span class="pun">.</span><span class="pln">mode</span><span class="pun">=</span><span class="str">"showing"</span><span class="pun">; // "hidden" would work too</span><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">if</span><span class="pun">(</span><span class="pln">trackAsHtmlElem</span><span class="pun">.</span><span class="pln">readyState </span><span class="pun">===</span><span class="pln"> </span><span class="lit">2</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="com">// the track has already been loaded</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;displayChapterMarkers</span><span class="pun">(</span><span class="pln">track</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;displayChapterMarkersAfterTrackLoaded</span><span class="pun">(</span><span class="pln">trackAsHtmlElem</span><span class="pun">,</span><span class="pln"> track</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln">&nbsp;</span><span class="pun"><spanline-height: 25.6px;">displayChapterMarkers</span>(</span><span class="pln">track</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> cues </span><span class="pun">=</span><span class="pln"> track</span><span class="pun">.</span><span class="pln">cues</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;// We must not see the cues on the video</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;track.mode = "hidden";</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// Iterate on cues</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> len </span><span class="pun">=</span><span class="pln"> cues</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> len</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> cue </span><span class="pun">=</span><span class="pln"> cues</span><span class="pun">[</span><span class="pln">i</span><span class="pun">];</span></li>
<li class="L0" style="margin-bottom: 0px;">&nbsp;</li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>&nbsp;</strong></span><strong><span class="kwd">var</span><span class="pln"> cueObject </span><span class="pun">=</span><span class="pln"> JSON</span><span class="pun">.</span><span class="pln">parse</span><span class="pun">(</span><span class="pln">cue</span><span class="pun">.</span><span class="pln">text</span><span class="pun">);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> description </span><span class="pun">=</span><span class="pln"> cueObject</span><span class="pun">.</span><span class="pln">description</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> imageFileName </span><span class="pun">=</span><span class="pln"> cueObject</span><span class="pun">.</span><span class="pln">image</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> imageURL </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://mainline.i3s.unice.fr/mooc/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> imageFileName</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="com">//&nbsp;Build the marker. It's a figure with an img and a figcaption inside.</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; // The img has an onclick listener that will make the video jump</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">&nbsp; &nbsp; &nbsp; // to the start time of the current cue/chapter</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> figure </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'figure'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; figure</span><span class="pun">.</span><span class="pln">classList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span><span class="str">"img"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; figure</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;img onclick='jumpTo("</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> cue</span><span class="pun">.</span><span class="pln">startTime </span><span class="pun">+</span><span class="pln"> </span><span class="str">");' class='thumb' src='"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> imageURL</span>&nbsp;+ <span class="str">"'&gt;&lt;figcaption class='desc'&gt;"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;+</span><span class="pln"> description </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/figcaption&gt;&lt;/figure&gt;"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; // Add the figure to the chapterMenuDiv</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; chapterMenuDiv</span><span class="pun">.</span><span class="pln">insertBefore</span><span class="pun">(</span><span class="pln">figure</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayChapterMarkersAfterTrackLoaded</span><span class="pun">(</span><span class="pln">trackElem</span><span class="pun">,</span><span class="pln"> track</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Create a listener that will only be called when the track has</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// been loaded</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; trackElem</span><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'load'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"chapter track loaded"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun"><span style="line-height: 25.6px;">displayChapterMarkers</span>(</span><span class="pln">track</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">});</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> jumpTo</span><span class="pun">(</span><span class="pln">time</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; video</span><span class="pun">.</span><span class="pln">currentTime </span><span class="pun">=</span><span class="pln"> time</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; video</span><span class="pun">.</span><span class="pln">play</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div><br>


__Explanations:__

+ _Lines  4-18_: when the page is loaded, we assemble all of the track HTML elements and their corresponding TextTrack objects.
+ _Line 19_: using that we can build the chapter navigation menu. All is done in the `window.onload` callback, so nothing happens until the DOM is ready.
+ _Lines 24-43_: the `buildChapterMenu` function first locates the chapter track for the given language, then checks if this track has been loaded by the browser. Once it has been confirmed that the track is loaded, the function `displayChapters` is called.
+ _Lines 45-65_: the `displayChapters(track)` function will iterate over all of the cues within the chapter track passed as its parameter. For each cue, the JSON content is re-formatted back into a JavaScript object (_line 55_) and the image filename and description of the chapter/cue are extracted (_lines 56-57_). Then an HTML description for the chapter is built and added to the `div` element with `id=chapterMenu`. Here is the HTML code for one menu marker:

  <div class="source-code"><ol class="linenums" style="list-style-type: decimal;">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;figure</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"<g class="gr_ gr_127 gr-alert gr_spell gr_run_anim ContextualSpelling ins-del multiReplace" id="127" data-gr-id="127">img</g>"</span><span class="tag">&gt;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">jumpTo</span><span class="pun">(</span><span class="lit">0</span><span class="pun">);</span><span class="atv">"</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"thumb"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://...../introduction.jpg"</span><span class="tag">&gt;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;figcaption</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"desc"</span><span class="tag">&gt;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; Introduction</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;/figcaption&gt;</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/figure&gt;</span></li>
  </ol></div><br>

Notice that we add a click listener to each thumbnail image. Clicking a chapter thumbnail will cause the video to jump to the chapter time location (the example above is for the first chapter with start time = 0).

We also added CSS classes "img", "thumb" and "desc", which make it easy to style and position the thumbnails using CSS.

CSS source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">#chapterMenuSection {</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightgrey</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">-</span><span class="pln">radius</span><span class="pun">:</span><span class="lit">10px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;padding</span><span class="pun">:</span><span class="pln"> </span><span class="lit">20px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;display</span><span class="pun">:</span><span class="kwd">inline</span><span class="pun">-</span><span class="pln">block</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;margin</span><span class="pun">:</span><span class="lit">0px</span><span class="pln"> </span><span class="lit">30px</span><span class="pln"> </span><span class="lit">30px</span><span class="pln"> </span><span class="lit">30px</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;width</span><span class="pun">:</span><span class="lit">90</span><span class="pun">%;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">figure</span><span class="pun">.</span><span class="pln">img </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; margin</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">float</span><span class="pun">:</span><span class="pln"> left</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">figcaption</span><span class="pun">.</span><span class="pln">desc </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln"> center</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; font</span><span class="pun">-</span><span class="pln">weight</span><span class="pun">:</span><span class="pln"> normal</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; margin</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">.</span><span class="pln">thumb </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="lit">75px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1px</span><span class="pln"> solid </span><span class="com">#000;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; margin</span><span class="pun">:</span><span class="pln"> </span><span class="lit">10px</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; box</span><span class="pun">-</span><span class="pln">shadow</span><span class="pun">:</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> grey</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; transition</span><span class="pun">:</span><span class="pln"> all </span><span class="lit">0.5s</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">.</span><span class="pln">thumb</span><span class="pun">:</span><span class="pln">hover </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; box</span><span class="pun">-</span><span class="pln">shadow</span><span class="pun">:</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> </span><span class="lit">5px</span><span class="pln"> black</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br>

A sample menu marker is shown below (it's also animated - hover your mouse over the thumbnail to see its animated shadow):


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9')"
    src    = "https://bit.ly/3ffAvsx"
    alt    = "Introduction"
    title  = "Introduction"
  />
</figure>


#### Chapter Menu w/ Clickable Transcript

__Combining techniques: a clickable transcript and a chapter menu__

This example is the same as the previous one except that we have kept the features that we saw previously: the buttons for displaying a clickable transcript. The code is longer, but it's just a combination of the "clickable transcript" example from the previous lesson, and the code from earlier in this lesson.

[Try it at JSBin](https://jsbin.com/zewemaj/edit?html,js,output)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick= "window.open('https://bit.ly/3bQuyA9")"
    src    = "https://bit.ly/3ucOkfp"
    alt    = "Chapter menu + clickable transcript"
    title  = "Chapter menu + clickable transcript"
  />
</figure>


#### Notes for 1.3.5 With thumbnails, using JSON cues

+ WebVTT file w/ JSON
  + possible to use JSON as cue values
  + able to manipulate JSON from JavaScript
  + able to be extracted JSON object w/ `cue.text`
  + a powerful way of embedding metadata
  + particularly used in conjunction w/ listening for cue and track events

+ Example: extract JSON object from WebVTT file
  + text within curly brackets `{...}` as a JSON object

    ```json
    WEBVTT
    Wikipedia
    00:01:15.200 --> 00:02:18.800
    {
      "title": "State of Wikipedia",
      "description": "Jimmy Wales talking ...",
      "src": "https://upload.wikimedia.org/...../120px-Wikipedia-logo-v2.svg.png",
      "href": "https://en.wikipedia.org/wiki/Wikipedia"
    }
    ```
  
  + JavaScript snippet:
    + declare variables for various elements: `var videoElement = document.querySelector("#myVideo"); var textTracks = videoElement.textTracks; var textTrack = textTracks[0];`
    + declare variables for cues: `var cues = textTrack.cues; var cue = cues[0];`
    + convert JSON text into JSON object: `var obj = JSON.parse(cue.text);`
    + access description: `var description = obj.description;`

+ Example: chapter menu w/ description of chapter markers
  + procedure: manually capture the images from the video file
    + click on each chapter link to pause video
    + using a screen capture tool to grape each image corresponding to the beginning of chapter
    + resizing the images approximately 200x400 pixels
  + WebVTT w/ chapter

    ```json
    WEBVTT
    
    chapter-1
    00:00:00.000 --> 00:00:26.000
    {
      "description": "Introduction",
      "image": "introduction.jpg"
    }
    
    chapter-2
    00:00:28.206 --> 00:01:02.000
    {
      "description": "Watch out!",
      "image": "watchOut.jpg"
    }
    ...
    ```

  + HTML snippet
    + same as [video element](#videoElmt)
    + resvised chapter track w/ JSON: `<track label="English chapters" kind=chapters srclang="https://.../elephants-dream-chapters-en-JSON.vtt">`
    + create chapter container: `<div id="chapterMenu"></div>`
    + no button left but thumbnails created by JavaScript snippet
  + JavaScript snippet
    + declare variables: `var video, chapterMenuDiv; var tracks, trackElems, tracksURLs = [];`
    + init page after DOM ready: `window.onload = function() {...}`
      + same snippet as [page load](#pageLoad)
      + build chapter navigation menu: `buildChapterMenu('en', 'chapters');`
    + create chapter menu: `function buildChapterMenu(lang, kind) {...}`
      + iterate on all tracks: `for (var i=0; i<tracks.length; i++) {...}`
      + declare variables: `var track = tracks[i]; var trackAsHtmlElem = trackElems[i];`
      + check language and kind of the current track: `if ((track.language === lang) && (track.kind === kind)) {...}`
        + almost same as [button click snippet](#buttonClick)
        + display chapter menu: `displayChapterMarkers(track);`
      + other than the same language and kind: `else { displayChapterMarkersAfterTrackLoaded(trackAsHtmlElem, track); }`
    + display chapter menu: `function displayChapterMarkers(track) {...}`
      + declare variable: `var cues = track.cues;`
      + assign invisible value: `track.mode = "hidden";`
      + iterate on cues: `for (var i=0, len = cues.length; i<len; i++) {...}`
        + declare variable for info: `var cue = cues[i];`
        + assign variables related to JSON object: `var cueObject = JSON.parse(cue.text); var description = cueObject.description; var imageFileName = cueObject.image; var imageURL = "https://.../mooc" + imageFileName;`
        + add figure: `var figure = document.createElement('figure'); figure.classList.add('img');`
        + add img element: `figure.innerHTML = "<img onclick='jumpTo(" + cue.startTime + ");' class='thumb' src='" + imageURL + "><figcaption class='desc'>" + description + "</figcaption></figure>";`
        + add figure to chapter menu: `chapterMenuDiv.insertBefore(figure, null);`
    + display chapter markers after track loaded: `function displayChapterMarkersAfterTrackLoaded(trackElem, track) {...}`
      + add listener after track loaded: `trackElem.addEventListener('load', function(e){...});`
      + log msg: `console.log('chapter track loaded');`
      + display chapter menu: `displayChapterMarkers(track);`
    + play video from given start time: `function jumpTo(time) {...}`
      + set start time: `video.currentTime = time;`
      + play video: `play.video();`
  + CSS style
    + chapter menu: `#chapterMenuSection { background-color: lightgrey; border-radius: 10px; padding: 20px; border: 1px solid; display: inline-block; margin: 0px 30px 30px 30px; width: 90% }`
    + image: `figure.img{ margin: 2px; float: left; }`
    + description: `figcaption.desc { text-align: center; font-weight: normal; margin: 2px; }`
    + thumbnail img: `.thumb { height: 75px; border: 1px solid #000; margin: 10px 5px 0 0; box-shadow: 5px 5px 5px grey; transition: all 0.5s; }`
    + thumbnail hover: `.thumb.hover { box-shadow: 5px 5px 5px black; }`


### 1.3.6 Discussion and project

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

__Suggested topics of discussion:__

+ We presented improved video players in the examples, with clickable transcripts, buttons for choosing the subtitles, chapter menus, etc. Which example is your favorite?
+ What other functionalities would you like us to cover in a future course? Small images in the progress bar? Bookmarks? Loop A/B for repeating a given part of a video/audio? Others?


__Optional project:__

+ Make an impressive video player with an attractive menu for choosing between different subtitle files and a nice chapter menu. Be creative! You may use the provided examples as a starting point or build something on your own. Some suggestions: animated menu markers (CSS3 or animated GIFs, or even small video clips), a nice popup menu for choosing the subtitles, a button for hiding/showing a transcript, etc.




