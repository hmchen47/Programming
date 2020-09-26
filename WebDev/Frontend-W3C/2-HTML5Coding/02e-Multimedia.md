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

  Ans: <br/>
  Explanation: 


7. Recommended attributes

  What is considered good practice when you target mobile applications, or when your document contains a lot of audios/videos? (2 correct answers.)<br/>
  a. use the autoplay attribute in audio and video elements<br/>
  b. use the attribute preload="none" in audio and video elements<br/>
  c. use the loop attribute in audio and video elements<br/>
  d. omit the autoplay attribute in audio and video elements<br/>
  
  Ans: <br/>
  Explanation: 


8. HTML5 relaxed syntax and boolean attributes

  We would like to have play/stop/pause buttons in our audio or video player. What should be added to the declaration of the video element? (2 correct answers.)<br/>
  a. If we want just a play/pause button, but no stop button, we will add two attributes: `play="true"` and `stop="false"`<br/>
  b. Just add an attribute named "controls" like in `<audio controls>`<br/>
  c. Same as above, but you can also use `<audio controls="controls">`<br/>
  d. Add this attribute: `showcontrols`<br/>

  Ans: <br/>
  Explanation: 


