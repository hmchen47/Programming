# Week 2: HTML5 Multimedia


## 2.5 Exercises - Week 2


### 2.5.1 Intro exercises - Week 2


Here is your opportunity to show that you can now play with multimedia content on the Web, and are ready to proceed with the rest of the course.

Please complete the following 25 exercises in a timely manner. As stated in the grading policy page, they count towards 15% of your final grade.
 

### 2.5.2 Quiz - `<audio>` and `<video>` (1-4)

1. Streaming?

  The `<audio>` and `<video>` elements are for streaming multimedia content. (True/False)

  Ans: True<br/>
  Explanation: Yes, content played when using these elements is streamed from a remote server to the browser: a small part of the remote audio or video files is loaded in a buffer, and the media starts being played as soon as the buffer is full enough. Insufficient bandwidth may lead to the media being stopped in the middle if the buffer becomes empty.


2. The codec nightmare!

  <pre>&lt;video width="320" height="240" controls&gt;
    &lt;source src="movie.mp4" type="video/mp4" /&gt;
    &lt;source src="movie.ogg" type="video/ogg" /&gt;
    Your browser does not support the &lt;video&gt; element.
  &lt;/video&gt;</pre>

  Why did we provide two different source entries in the above video element?<br/>

  a. The browser will first use the format/codec it supports, or in some cases it will choose its "preferred" format/codec. Furthermore, some browsers do not recognize all codecs.<br/>
  b. This is actually useless as all browsers know how to play all popular formats/codecs.<br/>
  c. It is a requirement to propose at least two codecs.<br/>

  Ans: a<br/>
  Explanation: It is always better to propose a video with different encodings. Usually, the browser will play the first one it is able to decode; also, some browsers may choose one particular codec if they support more than one of the proposed encodings.
  

3. YouTube in your video element

  <pre>&lt;video width="560" height="315" src="https://www.youtube.com/embed/ZH1XOsv8Oyo"&gt;
  &lt;/video&gt;</pre>

  Will the above YouTube video example work (note that the video has public access)?<br/>

  a. Yes, but we need to have a YouTube account<br/>
  b. No<br/>
  c. Yes, without any constraint<br/>
  
  Ans: b<br/>
  Explanation: No, while the YouTube player is pure HTML5 and is based on the `<video>` element, YouTube only allows their videos to be embedded using an `<iframe>` element, as they inject advertising and do a lot more data processing than you can ever imagine.


4. Audio reduction!

  Are the attributes, event set and JavaScript API of the `<audio>` element <u>exactly</u> the same as those of the `<video>` element? (Yes/No)

  Ans: No<br/>
  Explanation: No, the attributes, event set and JavaScript API of the `<audio>` element are just a "reduced" version of the ones from the `<video>` element.



### 2.5.3 Quiz - Attributes of `<audio>` and `<video>` (5-8)

5. Lost attributes...

  Which of the following are valid attributes for the `<audio>` and `<video>` elements? (4 correct answers.)<br/>

  a. stream<br/>
  b. controls<br/>
  c. src<br/>
  d. loop<br/>
  e. looping<br/>
  f. autoplay<br/>

  Ans: bcdf<br/>
  Explanation: Correct attributes in the list are: controls, src, loop, and autoplay.


6. Dangerous attributes!

  Which attribute is not recommended with mobile browsers or with documents that contain multiple videos?<br/>

  a. src<br/>
  b. controls<br/>
  c. autoplay<br/>
  d. poster<br/>
  e. loop<br/>

  Ans: c<br/>
  Explanation: The `autoplay` attribute is not recommended if your Web site targets mobile applications or has documents with multiple videos, as it may consume bandwidth even if the user is not interested in watching/listening to the proposed video/audio.


7. Recommended attributes

  What is considered good practice when you target mobile applications, or when your document contains a lot of audios/videos? (2 correct answers.)<br/>

  a. use the autoplay attribute in audio and video elements<br/>
  b. use the attribute preload="none" in audio and video elements<br/>
  c. use the loop attribute in audio and video elements<br/>
  d. omit the autoplay attribute in audio and video elements<br/>
  
  Ans: bd<br/>
  Explanation: The `autoplay` attribute is not recommended if your Web site targets mobile applications or dislays documents with multiple videos, as it may consume bandwidth even if the user is not interested in watching/listening to the proposed video/audio. `preload="none"` is also highly recommended as the default value is "auto" and that may cause preloading data.


