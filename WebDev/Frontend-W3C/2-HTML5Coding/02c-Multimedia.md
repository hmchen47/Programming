# Week 2: HTML5 Multimedia


## 2.3 Subtitles and closed captions


### 2.3.0 Lecture Notes

+ The `<track>` element
  + adding closed captions, subtitles, descriptions, and metadata to videos
  + `WebVTT` format used for describing a track file
  + __closed caption__: describing all relevant audio present in the video; e.g., fire, rain, birds, gun fights, etc.
  + __subtitle__: only for spoken words
  + NB: unable to be used w/ `file://` url
  + e.g., `<track src="https://mainline.i3s.unice.fr/mooc/sintel-captions.vtt" kind="captions" label="Closed Captions" default>`
  + `kind` attribute: `subtitles`, `captions`, `descriptions`, `chapters` or `metadata`
  + `default` attribute: track to be displayed by default when reading the video
  + `label` attribute: displayed in the GUI control that is included in the default HTML5 video player
  + `srclang`: the language for the text track data, MUST present if `kind=subtitles`

+ The `WebVTT` format
  + WebVTT: The Web Video Text Tracks Format
  + files containing text for captions and subtitles, and much more..
  + used with the `src` attribute of the `<track>` element
  + format: a starting and ending time, plus a value (the text that will be displayed), followed by a blank line (blank lines are separators between elements)
  + "cue"
    + (optional) an ID useful when using the track element JavaScript API, in particular the `getCueById()` method of `TextTrack` object
    + types of ID:
      + numeric ID; e.g., `9`
      + string ID; e.g., `opening`
  + able to be displayed multiple lines w/o blank lines



### 2.3.1 HTML5 captioning

This section introduces the HTML5 `<track>` element, useful for adding closed captions, subtitles, descriptions, and metadata to your videos. It comes with a new JavaScript API.

The `WebVTT` format used for describing a track file is also presented in this chapter.


#### Most of the major desktop browsers support HTML5 captioning

