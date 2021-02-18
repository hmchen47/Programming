# Module 3: Playing with HTML5 APIs
 
## 3.2 Arrays (part 2): iterators

### 3.2.1 Arrays

<a href="https://edx-video.net/W3CJSIXX2016-V003200_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/2oemwc87)

<span style="color: brown; font-style: bold;">ERRATA in the above video:</span>

+ In the part that explains the splice method for removing element, I say "splice(0, 1) removed the element that was in the middle". This is a mistake, as it removes the FIRST element, the one that was at index 0. It is not the element that was "in the middle", as I say in the video (the element was in the middle of the array before we sorted it).

__Source code of the example in the video:__

The example shown in the video is available at CodePen

[CodePen Demo](https://codepen.io/w3devcampus/pen/owgeyJ)

[Local Demo](src/ls/03b-example01.js)


#### JavaScript arrays

In JavaScript, arrays represent a collection of "things", which may be strings, integer values, decimal values, boolean values, or any sort of JavaScript object.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> myarr </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'red'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'blue'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'yellow'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'purple'</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> myarr</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="str">"red"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"blue"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"yellow"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"purple"</span><span class="pun">]</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> myarr</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"red"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> myarr</span><span class="pun">[</span><span class="lit">3</span><span class="pun">];</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"purple"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">"purple"</span></li>
</ol></div>


Each element of an array has a key/index and a value. Here are the keys/indexes and values from the above example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/19asezfy')"
    src    ="https://tinyurl.com/1ggh319d"
    alt    ="Table with key and values of the previous array example"
    title  ="Table with key and values of the previous array example"
  />
</figure>

Below is an another example with an array containing three integers. The first element is at index 0, and the last at the index equal to the number of elements-1.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln">&nbsp;</span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln">&nbsp;</span><span class="kwd">typeof</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"object"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln">&nbsp;</span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="lit">2</span><span class="pun">,</span><span class="lit">3</span><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln">&nbsp;a</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln">&nbsp;a</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="lit">1</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln">&nbsp;a</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="lit">2</span></li>
</ol></div>

##### Properties and methods of array objects

JavaScript arrays are objects and have some useful properties and methods

Note that in JavaScript, arrays are "objects" (_lines 2-3_ in the above example), which means that they have properties and methods. You can access/call them using the "." operator. Here are the most common properties and methods.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span></strong><span class="pln"> </span><span class="com">// number of elements</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">5</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">sort</span><span class="pun">();</span></strong><span class="pln"> </span><span class="com">// sorts element in a</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">);</span></strong><span class="pln"> </span><span class="com">// remove 1 element starting from index=2 (3rd element)</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">3</span><span class="pun">]</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span><span class="pln"> </span><span class="com">// the '3' has been removed from the array</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">]</span></li>
</ol></div>

By default, the `sort()` method sorts elements alphabetically if they are strings, or from lowest to highest if they are numeric. If you want to sort objects like `{firstName:'michel', lastName:'Buffa', age:51}`, you will need to use another method passed as an argument to the sort method, for example to indicate the property you want to use for sorting (i.e., sort by age);

