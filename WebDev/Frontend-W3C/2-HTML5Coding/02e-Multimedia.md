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




