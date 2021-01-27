# Module 1: Introduction to JavaScript

## 1.7 Exercises - Module 1


### 1.7.1 Exercises (1-6)

1. Can I go outside?

  Can JavaScript only run in a Web browser? (No/Yes)
  
  Ans: No<br/>
  Explanation: JavaScript can be run outside of the browser (on a nodeJS interpreter on a remote server, for example, or in scripts run by the operating system), but for this intro course, we focus on "JavaScript in the browser" (an advanced course about "server side JavaScript" is on its way at W3Cx).


2. Browser, what language do you speak?

  On modern browsers, JavaScript is the only programming language a browser can run without installing any plugins or extensions. True or false?
  
  Ans: True<br/>
  Explanation: JavaScript is the third of the "magic trio": HTML5/CSS/JavaScript. It is the only programming language a browser can run (without installing any plugins or extensions), and it's a real standard of the Web (even if not standardized by the W3C).


<hr/>

__Source code for the next question (3):__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">JavaScript and HTML</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">/&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> changeTitleCSSStyle</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> title </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#mainTitle"</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> title</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'black'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> title</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">backgroundColor </span><span class="pun">=</span><span class="pln"> </span><span class="str">"yellow"</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> title</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">border </span><span class="pun">=</span><span class="pln"> </span><span class="str">"5px dashed red"</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h1</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mainTitle"</span><span class="tag">&gt;</span><span class="pln">My home page</span><span class="tag">&lt;/h1&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span><span class="pln">This is an example of interactivity between JavaScript and the HTML content of a document.</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">changeTheTitle</span><span class="pun">();</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Click me</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


3. Do you like buttons?

  With the above source code, what will happen when one clicks on the button?

  a. The HTML content of the title whose id is "mainTitle" will change<br>
  b. There is an error in this code, it will do nothing and raise an error in the devtool console<br>
  c. The style of the title whose id is "mainTitle" will change (colors, border)<br>
  
  Ans: b<br/>
  Explanation: This code will do nothing and display an error in the devtool console. A click on a button will try to call a JavaScript function named "changeTheTitle", and there is no such function in the JavaScript code between <script> and </script>. The only defined function is named "changeTitleCSSStyle".


<hr/>

__Source code for the next 3 questions (4, 5 and 6)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> parameters </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; target</span><span class="pun">:</span><span class="pln"> </span><span class="str">'#myFunction'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; data</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; fn</span><span class="pun">:</span><span class="pln"> </span><span class="str">'sin(x)'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; color</span><span class="pun">:</span><span class="pln"> </span><span class="str">'red'</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; }</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; ],</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; grid</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; yAxis</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln">domain</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[-</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">]},</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; xAxis</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln">domain</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">]},</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">functionPlot</span><span class="pun">(</span><span class="pln">parameters</span><span class="pun">);</span></li>
</ol></div>


4. Detect the array

  In the above code, the variable named "parameters" is an object. One of its direct properties is an array. Please enter its name:
  
  Ans: data<br/>
  Explanation: The `data` property is the only direct property that is an array, as it is declared using brackets.


5. Detect the grid

  In the above code, how would you access the grid property of the parameters object?

  a. `parameters.grid`<br/>
  b. `parameters(grid)`<br/>
  c. `parameters/grid`<br/>
  
  Ans: a<br/>
  Explanation: We access properties of an object using the "." operator. The correct answer is `parameters.grid`.


6. Detect the color

  In the above code, how would you access the color located at line 5?

  a. `parameter.data.color`<br/>
  a. `parameters.data[0].color`<br/>
  a. `parameters.color`<br/>
  a. `parameter.data[1].color`<br/>
  a. `parameters/data/color`<br/>
  
  Ans: b</br/>
  Explanation: _data_ is a direct property of parameters. We access the data property using `parameters.data`, then _data_ is an array, and array indexes start at 0. data has only one element (the object {fn: 'sin(x)', color: 'red'}).







