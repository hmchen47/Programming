# Week 2: HTML5 Multimedia


## 2.2 Streaming multimedia content

### 2.2.0 Lecture Notes

+ [The `<video>` element](#221-the-video-element)
	+ HTML5 Flash Killers: `<video>` and `<canvas>` elements
	+ `<video>` element: a DOM member
		+ CSS styling applied
		+ manipulation w/ the DOM API
	+ example code

		<div><ol>
		<li style="margin-bottom: 0px;" value="1"><span>&lt;video</span><span> </span><span>width</span><span>=</span><span>"320"</span><span> </span><span>height</span><span>=</span><span>"240"</span><span> </span><span>controls</span><span>=</span><span>"controls"</span><span>&gt;</span></li>
		<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"movie.mp4"</span><span> </span><span>type</span><span>=</span><span>"video/mp4"</span><span> </span><span>/&gt;</span></li>
		<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"movie.ogg"</span><span> </span><span>type</span><span>=</span><span>"video/ogg"</span><span> </span><span>/&gt;</span></li>
		<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;Your browser does not support the </span><span>&lt;video&gt;</span><span> element.</span></li>
		<li style="margin-bottom: 0px;"><span>&lt;/video&gt;</span></li>
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

		<div><ol>
		<li style="margin-bottom: 0px;" value="1"><span>var</span><span> video </span><span>=</span><span> document</span><span>.</span><span>createElement</span><span>(</span><span>'video'</span><span>);</span></li>
		<li style="margin-bottom: 0px;"><span>video</span><span>.</span><span>src </span><span>=</span><span> </span><span>'video.mp4'</span><span>;</span></li>
		<li style="margin-bottom: 0px;"><span>video</span><span>.</span><span>controls </span><span>=</span><span> </span><span>true</span><span>;</span></li>
		<li style="margin-bottom: 0px;"><span>document</span><span>.</span><span>body</span><span>.</span><span>appendChild</span><span>(</span><span>video</span><span>);</span></li>
		</ol></div>

+ [Categories of HTML elements](https://html.spec.whatwg.org/multipage/dom.html#content-categories)
	+ Metadata content
		+ set up the presentation or behavior of the rest of the content
		+ set up the relationship of the document with other documents
		+ convey other "out of band" information
		+ list of elements: base, link, meta, noscript, script, style, template, title
	+ Flow content: most elements that are used in the body of documents and applications
	+ Sectioning content
		+ define the scope of headings and footers
		+ list of element: article, aside, nav, section
	+ Heading content
		+ define the header of a section
		+ lis of elements: h1, h2, h3, h4, h5, h6, hgroup
	+ Phrasing content
		+ the text of the document, as well as elements that mark up that text at the intra-paragraph level
		+ runs of phrasing content form paragraphs
	+ Embedded content
		+ import another resource into the document, or content from another vocabulary that is inserted into the document
		+ list of element: audio, canvas, embed, iframe, img, math, object, picture, svg, video
	+ Interactive content
		+ specifically intended for user interaction
		+ a (if the href attribute is present), audio (if the controls attribute is present), button, details, embed, iframeimg (if the usemap attribute is present), input (if the type attribute is not in the Hidden state), label, object (if the usemap attribute is present), select, textarea, video (if the controls attribute is present)

+ [The most interesting methods, properties, and events provided by the `<video>` element API](#226-the-javascript-api)

	<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 40vw;" cellspacing="0" cellpadding="5" border="1">
  	<caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://www.w3.org/2010/05/video/mediaevents.html">HTML5 Video Events and API</a></caption>
		<thead>
		<tr style="font-size: 1.2em;">
			<th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Methods</th>
			<th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Properties</th>
			<th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Events</th>
		</tr>
	<tbody>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">play()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">currentSrc</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">play</span></strong></td>
		</tr>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">pause()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">currentTime</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">pause</span></strong></td>
		</tr>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">load()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">startTime (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">progress</span></strong></td>
		</tr>
		<tr>
			<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">canPlayType()</strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">videoWidth</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">error</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">videoHeight</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">timeupdate</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">duration (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">ended</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">ended (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">abort</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">error</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">empty</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">paused (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">emptied</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">muted</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">waiting</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">seeking</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">loadedmetadata</strong></td>
		</tr>
		<tr>
			<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">volume</span></strong></td> <td></td>
		</tr>
		<tr>
			<td></td>	<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">height</span></strong></td> <td></td>
		</tr>
		<tr>
			<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">width</span></strong></p> </td> <td></td>
		</tr>
		<tr>
			<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;" face="courier new, courier, monospace">seekable (readonly)</span></strong></p> </td> <td></td>
		</tr>
		<tr>
			<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">played (readonly)</span></strong></p> </td> <td></td>
		</tr>
	</tbody>
	</table>


+ The `<video>` element JavaScript API
	+ useful for implementing playlists, making custom user interfaces and many other interesting things
	+ use external buttons to control the player's behavior
		+ HTML code
			+ `<button onclick="playVideo();" style="cursor: pointer;">Play</button>`
			+ `<button onclick="pauseVideo();" style="cursor: pointer;">Pause</button>`
		+ JavaScript:
			+ `vid = document.querySelector("#vid");`: get the JavaScript object corresponding to the video element
			+ `vid.play();` & `vid.pause()`: methods from API for plating/pausing the video
			+ `vid.currentTime = 0;`: rewind the video
			+ `vid.load()`: rewind the video to `vid.currentTime = 0` and pause the video
	+ detect end of the video and start another one
		+ HTML code: `vid.addEventListener('ended', playNextVideo, false);`
		+ JavaScript: 

			```js
			function playNextVideo(e) {
				// Whatever you want to do after the event, change the src attribute
				// of the video element, for example, in order to play another video
			}
			```

	+ manage playlist
		+ HTML code
			+ `var sources = ["https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4", "https://www.archive.org/.../P1120973_512kb.mp4"];`: a list for videos to play
			+ `<body onload="init()">`: call `init()` as the page loaded
		+ JavaScript:
			+ `myVideo = document.querySelector("#myVideo");`: used the DOM to get the JavaScript object corresponding to the video element
			+ `myVideo.addEventListener('ended', loadAndplayNextVideo, false);`: define the listerner for the `ended` event
			+ `loadNextVideo();`: callback function to react the `ended` event
				+ `currentVideo`: a variable corresonding to the the index of the current video
				+ `myVideo.src = sources [currentVideo % sources.length]`: set the src of the video element to `sources[0]`, then to `sources[1]`, and nodule w/ the length of the list to repeat the playing





### 2.2.1 The `<video>` element

The `<video>` element of HTML5 is one of the two "Flash killers" (the other being the `<canvas>` element). It was designed to replace horrible things like embedded Flash objects that used to be around.


#### Before HTML5, how did we embed videos in a Web page?

Like this!

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;object</span><span> </span><span>width</span><span>=</span><span>"425"</span><span> </span><span>height</span><span>=</span><span>"344"</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;param</span><span> </span><span>name</span><span>=</span><span>"movie"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>value</span><span>=</span><span>"https://www.youtube.com/v/9sEI1AUFJKw&amp;hl=en_GB&amp;fs=1&amp;"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;/param&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;param</span><span> </span><span>name</span><span>=</span><span>"allowFullScreen"</span><span>&nbsp; &nbsp;</span><span>value</span><span>=</span><span>"true"</span><span>&gt;&lt;/param&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;param</span><span> </span><span>name</span><span>=</span><span>"allowscriptaccess"</span><span> </span><span>value</span><span>=</span><span>"always"</span><span>&gt;&lt;/param&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;embed</span><span> </span><span>src</span><span>=</span><span>"https://www.youtube.com/v/9sEI1AUFJKw&amp;hl=en_GB&amp;fs=1&amp;"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>type</span><span>=</span><span>"application/x-shockwave-flash"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>allowscriptaccess</span><span>=</span><span>"always"</span><span> </span><span>allowfullscreen</span><span>=</span><span>"true"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>width</span><span>=</span><span>"425"</span><span> </span><span>height</span><span>=</span><span>"344"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;/embed&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&lt;/object&gt;</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;video</span><span> </span><span>width</span><span>=</span><span>"320"</span><span> </span><span>height</span><span>=</span><span>"240"</span><span> </span><span>controls</span><span>=</span><span>"controls"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"movie.mp4"</span><span> </span><span>type</span><span>=</span><span>"video/mp4"</span><span> </span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"movie.ogg"</span><span> </span><span>type</span><span>=</span><span>"video/ogg"</span><span> </span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;Your browser does not support the </span><span>&lt;video&gt;</span><span> element.</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/video&gt;</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;iframe</span><span> </span><span>width</span><span>=</span><span>"560"</span><span> </span><span>height</span><span>=</span><span>"315"</span><span> </span><span>src</span><span>=</span><span>"https://www.youtube.com/watch?v=9NTrwrfI-X4"</span><span> </span><span>frameborder</span><span>=</span><span>"0"</span><span> </span><span>allowfullscreen</span><span>&gt;&lt;/iframe&gt;</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span><span></span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span></span><span><span><span>&nbsp;&nbsp; </span><span></span></span>&lt;title&gt;</span><span>horse song</span><span>&lt;/title&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span>&lt;body&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span></span><span><span><span>&nbsp;&nbsp; </span><span></span></span>&lt;audio</span><span> </span><span>controls</span><span>=</span><span>"controls"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span><span></span><span></span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/horse.ogg"</span><span> </span><span>type</span><span>=</span><span>"audio/ogg"</span><span> </span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span><span></span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/horse.mp3"</span><span> </span><span>type</span><span>=</span><span>"audio/mp3"</span><span> </span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span></span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span><span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span></span><span><span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span></span>Your browser does not support the audio element.</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span></span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span><span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span></span><span><span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span></span>Download the audio/video in</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span><span>&nbsp;&nbsp; </span><span></span><span>&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/horse.ogg"</span><span>&gt;</span><span>OGG</span><span>&lt;/a&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span></span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span><span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span>or </span><span>&lt;a</span><span> </span><span>href</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/horse.mp3"</span><span>&gt;</span><span>MP3</span><span>&lt;/a&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span></span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span><span><span><span><span>&nbsp;&nbsp; </span><span></span></span></span>format.</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span></span><span><span><span>&nbsp;&nbsp; </span><span></span></span>&lt;/audio&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp;&nbsp; </span><span></span>&lt;/body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/html&gt;</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;figure</span><span> </span><span>id</span><span>=</span><span>"figaudio1"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;</span><span>&lt;img</span><span> </span><span>id</span><span>=</span><span>"imghorse"</span><span> </span><span>width</span><span>=</span><span>"200"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;</span><span>src</span><span>=</span><span>"https://upload.wikimedia.org/wikipedia/commons/d/d4/Nokota_Horses.jpg"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;alt</span><span> </span><span>=</span><span> </span><span>"a horse"</span><span>/&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;</span><span>&lt;figcaption</span><span> </span><span>id</span><span>=</span><span>"figcptionaudio1"</span><span>&gt;</span><span> Press Play to hear the horse! </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &lt;audio</span><span> </span><span>controls</span><span>=</span><span>"controls"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/horse.ogg"</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span>=</span><span>"audio/ogg"</span><span> </span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/horse.mp3"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span>=</span><span>"audio/mp3"</span><span> </span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;Your browser does not support the audio element.</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;Download the audio/video in</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>&lt;a</span><span> </span><span>href</span><span>=</span><span>”https://mainline.i3s.unice.fr/mooc/horse.ogg”</span><span>&gt;</span><span>OGG</span><span>&lt;/a&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;or </span><span>&lt;a</span><span> </span><span>href</span><span>=</span><span>”https://mainline.i3s.unice.fr/mooc/horse.mp3”</span><span>&gt;</span><span>MP3</span><span>&lt;/a&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; format.</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp; &nbsp;&lt;/audio&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp; </span><span>&lt;/figcaption&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/figure&gt;</span></li>
</ol></div>


CSS source code:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>#figaudio1 {</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; width </span><span>:</span><span> </span><span>420px</span><span>;;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; text</span><span>-</span><span>align</span><span>:</span><span>center</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; padding </span><span>:</span><span> </span><span>6px</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; background </span><span>:</span><span> white</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; margin </span><span>:</span><span> </span><span>0</span><span> </span><span>11px</span><span> </span><span>0px</span><span> </span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; border </span><span>:</span><span>solid </span><span>1px</span><span> </span><span>#888888;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; border</span><span>-</span><span>radius </span><span>:</span><span> </span><span>8px</span><span> </span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>#figcptionaudio1 {</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; font</span><span>-</span><span>size </span><span>:</span><span> </span><span>.</span><span>8em</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; padding </span><span>:</span><span> </span><span>6px</span><span> </span><span>8px</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; background </span><span>:</span><span> </span><span>#dddddd; </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; display </span><span>:</span><span>block</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; text</span><span>-</span><span>align </span><span>:</span><span>center</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; font</span><span>-</span><span>family </span><span>:</span><span> georgia</span><span>,</span><span> serif</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; font</span><span>-</span><span>style </span><span>:</span><span> italic</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; border</span><span>-</span><span>radius </span><span>:</span><span> </span><span>7px</span><span> </span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>#figaudio1 &gt; img {</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; background </span><span>:</span><span> </span><span>#eeeeee;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; padding </span><span>:</span><span> </span><span>5px</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; border </span><span>:</span><span> solid </span><span>1px</span><span> </span><span>#444444;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>/* For audio and img transitions/animation */</span></li>
<li style="margin-bottom: 0px;"><span>audio</span><span>,</span><span> </span><span>#figaudio1 &gt; img {</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; transition</span><span>:</span><span>all </span><span>0.5s</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>#figaudio1 &gt; img:hover {</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; box</span><span>-</span><span>shadow</span><span>:</span><span> </span><span>15px</span><span> </span><span>15px</span><span> </span><span>20px</span><span> rgba</span><span>(</span><span>0</span><span>,</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0.4</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; transform</span><span>:</span><span> scale</span><span>(</span><span>1.05</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>audio</span><span>:</span><span>hover</span><span>,</span><span> audio</span><span>:</span><span>focus</span><span>,</span><span> audio</span><span>:</span><span>active </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; box</span><span>-</span><span>shadow</span><span>:</span><span> </span><span>15px</span><span> </span><span>15px</span><span> </span><span>20px</span><span> rgba</span><span>(</span><span>0</span><span>,</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0.4</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; transform</span><span>:</span><span> scale</span><span>(</span><span>1.05</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;video</span><span> </span><strong><span>id</span><span>=</span><span>"w3devCampusVideo"</span></strong><span> </span><span>autoplay</span><span> </span><span>controls</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.webm</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span>=</span><span>video/webm</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.ogg</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span>=</span><span>video/ogg</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span>=</span><span>video/mp4</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&lt;/video&gt;</span><span> </span></li>
</ol></div>

... and the CSS source code is as follows:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>#w3devCampusVideo {</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; width</span><span>:</span><span> </span><span>300px</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; <strong>transition</strong></span><strong><span>:</span><span> all </span><span>0.5s</span><span> ease</span><span>-</span><span>in</span><span>-</span><span>out</span><span>;</span></strong></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>#w3devCampusVideo<strong>:hover</strong>&nbsp;{ </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; width</span><span>:</span><span>400px</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; transform</span><span>:</span><span>rotate</span><span>(-</span><span>5deg</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;html lang="en"&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;title&gt;</span><span>Full width video like PayPal site</span><span>&lt;/title&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;body</span><span> </span><strong><span>onload</span><span>=</span><span>"</span><span>init</span><span>();</span><span>"</span></strong><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &lt;video</span><span> </span><span><strong>id</strong></span><strong><span>=</span><span>"myVideo"</span></strong><span> </span><span>autoplay</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &lt;source</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span>=</span><span>https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.webm</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>video/webm</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;source</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span>=</span><span>https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.ogg</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>video/ogg</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;source</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; src</span><span>=</span><span>https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>video/mp4</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/body&gt;</span></li>
</ol></div>


Here is the CSS (remove margins, remove padding, hide parts that could overflow from the <body>):

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>body </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; margin</span><span>:</span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; padding</span><span>:</span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; overflow</span><span>:</span><span>hidden</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
</ol></div>


And now the JavaScript code:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>var</span><span> video</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>function</span><span> init</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>// function called when the page is loaded</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;video </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>"#myVideo"</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>// For initial value</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;video</span><span>.</span><span>width </span><span>=</span><span> window</span><span>.</span><span>innerWidth</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;video</span><span>.</span><span>height </span><span>=</span><span> window</span><span>.</span><span>innerHeight</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>// For dealing with window resize</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;window</span><span>.</span><span>onresize </span><span>=</span><span> </span><span>function</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;video</span><span>.</span><span>width </span><span>=</span><span> window</span><span>.</span><span>innerWidth</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;video</span><span>.</span><span>height </span><span>=</span><span> window</span><span>.</span><span>innerHeight</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>};</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span> body </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; margin</span><span>:</span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; padding</span><span>:</span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; overflow</span><span>:</span><span>hidden</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>}</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>video </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; width</span><span>:</span><span>100</span><span>%;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; height</span><span>:</span><span>auto</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;!DOCTYPE html&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;html lang="en"&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><span>&lt;title&gt;</span><span>Full screen video, example from demosthene.info by </span><span>&lt;/title&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;header&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&lt;video</span><span> </span><span>autoplay</span><span></span><span></span><span> </span><span>loop</span><span>=</span><span>""</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; poster</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/polina.jpg"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; id</span><span>=</span><span>"bgvid"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &lt;source</span><span> </span><span>src</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/polina.webm"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>"video/webm"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &lt;source</span><span> </span><span>src</span><span>=</span><span>"https://mainline.i3s.unice.fr/mooc/polina.mp4"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>"video/mp4"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/header&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;section&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>&lt;h1&gt;</span><span>https://demosthenes.info/blog/777/Create-Fullscreen-HTML5-Page-</span></li>
<li style="margin-bottom: 0px;"><span>Background-Video</span><span>&lt;/h1&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/section&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/html&gt;</span></li>
</ol></div>


CSS code:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>html</span><span>,</span><span> body</span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; color</span><span>:</span><span>white</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; height</span><span>:</span><span> </span><span>100</span><span>%;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>header</span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; height</span><span>:</span><span> </span><span>100</span><span>%;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; background</span><span>-</span><span>image</span><span>:</span><span> url</span><span>(</span><span>'https://dupontcours.free.fr/IMG/dots.png'</span><span>),</span><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>url</span><span>(</span><span>'#'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; background</span><span>-</span><span>repeat</span><span>:</span><span> repeat</span><span>,</span><span> </span><span>no</span><span>-</span><span>repeat</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; background</span><span>-</span><span>size</span><span>:</span><span> </span><span>auto</span><span>,</span><span> cover</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; background</span><span>-</span><span>position</span><span>:</span><span> center center</span><span>,</span><span> top left</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; font</span><span>-</span><span>family</span><span>:</span><span> sans</span><span>-</span><span>serif</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; color</span><span>:</span><span> </span><span>#051a00;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>header video </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; position</span><span>:</span><span>fixed</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; top</span><span>:</span><span>50</span><span>%;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; left</span><span>:</span><span>50</span><span>%;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; min</span><span>-</span><span>width</span><span>:</span><span>100</span><span>%;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; min</span><span>-</span><span>height</span><span>:</span><span>100</span><span>%;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; width</span><span>:</span><span>auto</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; height</span><span>:</span><span>auto</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; z</span><span>-</span><span>index</span><span>:-</span><span>100</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; transform</span><span>:</span><span>translateX</span><span>(-</span><span>50</span><span>%)</span><span> translateY</span><span>(-</span><span>50</span><span>%);</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
</ol></div>


The trick here is that:

+ the video is in the header, and the header has a plotted transparent background that is repeated in X and Y (see lines 8 and 9).
+ The video is positioned so that it's origin (top left corner) is away from the visible surface (line 25), while it is set to take 100% of the surface (lines 20 and 21).

__Full screen video that resizes and keeps its ratio, using the viewport units.__

[Example on JsBin](https://output.jsbin.com/henaruv) ([Local example - Full Screen w/ Viewport](src/2.2.4-example4.html))

This time we obtain the same result as with the first example that used JavaScript and a resize event. The video resizes correctly and keeps its ratio.

CSS code:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>body </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;margin</span><span>:</span><span> </span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>video </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;position</span><span>:</span><span> absolute</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; <strong>&nbsp;width</strong></span><strong><span>:</span><span> </span><span>100vw</span><span>;</span></strong></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;<strong>height</strong></span><strong><span>:</span><span> </span><span>100vh</span><span>;</span></strong></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><strong><span>object</span><span>-</span><span>fit</span><span>:</span><span> cover</span><span>;</span></strong></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;</span><strong><span>object</span><span>-</span><span>position</span><span>:</span><span> center center</span><span>;</span></strong></li>
<li style="margin-bottom: 0px;"><span>}</span></li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>var</span><span> video </span><span>=</span><span> document</span><span>.</span><span>createElement</span><span>(</span><span>'video'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>video</span><span>.</span><span>src </span><span>=</span><span> </span><span>'video.mp4'</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>video</span><span>.</span><span>controls </span><span>=</span><span> </span><span>true</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>document</span><span>.</span><span>body</span><span>.</span><span>appendChild</span><span>(</span><span>video</span><span>);</span></li>
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


### 2.2.6 The JavaScript API

#### Methods, properties, and events

The JavaScript API gives you powerful tools to manipulate the `<video>` element, as the video object provides many properties, methods and events.

The complete list of events can be found in the [HTML5 living standard specification](https://tinyurl.com/y4rvva5s).

The list of properties can be found at the [W3C HTML5 Video Events and API page](https://tinyurl.com/2a3jncy). This page is interesting for Web developers because it shows an interactive view of the different values and events changing over time while the video is playing within the page.

Click on the picture below to see it running online (or try the [direct link](https://www.w3.org/2010/05/video/mediaevents.html)), then play with the different buttons and look at the table of events and properties that will change in real time. The displayed names show the properties, events, and methods from the API.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 35vw;"
    onclick="window.open('https://tinyurl.com/y6s8knns')"
    src    ="https://tinyurl.com/yyas2nmz"
    alt    ="Interactive demo fro W3C specification page that shows all properties/methods/events available"
    title  ="Interactive demo fro W3C specification page that shows all properties/methods/events available"
  />
</figure>

Here is a table that shows the most interesting methods, properties, and events provided by the `<video>` element API

We provide this as a quick reminder - keep in mind that the [complete list](https://tinyurl.com/yxeolk5k) is much longer! 

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 40vw;" cellspacing="0" cellpadding="5" border="1">
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Methods</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Properties</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Events</th>
  </tr>
<tbody>
	<tr>
		<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">play()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">currentSrc</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">play</span></strong></td>
	</tr>
	<tr>
		<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">pause()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">currentTime</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">pause</span></strong></td>
	</tr>
	<tr>
		<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">load()</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">startTime (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">progress</span></strong></td>
	</tr>
	<tr>
		<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">canPlayType()</strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">videoWidth</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">error</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">videoHeight</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">timeupdate</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">duration (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">ended</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">ended (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">abort</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">error</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">empty</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">paused (readonly)</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">emptied</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">muted</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">waiting</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">seeking</span></strong></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;">loadedmetadata</strong></td>
	</tr>
	<tr>
		<td></td> <td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">volume</span></strong></td> <td></td>
	</tr>
	<tr>
		<td></td>	<td><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">height</span></strong></td> <td></td>
	</tr>
	<tr>
		<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">width</span></strong></p> </td> <td></td>
	</tr>
	<tr>
		<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;" face="courier new, courier, monospace">seekable (readonly)</span></strong></p> </td> <td></td>
	</tr>
	<tr>
		<td></td> <td> <p style="margin: 0px 0px 10px;"><strong style="font-weight: bold; font-family: Arial, Helvetica, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">played (readonly)</span></strong></p> </td> <td></td>
	</tr>
</tbody>
</table>


Let's see now, through a set of examples, how to use these most important properties, methods, and events...


#### Knowledge check 2.2.6

1. The W3C specification about the JavaScript API associated to `<audio>` and `<video>` elements, proposes an interactive demonstration of the different properties/methods/events; it's a must see for all Web developers interested in multimedia. Try it and guess what properties indicate the length of the video in seconds and the name of a valid event that is sent while the video is being played...

	a. duration and timeupdate<br/>
	b. currentTime and play<br/>

	Ans: a<br/>
	Explanation: If you try the intereactive demonstration, and play the example video, you will see that the duration property indicates the total length of the video. You will also see that the timeupdate event is emitted regularly while the video is being played?


### 2.2.7 The `<video>` element JavaScript API

The JavaScript API is useful for implementing playlists, making custom user interfaces and many other interesting things. The "enhanced HTML5 multimedia players" lesson presented further on the course relies heavily on this API.

#### Example #1: how to use external buttons to control the player's behavior

This example shows the first steps towards writing a custom video player. It shows basic usage of the JavaScript API for adding custom buttons to play/pause the video or to go back to the beginning by setting the `currentTime` property to zero.

[Try it online](https://jsbin.com/wapaxex/3/edit?html,css,output), and look at the source code below. [Local Example - Buttons](src/2.2.7-example1.html)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/yxvo5ont')"
    src    ="https://tinyurl.com/y6qx3agb"
    alt    ="use external buttons to control the player's behavior"
    title  ="use external buttons to control the player's behavior"
  />
</figure>


Source code extract:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;video</span><span> </span><span>id</span><span>=</span><span>"vid"</span><span> </span><span>controls</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.webm</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type</span><span>=</span><span>video/webm</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;">...</li>
<li style="margin-bottom: 0px;"><span>&lt;/video&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&lt;p&gt;</span><span>Example of custom controls:</span><span>&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>playVideo</span><span>();</span><span>"</span><span> </span><span>style</span><span>=</span><span>"</span><span>cursor</span><span>:</span><span> pointer</span><span>;</span><span>"</span><span>&gt;</span><span>Play</span><span>&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>pauseVideo</span><span>();</span><span>"</span><span> </span><span>style</span><span>=</span><span>"</span><span>cursor</span><span>:</span><span> pointer</span><span>;</span><span>"</span><span>&gt;</span><span>Pause</span><span>&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;button</span><span> </span><span>onclick</span><span>=</span><span>"</span><span>rewindVideo</span><span>();</span><span>"</span><span> </span><span>style</span><span>=</span><span>"</span><span>cursor</span><span>:</span><span> pointer</span><span>;</span><span>"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;Back to beginning</span><span>&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>&lt;script&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; vid </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>"#vid"</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; function</span><span> playVideo</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;vid</span><span>.</span><span>play</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; function</span><span> pauseVideo</span><span>() {</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;vid</span><span>.</span><span>pause</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; function</span><span> rewindVideo</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;vid</span><span>.</span><span>currentTime </span><span>=</span><span> </span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/script&gt;</span></li>
</ol></div>
 

_Explanations:_

+ _Lines 7, 9 and 11:_ we add a click listener to each button, in order to call a JavaScript function when the button is clicked.
+ _Line 14_: using the DOM API we get the JavaScript object that corresponds to the video element we inserted in the HTML document. This line is outside a function, it will be executed when the page loads.
+ _Lines 17 and 20_: we call methods from the API for playing/pausing the video.
+ _Line 24_: we modify the currentTime property in order to rewind the video. Note that `vid.load()` also rewinds the video, shows the poster image again, but also pauses the video. By using `currentTime=0` the playback does not stop.


#### Example #2: how to detect the end of a video and start another one

This example listens for the ended event, and calls a callback function when the video is ended.

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;video</span><span> </span><span>src</span><span>=</span><span>"video.ogv"</span><span> </span><span>id</span><span>=</span><span>"myVideo"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; video not supported</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&lt;script</span><span> </span><span>type</span><span>=</span><span>'text/javascript'</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; var vid = document</span><span>.querySelector</span><span>(</span><span>'#myVideo'</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; vid.addEventListener</span><span>(</span><span>'ended'</span><span>,&nbsp;</span><span><span style="color: #000000; line-height: 23.2727279663086px; background-color: #ffffff;">playN</span><span style="color: #000000; line-height: 23.2727279663086px; background-color: #ffffff;">extVideo</span>,&nbsp;</span><span>false</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span></span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; function</span><span>&nbsp;playNextVideo</span><span>(</span><span>e</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;</span><span>// Whatever you want to do after the event, change the src attribute</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;// of the video element, for example, in order to play another video</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;</span><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/script&gt;</span></li>
</ol></div>


#### Example #3: how to manage playlists

This example detects the end of a video then loads the next video, changes the src attribute of the video element and plays the video (see the online [example](https://jsbin.com/nuvejos/edit?html,output) [[Local Example - Playlist](src/2.2.7-example3.html)]). 

To try this example: use the progress cursor to go near the end of the first video that is being played and see how it continues with the next video. 

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;!doctype html&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;html</span><span> </span><span>lang</span><span>=</span><span>"en"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;meta</span><span> </span><span>charset</span><span>=</span><span>"utf-8"</span><span>/&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;title&gt;</span><span>Sequential Movies</span><span>&lt;/title&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;script&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>var</span><span> myVideo</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>var</span><span> currentVideo </span><span>=</span><span> </span><span>0</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>var</span><span> sources </span><span>=</span><span> </span><span>[</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>"https://mainline.i3s.unice.fr/mooc/samuraiPizzacat.mp4"</span><span>,</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>"https://www.archive.org/download/AnimatedMechanicalArtPiecesAtMit/P1120973_512kb.mp4"</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>];</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// Set the src of the video to the next URL in the playlist</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// If at the end we start again from beginning (the modulo </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// source.length does that)</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>function</span><span> loadNextVideo</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span></span><span><span><span><span><span>&nbsp; </span></span></span></span>myVideo</span><span>.</span><span>src </span><span>=</span><span> sources</span><span>[</span><span>currentVideo </span><span>%</span><span> sources</span><span>.</span><span>length</span><span>]</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span></span><span><span><span><span><span>&nbsp; </span></span></span></span>myVideo</span><span>.</span><span>load</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span></span><span><span><span><span><span>&nbsp; </span></span></span></span>currentVideo</span><span>++;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>}</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// listener plays the video</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>function</span><span> loadAndplayNextVideo</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span>console</span><span>.</span><span>log</span><span>(</span><span>"playing "</span><span> </span><span>+</span><span> sources</span><span>[</span><span>currentVideo </span><span>%</span><span> sources</span><span>.</span><span>length</span><span>])</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span>loadNextVideo</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span></span><span><span><span><span>&nbsp; </span></span></span>myVideo</span><span>.</span><span>play</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>}</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// Called when the page is loaded</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>function</span><span> init</span><span>(){</span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// get the video element using the DOM api</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span>myVideo </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>"#myVideo"</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// Define a callback function called each time a video ended</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span>myVideo</span><span>.</span><span>addEventListener</span><span>(</span><span>'ended'</span><span>,</span><span> loadAndplayNextVideo</span><span>,</span><span> </span><span>false</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span> </span><span>// Load the first video when the page is loaded.</span></li>
<li style="margin-bottom: 0px;"><span><span>&nbsp; </span></span><span><span><span>&nbsp; </span></span>loadNextVideo</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&lt;/script&gt;</span></li>
<li style="margin-bottom: 0px;"><span><span></span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;body</span><span> </span><span>onload</span><span>=</span><span>"</span><span>init</span><span>()</span><span>"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;video</span><span> </span><span>id</span><span>=</span><span>"myVideo"</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&nbsp; </span><span>controls</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; </span><span>&nbsp; </span><span>&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/html&gt;</span></li>
</ol></div>

+ _Line 9_: the JavaScript array that contains the URLs of the videos in the playlist. In this example, we've got only two of them, but if the array is larger the example will still work.
+ _Line 44_: When the page is loaded, an `init()` function is called.
+ _Lines 34-40_: we used the DOM to get the JavaScript object corresponding to the video element, then define a listener for the `ended` event. Each time a video will end, the `loadAndplayNextVideo()` callback will be called. As the video element has no src attribute by default, we also preload the first video (call to `loadNextVideo()` at line 38).
+ _Lines 17-21_: the `loadNextVideo()` function uses a variable called `currentVideo` that corresponds to the index of the current video. By setting `myVideo.src = sources [currentVideo % sources.length]`, we set the src of the video element to sources[0], then to sources[1], and as we increment the `currentVideo` index each time (line 19), if it becomes greater than 1, the modulo (the "%" symbol is the modulo in JavaScript) will make it "loop" between 0 and the number of videos in the playlist. In other words, when the last video ends, it starts back to the first one.



### 2.2.8 [Advanced] Extended examples

In this section, we propose five extended examples that use more JavaScript and more complex CSS manipulation. They might be a little hard to understand if you are a JavaScript beginner, but don't be afraid to try and test them, look at the code, etc.

Some examples are given "as is", such as the custom video player that uses SVG (at the end of the page); if you are interested, you may view the code. 


#### Example #1: a player showing the use of every type of CSS3 transformation

Please see this [example online](https://jsbin.com/vaqulep/edit?html,css,output), originally written by [Chris Heilmann](https://christianheilmann.com/), and tuned by us ;). ([Local Example - CSS Transformation](src/2.2.8-example1.html))

Don't forget to click the JavaScript and CSS tabs in JS Bin in order to display the JavaScript code that creates the buttons on the right of the video, and the CSS that processes the different clicks and applies CSS3 transforms.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y56yuvq5')"
    src    ="https://tinyurl.com/yymcxk7a"
    alt    ="a player showing the use of every type of CSS3 transformation"
    title  ="a player showing the use of every type of CSS3 transformation"
  />
</figure>

This example shows a lot:

+ It uses the HTML5 elements `<nav>`, `<footer>`, `<header>`.
+ It shows the use of CSS3 2D transformations (scale, translate, and rotate).
+ It shows how to handle DOM events using JavaScript and how to modify CSS properties of the `<video>` element from JavaScript.


#### Example #2: how to track all possible events and manipulate many properties

This example also shows how to handle failures. See the code and play with this [example online](https://jsbin.com/becaref/3/edit?html,output). ([Local Example - Track Events](src/2.2.8-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y56yuvq5')"
    src    ="https://tinyurl.com/y5627wpr"
    alt    ="track all possible events and manipulate many properties"
    title  ="track all possible events and manipulate many properties"
  />
</figure>

Here is an example of a piece of code for handling errors during video playback:

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>...</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>vid</span><span>.</span><span>addEventListener</span><span>(</span><span>'error'</span><span>,</span><span> </span><span>function</span><span>(</span><span>evt</span><span>)</span><span> </span><span>{</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; logEvent</span><span>(</span><span>evt</span><span>,</span><span>'red'</span><span>);</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>},</span><span> </span><span>false</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>...</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>function</span><span> logEvent</span><span>(</span><span>evt</span><span>,</span><span> color</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; switch</span><span> </span><span>(</span><span>evt</span><span>.</span><span>type</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>...</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> </span><span>'error'</span><span>:</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>var</span><span> error </span><span>=</span><span> document</span><span>.</span><span>querySelector</span><span>(</span><span>'video'</span><span>).</span><span>error</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>switch</span><span> </span><span>(</span><span>error</span><span>.</span><span>code</span><span>)</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>MEDIA_ERR_ABORTED</span><span>:</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span>.</span><span>innerHTML </span><span>=</span><span> </span><span>"fetching aborted at the user's request"</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>MEDIA_ERR_NETWORK</span><span>:</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span>.</span><span>innerHTML </span><span>=</span><span> </span><span>"a network error caused the browser to stop fetching the media"</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>MEDIA_ERR_DECODE</span><span>:</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span>.</span><span>innerHTML </span><span>=</span><span> </span><span>"an error occurred while decoding the media"</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>case</span><span> error</span><span>.</span><span>MEDIA_ERR_SRC_NOT_SUPPORTED</span><span>:</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span>.</span><span>innerHTML </span><span>=</span><span> </span><span>"the media indicated by the src </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; attribute was not suitable"</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>default</span><span>:</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; note</span><span>.</span><span>innerHTML </span><span>=</span><span> </span><span>"an error occurred"</span><span>;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>break</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span>break</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp;</span><span>}</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;</span><span>...</span></li>
<li style="margin-bottom: 0px;">}</li>
</ol></div>


#### Example #3: how to display a percentage of buffering when using a slow connection

See the [example online](https://jsbin.com/xororol/3/edit?html,output) here too. ([Local Example - Buffering](src/2.2.8-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y56yuvq5')"
    src    ="https://tinyurl.com/y2xjxp9h"
    alt    ="how to display the percentage of buffering"
    title  ="how to display the percentage of buffering"
  />
</figure>


Note that on mobile phones, the video does not start until the user presses the play control or clicks on the video picture. Using the "`canplaythrough`" event is a trick to call a function that starts the video player as soon as the page is loaded on desktop. This event is not supported by mobile devices, so if you try this example on a mobile, the video will not start automatically.

As explained by the [Apple Developer Web site](http://developer.apple.com/):  "The `buffered` property is a `TimeRanges` object: an array of start and stop times, not a single value. Consider what happens if the person watching the media uses the time scrubber to jump forward to a point in the movie that hasn’t loaded yet—the movie stops loading and jumps forward to the new point in time, then starts buffering again from there. So the `buffered` property can contain an array of discontinuous ranges. The example simply seeks the end of the array and reads the last value, so it actually shows the percentage into the movie duration for which there is data. "

<div><ol>
<li style="margin-bottom: 0px;" value="1"><span>&lt;!doctype html&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;html lang="en"&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &lt;head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &lt;title&gt;</span><span>JavaScript Progress Monitor</span><span>&lt;/title&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp;&nbsp;&nbsp; &lt;meta charset="utf-8"/&gt;<br></span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &lt;script</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; function</span><span> getPercentProg</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> myVideo </span><span>=</span><span> document</span><span>.</span><span>getElementsByTagName</span><span>(</span><span>'video'</span><span>)[</span><span>0</span><span>];</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> endBuf </span><span>=</span><span> myVideo</span><span>.</span><span>buffered</span><span>.</span><span>end</span><span>(</span><span>0</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> soFar </span><span>=</span><span> parseInt</span><span>(((</span><span>endBuf </span><span>/</span><span> myVideo</span><span>.</span><span>duration</span><span>)</span><span> </span><span>*</span><span> </span><span>100</span><span>));</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document</span><span>.</span><span>getElementById</span><span>(</span><span>"loadStatus"</span><span>).</span><span>innerHTML </span><span>=</span><span> soFar </span><span>+</span><span> </span><span>'%'</span><span>;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; // Will be called as soon as the page is ready on desktop computer, </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; // Only when a user clicks on play control or image on mobile</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; function</span><span> myAutoPlay</span><span>()</span><span> </span><span>{</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> myVideo </span><span>=</span><span> document</span><span>.</span><span>getElementsByTagName</span><span>(</span><span>'video'</span><span>)[</span><span>0</span><span>];</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVideo</span><span>.</span><span>play</span><span>();</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span></span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; function</span><span> addMyListeners</span><span>(){</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>var</span><span> myVideo </span><span>=</span><span> document</span><span>.</span><span>getElementsByTagName</span><span>(</span><span>'video'</span><span>)[</span><span>0</span><span>];</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVideo</span><span>.</span><span>addEventListener</span><span>(</span><span>'progress'</span><span>,</span><span> getPercentProg</span><span>,</span><span> </span><span>false</span><span>);</span></li>
<li style="margin-bottom: 0px;"><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>// Calls autoplay only if the device is adapted</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myVideo</span><span>.</span><span>addEventListener</span><span>(</span><span>'canplaythrough'</span><span>,</span><span> myAutoPlay</span><span>,</span><span> </span><span>false</span><span>);</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; }</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &lt;/script&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/head&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;body</span><span> </span><span>onload</span><span>=</span><span>"</span><span>addMyListeners</span><span>()</span><span>"</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &lt;h1&gt;</span><span>Check progression of buffering before playing a movie. Useful withy </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; slow&nbsp;</span><span>connexion (3G, etc.)</span><span>&lt;/h1&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;div&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;video</span><span> </span><span>controls</span><span>&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>https://html5doctor.com/demos/video-canvas-magic/video.webm</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>video/webm</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>https://html5doctor.com/demos/video-canvas-magic/video.ogg</span><span>&nbsp;&nbsp;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>video/ogg</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;source</span><span> </span><span>src</span><span>=</span><span>https://html5doctor.com/demos/video-canvas-magic/video.mp4</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span>=</span><span>video/mp4</span><span>&gt;</span><span> </span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;/video&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp; &nbsp;&nbsp;</span><span>&lt;p</span><span> </span><span>id</span><span>=</span><span>"loadStatus"</span><span>&gt;</span><span>Buffering...</span><span>&lt;/p&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&nbsp; &nbsp;&nbsp;</span><span>&lt;/div&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/body&gt;</span></li>
<li style="margin-bottom: 0px;"><span>&lt;/html&gt;</span></li>
</ol></div>


#### Example #4: how to use SVG elements as external controllers

This is the ultimate way of doing a real custom player: redesign your own controls using SVG shapes! This example (try it [online](https://tinyurl.com/yyy4efgl)) is given "as is" for those of you who may be curious.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y56yuvq5')"
    src    ="https://tinyurl.com/yxrpx24e"
    alt    ="use SVG elements as external controllers"
    title  ="use SVG elements as external controllers"
  />
</figure>


#### Example #5: a custom video player written by a previous student

This is more an example than a tutorial. Maurice, a student who followed the precursor version of this MOOC, had the assignment to write a custom video player with playlist, video thumbnails, custom play/pause/next/previous/volume controls, and present it in a Web page that used a nice layout based on the new structuring elements seen during Week 1.

[Here is the online example on JS Bin](https://jsbin.com/noqubut/4/edit?html,js,output), by Maurice Buiten. We recommend that you look at the source code. ([Local Example - custom video player](src/2.2.8-example5.html))

Screenshot:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y56yuvq5')"
    src    ="https://tinyurl.com/y44qsh8h"
    alt    ="a custom video player in a nice presented html page"
    title  ="a custom video player in a nice presented html page"
  />
</figure>


### 2.2.9 Discussion and projects

This is the discussion forum dedicated to "streaming multimedia content". You are welcome to post comments and share your creations here, and of course ask questions.

Some topics of discussion and optional projects:


#### Suggested topics

+ Where do you host your video files (we are speaking about files that can be used with the `<video>` element directly, not on YouTube, DailyMotion, etc.)?
+ Have you already tried some of the enhanced audio or video players? Would you please share opinions or make a review of these players?
+ What tool do you use for encoding your audio and video files?


#### Optional projects

This might be useful (find [free videos](https://download.blender.org/peach/bigbuckbunny_movies/)).

Here are a few ideas to play with the material learned in this section. Your classmates and the team who prepared the course will be happy to look at them and give feedback. Please post URLs of your work in this discussion forum. These projects are optional, meaning that they won't be graded.

__Project 1 (very easy)__: find the "enhanced HTML5 video players" described in the course and try to use one of them to play a video. Do some customization as well, such as adding a logo, choosing a theme, etc.

__Project 2 (easy)__: try to write a video or an audio player with a few custom buttons for play/stop/etc. When your custom player is done, please add a way to play several videos one after another (what we call a playlist), etc.

Examples that can help you, created by students of earlier versions of this MOOC:

+ [A custom player with nice CSS and buttons](https://jsbin.com/dacevo/2/edit?html,css,output)
+ [Custom players with a small playlist composed of three songs by Queen](https://jsbin.com/vefiniq/5/edit?html,output)
+ [An awesome custom player created by @GeorgianaB, with playlist, progress bar, CSS3 animations, etc.](https://codepen.io/w3devcampus/pen/reQbow) Check this out!

__Project 3 (with JavaScript knowledge)__: play a video file or an audio file with an external synchronization. Use the progress event and the `currentTime` property from the audio and video objects you can manipulate with the JavaScript API described in the course. For example, please display some text aside the video, and/or display a Wikipedia page in an iframe, and/or display a Google map if you know how to do it.