Example with an array of persons (each person is an object):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> persons </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; {</span><span class="pln">givenName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">,</span><span class="pln">&nbsp;familyName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Buffa'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">51</span><span class="pun">},</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; {<span style="color: #000000;">given</span></span><span class="pln" style="color: #000000;">Name</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Pig'</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="pun"><span style="color: #000000;">family<span style="background-color: #eeeeee;">Name</span></span>:</span><span class="pln"> </span><span class="str">'Bodine'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">20</span><span class="pun">},</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; {</span><span class="pun"><span style="color: #000000;">given</span><span class="pln" style="background-color: #ffffff;">Name</span>:</span><span class="pln"> </span><span class="str">'Pirate'</span><span class="pun">,</span><span class="pln">&nbsp;</span><span class="pun"><span style="color: #000000;">familyName</span>:</span><span class="pln"> </span><span class="str">'Prentice'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">32</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> compareByAge</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln">b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{ // comparison function, a and b are persons</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">a</span><span class="pun">.</span><span class="pln">age </span><span class="pun">&lt;</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">age</span><span class="pun">) &nbsp; &nbsp; &nbsp; &nbsp; // compare by age</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> </span><span class="pun">-</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">a</span><span class="pun">.</span><span class="pln">age </span><span class="pun">&gt;</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">age</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; return</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">persons</span><span class="pun">.</span><span class="pln">sort</span><span class="pun">(</span><span class="pln">compareByAge</span><span class="pun">); // this will call automatically compareByAge</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // passing all persons from the array, compare</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // them by age and sort the array.</span></strong></li>
</ol></div>

Explanations:

+ _Line 17_ calls `persons.sort(function_that_compares_two_elements)`, passing as an unique parameter a function that compares two people's ages. This function must return -1 if the first person is younger than the second person. It must return +1 if the first person is older than second person, and 0 if they are the same age.

We will see more methods in the other subsections of this page.

##### Types of elements in array

Elements can be of different types in a same array

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="lit">2</span><span class="pun">,</span><span class="lit">3</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">2</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'three'</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"three"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="str">"three"</span><span class="pun">]</span></li>
</ol></div>


##### Adding elements to an array

We can add new elements using a new index, if you want to add a new element at the end, use the `push` method!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="lit">2</span><span class="pun">,"three"</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">3</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'four'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"four"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="str">"three"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"four"</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="pln">a</span><span class="pun">.</span><span class="pln">length</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">;</span><span class="pln"> </span><span class="com">// adding at the end</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="str">"three"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">]</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="str">"six"</span><span class="pun">);</span><span class="pln"> </span><span class="com">// but usually we prefer using the push method for adding</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"six"</span><span class="pun">] &nbsp;<strong>// a new element at the end</strong></span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div>

When using indexes, be careful not to leave "holes" in the array:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">7</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'height'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"height"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"six"</span><span class="pun">,</span><span class="pln"> </span><strong><span class="kwd">undefined</span><span class="pln"> </span><span class="pun">×</span><span class="pln"> </span><span class="lit">1</span></strong><span class="pun">,</span><span class="pln"> </span><span class="str">"height"</span><span class="pun">]</span></li>
</ol></div>

This array is valid, but having a [6] equal to "undefined" is often prone to errors. Be careful when using absolute indexes for adding elements. We recommend using the `push` method instead.


##### Removing elements from an array

The recommended method is to use the `splice` method:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">array</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="pln">start</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">array</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="pln">start</span><span class="pun">,</span><span class="pln"> deleteCount</span><span class="pun">)</span></li>
</ol></div>

+ __start:__ index at which to start changing the array (with origin 0). 
+ __deleteCount (Optional):__ an integer indicating the number of old array elements to remove.  If deleteCount is greater than the number of elements left in the array starting at start, then all of the elements through the end of the array will be deleted. __If deleteCount is omitted,__ deleteCount will be equal to `(array.length - start)`, i.e., __all of the elements beginning with start index on through the end of the array will be deleted.__
+ __Return value:__ an array containing the deleted elements. If only one element is removed, an array of one element is returned. If no elements are removed, an empty array is returned.

Examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"six"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pln"> </span><span class="pun">×</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="str">"height"</span><span class="pun">]</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="lit">6</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">);</span><span class="pln"> </span><span class="com">// remove element at the sixth index, the undefined one!</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="kwd">undefined</span><span class="pln"> </span><span class="pun">×</span><span class="pln"> </span><span class="lit">1</span><span class="pun">]</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"six"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"height"</span><span class="pun">]</span><span class="pln"> </span><span class="com">// it's no more here :-)</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span><span class="pln"> </span><span class="com">// remove the three first elements</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">[</span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"six"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"height"</span><span class="pun">]</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="pln">a</span><span class="pun">.</span><span class="pln">length</span><span class="pun">-</span><span class="lit">1</span><span class="pun">);</span><span class="pln"> </span><span class="com">// remove the last element</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="str">"height"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">[</span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"six"</span><span class="pun">]</span></li>
</ol></div>


##### Removing element with `pop` method

Recommended method for removing the last element: the `pop` method!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pun">&gt;</span><span class="pln"> a</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">[</span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"six"</span><span class="pun">]</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> a</span><span class="pun">.</span><span class="pln">pop</span><span class="pun">();</span><span class="pln"> </span><span class="com">// remember push/pop = add / remove element at last position!</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"six"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"five"</span><span class="pun">]</span></li>
</ol></div>

Trap: the delete method is not good for removing an element from an array!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">delete</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">1</span><span class="pun">];</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">true</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="str">"four"</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pln"> </span><span class="pun">×</span><span class="pln"> </span><span class="lit">1</span><span class="pun">]</span><span class="pln"> </span><strong><span class="com">// the element became undefined, </span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // but it's still in the array!</span></strong></li>
</ol></div>


#### Arrays of arrays

