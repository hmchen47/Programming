# Module 5: Working with forms


## 5.2 Built-in JavaScript objects


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

<div><ol>
<li value="1">// Defining two variables</li>
<li>var x = 2; // the variable x contains the primitive datum 2</li>
<li>var y = { a: 2 } // The variable y references the object {a: 2}</li>
<li> </li>
<li>// "Copying" two variables</li>
<li>var x2 = x;</li>
<li>var y2 = y;</li>
<li>var y3 = y;</li>
<li> </li>
<li>// Modifying copied variables</li>
<li>x2 = 3;</li>
<li>y2 = { a: 3 };</li>
<li> </li>
<li>// Check</li>
<li>x; // 2 &lt;- x is not modified because it contains a primitive value</li>
<li>y; // { a: 2 } &lt;- y is not modified because y2 does not point to same object</li>
<li></li>
<li>y3.a = 4;</li>
<li>y; // { a: 4 } &lt;- The object referenced by "y" and "y3" is modified</li>
</ol></div>

Of course, these rules also apply to the properties of objects.

Example:

<div><ol>
<li value="1">var driver = {</li>
<li>&nbsp; &nbsp; name: 'Jean'</li>
<li>};</li>
<li> </li>
<li>var car = {</li>
<li>&nbsp; &nbsp; color: 'red',</li>
<li>&nbsp; &nbsp; driver: driver</li>
<li>};</li>
<li></li>
<li>driver.name = 'Albert';</li>
<li>car.driver.name; // 'Albert'</li>
</ol></div>

JavaScript is a "pass by value" language, unlike some other languages, which are "pass by reference" languages. This means that when you pass a variable to a function as argument, the value of the variable is copied into the argument.

Example:

<div><ol>
<li value="1">var x = 2;</li>
<li> </li>
<li>function sum(a, b) {</li>
<li>&nbsp; &nbsp; a = a + b;</li>
<li>&nbsp; &nbsp; return a;</li>
<li>}</li>
<li> </li>
<li>sum(x, 3); // returns 5</li>
<li>x; // 2 &lt;- but x equals 2</li>
</ol></div>

When working with objects, the reference of the object is copied into the argument. That means you can modify the referenced object. But if you change the reference (for example by assigning a new object), the original variable (which now points to another object) will not be modified.

Example 1:

<div><ol>
<li value="1">var obj = { x: 2 }</li>
<li> </li>
<li>function add(a, b) {</li>
<li> a.x += b;</li>
<li>}</li>
<li> </li>
<li>add(obj, 3);</li>
<li>obj.x; // 5 &lt;- The referenced object is modified</li>
</ol></div>

Example 2:

<div><ol>
<li value="1">var obj = { x: 2 };</li>
<li> </li>
<li>function addAndSet(a, b) {</li>
<li>&nbsp; &nbsp; var addition = a.x + b;</li>
<li>&nbsp; &nbsp; a = { x: addition };</li>
<li>};</li>
<li> </li>
<li>addAndSet(obj, 3);</li>
<li>obj.x; /* 2 &lt;- The referenced object is not modified</li>
<li>because at the end of the function the variable "obj"</li>
<li> and the variable "a" are not referencing the same object.*/</li>
</ol></div>

Other examples:

<div><ol>
<li value="1">&gt; var originalObject = {name:'Michel'};</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; var copy = originalObject;</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; copy.name;</li>
<li>"Michel"</li>
<li>&nbsp;</li>
<li>&gt; copy.name = 'Dark Vador';</li>
<li>"Dark Vador"</li>
<li>&nbsp;</li>
<li>&gt; originalObject.name</li>
<li>"Dark Vador"</li>
<li>&nbsp;</li>
<li>// They are the same. originalObject and copy are two "references" of the same object in memory</li>
<li>// If we change the name, we change the value in memory, but copy and originalObject "point to" the</li>
<li>// same place, to the same object. They are just "pointers" or "reference" to the same object</li>
</ol></div>


#### Notes for 5.2.1 References and objects

+ References and objects
  + pointer variable: containing the actual address of an object within the variable
  + reference variable: an alias to a variable
  + when modifying a reference variable, the original variable is modified $\gets$ two variables w/ the same object
  + types of values of a variable
    + primitive value (number, string, or boolean):
      + the variable containing the value directly
      + example: `let x = 10;`, `let name = 'Michel'`
    + object:
      + containing the memory address of the object
      + pointing to an object or reference of this object
      + accessing the variable automatically resolving the reference
      + the value of the variable = the referenced object
  + arguments of function
    + primitive values
      + a "pass by value" language
      + passing a variable to a function as argument, the value of the variable copied into the argument
    + objects
      + reference of object copied into the argument
      + able to modify the reference object
      + change of reference: the origin variable (now point to another object) not modified
  
+ Example: primitive and object
  + declare two variables: `var x = 2; var y = {a: 2};`
  + copy two variables: `var x2 = x; var y2 = y; var y3 = y;`
  + modify copied variables: `x2 = 4; y2 = {a: 3}`
    + `x` not modified: primitive value
    + `y` not modified: `y` & `y2` pointing to different objects
  + modify value of property: `y3.a = 4;`
    + `y` and `y3`: both modified $\gets$ object reference changing to `{a: 2}`

+ Example: properties of objects
  + declare an object: `var driver = { name: 'Jean' }; var car = {color: 'red', driver: driver };`
  + modify drive name: `driver.name = 'Albert';`
  + car driver modified: `car.driver.name; // 'Albert';`

+ Example: function passed by value
  + declare a variable: `var x = 2;`
  + declare a function: `function sum(a, b) { a = a + b; return a; }`
  + call function `sum`: `sum(x, 3); // 5`
  + `a` modified within function `sum` but `x` remaining the same: `x; // 2`

+ Example: function argument as object
  + declare object: `var obj = {x: 2 };`
  + declare function: `function add(a, b) { a.x += b; }`
  + call function `add()`: `add(obj, 3);`
  + the reference object modified: `obj.x; // 5`
  + declare function: `function addAndSet(a, b) { var addition = a.x + b; a = {x: addition}; }`
  + call function `addAndSet()`: `addAndSet(obj, 3);`
  + reference object not modified (`obj` and `a` not pointing to the same object at the end of the function): `obj.x; // 2`

+ Example: modifying copied object to modify original object
  + original object: `var originalObject = { name: 'Michel' };`
  + copied object: `var copy = originalObject;`
  + verification: `copy.name; // 'Michel'`
  + modify copied object: `copy.name = 'Dark Vador';`
  + original object verification: `originalObject.name; // 'Dark Vador'`


### 5.2.2 Comparing two objects

Comparing two objects will only return true if they point to the same object (i.e., if they have the same reference).

Two objects of the same type, with the same property value, that look identical, will not be equal one to another if they don’t have the same reference (if they point to different places in memory).

<div><ol>
<li value="1">&gt; var originalObject = {name:'Michel'};</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; var copy = originalObject;</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; copy === originalObject</li>
<li>true</li>
<li>&nbsp;</li>
<li>&gt; var anotherObject = {name:'Michel'};</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; copy === anotherObject</li>
<li>false</li>
</ol></div>


#### Notes for 5.2.2 Comparing two objects

+ Object comparison
  + returning boolean value whether w/ the same reference (pointing to the same objects)
  + identical objects but unequal
    + returning `false` (`===` or `==`)
    + objects w/ same type, same property values
    + w/ different references
    + pointing to different places in memory
  
+ Example: comapring objects
  + declare objects: `var originalObject = { name: 'Michel' }; var copy = originalObject;`
  + compare original and copied objects: `copy === originalCopy; // true`
  + declare another object: `var anotherObject = { name: 'Michel' };`
  + compare copied and another objects: `copy === anotherObject; // false`



### 5.2.3 The "global" window object

