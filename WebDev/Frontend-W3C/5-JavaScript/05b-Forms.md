# Module 5: Working with forms


## 5.2 [Built-in JavaScript objects


### 5.2.1 References and objects

#### Live coding video: references and objects

<a href="https://edx-video.net/W3CJSIXX2016-V004500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/2wc8kh2p)


__Source code shown in the video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/KqmGgq?editors=0012)

[Local Demo](src/js/05b-exmapl01.js)


First of all, we have to define "reference". Unlike a pointer variable, which contains the actual address of an object within the memory, a reference variable is an alias to a variable. This means that when you modify a reference variable, the original variable is modified too. This is because the two variables reference (i.e. point to) the same object.

When you define a variable (such as `var x = 10;` or `let name = "Michel";` or `let courseAuthor = {firstName:'Michel', lastName:'Buffa'}`, this is what happens:

+ If its value is a primitive value (number, string, or boolean), _the variable contains this value directly_.
+ If its value is an object, the variable contains _the memory address of the object_. We say that this variable "points to" an object (or references this object). Accessing the variable will automatically resolve the reference, meaning that the value of the variable is the referenced object.

Examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="com">// Defining two variables</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span><span class="pln"> </span><span class="com">// the variable x contains the primitive datum 2</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> a</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="pun">}</span><span class="pln"> </span><span class="com">// The variable y references the object {a: 2}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// "Copying" two variables</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> x2 </span><span class="pun">=</span><span class="pln"> x</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> y2 </span><span class="pun">=</span><span class="pln"> y</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> y3 </span><span class="pun">=</span><span class="pln"> y</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">// Modifying copied variables</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">x2 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">y2 </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> a</span><span class="pun">:</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="pun">};</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// Check</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">x</span><span class="pun">;</span><span class="pln"> </span><span class="com">// 2 &lt;- x is not modified because it contains a primitive value</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">y</span><span class="pun">;</span><span class="pln"> </span><span class="com">// { a: 2 } &lt;- y is not modified because y2 does not point to same object</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">y3</span><span class="pun">.</span><span class="pln">a </span><span class="pun">=</span><span class="pln"> </span><span class="lit">4</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">y</span><span class="pun">;</span><span class="pln"> </span><span class="com">// { a: 4 } &lt;- The object referenced by "y" and "y3" is modified</span></li>
</ol></div>

Of course, these rules also apply to the properties of objects.

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> driver </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; name</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Jean'</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> car </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; color</span><span class="pun">:</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">,</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; driver</span><span class="pun">:</span><span class="pln"> driver</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">driver</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Albert'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">car</span><span class="pun">.</span><span class="pln">driver</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span><span class="pln"> </span><span class="com">// 'Albert'</span></li>
</ol></div>

JavaScript is a "pass by value" language, unlike some other languages, which are "pass by reference" languages. This means that when you pass a variable to a function as argument, the value of the variable is copied into the argument.

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> sum</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln"> b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; a </span><span class="pun">=</span><span class="pln"> a </span><span class="pun">+</span><span class="pln"> b</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">sum</span><span class="pun">(</span><span class="pln">x</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span><span class="pln"> </span><span class="com">// returns 5</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">x</span><span class="pun">;</span><span class="pln"> </span><span class="com">// 2 &lt;- but x equals 2</span></li>
</ol></div>

When working with objects, the reference of the object is copied into the argument. That means you can modify the referenced object. But if you change the reference (for example by assigning a new object), the original variable (which now points to another object) will not be modified.

Example 1:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> obj </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> x</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> add</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln"> b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> a</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+=</span><span class="pln"> b</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">add</span><span class="pun">(</span><span class="pln">obj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">obj</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span><span class="pln"> </span><span class="com">// 5 &lt;- The referenced object is modified</span></li>
</ol></div>

Example 2:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> obj </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> x</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> addAndSet</span><span class="pun">(</span><span class="pln">a</span><span class="pun">,</span><span class="pln"> b</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> addition </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">x </span><span class="pun">+</span><span class="pln"> b</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> x</span><span class="pun">:</span><span class="pln"> addition </span><span class="pun">};</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">};</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">addAndSet</span><span class="pun">(</span><span class="pln">obj</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">obj</span><span class="pun">.</span><span class="pln">x</span><span class="pun">;</span><span class="pln"> </span><span class="com">/* 2 &lt;- The referenced object is not modified</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="com">because at the end of the function the variable "obj"</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com"> and the variable "a" are not referencing the same object.*/</span></li>
</ol></div>

Other examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> originalObject </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Michel'</span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> copy </span><span class="pun">=</span><span class="pln"> originalObject</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> copy</span><span class="pun">.</span><span class="pln">name</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"Michel"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> copy</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Dark Vador'</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">"Dark Vador"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> originalObject</span><span class="pun">.</span><span class="pln">name</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">"Dark Vador"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// They are the same. originalObject and copy are two "references" of the same object in memory</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// If we change the name, we change the value in memory, but copy and originalObject "point to" the</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// same place, to the same object. They are just "pointers" or "reference" to the same object</span></li>
</ol></div>


#### Notes for 5.2.1 References and objects

+ References and objects
  + pointer variable: containing the actual address of an object within the variable
  + reference variable: an alias to a variable
  + when modifying a reference variable, the original variable is modified $\gets$ two variables the sam eobject
  + types of values of a variable
    + primitive value (number, string, or boolean):
      + the variable containing the value directly
      + example: `let x = 10;`, `let name = 'Michel'`
    + object:
      + containing the memory address of the object
      + pointing to an object or reference this object
      + accessing the variable automatically resolving the reference
      + the value of the variable is the referenced object
  + function
    + primitive values
      + a "pass by value" language
      + passing a variable to a function as argument, the value of the variable copied into the argument
    + objects
      + reference of object copied into the argument
      + able to modify the reference object
      + change of reference: the origin variable (now point to another object) not modified
  
+ Example: primitive and object
  + definiting two variables: `var x = 2; var y = {a: 2}`
  + copying two variables: `var x2 = x; var y2 = y; var y3 = y;`
  + modifying copied variables: `x2 = 4; y2 = {a: 3}`
  + `x` not modified: primitive value
  + `y` not modified: `y` & `y2` pointing to different objects
  + modifying value of property: `y3.a = 4;`
  + `y` and `y3`: both modified $\gets$ object reference changing to `{a: 2}`

+ Example: properties of objects
  + defining an object: `var driver = { name: 'Jean' }; var car = {color: 'red', driver: driver };`
  + modifying drive name: `driver.name = 'Albert';`
  + car driver modified: `car.driver.name; // 'Albert';`

+ Example: function passed by value
  + defining a variable: `var x = 2;`
  + defining a function: `function sum(a, b) { a = a + b; return a; }`
  + calling function `sum`: `sum(x, 3); // 5`
  + `a` modified within function `sum` but `x` remaining the same: `x; // 2`

+ Example: function argument as object
  + defining object: `var obj = {x: 2 };`
  + defining function: `function add(a, b) { a.x += b; }`
  + calling function `add()`: `add(obj, 3);`
  + the reference object modified: `obj.x; // 5`
  + defining function: `function addAndSet(a, b) { var addition = a.x + b; a = (x: addition); }`
  + calling function `addAndSet()`: `addAndSet(obj, 3);`
  + reference object not modified (`obj` and `a` not pointing to the same object at then end of the function): `obj.x; // 2`

+ Example: modifying copied object to modify original object
  + original object: `var originalObject = { name: 'Michel' };`
  + copied object: `var copy = originalObject;`
  + verification: `copy.name; // 'Michel'`
  + modify copied object: `copy.name = 'Dark Vador';`
  + original object verification: `originalObject.name; // 'Dark Vador'`


### 5.2.2 Comparing two objects

Comparing two objects will only return true if they point to the same object (i.e., if they have the same reference).

Two objects of the same type, with the same property value, that look identical, will not be equal one to another if they don’t have the same reference (if they point to different places in memory).

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> originalObject </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Michel'</span><span class="pun">};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> copy </span><span class="pun">=</span><span class="pln"> originalObject</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> copy </span><span class="pun">===</span><span class="pln"> originalObject</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">true</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> anotherObject </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">name</span><span class="pun">:</span><span class="str">'Michel'</span><span class="pun">};</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> copy </span><span class="pun">===</span><span class="pln"> anotherObject</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">false</span></li>
</ol></div>


#### Notes for 5.2.2 Comparing two objects

+ Object comparison
  + returning boolean value whether w/ the same reference (pointing to the same objects)
  + identical objects but unequal
    + returning `false`
    + objects w/ same type, same property values
    + w/ difference references
    + pointing to difference places in memory
  
+ Example: comapring objects
  + defining objects: `var originalObject = { name: 'Michel' }; var copy = originalObject;`
  + comparing original and copied objects: `copy === originalCopy; // true`
  + defining another object: `var anotherObject = { name: 'Michel' };`
  + comparing copied and another objects: `copy === anotherObject; // false`



### 5.2.3 The "global" window object

It is time to tell you the truth: the JavaScript code is executed by an “environment" (usually a Web browser, but there are some HTTP Web servers that use JavaScript for coding the server side of Web sites of applications, such as the NodeJS HTTP server). 

This environment defines a “global object”.

<div style="border: 1px solid; margin: 20px; padding: 20px; text-align: center;">
<p><strong>When this environment is a Web server <br>(and this is the case for all examples we have seen in this course),</strong><br><span style="color: #ff0000;"><strong>this global object is named <span style="font-family: 'courier new', courier;">window</span>.</strong></span></p>
<p><strong>The “global variables” defined with the keyword <span style="font-family: 'courier new', courier;">var</span> are properties of this <span style="font-family: 'courier new', courier;">window</span> object, <br>and we can say the same of predefined functions like prompt, alert, etc.</strong></p>
<p><strong>However, at the top level of programs and functions, <br><span style="font-family: 'courier new', courier;">let</span>, unlike <span style="font-family: 'courier new', courier;">var</span>, does not create a property on the global <span style="font-family: 'courier new', courier;">window</span> object.</strong></p>
<p><span style="color: #0000ff;"><strong>TIP: </strong>if you have global variables/objects declared with <span style="font-family: 'courier new', courier;">let</span>,<br>just declare them with <span style="font-family: 'courier new', courier;">var <span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">instead</span></span>, and you will be able to inspect them <br>easily from the devtool console. <br>You can switch back to using <span style="font-family: 'courier new', courier;">let</span>, later.</span></p>
</div>

Let's see some examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">1</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">a</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">1</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> window</span><span class="pun">[</span><span class="str">'a'</span><span class="pun">];</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">1</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">&gt;&nbsp;</span><strong>let z = 1;</strong> // LET DOES NOT DEFINE properties of the window object</li>
<li class="L0"><span color="#006666" style="color: #006666;">undefined</span></li>
<li class="L0"><span color="#006666" style="color: #006666;">&gt; <strong>window.z</strong></span></li>
<li class="L0"><strong><span color="#006666" style="color: #006666;">undefined</span></strong></li>
</ol></div>

`a` and `window.a` are the same variable.

`navigator` and `window.navigator` are the same, `document` and `window.document` are the same thing.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> document </span><span class="pun">===</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">document</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">true</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> navigator </span><span class="pun">===</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">navigator</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">true</span></li>
</ol></div>

Predefined functions are methods from the global object window:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> parseInt</span><span class="pun">(</span><span class="str">'10 little children'</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">10</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">parseInt</span><span class="pun">(</span><span class="str">'10 little children'</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">10</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> alert </span><span class="pun">===</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">alert</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">true</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> prompt </span><span class="pun">===</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">prompt</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">true</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> window</span><span class="pun">.</span><span class="pln">addEventListener&nbsp;</span><span class="pun">===</span><span class="pln"> addEventListener</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">true</span></li>
</ol></div>


#### Notes for 5.2.3 The "global" window object

+ `window` object
  + JS executed by an environment
    + usually a Web browser
    + some HTTP Web servers using JS for coding the servicer side of Web sites of applications
  + environment as 'global object'
    + Web server: global object named `window`
    + global variables defined w/ keyword `var`: properties of the `window` object, e.g., `var a = 1;` $\to$ `a === window.a` the same variable
    + predefined functions as the methods of the `window` object, including `prompt`, `alert`, etc.
    + global variable created w/ keyword `let`: not part of the `window` object
    + top-level of programs and functions: not part of the `window` object
  + best practice: global variables declared w/ `let`
    + declared the w/ `var` instead to inspect from the devtool console
    + switching back to using `let`, later
  + predefined objects: `navigator === window.navigator` & `document === window.document`
  + predefined functions and methods:
    + functions: `parseInt('10 little children'); // 10` & `window.parseInt('10 little children'); // 10`
    + methods: `alert === window.alert;  prompt === window.prompt`

+ Example: global variables declared w/ `var` and 'let`
  + declare global variable w/ `var`: `var a = 1;`
  + verify the global variable `a`: `a;` $\to$ 1, `window.a;` $\to$ 1, `window['a'];` $\to$ 1
  + declare global variable w/ `'et`: `let z = 1;`
  + verify the global variable `z`: `z;` $\to$ 1; `window.z;` $\to$ undefined 


### 5.2.4 Built-in JS class: `Object`

#### Live coding video: predefined class - Object

<a href="https://edx-video.net/W3CJSIXX2016-V004600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/7zkx28y9)

__Source code shown in the above video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/EXmONY?editors=0012)

[Local Demo](src/js/05b-example02.js)


The father of all objects: `Object`. All objects will inherit the properties and methods from the special class named `Object`.

These two lines are equivalent:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> o </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{}; // creation of an empty object</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> o </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Object</span><span class="pun">(); // same thing as in line 1</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
</ol></div>


#### The `toString` method

__The `toString` method inherited from `Object` by all objects__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> o</span><span class="pun">.</span><span class="pln">toString</span><span class="pun">();</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="str">"[object Object]"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> o</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"Michel"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> o</span><span class="pun">.</span><span class="pln">toString</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="str">"[object Object]"</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">];</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">toString</span><span class="pun">();</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="str">"1,2,3"</span></li>
</ol></div>

`toString()` in JavaScript is rather similar to the `Object.toString()` method we find in the Java programming language: __when we try to "display" an object, it is transformed into a string by calling `toString()` implicitly.__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> alert</span><span class="pun">(</span><strong><span class="pln">t</span></strong><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> alert</span><span class="pun">(</span><strong><span class="pln">t</span><span class="pun">.</span><span class="pln">toString</span></strong><span class="pun"><strong>()</strong>);</span><span class="pln"> </span><strong><span class="com">// same as previous line of code</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="str">"An object into a string : "</span><span class="pln"> </span><strong><span class="pun">+</span><span class="pln"> t </span></strong><span class="com">// same as <strong>t.toString() </strong></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">"The object as a String : 1, 2, 3"</span></li>
</ol></div>

Line 5: using the + operator with a string as the left argument will force the other arguments to convert to string by implicitly calling their toString() method.


#### The `valueOf` method

__The `valueOf` method inherited from `Object` by all objects__

The `ValueOf` method returns the value of an object:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> t </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">valueOf</span><span class="pun">()</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> t</span><span class="pun">.</span><span class="pln">toString</span><span class="pun">();</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="str">"1,2,3"</span></li>
</ol></div>


#### Notes for 5.2.4 Built-in JS class: Object

+ `Object` class
  + father of all objects
  + all objects inherit the properties and methods from the special class
  + `var o = {};` equivalent to `var o = new Object();`

+ The `toString()` method
  + inherited from `Object` by all objects
  + transformed into a string by calling `toString()` implicitly
  + using `+` operator to concantate string will force the other arguments to convert to string by implicitly calling `toString()` method
  + example:
    + declare object: `var o = {}; o.toString(); // "[object Object]`
    + set property value: `o.name = 'Michel'; o.toString(); // "[object Object]"`
    + declare numerical object: `var t = [1, 2, 3]; t.toString(); // "1,2,3"`
    + predefined function: `alert(t); alert(t.toString()); // display '1,2,3' on popup window`
    + concatate string: `"An object into a string: " + t; // "An object into a string: 1,2,3"`

+ The `valueOf()` method
  + return the value of an object
  + inherited from `Object` by all objects
  + example: `var t = [1, 2, 3]; t.valueOf(); // [1, 2, 3]`, `t.toString(); // "1,2,3"`

+ [`toString()` method in MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)
  + syntax: `obj.toString()`
  + docstring:
    + Every object w/ a `toString()` method that automatically called when the object is to be represented as a text value or when an objkject is referred to be in manner in which a string is expected
    + by default, inherited by every object descent from `Object`
  + parameter
    + `radix` (option): $2 \le \text{ radix } \le 36$
  + return:  a string representing the object

+ [`valueOf()` method in MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)
  + syntax: `obj.value()`
  + docstring:
    + convert an object to a primitive value
    + rarely invoke by user
    + automatically invoke by JS when encountering an object where a primitive value is expected
    + by default, inherited by every object descended from `Object`
  + return: the primitive value of the specified object


### 5.2.5 Built-in JS class: Array

#### Live coding video: predefined object - Array

<a href="https://edx-video.net/W3CJSIXX2016-V004700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/ar477arv)

__Source code from the above video__

[CodePen Demo](https://codepen.io/w3devcampus/pen/XgRyar?editors=0012)

[Local Demo](src/js/05b-example03.js)

The `Array` class can be used for creating arrays (however, we recommend that you use the other methods presented instead):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Array</span><span class="pun">();</span></strong><span class="pln"> </span><span class="com">// <strong>same as a = []; use this instead!</strong></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Array</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> b</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
</ol></div>

Attention: if only one element, this corresponds to the initial size of the array.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> myArray </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Array</span><span class="pun">(</span><span class="lit">3</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> myArray</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="kwd">undefined</span><span class="pln"> </span><span class="pun">×</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
</ol></div>


#### Arrays as objects

Arrays are objects, but they are “special” objects

+ Their property names are numerical indexes that start from 0
+ They have a special `length` property that represents their length/number of elements
+ They have other built-in properties in addition to the ones inherited from Object (`toString`, `valueOf`)

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[],</span><span class="pln"> o </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{};</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> </span><span class="com">// a is an array</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">0</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> o</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> </span><span class="com">// o is a simple literal object</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
</ol></div>

Some horrible things we can do with arrays (TO AVOID!):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> a</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">"object"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="lit">3</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="lit">3</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">length</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">3</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="com">// Now let’s add a name property to the array. Yes, we can do that!</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">name </span><span class="pun">=</span><span class="pln"> </span><span class="str">"I'm an array named a!"</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="str">"I'm an array named a!"</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="lit">3</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> name</span><span class="pun">:</span><span class="pln"> </span><span class="str">"I'm an array named a!"</span><span class="pun">]</span></strong></li>
</ol></div>

<p style="border: 1px solid; padding: 20px; text-align: center;"><span style="color: #ff0000;"><strong>With arrays, only properties with a numerical index are taken into account by the <span style="font-family: 'courier new', courier;">length</span> property!</strong></span></p>

#### Reducing and increasing the size of an array

__The `length` property can be modified: reducing or increasing the size of an array__

If you give to the `length` property a value bigger than the number of elements in an array, it adds undefined elements to it:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">length </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">5</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pln"> </span><span class="pun">×</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
</ol></div>

If you give to the length property a value less than the array’s number of elements, it reduces the size of the array:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">length </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">2</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">]</span></li>
</ol></div>


#### Notes for 5.2.5 Built-in JS class: Array

+ `Array` class
  + used for creating arrays
  + recommendation: used '[' and ']' to create arrays
  + a global object that is used in the construction of arrays
  + constructor
    + list of elements: `new Array(element0, element1[, ...[, elementN]])`
    + empty array w/ reserved space: `new Array(arrayLength)`
  + arrays as "special" objects
    + property names: numerical indexes starting from 0
    + `length` property: representing the length/number of elements
    + other built-in properties besides the inherited ones from `Object`, including, `sort()`, `join()`, `slide()`, `splice()`,`push()` and `pop()`
  + array length and elements:
    + length of array bigger that the number of elements: add undefined elements to it
    + length of array less than the number of elements: truncate the array to comply the length

+ Example: constructing array and size
  + constructor w/ elements: `var a = new Array(); // same as a = [];` and `var b = new Array(1, 2, 3); // [1, 2, 3]`
  + constructor w/ size: `var myArray = new Array(3); // [undefined x 3]`
  + `length` property: `var a = []; o = {};`, `a.length;  // 0 - an array` and `o.length; // undefined - a simple object literal`

+ Example: bad practices
  + declaration and some info: `var a = [1, 2];`, `typeof a; // "object"`, `a.push(3); // 3`, `a; // [1, 2, 3]` and `a.length; //3`
  + add a name propert into array: `a.name = "I'm an array named a!";`, `a.length; // 3` and `a; // [1, 2, 3, name: "I'm an array named a!"]`

+ Example: reducing and increasing the size of an array
  + declare array and assign length: `var a = [1, 2]; a.length = 5;`
  + increased array: `a; // [1, 2, undefined x 3]`
  + declare array and assign length: `var a = [1, 2, 3, 4]; a.length = 2;`
  + reduced array: `a; // [1, 2]`


+ `Array()` constructor
  + syntax:
    + `[element0, element1, ..., elementN]`
    + `new Array(element0, element1[, ...[, elementN]])`
    + `new Array(arrayLength)`
  + docstring: used to create `Array` objects
  + parameters
    + `elementN`:
      + initialized w/ the given elements, except in the case where a single argument is passed to the `Array` constructor
      + applied to JS arrays created w/ the `Array` constructor, not array literals created w/ the bracket syntax
    + `arrayLength`
      + the only argument
      + an interger btw 0 and $2^{32} - 1$ (inclusive)
      + return a new JS array w/ its `length` property set to the number
      + an array of `arrayLength` empty slots


### 5.2.6 The most useful methods of the class Array

The most useful methods you can use on arrays are: `sort()`, `join()`, `slice()`, `splice()`, `push()` and `pop()`

+ `sort`: sort the elements in the array. Either alphabetically if they are strings, or in ascending order if they are numbers. There is also a way to sort the elements using other criteria, which is explained a bit further on in the course. With a call to `var b = a.sort()`, a is also sorted. The sort method sorts the array + returns it.
+ `join`: adds a string between each element and returns the result as a string
+ `slice`: returns a sub-array without modifying the original array
+ `splice`: modifies the array, it removes “a slice” and it also adds new elements
+ `push`: appends an element at the end of the array and returns the new length
+ `pop`: removes the last element and returns it


#### Typical uses of `push`, `pop`, `sort`, `join`

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">'test'</span><span class="pun">];</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">push</span><span class="pun">(</span><span class="str">'new'</span><span class="pun">)</span><span class="pln"> </span><span class="com">// appends at the end and returns the new length</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">6</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">,</span><span class="pln"> </span><span class="str">"new"</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">pop</span><span class="pun">();</span><span class="pln"> </span><span class="com">// removes the last element and returns it</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="str">"new"</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">sort</span><span class="pun">();</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> b</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// a is also sorted. The sort method sorts the array + returns it</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">join</span><span class="pun">(</span><span class="str">' and '</span><span class="pun">);</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="str">"1 and 3 and 5 and 7 and test"</span></li>
<li class="L9" style="margin-bottom: 0px;"></li>
</ol></div>


#### The `slide()` method

__The `slice()` method returns a sub-array without modifying the original array__

The `slice()` method returns a shallow copy of a portion of an array into a new array object selected from begin to end (__end not included__). The original array will not be modified.

Possible syntaxes:

+ `arr.slice()`
+ `arr.slice(begin)`
+ `arr.slice(begin, end) // ELEMENT AT INDEX=end will not be included in the slice!`

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">slice</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span><span class="pln"> </span><span class="com">// elements of indexes = 1 and 2</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">]</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">slice</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">);</span><span class="pln"> </span><span class="com">// element of index = 0</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">slice</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">);</span><span class="pln"> </span><span class="com">// elements o indexes = 0 and 1</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">]</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">// a is unchanged by calls to a.slice(...)</span></li>
</ol></div>


#### The `slide()` method

__The `splice()` method modifies the array: it removes “a slice” and also adds new elements__

The first two parameters are start and the number of elements to delete, the other parameters are the elements to add to the array to replace the slice that will be removed.

Possible syntaxes:

+ `array.splice(start)`
+ `array.splice(start, deleteCount)`
+ `array.splice(start, deleteCount, item1, item2, ...)`

Parameters:

+ `start`: index at which to start changing the array (with origin 0)
+ `deleteCount`: An integer indicating the number of old array elements to remove.
+ `item1, item2, ...`: these are optional. They are the elements to add to the array, beginning at the `start` index. If you don't specify any elements, `splice()` will only remove elements from the array.

Examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">101</span><span class="pun">,</span><span class="pln"> </span><span class="lit">102</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> </span><span class="lit">5</span><span class="pun">]</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">101</span><span class="pun">,</span><span class="pln"> </span><span class="lit">102</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">splice</span><span class="pun">(</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">3</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">100</span><span class="pun">,</span><span class="pln"> </span><span class="lit">101</span><span class="pun">,</span><span class="pln"> </span><span class="lit">102</span><span class="pun">]</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">[</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">7</span><span class="pun">,</span><span class="pln"> </span><span class="str">"test"</span><span class="pun">]</span></li>
</ol></div>







