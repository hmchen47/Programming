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
  + `label` attribute: displayed in the GUI control included in the default HTML5 video player
  + `srclang`: the language for the text track data, MUST present if `kind=subtitles`

+ [The `WebVTT` format](#232-the-webvtt-format)
  + WebVTT: The Web Video Text Tracks Format
  + files containing text for captions and subtitles, and much more..
  + used w/ the `src` attribute of the `<track>` element
  + format: a starting and ending time, plus a value (the text that will be displayed), followed by a blank line (blank lines are separators between elements)
  + example

    ```vtt
    00:00:15.000 --> 00:00:18.183
    (wind whistling)

    00:00:54.192 --> 00:00:55.150
    (blade rings)
    ```

  + chapter
    + defined in `track` elements with a `kind="chapters"` attribute
    + a CUE with starting and ending times, and a text for its description
    + (optional) an ID useful when using the track element JavaScript API, in particular the `getCueById()` method of `TextTrack` object
    + types of ID:
      + numeric ID; e.g., `9`
      + string ID; e.g., `opening`
    + able to be displayed multiple lines w/o blank lines
    + example

      ```vtt
      9
      00:00:21.000 --> 00:00:22.000
      to hear from <u>you</u>

      Opening
      00:00:00.000 --> 00:00:30.000
      Welcome to our <i>nice film</i>

      00:01:57.083 --> 00:02:00.000
      <p>You're a fool for traveling alone</p>
      <p>so completely unprepared.</p>
      ```

+ [Adding subtitles to a video](#233-adding-subtitles-to-a-video)
  + required a video on one of the formats/codecs supported by the browsers you target; e.g., `H624` and `webm`
  + video encoding software: [Handbrake](https://handbrake.fr/), [Super](https://www.erightsoft.com/SUPER.html)
  + online video encoding services, such as [amara](https://amara.org/en/)

+ [Styling captions](#234-styling-captions)
  + __line:5%__: vertical position at a line 5% of the height of the video viewport (from top)
  + __position:5% align:start__: regular location at the bottom of the video, the start of the sentence will be located at 5% of the width of the video, i.e., near the left side
  + __position:95% align:end__: regular location at the bottom of the video, the end of the sentence will be at 95% of the horizontal width of the video
  + __size:33%__: size of each line = 1/3 the size of the video (displayed in multiple lines)
  + use of `<b>`, `<i>`, `<u>` for styling subtitles / captions
  + CSS rules example

    <div><ol style="list-style-type: decimal;">
    <li value="1">&lt;c.myclass&gt;This cue contains the class "myclass". </li>
    <li>Browsers that support ::cue CSS should make it red.&lt;/c&gt;</li>
    </ol></div><br/>

    + `::cue` pseudo element selector: used to match "cues" in the webVTT file
    + add parenthesis and a secondary CSS selector to match cues w/ a particular id, or a particular CSS class
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

+ [The `<track>` JavaScript API](#237-the-track-javascript-api)
  + powerful API used to develop many interesting features
    + dynamically building a navigation menu
    + synchronizing page content w/ timestamps in the WebVTT file
    + displaying all the subtitles/captions at once
    + making an app for creating on the fly subtitles/captions
    + etc.
  + example: sync guitar tablature and music score w/ a video
    + JavaScript code listens to the `ontimeupdate` event while the video is playing
    + the `currentTime` property: knowing exactly where we are in the video
    + an external library to render in an HTML5 canvas the bars corresponding to the current video explanations

+ [Pros of customized video players](#advantages-and-disadvantages-of-using-a-custom-player)
  + advantages of enhanced video players
    + support all kinds of subtitle formats
    + customizable look'n'feel
    + full screen mode w/o borders on old browsers
    + consistent look'n'feel for browsers
    + fast playback
    + sharing buttons for social media
    + support chapters
    + support scrub bar thumbnails
    + extra features for better accessibility
    + and so on...
  + advantages of using the `<video>` elements
    + total control
    + no need for external dependencies
    + lightweight: prevent from downloading JavaScript and CSS code


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
<div><ol>
<li value="1">&lt;Files mysubtitle.vtt&gt;</li>
<li> ForceType text/vtt;charset=utf-8</li>
<li>&lt;/Files&gt;</li>
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

<div><ol>
<li value="1">&lt;video height="272" width="640" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;poster="https://mainline.i3s.unice.fr/mooc/q1fx20VZ-640.jpg" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;crossorigin="anonymous" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;controls&gt;</li>
<li>&nbsp; &nbsp;&lt;source src="https://<span style="background-color: #eeeeee;">mainline.i3s.unice.fr<span style="background-color: #eeeeee;">/mooc/sintel.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/mp4"&gt; </li>
<li>&nbsp; &nbsp;&lt;source src="https://<span style="background-color: #eeeeee;">mainline.i3s.unice.fr<span style="background-color: #eeeeee;">/mooc/sintel.webm" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li>&nbsp; &nbsp;&lt;track src="https://<span style="background-color: #eeeeee;">mainline.i3s.unice.fr/</span>mooc/sintel-captions.vtt"</span> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; kind="captions" label="Closed Captions" default&gt;</li>
<li>&lt;/video&gt;</li>
</ol></div>


Notice that the `<track>` element at line 9 has an attribute named `kind` that indicates the type of the track that is included. Possible values are: `subtitles`, `captions`, `descriptions`, `chapters` or `metadata`.

 The `<track>` element also has an attribute `default` that indicates that we want this track to be displayed by default when reading the video.

We also used  an attribute named `crossorigin` that is necessary just to run this demo, as it is required by the server that hosts the video from this example.


#### Multiple tracks may be included in a video element

Multiple tracks are needed to support different langages, video captions for the hearing-impaired, subtitles, etc.

Below is an example ([from the specification](https://html.spec.whatwg.org/multipage/media.html#the-track-element)) that includes multiple `<track>` elements (subtitles for three languages and captions only for English):

<div><ol>
<li value="1">&lt;video src="brave.webm"&gt;</li>
<li>&nbsp; &nbsp;&lt;track kind=subtitles src=brave.en.vtt </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang=en </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label="English"&gt;</li>
<li>&nbsp; &nbsp;&lt;track kind=captions src=brave.en.hoh.vtt </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang=en </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;label="English for the Hard of Hearing"&gt;</li>
<li>&nbsp; &nbsp;&lt;track kind=subtitles src=brave.fr.vtt </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang=fr </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lang=fr&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label="Français"&gt;</li>
<li>&nbsp; &nbsp;&lt;track kind=subtitles src=brave.de.vtt </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; srclang=de </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; lang=de </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label="Deutsch"&gt;</li>
<li>&lt;/video&gt;</li>
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

<div style="line-height: 23.2727279663086px;"><ol>
<li value="1">&lt;video&nbsp;height="272"&nbsp;width="640"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;poster="https://mainline.i3s.unice.fr/mooc/q1fx20VZ-640.jpg"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;crossorigin="anonymous"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;controls&gt;</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;&lt;track&nbsp;src="https://mainline.i3s.unice.fr<span style="background-color: #eeeeee;">/mooc/<strong>sintel-captions.vtt</strong>"</span></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;kind="captions"&nbsp;label="Closed Captions"&nbsp;default&gt;</li>
<li>&lt;/video&gt;</li>
</ol></div>

And here is an extract of the corresponding [sintel-captions.vtt](https://mainline.i3s.unice.fr/mooc/sintel-captions.vtt) file:

<div><ol>
<li value="1">WEBVTT</li>
<li> </li>
<li>00:00:01.000 --&gt; 00:00:02.042</li>
<li>(drumbeat)</li>
<li> </li>
<li>00:00:07.167 --&gt; 00:00:12.025</li>
<li>(plaintive violin solo playing)</li>
<li> </li>
<li>00:00:15.000 --&gt; 00:00:18.183</li>
<li>(wind whistling)</li>
<li> </li>
<li>00:00:24.167 --&gt; 00:00:27.025</li>
<li>(orchestra music swells)</li>
<li> </li>
<li>00:00:43.033 --&gt; 00:00:43.192</li>
<li>(weapons clash)</li>
<li> </li>
<li>00:00:44.000 --&gt; 00:00:44.175</li>
<li>(gasps)</li>
<li> </li>
<li>00:00:44.183 --&gt; 00:00:45.158</li>
<li>(grunts)</li>
<li> </li>
<li>00:00:45.167 --&gt; 00:00:47.058</li>
<li>(groaning)</li>
<li> </li>
<li>00:00:54.192 --&gt; 00:00:55.150</li>
<li>(blade rings)</li>
<li> </li>
<li>00:00:55.158 --&gt; 00:00:57.008</li>
<li>(bellowing)</li>
<li> </li>
<li>00:00:57.017 --&gt; 00:00:58.067</li>
<li>(grunting)</li>
<li> </li>
<li>00:00:59.075 --&gt; 00:01:00.133</li>
<li>(panting)</li>
<li> </li>
<li>00:01:05.108 --&gt; 00:01:06.125</li>
<li>(cries out in agony)</li>
<li> </li>
<li>00:01:08.050 --&gt; 00:01:09.058</li>
<li>(panting)</li>
<li> </li>
<li>00:01:12.092 --&gt; 00:01:13.142</li>
<li>(panting)</li>
<li> </li>
<li>00:01:14.017 --&gt; 00:01:18.125</li>
<li>(orchestra plays ominous low notes)</li>
<li> </li>
<li>00:01:31.058 --&gt; 00:01:35.133</li>
<li>(plaintive violin solo returns)</li>
<li> </li>
<li>00:01:46.158 --&gt; 00:01:49.058</li>
<li>This blade has a dark past.</li>
<li> </li>
<li>00:01:51.092 --&gt; 00:01:54.108</li>
<li>It has shed much innocent blood.</li>
<li> </li>
<li>00:01:57.083 --&gt; 00:02:00.000</li>
<li>You're a fool for traveling alone </li>
<li> so completely unprepared. </li>
<li> </li>
<li>00:02:01.100 --&gt; 00:02:03.033</li>
<li>You're lucky your blood's still flowing.</li>
<li> </li>
<li>00:02:04.183 --&gt; 00:02:06.075</li>
<li>Thank you.</li>
</ol></div>

This format is rather simple, but we still recommend reading [this excellent article from Mozilla Developer Network](https://tinyurl.com/y3sxj9a3) that explains in detail all the different options.

Each "element" in this file has a starting and ending time, plus a value (the text that will be displayed), followed by a blank line (blank lines are separators between elements).

__Each element is called "a cue"__, and may optionally have an ID that will be useful when using the track element JavaScript API, in particular the `getCueById()` method of `TextTrack` objects. How to use these will be taught in the "advanced HTML5" course, soon on W3Cx

Example of numeric IDs:

<div><ol>
<li value="1">9</li>
<li>00:00:21.000 --&gt; 00:00:22.000 </li>
<li>to hear from &lt;u&gt;you&lt;/u&gt;</li>
<li> </li>
<li>10</li>
<li>00:00:22.500 --&gt; 00:00:25.000 </li>
<li>We want to hear what inspires you as a developer</li>
</ol></div>

IDs may also be defined as strings, and values can use HTML as well:

<div><ol>
<li value="1">Opening</li>
<li>00:00:00.000 --&gt; 00:00:30.000 </li>
<li>Welcome to our &lt;i&gt;nice film&lt;/i&gt;</li>
</ol></div>

The displayed text can span multiple lines, but blank lines are not allowed, as they would be interpreted as a separator:

<div><ol>
<li value="1">00:01:57.083 --&gt; 00:02:00.000</li>
<li>&lt;p&gt;You're a fool for traveling alone&lt;/p&gt;</li>
<li>&lt;p&gt;so completely unprepared.&lt;/p&gt;</li>
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

<div><ol>
<li value="1">&lt;video id="myVideo" width=500 controls&gt;</li>
<li>&nbsp;&nbsp;&lt;source&nbsp;&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; src="videos/SameOldSongAndDanceRogerLathaudPart1MidRes.mp4" </li>
<li>&nbsp; &nbsp; &nbsp; type="video/mp4"&gt;</li>
<li>&nbsp; &lt;source&nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; src="videos/SameOldSongAndDanceRogerLathaudPart1MidRes.webm" </li>
<li>&nbsp; &nbsp; &nbsp; type="video/webm"&gt;</li>
<li>&nbsp;</li>
<li>&nbsp;&nbsp;&lt;track src="videos/subtitles.vtt"&nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;kind="subtitles"&nbsp;srclang="en"&nbsp;default&gt;</li>
<li>&lt;/video&gt; </li>
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

<div><ol>
<li value="1">WEBVTT</li>
<li> </li>
<li>00:00:01.000 --&gt; 00:00:05.000</li>
<li>These captions test some features of the WebVTT formats </li>
<li> </li>
<li>00:00:06.000 --&gt; 00:00:10.000<strong> line:5%</strong></li>
<li>This cue is positioned at the top of the video</li>
<li> </li>
<li>00:00:11.000 --&gt; 00:00:15.000<strong> position:5% align:start</strong></li>
<li>This cue is positioned at the left side of the video.</li>
<li> </li>
<li>00:00:16.000 --&gt; 00:00:20.000 position:95%<strong> align:end</strong></li>
<li>And this one ate the right side.</li>
<li> </li>
<li>00:00:21.000 --&gt; 00:00:25.000<strong> size:33%</strong></li>
<li>This cue is only a third of the width of the video, hence the multiple line breaks.</li>
<li> </li>
<li>00:00:26.000 --&gt; 00:00:30.000</li>
<li>This cue contains <strong>&lt;b&gt;</strong>bold<strong>&lt;/b&gt;</strong> text.</li>
<li> </li>
<li>00:00:31.000 --&gt; 00:00:35.000</li>
<li>This cue contains <strong>&lt;i&gt;</strong>italic<strong>&lt;/i&gt;</strong> text.</li>
<li> </li>
<li>00:00:36.000 --&gt; 00:00:40.000</li>
<li>This cue contains <strong>&lt;u&gt;</strong>underlined<strong>&lt;/u&gt;</strong> text.</li>
<li> </li>
<li>00:00:41.000 --&gt; 00:00:45.000</li>
<li>This cue contains <strong>&lt;b&gt;&lt;i&gt;&lt;u&gt;</strong>bold, italic, underlined<strong>&lt;/u&gt;&lt;/i&gt;&lt;/b&gt;</strong> text.</li>
<li> </li>
<li>00:00:46.000 --&gt; 00:00:50.000</li>
<li><strong>&lt;c.myclass&gt;</strong>This cue contains the class "myclass". </li>
<li>Browsers that support ::cue CSS should make it red.<strong>&lt;/</strong><strong>c&gt;</strong></li>
<li> </li>
<li>00:00:51.000 --&gt; 00:00:55.000</li>
<li>The following cue contains two voices.</li>
<li>Tarzan should be blue and Jane green.</li>
<li> </li>
<li>00:00:56.000 --&gt; 00:01:00.000</li>
<li>&lt;v Tarzan&gt;Me Tarzan...</li>
<li>&lt;v Jane&gt;That would make me Jane!</li>
<li> </li>
<li>bigtext</li>
<li>00:01:01.000 --&gt; 00:01:05.000</li>
<li>This cue has a unique id.</li>
<li>Using CSS, its font size should be 150%.</li>
<li> </li>
<li>00:01:06.000 --&gt; 00:01:10.000</li>
<li>The &lt;00:01:06.333&gt;text &lt;00:01:06.666&gt;in &lt;00:01:07.000&gt;this &lt;00:01:07.333&gt;cue &lt;00:01:07.666&gt;should &lt;00:01:08.000&gt;grow</li>
<li>&lt;00:01:08.333&gt;one &lt;00:01:08.666&gt;word &lt;00:01:09.000&gt;at &lt;00:01:09.333&gt;a &lt;00:01:09.666&gt;time</li>
<li> </li>
<li>00:01:11.000 --&gt; 00:01:15.000</li>
<li>That's it! For now...</li>
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

<div><ol>
<li value="1">00:00:11.000 --&gt; 00:00:15.000<strong><span style="color: #ff0000;"> position:5% align:start</strong></li>
<li>This cue is positioned at the left side of the video.</li>
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

<div><ol>
<li value="1">&lt;c.myclass&gt;This cue contains the class "myclass". </li>
<li>Browsers that support ::cue CSS should make it red.&lt;/c&gt;</li>
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

<div><ol>
<li value="1"> &lt;style type="text/css"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;::cue(.myclass) { color: red; }</li>
<li>&nbsp; &nbsp; &nbsp;::cue(v[voice="Tarzan"]) { color: blue; }</li>
<li>&nbsp; &nbsp; &nbsp;::cue(v[voice="Jane"]) { color: green; }</li>
<li>&nbsp; &nbsp; &nbsp;::cue(#bigtext) { font-size: 150%; }</li>
<li> &lt;/style&gt;</li>
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

<div><ol>
<li value="1">00:00:56.000 --&gt; 00:01:04.000</li>
<li>&lt;v Tarzan&gt;Me Tarzan...</li>
<li>&lt;v Jane&gt;That would make me Jane</li>
</ol></div>


#### Knowledge check 2.3.4

1. Is it possible to use CSS for styling subtitles or captions? (Yes/No)

  Ans: Yes <br/>
  Explanation: Yes, CSS can be used since subtitles and captions can be pure HTML with id and class attributes. They can also include spans, bold, italic markers, etc.


### 2.3.5 Chapters

Adding chapters is very similar to adding subtitles/captions. Look at line 5 in the code below, where we use an extra `<track>` element with a `kind="chapters"` attribute.

<div><ol>
<li value="1">&lt;video poster="webvtt_talk.png" style="width:100%" preload="metadata"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="webvtt_talk.webm"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="webvtt_talk.mp4"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="webvtt_talk.ogv"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track id="nav" src="webvtt_talk_navigation.vtt" <strong>kind="chapters"</strong> srclang="en"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;track id="cc" src="webvtt_talk_captions.vtt" kind="captions" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; label="captions" srclang="en" default&gt;</li>
<li>&lt;/video&gt;</li>
</ol></div>

Here is an example of WebVTT files with defined chapters. Each "CUE" at lines 3, 7, 11, ... can bear any name. We use "Chapter 1, Chapter 2, Ending, etc." but you are free to name them as you choose.

What makes them special is that the track has an attribute `kind="chapters"`. 

It's also easy to process them, and for example, to generate a custom navigation menu, using the `<track>` JavaScript API (explained later in this section).

Example of a WebVTT file that defines chapters:

<div><ol>
<li value="1">WEBVTT FILE</li>
<li>&nbsp;</li>
<li><span style="color: #660066;" color="#660066">Chapter&nbsp;1</li>
<li>00:00:00.000 --&gt; 00:00:10.700</li>
<li>Title Slide</li>
<li>&nbsp;</li>
<li>Chapter&nbsp;2</li>
<li>00:00:10.700 --&gt; 00:00:47.600</li>
<li>Introduction by Naomi Black</li>
<li>&nbsp;</li>
<li>Chapter&nbsp;3</li>
<li>00:00:47.600 --&gt; 00:01:50.100</li>
<li>Impact of Captions on the Web</li>
<li>&nbsp;</li>
<li>Chapter&nbsp;4</li>
<li>00:01:50.100 --&gt; 00:03:33.000</li>
<li>Requirements of a Video text format</li>
<li>&nbsp;</li>
<li><span style="color: #660066;" color="#660066">Ending</li>
<li>00:03:33.000 --&gt; 00:04:57.766</li>
<li>Simple WebVTT file</li>
<li>&nbsp;</li>
<li><span style="color: #660066;" color="#660066">Greetings&nbsp;6</li>
<li>00:04:57.766 --&gt; 00:06:16.666</li>
<li>Styled WebVTT file</li>
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


### 2.3.7 The `<track>` JavaScript API

The `<track>` element comes with a powerful API that is used to develop many interesting features such as:

+ Dynamically building a navigation menu that shows the different chapters of the video,
+ Synchronizing page content with timestamps in the WebVTT file (for example: show a map next to the video, that shows the location corresponding to the video content),
+ Displaying all the subtitles/captions at once as HTML in the page,
+ Making an app for creating on the fly subtitles/captions,
+ Etc.

#### Examples of use

__Add a navigation menu to start playing the video at given chapters__

This example shows a video with an enhanced progress bar that displays the different chapters as small "clickable" squares. Furthermore, using the JavaScript API of the <track> element, this Web site builds a navigation menu (on the right of the video):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y2rw88n4')"
    src    ="https://tinyurl.com/y3p6k8xa"
    alt    ="navigation menu using the track javascript api"
    title  ="navigation menu using the track javascript api"
  />
</figure>


__Sync video with Google Map and Google Street View__

Check [this demo](https://simpl.info/track/map/index.html) (only on Chrome) by [Sam Dutton](https://samdutton.com/): it shows a video that comes with a WebVTT file that contains longitudes and latitudes. When the video plays, JavaScript functions are called at given times and get the longitude and latitude. A Google Map and a Google Street views are updated in real time.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 35vw;"
    onclick="window.open('https://tinyurl.com/y2rw88n4')"
    src    ="https://tinyurl.com/y5ox7v9s"
    alt    ="video sync with map and street view"
    title  ="video sync with map and street view"
  />
</figure>


__Sync guitar tablatures and music score with a video__

This example shows how we manage to render music scores in real time as the video plays. 

Some JavaScript code listens to the `ontimeupdate` event while the video is playing. We use the `currentTime` property of the video to know exactly where we are in the video. Finally, we also rely on an external library to render in an HTML5 canvas the bars corresponding to the current video explanations. We render in real time guitar pro tablatures using the alphatab.net library.

<a href="https://youtu.be/JyNSyL-MmFI" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="demo video" width=150/>
</a><br/>


### 2.3.8 Enhanced HTML5 video players

There are numerous "enhanced" video players; most are free and open source, some are commercial. They offer lots of features, which are listed below. Not all of these features are available in every player, this list just illustrates what can be added to the standard `<video>` element. 

We call them "HTML5 enhanced video players" because on top of being based on the `<video>` element, they come with custom features, custom look'n'feel, chapters, etc., based on a JavaScript API that makes such customizations possible.


#### Accessible players

For those of you interested in this particular topic, here is a very good resource that compares most of the players presented in this section, in terms of accessibility. This resource has links to players designed especially for people with disabilities: [accessible media players and resources](https://tinyurl.com/yywpkanp).


#### Advantages and disadvantages of using a custom player

__Advantages of enhanced video players:__

+ Support for all kinds of subtitle formats
+ Customizable look'n'feel (add your logo, custom themes, etc.)
+ Full screen mode without borders on old browsers (today's implementations of the `<video>` element support full screen mode)
+ Consistent look'n'feel across browsers (menus for subtitles, etc.)
+ 1.5x, 2x, 3x speeds for fast playback
+ Social buttons for sharing on Facebook, Twitter, etc.
+ Support for chapters
+ Support for scrub bar thumbnails
+ Extra features for better accessibility
+ And so on...

__Advantages of relying only on the `<video>` element  rather than on an enhanced player:__

+ Total control!
+ No need for external dependencies
+ Lightweight: no need to download lots of JavaScript and CSS code (also, Flash fallbacks in some cases)


#### Video.js: a framework for building your own custom video player

Open source, and made for developers, [video.js](https://videojs.com/) comes with many plugins (chapters, thumbnails etc.). 

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y2ndcobj')"
    src    ="https://tinyurl.com/y35sl96w"
    alt    ="VideoJS examples"
    title  ="VideoJS examples"
  />
</figure>


__Which should I use? the `<video>` element and my own customizations or an out of the box enhanced player?__

Either solution (basic player or enhanced player) is good and HTML5 compliant.

Popular players such as [JWPlayer](https://www.jwplayer.com/) have many explanations and examples on their Web sites, and are either free of charge or come with free versions.

Interesting comparisons and reviews are available on the following Web sites:

+ Comparison matrix of most of [existing HTML5 video players](https://videosws.praegnanz.de/)
+ [10 HTML5 video players compared](https://tinyurl.com/y4fmzwwd)


#### Example screenshots

Scrub Bar thumbnails (JWPlayer)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y2ndcobj')"
    src    ="https://tinyurl.com/y4v7ajv2"
    alt    ="scrub bar thumbnails"
    title  ="scrub bar thumbnails"
  />
</figure>


Custom look'n'feel and logo (Sublime video player):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y2ndcobj')"
    src    ="https://tinyurl.com/y6bko6jz"
    alt    ="custom look'n'feel and logo"
    title  ="custom look'n'feel and logo"
  />
</figure>


Chapters and chapter thumbnails (JWPlayer):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y2ndcobj')"
    src    ="https://tinyurl.com/y28oo95x"
    alt    ="chapters and chapter thumbnails"
    title  ="chapters and chapter thumbnails"
  />
</figure>


PayPal accessible player:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y2ndcobj')"
    src    ="https://tinyurl.com/y5cwgplp"
    alt    ="paypal accessible player"
    title  ="paypal accessible player"
  />
</figure>


LeanBack (says "free for non-commercial use", licensing is not very clear...):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y2ndcobj')"
    src    ="https://tinyurl.com/y3njxae3"
    alt    ="leanback free and open source"
    title  ="leanback free and open source"
  />
</figure>


### 2.3.9 Discussion and projects

Here is the discussion forum dedicated to "closed captions and subtitles". Do not hesitate to post comments and questions, as well as to share your creations here.

Some topics of discussion and optional projects:

#### Suggested topics

+ What tools do you use for adding subtitles to videos?
+ Did you have problems with encoding foreign languages?
+ What subtitle format do you use? WebVTT or .srt or something else?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will all be glad to try them and give some feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

__Project 1 (very easy)__: add some subtitles of your own on one of your videos. Share your step by step experience. This will be a valuable resource for your classmates.

See an example that might help:

+ [Very simple example on JsBin with a video and subtitles](https://jsbin.com/jicanav/2/edit?html,css,output). Note the use of the `crossorigin` attribute of the `<video>` element. The subtitles were created by hand (using amara).

__Project 2 (easy)__: try to style some of the subtitles, set their position, etc.

Example that can help:

+ Try it on JSBin: [Samurai Pizza Cat](https://jsbin.com/fadayoq/3/edit?html,css,output) with subtitled lyrics grabbed from the [Wikiquote Web site](https://en.wikiquote.org/wiki/Samurai_Pizza_Cats#Main_Title_Song), and synchronized using [amara](https://amara.org/en/).

__Project 3 (with JavaScript knowledge)__: Please write a karaoke player with a small list of songs for people to choose from.


