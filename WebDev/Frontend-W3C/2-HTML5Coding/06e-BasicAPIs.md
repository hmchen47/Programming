# Week 6: HTML5 Basic APIs


## 6.5 Final exam


### 6.5.1 Intro final exam

The final exam consists of 28 questions (multiple choice, checkboxes, etc.) covering the entirety of the course.

As stated in the grading policy page, this final exam counts towards 25% of the final grade.


### 6.5.2 Exercises (1-4)

1. localStorage vs sessionStorage

  What is the difference between localStorage and sessionStorage?

  a. With localStorage, the data will remain until deleted. With sessionStorage, the data is erased when the tab/browser is closed.<br/>
  b. Session storage uses cookies and HTTP sessions similar to PHP or Java Servlets. Data is stored on the memory of a remote server, and only the session ID is stored locally.<br/>

  Ans: a<br/>
  Explanation: Web storage provides two interfaces called sessionStorage and localStorage, whose main difference is data longevity. This specification defines an API for persistent data storage of key-value pair data in Web clients.


2. Help the Beatles!

  Check the correct syntaxes for writing data in localStorage: (3 correct answers.)

  a. `localStorage.name = "John Lennon";`<br/>
  b. `localStorage.setItem("Paul McCartney");`<br/>
  c. `localStorage['name'] = "George Harrison";`<br/>
  d. `localStorage.setItem("Full Name","Ringo Starr");`<br/>

  Ans: acd<br/>
  Explanation: The first answer is correct. The third answer is correct as localStorage.name is equivalent in JavaScript to the proposed syntax with brackets. The fourth answer is correct as the setItem method takes the key as the first parameter, and the value as the second parameter. The key can contain spaces. This is why setItem is useful: for storing data whose key contains spaces. Correct answers are 1, 3 and 4.


3. localStorage for all or just for me?

  Important note: the domain buffa.org does not actually exist in real life, but for the sake of this exercise, we'll pretend that it does.

  <pre>for (var i = 0, n = localStorage.length; i &lt; n; i++) {
      var k = localStorage.key(i);
      console.log(k + ": " + localStorage[k]); 
  }
  </pre>

  I visit `http://buffa.org/index.html`. The page contains the above code: what does it do?

  a. It prints in the dev. tools console all the keys and values for all visited Web sites that used localStorage for storing data.<br/>
  b. It prints in the dev. tools console all the keys and values for the domain buffa.org (following the "same origin policy").<br/>
  c. It prints in the dev. tools console all the keys and values for the page http://buffa.org/index.html<br/>

  Ans: <span style="color: magenta;">b</span>, xa<br/>
  Explanation: The data written in local storage is "per domain", following the same origin policy.


4. Store arrays or objects?

  How can we store JavaScript arrays and objects in localStorage or sessionStorage?

  a. We can use the JSON format, together with the JSON.stringify and JSON.parse methods.<br/>
  b. We can't.<br/>

  Ans: a<br/>
  Explanation: JSON provides a great way of encoding and decoding data that is a really good match for JavaScript. We saw this in the course examples that store JavaScript objects as JSON.


### 6.5.3 Exercises (5-9)

5. Local or remote?

  The File API has been designed to work with?

  a. Local files (located on the client-side)<br/>
  b. Remote files (located on a distant server)<br/>

  Ans: a<br/>
  Explanation: The File API is for working with local files.


6. Which metadata?

  <pre>&lt;input type="file" id="input"/&gt;

  ...
  var selectedFile = document.getElementById('input').files[0];
  </pre>

  Suppose that we have selected at least one file with the above input field, and that selectedFile is its file descriptor.

  What properties are provided by the File API on file descriptors, for consulting metadata? (4 correct answers.)

  a. width<br/>
  b. size<br/>
  c. type<br/>
  d. name<br/>
  e. date<br/>
  f. lastModifiedDate<br/>

  Ans: bcdf<br/>
  Explanation: The different file metadata properties are `size`, `type`, `name`, and `lastModifiedDate`.