It is possible for an array to be an element within an array! This example shows an array made of two arrays of three elements each. It's a 2x3 matrix with two rows and three columns!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[[</span><span class="lit">1</span><span class="pun">,</span><span class="lit">2</span><span class="pun">,</span><span class="lit">3</span><span class="pun">],</span><span class="pln"> </span><span class="pun">[</span><span class="lit">4</span><span class="pun">,</span><span class="lit">5</span><span class="pun">,</span><span class="lit">6</span><span class="pun">]];</span><span class="pln"> </span><span class="com">// a is a matrix: 2 rows, 3 columns.</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span><span class="pln"> </span><span class="com">// first row</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">1</span><span class="pun">];</span><span class="pln"> </span><span class="com">// second row</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">4</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">6</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">0</span><span class="pun">][</span><span class="lit">0</span><span class="pun">];</span><span class="pln"> </span><span class="com">// top left element</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">1</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">0</span><span class="pun">][</span><span class="lit">1</span><span class="pun">];</span><span class="pln"> </span><span class="com">// second element, first line</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">2</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">0</span><span class="pun">][</span><span class="lit">2</span><span class="pun">];</span><span class="pln"> </span><span class="com">// third element, first line</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="lit">3</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">1</span><span class="pun">][</span><span class="lit">0</span><span class="pun">];</span><span class="pln"> </span><span class="com">// first element, second line</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="lit">4</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">1</span><span class="pun">][</span><span class="lit">1</span><span class="pun">];</span><span class="pln"> </span><span class="com">// second element, second line</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="lit">5</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">1</span><span class="pun">][</span><span class="lit">2</span><span class="pun">];</span><span class="pln"> </span><span class="com">// third element, second line</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">6</span></li>
</ol></div>

It is possible to have different arrays with different lengths and different types of element in an array:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">4</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">4</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">]</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">[</span><span class="lit">1</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'michel'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'henri'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'francois'</span><span class="pun">]</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="str">"michel"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"henri"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"francois"</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">[</span><span class="typ">Array</span><span class="pun">(</span><span class="lit">5</span><span class="pun">),</span><span class="pln"> </span><span class="typ">Array</span><span class="pun">(</span><span class="lit">3</span><span class="pun">)]</span></li>
</ol></div>


#### Notes for 3.2.1 Arrays

+ Elements in an array
  + array: a collection of "things", including strings, integer values, decimal values, boolean values, or any objects
  + creating an array: putting elements btw "[" abd "]", e.g., `var myarr = ['red', 'blue', 'yellow', 'purple'];`
  + each element of an array w/ key/index and a value
  + type of an array: object, e.g., `var a = []; typeof a; // "object"`
  + index beginning at "0"
  + properties and methods: `let a = [...];`
    + size of an array: `a.length`
    + sort an array: `a.sort([function_that_compares_two_elements]);`
      + numeric: return array object from lowest to highest
      + string: return array object w/ element alphabetically
      + object: depending on `function_that_compares_two_elements`, e.g., 

        ```js
        var persons = [
            {givenName: 'Michel', familyName: 'Buffa', age:51},
            {givenName: 'Pig', familyName: 'Bodine', age:20},
            {givenName: 'Pirate', familyName: 'Prentice', age:32}
        ];
        
        function compareByAge(a,b) { // comparison function, a and b are persons
          if (a.age < b.age)         // compare by age
            return -1;
          if (a.age > b.age)
            return 1;
          return 0;
        }

        persons.sort(compareByAge);
        ```

    + remove n elements starting from idx: `a.splice(idx, n);`; e.g., `a.splice(2, 1); // remove 1 elt starting from idx=2 (3rd elt)`
  + type of elements: different types of element allowed in an array; e.g., `let a = [1, 2, "three"]`

+ Adding element
  + using a new index
    + not to leave a hole in the array; e.g., `let a = [1, 2, 3]; a[4] = 4; a; // a = [1, 2, 3, undefined x 1, 4]`
    + example: `let a = [1, 2, 3]; a[3] = "four"; a[a.length] = "five"; // a = [1, 2, 3, "four", "five"]`
  + adding a new element at the end w/ `push()` method, e.g., `a.push("five"); // a = [..., "five"]`
  + recommendation: using `push()` method

