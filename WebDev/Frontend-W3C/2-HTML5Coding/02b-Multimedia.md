# Week 2: HTML5 Multimedia


## 2.2 Streaming multimedia content

### 2.2.0 Lecture Notes

+ [The `<video>` element](#221-the-video-element)
	+ HTML5 Flash Killers: `<video>` and `<canvas>` elements
	+ `<video>` element: a DOM member
		+ CSS styling applied
		+ manipulation w/ the DOM API
	+ example code

		<div class="source-code"><ol class="linenums">
		<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"320"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"240"</span><span class="pln"> </span><span class="atn">controls</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;</span></li>
		<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"movie.mp4"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
		<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"movie.ogg"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/ogg"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
		<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Your browser does not support the </span><span class="tag">&lt;video&gt;</span><span class="pln"> element.</span></li>
		<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
		</ol></div>

		+ `controls` attribute: a control panel displayed with play/stop/volume/progress widgets
		+ usually browser using the first format it recognizes, but some browsers choosing a "preferred" format
	+ unable to embed a YouTube or DailyMotion video using the `<video>` element
		+ using rather complex techniques to prevent people from using them with the `<video>` element
		+ embedding an `<iframe>` to render the HTML5 videos in one's own Web site
		+ usually an "embed" button close to the videos that prompts people with some HTML code that you can copy and paste for embedding
		+ YouTube example: `<iframe width="560" height="315" src="https://www.youtube.com/watch?v=9NTrwrfI-X4" frameborder="0" allowfullscreen></iframe>`

+ [Most common attributes of `<video>` element](#most-useful-attributes-of-the-video-element)
	+ `src`: source of the video.
	+ `width` and `height`:
		+ size of the video. 
		+ default: width and height of the video if unspecified
		+ only one dimension specified: adjusting the size of the unspecified dimension to preserve the aspect ratio of the video
	+ `controls`: display its own controls for video playback and volume
	+ `poster`:
		+ specify an image that the browser will use while video is being downloaded, or until the user starts playing the video
		+ not specified: 1st frame of the video used
	+ `autoplay` (Boolean): browser to start playing the video automatically as soon as the page is ready
	+ `preload`:
		+ used when autoplay not used
		+ telling the browser what to do before a user plays a video
		+ hint: the browser may ignore it
		+ `autoplay` and `preload` mutually exclusive, if both are present, then preload is ignored.
		+ Possible values:
			+ `none`: do nothing. no video downloaded in background before a user or a call to the play() method starts playing the video.
			+ `metadata`: download metadata, such as length of the video or its format.
			+ `auto` (default value): the browser decides, depending on the implementation, and on the kind of connection: wifi, 3G, data roaming etc.
	+ `loop` (Boolean): play the video in loop mode (and it starts again when finished).

+ [Recommendation & Best Practices for `<video>` element](#most-useful-attributes-of-the-video-element)
	+ mobile application or multiple videos in a page
		+ not using `autoplay` attribute
		+ `preload=none` to save bandwidth
	+ `poster` attribute: usually the first non-blank frame of the video if missing
	+ limiting the use of `autoplay` attribute

+ [The `<audio>` element](#222-the-audio-element)
	+ embedding an audio player into a Web page
	+ dedicated for streamed audio
	+ similar to the `<video>` element, both in its use and in its API
	+ reduced version of the `<video>` on attributes, event set and JavaScript API 
	+ using the `controls` attribute in order to render the play/stop, time, volume and progress widgets
	+ text message btw the `<audio>`...`</audio>` tags: displayed if the Web browser doesn't support the <audio> element
	+ several `<source>`...`</source>` elements: link to different audio formats for the same file

+ [Most common attributes of `<audio>` element](#attributes-of-the-audio-element)
	+ `src`: source of an audio stream.
	+ `controls` (Boolean): display controls for audio playback and volume.
	+ `autoplay`: start playing the audio stream automatically as soon as the page is ready
	+ `preload`: tells the browser what to do before a user plays a sound - please read details in the above table.
	+ `loop`: play the audio stream in loop mode
	+ best practice in regard to `preload` and `autoplay` attributes should be followed as `<video>` element

+ [Styling media palyers](#224-styling-media-players-with-css)
	+ CSS w/ transitions, animations and transforms but not Flash technology
	+ CSS: resizing and rotating a video as mouse hover
		+ pseudo CSS class :`hover` to track `mouseover`event
		+ `transition` property: interpolate the changes in the scale; e.g., `transition: all 0.5s ease-in-out;`
		+ `transform` property: orientation of the video element; e.g., `transform:rotate(-5deg);`
	+ Solutions for full screen video
		+ full screen video: JavaScript modifying CSS properties
			+ resizing and maintaing ratio for full screen
			+ a trendy way to displaying videos
			+ regular video & embedded YouTube
				+ using `<video>` and `<source>` elements
				+ applying JavaScript code to handle the window `resize` event
				+ regular CSS properties `width` and `height` to resize
			+ working on any browser and displayed the whole vidoe
		+ full screen video: pure CSS
			+ cropped video frame than rescaled
			+ zoomed-in video to make video bigger than browser's window
			+ placing the video within `<header>` element w/ transparent and repeated background; e.g., `background-image: url('https://dupontcours.free.fr/IMG/dots.png'),  url('#');` & `background-repeat: repeat, no-repeat;`
			+ video position: origin (top left corner) away from the visible surface w/ 100% surface; e.g., `transform:translateX(-50%) translateY(-50%);` & `min-width:100%; min-height:100%;`
			+ cropped video
		+ full screen video: CSS `viewport` unit
			+ using `viewport` instead of default video size; e.g., `width: 100vw; height: 100vh;`
			+ behave the same as the 1st solution w/ JavaScript
			+ dispalyed the whole video
	+ effecct of `width: 100%; height: 100%`
		+ 100% size of the tag
		+ `<body>` tage w/ `width: 100%;`: the browser windows size, i.e., video always full width
		+ `<body>` tage w/ `height: 100%;`: determined by the size of its children, gorw or shrink according the size of its children
		+ part of the video invisible as the browser window shorter the video height

+ [DOM JavaScript API](#225-control-players-from-javascript)
	+ __mathods__: controlling the behavior, such as play(), pause(), etc.
	+ __properties__:
		+ read/write mode, e.g., volume
		+ read-only mode, e.g., encoding, duration, etc.
	+ __event__:
		+ generated during the lifecycle of the element
		+ processed using JavaScript callbacks
		+ able to send events to control the video player
	+ example:

		<div class="source-code"><ol class="linenums">
		<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">);</span></li>
		<li class="L1" style="margin-bottom: 0px;"><span class="pln">video</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">'video.mp4'</span><span class="pun">;</span></li>
		<li class="L2" style="margin-bottom: 0px;"><span class="pln">video</span><span class="pun">.</span><span class="pln">controls </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
		<li class="L3" style="margin-bottom: 0px;"><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">video</span><span class="pun">);</span></li>
		</ol></div>




### 2.2.1 The `<video>` element

The `<video>` element of HTML5 is one of the two "Flash killers" (the other being the `<canvas>` element). It was designed to replace horrible things like embedded Flash objects that used to be around.


#### Before HTML5, how did we embed videos in a Web page?

Like this!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;object</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"425"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"344"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;param</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"movie"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"https://www.youtube.com/v/9sEI1AUFJKw&amp;hl=en_GB&amp;fs=1&amp;"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;/param&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;param</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"allowFullScreen"</span><span class="pln">&nbsp; &nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"true"</span><span class="tag">&gt;&lt;/param&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;param</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"allowscriptaccess"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"always"</span><span class="tag">&gt;&lt;/param&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;embed</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://www.youtube.com/v/9sEI1AUFJKw&amp;hl=en_GB&amp;fs=1&amp;"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"application/x-shockwave-flash"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">allowscriptaccess</span><span class="pun">=</span><span class="atv">"always"</span><span class="pln"> </span><span class="atn">allowfullscreen</span><span class="pun">=</span><span class="atv">"true"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">width</span><span class="pun">=</span><span class="atv">"425"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"344"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;/embed&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/object&gt;</span></li>
</ol></div>

Indeed, this was the only way to embed a YouTube video (fortunately, YouTube has changed that now). Furthermore, embedding a Flash player made it impossible to watch videos on some mobile platforms (especially Apple devices).


#### With HTML5:

The new way of doing things is a lot better... (please open [this live example at JS Bin](https://tinyurl.com/y2242ym7)). [[Local Example](src/2.2.1-example1.html)]

<video controls="controls" poster="https://bit.ly/2JtB40Q">
	<!-- I have three versions of the video encoded with
	     different codecs.  The browser will automatically
	     choose the first one it knows it can play. -->
	<source src="https://html5doctor.com/demos/video-canvas-magic/video.webm" type="video/webm">
	<source src="https://html5doctor.com/demos/video-canvas-magic/video.ogg" type="video/ogg">
	<source src="https://html5doctor.com/demos/video-canvas-magic/video.mp4" type="video/mp4">
</video><br/><br/>

The source code of this example shows the typical usage of the `<video>` element:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"320"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"240"</span><span class="pln"> </span><span class="atn">controls</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"movie.mp4"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"movie.ogg"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/ogg"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;Your browser does not support the </span><span class="tag">&lt;video&gt;</span><span class="pln"> element.</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div>

Please note that:

+ The `controls` attribute indicates that a control panel with play/stop/volume/progress widgets should be displayed;
+ Usually the browser  will use the first format it recognizes  (in this case, the browser checks whether `mp4` is supported, and if not, it will check for the `ogg` format, and so on). Some browsers may use a different heuristic and choose a "preferred" format.
+ The `<video>` element is a DOM member, so  CSS styling can be applied, as well as manipulation using the DOM API.

You will learn more about the different attributes of the `<video>` element later on in the course...


#### Current browser support for the `<video>` element

The `<video>` element is supported by all major browsers. To get an updated version, [see the related support table from CanIUse](https://tinyurl.com/y9phqxgw).


#### Restriction: you cannot embed a YouTube or DailyMotion video using the `<video>` element

Help! `<video src="my youtube video URL"></video>` does not work! 

<span style="color: magenta; font-weight: bold;">BEWARE</span>: _you cannot directly embed videos from most of the popular social Web sites such as YouTube, Dailymotion, Vimeo, etc. For commercial reasons, and because advertising is automatically  added to the videos, these Web sites do not allow "regular" embedding of their videos._

While they use HTML5 to render their videos, these hosting sites (YouTube, etc.) use rather complex techniques in order to prevent you from using them with the `<video>` element. Instead, you often need to embed an `<iframe>` that will render the HTML5 videos in your Web site, and of course, the advertising that comes along with them.

Usually you have an "embed" button close to the videos that prompts you with some HTML code that you can copy and paste for embedding.

__An example using YouTube:__

Here is the HTML code you need to copy and paste in order to embed a video (in this case, a tutorial that tells you how to embed a YouTube video):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;iframe</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"560"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"315"</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://www.youtube.com/watch?v=9NTrwrfI-X4"</span><span class="pln"> </span><span class="atn">frameborder</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">allowfullscreen</span><span class="tag">&gt;&lt;/iframe&gt;</span></li>
</ol></div>

The YouTube video embedded in this page by the above code: it's HTML5 but it's not a `<video>` element directly inserted in the HTML of this page, it's an `<iframe>`:

<a href="https://youtu.be/9NTrwrfI-X4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=150/>
</a><br/>


#### External resources

+ From W3C's specification: [The video element](https://tinyurl.com/y3qh8qtr)
+ MDN's Web Docs:  [`<video>`: The Video Embed element](https://tinyurl.com/k8qo497)
+ From Apple's developer site: [Safari HTML5 audio and video guide](https://tinyurl.com/y4fp4nyw).
+ Article from HTML5 Rocks: [HTML5 video](https://tinyurl.com/leuv9j3)
+ [HTML5 Video Player: How to Embed a Video in HTML](https://tinyurl.com/y4ae67wv)


#### Knowledge check 2.2.1

1. The video element is like any other HTML element: I can style it using CSS and interact programmatically with it using the JavaScript DOM API. (True/False)

  Ans: True<br/>
	Explanation: Indeed, the `<video>` element is, like other HTML elements, a first class citizen of the DOM and can be styled using CSS or manipulated using the JavaScript DOM API.


### 2.2.2 The `<audio>` element

HTML5 audio is composed of several layers:

+ The `<audio>` element is useful for embedding an audio player into a Web page. It is dedicated for __streamed audio__. It is very similar to the `<video>` element, both in its use and in its API.
+ The Web Audio API is designed for musical applications and for adding sound effects to games. This pure JavaScript API supports manipulation of sound samples (loops, etc.), music synthesis and sound generation (oscillators, etc.). It also comes with a set of predefined sound processing modules (reverb, delay, etc.).

<div style="border: 1px solid red; padding: 10px;">This course will&nbsp;focus on the <span style="font-family: 'courier new', courier;">&lt;audio&gt;</span> element. We present the <a href="https://www.w3.org/TR/webaudio/" target="_blank">Web Audio API</a>&nbsp;and<span style="line-height: 1.6;">&nbsp;other advanced HTML5 features in the</span> <a href="https://www.edx.org/course/html5-apps-and-games" target="_blank">W3Cx HTML5 Apps and Games course</a><span style="line-height: 1.6;"></span><span style="line-height: 1.6;">.</span></div>

The attributes, event set and JavaScript API  of the `<audio>` element are just a "reduced" version of the ones from the `<video>` element, and here we will only address the differences and peculiarities.


#### The `<audio>` element, basic usage

Here is a simple example (also available [online example from JSBin](https://jsbin.com/yogojis/edit?html,output)) [Local Example](src/2.2.2-example1.html):

Press play to stream the neigh of a horse: 
<audio controls="controls">
  <source src="https://mainline.i3s.unice.fr/mooc/horse.ogg" type="audio/ogg">
  <source src="https://mainline.i3s.unice.fr/mooc/horse.mp3" type="audio/mp3">
  Your browser does not support the audio element.
</audio>

As you can see, the code is very similar to the basic `<video>` element usage.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>&lt;title&gt;</span><span class="pln">horse song</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span>&lt;/head&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span>&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>&lt;audio</span><span class="pln"> </span><span class="atn">controls</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/horse.ogg"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"audio/ogg"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/horse.mp3"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"audio/mp3"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span></span>Your browser does not support the audio element.</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span></span>Download the audio/video in</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/horse.ogg"</span><span class="tag">&gt;</span><span class="pln">OGG</span><span class="tag">&lt;/a&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>or </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/horse.mp3"</span><span class="tag">&gt;</span><span class="pln">MP3</span><span class="tag">&lt;/a&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>format.</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>&lt;/audio&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span>&lt;/body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


In this example, just as for the `<video>` element, we used the controls attribute in order to render the play/stop, time, volume and progress widgets.

Notice the other similarities: between the `<audio>`...`</audio>` tags, we added a text message that is displayed if the Web browser doesn't support the `<audio>` element, and we used several `<source>`...`</source>` elements that link to different audio formats for the same file. The browser will use the first format it recognizes.


#### External resources

+ From W3C's specification: [The audio element](https://www.w3.org/TR/html52/semantics-embedded-content.html#the-audio-element)
+ From MDN's Web Docs: `<audio>`: [The Embed Audio element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)


#### Knowledge check 2.2.2

1. HTML5 comes with several ways of handling audio - what are they? (2 correct answers)

	a. HTML5 can use flash players<br/>
	b. The WebAudio API<br/>
	c. The <music> element<br/>
	d. The <audio> element<br/>
	e. The JavaScript sound.js library<br/>
	
	Ans: bd, xde<br/>
	Explanation: HTML5 provides the `<audio>` element for streaming audio content, and the WebAudio API for playing samples loaded in memory, for synthesizing music or for real time sound processing.


### 2.2.3 Attributes of `<video>` and `<audio>`

#### Live coding video: usage of the different attributes

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V001400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" width=150/>
</a><br/>

[Transcript](https://tinyurl.com/y3c8fcg6)


#### Most useful attributes of the `<video>` element

Here are the most common attributes you can use with the `<video>` element. They are self explanatory...

+ `src`: source of the video.
+ `width` and `height`: size of the video. If unspecified, the default width and height of the video will be used. If you specify one dimension but not the other, the browser will adjust the size of the unspecified dimension to preserve the aspect ratio of the video.
+ `controls`: If this boolean attribute is present, the browser displays its own controls for video playback and volume.
+ `poster`: This attribute allows you to specify an image that the browser will use while video is being downloaded, or until the user starts playing the video. If this attribute is not specified, the first frame of the video will be used instead.
+ `autoplay`: This attribute asks the browser to start playing the video automatically as soon as the page is ready.
+ `preload`:  The `preload` attribute is used when `autoplay` is not used. It tells the browser what to do before a user plays a video. This attribute is a hint - the browser may ignore it. While `autoplay` and `preload` are mutually exclusive, if both are present, then `preload` is ignored. Possible values:
	+ `none`: do nothing. This saves bandwidth, no video will be downloaded in background before a user or a call to the play() method starts playing the video.
	+ `metadata`: download metadata, such as length of the video or its format.
	+ `auto` (default value): the browser will decide. This will depend on the implementation, and on the kind of connection: wifi, 3G, data roaming etc.
+ `loop`: Another boolean attribute that indicates to play the video in loop mode (and it starts again when finished).

__Be careful if you target mobile applications or if you have multiple videos on the same page__

The `autoplay` attribute is not recommended if your Web site targets mobile applications, as it may consume bandwidth even if the user is not interested in watching the proposed video. If you target mobile devices, we recommend using `preload=none` as well, as the default value for this attribute is `auto`.

__Best practice__: do not use autoplay and add preload="none" if you target mobile devices or if you have multiple audio/video on the same page.  For example, this page contains many audio elements and it does not make sense to have them preload or autoplay.


__About the poster attribute__

If the `poster` attribute is missing, usually the first non-blank frame of the video will be used as the image that is shown when the video is not playing. 

About the `autoplay` attribute for general use

Do not abuse of the `autoplay` attribute. We talked earlier about mobile applications, but even on desktop applications it's usually a bad idea to use it (except for WebCams and for some animations with small video loops, without sound, or for sites like YouTube, with just videos). This is the testimony of a user in this course forum: "_When I'm following the news, I open several headlines in separate tabs. And then all of them start screaming at me with some autoplays. I know this is supposed to make me watch the video, but for me - it makes me close the loud tab and try another source._"

__Best practice__: think twice before using the autoplay attribute, even for desktop applications.


#### Attributes of the `<audio>` element

The attributes you can use with the `<audio>` element are a subset of those available for the `<video>` element. Except for the poster attribute, they are all recognized and have the expected meanings: 

+ `src`: source of an audio stream.
+ `controls`: if this attribute is present, the browser displays its own controls for audio playback and volume.
+ `autoplay`: tells the browser to start playing the audio stream automatically as soon as the page is ready - please read details in the above table.
+ `preload`: tells the browser what to do before a user plays a sound - please read details in the above table.
+ `loop`:  indicates to play the audio stream in loop mode (start again when finished).

As with the `<video>` element, the same best practice in regard to preload and autoplay attributes should be followed.


#### Knowledge check 2.2.3

1. Which of the following statements about the `preload` attribute is correct?

	a. When present, it tells the browser to load multiple multimedia files in advance.<br/>
	b. If this attribute is present, the browser checks if the multimedia content can be loaded from its cache.<br/>
	c. This attribute can take different values that will avoid preloading mutimedia content, or on the contrary, that will tell the browser to preload this content, or tell the browser to preload only some multimedia content metadata.<br/>
	d. If this attribute is present in an audio or video element, the multimedia content is preloaded as soon as the page is loaded.<br/>

	Ans: <span style="color: magenta;">c</span>, xa, xd<br/>
	Explanation: The `preload` attribute can have different values: `none`, `metadata` or `auto`, and will give hints to the browser for preloading multimedia content.


### 2.2.4 Styling media players with CSS

The `<video>` and `<audio>` elements are just like other HTML elements, so CSS can be used for styling, including CSS transitions, animations and transforms (this was not possible with Flash technology).


#### An example of an audio player with some style

You can try this example [online at JSBin](https://jsbin.com/zoquru/2/edit?html,css,output) ([Local Example - Styling Audio player](src/2.2.4-example1.html))

To add some styling to the basic example we saw when we introduced the `<audio>` element, we just add a `<figure>` with two children: an `<img>` and a `<figcaption>`. Inside the `<figcaption>` we add the `<audio>` element from the previous example.

MOVE THE MOUSE POINTER OVER THIS PLAYER'S ELEMENTS! (Effect not shown due to CSS pseudo-class selector)

<figure style="width : 420px;;
    text-align:center; padding : 6px; background : white; margin : 0 11px 0px 0; border :solid 1px #888888; border-radius : 8px ;"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Nokota_Horses.jpg" width="300"> <figcaption style="font-size : .8em; padding : 6px 8px; background : #dddddd; display :block; text-align :center; font-family : georgia, serif; font-style : italic; border-radius : 7px ; color: black;"> Press Play to hear the horse !<br/> <audio controls="controls" style="margin: auto;">
  <source src="https://mainline.i3s.unice.fr/mooc/horse.ogg" type="audio/ogg">
  <source src="https://mainline.i3s.unice.fr/mooc/horse.mp3" type="audio/mp3">
  Your browser does not support the audio element.
</audio> </figcaption></figure><br/>

HTML source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;figure</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"figaudio1"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;img</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"imghorse"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"200"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://upload.wikimedia.org/wikipedia/commons/d/d4/Nokota_Horses.jpg"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp;alt</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="atv">"a horse"</span><span class="tag">/&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;figcaption</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"figcptionaudio1"</span><span class="tag">&gt;</span><span class="pln"> Press Play to hear the horse! </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;audio</span><span class="pln"> </span><span class="atn">controls</span><span class="pun">=</span><span class="atv">"controls"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/horse.ogg"</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"audio/ogg"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/horse.mp3"</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">"audio/mp3"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;Your browser does not support the audio element.</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;Download the audio/video in</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">”https://mainline.i3s.unice.fr/mooc/horse.ogg”</span><span class="tag">&gt;</span><span class="pln">OGG</span><span class="tag">&lt;/a&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;or </span><span class="tag">&lt;a</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">”https://mainline.i3s.unice.fr/mooc/horse.mp3”</span><span class="tag">&gt;</span><span class="pln">MP3</span><span class="tag">&lt;/a&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; format.</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp;&nbsp; &nbsp;&lt;/audio&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;/figcaption&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/figure&gt;</span></li>
</ol></div>


CSS source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">#figaudio1 {</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width </span><span class="pun">:</span><span class="pln"> </span><span class="lit">420px</span><span class="pun">;;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; text</span><span class="pun">-</span><span class="pln">align</span><span class="pun">:</span><span class="pln">center</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; padding </span><span class="pun">:</span><span class="pln"> </span><span class="lit">6px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background </span><span class="pun">:</span><span class="pln"> white</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; margin </span><span class="pun">:</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="lit">11px</span><span class="pln"> </span><span class="lit">0px</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border </span><span class="pun">:</span><span class="pln">solid </span><span class="lit">1px</span><span class="pln"> </span><span class="com">#888888;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border</span><span class="pun">-</span><span class="pln">radius </span><span class="pun">:</span><span class="pln"> </span><span class="lit">8px</span><span class="pln"> </span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">#figcptionaudio1 {</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; font</span><span class="pun">-</span><span class="pln">size </span><span class="pun">:</span><span class="pln"> </span><span class="pun">.</span><span class="lit">8em</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; padding </span><span class="pun">:</span><span class="pln"> </span><span class="lit">6px</span><span class="pln"> </span><span class="lit">8px</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background </span><span class="pun">:</span><span class="pln"> </span><span class="com">#dddddd; </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; display </span><span class="pun">:</span><span class="pln">block</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; text</span><span class="pun">-</span><span class="pln">align </span><span class="pun">:</span><span class="pln">center</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; font</span><span class="pun">-</span><span class="pln">family </span><span class="pun">:</span><span class="pln"> georgia</span><span class="pun">,</span><span class="pln"> serif</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; font</span><span class="pun">-</span><span class="pln">style </span><span class="pun">:</span><span class="pln"> italic</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border</span><span class="pun">-</span><span class="pln">radius </span><span class="pun">:</span><span class="pln"> </span><span class="lit">7px</span><span class="pln"> </span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">#figaudio1 &gt; img {</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background </span><span class="pun">:</span><span class="pln"> </span><span class="com">#eeeeee;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; padding </span><span class="pun">:</span><span class="pln"> </span><span class="lit">5px</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; border </span><span class="pun">:</span><span class="pln"> solid </span><span class="lit">1px</span><span class="pln"> </span><span class="com">#444444;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">/* For audio and img transitions/animation */</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">audio</span><span class="pun">,</span><span class="pln"> </span><span class="com">#figaudio1 &gt; img {</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; transition</span><span class="pun">:</span><span class="pln">all </span><span class="lit">0.5s</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">#figaudio1 &gt; img:hover {</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; box</span><span class="pun">-</span><span class="pln">shadow</span><span class="pun">:</span><span class="pln"> </span><span class="lit">15px</span><span class="pln"> </span><span class="lit">15px</span><span class="pln"> </span><span class="lit">20px</span><span class="pln"> rgba</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0.4</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; transform</span><span class="pun">:</span><span class="pln"> scale</span><span class="pun">(</span><span class="lit">1.05</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">audio</span><span class="pun">:</span><span class="pln">hover</span><span class="pun">,</span><span class="pln"> audio</span><span class="pun">:</span><span class="pln">focus</span><span class="pun">,</span><span class="pln"> audio</span><span class="pun">:</span><span class="pln">active </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; box</span><span class="pun">-</span><span class="pln">shadow</span><span class="pun">:</span><span class="pln"> </span><span class="lit">15px</span><span class="pln"> </span><span class="lit">15px</span><span class="pln"> </span><span class="lit">20px</span><span class="pln"> rgba</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0.4</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; transform</span><span class="pun">:</span><span class="pln"> scale</span><span class="pun">(</span><span class="lit">1.05</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


#### Changing the size of a video on the fly using CSS transforms

__Resizing and rotating a video as the mouse pointer comes over it__

See this [example online](https://tinyurl.com/y3gh2gms) (where you can modify the code on the fly) or just play the following video, and move the mouse pointer in and out of the video while it's playing.

<video id="w3devCampusVideoTransition" controls="controls">
	<!-- I have three versions of the video encoded with
	     different codecs.  The browser will automatically
	     choose the first one it knows it can play. -->
	<source src="https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.webm" type="video/webm">
	<source src="https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.ogg" type="video/ogg">
	<source src="https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4" type="video/mp4">
</video><br/>

This example uses the pseudo CSS class :hover in order to track the `mouseover` event. On mouseover, it uses a CSS `transition` property that interpolates the changes in the scale and orientation of the video element (done using a `transform` CSS property).

The corresponding HTML source code is:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><strong><span class="atn">id</span><span class="pun">=</span><span class="atv">"w3devCampusVideo"</span></strong><span class="pln"> </span><span class="atn">autoplay</span><span class="pln"> </span><span class="atn">controls</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.webm</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">video/webm</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.ogg</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">video/ogg</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span class="pun">=</span><span class="atv">video/mp4</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span><span class="pln"> </span></li>
</ol></div>

... and the CSS source code is as follows:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">#w3devCampusVideo {</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width</span><span class="pun">:</span><span class="pln"> </span><span class="lit">300px</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>transition</strong></span><strong><span class="pun">:</span><span class="pln"> all </span><span class="lit">0.5s</span><span class="pln"> ease</span><span class="pun">-</span><span class="kwd">in</span><span class="pun">-</span><span class="kwd">out</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">#w3devCampusVideo<strong>:hover</strong>&nbsp;{ </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width</span><span class="pun">:</span><span class="lit">400px</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; transform</span><span class="pun">:</span><span class="pln">rotate</span><span class="pun">(-</span><span class="lit">5deg</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

__Fullscreen video that resizes and maintains ratios. Uses simple JavaScript to modify CSS properties__

This is a trendy way of displaying videos. For a while, the [PayPal Web site](https://tinyurl.com/yxe56fp7) used a small size video that looped and started playing as soon as the page was loaded. One of the JsBin examples below uses this video. 

<figure style="margin: 0.5em; text-align: center;">
	<img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
		onclick="window.open('https://tinyurl.com/y5skfhor')"
		src    ="https://tinyurl.com/yy8u724k"
		alt    ="paypal web site with full screen video"
		title  ="paypal web site with full screen video"
	/>
</figure>


Below you will find two examples that show how to do this trick. The first is for a "regular" video, using the `<video>` and `<source>` elements. This technique can also be used on any YouTube embedded videos (see Example 2 below).

The interesting part is that we use a 100% standard (and really small and simple) JavaScript code here to handle the window `resize` events and we just set regular CSS properties width and height of the video element, to resize the video.


__Example #1: with a regular video__

[Online at JS Bin](https://jsbin.com/gezudoy/edit?html,css,js,console,output) ([Local Example - Regular Video](src/2.2.4-example2.html))

<figure style="margin: 0.5em; text-align: center;">
	<img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
		onclick="window.open('https://tinyurl.com/y5skfhor')"
		src    ="https://tinyurl.com/y5baoc64"
		alt    ="Samurai pizzacat video full screen with css and dom events"
		title  ="Samurai pizzacat video full screen with css and dom events"
	/>
</figure>


Here is the HTML code. It's really simple, just notice the <body onload="init();"> which calls the JavaScript init() function right after the page is loaded.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">Full width video like PayPal site</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body</span><span class="pln"> </span><strong><span class="atn">onload</span><span class="pun">=</span><span class="atv">"</span><span class="pln">init</span><span class="pun">();</span><span class="atv">"</span></strong><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;video</span><span class="pln"> </span><span class="atn"><strong>id</strong></span><strong><span class="pun">=</span><span class="atv">"myVideo"</span></strong><span class="pln"> </span><span class="atn">autoplay</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp; &lt;source</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.webm</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">video/webm</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.ogg</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">video/ogg</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span class="pun">=</span><span class="atv">https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">video/mp4</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/video&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>


Here is the CSS (remove margins, remove padding, hide parts that could overflow from the <body>):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">body </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; margin</span><span class="pun">:</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; padding</span><span class="pun">:</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; overflow</span><span class="pun">:</span><span class="pln">hidden</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


And now the JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> video</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> init</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// function called when the page is loaded</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myVideo"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// For initial value</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video</span><span class="pun">.</span><span class="pln">width </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">innerWidth</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;video</span><span class="pun">.</span><span class="pln">height </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">innerHeight</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="com">// For dealing with window resize</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;window</span><span class="pun">.</span><span class="pln">onresize </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;video</span><span class="pun">.</span><span class="pln">width </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">innerWidth</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;video</span><span class="pun">.</span><span class="pln">height </span><span class="pun">=</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">innerHeight</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Example #2: with a YouTube video__

[Online at JS Bin](https://jsbin.com/yoreco/1/edit?html,css,js,output)  ([Local Example - YouTube](src/2.2.4-example3.html))

The CSS and JavaScript codes for this example are exactly the same as in Example #1.

<figure style="margin: 0.5em; text-align: center;">
	<img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
		onclick="window.open('https://tinyurl.com/y5skfhor')"
		src    ="https://tinyurl.com/y3j3cs9u"
		alt    ="full screen video from youtube"
		title  ="full screen video from youtube"
	/>
</figure>


__Full screen video, pure CSS approaches__

1. Let's use the video from the PayPal Web site, played full screen using only very simple CSS.

	In this example ([online at JSBin](https://tinyurl.com/y2jw87hj)), the video does not rescale; it's just cropped if the browser window is resized. Enlarge your browser and you'll see a man with a phone on the right. Resize your browser and you'll see only part of the video.

	<figure style="margin: 0.5em; text-align: center;">
		<img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
			onclick="window.open('https://tinyurl.com/y5skfhor')"
			src    ="https://tinyurl.com/y2zhgkxv"
			alt    ="Paypal video full screen"
			title  ="Paypal video full screen"
		/>
	</figure>

CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> body </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; margin</span><span class="pun">:</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; padding</span><span class="pun">:</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; overflow</span><span class="pun">:</span><span class="pln">hidden</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">video </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; width</span><span class="pun">:</span><span class="lit">100</span><span class="pun">%;</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; height</span><span class="pun">:</span><span class="kwd">auto</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

2. Full screen video with CSS effects

	This time the video is zoomed in so that it's much bigger than the browser's window. When we resize the browser, the part of the video that is visible adapts itself. It's not "real resize" of the video.

	Try the [example and read the explanation in this article by Dudley Storey](https://tinyurl.com/yxldqdt2). Also available as a [simplified JsBin example](https://tinyurl.com/y2m2lnjf).

	<figure style="margin: 0.5em; text-align: center;">
		<img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
			onclick="window.open('https://tinyurl.com/y5skfhor')"
			src    ="https://tinyurl.com/y22o92ej"
			alt    ="full screen video pure CSS"
			title  ="full screen video pure CSS"
		/>
	</figure>


HTML code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">Full screen video, example from demosthene.info by </span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;header&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;video</span><span class="pln"> </span><span class="atn">autoplay</span><span class="pun"></span><span class="atv"></span><span class="pln"> </span><span class="atn">loop</span><span class="pun">=</span><span class="atv">""</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; poster</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/polina.jpg"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; id</span><span class="pun">=</span><span class="atv">"bgvid"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/polina.webm"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/polina.mp4"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;/video&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/header&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;section&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h1&gt;</span><span class="pln">https://demosthenes.info/blog/777/Create-Fullscreen-HTML5-Page-</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">Background-Video</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/section&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">html</span><span class="pun">,</span><span class="pln"> body</span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="pln">white</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="lit">100</span><span class="pun">%;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">header</span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; height</span><span class="pun">:</span><span class="pln"> </span><span class="lit">100</span><span class="pun">%;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">image</span><span class="pun">:</span><span class="pln"> url</span><span class="pun">(</span><span class="str">'https://dupontcours.free.fr/IMG/dots.png'</span><span class="pun">),</span><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="pln">url</span><span class="pun">(</span><span class="str">'#'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">repeat</span><span class="pun">:</span><span class="pln"> repeat</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">no</span><span class="pun">-</span><span class="pln">repeat</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">size</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">auto</span><span class="pun">,</span><span class="pln"> cover</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">position</span><span class="pun">:</span><span class="pln"> center center</span><span class="pun">,</span><span class="pln"> top left</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; font</span><span class="pun">-</span><span class="pln">family</span><span class="pun">:</span><span class="pln"> sans</span><span class="pun">-</span><span class="pln">serif</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="pln"> </span><span class="com">#051a00;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">header video </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; position</span><span class="pun">:</span><span class="kwd">fixed</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; top</span><span class="pun">:</span><span class="lit">50</span><span class="pun">%;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; left</span><span class="pun">:</span><span class="lit">50</span><span class="pun">%;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; min</span><span class="pun">-</span><span class="pln">width</span><span class="pun">:</span><span class="lit">100</span><span class="pun">%;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; min</span><span class="pun">-</span><span class="pln">height</span><span class="pun">:</span><span class="lit">100</span><span class="pun">%;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; width</span><span class="pun">:</span><span class="kwd">auto</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; height</span><span class="pun">:</span><span class="kwd">auto</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; z</span><span class="pun">-</span><span class="pln">index</span><span class="pun">:-</span><span class="lit">100</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; transform</span><span class="pun">:</span><span class="pln">translateX</span><span class="pun">(-</span><span class="lit">50</span><span class="pun">%)</span><span class="pln"> translateY</span><span class="pun">(-</span><span class="lit">50</span><span class="pun">%);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


The trick here is that:

+ the video is in the header, and the header has a plotted transparent background that is repeated in X and Y (see lines 8 and 9).
+ The video is positioned so that it's origin (top left corner) is away from the visible surface (line 25), while it is set to take 100% of the surface (lines 20 and 21).

__Full screen video that resizes and keeps its ratio, using the viewport units.__

[Example on JsBin](https://output.jsbin.com/henaruv) ([Local example - Full Screen w/ Viewport](src/2.2.4-example4.html))

This time we obtain the same result as with the first example that used JavaScript and a resize event. The video resizes correctly and keeps its ratio.

CSS code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">body </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;margin</span><span class="pun">:</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">video </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;position</span><span class="pun">:</span><span class="pln"> absolute</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; <strong>&nbsp;width</strong></span><strong><span class="pun">:</span><span class="pln"> </span><span class="lit">100vw</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;<strong>height</strong></span><strong><span class="pun">:</span><span class="pln"> </span><span class="lit">100vh</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">object</span><span class="pun">-</span><span class="pln">fit</span><span class="pun">:</span><span class="pln"> cover</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">object</span><span class="pun">-</span><span class="pln">position</span><span class="pun">:</span><span class="pln"> center center</span><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__Discussion: why can't we achieve perfect resizing with only CSS and the use of properties width=100% and height=100%?__

Let's use the same video to compare the different approaches again:

1. [Original approach](https://jsbin.com/zowuqey/edit?html,css,js,output), using JavaScript. This solution works on any browser, so we will focus on the two following methods, based on pure CSS.
2. [Using CSS 100%](https://jsbin.com/sakujuv/1/edit?html,css,output) width and height properties (no JavaScript).
3. [Using CSS viewport](https://jsbin.com/xureyu/3/edit?html,css,output) units for width and height (no JavasScript).

Resizing the browser window shows that #1 (JavaScript) and #3 (viewport units) behave in the same way: the width or height of the video always fills the window (whichever is smaller), and we always see the whole video.

__Conclusion__: we can get full size video without JavaScript by using viewport units, unless we need to support some old browsers (see their [current support on CanIUse](https://caniuse.com/#feat=viewport-units)).

Setting the video to 100% `width` and `height` results in different behavior:

+ 100% means 100% of the size of the <body> tag.
+ The body tag's width is 100% of the browser window width, so the video is always full width.
+ The body tag's height, however, is determined by the size of its children: the body tag's height grows and shrinks to accommodate the size of the children.
+ If the browser window is made wide and short, the video is full width, the height is taller than the window, and part of the video is not visible. It seems that just using % does not get us the same effect.


#### Knowledge check 2.2.4

1. Using CSS, is it possible to apply geometric transformations to a video player, or to add shadows to an audio player? (Yes/No)

	Ans: Yes<br/>
	Explanation: The `<audio>` and `<video>` elements are like any other HTML element. CSS 2D and 3D transform rules can be applied, like in some of the examples in this page, that use the CSS transform property. Also, shadows can be added using the box-shadow property.


### 2.2.5 Control players from JavaScript

The `<video>` element has methods, properties/attributes and events that can be manipulated with JavaScript. Using the DOM API, it's possible to manipulate an audio or video element as a JavaScript object that has:

+ __Methods__ for controlling the behavior, such as play(), pause(), etc.
+ __Properties__ (duration, current position, etc.), either in read/write mode (such as volume), or in read-only mode (such as encoding, duration, etc.)
+ __Events__ generated during the life cycle of the element that can be processed using JavaScript callbacks. It is also possible to send events to control the video player

Like any HTML element, the `<video>` element can be manipulated/created using the DOM JavaScript API. Here is an example of programmatically creating a `<video>` element:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> video </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">createElement</span><span class="pun">(</span><span class="str">'video'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">video</span><span class="pun">.</span><span class="pln">src </span><span class="pun">=</span><span class="pln"> </span><span class="str">'video.mp4'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">video</span><span class="pun">.</span><span class="pln">controls </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">appendChild</span><span class="pun">(</span><span class="pln">video</span><span class="pun">);</span></li>
</ol></div>

This will create a complete video player for the file "video.mp4", with control buttons, and will add it to the `<body>` element of the page.


#### Example that shows how to call play/pause or rewind a video

Please look at this [interesting example](https://jsbin.com/gowowoj/edit?html,output) (you can click on "edit in JsBin" to view the source, but we will give simpler and more detailed examples in the next section - this one is more to show what can be done). [[Local Example - Controls](src/2.2.5-controls.html)]

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y3qo49w6')"
    src    ="https://tinyurl.com/y4skpsq5"
    alt    ="video + use of the JavaScript API"
		title  ="video + use of the JavaScript API"
  />
</figure>

Note that in order to play the video, you must click on the "vid.play()" text. To pause it, you click on the "vid.pause()" text, and so on. _Notice the text at the top of the video, as well as the transparency._ The text can be selected, since all the elements displayed are pure DOM objects. You can zoom the page in and out, etc. This was not possible with the Flash technology.

__Conclusion__:  you can very easily change the look and feel of the standard video player: use custom CSS and design your own control widgets. We can find many examples of such video players that offer extended functionalities on the Web. We will present some of them later in the course, but before that, let's see a little more of what we can do using the JavaScript API of the `<video>` element.


#### Knowledge check 2.2.5

1. Once created or selected using the standard DOM API, can audio and video elements be manipulated as JavaScript objects? (Yes/No)

	Ans: Yes<br/>
	Explanation: Using the DOM API, it is possible to create programmatically an audio or video element and insert it into the HTML page. If it has already been declared, you can just select it from JavaScript. The JavaScript object created/selected has properties such as duration, currentTime, etc., and also has methods such as play(), stop(), etc. It can also send events (it is possible to monitor the progress for example) or receive events.