__Source code for the next 2 questions (7 and 8)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"files"</span><span class="tag">&gt;</span><span class="pln">Choose a text file:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"file"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"files"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">onchange</span><span class="pun">=</span><span class="atv">"</span><span class="pln">readFileContent</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">files</span><span class="pun">)</span><span class="atv">"</span><span class="tag">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;textarea</span><span class="pln"> </span><span class="atn">rows</span><span class="pun">=</span><span class="atv">15</span><span class="pln"> </span><span class="atn">cols</span><span class="pun">=</span><span class="atv">50</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"fileContent"</span><span class="tag">&gt;&lt;/textarea&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> readFileContent</span><span class="pun">(</span><span class="pln">files</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> reader </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">FileReader</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>reader</strong></span><strong><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">"fileContent"</span><span class="pun">).</span><span class="pln">value</span><span class="pun">=</span><span class="pln"> </span><span class="pun"><strong><span style="color: #ff0000;">?</span></strong>;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>reader</strong></span><strong><span class="pun">.</span><span class="pln">readAsText</span><span class="pun">(</span><span class="pln">files</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]);</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/script&gt;</span></li>
</ol></div>

7. Execution order...

  The above code works.

  When a file is selected by a user, the function readFileContent is called.

  Is line 12 executed before line 10? (Yes/No)

  Ans: yes<br/>
  Explanation: Yes, when we call reader.readAsText(...);, the file starts being read. Then, once entirely read, the reader.onload callback is called. The correct answer is "Yes".


8. Value or result?

  At line 10, what should you put instead of the red bold "?" in order to get the file content?

  a. `e.target.result;`<br/>
  b. `e.target.value;`<br/>

  Ans: a<br/>
  Explanation: The content of the file that has been read is located in the `e.target.result` property.


9. data URL?

  <pre>data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyb
  lAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==
  </pre>

  A data URL is?

  a. A URL that contains the resource data within the URL string itself, as a base64-encoded string.<br/>
  b. A URL for exchanging data in binary format. It is more compressed, which is useful for compressing text data, for example.<br/>
  
  Ans: a<br/>
  Explanation: Data URLs are a Uniform Resource Identifier scheme that allows you to include data items inline in a Web page as if they were being referenced as external resources. Data URLs are a form of Uniform Resource Locator, although they do not in fact remotely locate anything. Instead, the resource data is contained within the URL string itself as a base64-encoded string.


### 6.5.4 Exercises (10-15)