It is time to tell you the truth: the JavaScript code is executed by an “environment" (usually a Web browser, but there are some HTTP Web servers that use JavaScript for coding the server side of Web sites of applications, such as the NodeJS HTTP server). 

This environment defines a “global object”.

<div style="border: 1px solid; margin: 20px; padding: 20px; text-align: center;">
<p><strong>When this environment is a Web server <br>(and this is the case for all examples we have seen in this course),</strong><br><span style="color: #ff0000;"><strong>this global object is named <span style="font-family: 'courier new', courier;">window.</strong></span></p>
<p><strong>The “global variables” defined with the keyword <span style="font-family: 'courier new', courier;">var</span> are properties of this <span style="font-family: 'courier new', courier;">window</span> object, <br>and we can say the same of predefined functions like prompt, alert, etc.</strong></p>
<p><strong>However, at the top level of programs and functions, <br><span style="font-family: 'courier new', courier;">let</span>, unlike <span style="font-family: 'courier new', courier;">var</span>, does not create a property on the global <span style="font-family: 'courier new', courier;">window</span> object.</strong></p>
<p><span style="color: #0000ff;"><strong>TIP: </strong>if you have global variables/objects declared with <span style="font-family: 'courier new', courier;">let</span>,<br>just declare them with <span style="font-family: 'courier new', courier;">var <span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">instead</span></span>, and you will be able to inspect them <br>easily from the devtool console. <br>You can switch back to using <span style="font-family: 'courier new', courier;">let</span>, later.</span></p>
</div>

Let's see some examples:

<div><ol>
<li value="1">&gt; var a = 1;</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>1</li>
<li>&nbsp;</li>
<li>&gt; window.a;</li>
<li>1</li>
<li>&nbsp;</li>
<li>&gt; window['a'];</li>
<li>1</li>
<li>&gt;&nbsp;<strong>let z = 1;</strong> // LET DOES NOT DEFINE properties of the window object</li>
<li><span color="#006666" style="color: #006666;">undefined</li>
<li><span color="#006666" style="color: #006666;">&gt; <strong>window.z</strong></li>
<li><strong><span color="#006666" style="color: #006666;">undefined</strong></li>
</ol></div>

`a` and `window.a` are the same variable.

`navigator` and `window.navigator` are the same, `document` and `window.document` are the same thing.

<div><ol>
<li value="1">&gt; document === window.document</li>
<li>true</li>
<li>&nbsp;</li>
<li>&gt; navigator === window.navigator</li>
<li>true</li>
</ol></div>

Predefined functions are methods from the global object window:

<div><ol>
<li value="1">&gt; parseInt('10 little children');</li>
<li>10</li>
<li>&nbsp;</li>
<li>&gt; window.parseInt('10 little children');</li>
<li>10</li>
<li>&nbsp;</li>
<li>&gt; alert === window.alert</li>
<li>true</li>
<li>&nbsp;</li>
<li>&gt; prompt === window.prompt</li>
<li>true</li>
<li>&nbsp;</li>
<li>&gt; window.addEventListener&nbsp;=== addEventListener</li>
<li>true</li>
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
    + declared w/ `var` instead to inspect from the devtool console
    + switching back to use `let`, later
  + predefined objects: `navigator === window.navigator` & `document === window.document`
  + predefined functions and methods:
    + functions: `parseInt('10 little children'); // 10` & `window.parseInt('10 little children'); // 10`
    + methods: `alert === window.alert;  prompt === window.prompt`

+ Example: global variables declared w/ `var` and `let`
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

<div><ol>
<li value="1">&gt; var o = {}; // creation of an empty object</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; var o = new Object(); // same thing as in line 1</li>
<li>undefined</li>
</ol></div>


#### The `toString` method

__The `toString` method inherited from `Object` by all objects__

<div><ol>
<li value="1">&gt; o.toString();</li>
<li>"[object Object]"</li>
<li>&nbsp;</li>
<li>&gt; o.name = 'Michel';</li>
<li>"Michel"</li>
<li>&nbsp;</li>
<li>&gt; o.toString();</li>
<li>"[object Object]"</li>
<li>&nbsp;</li>
<li>&gt; var t = [1, 2, 3];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; t.toString();</li>
<li>"1,2,3"</li>
</ol></div>

`toString()` in JavaScript is rather similar to the `Object.toString()` method we find in the Java programming language: __when we try to "display" an object, it is transformed into a string by calling `toString()` implicitly.__

<div><ol>
<li value="1">&gt; alert(<strong>t</strong>);</li>
<li>&nbsp;</li>
<li>&gt; alert(<strong>t.toString</strong><strong>()</strong>); <strong>// same as previous line of code</strong></li>
<li>&nbsp;</li>
<li>&gt; "An object into a string : " <strong>+ t </strong>// same as <strong>t.toString() </strong></li>
<li> "The object as a String : 1, 2, 3"</li>
</ol></div>

Line 5: using the + operator with a string as the left argument will force the other arguments to convert to string by implicitly calling their toString() method.


#### The `valueOf` method

__The `valueOf` method inherited from `Object` by all objects__

The `ValueOf` method returns the value of an object:

<div><ol>
<li value="1">&gt; var t = [1, 2, 3];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; t.valueOf()</li>
<li>[1, 2, 3]</li>
<li>&nbsp;</li>
<li>&gt; t.toString();</li>
<li>"1,2,3"</li>
</ol></div>


#### Notes for 5.2.4 Built-in JS class: Object

+ `Object` class
  + father of all objects
  + all objects inherit the properties and methods from the special class
  + `var o = {};` equivalent to `var o = new Object();`

+ The `toString()` method
  + inherited from `Object` by all objects
  + transformed into a string by calling `toString()` implicitly when trying to display an object
  + using `+` operator to concantate string will force the other arguments to convert to string by implicitly calling `toString()` method

+ Example: `toString`method of an object
  + declare object: `var o = {}; o.toString(); // "[object Object]`
  + set property value: `o.name = 'Michel'; o.toString(); // "[object Object]"`
  + declare numerical object: `var t = [1, 2, 3]; t.toString(); // "1,2,3"`
  + predefined function: `alert(t); alert(t.toString()); // display '1,2,3' on popup window`
  + concatate string: `"An object into a string: " + t; // "An object into a string: 1,2,3"`

+ The `valueOf()` method
  + return the value of an object
  + inherited from `Object` by all objects
  + example: `var t = [1, 2, 3]; t.valueOf(); // [1, 2, 3]`, `t.toString(); // "1,2,3"`

+ [`toString()` method: specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)

+ [`valueOf()` method: specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)


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

<div><ol>
<li value="1">&gt; <strong>var a = new Array();</strong> // <strong>same as a = []; use this instead!</strong></li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; <strong>var b = new Array(1, 2, 3);</strong></li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; b;</li>
<li>[1, 2, 3]</li>
</ol></div>

Attention: if only one element, this corresponds to the initial size of the array.

<div><ol>
<li value="1">&gt; var myArray = new Array(3);</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; myArray;</li>
<li>[undefined × 3]</li>
</ol></div>


#### Arrays as objects

Arrays are objects, but they are “special” objects

+ Their property names are numerical indexes that start from 0
+ They have a special `length` property that represents their length/number of elements
+ They have other built-in properties in addition to the ones inherited from Object (`toString`, `valueOf`)

<div><ol>
<li value="1">&gt; var a = [], o = {};</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; a.length; // a is an array</li>
<li>0</li>
<li>&nbsp;</li>
<li>&gt; o.length; // o is a simple literal object</li>
<li>undefined</li>
</ol></div>

Some horrible things we can do with arrays (TO AVOID!):