8. HTML5 relaxed syntax and boolean attributes

  We would like to have play/stop/pause buttons in our audio or video player. What should be added to the declaration of the video element? (2 correct answers.)<br/>

  a. If we want just a play/pause button, but no stop button, we will add two attributes: `play="true"` and `stop="false"`<br/>
  b. Just add an attribute named "controls" like in `<audio controls>`<br/>
  c. Same as above, but you can also use `<audio controls="controls">`<br/>
  d. Add this attribute: `showcontrols`<br/>

  Ans: bd<br/>
  Explanation:
    + Right answer: add the `controls` boolean attribute.
    + From the HTML5 specification: "A number of attributes are boolean attributes. The presence of a boolean attribute on an element represents the true value, and the absence of the attribute represents the false value.
    + If the attribute is present, its value must either be the empty string nor a value that is an ASCII case-insensitive match for the attribute's canonical name, with no leading or trailing whitespace.
    + The values "true" and "false" are not allowed on boolean attributes. To represent a false value, the attribute has to be omitted altogether. This means that controls="false" will be the same as controls="true" or controls="controls" or controls alone.
    + It is bad practice to use controls="true" as one might think that controls="false" will have the opposite effect (and it won't: in order not to have controls, just ommit the attribute).
    + To sum up, the right answers are: only adding controls or controls="controls". Both are valid.


### 2.5.4 Quiz - CSS styling of `<audio>` and `<video>` (9-10)

9. Make me twist!

  <pre>&lt;style&gt;
      #W3DevCampusVideo {
          width: 300px;
          transition: all 0.5s ease-in-out;
      }
  
      #W3DevCampusVideo:hover {
          width:400px;
          transform:rotate(-5deg);
      }
  &lt;/style&gt;
  ...
  &lt;video id="W3DevCampusVideo" autoplay controls&gt;
      &lt;source src=https://html5doctor.com/demos/video-canvas-magic/video.webm
              type=video/webm&gt;
      &lt;source src=https://html5doctor.com/demos/video-canvas-magic/video.ogg
              type=video/ogg&gt;
      &lt;source src=https://html5doctor.com/demos/video-canvas-magic/video.mp4
              type=video/mp4&gt;
  &lt;/video&gt;</pre>

  What will the above code do?<br/>

    a. Play a 300px video as soon as it is ready, rotate and resize it to 400px instantaneously.<br/>
    b. Play a 300px video as soon as it is ready, rotate and resize it to 400px smoothly when the mouse cursor comes over it.<br/>
    c. The CSS rules will be ignored as the video element cannot be resized or rotated on the fly once it has started playing.<br/>
    d. Play a rotated video at size 400px as soon as the streamed content is ready to be played.<br/>

  Ans: b<br/>
  Explanation: The second answer is correct: the video will play when the buffer is full enough, then if we put the mouse cursor over the video, it will smoothly resize and rotate (in 0.5s).
  


10. Buttons with style!

  Does HTML5 enable us to change the style of default players' controls (the play/pause/stop buttons that appear when we add the controls attribute to an audio or video element)?

    a. No, this is not possible.<br/>
    b. No need to use JavaScript, the audio and video elements expose these controls, read the documentation to get their IDs and use CSS for that.<br/>
    c. Yes, with JavaScript it's possible to use the DOM API to select and modify the different buttons of the default control bar.<br/>

  Ans: <span style="color: magenta;">a</span>, xc<br/>
  Explanation: 
    + Unfortunately, the standard control bar cannot be accessed using CSS or the DOM API. Instead, hide the standard controls (ommit the controls attribute) and use your own HTML buttons, sliders, etc. to control the audio or video element using their JavaScript API.
    + Advanced users may argue that in some browsers, the audio and video players are implemented using Web Components, and that by setting some options in the devtools of the browser, it's possible to access the control bar widgets through the shadow DOM. But this is not something that would work on any browsers with default settings. Web Components will be studied in the HTML5 part-2 course.



### 2.5.5 Quiz - JavaScript API (11-15)

11. JavaScript API?

  What do we mean by "audio and video elements have a JavaScript API"?<br/>

  a. They have properties, events and methods that can be manipulated from JavaScript<br/>
  b. They are written 100% in JavaScript<br/>

  Ans: a<br/>
  Explanation: Indeed, it means that, from JavaScript, we are able to call the `play()`, `stop()`, `pause()` methods, access the current time through the `currentTime` property or listen to progress events (for example when synchronizing things when a video is played).


__Source code for the next 3 questions (12, 13 and 14)__

