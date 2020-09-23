# Week 2: HTML5 Multimedia


## 2.3 Subtitles and closed captions


### 2.3.0 Lecture Notes

+ [The `<track>` element](#231-html5-captioning)
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

+ [The `WebVTT` format](#232-the-webvtt-format)
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

+ [Adding subtitles to a video](#233-adding-subtitles-to-a-video)
  + required a video on one of the formats/codecs supported by the browsers you target; e.g., `H624` and `webm`
  + video encoding software: [Handbrake](https://handbrake.fr/), [Super](https://www.erightsoft.com/SUPER.html), online video encoding services, such as [amara](https://amara.org/en/)

+ [Styling captions](#234-styling-captions)
  + __line:5%__: vertical position at a line 5% of the height of the video viewport (located at the top of the video, proportional to its vertical size)
  + __position:5% align:start__: regular location at the bottom of the video, the start of the sentence will be located at 5% of the width of the video, i.e., near the left side
  + __position:95% align:end__: regular location at the bottom of the video, the end of the sentence will be at 95% of the horizontal width of the video
  + __size:33%__: The size of each line will be one third of the size of the video (displayed in multiple lines)
  + use of `<b>`, `<i>`, `<u>` for styling subtitles / captions
  + CSS rules example

    <div class="source-code"><ol class="linenums">
    <li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;c.myclass&gt;</span><span class="pln">This cue contains the class "myclass". </span></li>
    <li class="L1" style="margin-bottom: 0px;"><span class="pln">Browsers that support ::cue CSS should make it red.</span><span class="tag">&lt;/c&gt;</span></li>
    </ol></div>

    + `::cue` pseudo element selector: used to match "cues" in the webVTT file
    + add parenthesis and a secondary CSS selector to match cues that have a particular id, or a particular CSS class
  + `<v>` element
    + voicing for styling
    + distinguishing different voices w/ different color
    + e.g., `<v Tarzan>Me Tarzan...` & `<v Jane>That would make me Jane`

+ [Chapter in subtitles/captions](#235-chapters)
  + generate a custom navigation menu
  + `kind=chapters` in `<track>` element
  + `Chapter x`, `Ending` & `Greetings` in WebVTT file
  + e.g., `<track id="nav" src="webvtt_talk_navigation.vtt" kind="chapters" srclang="en">`

+ [Tools to create WebVTT files](#236-tools-for-creating-webvtt-files)
  + converting from other formats
  + creating subtitles/captions from scratch
  + enhanced HTML5 video player using `<video>`, `<source>` & `<track>` elements




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



### 2.3.3 Adding subtitles to a video

Let's look at a simple example. First, you need a video on one of the formats/codecs supported by the browsers you target. A recommended codec is `H264`, but other formats, such as `webm`, may have some advantages if the browser supports them. For example, webm allows the video to start playing after a much shorter buffering time. In other words, try if possible to provide the video encoded with more than one codec.

For this, use any sort of open source, free or commercial video encoding software, such as [Handbrake](https://handbrake.fr/) (free, open source) or [Super](https://www.erightsoft.com/SUPER.html) (free). There are also online video encoding services, and you can even upload your video to YouTube, let it encode your video in several resolutions and codecs, and use a browser extension such as [Video DownloadHelper](https://addons.mozilla.org/fr/firefox/addon/video-downloadhelper/) (for Firefox) to download the video in your chosen formats.

So, let's suppose you have a video like the one below (we included it on YouTube for practical reasons). This video has subtitles (you can activate them in the YouTube player), but the goal of this lesson is to explain how we made them without using the YouTube embedded tools, which do not allow export the subtitle file to be exported in the webVTT format.

<a href="https://youtu.be/wdnqBfwI2p0" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=150/>
</a><br/>

And you've also got it in `mp4/H264` and in `webm` formats. Here is how you can embed it in your page using the video element:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myVideo"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">500</span><span class="pln"> </span><span class="atn">controls</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln">&nbsp;&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"videos/SameOldSongAndDanceRogerLathaudPart1MidRes.mp4"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="tag">&lt;source</span><span class="pln">&nbsp; &nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">"videos/SameOldSongAndDanceRogerLathaudPart1MidRes.webm"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"videos/subtitles.vtt"</span><span class="pln">&nbsp; &nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind</span><span class="pun">=</span><span class="atv">"subtitles"</span><span class="pln">&nbsp;srclang="en"&nbsp;</span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span><span class="pln"> </span></li>
</ol></div>

At line 9, we added a <track> element to add English subtitles, as the guitar teacher there is speaking in French. We will now explain how we created this subtitle track.


#### Adding subtitles to the video

Now, we need to create a WebVTT file for this video. How can we synchronize an English translation of what the guitar teacher says in French?

Many tools - both free and commercial - are available to add subtitles to a video. Most are native applications you need to install on your computer. However, a free and very practical tool is available for doing this 100% in a Web browser: [amara](https://amara.org/en/).

Go to the above Web site, click on the "subtitle a video" link, then follow the different tutorials/instructions. It will ask for a YouTube URL, so it's better to first upload your video to YouTube (even in private mode). Once you have entered the URL of your video, you will have an online subtitles/caption editor. Enter your subtitles and sync them until you are happy with the results.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 35vw;"
    onclick="window.open('https://tinyurl.com/y3rcrvpb')"
    src    ="https://tinyurl.com/y5qp8n89"
    alt    ="universalsubtitles"
    title  ="universalsubtitles"
  />
</figure>


Once your subtitles/captions are ok, you will be able to upload them to YouTube, or -this is what we wanted first- download them as WebVTT format:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y3rcrvpb')"
    src    ="https://tinyurl.com/yxrko75l"
    alt    ="download subtitles"
    title  ="download subtitles"
  />
</figure>


#### Try your subtitled/captioned video

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y3rcrvpb')"
    src    ="https://tinyurl.com/y2cyavb5"
    alt    ="subtitled/captioned video"
    title  ="subtitled/captioned video"
  />
</figure>


### 2.3.4 Styling captions

In this section, we will look at different possibilities for styling and positioning  the text displayed as captions/subtitles while playing a video.

This [example on JSBin](https://output.jsbin.com/lopudu) shows how we can do that (look at the HTML in JSBin). ([Local Example - Styling Cation](src/2.3.4-example1.html))

The WebVTT file is shown below. Notice the new attributes that have been added on the right end of the duration values:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">05.000</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="typ">These</span><span class="pln"> captions test some features of the </span><span class="typ">WebVTT</span><span class="pln"> formats </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">06.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">10.000</span><strong><span class="pln"> line</span><span class="pun">:</span><span class="lit">5</span><span class="pun">%</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue </span><span class="kwd">is</span><span class="pln"> positioned at the top of the video</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">11.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">15.000</span><strong><span class="pln"> position</span><span class="pun">:</span><span class="lit">5</span><span class="pun">%</span><span class="pln"> align</span><span class="pun">:</span><span class="pln">start</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue </span><span class="kwd">is</span><span class="pln"> positioned at the left side of the video</span><span class="pun">.</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">16.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">20.000</span><span class="pln"> position</span><span class="pun">:</span><span class="lit">95</span><span class="pun">%</span><strong><span class="pln"> align</span><span class="pun">:</span><span class="kwd">end</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="typ">And</span><span class="pln"> </span><span class="kwd">this</span><span class="pln"> one ate the right side</span><span class="pun">.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">21.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">25.000</span><strong><span class="pln"> size</span><span class="pun">:</span><span class="lit">33</span><span class="pun">%</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue </span><span class="kwd">is</span><span class="pln"> only a third of the width of the video</span><span class="pun">,</span><span class="pln"> hence the multiple line breaks</span><span class="pun">.</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">26.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">30.000</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue contains </span><strong><span class="str">&lt;b&gt;</span></strong><span class="pln">bold</span><strong><span class="pun">&lt;/</span><span class="pln">b</span><span class="pun">&gt;</span></strong><span class="pln"> text</span><span class="pun">.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">31.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">35.000</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue contains </span><strong><span class="str">&lt;i&gt;</span></strong><span class="pln">italic</span><strong><span class="pun">&lt;/</span><span class="pln">i</span><span class="pun">&gt;</span></strong><span class="pln"> text</span><span class="pun">.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">36.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">40.000</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue contains </span><strong><span class="str">&lt;u&gt;</span></strong><span class="pln">underlined</span><strong><span class="pun">&lt;/</span><span class="pln">u</span><span class="pun">&gt;</span></strong><span class="pln"> text</span><span class="pun">.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">41.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">45.000</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue contains </span><strong><span class="str">&lt;b&gt;&lt;i&gt;&lt;u&gt;</span></strong><span class="pln">bold</span><span class="pun">,</span><span class="pln"> italic</span><span class="pun">,</span><span class="pln"> underlined</span><strong><span class="pun">&lt;</span><span class="str">/u&gt;&lt;/</span><span class="pln">i</span><span class="pun">&gt;&lt;/</span><span class="pln">b</span><span class="pun">&gt;</span></strong><span class="pln"> text</span><span class="pun">.</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">46.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">50.000</span></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pun">&lt;</span><span class="pln">c</span><span class="pun">.</span><span class="pln">myclass</span><span class="pun">&gt;</span></strong><span class="typ">This</span><span class="pln"> cue contains the </span><span class="kwd">class</span><span class="pln"> </span><span class="str">"myclass"</span><span class="pun">.</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="typ">Browsers</span><span class="pln"> that support </span><span class="pun">::</span><span class="pln">cue CSS should make it red</span><span class="pun">.<strong>&lt;/</strong></span><strong><span class="pln">c</span><span class="pun">&gt;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">51.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">55.000</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">The</span><span class="pln"> following cue contains two voices</span><span class="pun">.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="typ">Tarzan</span><span class="pln"> should be blue </span><span class="kwd">and</span><span class="pln"> </span><span class="typ">Jane</span><span class="pln"> green</span><span class="pun">.</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">56.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">00.000</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Tarzan</span><span class="pun">&gt;</span><span class="typ">Me</span><span class="pln"> </span><span class="typ">Tarzan</span><span class="pun">...</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Jane</span><span class="pun">&gt;</span><span class="typ">That</span><span class="pln"> would make me </span><span class="typ">Jane</span><span class="pun">!</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">bigtext</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">01.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">05.000</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue has a unique id</span><span class="pun">.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">Using</span><span class="pln"> CSS</span><span class="pun">,</span><span class="pln"> its font size should be </span><span class="lit">150</span><span class="pun">%.</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">06.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">10.000</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="typ">The</span><span class="pln"> </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">06.333</span><span class="pun">&gt;</span><span class="pln">text </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">06.666</span><span class="pun">&gt;</span><span class="kwd">in</span><span class="pln"> </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">07.000</span><span class="pun">&gt;</span><span class="kwd">this</span><span class="pln"> </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">07.333</span><span class="pun">&gt;</span><span class="pln">cue </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">07.666</span><span class="pun">&gt;</span><span class="pln">should </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">08.000</span><span class="pun">&gt;</span><span class="pln">grow</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">08.333</span><span class="pun">&gt;</span><span class="pln">one </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">08.666</span><span class="pun">&gt;</span><span class="pln">word </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">09.000</span><span class="pun">&gt;</span><span class="pln">at </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">09.333</span><span class="pun">&gt;</span><span class="pln">a </span><span class="pun">&lt;</span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">09.666</span><span class="pun">&gt;</span><span class="pln">time</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">11.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">15.000</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="typ">That</span><span class="str">'s it! For now...</span></li>
</ol></div>


#### How to position the subtitles

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/yy4aaax5" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y44rrucw" 
      alt  ="This cue is only a third if the width of this video, hence the multiple line breaks." 
      title="This cue is only a third if the width of this video, hence the multiple line breaks."
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y6jlz9jc" 
      alt  ="This cue is positioned at the top of the video." 
      title="This cue is positioned at the top of the video."
    >
  </a>
</div>


The video example tests nearly all the possibilities for positioning subtitles/captions, styling (using HTML element wrapping with `<b>`, `<i>`,  etc.), voicing (subtitles corresponding to different characters will be displayed in different colors) and CSS styling.

It is possible to locate the cues in the video viewport using absolute or relative values. The attributes that position the text are located on the same line as the cue definition, like at line 9 of the previous WebVTT example file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">11.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">15.000</span><strong><span style="color: #ff0000;"><span class="pln"> position</span><span class="pun">:</span><span class="lit">5</span><span class="pun">%</span><span class="pln"> align</span><span class="pun">:</span><span class="pln">start</span></span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="typ">This</span><span class="pln"> cue </span><span class="kwd">is</span><span class="pln"> positioned at the left side of the video</span><span class="pun">.</span></li>
</ol></div>

There are several possible values:

+ __line:5%__ means "vertical position at a line 5% of the height of the video viewport (it will be located at the top of the video, proportional to its vertical size).
+ __position:5% align:start__ means "regular location at the bottom of the video, the start of the sentence will be located at 5% of the width of the video", i.e., near the left side.
+ __position:95% align:end__ means "regular location at the bottom of the video, the end of the sentence will be at 95% of the horizontal width of the video".
+ __size:33%__ The size of each line will be one third of the size of the video. Since the sentence won't fit, it will be displayed in multiple lines.

And so on. Please look at the video as it is self-explanatory.


#### Use of `<b>`, `<i>`, `<u>` for styling subtitles / captions

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy4aaax5')"
    src    ="https://tinyurl.com/yyarrfuq"
    alt    ="Using voicing for styling"
    title  ="Using voicing for styling"
  />
</figure>


#### Using CSS classes for styling

It is possible to style using CSS classes as part of a cue value, using the `<c>` element. You can specify the CSS class that should be applied by adding "." followed by the name of your CSS class. Here is an example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;c.myclass&gt;</span><span class="pln">This cue contains the class "myclass". </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">Browsers that support ::cue CSS should make it red.</span><span class="tag">&lt;/c&gt;</span></li>
</ol></div>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy4aaax5')"
    src    ="https://tinyurl.com/y48bxcfm"
    alt    ="Using voicing for styling"
    title  ="Using voicing for styling"
  />
</figure>


CSS rules used in this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;style</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/css"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">::</span><span class="pln">cue</span><span class="pun">(.</span><span class="pln">myclass</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> color</span><span class="pun">:</span><span class="pln"> red</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">::</span><span class="pln">cue</span><span class="pun">(</span><span class="pln">v</span><span class="pun">[</span><span class="pln">voice</span><span class="pun">=</span><span class="str">"Tarzan"</span><span class="pun">])</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> color</span><span class="pun">:</span><span class="pln"> blue</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">::</span><span class="pln">cue</span><span class="pun">(</span><span class="pln">v</span><span class="pun">[</span><span class="pln">voice</span><span class="pun">=</span><span class="str">"Jane"</span><span class="pun">])</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> color</span><span class="pun">:</span><span class="pln"> green</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">::</span><span class="pln">cue</span><span class="pun">(#</span><span class="pln">bigtext</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> font</span><span class="pun">-</span><span class="pln">size</span><span class="pun">:</span><span class="pln"> </span><span class="lit">150</span><span class="pun">%;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/style&gt;</span></li>
</ol></div>

The `::cue` pseudo element selector is used to match "cues" in the webVTT file. You add parenthesis and a secondary CSS selector to match cues that have a particular id, or a particular CSS class, etc. Look at the CSS above and at the extract from the webVTT file, play the video, you will understand how this works...

Support differs from one browser to another, see [this compatibility table](https://caniuse.com/#feat=webvtt) (from CanIuse). Notice that most of the enhanced players presented further on in the course provide full support.


#### Using voicing for styling: the `<v>` element

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yy4aaax5')"
    src    ="https://tinyurl.com/yyv7y67j"
    alt    ="Using voicing for styling"
    title  ="Using voicing for styling"
  />
</figure>

Using the `<v>` tag, you will distinguish different voices that should be displayed in different colors (depending on the HTML5 video player implementation). See the CSS presented in the previous section to see how to specify the colors for the different voices.

Example source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">56.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">04.000</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Tarzan</span><span class="pun">&gt;</span><span class="typ">Me</span><span class="pln"> </span><span class="typ">Tarzan</span><span class="pun">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&lt;</span><span class="pln">v </span><span class="typ">Jane</span><span class="pun">&gt;</span><span class="typ">That</span><span class="pln"> would make me </span><span class="typ">Jane</span><span class="pun"></span></li>
</ol></div>


#### Knowledge check 2.3.4

1. Is it possible to use CSS for styling subtitles or captions? (Yes/No)

  Ans: Yes <br/>
  Explanation: Yes, CSS can be used since subtitles and captions can be pure HTML with id and class attributes. They can also include spans, bold, italic markers, etc.


### 2.3.5 Chapters

Adding chapters is very similar to adding subtitles/captions. Look at line 5 in the code below, where we use an extra `<track>` element with a `kind="chapters"` attribute.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">poster</span><span class="pun">=</span><span class="atv">"webvtt_talk.png"</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">width</span><span class="pun">:</span><span class="lit">100</span><span class="pun">%</span><span class="atv">"</span><span class="pln"> </span><span class="atn">preload</span><span class="pun">=</span><span class="atv">"metadata"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"webvtt_talk.webm"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"webvtt_talk.mp4"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"webvtt_talk.ogv"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"nav"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"webvtt_talk_navigation.vtt"</span><span class="pln"> </span><strong><span class="atn">kind</span><span class="pun">=</span><span class="atv">"chapters"</span></strong><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"cc"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"webvtt_talk_captions.vtt"</span><span class="pln"> </span><span class="atn">kind</span><span class="pun">=</span><span class="atv">"captions"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label</span><span class="pun">=</span><span class="atv">"captions"</span><span class="pln"> </span><span class="atn">srclang</span><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div>

Here is an example of WebVTT files with defined chapters. Each "CUE" at lines 3, 7, 11, ... can bear any name. We use "Chapter 1, Chapter 2, Ending, etc." but you are free to name them as you choose.

What makes them special is that the track has an attribute `kind="chapters"`. 

It's also easy to process them, and for example, to generate a custom navigation menu, using the `<track>` JavaScript API (explained later in this section).

Example of a WebVTT file that defines chapters:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">WEBVTT FILE</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span style="color: #660066;" color="#660066">Chapter</span>&nbsp;</span><span class="lit">1</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">00.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">10.700</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">Title</span><span class="pln"> </span><span class="typ">Slide</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="typ">Chapter</span><span class="pln">&nbsp;</span><span class="lit">2</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">10.700</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">47.600</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="typ">Introduction</span><span class="pln"> </span><span class="kwd">by</span><span class="pln"> </span><span class="typ">Naomi</span><span class="pln"> </span><span class="typ">Black</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="typ">Chapter</span><span class="pln">&nbsp;</span><span class="lit">3</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">00</span><span class="pun">:</span><span class="lit">47.600</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">50.100</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="typ">Impact</span><span class="pln"> of </span><span class="typ">Captions</span><span class="pln"> on the </span><span class="typ">Web</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">Chapter</span><span class="pln">&nbsp;</span><span class="lit">4</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">01</span><span class="pun">:</span><span class="lit">50.100</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">03</span><span class="pun">:</span><span class="lit">33.000</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="typ">Requirements</span><span class="pln"> of a </span><span class="typ">Video</span><span class="pln"> text format</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"><span style="color: #660066;" color="#660066">Ending</span></span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">03</span><span class="pun">:</span><span class="lit">33.000</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">04</span><span class="pun">:</span><span class="lit">57.766</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="typ">Simple</span><span class="pln"> </span><span class="typ">WebVTT</span><span class="pln"> file</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span style="color: #660066;" color="#660066">Greetings</span>&nbsp;</span><span class="lit">6</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">00</span><span class="pun">:</span><span class="lit">04</span><span class="pun">:</span><span class="lit">57.766</span><span class="pln"> </span><span class="pun">--&gt;</span><span class="pln"> </span><span class="lit">00</span><span class="pun">:</span><span class="lit">06</span><span class="pun">:</span><span class="lit">16.666</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="typ">Styled</span><span class="pln"> </span><span class="typ">WebVTT</span><span class="pln"> file</span></li>
</ol></div>

Examples of what you can achieve using chapters (more details are shown in the [W3Cx HTML5 Apps and Games course](https://www.edx.org/course/html5-apps-and-games)).

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/yyurmkx4" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/yy8eglzq" 
      alt  ="jwplayer and chapters" 
      title="jwplayer and chapters"
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/yxa7e2ng" 
      alt  ="sublimevideo player takes into account chapters" 
      title="sublimevideo player takes into account chapters"
    >
  </a>
</div>



### 2.3.6 Tools for creating WebVTT files

Many tools are available to make and edit HTML5 video and caption/subtitles:

+ __Tools for converting existing file formats to  WebVTT files__, such as the `.srt` format, which is popular in the DivX/AVI/Mkv scene. This [article](https://tinyurl.com/y3cug5zk) reviews 3 of them, but there are many more. Do a quick Web search and you will get plenty of results.
+ __Tools for creating subtitles/captions from scratch. Use these to generate a WebVTT file.__ You can embed the `<track>` element in your own videos, on your own Web pages, or upload the WebVTT file to YouTube.  We recommend [amara](https://amara.org/en/). It's a free online tool that is very easy to use. Check the "add subtitles/captions to your video" unit of this course. 
+ __Enhanced HTML5 video players__ that use the `<video>`, `<source>` and `<track>` elements under the hood. They also provide many extra features, including __support for subtitle/caption formats other than WebVTT (by converting on the fly)__.


### 2.3.7 The <track> JavaScript API





### 2.3.8 Enhanced HTML5 video players





### 2.3.9 Discussion and projects






