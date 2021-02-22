# Module 3: Playing with HTML5 APIs


## 3.6 Exercises - Module 3


### 3.6.1 Exercises (1-5)

__Source code for the next 3 questions (1, 2 and 3)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> persons </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; {</span><span class="pln">givenName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">,</span><span class="pln">&nbsp;familyName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Buffa'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">51</span><span class="pun">},</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; {</span><span class="pln">givenName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Pig'</span><span class="pun">,</span><span class="pln">&nbsp;familyName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Bodine'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">20</span><span class="pun">},</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; {</span><span class="pln">givenName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Pirate'</span><span class="pun">,</span><span class="pln">&nbsp;familyName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Prentice'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">32</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> compareByAge</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span><span class="com">// comparison function</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">a</span><span class="pun">.</span><span class="pln">age </span><span class="pun">&lt;</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">age</span><span class="pun">)</span><span class="pln"> </span><span class="com">// compare by age</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">a</span><span class="pun">.</span><span class="pln">age </span><span class="pun">&gt;</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">age</span><span class="pun">)</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; return</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span color="#666600" style="color: #666600;">console.log(<strong>XXX</strong>);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">persons</span><span class="pun">.</span><span class="pln">sort</span><span class="pun">(</span><span class="pln">compareByAge</span><span class="pun">);</span></li>
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

  Ans: <br>
  Explanation: 


__Source code for the next 3 questions (7, 8 and 9):__

```html
<video id="vid" poster="preview.png" controls>
    <source src="http://html5doctor.com/demos/video-canvas-magic/video.mp4"
            type="video/mp4">
</video>
<p>Example of custom controls :</p>
 
<button class="mybutton" onclick="go();">Play</button>
<button class="mybutton" onclick="haveARest();">Pause</button>
<button class="mybutton" onclick="rewind();">Start from beginning</button>
 
<script>
  vid = document.querySelector("#vid");
  function go() {
    vid.BBB();
  }
  function haveARest() {
    vid.CCC();
  }
  function rewind() {
    vid.DDD = 0;
  }
</script>
```

7. Which method?

  Which method would you call to start playing the video, instead of BBB?

  a. `go()`<br>
  b. `play()`<br>
  c. `start()`<br>

  Ans: <br>
  Explanation: 


8. Which method? (Part 2)

  Which method would you call to pause the video, instead of CCC?

  a. `stop()`<br>
  b. `pause()`<br>
  c. `cancel()`<br>

  Ans: <br>
  Explanation: 


9. Be kind, rewind!

  Which property would you use to rewind completely the video without stopping it (playback continues as if we jumped to the beginning), instead of the DDD string in the source code above?

  a. `progress`<br>
  b. `location`<br>
  c. `currentTime`<br>
  d. `time`<br>

  Ans: <br>
  Explanation: 


10. Event for playlists?

  Which event is used in the course to detect the end of video and implement playlist management?
  a. `end`<br>
  b. `chained`<br>
  c. `ended`<br>
  d. `finished`<br>
  e. `finish`<br>

  Ans: <br>
  Explanation: 




