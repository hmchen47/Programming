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