<div><ol>
<li value="1">&gt; var a = [1, 2];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; typeof a</li>
<li>"object"</li>
<li>&nbsp;</li>
<li>&gt; a.push(3);</li>
<li>3</li>
<li>&nbsp;</li>
<li>&gt; a</li>
<li>[1, 2, 3]</li>
<li>&nbsp;</li>
<li>&gt; a.length</li>
<li>3</li>
<li>&nbsp;</li>
<li><strong>// Now let’s add a name property to the array. Yes, we can do that!</strong></li>
<li>&nbsp;</li>
<li><strong>&gt; a.name = "I'm an array named a!";</strong></li>
<li><strong>"I'm an array named a!"</strong></li>
<li><strong>&nbsp;</strong></li>
<li><strong>&gt; a.length;</strong></li>
<li><strong>3</strong></li>
<li><strong>&nbsp;</strong></li>
<li><strong>&gt; a;</strong></li>
<li><strong>[1, 2, 3, name: "I'm an array named a!"]</strong></li>
</ol></div>

<p style="border: 1px solid; padding: 20px; text-align: center;"><span style="color: #ff0000;"><strong>With arrays, only properties with a numerical index are taken into account by the <span style="font-family: 'courier new', courier;">length property!</strong></p>

#### Reducing and increasing the size of an array

__The `length` property can be modified: reducing or increasing the size of an array__

If you give to the `length` property a value bigger than the number of elements in an array, it adds undefined elements to it:

<div><ol>
<li value="1">&gt; var a = [1, 2];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; a.length = 5;</li>
<li>5</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[1, 2, undefined × 3]</li>
</ol></div>

If you give to the length property a value less than the array’s number of elements, it reduces the size of the array:

<div><ol>
<li value="1">&gt; var a = [1, 2, 3];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; a.length = 2;</li>
<li>2</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[1, 2]</li>
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
    + other built-in properties besides the inherited ones from `Object`, including, `sort()`, `join()`, `slice()`, `splice()`,`push()` and `pop()`
  + array length and elements:
    + length of array bigger than the number of elements: add undefined elements to it
    + length of array less than the number of elements: truncate the array to comply the length

+ Example: constructing array and size
  + constructor w/ elements: `var a = new Array(); // same as a = [];` and `var b = new Array(1, 2, 3); // [1, 2, 3]`
  + constructor w/ size: `var myArray = new Array(3); // [undefined x 3]`
  + `length` property: `var a = []; o = {};`, `a.length;  // 0 - an array` and `o.length; // undefined - a simple object literal`

+ Example: bad practices
  + declaration and some info: `var a = [1, 2];`, `typeof a; // "object"`, `a.push(3); // 3`, `a; // [1, 2, 3]` and `a.length; //3`
  + add a name property into array: `a.name = "I'm an array named a!";`, `a.length; // 3` and `a; // [1, 2, 3, name: "I'm an array named a!"]`

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

<div><ol>
<li value="1">&gt; var a = [3, 5, 1, 7, 'test'];</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; a.push('new') // appends at the end and returns the new length</li>
<li>6</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[3, 5, 1, 7, "test", "new"]</li>
<li>&nbsp;</li>
<li>&gt; a.pop(); // removes the last element and returns it</li>
<li>"new"</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[3, 5, 1, 7, "test"]</li>
<li>&nbsp;</li>
<li>&gt; var b = a.sort();</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; b;</li>
<li>[1, 3, 5, 7, "test"]</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[1, 3, 5, 7, "test"]</li>
<li>&nbsp;</li>
<li>// a is also sorted. The sort method sorts the array + returns it</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; a.join(' and ');</li>
<li>"1 and 3 and 5 and 7 and test"</li>
<li></li>
</ol></div>


#### The `slice()` method

__The `slice()` method returns a sub-array without modifying the original array__

The `slice()` method returns a shallow copy of a portion of an array into a new array object selected from begin to end (__end not included__). The original array will not be modified.

Possible syntaxes:

+ `arr.slice()`
+ `arr.slice(begin)`
+ `arr.slice(begin, end) // ELEMENT AT INDEX=end will not be included in the slice!`

<div><ol>
<li value="1">&gt; a;</li>
<li>[1, 3, 5, 7, "test"]</li>
<li>&nbsp;</li>
<li>&gt; b = a.slice(1, 3); // elements of indexes = 1 and 2</li>
<li>[3, 5]</li>
<li>&nbsp;</li>
<li>&gt; b = a.slice(0, 1); // element of index = 0</li>
<li>[1]</li>
<li>&nbsp;</li>
<li>&gt; b = a.slice(0, 2); // elements o indexes = 0 and 1</li>
<li>[1, 3]</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[1, 3, 5, 7, "test"]</li>
<li>&nbsp;</li>
<li>// a is unchanged by calls to a.slice(...)</li>
</ol></div>


#### The `splide()` method

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

<div><ol>
<li value="1">&gt; a;</li>
<li>[1, 3, 5, 7, "test"]</li>
<li>&nbsp;</li>
<li>&gt; b = a.splice(1, 2, 100, 101, 102);</li>
<li>[3, 5]</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[1, 100, 101, 102, 7, "test"]</li>
<li>&nbsp;</li>
<li>&gt; a.splice(1, 3);</li>
<li>[100, 101, 102]</li>
<li>&nbsp;</li>
<li>&gt; a;</li>
<li>[1, 7, "test"]</li>
</ol></div>


#### Notes for 5.2.6 The most useful methods of the class Array

+ Useful methods of the class Array
  + `sort`:
    + sort elements in the array and return it
    + string elements: alphabetical
    + numeric elements: ascending
    + other criteria: usually a special function for objects
  + `join`: add a string btw each element and return the result as a string
  + `slice`:
    + return a sub-array w/o modifying the original way
    + possible syntaxes:
      + `arr.slice()`
      + `arr.slice(begin)`
      + `arr.slice(begin, end)`: element at index = end bot included in the slice
    + return a shallow copy of a portion of an array into a new array object selected from begin to end (excluding)
    + original array not modified
  + `splice`:
    + modify array by replacing a slice w/ new elements
    + possible syntaxes:
      + `arr.splice(start)`
      + `arr.splice(start, deleteCount)`
      + `arr.splice(start, deleteCount, item1, item2, ...)`
    + parameters
      + `start`: index at which to start changing the array (w/ origin 0)
      + `deleteCount`: an integer indicating the number of old array elements to remove
      + `item1, item2, ...` (optional):
        + present: elements to add to the array, beginning at the `start` index
        + ignore: only remove elements from the array
  + `push`: append an element at the end of the array and return the new length
  + `pop`: return an array by removing the last element

+ Example: use of `push`, `pop`, `sort` and `join`
  + declare object: `var a = [3, 5, 1, 7, 'test'];`
  + append an element w/ `push` method: `a.push('new'); // 6` and `a; // [3, 5, 1, 7, 'test', 'new']`
  + remove the last element w/ `pop` method: `var b = a.sort();`, `b; // [1, 3, 5, 7, "test"]` and `a; // [1, 3, 5, 7, "test"]`
  + concatenate element w/ a given string by `join` method: `a.join(' and '); // "1 and 3 and 5 and 7 and test"`

+ Example: `slice` method
  + declare object: `a = [1, 3, 5, 7, "test"];`
  + get a slice from array:
    + remove elements w/ indexes from 1 to 2: `var b = a.slice(1, 3); // [3, 5]`
    + remove element w/ index 1: `b = a.slice(0, 1); // [1]`
    + remove elements w/ indexes from 0 to 1: `b = a.slice(0, 2); // [1, 3]`
  + original array not modified: `a; // [1, 3, 5, 7, "test"]`

+ Example: `splice` method
  + declare object: `a; // [1, 3, 5, 7, "test"]`
  + replace elements: `b = splice(1, 2, 100, 101, 102); // [3, 5]`
  + original array modified: `a; // [1, 100, 101, 102, 7, "test"]`
  + remove elements: `a.splice(1, 3); // [101, 102, 103]`
  + original array modified: `a; // [1, 7, "test"]`

