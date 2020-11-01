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

  Ans: <br/>
  Explanation: 


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

  Ans: <br/>
  Explanation: 


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

  Ans: <br/>
  Explanation: 


8. Value or result?

  At line 10, what should you put instead of the red bold "?" in order to get the file content?

  a. e.target.result;<br/>
  b. e.target.value;<br/>

  Ans: <br/>
  Explanation: 


9. data URL?

  <pre>data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyb
  lAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==
  </pre>

  A data URL is?

  a. A URL that contains the resource data within the URL string itself, as a base64-encoded string.<br/>
  b. A URL for exchanging data in binary format. It is more compressed, which is useful for compressing text data, for example.<br/>
  
  Ans: <br/>
  Explanation: 





