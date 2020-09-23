# Week 2: HTML5 Multimedia


## 2.3 Subtitles and closed captions


### 2.3.0 Lecture Notes





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

What is the name of the element we must include inside a `<video>` element, in order to display captions and subtitles? Just type the name of the element, without < or > characters.



### 2.3.2 The WebVTT format





### 2.3.3 Adding subtitles to a video





### 2.3.4 Styling captions





### 2.3.5 Chapters





### 2.3.6 Tools for creating WebVTT files





### 2.3.7 The <track> JavaScript API





### 2.3.8 Enhanced HTML5 video players





### 2.3.9 Discussion and projects