Please check the [browser support](https://caniuse.com/#search=webvtt) related to the `<track>` element support by browsers.


#### Some definitions

+ __closed captions__ describe all relevant audio present in the video (fire, rain, birds, gun fights, etc.).
+ __subtitles__ are only for spoken words.

The accessibility features of TV programs often propose both options for people with hearing deficiencies. 


#### Typical use: add a subtitle/caption track to a `<video>` element

<div style="border: 2px solid red; margin: 10px; padding: 10px;">
<p><span style="color: #ff0000;"><strong>Important warning!!</strong></span></p>
<p>The <span style="font-family: 'courier new', courier;">&lt;track&gt;</span> element cannot be used with a <span style="font-family: 'courier new', courier;">file://</span> URL. Please use <span style="font-family: 'courier new', courier;">https://</span> and a Web server. Your server must use a special MIME format for the <span style="font-family: 'courier new', courier;">.vtt</span> files: <span style="font-family: 'courier new', courier;">text/vtt;charset=utf-8 <span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">(set by default on most servers now).</span></span></p>
<p>Examples of the lines to add to an Apache Web server:</p>
<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;Files</span><span class="pln"> </span><span class="atn">mysubtitle</span><span class="pln">.</span><span class="atn">vtt</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> ForceType text/vtt;charset=utf-8</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/Files&gt;</span></li>
</ol></div>
</div>

Here is [an example on JsBin](https://jsbin.com/nuqejof/edit?html,output) ([Local Example - Track](src/2/3/1-example1.html)) of a video element that includes a `<track>` element in the `.vtt` (WebVTT) format (line 9 in the source code shown below), .

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y3lkgdt2')"
    src    ="https://tinyurl.com/y3vd7ew4"
    alt    ="Adding a subtitle/caption track to a <video> element"
    title  ="Adding a subtitle/caption track to a <video> element"
  />
</figure>

As seen in this screenshot, the example uses a `<track>` element to insert basic captions to the video: sounds and music are described, in addition to standard subtitles that correspond to what the different movie characters say.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"272"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"640"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">poster</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/q1fx20VZ-640.jpg"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">controls</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="background-color: #eeeeee;">mainline.i3s.unice.fr</span><span style="background-color: #eeeeee;">/</span>mooc/sintel.mp4"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="background-color: #eeeeee;">mainline.i3s.unice.fr</span><span style="background-color: #eeeeee;">/</span>mooc/sintel.webm"</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://<span style="background-color: #eeeeee;">mainline.i3s.unice.fr</span><span style="background-color: #eeeeee;">/</span>mooc/sintel-captions.vtt"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"captions"</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Closed Captions"</span><span class="pln"> </span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div>


Notice that the `<track>` element at line 9 has an attribute named `kind` that indicates the type of the track that is included. Possible values are: `subtitles`, `captions`, `descriptions`, `chapters` or `metadata`.

 The `<track>` element also has an attribute `default` that indicates that we want this track to be displayed by default when reading the video.

We also used  an attribute named `crossorigin` that is necessary just to run this demo, as it is required by the server that hosts the video from this example.


#### Multiple tracks may be included in a video element

Multiple tracks are needed to support different langages, video captions for the hearing-impaired, subtitles, etc.

Below is an example ([from the specification](https://html.spec.whatwg.org/multipage/media.html#the-track-element)) that includes multiple `<track>` elements (subtitles for three languages and captions only for English):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"brave.webm"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">subtitles</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">brave.en.vtt</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">en</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label</span><span class="pun">=</span><span class="atv">"English"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">captions</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">brave.en.hoh.vtt</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">en</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"English for the Hard of Hearing"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">subtitles</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">brave.fr.vtt</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">fr</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lang</span><span class="pun">=</span><span class="atv">fr</span><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label</span><span class="pun">=</span><span class="atv">"Français"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">subtitles</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">brave.de.vtt</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang</span><span class="pun">=</span><span class="atv">de</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lang</span><span class="pun">=</span><span class="atv">de</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label</span><span class="pun">=</span><span class="atv">"Deutsch"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div>

Note the use of some new attributes in the `<track>` element:

+ `label`: the label value will be displayed in the GUI control that is included in the default HTML5 video player,
+ `srclang`:  gives the language for the text track data. The value must be a valid [BCP 47 language tag](https://tools.ietf.org/html/bcp47). This attribute must be present if the [element's `kind` attribute](https://tinyurl.com/y42aldg6) is in the [`subtitles` state](https://www.w3.org/TR/html5/embedded-content-0.html#attr-track-kind-subtitles).


#### External resources

+ From the HTML specification: [The track element](https://html.spec.whatwg.org/multipage/media.html#the-track-element)
+ From the W3C specification: [WebVTT: The Web Video Text Tracks Format](https://www.w3.org/TR/webvtt1/)
+ From MDN's Web Docs: [WebVTT](https://tinyurl.com/yco5lr7y) and [Adding captions and subtitles to HTML5 video](https://tinyurl.com/y2lokg9k)
+ An article from 3playmedia: How to create a WebVTT file


#### Knowledge check 2.3.1

1. What is the name of the element we must include inside a `<video>` element, in order to display captions and subtitles? Just type the name of the element, without &lt; or &gt; characters.

  Ans: track<br>
  Explanation: One or more `<track>` elements can be used.


### 2.3.2 The WebVTT format

The "[WebVTT: The Web Video Text Tracks Format](http://dev.w3.org/html5/webvtt/)" defines files that contain text for captions and subtitles, and much more... The WebVTT files are used with the src attribute of the `<track>` element, that can be used inside a `<video>`...`</video>`.

In [the JsBin example presented in the previous section](https://jsbin.com/bewuyuc/4/edit?html,output), we used a file called `sintel-captions.vtt`:

<div class="source-code" style="line-height: 23.2727279663086px;"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln">&nbsp;</span><span class="atn">height</span><span class="pun">=</span><span class="atv">"272"</span><span class="pln">&nbsp;</span><span class="atn">width</span><span class="pun">=</span><span class="atv">"640"</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">poster</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/q1fx20VZ-640.jpg"</span><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span><span class="pln"></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">controls</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;...</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr<span style="background-color: #eeeeee;">/mooc</span>/<strong>sintel-captions.vtt</strong>"</span><span class="pln"></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"captions"</span><span class="pln">&nbsp;</span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Closed Captions"</span><span class="pln">&nbsp;</span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div>

And here is an extract of the corresponding [sintel-captions.vtt](https://mainline.i3s.unice.fr/mooc/sintel-captions.vtt) file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">02.042</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">drumbeat</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">07.167</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">12.025</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">plaintive violin solo playing</span><span class="pun">)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">15.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">18.183</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">wind whistling</span><span class="pun">)</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">24.167</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">27.025</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">orchestra music swells</span><span class="pun">)</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">43.033</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">43.192</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">weapons clash</span><span class="pun">)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">44.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">44.175</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">gasps</span><span class="pun">)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">44.183</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">45.158</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">grunts</span><span class="pun">)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">45.167</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">47.058</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">groaning</span><span class="pun">)</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">54.192</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">55.150</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">blade rings</span><span class="pun">)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">55.158</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">57.008</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">bellowing</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">57.017</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">58.067</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">grunting</span><span class="pun">)</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">59.075</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">00.133</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">panting</span><span class="pun">)</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">05.108</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">06.125</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">cries </span><span class="kwd">out</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> agony</span><span class="pun">)</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">08.050</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">09.058</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">panting</span><span class="pun">)</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">12.092</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">13.142</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">panting</span><span class="pun">)</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">14.017</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">18.125</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">orchestra plays ominous low notes</span><span class="pun">)</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">31.058</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">35.133</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">(</span><span class="pln">plaintive violin solo returns</span><span class="pun">)</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">46.158</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">49.058</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> blade has a dark past</span><span class="pun">.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">51.092</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">54.108</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="typ">It</span><span class="pln"> has shed much innocent blood</span><span class="pun">.</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">57.083</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">02</span><span class="pun">:</span><span class="lit">00.000</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="typ">You</span><span class="str">'re a fool for traveling alone </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str"> so completely unprepared. </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">00:02:01.100 --&gt; 00:02:03.033</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">You'</span><span class="pln">re lucky your blood</span><span class="str">'s still flowing.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="str">00:02:04.183 --&gt; 00:02:06.075</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">Thank you.</span></li>
</ol></div>

This format is rather simple, but we still recommend reading [this excellent article from Mozilla Developer Network](https://tinyurl.com/y3sxj9a3) that explains in detail all the different options.

Each "element" in this file has a starting and ending time, plus a value (the text that will be displayed), followed by a blank line (blank lines are separators between elements).

__Each element is called "a cue"__, and may optionally have an ID that will be useful when using the track element JavaScript API, in particular the `getCueById()` method of `TextTrack` objects. How to use these will be taught in the "advanced HTML5" course, soon on W3Cx

Example of numeric IDs:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="lit">9</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">21.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">22.000</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">to hear </span><span class="kwd">from</span><span class="pln"> </span><span class="str">&lt;u&gt;</span><span class="pln">you</span><span class="pun">&lt;/</span><span class="pln">u</span><span class="pun">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">10</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">22.500</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">25.000</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="typ">We</span><span class="pln"> want to hear what inspires you </span><span class="kwd">as</span><span class="pln"> a developer</span></li>
</ol></div>

IDs may also be defined as strings, and values can use HTML as well:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="typ">Opening</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">00.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">30.000</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="typ">Welcome</span><span class="pln"> to </span><span class="kwd">our</span><span class="pln"> </span><span class="str">&lt;i&gt;</span><span class="pln">nice film</span><span class="pun">&lt;/</span><span class="pln">i</span><span class="pun">&gt;</span></li>
</ol></div>

The displayed text can span multiple lines, but blank lines are not allowed, as they would be interpreted as a separator:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">57.083</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">02</span><span class="pun">:</span><span class="lit">00.000</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">&lt;p&gt;</span><span class="typ">You</span><span class="str">'re a fool for traveling alone&lt;/p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="str">&lt;p&gt;so completely unprepared.&lt;/p&gt;</span></li>
</ol></div>


#### External resource:

+ An unofficial [Live WebbVTT format](https://quuz.org/webvtt/)


#### Knowledge check 2.3.2

1. What is a CUE in a WebVTT file?<br/>
  a. A subtitle<br/>
  b. The name of the subtitle or caption text displayed at a given time<br/>
  c. A starting time, an ending time and a textual value<br/>
  d. A timestamp<br/>

  Ans: 





### 2.3.2 The WebVTT format





### 2.3.3 Adding subtitles to a video





### 2.3.4 Styling captions





### 2.3.5 Chapters





### 2.3.6 Tools for creating WebVTT files





### 2.3.7 The <track> JavaScript API





### 2.3.8 Enhanced HTML5 video players





### 2.3.9 Discussion and projects






