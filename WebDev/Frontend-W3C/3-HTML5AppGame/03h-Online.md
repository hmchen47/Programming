# Module 3: HTML5 file upload and download section


## 3.8 Exercises - Module 3 (26 Questions)


### 3.8.1 Ajax and XHR2 (1-6)

1. Is XHR2 twice as good?

  XHR2 improved upon the "old way" of using Ajax. Which of the following improvements came with XHR2? (3 correct answers._

  a. Data transfer is faster than before<br>
  b. The syntax has been simplified<br>
  c. Encoding / decoding of binary files is done directly within the browser<br>
  d. Progress monitoring for uploads and downloads is now possible without polling the server<br>
  e. Native support for multimedia files<br>
  
  Ans: bcd<br>
  Explanation: XHR2 improvements include: New, easier to use syntax, Encoding / decoding of binary files performed directly by the browser, Progress monitoring for uploads and downloads is possible without querying the server.


<hr>

__Source code for the next question (2)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Load a binary file from a URL as an ArrayBuffer.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> loadSoundFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">responseType </span><span class="pun">=</span><span class="pln"> </span><span class="str">'arraybuffer'</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">onload </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;initSound</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">response</span><span class="pun">);</span><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">};</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

2. Array of buffers? ArrayBuffer? A ray buffed air?

  What is line 6 useful for?

  a. It indicates that we want the browser to decode into some binary format, the text-encoded data received from the server.<br>
  b. arrayBuffer is the name of the variable where the requested data will be stored.<br>
  
  Ans: a<br>
  Explanation: With XHR2, you can ask the browser to decode the file you send/receive natively. To do this, when you use an `XMLHttpRequest` to send or receive a file, you need to specify the type of file with a value equal to `arrayBuffer`.



<hr>

__Source code for the next 3 questions (3, 4 and 5)__

HTML:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;progress</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"downloadProgress"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">0</span><span class="tag">&gt;&lt;progress&gt;</span></li>
</ol></div>

JavaScript:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">....</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// progress element</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> progress </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">'#downloadProgress'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> downloadSoundFile</span><span class="pun">(</span><span class="pln">url</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="kwd">var</span><span class="pln"> xhr </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">XMLHttpRequest</span><span class="pun">();</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">open</span><span class="pun">(</span><span class="str">'GET'</span><span class="pun">,</span><span class="pln"> url</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="com">// Monitor progress by updating the progress element</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.<span style="color: #ff0000;"><strong>AAA</strong></span></span><span class="pln">&nbsp;</span><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">e</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; progress</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.<span style="color: #ff0000;"><strong>BBB</strong></span></span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; progress</span><span class="pun">.</span><span class="pln">max </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.<span style="color: #ff0000;"><strong>CCC</strong></span></span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; xhr</span><span class="pun">.</span><span class="pln">send</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

3. Fill in the blank (1/3)

  What would you write instead of the AAA placeholder in the above code? Use lowercase letters please.

  Ans: `onprogress`<br>
  Explanation: `xhr.onprogress` is the correct answer. For an upload it would have been `xhr.upload.onprogress`


4. Fill in the blank (2/3)

  What would you write instead of the BBB placeholder in the above code? Use lowercase letters please.

  Ans: `loaded`<br>
  Explanation: The `loaded` property of the progress event is the correct answer.


5. Fill in the blank (3/3)

  What would you write instead of the CCC placeholder in the above code? Use lowercase letters please.

  Ans: `total`<br>
  Explanation: The `total` property of the progress event is the correct answer.


6. Give me a bag to put all these parts together!

  What object, introduced during the course, is used when sending a multipart form?

  a. The `serializeArray(form)` function<br>
  b. The `FormData` object type<br>
  c. The `arrayBuffer` type<br>

  Ans: b<br>
  Explanation: A `FormData` object is a container for parts in the multipart data that will be sent by an XHR2 POST request. If we create the `FormData` like this: `var data = new FormData(form);` where `form` is the HTML form, then `data` will contain all the input fields' values. We can add files to this object using the `data.append(name, value)` method.








