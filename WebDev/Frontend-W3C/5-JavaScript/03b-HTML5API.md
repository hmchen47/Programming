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

[Local Demo](src/ls/03b-exapmple01.js)


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

###### JavaScript arrays are objects and have some useful properties and methods

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

##### Elements can be of different types in a same array

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

This array is valid, but having a \[6\] equal to "undefined" is often prone to errors. Be careful when using absolute indexes for adding elements. We recommend using the `push` method instead.


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


##### Recommended method for removing the last element: the `pop` method!

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


##### Arrays of arrays

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

#### Knowledge check 3.2.1 (not graded)

```js
var a = [1, 2, 3, "four", "five", "six", "seven", "height"]
```

1. How would you remove elements "four" and "five" at once?

  a. `a.splice(3, 2);`<br>
  b. `a.delete(4, 5);`<br>
  c. `a.remove(3, 2);`<br>
  d. `a.splice(2, 4);`<br>

  Ans: <br>
  Explanation: 