+ [The `Array.prototype.join()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
  + syntax: `arr.join([separator])`
  + docstring:
    + create and return a new substring by concatenating all of the element in an array (or an array-like object)
    + sparated by commas or a specified seperator string
    + no separator if only one element
  + parameters:
    + `separator` (optional):
      + specify a string to separate each pair of adjacent of the array
      + separator coverted to a sting if necessary
      + omitted: separated w/ a comma (",")
  + return:
    + a string w/ all array elements jointed
    + the empty string if `arr.length = 0`

+ [The `Array.prototype.slice()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)
  + syntax: `arr.slice()`, `arr.slice(start)`, and `arr.slice(start, end)`
  + docstring:
    + return a shallow copy of a portion of an array into a new array object selected from `start` to `end` (excluded)
    + original array not modified
  + parameters
    + `start` (optional)
      + zero-based index at which to start extraction
      + negative index: indicating an offset from the end of sequence, e.g., `slice(-2)` extracting the last two elements in the sequence
      + undefined: start from the index 0
      + greater than the index range of the sequence: return an empty array
    + `end` (optional)
      + zero-based index before which to end extraction
      + extract up to but not including `end`
      + negative index: indicating an offset from the end of the sequence, e.g., `slice(2, -1)` extracting the 3rd element through the second-to-last element in the sequence
      + omitted: extract through the end of the sequence (`arr.length`)
      + greater than the length of the sequence: extract through to the end of the sequence


### 5.2.7 Built-in JS class: `Number`

The `Number` class can be used to transform strings into numbers, but it is recommended that you use `parseInt` or `parseFloat` instead.

<div><ol>
<li value="1">&gt; var n = Number('3.1416');</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; n;</li>
<li>3.1416</li>
<li>&nbsp;</li>
<li>&gt; typeof n;</li>
<li>"number"</li>
<li>&nbsp;</li>
<li>&gt; var n = parseInt('3.1416'); // convert a string to an integer number</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; n;</li>
<li>3</li>
<li>&nbsp;</li>
<li>&gt; var n = parseFloat('3.1416'); // convert a string to a float number</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; n;</li>
<li>3.1416</li>
</ol></div>

`Number` has useful non-modifiable properties (constants): `MAX_VALUE` and `MIN_VALUE`:

<div><ol>
<li value="1">&gt; Number.MAX_VALUE;</li>
<li>1.7976931348623157e+308</li>
<li>&nbsp;</li>
<li>&gt; Number.MIN_VALUE;</li>
<li>5e-324</li>
</ol></div>


#### Methods useful for converting numbers: `toFixed()`, `toExponential()`, `toString()`

+ `toFixed`: sets the number of digits for the decimal part of a number. There is also another method, named `toPrecision`, that has a very close behavior, and can also return numbers in scientific notation. 
+ `toExponential`: force a number to use a scientific notation. For example `var a=1000; a.toExponential(); console.log(a);` will give `1e+3`
+ `toString`: converts a number to its string representation. `let n = 10; n.toString()` converts by default to base 10 and will return "10", but you can also pass the base you want to convert to as a unique parameter, `n.toString(2)` will convert the number 10 to base 2 and display "1010";

<div><ol>
<li value="1">&gt; var n = 123.456;</li>
<li>123.456</li>
<li>&nbsp;</li>
<li>&gt; n.toFixed(1); // sets the number of digits for the decimal part of the number</li>
<li>"123.5"</li>
<li>&nbsp;</li>
<li>&gt; n = new Number(123.456); // same as n = 123.456</li>
<li>Number {[[PrimitiveValue]]: 123.456} // well, not exactly, but when you use n, it is equivalent</li>
<li>&nbsp;</li>
<li>&gt; n.toFixed(1);</li>
<li>"123.5"</li>
<li>&nbsp;</li>
<li>&gt; n.toExponential();</li>
<li>"1.23456e+2"</li>
<li>&nbsp;</li>
<li>&nbsp;</li>
<li>&gt; var n = 255;</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; n.toString();</li>
<li>"255"</li>
<li>&nbsp;</li>
<li>&gt; n.toString(10);</li>
<li>"255"</li>
<li>&nbsp;</li>
<li>&gt; n.toString(16);</li>
<li>"ff"</li>
<li>&nbsp;</li>
<li>&gt; (3).toString(2);</li>
<li>"11"</li>
<li>&nbsp;</li>
<li>&gt; (3).toString(10);</li>
<li>"3"</li>
</ol></div>


#### Notes for 5.2.7 Built-in JS class: `Number`

+ `Number` class
  + used to transform strings into numbers
  + recommendation: using `parseInt` or `parseFloat` instead
  + constructing w/ `Number` class
    + `new` keyword, e.g., `var n = Number('3.1416'); n; // 3.1415`
    + type of variable: `typeof n; // "number"`
  + convert a string to an integer number: `var n = parseInt('3.1416'); n; // 3`
  + convert a string to a float number: `var n = parseFloat('3.1416'); n; // 3.1416`
  + `MAX_VALUE` and `MIN_VALUE`: useful non-modifiable properties (constants)
    + `Number.MAX_VALUE`: 1.7976931348623157e+308
    + `Number.MIN_VALUE`: 5e-324

+ Useful methods for converting numbers
  + `toFixed()`: set the number of digits for the deccimal part of a number
  + `toPrecision()`: return numbers in scientific notation
  + `toExponential()`:
    + a number to use a scientific notation
    + example: `var a = 1000; a.toExponential(); console.log(a); // le+3`
  + `toString([b])`:
    + convert a number to its string representation
    + `b`: base, default base 10
    + example: `let n = 10; n.toString(); // 10` & `n.toString(2); // 1010`

+ Example: `toFixed()`, `toExponential()`, and `toString()`
  + declare floating number: `var n = 123.456`
  + set the number of digits for the decimal part of the number: `n.toFixed(1); // 123.5`
  + create number w/ `Number` class: `n = new Number(123.456); // Number {[[PrimitiveValue]]: 123.456}`
  + set decimal digits and rounded the result: `n.toFixed(1); // "123.5"`
  + get scientific notation: `n.toExponential();  // "1.23456e+2`
  + declare integer: `var n = 255;`
  + convert integer to string: `n.toString(); // "255"`
  + convert integer to string w/ different bases: `n.toString(10); // "255"`, `n.toString(16); // "ff"`
  + convert integer to string: `(3).toString(2); // "11"`, `(3).toString(10); // "3"`

+ [`Number()` constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number)
  + syntax: `new Number(value)`
  + docstring: create a `Number` object
  + parameter
    + `value`: the numeric value of the object being created

+ [`Number.prototype.toFixed()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)
  + syntax: `numObj.toFixed([digits])`
  + docstring: format a number using fixed-point notation
  + parametre
    + `digits` (optional):
      + the number of digits to apprear after the decimal point
      + range: [0, 20]
      + default: 0
  + return: a string representing the given number using fixed-point notation

+ [`Number.prototype.toExponential()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toExponential)
  + syntax: `numObj.toExponential([fractionDigits])`
  + docstring: return a string representing the `Number` object in exponential notation
  + parameter
    + `fractionDigits` (optional):
      + specify the number of digits after the decimal point
      + default: as many digits as necessary to specify the number
  + return: a string representing the given `Number` object in exponential notation w/ one digit before the decimal point, rounded to `fractionDigits` digits after the decimal point

+ [`Number.prototype.toString()` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString)
  + syntax: `numObj.toString([radix])`
  + docstring: return a string representing the specified `Number` object
  + parameter
    + `radix` (optional): specify the base to use for representing numeric values, [0, 36]
  + return: a string representing the specified `Number` object



### 5.2.8 Built-in JS class: `String`


#### Live coding video: predefined class - String

<a href="https://edx-video.net/W3CJSIXX2016-V005600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/af3rcw)

__Source code from the video example__

