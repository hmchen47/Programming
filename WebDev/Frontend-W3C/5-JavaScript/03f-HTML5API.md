# Module 3: Playing with HTML5 APIs


## 3.6 Exercises - Module 3


### 3.6.1 Exercises (1-5)

__Source code for the next 3 questions (1, 2 and 3)__

<div><ol>
<li style="margin-bottom: 0px;" value="1">var persons = [</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; {givenName: 'Michel',&nbsp;familyName: 'Buffa', age:51},</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; {givenName: 'Pig',&nbsp;familyName: 'Bodine', age:20},</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; {givenName: 'Pirate',&nbsp;familyName: 'Prentice', age:32}</li>
<li style="margin-bottom: 0px;">];</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">function compareByAge(a,b) { // comparison function</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; if (a.age &lt; b.age) // compare by age</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; return -1;</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; if (a.age &gt; b.age)</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; return 1;</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; return 0;</li>
<li style="margin-bottom: 0px;">}</li>
<li style="margin-bottom: 0px;"><span color="#666600" style="color: #666600;">console.log(<strong>XXX</strong>);</span></li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">persons.sort(compareByAge);</li>
</ol></div>

1. Call me back please!

  At _line 16_, we pass the compareByAge function as an argument to the `sort()` method of the array. How do we call such a function, passed as an argument to another function?

  a. A 'called back'<br>
  b. A 'callback'<br>
  c. Nothing special, it's just 'a function'<br>

  Ans: b<br>
  Example: The `sort()` method of arrays accepts 'a callback' as an optional argument.


2. Print Pirate Prentice's age!

  How would you access the age of Pirate Prentice, at _line 14_ (what would you write instead of __XXX__)?

  a. `persons[1].age;`<br>
  b. `persons[2].age;`<br>
  c. `persons.Pirate.Prentice.age;`<br>

  Ans: b<br>
  Example: Index starts at 0. Pirate Prentice is at index 2. Then, as the array contains objects, we use the . operator to access the age property.


3. Add a new pirate!

  How would you add a new Pirate to the persons array? (2 correct answers.)

  a. `persons.push({givenName:'Captain', familyName:'Hook', age:43});`<br>
  b. `persons.add({givenName:'Captain', familyName:'Hook', age:43});`<br>
  c. `persons[persons.length] = {givenName:'Captain', familyName:'Hook', age:43};`<br>
  d. `persons[persons.length-1] = {givenName:'Captain', familyName:'Hook', age:43};`<br>

  Ans: ac<br>
  Example: You can use the `push` method, or you can add an element at the first index after the last element of the array. The last element of an array persons is at position persons.length-1, so a new element inserted at the end of an array persons will be inserted at index equal to `persons.length`.


4. Strings and arrays

  ```js
  var s = "Michel";
  var a = ['B', 'u', 'f', 'f', 'a'];
  ```

  Check the common things arrays and strings share. (2 correct answers.)

  a. The `length` property<br/>
  b. The `push` and `pop` methods<br/>
  c. elements/characters can be accessed using the bracket notation and indexes, like in `s[3];`<br/>

  Ans: ac<br>
  Example: Indeed, the string s behaves like an array, it has the `length` property like an array, and we can access individual characters using indexes that go from 0 to length-1, like arrays... But you cannot use the push/pop methods for adding/removing characters to s, like in arrays.


5. Classic forEach

  ```js
  var persons = [
    {name:'Michel', age:51},
    {name:'Henri', age:20},
    {name:'Francois', age:29}
  ];

  persons.forEach(function(a, b, c) {
      var currentElem = XXX;
  });
  ```

  What would you write instead of __XXX__ in the code above, in order to get the current element of the array, while iterating on the elements of the array?

  Ans: a<br>
  Example: 
    + The `forEach` method takes a single argument that is a function/callback that can have one, two or three parameters:
      + The first parameter is the current element of the array.
      + The second parameter (optional) is the index of the current element in the array.
      + The third element is the array itself.
    + So, the right answer is "a".


### 3.6.2 Exercises (6-10)

6. JavaScript API?

  What do we mean by "audio and video elements have a JavaScript API"?

  a. They have properties, events and methods that can be manipulated from JavaScript<br>
  b. They are written 100% in JavaScript<br>

  Ans: a<br>
  Explanation: Indeed, it means that, from JavaScript, we are able to call the `play()`, `stop()`, `pause()` methods, access the current time through the `currentTime` property or listen to progress events (for example when synchronizing things when a video is played).


__Source code for the next 3 questions (7, 8 and 9):__