+ Removing element
  + `splice()` method
    + syntax:
      + `array.splice(start)`
      + `array.splice(start, deleteCount)`
    + parameters
      + __start:__ index at which to start changing the array
      + __deleteCount:__  (optional)
        + an integer indicating the number of old array elements to remove
        + `deleteCount` > size of array left (from start to end): remove all elements
        + `deleteCount` omitted: `deleteCount = array.length - start`, delete all elements starting from `start` to end of array
    + return value:
      + an array containing the deleted elements
      + a one-element array if only one element removed
      + empty array if no element removed
    + examples: `a = [1, 2, 3, "four", "five", "six", undefined × 1, "height"];`
      + remove element at 6th index: `[undefined x 1]` & `a = [1, 2, 3, "four", "five", "six", "height"]`
      + remove the 1st three elements: `a.splice(0, 3); // [1, 2, 3]` & `a = ["four", "five", "six", "height"]`
      + remove the last element: `a.splice(a.length-1); // "height"` & `a = ["four", "five", "six"]`
  + `pop()` method
    + recommended method for removing the last element
    + example: `a = ["four", "five", "six"]`, `a.pop(); // "six"` & `a = ["four", "five"]`
  + `delete()` method
    + not good for removing an element from an array
    + example: `delete a[1]; // true` & `a = ["four", undefined × 1]`

+ Arrays of arrays
  + numerical array
    + a `n x m` matrix
    + examples
      + a matrix w/ 2 rows, 3 columns: `var a = [[1,2,3], [4,5,6]];`
      + accessing rows: `a[0]; // [1, 2, 3]` & `a[1]; // [4, 5, 6]`
      + element: `a[0][0]; // top left element` $\to$ 1; `a[0][1]; // second element, first line` $\to$ 2; `a[1][2]; // third element, second line` $\to$ 6
  + array w/ differnet types of arrays, e.g., `a[0] = [1, 2, 3, 4, 5]; a[1] = ['michel', 'henri', 'francois']; a; // [Array(5), Array(3)]`

+ [`array.push()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)
  + syntax: `arr.push([element1[, ...[, elementN]]])`
  + docstring: add one or more elements to the end of an array and return the new length of the array
  + parameters
    + `elementN`: the element(s) to add to the end of the array.
  + return: The `new` length property of the object upon which the method was called.

+ [`array.pop()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)
  + syntax: `arr.pop()`
  + docstring:
    + remove the __last__ element from an array and return that element
    + change the length of the array
  + return: the removed element from the array; `undefined` if the array is empty.

