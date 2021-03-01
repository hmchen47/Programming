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