<div><ol>
<li style="margin-bottom: 0px;" value="1">&lt;video id="vid"&nbsp;poster="preview.png"&nbsp;controls&gt; </li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;&lt;source src="http://html5doctor.com/demos/video-canvas-magic/video.mp4"</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; type="video/mp4"&gt;</li>
<li style="margin-bottom: 0px;">&lt;/video&gt; </li>
<li style="margin-bottom: 0px;">&lt;p&gt;Example of custom controls :&lt;/p&gt;</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&lt;button class="mybutton" onclick="go();"&gt;<span style="line-height: 1.6;">Play</span><span style="line-height: 1.6;">&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;">&lt;button class="mybutton" onclick="haveARest();"&gt;<span style="line-height: 1.6;">Pause</span><span style="line-height: 1.6;">&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;">&lt;button class="mybutton" onclick="rewind();"&gt;<span style="line-height: 1.6;">Start from beginning</span><span style="line-height: 1.6;">&lt;/button&gt;</span></li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&lt;script&gt;</li>
<li style="margin-bottom: 0px;">&nbsp; vid = document.querySelector("#vid");</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">&nbsp;&nbsp;function go() {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; vid.<strong>BBB</strong>();</li>
<li style="margin-bottom: 0px;">&nbsp;&nbsp;}</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">&nbsp; function haveARest() {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; vid.<strong>CCC</strong>();</li>
<li style="margin-bottom: 0px;">&nbsp;&nbsp;}</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">&nbsp;&nbsp;function rewind() {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; vid.<strong>DDD</strong>&nbsp;= 0;</li>
<li style="margin-bottom: 0px;">&nbsp;&nbsp;}</li>
<li style="margin-bottom: 0px;">&lt;/script&gt;</li>
</ol></div>

7. Which method?

  Which method would you call to start playing the video, instead of __BBB__?

  a. `go()`<br>
  b. `play()`<br>
  c. `start()`<br>

  Ans: b<br>
  Explanation: There is no `start()` nor `go()` method in the JavaScript API of the video element. The right answer is `play()`.


8. Which method? (Part 2)

  Which method would you call to pause the video, instead of CCC?

  a. `stop()`<br>
  b. `pause()`<br>
  c. `cancel()`<br>

  Ans: b<br>
  Explanation: There is no `cancel()` in the JavaScript API of the video element. The `stop()` method exists but it is for stopping the video (and once stopped, it cannot be resumed). The right answer is the `pause()` method.


9. Be kind, rewind!

  Which property would you use to rewind completely the video without stopping it (playback continues as if we jumped to the beginning), instead of the DDD string in the source code above?

  a. `progress`<br>
  b. `location`<br>
  c. `currentTime`<br>
  d. `time`<br>

  Ans: c<br>
  Explanation: The `currentTime` property is in read/write. Its value changes during playback, but if we give it a value, then the video "jumps" to the position that corresponds to its value (in seconds).


10. Event for playlists?

  Which event is used in the course to detect the end of video and implement playlist management?
  a. `end`<br>
  b. `chained`<br>
  c. `ended`<br>
  d. `finished`<br>
  e. `finish`<br>

  Ans: c<br>
  Explanation: The course examples use the `ended` event to detect the end of a video playback. See the code from the example 1 in section 2.2.7 for instance: http://jsbin.com/temupe/1/edit.


### 3.6.3 Exercises (11-12)

11. How do you geolocate me?

  How does the HTML5 geolocation API locate the client's browser?

  a. Different methods, including: GPS, GSM/3G triangulation, WIFI, and IP address; are tried to get the current location.<br>
  b. Using GPS only. If no GPS, it's impossible to geolocate. That's why smartphones often ask the user to turn on the GPS.<br>

  Ans: a<br>
  Explanation: The geolocation HTML5 JavaScript API is implemented by most modern web browsers, and uses different means to get the current location: GPS, GSM/3G triangulation, WIFI, IP address, etc. Sometimes it is not possible to get a location (behind an organization's firewall, for instance).


12. She's the one!

  ```js
  navigator.geolocation.getCurrentPosition(showPosition, onError);

  function showPosition(position) {
      console.log("latitude is: " + position.coords.latitude);
      console.log("longitude is: " + position.coords.longitude);
  }
  
  function onError(err) {
      console.log("Could not get the position");
  }
  ```

  With the above code, if a position is available, how many times will the showPosition callback be called?

  a. Once.<br>
  b. Several times: if we move and the position changes, the showPosition method will be called again.<br>

  Ans: <span style="color: brown;">a</span>, xb<br>
  Explanation: When a position is available, the showPosition will be called once.



