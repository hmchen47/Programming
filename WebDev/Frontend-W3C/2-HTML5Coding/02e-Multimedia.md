# Week 2: HTML5 Multimedia


## 2.5 Exercises - Week 2
 

### 2.5.1 Intro exercises - Week 2


Here is your opportunity to show that you can now play with multimedia content on the Web, and are ready to proceed with the rest of the course.

Please complete the following 25 exercises in a timely manner. As stated in the grading policy page, they count towards 15% of your final grade.
  

### 2.5.2 `<audio>` and `<video>` (1-4)

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



### 2.5.3 Attributes of `<audio>` and `<video>` (5-8)

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

  Ans: bc<br/>
  Explanation:
    + Right answer: add the `controls` boolean attribute.
    + From the HTML5 specification: "A number of attributes are boolean attributes. The presence of a boolean attribute on an element represents the true value, and the absence of the attribute represents the false value.
    + If the attribute is present, its value must either be the empty string nor a value that is an ASCII case-insensitive match for the attribute's canonical name, with no leading or trailing whitespace.
    + The values "true" and "false" are not allowed on boolean attributes. To represent a false value, the attribute has to be omitted altogether. This means that controls="false" will be the same as controls="true" or controls="controls" or controls alone.
    + It is bad practice to use controls="true" as one might think that controls="false" will have the opposite effect (and it won't: in order not to have controls, just ommit the attribute).
    + To sum up, the right answers are: only adding controls or controls="controls". Both are valid.


### 2.5.4 CSS styling of `<audio>` and `<video>` (9-10)

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



### 2.5.5 JavaScript API (11-15)

11. JavaScript API?

  What do we mean by "audio and video elements have a JavaScript API"?<br/>

  a. They have properties, events and methods that can be manipulated from JavaScript<br/>
  b. They are written 100% in JavaScript<br/>

  Ans: a<br/>
  Explanation: Indeed, it means that, from JavaScript, we are able to call the `play()`, `stop()`, `pause()` methods, access the current time through the `currentTime` property or listen to progress events (for example when synchronizing things when a video is played).


__Source code for the next 3 questions (12, 13 and 14)__

<div><ol>
<li value="1">&lt;video id="vid"&nbsp;poster="preview.png"&nbsp;controls&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;source src="https://html5doctor.com/demos/video-canvas-magic/video.mp4"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type="video/mp4"&gt;</li>
<li>&lt;/video&gt; </li>
<li>&lt;p&gt;Example of custom controls :&lt;/p&gt;</li>
<li>&nbsp;</li>
<li>&lt;button class="mybutton" onclick="go();"&gt;<span style="line-height: 1.6;">Play&lt;/button&gt;</span></li>
<li>&lt;button class="mybutton" onclick="haveARest();"&gt;<span style="line-height: 1.6;">Pause&lt;/button&gt;</span></li>
<li>&lt;button class="mybutton" onclick="rewind();"&gt;<span style="line-height: 1.6;">Start from beginning</span>&lt;/button&gt;</li>
<li>&nbsp;</li>
<li>&lt;script&gt;</li>
<li>&nbsp; vid = document.querySelector("#vid");</li>
<li> </li>
<li>&nbsp;&nbsp;function go() {</li>
<li>&nbsp; &nbsp; vid.<strong>BBB</strong>();</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp; function haveARest() {</li>
<li>&nbsp; &nbsp; vid.<strong>CCC</strong>();</li>
<li>&nbsp;&nbsp;}</li>
<li> </li>
<li>&nbsp;&nbsp;function rewind() {</li>
<li>&nbsp; &nbsp; vid.<strong>DDD</strong>&nbsp;= 0;</li>
<li>&nbsp;&nbsp;}</li>
<li>&lt;/script&gt;</li>
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



### 2.5.6 Closed captions and subtitles (16-21)

__Source code for the next 3 questions (16, 17 and 18):__

<div><ol>
<li value="1">&lt;video height="272" width="640"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;poster="https://mainline.i3s.unice.fr/mooc/sintel.jpg"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;crossorigin="anonymous"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;controls&gt;</li>
<li>&nbsp; &nbsp;&lt;source src="https://mainline.i3s.unice.fr/mooc/sintel.mp4"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/mp4"&gt;</li>
<li>&nbsp; &nbsp;&lt;source src="https://mainline.i3s.unice.fr/mooc/sintel.webm"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="video/webm"&gt;</li>
<li>&nbsp; &nbsp;&lt;track src="https://mainline.i3s.unice.fr/mooc/sintel-captions.vtt"&nbsp; &nbsp; &nbsp; &nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>AAA</strong>="captions" <strong>BBB</strong>="Closed Captions" <strong>CCC</strong>="en" default&gt;</li>
<li>&lt;/video&gt;</li>
</ol></div>

16. Captions or subtitles

  What is the name of the attribute for setting the track type? What would you use instead of the __AAA__ string in the source code above?

  Ans: kind<br/>
  Explanation: The correct attribute is `kind`, like in: `kind="subtitles"` or `kind="captions"`.



17. Nice subtitle/caption menu in the player?

  What is the name of the attribute whose role is to inform the browser of the subtitle's description (to appear in the player menu when choosing subtitles)? What would you use instead of the __BBB__ string in the source code above?

  Ans: label<br/>
  Explanation: The correct attribute is `label`, like in: `label="English for the Hard of Hearing"` or `label="French"`.


18. Which language?

  What is the name of the attribute which will tell the browser what language is used by the track subtitles/captions? What would you use instead of the __CCC__ string in the source code above?

  Ans: srclang<br/>
  Explanation: The correct attribute is `srclang`, like in: `srclang="fr"` or `srclang="en"`.


19. Nice subtitles

  Extract from a .vtt file:

  <pre class="prettyprint  linenums:1">00:00:41.000 --&gt; 00:00:45.000
  This course is about &lt;b&gt;&lt;i&gt;&lt;u&gt;HTML5!&lt;/u&gt;&lt;/i&gt;&lt;/b&gt;.</pre>

  Is the above code correct? (Yes/No)

  Ans: Yes<br/>
  Explanation: This is an extract from a .vtt file. We see here a CUE with a text value that contains some HTML markers. This is indeed correct: HTML is allowed in subtitles/captions.


20. Karaoke duo?

  How can we distinguish different voices, to be displayed in different colors, in subtitles/captions (for example, a karaoke duo)?<br/>

  a. Use `<v nameOfVoice>` followed by the text of the subtitle, like in: `<v Michel>` Hello dear students of this W3Cx course!<br/>
  b. Use `<voice nameOfVoice>` followed by the text of the subtitle, like in `<voice Michel>` Hello dear students of this W3Cx course!<br/>

  Ans: a<br/>
  Explanation: Using the `<v>` tag, you can distinguish different voices that should be displayed in different colors (depending on the HTML5 video player implementation).


21. Chapters

  Which of these statements are true about chapters: (3 correct answers)

  a. Chapters are defined with `<track kind="chapters" .../>`<br/>
  b. Some enhanced players support chapters<br/>
  c. Chapters are supported by all major browsers natively, without the need to use an enhanced player such as the ones presented in the course<br/>
  d. Chapters use a particular syntax and are declared in files with the .chapters suffix<br/>
  e. Chapters are defined in .vtt files<br/>

  Ans: <span style="color: magenta;">abe, xace<br/>
  Explanation: 
    + Chapters are defined in track elements with a `kind="chapters"` attribute. Each chapter is a CUE with starting and ending times, and a text for its description. Optionally, each chapter can have an ID.
    + As of 2015, no native implementation of the video element supports chapters. You will need to use one of the enhanced players presented in the course.


### 2.5.7 The getUserMedia API (22-25)

__Source code for the next 3 questions (22, 23 and 24):__

<div><ol>
<li value="1">&lt;video id="myVideo"<strong> </strong><strong>AAA</strong>&gt;Fallback msg here.&lt;/video&gt;</li>
<li>&lt;script&gt;</li>
<li> function onSuccess(stream) {</li>
<li>&nbsp; &nbsp;var output = document.getElementById('myVideo');</li>
<li>&nbsp; &nbsp;output.srcObject&nbsp;=&nbsp;<strong>CCC;</strong></li>
<li> }</li>
<li> function onError() {</li>
<li>&nbsp; &nbsp;&nbsp;// getUserMedia API not supported, or another application is using the webcam!</li>
<li> }</li>
<li> </li>
<li> if (navigator.getUserMedia) {</li>
<li>&nbsp; &nbsp; navigator.getUserMedia(<strong>BBB</strong>, onSuccess, onError);</li>
<li> }</li>
<li>&lt;/script&gt;</li>
</ol></div>

22. Display video stream from webcam?

  Instead of __AAA__ in the source code above, which attribute is used to start displaying the webcam stream as soon as it is available?<br/>

  a. loop<br/>
  b. autoplay<br/>
  c. preload="none"<br/>

  Ans: b<br/>
  Explanation: The `autoplay` attribute is the one that should be used. It will play the video stream as soon as data become available.


23. Video no audio

  How do you indicate that you want to capture the webcam stream (only the video, not the audio)? What would you use instead of the __BBB__ string in the source code above?<br/>

  a. {video=true}<br/>
  b. {video:true, audio:false}<br/>
  c. {video}<br/>

  Ans: b<br/>
  Explanation: The second answer is correct: we pass as first parameter a JavaScript object with a set of properties/values. The second answer will enable video capture, without audio.


24. Stream to URL

  What would you use instead of the __CCC__ string in the above code?<br/>

  a. createObjectURL as in: `output.srcObject = window.URL.createObjectURL(stream);`<br/>
  b. Nothing, the stream is a UR, just use `output.srcObject = stream;`<br/>
  c. toURL as in: `output.srcObject = window.URL.toURL(stream);`<br/>

  Ans: b<br/>
  Explanation: The second answer is correct. The `srcObject` property of the video object takes the stream directly.


25. What is that?

  <pre class="prettyprint  linenums:1">    navigator.getUserMedia = ( navigator.getUserMedia ||
                          navigator.webkitGetUserMedia ||
                          navigator.mozGetUserMedia ||
                          navigator.msGetUserMedia);</pre>

  What does the above code do?<br/>

  a. Does nothing as navigator.getUserMedia is supported by all major browsers<br/>
  b. Test if getUserMedia works in your browser, with the standard syntax or with a vendor prefixed syntax, and set navigator.getUserMedia with the version that works<br/>
  c. Test if getUserMedia works in your current browser and if not choose a polyfill<br/>

  Ans: b<br/>
  Explanation: Since 2012, the getUserMedia API has been supported by Google Chrome, Firefox and Opera, both on desktops and mobile devices, but you still need to use the prefixed version of the API (i.e. call webkitGetUserMedia or mozGetUserMedia instead of getuserMedia). These 4 lines of code will enable you to write your code without worrying about prefixes.