<div class="source-code"><ol class="linenums">
<li value="1" class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"vid"</span><span class="pln">&nbsp;poster="preview.png"&nbsp;</span><span class="atn">controls</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">="</span><span class="atv">https://html5doctor.com/demos/video-canvas-magic/video.mp4"</span><span class="pln"></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type</span><span class="pun">="</span><span class="atv">video/mp4"</span>&gt;</li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span><span class="pln">Example of custom controls :</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">class</span><span class="pun">=</span><span class="atv">"mybutton"</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">go</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln" style="line-height: 1.6;">Play</span><span class="tag" style="line-height: 1.6;">&lt;/button&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">class</span><span class="pun"></span><span class="pun">=</span><span class="atv">"mybutton"</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">haveARest</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln" style="line-height: 1.6;">Pause</span><span class="tag" style="line-height: 1.6;">&lt;/button&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">class</span><span class="pun"></span><span class="pun">=</span><span class="atv">"mybutton"</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">rewind</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln" style="line-height: 1.6;">Start from beginning</span><span class="tag" style="line-height: 1.6;">&lt;/button&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; vid </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#vid"</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> go</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; vid</span><span class="pun">.<strong>BBB</strong></span><span class="pun">();</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; </span><span class="kwd">function</span><span class="pln"> haveARest</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; vid</span><span class="pun">.<strong>CCC</strong></span><span class="pun">();</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">function</span><span class="pln"> rewind</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; vid</span><span class="pun">.<strong>DDD</strong></span><span class="pln">&nbsp;</span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
</ol></div>

12. Which method to start?

  Which method would you call to start playing the video, instead of BBB?<br/>

  a. `go()`<br/>
  b. `play()`<br/>
  c. `start()`<br/>

  Ans: b<br/>
  Explanation: There is no `start()` nor `go()` method in the JavaScript API of the video element. The right answer is `play()`.



13. Which method to pause?

  Which method would you call to pause the video, instead of CCC?<br/>

  a. `stop()`<br/>
  b. `pause()`<br/>
  c. `cancel()`<br/>

  Ans: b<br/>
  Explanation: There is no `cancel()` in the JavaScript API of the video element. The `stop()` method exists but it is for stopping the video (and once stopped, it cannot be resumed). The right answer is the `pause()` method.


14. Be kind, rewind!

  Which property would you use to rewind completely the video without stopping it (playback continues as if we jumped to the beginning), instead of the DDD string in the source code above? <br/>

  a. progress<br/>
  b. location<br/>
  c. currentTime<br/>
  d. time<br/>
  
  Ans: c<br/>
  Explanation: The `currentTime` property is in read/write. Its value changes during playback, but if we give it a value, then the video "jumps" to the position that corresponds to its value (in seconds).



15. Event for playlists?

  Which event is used in the course to detect the end of video and implement playlist management?<br/>

  a. end<br/>
  b. chained<br/>
  c. ended<br/>
  d. finished<br/>
  e. finish<br/>

  Ans: c<br/>
  Explanation: The course examples use the `ended` event to detect the end of a video playback. See the code from the example 1 in section 2.2.7 for instance: http://jsbin.com/temupe/1/edit.



### 2.5.6 Quiz - Closed captions and subtitles (16-21)

__Source code for the next 3 questions (16, 17 and 18):__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;video</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"272"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"640"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">poster</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/sintel.jpg"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">crossorigin</span><span class="pun">=</span><span class="atv">"anonymous"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">controls</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/sintel.mp4"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/mp4"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;source</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/sintel.webm"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"video/webm"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;track</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mainline.i3s.unice.fr/mooc/sintel-captions.vtt"</span><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>AAA</strong></span><span class="pun">=</span><span class="atv">"captions"</span><span class="pln"> </span><strong><span class="atn">BBB</span></strong><span class="pun">=</span><span class="atv">"Closed Captions"</span><span class="pln"> </span><strong><span class="atn">CCC</span></strong><span class="pun">=</span><span class="atv">"en"</span><span class="pln"> </span><span class="atn">default</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/video&gt;</span></li>
</ol></div>

16. Captions or subtitles

  What is the name of the attribute for setting the track type? What would you use instead of the AAA string in the source code above?

  Ans: <br/>
  Explanation: 



17. Nice subtitle/caption menu in the player?

  What is the name of the attribute whose role is to inform the browser of the subtitle's description (to appear in the player menu when choosing subtitles)? What would you use instead of the BBB string in the source code above?

  Ans: <br/>
  Explanation: 


18. Which language?

  What is the name of the attribute which will tell the browser what language is used by the track subtitles/captions? What would you use instead of the CCC string in the source code above?

  Ans: <br/>
  Explanation: 


19. Nice subtitles

  Extract from a .vtt file:

  <pre class="prettyprint  linenums:1">00:00:41.000 --&gt; 00:00:45.000
  This course is about &lt;b&gt;&lt;i&gt;&lt;u&gt;HTML5!&lt;/u&gt;&lt;/i&gt;&lt;/b&gt;.</pre>

  Is the above code correct? (Yes/No)

  Ans: <br/>
  Explanation: 


20. Karaoke duo?

  How can we distinguish different voices, to be displayed in different colors, in subtitles/captions (for example, a karaoke duo)?<br/>

  a. Use <v nameOfVoice> followed by the text of the subtitle, like in: <v Michel> Hello dear students of this W3Cx course!<br/>
  a. Use <voice nameOfVoice> followed by the text of the subtitle, like in <voice Michel> Hello dear students of this W3Cx course!<br/>

  Ans: <br/>
  Explanation: 



