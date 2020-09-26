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