+ [`array.sort()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
  + syntax: `arr.sort([compareFunction])`
  + docstring:
    + sort the elements of an array in place and return the sorted array
    + default sort order: ascending, built upon converting the elements into strings, then comparing their sequences of UTF-16 code units values.
  + parameters
    + `compareFunction` (optional):
      + specify a function that defines the sort order.
      + omitted: the array elements are converted to strings, then sorted according to each character's Unicode code point value.
  + compare function

    ```js
    function compare(a, b) {
      if (a is less than b by some ordering criterion) {
        return -1;
      }
      if (a is greater than b by the ordering criterion) {
        return 1;
      }
      // a must be equal to b
      return 0;
    }
    ```

+ [`array.splice()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
  + syntax: `let arrDeletedItems = arr.splice(start[, deleteCount[, item1[, item2[, ...]]]])`
  + docstring: change the contents of an array by removing or replacing existing elements and/or adding new elements in place
  + parameters
    + `start`: the index at which to start changing the array
      + start &lt; array.length: `start` set to the length of the array. No element will be deleted but the method will behave as an adding function, adding as many element as item[n*] provided.
      + negative: begin that many elements from the end of the array (`-n` is the index of the nth last element)
      + array.length + start &lt; 0: begin from index `0`
    + `deleteCount` (optional)
      + an integer indicating the number of elements in the array to remove from start
      + omitted, or &ge; array.length - start: all the elements from start to the end of the array will be deleted
      + &le; 0: no elements removed
    + `item1, item2, ...` (optional):
      + the elements to be added to the array, beginning from start
      + not specifying any elements: only removing elements from the array
  + return:
    + an array containing the deleted elements
    + a one-element array if only one eleemnet removed
    + an empty array ih noyjing removed




#### Knowledge check 3.2.1

```js
var a = [1, 2, 3, "four", "five", "six", "seven", "height"]
```

1. How would you remove elements "four" and "five" at once?

  a. `a.splice(3, 2);`<br>
  b. `a.delete(4, 5);`<br>
  c. `a.remove(3, 2);`<br>
  d. `a.splice(2, 4);`<br>

  Ans: a<br>
  Explanation: You must use the `splice` method. The arguments are two-fold: the starting index, and the number of elements to remove. "four" is at index 3, the number of elements to remove is 2. The correct answer is `a.splice(3, 2);`.


### 3.2.2 Strings are arrays of characters

Yes, they do look like arrays!

JavaScript strings are "like" arrays of characters, but they have some limitations, and some dedicated properties and methods:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> s </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> s</span><span class="pun">[</span><span class="lit">0</span><span class="pun">];</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"M"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> s</span><span class="pun">[</span><span class="lit">1</span><span class="pun">];</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"i"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> s</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">6</span></li>
</ol></div>

Indeed, the string `s` behaves like an array, it has the `length` property like an array, and we can access individual characters using indexes that go from 0 to `length-1`, like arrays...

However... they are not quite the same as arrays!

You cannot add elements to strings using a non-existent index, you cannot use the push/pop methods for adding/removing  characters at the end of the string:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pln">s</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="str">' Buffa'</span><span class="pun">);</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">ERROR</span><span class="pun">:</span><span class="pln"> VM5748</span><span class="pun">:</span><span class="lit">1</span><span class="pln"> </span><span class="typ">Uncaught</span><span class="pln"> </span><span class="typ">TypeError</span><span class="pun">:</span><span class="pln"> s</span><span class="pun">.</span><span class="pln">push </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> a </span><span class="kwd">function</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"> at </span><span class="str">&lt;anonymous&gt;</span><span class="pun">:</span><span class="lit">1</span><span class="pun">:</span><span class="lit">3</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">(</span><span class="pln">anonymous</span><span class="pun">)</span><span class="pln"> </span><span class="pun">@</span><span class="pln"> VM5748</span><span class="pun">:</span><span class="lit">1</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">s</span><span class="pun">[</span><span class="pln">s</span><span class="pun">.</span><span class="pln">length</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'B'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// add 'B' at the end?</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"B"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">s</span><span class="pun">[</span><span class="pln">s</span><span class="pun">.</span><span class="pln">length</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'u'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// add 'u' at the end?</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">"u"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">s</span><span class="pun">[</span><span class="pln">s</span><span class="pun">.</span><span class="pln">length</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">'f'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// add 'f' at the end?</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">"f"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">s</span><span class="pun">;</span><span class="pln"> </span><span class="com">// s remained UNCHANGED!</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="str">"Michel"</span></strong><span class="pln"> </span></li>
</ol></div>

+ You cannot use push/pop as this raises an error "is not a function" (_lines 1-5_)
+ You can try to put elements out of the range of the string: nothing will happen and the string will remain unchanged (_lines 7-17_)

You can't even modify a character using an index. Strings are "read only" when using brackets to access individual characters!

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> s </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> s</span><span class="pun">[</span><span class="lit">0</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">"R"</span><span class="pun">;</span><span class="pln"> </span><span class="com">// trying to change the 'M' into an 'R'</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"R"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">s</span><span class="pun">;</span><span class="pln"> </span><span class="com">// no luck!</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"Michel"</span></li>
</ol></div>

You also can't remove characters using the array's splice method:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> s</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">ERROR</span><span class="pun">:</span><span class="pln"> VM716</span><span class="pun">:</span><span class="lit">1</span><span class="pln"> </span><span class="typ">Uncaught</span><span class="pln"> </span><span class="typ">TypeError</span><span class="pun">:</span><span class="pln"> s</span><span class="pun">.</span><span class="pln">splice </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> a </span><span class="kwd">function</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> at </span><span class="str">&lt;anonymous&gt;</span><span class="pun">:</span><span class="lit">1</span><span class="pun">:</span><span class="lit">3</span></li>
</ol></div>

So: how do we add characters to a string, how can we modify a string? How can we delete elements in a string ?

Strings come with a whole set of methods, which we'll come to in module 4 when we talk about JavaScript objects (in the section titled "JavaScript predefined objects"). Without going into detail just yet, here are some examples:

#### Concatenation with `+` operator

__Adding a string to the beginning of a string using the + operator:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> s </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> s </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Hello "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> s</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"Hello Michel"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> s </span><span class="pun">=</span><span class="pln"> </span><span class="str">'O'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> s</span><span class="pun">;</span></strong><span class="pln"> </span><span class="com">// equivalent to push('0') with arrays</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"OHello Michel"</span></li>
</ol></div>

__Adding a string to the end of another one with the + operator:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="pun">&gt;</span><span class="pln">s </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">"Michel"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln"> s </span><span class="pun">+=</span><span class="pln"> </span><span class="str">' Buffa'</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"Michel Buffa"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> s</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"Michel Buffa"</span></li>
</ol></div>


#### Removing substring

__Removing chars from a string using the `substring` method:__

Removing the last char (equivalent to the pop method from arrays):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> s </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><strong><span class="pln">&nbsp;</span>s = s.substring(0, s.length-1);</strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"Miche"</span></li>
</ol></div>


__Removing a certain number of chars starting from a string, starting at a given index:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> s </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">function</span><span class="pln"> removeChars</span><span class="pun">(</span><span class="pln">s</span><span class="pun">,</span><span class="pln"> startIndex</span><span class="pun">,</span><span class="pln"> numberOfCharsToRemove</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp;return</span><span class="pln"> s</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> startIndex</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln">&nbsp; &nbsp;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; s</span><span class="pun">.</span><span class="pln">substring</span><span class="pun">(</span><span class="pln">startIndex&nbsp;</span><span class="pun">+&nbsp;</span><span class="pln">numberOfCharsToRemove</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// remove 3 consecutive chars from s, starting at index = 1</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">s </span><span class="pun">=</span><span class="pln"> removeChars</span><span class="pun">(</span><span class="pln">s</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span><span class="pln"> </span><span class="com">// will display "Mel" in the console</span></li>
</ol></div>


__Replacing a char at a given index:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> replaceAt</span><span class="pun">(</span><span class="pln">s</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">,</span><span class="pln"> character</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> s</span><span class="pun">.</span><span class="pln">substr</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> index</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> character </span><span class="pun">+</span><span class="pln"> s</span><span class="pun">.</span><span class="pln">substr</span><span class="pun">(</span><span class="pln">index</span><span class="pun">+</span><span class="pln">character</span><span class="pun">.</span><span class="pln">length</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="kwd">var</span><span class="pln"> s2 </span><span class="pun">=</span><span class="pln"> </span><span class="str">"JavaScript"</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln">s2 </span><span class="pun">=</span><span class="pln"> replaceAt</span><span class="pun">(</span><span class="pln">s2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="str">"o"</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">s2</span><span class="pun">);</span><span class="pln"> </span><span class="com">// will display "JovaScript"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="com">// it also works with a string instead of a simple char</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">s2 </span><span class="pun">=</span><span class="pln"> replaceAt</span><span class="pun">(</span><span class="pln">s2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="str">"Coca"</span><span class="pun">);</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">s2</span><span class="pun">);</span><span class="pln"> </span><span class="com">// Will display "CocaScript"</span></strong></li>
</ol></div>


#### Notes for 3.2.2 Strings are arrays of characters

+ String as array
  + "like" array of characters
    + behave like an array
    + w/ `length` property
    + able to access individual characters w/ indexes
    + example: `let s = 'Michel'; s[0]; // 'M'`, `s[1] // 'i'` & `s.length; // 6`
  + limitations
    + unable to add elements to string using a non-existent index
    + unable to use `push/pop` methods for adding/removing characters at the end of string
    + unable to modify a character w/ an index
    + unable to remove a character w/ `splice` method
    + examples
      + using `push` method: `s.push('Buffa); // ERROR: VM5748:1 Uncaught TypeError: s.push is not a function at <anonymous>:1:3 (anonymous) @ VM5748:1`
      + adding a character at the end but remaining UNCHANGED: `s[s.length] = 'B'; // "B"` but `s; // "Michel"`
      + changing a character in string: `s[0] = "R"; // "R"` & `s; // "Michel"`
      + using `splice` method: `s.splice(0, 3); // ERROR: VM716:1 Uncaught TypeError: s.splice is not a function at <anonymous>:1:3`

+ String operation
  + concatenation w/ `+` operator
    + prepend: `var s = 'Michel'; s = "Hello " + s; // "Hello Michel"`
    + append: `var s = 'Michel'; s += " Buffa"; // "Michel Buffa"`
  + removing substring w/ `substring()` method; e.g.,
    + removing last char (equivalent to `pop` method): `s = s.substring(0, s.length-1); // "Miche"`
    + removing a certain number of chars: `function removeChars(s, startIndex, numberOfCharsToRemove) { return s.substring(0, startIndex) + s.substring(startIndex + numberOfCharsToRemove); }` & `var s = 'Michel'; s = removeChars(s, 1, 3); console.log(s); // "Mel"`
  + replacing a char w/ index
    + `function replaceAt(s, index, character) { return s.substr(0, index) + character + s.substr(index+character.length); }`
    + `var s2 = "JavaScript"; s2 = replaceAt(s2, 1, "o"); console.log(s2); // "JovaScript"`
    + `s2 = replaceAt(s2, 0, "Coca"); console.log(s2); // Will display "CocaScript"`

+ [`str.substring()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)
  + syntax: `str.substring(indexStart[, indexEnd])`
  + docstring: return the part of the string between the start and end indexes, or to the end of the string.
  + parameters
    + `indexStart`: the index of the first character to include in the returned substring
    + `indexEnd` (optional): the index of the first character to exclude from the returned substring
  + return: the part of the string between the start and end indexes, or to the end of the string


#### Knowledge check 3.2.2

1. What is the name of the function/method for removing a given number of chars from a string, starting at a given index?

  a. There is no built-in method/function for that, we need to build one.<br>
  b. `splice`, with the same syntax we used with JavaScript arrays<br>
  c. `substring`<br>

  Ans: <span style="color: brown;">a</span>, xc<br>
  Explanation: Indeed, there is no built-in function for that. We presented in the course a `removeChars(s, startIndex, numberOfCharsToRemove)` function that uses the substring method.


### 3.2.3 Iterating on array elements


#### Live coding video: iterating on arrays

<a href="https://edx-video.net/W3CJSIXX2016-V003300_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y7dzppcz)

Get the source code of the example shown in the video:

[CodePen Demo](https://codepen.io/w3devcampus/pen/VWYMNK)

[Local Demo](src/03b-example02.html)

Let's study the different methods for iterating on array elements.


#### Method #1: iterating using `forEach`

The `forEach` method takes a single argument that is a function/callback that can have one, two or three parameters:

+ The first parameter is the current element of the array,
+ The second parameter (optional) is the index of the current element in the array,
+ The third element is the array itself

__Typical use with only one parameter (the current element):__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'Monday'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'Tuesday'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'Wednesday'</span><span class="pun">];</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">a</span><span class="pun">.</span><span class="pln">forEach</span></strong><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><span class="pln">day</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; // day is the current element</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> day </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; "&lt;br&gt;"</span><span class="pun">;</span><span class="pln"> </span><span class="com">// will display Monday, Tuesday, Wednesday</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">})</span></li>
</ol></div>

This is the most practical way to iterate on each individual element of a collection (array, string);

[CodePen Demo](https://codepen.io/w3devcampus/pen/QpRybG)

[Local Demo](src/03b-example03.html)


Now, let's iterate on an array of person, and use two parameters in the callback function in order to get the index of the current element:

[CodePen Demo](https://codepen.io/w3devcampus/pen/rygxpr)

[Local Demo](src/03b-example04.html)

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> persons </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp;{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Michel'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">51</span><span class="pun">},</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp;{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Henri'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">20</span><span class="pun">},</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp;{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Francois'</span><span class="pun">,</span><span class="pln"> age</span><span class="pun">:</span><span class="lit">29</span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">];</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">persons</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">(</span><strong><span class="pln">p</span><span class="pun">,</span><span class="pln"> index</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> p</span><span class="pun">.</span><span class="pln">name </span><span class="pun">+</span><span class="pln"> </span><span class="str">", age "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> p</span><span class="pun">.</span><span class="pln">age </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span style="color: #000000;" color="#000000">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span>", at index "<span class="pln"> </span><span class="pun">+</span><span class="pln"> index </span><span class="pun">+</span><span class="pln"> </span><span class="str">" in the array&lt;br&gt;"</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">});</span></li>
</ol></div>

__Finally, let's use three parameters, the last one being the array itself__

This can be useful if we need to know the length of the array, or do special things within the array (add/change/move elements during the iteration):

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZKyMQj)

[Local Demo](src/03b-example05.html)

In this example, we used the third parameter (the array) to access its length inside the iteration loop.


#### Method #2: iterating on an array using regular loop statements

You can use any standard loop statement that we saw during in module 2. The most common way to iterate over an array is to use a `for` loop from 0 to length-1. 

Using this method allows elements to be iterated two by two, or the loop to be broken in the middle using the `break` instruction, etc.

__Iterating over all elements in an array, using a for loop__

[CodePen Demo](https://codepen.io/w3devcampus/pen/evaJKL)

[Local Demo](src/03b-example06.html)

Another example where we iterate two by two (just changed the increment in the for loop):

[CodePen Demo](https://codepen.io/w3devcampus/pen/zZQrme)

[Local Demo](src/03b-example07.html)


#### Notes for 3.2.3 Iterating on array elements

+ Iterating w/ array
  + iterating w/ `forEach`
    + parameters of `forEach`
      + the current element of the array
      + (optional) the index of the current element in the array
      + (optional) the array itself
    + examples:
  
      ```js
      var a = ['Monday', 'Tuesday', 'Wednesday'];

      a.forEach(function(day) { // day is the current element
          document.body.innerHTML += day + "<br>"; // will display Monday, Tuesday, Wednesday
      })

      persons.forEach(function(p, index) {
        document.body.innerHTML += p.name + ", age " + p.age +
                             ", at index " + index + " in the array<br>";
      });

      persons.forEach(function(p, index, theArray) {
        document.body.innerHTML += p.name + ", age " + p.age +
            ", at index " + index + " in the array of " + theArray.length + " elements<br>";
      });
      ```

  + iterate using regular `for` loop
    + most common way to iterate over an array is to use a `for` loop from 0 to length-1
    + allowing element to be iterated step  other than 1 or broken in the middle w/ `break` instruction
    + examples:

      ```js
      var persons = [
        {name:'Michel', age:51}, {name:'Henri', age:20}, {name:'Francois', age:29}
      ];

      for(var i = 0; i < persons.length; i++) {
        var p = persons[i]; // current element
        document.body.innerHTML += p.name + "<br>"; 
      }

      for(var i = 0; i < persons.length; i+=2) {
        var p = persons[i]; // current element
        document.body.innerHTML += p.name + "<br>"; 
      }
      ```

+ [`array.forEach` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
  + syntax:

    ```js
    arr.forEach(callback(currentValue[, index[, array]]) {
      // execute something
    }[, thisArg]);
    ```
  
  + docstring: execute a provided function once for each array element
  + parameters
    + `callback`: function to execute on each element. It accepts between one and three arguments:
      + `currentValue`: The current element being processed in the array.
      + `index` (optional): The index of `currentValue` in the array.
      + `array` (optional): The array `forEach()` was called upon.
    + `thisArg` (optional): Value to use as `this` when executing `callback`.
  + return: `undefined`

#### Knowledge check 3.2.3

1. Can you iterate only on elements that have an odd index using the forEach iterator, without adding a test inside the instructions in the body of the loop? (No/Yes)

  Ans: No<br>
  Explanation: No, the forEach method iterates on all the elements of an array. You can use a for loop for iterating on odd indexes, like that: `for(var i = 1; i less than a.length; i += 2) {....}`


### 3.2.4 Discussion and projects

Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ Which syntax do you prefer for iterating arrays?
+ We decided not to explain all the things you can do with the `splice` method. It's a very powerful method, but showing all its features could be overwhelming. However, if you're curious, please look on the Web for more details. Do you think we've been right not to tell you all the possibilities of splice?

#### optional project: an interactive picture album browser

Let's start with an array variable like that:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">let myPicturesArray = [</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"accusamus beatae ad facilis cum similique qui sunt"</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/92c952"</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/92c952"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">},</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"reprehenderit est deserunt velit ipsam"</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/771796"</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/771796"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">},</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">51</span><span class="pun">,</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"non sunt voluptatem placeat consequuntur rem incidunt"</span><span class="pun">,</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/8e973b"</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/8e973b"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">},</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">52</span><span class="pun">,</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"eveniet pariatur quia nobis reiciendis laboriosam ea"</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/121fa4"</span><span class="pun">,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/121fa4"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">},</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">127</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"magnam quia sed aspernatur"</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/74456b"</span><span class="pun">,</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/74456b"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">},</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "albumId"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "id"</span><span class="pun">:</span><span class="pln"> </span><span class="lit">128</span><span class="pun">,</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "title"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"est facere ut nam repellat numquam quia quia eos"</span><span class="pun">,</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "url"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/600/b0931d"</span><span class="pun">,</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; "thumbnailUrl"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"https://placehold.it/150/b0931d"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">];</span></li>
</ol></div>

+ It's an array of pictures, each picture having a URL, a URL for a tiny version of the picture, called a thumbnail, a title, and the name of the album it belongs to, that can be used as a picture description (HTML `alt` attribute) but also for displaying it next to the picture.
+ Here is a small example that iterates on the pictures and create `<img>` elements on the fly:

[CodePen Demo](https://codepen.io/w3devcampus/pen/KqzPOm)

[Local Demo](src/03b-example08.html)

What you will have to do:

1. __Improve the display, by adding margins (CSS), shadows, border, and changing the URLs for real pictures.__ Remember that you need to have a smaller versions of the pictures, i.e., thumbnails. You can use existing images (images.google.com is your friend) or images you upload somewhere.
1. __Use JavaScript for adding a click event listener on each image,__ then when clicked, you will show a bigger version of each picture. For the moment, just change the value of the src attribute of the clicked image (set it to the URL of the full size image from the array).
1. __Try to make something nicer: reserve a `<div>` on the right of the document so to display the clicked image with a bigger size.__ In that case, you will need to create an image (only once, after the first click), to set it to the size of the div (use the width and height attributes of the img element), and to append it to the div.
1. __Try to add more images, and find a way to display them per album.__ Create buttons entitled "album1", "album2", etc., and when clicked, you will only display images from the selected album.
1. __[Advanced] Add an option for deleting a picture.__ It should be removed from the document and from the array too...
1. __Feel free to add any interesting feature you think about ;-)__