[CodePen Demo](https://codepen.io/w3devcampus/pen/pwPGve?editors=0012)

[Local Demo](src/js/05b-example04.js)


The `String` class can be used to build new strings, but it’s preferable to use the standard syntax:

<div><ol>
<li value="1">&gt;<strong> var name = 'Michel'; // use this rather than&nbsp;using new String(...)</strong></li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; typeof name;</li>
<li>"string"</li>
<li>&nbsp;</li>
<li>&gt; var name = new String('Michel');</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; typeof name;</li>
<li>"string"</li>
</ol></div>

Some reminders about strings:

<div><ol>
<li value="1">&gt; var name = 'Michel';</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; name.length;</li>
<li>6</li>
<li>&nbsp;</li>
<li>&gt; name[0];</li>
<li>"M"</li>
<li>&nbsp;</li>
<li>&gt; name[0] = 'Z';</li>
<li>"Z"</li>
<li>&nbsp;</li>
<li>&gt; name; <strong>// we cannot modify a string using s[index] = value;</strong></li>
<li>"Michel"</li>
<li>&nbsp;</li>
<li>&gt; 'Michel'.length;</li>
<li>6</li>
<li>&nbsp;</li>
<li>&gt; 'Michel'[0];</li>
<li>"M"</li>
</ol></div>

Explanations: 

+ _Line 10_: in JavaScript, and in many other programming languages, __a string is not modifiable at all.__

  __When we do `var s = s + "hello"`, in fact, we are building a new string somewhere in memory, and we assign this new value to the variable `s`.__

  We never "modify" the characters of the string s, we just give to s another address in memory to point to. 

#### Useful methods: `toUpperCase`, `toLowerCase`, `indexOf`, `charAt`

These methods are all inherited from the String class:

+ `toUpperCase`: returns the string in upper case. Do not change the original string.
+ `toLowerCase`: returns the string in lower case. Do not change the original string.
+ `indexOf`: returns the index of the string value passed as parameter, -1 if the string value is not found in the original string.
+ `charAt`: returns the char at the index passed as parameter. Returns an empty string if the index is out of bounds (less than 0 or greater than the length of the string).

<div><ol>
<li value="1">&gt; var s = "I'm the Walrus";</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; var s1 = s.toUpperCase();</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; s1;</li>
<li>"I'M THE WALRUS"</li>
<li>&gt; var s2 = s1.toLowerCase();</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; s2;</li>
<li>"i'm the walrus"</li>
<li>&nbsp;</li>
<li>&gt; s; // s is unchanged</li>
<li>"I'm the Walrus"</li>
<li>&nbsp;</li>
<li>&gt; s.indexOf('w'); // no ‘w’ in s</li>
<li>-1</li>
<li>&nbsp;</li>
<li>&gt; s2.indexOf('w');</li>
<li>8</li>
<li>&nbsp;</li>
<li>&gt; s2[8]; // char at index 8</li>
<li>"w"</li>
<li>&nbsp;</li>
<li>s2.charAt(8); // same as s2[8]</li>
<li>"w"</li>
</ol></div>


#### Other useful methods: lastIndexOf, chaining methods

+ `lastIndexOf`: returns the last index of the string value passed as parameter
+ `indexOf` can also be used with two parameters, the second one being the starting index when looking for the string value passed as parameter

<div><ol>
<li value="1">&gt; s = 'wow wow wow!';</li>
<li>"wow wow wow!"</li>
<li>&nbsp;</li>
<li>&gt; s.lastIndexOf('w');</li>
<li>10</li>
<li>&nbsp;</li>
<li>&gt; s.indexOf('w', 1); // start looking at s at index=1, s[0] is ignored</li>
<li>2</li>
<li>&nbsp;</li>
<li>&gt; var s1 = s.toUpperCase();</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; s1;</li>
<li>"WOW WOW WOW!"</li>
<li>&nbsp;</li>
<li>&gt; s1.toLowerCase().lastIndexOf('w'); // we can chain method calls using ‘.’</li>
<li>10</li>
</ol></div>


#### Notes for 5.2.8 Built-in JS class: String

+ `String` class
  + used to build new strings
  + constructor: `var name = new String('Miche');`
  + recommendaton: using the standard syntax, e.g., `var name = 'Michel';`
  + properties and methods: `var name = 'Michel';`
    + `length` property: `name.length; // 6`
    + string as an array w/ index: `name[0]; // "M"`
    + not modifiable: `name[0] = 'Z'; // "Z"` and `name; // 'Michel'`
    + other expression: `'Michel'.length; // 6` and `'Michel'[0]; // "M"`
  + changing character(s)
    + string not modifiable
    + build a new string by concatenating substrings
    + reference to another address in memory

+ Useful methods of `String` class
  + `toUpperCase`: return the string in upper case, not changing the original string
  + `toLowerCase`: return the string in lower case, not changing the original string
  + `indexOf(char[, start])`:
    + looking for string value `char` starting from `start`
    + return the index of string valuse passed as parameter (`char`)
    + return `-1` if nothing matched
  + `charAt`:
    + return the char at the index passed as parameters
    + return empty string if index out of bound (< 0 or > str.length )
  + `lastIndexOf`: return the last index of the string value passed as parameter

+ [`String.prototype.indexOf()` method](https://tinyurl.com/n2m66t3p)
  + syntax: `str.indexOf(searchValue [, fromIndex])`
  + docstring: return the index within the calling `String` object of the 1st occurrence of the specified value
  + parameters:
    + `searchValue`: the string value to search for
    + `fromIndex` (optional): an integer representing the index at which to start the search, defaults to 0
  + return: the index of the first occurrent of `searchValue` or `-1` if not found


### 5.2.9 The most useful methods of the class String

The most useful methods of the String are: slice, substring, split, join

#### The `slice` and `substring` methods

__Both these methods can be used to extract a substring from a string.__ They take two parameters: the start and end index of the slice (element at end index will NOT be included in the slice): “please cut from this index, to this one, not included!”.

These two methods are very similar.

Examples:

<div><ol>
<li value="1">&gt; var s = "My name is Bond! James Bond!"; </li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; s;</li>
<li>"My name is Bond! James Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s.slice(11, 16);</li>
<li>"Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s; <strong>// s is unchanged</strong></li>
<li>"My name is Bond! James Bond!"</li>
<li>&nbsp;</li>
<li>s.substring(11,&nbsp;16);</li>
<li>"Bond!"</li>
<li>&nbsp;</li>
<li>&gt;&nbsp;s;&nbsp;<strong>// s is still unchanged</strong></li>
<li>"My name is Bond! James Bond!"</li>
<li></li>
<li>&gt; s = s.substring(11, 16);</li>
<li>"Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s; <strong>// this time s has changed, because we did s = s.substring(...), the same&nbsp;</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;// could have been done with s = s .slice(...)</strong></li>
<li>"Bond!"</li>
</ol></div>


#### Difference between `slice` and `substring`

__[Advanced] There is a difference between `slice` and `substring`, when the second parameter is negative__

If you are a beginner, we recommend that you use `substring` for most common cases (as it will behave the same as `slice`) and that you stay away from negative parameters, where `slice` and `substring` show small differences.

Beginners: do not read what follows about slice and substring! There will be no related graded questions at the end of this chapter!

<div><ol>
<li value="1">&gt; var s = "My name is Bond! James Bond!"; </li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; s.slice(11, -1); // start from index = 11 to length-1, extract the end of the string from 11th element</li>
<li>"Bond! James Bond"</li>
<li>&nbsp;</li>
<li>&gt; s.substring(11, -1); // the reverse, extract from 0 until 11-1, get the first 10 chars</li>
<li>"My name is "</li>
<li>&nbsp;</li>
<li>&gt; s.substring(1, -1); // extract from 0 to 1-1 = 0, get the first char</li>
<li>"M"</li>
</ol></div>

Actually, here is a summary of the common behaviors and the differences between slice and substring.


__[Advanced] `slice(start, stop)` works like `substring(start, stop)` with a few different behaviors__

What they have in common:

+ If `start` equals `stop`: returns an empty string
+ If `stop` is omitted: extracts characters to the end of the string
+ If either argument is greater than the string's length, the string's length will be used instead.

Distinctions of `substring()`:

+ If `start` > `stop`, then substring will swap those two arguments.
+ If either argument is negative or is NaN, it is treated as if it were 0.


Distinctions of `slice()`:

+ If `start` > `stop`, `slice()` will NOT swap the two arguments.
+ If `start` is negative: sets char from the end of string.
+ If `stop` is negative: sets `stop` to `string.length – Math.abs(stop)`.


#### The `split()`, `join()` and `concat()` methods

The `split` method returns an array of strings, the parameter is a separator. The `join` method builds a string from an array of strings.

<div><ol>
<li value="1">&gt; var s = "My name is Bond! James Bond!"; </li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; s.split(" ");</li>
<li>["My", "name", "is", "Bond!", "James", "Bond!"]</li>
<li>&nbsp;</li>
<li>&gt; s;</li>
<li>"My name is Bond! James Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s.split(' ').join('-#-');</li>
<li>"My-#-name-#-is-#-Bond!-#-James-#-Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s.split(' ').join('.......');</li>
<li>"My.......name.......is.......Bond!.......James.......Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s.split('Bond!').join('.......');</li>
<li>"My name is ....... James ......."</li>
<li>&nbsp;</li>
<li>&gt; s.split('Bond!').join(' ');</li>
<li>"My name is James "</li>
<li>&nbsp;</li>
<li>&gt; s; // s is unchanged </li>
<li>"My name is Bond! James Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s.concat("And I've made a lot of movies!");</li>
<li>"My name is Bond! James Bond! And I've made a lot of movies!"</li>
<li>&nbsp;</li>
<li>&gt; s; // s is also unchanged by concat</li>
<li>"My name is Bond! James Bond!"</li>
<li>&nbsp;</li>
<li>&gt; s = s + "and I've made a lot of movies!"; // this changes s</li>
<li>"My name is Bond! James Bond! And I've made a lot of movies!"</li>
<li>&nbsp;</li>
<li>&gt; s += " Action films!" // this too, most common syntax for concatenating strings</li>
<li>"My name is Bond! James Bond! And I've made a lot of movies! Action films!"</li>
<li>&nbsp;</li>
<li>&gt; s; // s changed too</li>
<li>"My name is Bond! James Bond! And I've made a lot of movies! Action films!"</li>
</ol></div>


#### Notes for 5.2.9 The most useful methods of the class String

+ The `slice` and `substring` methods
  + both used to extract a substring from a string
  + similarity
    + two parameters: `start` and `stop` index
    + excluding element at `stop` index
    + the original string remaining unchanged
    + `start = stop`: return an empty string
    + `stop` omitted: extract characters to the end of the string
    + either arguments > `str.length`: using `str.length` instead
  + difference
    + occuring only when the second parameter is negative
    + recommendation: using `substring` for most common cases
    + `slice()`
      + w/ negative `stop`: extract substring starting from index `start` to `length + stop`
      + `start > stop`: NOT swap these two arguments
      + `start < 0`: set char from the end of string
      + `stop < 0`: set stop to `length + stop`
    + `substring`
      + w/ negative `stop`: extract substring reverse from index start to `start + stop`
      + `start > stop`: swap these two parameters
      + either argument negative or NaN: treated as 0

+ Example: similarity of `slice` and `substring`
  + declare string: `var s = "My name is Bond! James Bond!";`
  + get substring w/ `slice`: `s.slice(11, 16); // "Bond!"`
  + get substring w/ `substring`: `s.substring(11, 16); // "Bond!"`
  + original string remaining unchanged: `s; // "My name is Bond! James Bond!";`
  + reassign value for variable: `s = s.slice(11, 16); // "Bond!"` and `s = s.substring(11, 16); // "Bond!"`
  + variable pointing to another object: `s; // "Bond!"`

+ Example: difference btw `slice` and `substring`
  + declare string: `var s = "My name is Bond! James Bond!";`
  + get substring w/ `slice` and negative `stop`: `s.slice(11, -1); // "Bind! James Bond"`
  + get substring w/ `substring` and negative `stop` as reverse direction: `s.substring(11, -1); // My name is "`
  + get the first character: `s.substring(1, -1); // "M"`

+ The `split()`, `join()` and `concat()` methods
  + `split()`:
    + return an array of strings w/ parameter as separator
    + original string unchanged
  + `join()`: build a string from an array of strings
  + `concat`:
    + return concatenated strings 
    + original string unchanged
    + `+` operator same effect but change the original string

+ Example: `split()`, `join()` and `concat()` methods
  + declare string: `var s = "My name is Bond! James Bond!";`
  + separate string into singleton object: `s.split(); // ["My", "name", "is", "Bond!", "James", "Bond!"]`
  + chaining methods w/ `split` and `join`
    + `s.split(' ').join('-#-');        // "My-#-name-#-is-#-Bond!-#-James-#-Bond!"`
    + `s.split(' ').join('.......');    // "My.......name.......is.......Bond!.......James.......Bond!"`
    + `s.split('Bond!').join('......);  // "My name is ....... James ......."`
    + `s.split('Bond!').join(' ');      // "My name is James "`
  + concatenate string:
    + `s.concat(" And I've made a lot of movies!"); // "My name is Bond! James Bond! And I've made a lot of movies!"`
    + `s; // "My name is Bond! James Bond!"`
  + concatenate w/ `+` operator:
    + `s = s + " And I've made a lot of movies!"; // "My name is Bond! James Bond! And I've made a lot of movies!"`
    + `s; // "My name is Bond! James Bond! And I've made a lot of movies!"`


### 5.2.10 Built-in JavaScript class: Math

It’s not possible to do `var m = new Math();`

<div><ol>
<li value="1">&gt; var m = new Math();</li>
<li>VM5777:1 <strong>Uncaught TypeError: Math is not a constructor</strong></li>
<li> at &lt;anonymous&gt;:1:9</li>
<li>(anonymous) @ VM5777:1</li>
</ol></div>

But the `Math` class has a lot of properties and methods that are useful for arithmetic expressions. __They are all class methods and properties, so you will need to use the name of the class followed by the dot operator to access them.__

Here are some examples:

<div><ol>
<li value="1">&gt; <strong>Math.PI;</strong></li>
<li>3.141592653589793</li>
<li>&nbsp;</li>
<li>&gt; <strong>Math.SQRT2;</strong></li>
<li>1.4142135623730951</li>
<li>&nbsp;</li>
<li>&gt; <strong>Math.E; // Euler constant</strong></li>
<li>2.718281828459045</li>
<li>&nbsp;</li>
<li>&gt; <strong>Math.LN2; // Neperian log of 2</strong></li>
<li>0.6931471805599453</li>
<li>&nbsp;</li>
<li>&gt; <strong>Math.LN10; // Neperian log of 10</strong></li>
<li>2.302585092994046</li>
</ol></div>


#### Random numbers between 0 and 1 with `Math.random()`

`Math.random()` returns a float value between 0 and 1.

Examples:

<div><ol>
<li value="1">&gt; <strong>Math.random();</strong></li>
<li>0.6033316111663034</li>
<li>&nbsp;</li>
<li>&gt; <strong>100 * Math.random(); // between 0 and 100</strong></li>
<li>11.780563288516422</li>
</ol></div>

__To get a number between a min and a max value, use this formula: `val = ((max - min) * Math.random()) + min`__

And here is an utility function:

<div><ol>
<li value="1">function getRandomValue(min, max) {</li>
<li>&nbsp; &nbsp; return ((max - min) * Math.random()) + min;</li>
<li>}</li>
<li>&nbsp;</li>
<li>&gt; getRandomValue(5, 10);</li>
<li>5.064160540161435</li>
</ol></div>


#### Math and rounding methods `round()`, `ceil()`, `floor()`

`round`: to get the closest integer value.

For example `Math.round(Math.random());` will return 0 or 1.

Indeed, if `Math.random()` returns a value above 0.5, `Math.round` of this value will return 1, if the value is below 0.5, `Math.round` will return 0:

<div><ol>
<li value="1">&gt; Math.round(Math.random());</li>
<li>1</li>
<li>&nbsp;</li>
<li>&gt; Math.round(Math.random());</li>
<li>0</li>
<li>&nbsp;</li>
<li>&gt; Math.round(Math.random());</li>
<li>1</li>
<li>&nbsp;</li>
<li>&gt; Math.round(Math.random());</li>
<li>1</li>
</ol></div>


#### Get the min and the max of two values with `Math.min(a, b)` and `Math.max(a, b)`

<div><ol>
<li value="1">&gt; Math.min(12, 4);</li>
<li>4</li>
<li>&nbsp;</li>
<li>&gt; Math.max(12, 4);</li>
<li>12</li>
</ol></div>

A useful function that restricts a value between  min and  max bounds:

<div><ol>
<li value="1"><strong>function restrictValue(value, min, max) {</strong></li>
<li><strong>&nbsp; &nbsp; return Math.min(Math.max(min, value), max);</strong></li>
<li><strong>}</strong></li>
<li>&nbsp;</li>
<li>&gt; restrictValue(40, 1, 20);</li>
<li>20</li>
<li>&nbsp;</li>
<li>&gt; restrictValue(-10, 1, 20);</li>
<li>1</li>
<li>&nbsp;</li>
<li>&gt; restrictValue(10, 1, 20);</li>
<li>10</li>
</ol></div>


#### Math functions for arithmetical computations sin(), cos(), tan(), atan(), atan2(), pow(), sqrt()

<div><ol>
<li value="1">&gt; Math.pow(2, 8); // 2^8</li>
<li>256</li>
<li>&nbsp;</li>
<li>&gt; Math.sqrt(9);</li>
<li>3</li>
<li>&nbsp;</li>
<li>&gt; Math.sin(Math.PI/2);</li>
<li>1</li>
<li>&nbsp;</li>
<li>&gt; Math.cos(Math.PI/2);</li>
<li>6.123233995736766e-17</li>
</ol></div>

__`Math.atan2(dy, dx)` is useful for getting an angle between a point in a canvas and the mouse cursor__

Here is a typical example of the use of `Math.atan2` in a video game, in order to make an object follow the mouse cursor by moving towards it. Look at the code in the `mainloop` function.

[CodePen Demo](https://codepen.io/w3devcampus/pen/aWOJQN)

[Local Demo](src/05b-example05.html)


#### Notes for 5.2.10 Built-in JavaScript class: Math

+ `Math` class
  + many properties and methods useful for arithmetic expressions
  + properties and methods by using the name of the class followed by the dot operator to access them
  + no constructor existed: `var m = new Math(); // M5777:1 Uncaught TypeError: Math is not a constructor ...`
  + common properties:
    + $\pi$: `Math.PI; // 3.141592653589793`
    + $\sqrt{2}$: `Math.SQRT2; // 1.4142135623730951`
    + Euler constant: `Math.E; // 2.718281828459045`
    + Neperian log of 2: `Math.LN2; // 0.6931471805599453`
    + Neperian log of 10: `Math.LN10; // 2.302585092994046`
  
+ `Math.random()` method
  + generate random numbers btw 0 and 1
  + return a float value btw 0 and 1
  + get a number btw a min and max value: `val = ((max - min) * Math.random()) + min;`
  + examples:
    + random number in [0, 1]: `Math.random(); // 0.6033316111663034`
    + random number in [0, 100]: `Math.random() * 100; // 11.780563288516422`
    + function to generate random number in [min, max]: `function getRandomValue(min, max) { return ((max - min) * Math.random()) + min; }`
    + random number in [5, 10]: `getRandomValue(5, 10); // 5.064160540161435`

+ Math and rounding methods
  + `round`: get the closest integer value
  + `ceil`: always round a number up to the next largest integer
  + `floor`: return the largest integer less than or equal to a given number
  + example - rounding a number: `Math.round(Math.random()); // 0 or 1`

+ The `max()` and `min()` methods
  + get max and min values w/ `Math.max(a, b)` and `Math.min(a, b)`
  + useful for restrict a value btw minimum and maximum bounds
  + examples
    + min of two values: `Math.min(12, 4); // 4`
    + max of two values: `Math.max(14, 4); // 14`
    + function to set restrict values: `function restrictValue(value, min, max) { return Math.min(Math.max(min, value), max) }`
    + apply restrict function: `restrictValue(40, 1, 20); // 20`, `restrictValue(-10, 1, 20); // 1`, and `restrictValue(10, 1, 20); // 10`

+ Some arithmetical methods
  + `sin()`: sine function in radians
  + `cos()`: cosine function in radians
  + `tan()`: tangent function in radians
  + `atan()`: arctangent function in radians
  + `atan2()`: arctangent function returning in angle in the plane; useful for getting an angle btw a point in a canvas and the mouse cursor


### 5.2.11 Built-in JS class: Date

Let's see how to get a date by calling the `Date` constructor.

__Without any argument, a call to `new Date()` returns the current date.__

Note: The return value is actually a Date object, which is displayed by calling `toString()` on this object.

<div><ol>
<li value="1">&gt; var date = new Date();</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; date;</li>
<li>Wed Apr 12 2017 11:10:28 GMT+0200 (CEST)</li>
<li></li>
<li>&gt;&nbsp;date.toString(); // same thing!</li>
<li>Wed&nbsp;Apr&nbsp;12&nbsp;2017&nbsp;11:10:28&nbsp;GMT+0200&nbsp;(CEST)</li>
</ol></div>


__We can also pass it an argument that can be:__

+ A string that encodes a date
+ A set of numeric values separated by a comma for month, day, hour, and so on
+ A Unix "timestamp"  (number of milliseconds elapsed since 1970)

... in this case it returns a date object that corresponds to the encoded date passed as argument.

Examples:

<div><ol>
<li value="1">&gt; new Date('2017 04 28');</li>
<li>Fri Apr 28 2017 00:00:00 GMT+0200 (CEST)</li>
<li>&nbsp;</li>
<li>&gt; new Date('2017 1 2');</li>
<li>Mon Jan 02 2017 00:00:00 GMT+0100 (CET)</li>
<li>&nbsp;</li>
<li>&gt; new Date('2017 1 2 8:30');</li>
<li>Mon Jan 02 2017 08:30:00 GMT+0100 (CET)</li>
</ol></div>

Numerical parameters can also be passed in this order: year, month (0-11), day (1-31), time (0-23), minutes (0-59), seconds , milliseconds (0-999). We do not have to pass everything but it should always be in this order.

Examples:

<div><ol>
<li value="1">&gt; new Date(2017, 3, 16, 14, 43, 10, 120);</li>
<li>Sun Apr 16 2017 14:43:10 GMT+0200 (CEST)</li>
<li>&nbsp;</li>
<li>&gt; new Date(2017, 0, 10, 14);</li>
<li>Tue Jan 10 2017 14:00:00 GMT+0100 (CET)</li>
<li>&nbsp;</li>
<li>&gt; new Date(2017, 1, 28) // 1 is February! Month indexes start at 0!</li>
<li>Tue Feb 28 2017 00:00:00 GMT+0100 (CET)</li>
<li>&nbsp;</li>
<li>&gt; new Date(2008, 1, 29);</li>
<li>Fri Feb 29 2008 00:00:00 GMT+0100 (CET)</li>
<li>&nbsp;</li>
<li>&gt; new Date(2017, 1, 29); // No February 29th in 2017! Gives 1st of March</li>
<li>Wed Mar 01 2017 00:00:00 GMT+0100 (CET)</li>
<li>&nbsp;</li>
<li>&gt; new Date(2017, 11, 31); // Happy new year!</li>
<li>Sun Dec 31 2017 00:00:00 GMT+0100 (CET)</li>
<li>&nbsp;</li>
<li>&gt; new Date(2017, 11, 32) // 32 Dec -&gt; 1st of January!</li>
<li>Mon Jan 01 2018 00:00:00 GMT+0100 (CET)</li>
</ol></div>

Calling `Date()` without "new" returns the current date as a string. It does not matter if we pass parameters:

<div><ol>
<li value="1">&gt; Date();</li>
<li>"Sun Apr 16 2017 14:51:47 GMT+0200 (CEST)"</li>
</ol></div>

#### Useful methods

<div><ol>
<li value="1">&gt; var d = new Date();</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; d.toString();</li>
<li>"Sun Apr 16 2017 14:52:52 GMT+0200 (CEST)"</li>
<li>&nbsp;</li>
<li>&gt; d.setMonth(2); // Change for month with index=2</li>
<li>1489672372092</li>
<li>&nbsp;</li>
<li>&gt; d.toString();</li>
<li>"Thu Mar 16 2017 14:52:52 GMT+0100 (CET)"</li>
<li>&nbsp;</li>
<li>&gt; d.getMonth(); // get current month index</li>
<li>2</li>
</ol></div>

__Let's play with my birthday!__

<div><ol>
<li value="1">&gt; var d = new Date(1965, 3, 16); // Michel Buffa's birthday</li>
<li>undefined</li>
<li>&nbsp;</li>
<li>&gt; d.getDay(); // Sunday is 0</li>
<li>5</li>
<li>&nbsp;</li>
<li>&gt; d; // let's verify</li>
<li><strong>Fri</strong> Apr 16 1965 00:00:00 GMT+0200 (CEST)</li>
<li>&nbsp;</li>
<li><strong>&gt; // Great, it was a Friday :-)</strong></li>
</ol></div>

Let's write a small piece of code that will guess which days of the week Michel Buffa's birthday will occur, between 2017 and 2047:

<div><ol>
<li value="1">&gt; var dayOfTheWeek = [0,0,0,0,0,0,0];</li>
<li>&nbsp;</li>
<li>for (var year = 2017; year &lt;= 2047; year++) {</li>
<li>&nbsp; &nbsp; dayOfTheWeek[new Date(year, 4, 16).getDay()]++;</li>
<li>}</li>
<li>&nbsp;</li>
<li>&gt; dayOfTheWeek</li>
<li>[4, 4, 5, 5, 5, 4, 4] // 4 times on a Sunday, Monday, Friday and Saturday, <br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // 5 times on Tuesday, Wednesday and Thursday</li>
</ol></div>

Explanations:

+ _Line 1_ we use an array with each element being the number of times the birthday occurs on a Sunday, Monday, etc.
+ _Line 3_: we iterate using a for loop on every year between 2017 and 2047.
+ _Line 4_: we build a `Date` object using 16 of April, but change the year, we compute the date of each of Michel Buffa's birthdays between 2017 and 2045, and we get the index of the day (using the `getDay()` method). This index is used to increment corresponding elements of the array defined in _line 1_.
+ Finally, _line 7_ displays the content of the array. Remember  that typing a variable name in the devtool console is equivalent to calling the object `toString()` method.

And here is a full version with input fields and results displayed in an HTML table:

[CodePen Demo](https://codepen.io/w3devcampus/pen/Mmwqgq)

[Local Demo](src/05b-example06.html)


#### Notes for 5.2.11 Built-in JS class: Date

+ `Date` class
  + constructor: `new Date(arg);`
    + return value actually a `Date` object but displayed by calling `toString()` on this object
    + `arg` omitted: return the current date
    + `arg`:
      + a string encoding a date
      + a set of numeric values separated by a comma for month, day, hour, and so on
      + a Unix "timestamp" (number of milliseconds elapsed since 1970)
  + numerical parameters:
    + order: year, month (0-11), dat (1-31), time (0-23), minutes (0-59), second, milliseconf (0-999)
    + not always w/ them all
    + must always be in the order
  + calling `Date` constructor w/o new: return currrent date
  + useful instance methods: [`getXXX` and `setXXX`](https://tinyurl.com/htvdv7ep)
    + set and get `XXX`
    + `XXX`: `FullYear`, `Month`, `Day`, `Hours`, `Minutes`, `Seconds`, `MilliSeconds`

+ Example: constructing `Date` object
  + current date:
    + `new Date(); // Wed Apr 12 2017 11:10:28 GMT+0200 (CEST)`
    + `Date(); // "Wed A"pr 12 2017 11:10:28 GMT+0200 (CEST)""`
  + encoded date:
    + `new Date('2017 04 28'); // "Fri Apr 28 2017 00:00:00 GMT+0200 (CEST)"`
    + `new Date('2017 1 2'); // "Mon Jan 02 2017 00:00:00 GMT+0100 (CEST)"`
    + `new Date('2017 1 2 8:30'); // "Mon Jan 02 2017 08:30:00 GMT+0100 (CEST)"`
  + numerical value
    + `new Date(2017, 3, 16, 14, 43, 10, 120); // "Sun Apr 16 2017 14:43:10 GMT+0200 (CEST)"`
    + `new Date(2017, 0, 10, 14); // "Tue Jan 10 2017 14:00:00 GMT+0100 (CET)"`
    + `new Date(2017, 1, 28) // "Tue Feb 28 2017 00:00:00 GMT+0100 (CET)"`
    + `new Date(2008, 1, 29); // "Fri Feb 29 2008 00:00:00 GMT+0100 (CET)"`
    + `new Date(2017, 1, 29); // "Wed Mar 01 2017 00:00:00 GMT+0100 (CET); No February 29th in 2017! Gives 1st of March"`
    + `new Date(2017, 11, 31); // "Sun Dec 31 2017 00:00:00 GMT+0100 (CET)"`
    + `new Date(2017, 11, 32) // "Mon Jan 01 2018 00:00:00 GMT+0100 (CET); 32 Dec -> 1st of January!"`

+ Example: useful instance methods
  + declare date: `var d = new Date(); // "Sun Apr 16 2017 14:52:52 GMT+0200 (CEST)"`
  + change month w/ index=2: `d.setMonth(2); // 1489672372092`, `d.tostring(); // "Thu Mar 16 2017 14:52:52 GMT+0100 (CET)"`
  + get current month index: `d.getMonth(); // 2`

+ Example: which day of the week
  + declare an array for counting: `var dayOfTheWeek = [0, 0, 0, 0, 0, 0, 0]`
  + iterate a range of years to find which day: `for (var year=2007; year <= 2047; year++) { dayOfTheWeek[new Date(year, 4, 16).getDay()]++; }`
  + display the result: `dayOfTheWeek; // [4, 4, 5, 5, 5, 4, 4]` $\to$ 4 times on Sunnday, Monday, Friday, and Saturday, ...


### 5.2.12 Discussion

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topics

+ Did you notice that the Math class has only class methods and properties: you always use `Math.PI`, `Math.cos(...)`, etc. Do class properties and methods make sense to you now? It would be nonsense to create two Math objects such as `m1 = new Math(); m2 = new Math(); var result = m1.cos(0.5); ...`
+ For a long time, we've talked about "predefined JavaScript objects", not "classes" when we talked about `Math`, `Date`, `Array`, etc. This is because JavaScript is not a class-based programming language.<br>ES6/ES2015 in 2015 introduced classes and the class keyword, but in fact there are no "real classes" in JavaScript, like in class-based languages such as Java or C#. ES6 classes are just constructor functions and prototypes (the thing behind Object Oriented JavaScript) disguised. Did you know that?