10. How do you geolocate me?

  How does the HTML5 geolocation API locate the client's browser?

  a. Different methods, including: GPS, GSM/3G triangulation, WIFI, and IP address; are tried to get the current location.<br/>
  b. Using GPS only. If no GPS, it's impossible to geolocate. That's why smartphones often ask the user to turn on the GPS.<br/>

  Ans: a<br/>
  Explanation: The geolocation HTML5 JavaScript API is implemented by most modern Web browsers, and uses different means to get the current location: GPS, GSM/3G triangulation, WIFI, IP address, etc. Sometimes it is not possible to get a location (behind an organization's firewall, for instance).


11. She's the one!

  <pre>navigator.geolocation.getCurrentPosition(showPosition, onError);
  
  function showPosition(position) {
      console.log("latitude is: " + position.coords.latitude);
      console.log("longitude is: " + position.coords.longitude);
  }
  
  function onError(err) {
      console.log("Could not get the position");
  }
  </pre>

  With the above code, if a position is available, how many times will the showPosition callback be called?

  a. Once.<br/>
  b. Several times: if we move and the position changes, the showPosition method will be called again.<br/>

  Ans: a<br/>
  Explanation: When a position is available, the showPosition will be called once.


12. Asking permission

  Can the JavaScript of a Web page turn geolocation on without asking the user at least once?

  a. No, a Web site user that uses geolocation must agree to be geolocated, at least once.<br/>
  b. Yes, we can geolocate without asking permission.<br/>

  Ans: a<br/>
  Explanation: The first time you open a Web page that uses geolocation, the browser will ask if you agree to share your position with the application, for privacy reasons.


13. Be accurate, please!

  Is it possible to know the accuracy of a given position? (Yes/No)

  Ans: Yes<br/>
  Explanation: It's possible to know the accuracy for the longitude/latitude positioning using the `position.coords.accuracy` property. It's also possible to know the accuracy of the altitude computation, when available, using the `position.coords.altitudeAccuracy` property.


14. Watch my position

  `var watchPosId = navigator.geolocation.watchPosition(showPosition);`

  With the above code, how often will the showPosition callback function be called?

  a. It will be called only when a new position is available.<br/>
  a. It will be called at regular intervals of time that depend on the browser's implementation; at least twice per minute.<br/>

  Ans: a<br/>
  Explanation: Whereas getCurrentPosition just gives a position once when called, watchPosition does the following:
    + it only calls the callback function when the current position changes. If you stay in the same place, it won't regularly call the callback function - it only does this when you move.
    + It returns an id so that you can use the clearWatch(id) method to stop the current tracking.




15. Get current position

  `navigator.geolocation.getCurrentPosition(showPosition, onError,{enableHighAccuracy:true});`

  What is the meaning of the third parameter?

  a. It will try to use the GPS if available. This may prompt the user to turn on the GPS of his mobile device, if the GPS is turned off.<br/>
  b. This just activates a high resolution computation of the coordinates (using 64 bit accuracy), independently of the means used to geolocate.<br/>

  Ans: a<br/>
  Explanation: Several options are available when using HTML5 geolocation. We can pass a third parameter to the getCurrentPosition and watchPosition methods, that will hold one or several options. enableHighAccuracy:true will indeed try to use GPS, if available.


### 6.5.5 Exercises (16-22)

__Source code for the next 3 questions (16, 17 and 18)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Canvas example</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;canvas</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"myCanvas"</span><span class="pln"> </span><span class="atn">width</span><span class="pun">=</span><span class="atv">"400"</span><span class="pln"> </span><span class="atn">height</span><span class="pun">=</span><span class="atv">"400"</span><span class="tag">&gt;&lt;/canvas&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> canvas </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#myCanvas"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> ctx </span><span class="pun">=</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">getContext</span><span class="pun">(</span><span class="str">'2d'</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;drawSomething</span><span class="pun">(</span><span class="lit">120</span><span class="pun">,</span><span class="pln"> </span><span class="lit">120</span><span class="pun">,</span><span class="pln"> </span><span class="lit">50</span><span class="pun">,</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;ctx</span><span class="pun">.</span><span class="pln">clearRect</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">width</span><span class="pun">,</span><span class="pln"> canvas</span><span class="pun">.</span><span class="pln">height</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;drawSomething</span><span class="pun">(</span><span class="lit">120</span><span class="pun">,</span><span class="pln"> </span><span class="lit">120</span><span class="pun">,</span><span class="pln"> </span><span class="lit">20</span><span class="pun">,</span><span class="pln"> </span><span class="str">'blue'</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="kwd">function</span><span class="pln"> drawSomething</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> r</span><span class="pun">,</span><span class="pln"> color</span><span class="pun">)</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">strokeStyle </span><span class="pun">=</span><span class="pln"> color</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">arc</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">,</span><span class="pln"> r</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;ctx</span><span class="pun">.</span><span class="pln">stroke</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

16. The tale of the two circles

  <div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
    <a href="https://tinyurl.com/y58zmzhg" ismap target="_blank">
      <img style="margin: 0.1em;" height=100
        src  ="https://tinyurl.com/y6375ecp"
        alt  ="2 blue circles, one big, one small linked together"
        title="2 blue circles, one big, one small linked together"
      >
      <img style="margin: 0.1em;" height=100
        src  ="https://tinyurl.com/y6375ecp"
        alt  ="2 circles: one red big and one blue small, disconnected"
        title="2 circles: one red big and one blue small, disconnected"
      >
      <img style="margin: 0.1em;" height=100
        src  ="https://tinyurl.com/y4aopujo"
        alt  ="2 blue circles, one big, one small, disconnected"
        title="2 blue circles, one big, one small, disconnected"
      >
    </a>
  </div>

  Which picture will be drawn by the above code?

  a. Image 1 (two blue circles with a blue line that goes from one to the other)<br/>
  b. Image 2 (a red circle and a blue circle)<br/>
  c. Image 3 (two blue circles, disconnected)<br/>

  Ans: a<br/>
  Explanation: The first answer is correct: the two circles are in the same path. The second call to drawSomething at line 18 will draw all arcs in the buffer (the one that has been added during the first call and the current one). As we never emptied the buffer, two circles will be drawn, in addition, as they are in the same path, they will be connected.


17. Which best practice?

  The function `drawSomething()` does not follow the best practice presented in the course. Which of the following describes the best practice?

  a. It is absolutely necessary to call ctx.beginPath() before calling ctx.arc(...)<br/>
  b. A function that changes the context must save the context at the beginning and restore it at the end.<br/>
  c. A function must not change the current color, as this may affect other parts of the code.<br/>

  Ans: b<br/>
  Explanation: Best practice is to save/restore the context at the beginning/end of each function that changes the context or apply transformations to the coordinate system.


18. Improve but make no new mistakes...

  drawSomething version 1

  <pre>    function drawSomething(x, y, r, color) {
        ctx.save();
        ctx.translate(x, y);
        ctx.strokeStyle = color;
        ctx.arc(0, 0, r, 0, 2*Math.PI);
        ctx.stroke();
      }
  </pre>

  drawSomething version 2

  <pre>    function drawSomething(x, y, r, color) {
        ctx.save();
        ctx.translate(x, y);
        ctx.strokeStyle = color;
        ctx.arc(x, y, r, 0, 2*Math.PI);
        ctx.stroke();
        ctx.restore();
      }
  </pre>

  drawSomething version 3

  <pre>    function drawSomething(x, y, r, color) {
        ctx.save();
        ctx.translate(x, y);
        ctx.strokeStyle = color;
        ctx.arc(0, 0, r, 0, 2*Math.PI);
        ctx.stroke();
        ctx.restore();
      }
  </pre>

  We tried to improve the drawSomething function, __without changing the meaning of its parameters. Call it with the same parameters and the new version should do the same thing as the original!__

  For example, if we replace the original version with the new version in the colored source code at the beginning of this page, the resulting drawing should be exactly the same, at the same location.

  Which of the above versions is the good one?

  a. Version 1<br/>
  b. Version 2<br/>
  c. Version 3<br/>

  Ans: c<br/>
  Explanation: Version 2 is incorrect: we translate(x, y) and keep drawing the arc at (x, y). This will move the center of the circle twice. Version 1 is incorrect, as we save the context at the beginning and never restore it. Consecutive calls of this function will accumulate the translation values. Version 3 is correct: we save and restore the context, and use translate(x, y) and draw the arc at (0, 0).


19. Microdata?

  What is the primary use of microdata?

  a. Defining new JavaScript variables that correspond to HTML elements in the page<br/>
  b. SEO (Search Engine Optimization)<br/>
  c. Better structuring of an HTML page<br/>

  Ans: b<br/>
  Explanation: The main use for Microdata is SEO (Search Engine Optimization).


20. I have a headache, doctor!

  <pre>&lt;section&gt;
    &lt;header&gt;
        &lt;p class="article title"&gt;Blog post of April 2020&lt;/p&gt;
        &lt;p&gt;Posted by Michel Buffa...&lt;/p&gt;
    &lt;/header&gt;
    ...
  &lt;/section&gt;
  </pre>

  While the above code has no errors, it does not follow best practice for accessibility. Which best practice is this?

  a. P elements should never be used inside a header element, only a H1, H2... H6.<br/>
  b. The code should use a heading (a H1, H2... H6) within each section element.<br/>
  c. A header should always be used at the beginning of the page, not inside a section element.<br/>

  Ans: b<br/>
  Explanation: Best practice: always add a heading to explicit sectioning content. This is from week 1 of the course!


21. Headers, headings, my poor head!

  <pre class="prettyprint  linenums:1">&lt;section&gt;
    &lt;header&gt;    
      &lt;h1&gt;Blog posts for April 2020&lt;/h1&gt;    
    &lt;/header&gt;
    &lt;article&gt;
      &lt;header&gt;
        &lt;h1&gt;&lt;a href=""&gt;Information about this example&lt;/a&gt;&lt;/h1&gt;
        This example is a modified version of 
        &lt;a href="http://netstream.ru/htmlsamples/html5-blog/index.html"&gt;
        http://netstream.ru/htmlsamples/html5-blog/index.html&lt;/a&gt;
      &lt;/header&gt;
    ...
  &lt;/article&gt;
  &lt;/section&gt;</pre>

  While the above code has no errors, the course offered a recommendation about using sectioning elements and headings in this way. What did the course recommend?

  a. Use H1 as top level headings only, use H2... H6 in sectioning content. The H1 in the article should be replaced by a H2.<br/>
  b. Do not use sections and articles, H1, H2 etc. are sufficient.<br/>
  c. Put sections into articles, not the reverse.<br/>

  Ans: a<br/>
  Explanation: Use H1 as top level headings only, use H2...H6 in sectioning content. Here, we have a H1 in a section; this is ok. But we have also another H1 in the article in the section. While this may be ok, according to the specification, due to the lack of implementation of the outline algorithm that renumbers H1s automatically depending on the hierarchy of sectioning elements, this practice is not recommended. 


22. Light, camera, action!

  What is the name of the API for accessing the Webcam or the microphone?

  a. getUserMedia API<br/>
  b. Multimedia API<br/>
  c. requestAnimationFrame API<br/>

  Ans: a<br/>
  Explanation: The correct answer is getUserMedia API.






