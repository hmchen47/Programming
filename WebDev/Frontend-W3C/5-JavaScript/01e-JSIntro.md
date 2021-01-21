# Module 1: Introduction to JavaScript

## 1.5 Variables, values, functions, operators and expressions

### 1.5.1 JS variables and values

#### Live coding video: JavaScript variables

<a href="https://edx-video.net/W3CJSIXX2016-V001400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y5y8mg88)

In most of the examples seen earlier, we've used the concept of "variable", and we have used them to "store values". It's time to take a break and talk about them :-)

#### Variables

In order to remember a value, programming languages share the concept of "variables". When you write programs, you will need to store values in the computer's memory. By saving these values in "variables", by giving them a "name" (we call it an identifier), you can reuse them later for display, for computations, etc.

##### Create (declaring) a variable

With JavaScript versions < 5 (prior to 2015), there was a single way to create (we say "declare") a variable: using the `var` keyword. But with the subsequent versions (called ES2015/ES2016 or JavaScript 6/7), we can also use the keyword `let` (this has some subtle differences, which we'll explain later in the course when we will talk about "functions").

JavaScript is weakly typed. Each variable is declared with the keyword `var` or `let`. So you are not requibrown to specify the type of variable you are creating. __After the keyword "var" and a space, just give the name of the variable.__

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> myVar</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> x</span><span class="pun">;</span></li>
</ol></div><br/>

The first letter of a variable can only be "$", "_", "a" to "z", or "A" to "Z". The other characters in a name must be any of these, or numeric digits. The name is case sensitive. __So variables "myVar" and "MyVar" are different variables.__

There are some reserved names that you can't use as a variable name: `boolean`, `if`, `delete`, `var`, `function`, etc. as they are reserved words of the JavaScript language.


##### Give a value to a variable (assign a value to a variable)

A value can be assigned to a declared variable, or even directly in the variable declaration. For this, we use the equal character, also called "the assignment operator".

Example:

(notice at _line 4_ one way to introduce comments in your code: start a line with "//"!)

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> myValue</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">myValue </span><span class="pun">=</span><span class="pln"> </span><span class="lit">78</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// With the ES2015 syntax. BTW, lines staring with // are comments!</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> myNumber </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1.34</span><span class="pun">;</span></li>
</ol></div><br/>

At _line 2_, we are not saying that "myValue" and "78" are the same, we're saying "hey, I want to store the value 78, and I'm putting it in a variable whose name is "myValue". It's like giving an id to a location somewhere in the memory of the computer.

Using the id "myValue", we store 78 into a memory location identified by the name "myValue": a variable, or if you prefer, a value that can vary over time if we assign a new value to the variable "myValue" (for example by executing `myValue = 5;`).

You can also declare many variables at once by separating them with a comma. Always end each instruction line with a semi colon.

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> myNumber1</span><span class="pun">,</span><span class="pln"> myNumber2 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">34</span><span class="pun">,</span><span class="pln"> myNumber3</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Or with the ES2015 syntax, you can also use "let"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">,</span><span class="pln"> z </span><span class="pun">=</span><span class="pln"> </span><span class="lit">12</span><span class="pun">;</span></li>
</ol></div><br/>


##### Try the devtool console - you can type code in there too!

Reminder: you can always open the devtool console using F12 on windows, or ctrl-shift i, or cmd-alt-i on other computers.

If we copy and paste the variable declarations from the previous example, and type myNumber2 in the devtool console, it will display 34 (while `myNumber1` will have an undefined value):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> myNumber1</span><span class="pun">,</span><span class="pln"> myNumber2 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">34</span><span class="pun">,</span><span class="pln"> myNumber3</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="com">// Or with the ES6 syntax you can also use "let"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">let</span><span class="pln"> x</span><span class="pun">=</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> y</span><span class="pun">=</span><span class="lit">3</span><span class="pun">,</span><span class="pln"> z</span><span class="pun">=</span><span class="lit">12</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> x</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">1</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> z</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="lit">12</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> myNumber2</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="lit">34</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> myNumber1</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
</ol></div>

Below is an image that explains how you can try JavaScript code in the devtools console:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y66nzttl')"
    src    ="https://tinyurl.com/y68zj6jo"
    alt    ="Display JS variable in the console devtools, type some instructions, press return. For example type var x=2; then press the enter key; then type x; it will display its value '2'"
    title  ="Display JS variable in the console devtools, type some instructions, press return. For example type var x=2; then press the enter key; then type x; it will display its value '2'"
  />
</figure>

If you try to use a variable that has never been declared, you get an error message:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y66nzttl')"
    src    ="https://tinyurl.com/y4nkh6zc"
    alt    ="If you type k; followed by the enter key in the devtool console, and if k has not been defined, then an error message is displayed: 'uncaught referenceError: k is not defined...'"
    title  ="If you type k; followed by the enter key in the devtool console, and if k has not been defined, then an error message is displayed: 'uncaught referenceError: k is not defined...'"
  />
</figure>

##### Name conventions for variables

The JavaScript community has some conventions about naming variables:

+ The camelCase notation is preferbrown: mySpaceShip, sumOfAllGrades, etc.
+ For a variable, the first letter is lowercase and each first letter of each word is capitalized. Example: var myVariableName

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln">&nbsp;m</span><span class="typ">yModel</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span style="color: #000000;" color="#000000">// ES2015 syntax</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> michelBuffaAge </span><span class="pun">=</span><span class="pln"> </span><span class="lit">51</span><span class="pun">;</span></li>
</ol></div><br/>

Most JavaScript examples you will find are written in the camelCase format. For harmony in the code source, it is a good idea to keep this convention. Sometimes, you will see the snake_case naming convention, which separates each word of a variable with an underscore.

Here's an interesting article: [CamelCase vs underscores: Scientific showdown](https://whatheco.de/2011/02/10/camelcase-vs-underscores-scientific-showdown/)


#### Constants

Constants are variables that cannot be modified after a value has been set.

__The naming convention is to use uppercase letters with underscores.__

__Example: `var TIME_LIMIT = 50;`__

With JavaScript 5, constants were declared as normal variables, using the `var` keyword, and there were no verifications by the JavaScript interpreter forbidding you to modify them after you assigned a value to them.

With ES2015/2016 it is recommended that you use the keyword `const` instead of `var` to declare them. This means that an error will be raised if you try to change their value in the future.

Example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> TIME_LIMIT</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// ES2015 Syntax</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">const</span><span class="pln"> MAX_GRADE </span><span class="pun">=</span><span class="pln"> </span><span class="lit">20</span><span class="pun">;</span></li>
</ol></div><br/>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y66nzttl')"
    src    ="https://tinyurl.com/y64wlzh2"
    alt    ="Constants in the devtool console. We see the difference between var and const. The code executed is the one from the above example"
    title  ="Constants in the devtool console. We see the difference between var and const. The code executed is the one from the above example"
  />
</figure>


#### Summary

Here are a set of examples (using the `let` keyword, but they would also work with `var`):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">let</span><span class="pln"> a</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> thisIsAVariable</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> and_this_too</span><span class="pun">;</span><span class="pln"> </span><span class="com">// but <strong>does not respect the usual naming convention</strong></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> mix12three</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// invalid!</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> </span><span class="lit">2three4five</span><span class="pun">;</span><span class="pln"> </span><span class="com">// <strong>can't start with a digit!</strong></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> v1</span><span class="pun">,</span><span class="pln"> v2</span><span class="pun">,</span><span class="pln"> v3 </span><span class="pun">=</span><span class="pln"> </span><span class="str">'hello'</span><span class="pun">,</span><span class="pln"> v4 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">4</span><span class="pun">,</span><span class="pln"> v5</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">// Beware with lowercase / uppercase</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> case_matters </span><span class="pun">=</span><span class="pln"> </span><span class="str">'lower'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">let</span><span class="pln"> CASE_MATTERS </span><span class="pun">=</span><span class="pln"> </span><span class="str">'upper'</span><span class="pun">;</span></li>
</ol></div><br/>

#### Notes for 1.5.1 JS variables and values

+ JavaScript common syntax and devtool console
  + `//`: comments
  + devtools console: able to type and execute JavaScript Code as an interperter


+ Variables
  + used to "store values"
  + declaration
    + `var`
      + 'variable'; the only keyword to declare a variable before version 5 (2015)
      + example: `var myVar;`
    + `let`
      + allowed in subsequent versions (ES2015/ES2016 or JavaScript 6/7)
      + example: `let x;`
  + naming rules
    + first letter only "$", "_", "a" to "z", or "A" to "Z" allowed
    + other letters: "$", "_", "a" to "z", "A" to "Z", or "0" to "9"
    + case sensitive
    + reserved names: `boolean`, `if`, `delete`, `var`, `function`, etc.
  + assigning value
    + `=`: the assignment operator
    + `var myValue; myValue = 78`
      + store the value 78 and put it in a variable named "muValue"
      + given an id to a location somewhere in the memory of the computer
      + using the id "myValue", store 78 into a memory location identified by the name "muValue"
      + a value able to vary over time if assigning a new value to the variable "myValue", e.g., `myValue = 5;`
    + multiple variables allowed and saparated by ";", eg, `var myNumber1, myNumber2 = 34, myNumber3;`
  + using a variable never assigning a value: error message, eg, `Uncaught ReferenceError: k is not defined`
  + naming conventions
    + CamelCase notation preferbrown
    + 1st letter is lowercase and each 1st letter of each letter is capitalized

+ Constant
  + variables unable to be modified after set
  + naming convention: all uppercase letter w/ underscore
  + decalration
    + using `var` to declare w/ JavaScript 5 and w/o verification to modify it
    + recommended `const` after ES2015/ES2016 and raising error message if modifying
  + example: `var TIME_LIMIT = 50;` & `const MAX_GRADE = 20;`


#### Knowledge check 1.5.1

1. What is valid JavaScript below? (four correct answers!)
  
  a. `var !x = 3;`<br/>
  b. `var x, y=2, z=3;`<br/>
  c. `let myCar = "Ferrari";`<br/>
  d. `let _12 = 4;`<br/>
  e. `var michel123Buffa = "Your JavaScript teacher";`<br/>
  
  Ans: bcde<br/>
  Explanation: Only `var !x = 3;` is incorrect, as `!x` is not a valid variable name. All other declarations are valid. It is not necessary to assign a value when a variable is declared, so `var x, y=2, z=3;` is valid, even if x is not initialized.


2. An undefined variable is:

  a. A variable that has been declared but not initialized<br/>
  b. A variable that has not been declared<br/>
  
  Ans: a<br/>
  Explanation: An undefined variable x is a variable that has been declared with `var x;` or with `let x;` but that has no value yet. An error is triggebrown only when the variable is used in an expression such as `var z = x + y;`. A `console.log(x)` would give the value "undefined".


### 1.5.2 Scope of JS variables

#### Live coding video: scope of JavaScript variables

<a href="https://edx-video.net/W3CJSIXX2016-V001500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y6kduvn9)

#### Scope of JavaScript variables

__1) JavaScript 5 / ES5 scopes, with the `var` keyword__

<span style="color: brown; font-weight: bold;">JavaScript 5 / ES5 has the <code>var</code> keyword for declaring variables.</span>

<span style="color: brown; font-weight: bold;">JavaScript 5 / ES5 has two scopes: 1) a global scope</span> for declaring global variables, and <span style="color: brown; font-weight: bold;">2) a function scope</span> for declaring variables that are local to a function.

Furthermore, like in most programming languages, inside a function, <span style="color: brown; font-weight: bold;">a local variable masks a global variable that has the same name.</span>

See examples below.

__1.1) Global scope / global variable__

Global variables are variables declared outside of functions. They can be used anywhere in the code.

Here is an example:

[CodePen Demo](https://codepen.io/hmchen47/pen/vYXMGoQ)

[Local Demo](src/js/01e-example01.js)


__1.2) Local scope / local variable (also called function scope)__

Variables declared with the keyword `var` in a function, are said to be "local to the function". They "mask" any global variable that may have the same name.

__When a variable is declared in a function, we also call it simply "a local variable",__ as opposed to "a global variable". __In JavaScript 5 (and this is not common in programming languages), local variables are__ <span style="color: brown; font-weight: bold;">local to the function</span>. They can be used anywhere inside the function.

Most programming languages have local variables that are limited to the block of instructions between '{' and '}' that contains the variable declaration. We call these variables "block variables". This is the case with variables declared with the let keyword  introduced by JavaScript 6 / ES6. See examples at the end of this section.

Example of a local variable declared in a function, that is NOT local to the block, but to the whole function:

[CodePen Demo](https://codepen.io/w3devcampus/pen/RVMOGx)

[Local Demo](src/js/01e-example02.js)

Here is another example that shows the differences between global and local variables, and highlights the "masking" of global variables by local variables when they share the same name.

[CodePen Demo](https://codepen.io/w3devcampus/pen/oWEEmN)

[Local Demo](src/js/01e-example03.js)

__1.3) Never declare a variable without the keyword var!__

JavaScript is sometimes an overly permissive language. We can make stupid errors that turn out to be very hard to detect. One such error occurs when we forgot to use the `var` keyword while declaring a local variable.

In JavaScript 5 / ES5, a variable declared in a function without the `var` keyword, makes it a global variable.

<p style="text-align: center; border: 1px solid; padding: 20px; margin: 20px;"><strong><span style="color: #ff0000;">BEST PRACTICE: in JavaScript 5 / ES5, always use the keyword <span style="font-family: 'courier new', courier;">var</span> when declaring a global or a local variable. <br><br>Better: use the keyword <span style="font-family: 'courier new', courier;">let</span> if you target browsers that support JavaScript 6 or above.</span></strong></p>

Here is an example that shows what happens when you forget to use var or let while declaring a local variable:

[CodePen Demo](https://codepen.io/w3devcampus/pen/rmJJbo)

[Local Demo](src/js/01e-example04.js)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3mylxab')"
    src    ="https://tinyurl.com/y6xaksco"
    alt    ="Declaring a variable without var in a function makes it global"
    title  ="Declaring a variable without var in a function makes it global"
  />
</figure>


__2) Since 2015 and ES2015, there are new scopes, with the `let` keyword__

<span style="color: brown; font-weight: bold;">Modern JavaScript has the <code>let</code> keyword for declaring variables, and the <code>const</code> keyword for declaring constants.</span>

<span style="color: brown; font-weight: bold;">Modern JavaScript has two scopes: 1) a global scope</span> for declaring global variables, and <span style="color: brown; font-weight: bold;">2) a block scope</span> for declaring variables between { and }. This is similar to what we find in many other programming languages such as Java, C# etc.

Furthermore, like in most programming languages, inside a block, <span style="color: brown; font-weight: bold;">a local variable masks other variables located in higher scopes (global or in another block that contains the current block).</span>

Example of a local variable declared with the `let` keyword. Its scope is the block:

[CodePen Demo](https://codepen.io/w3devcampus/pen/VbXNPz)

[Local Demo](src/js/01e-example05.js)

__3) Recommended way to declare variables: var or let?__

Well, all modern browsers support the `let` and `const` keywords, however, you might find lots of examples that still use the `var` keyword...

<span style="color: brown; font-weight: bold;">Anyway, we highly recommend to use <code>let</code> and <code>const</code> instead of <code>var</code>, for declaring </span>variables and constants!

#### Notes for 1.5.2 Scope of JS variables

+ Scope of JS variables
  + `var` keyword in JavaScript 5 / ES5
    + declaring variable
    + scope
      + global scope for global variable
      + function scope for local variable within function
    + local variable within a function overrides a global variable w/ the same name
    + global scope / global variable
      + variable declared outside of a function
      + used naywhere in the code
    + local scope / local variable (function scope)
      + variable declared to be local to the function
      + override any global variable w/ the same name
      + local to the function
      + used anywhere inside the function
    + only declaring a variable w/ `var` keyword
      + possibly making stupid errors hard to detect
      + variable declared in function w/o the `var` keyword $\to$ global variable
    + best practice
      + always declaring a global or a local variable w/ `var`
      + using `let` if browser supporting JavaScript 6
  + `let` & `const` keywords since ES2015
    + `let` keyword to declar variables
    + `const` keywork to declare constants
    + scope
      + global scope for global variable
      + block scope for variable declared btw "{" and "}"
    + a local variable override other variables located in higher scopes
  + block variables
    + most programming languages applied
    + local variable within the block of instructions btw "{" and "}"
    + variable declared within "{" and "}"
  + highly recommended to use `let` and `const` instead of `var` for declaring variables and constants


### 1.5.3 JS data types

#### Live coding video: JavaScript data types

<a href="https://edx-video.net/W3CJSIXX2016-V001600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y62bflrz)

#### What kind of values can we assign to a variable?

Well, there are multiple possibilities:

1. What we call "primitive data types": for example a number, a string, etc. ex: `var x = 3; var name = "Buffa";`
2. Objects (everything that is not a  "primitive data type" is an object): `var michel = {firstName:'Michel', lastName:'Buffa'};`
    + There is a set of "predefined objects" in JavaScript (arrays, functions, etc). We will come back on these later in the course.

##### JavaScript has a small set of primitive data types

+ __number:__ `1,2,105,3.14 ...`
+ __string:__ `'a', "one", 'two' , 'World Wide Web' ...`
+ __boolean:__ `true / false`
+ __undefined:__ absent or unknown value
+ __null:__ special keyword, meaning no value or empty. The difference from `undefined` is that when a variable is `null`, it is still defined.

These are the simplest forms of data we can use in programming.

Anything that is not listed above is _an object_ (JavaScript objects are covered later in Week 3). 

##### You said JavaScript does not have types for variables?

No! I said that JavaScript is weakly typed; you do not declare the type of variable. In some other languages (Java language syntax, for instance) instead of `var x=2;` or `let name="Buffa";` you would write `int x=2;` or String `name = "Buffa";`, with the datatype explicit in the variable declaration.

#### Knowing the type of a JavaScript variable: the `typeof` operator

The next section of the course talks about "operators" but there is one that is better introduced in this section: the typeof operator, that is useful for knowing the type of a variable depending in its value (possible values: `number`, `string`, `boolean`, `undefined`, `object`, or `function`)

We will use it in lots of examples in the next three sections.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5rea57w')"
    src    ="https://tinyurl.com/y6hmpqr9"
    alt    ="dynamic typing. You can use the typeof operator to see the 'dynamic type of a variable'. For example, type let n=3; then typeof n, it will display 'number'. Then type n='toto'; and typeof n; this time it displays 'string'"
    title  ="dynamic typing. You can use the typeof operator to see the 'dynamic type of a variable'. For example, type let n=3; then typeof n, it will display 'number'. Then type n='toto'; and typeof n; this time it displays 'string'"
  />
</figure>

This operator is not often use in JavaScript programs, but it's useful for us, for explaining the data types.


#### Notes for 1.5.3 JS data types

+ Types of data in JS
  + primitive data types
    + __number:__ `1,2,105,3.14 ...`
    + __string:__ `'a', "one", 'two' , 'World Wide Web' ...`
    + __boolean:__ `true / false`
    + __undefined:__ absent or unknown value
    + __null:__ special keyword, meaning no value or empty
  + objects
    + everything not a "primitive data type"
    + a set of "predefined objects": arrays, functions, etc.
    + example: `ar michel = {firstName:'Michel', lastName:'Buffa'};`
  + `null` still defined

+ JavaScript data type
  + weakly typed programming language
  + not declaring w/ the type of variable
  + `typeof` operator: showing the type of a variable depending on its value
  + possible values of `typeof` operator: `number`, `string`, `boolean`, `undefined`, `object`, or `function`


#### Knowledge check 1.5.3

1. Can we declare types for JavaScript variables, like var String givenName = "Michel";

  a. No, JavaScript does not allow you to declare a type for its variables.<br/>
  b. Yes, you can optionally declare the type of a variable.<br/>

  Ans: a<br/>
  Explanation: JavaScript variables are dynamically typed, but you can't add a data type when you declare a variable.


### 1.5.4 Numbers

Number values can be:

+ __Integer:__ `1`, `4`, `274929`<br/>
  Type `343` in the devtool console, and after you press the Enter key,  the corresponding value (343) will be displayed.
+ __Signed integer:__ `-17`
+ __Decimal:__ `3.46`, `-466.8770`

  Examples of integer and decimals:

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> n</span><span class="pun">=</span><span class="lit">1</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> n</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> n</span><span class="pun">=</span><span class="lit">1234</span><span class="pun">;</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="lit">1234</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> n</span><span class="pun">;</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> n</span><span class="pun">=</span><span class="lit">1.23</span><span class="pun">;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="lit">1.23</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> n</span><span class="pun">;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> </span><span class="lit">123</span><span class="pun">;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  </ol></div>

+ __Scientific notation:__ `3.46e4`, `5.3e+6`, `5344000e-5`

  `3.46e4` equals `3.46 x 10^4` equals `34600`

  Examples:

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">1e1</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="lit">10</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">1e+1</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="lit">10</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">2e+3</span><span class="pun">;</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="lit">2000</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> </span><span class="lit">2e+3</span><span class="pun">;</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">2e-3</span><span class="pun">;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="lit">0.002</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">123.456E-3</span><span class="pun">;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="lit">0.123456</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> </span><span class="lit">2e-3</span><span class="pun">;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  </ol></div>

+ __Octal:__ `010`

  <span style="color: brown; font-weight: bold;">Be careful with this, don't start an integer with 0 (zero), JavaScript will understand it as an octal value.</span>

  `010` equals `8` which means `1 * 8^1 + 0 * 8^0`

  The number `0456` means `4 * 8^2 + 5 * 8^1 + 6 * 8^0`

  __Question 1:__ What's the result, as an integer, of the operation: `24 - 024`?

  __Explanation 1:__ `24` is an integer which equals `24` but `024` is an octal value which equals `20`.

  __Question 2:__ Which value will be displayed in the devtool console if you type 098 followed by the Enter key?

  __Explanation 2:__ `9` and `8` don't exist in base `8` (only `0` to `7`), so the typed number will be considered as an integer.

+ __Hexadecimal:__ `0xF3`

  `0xFF` equals `255`, `0xF3` means `15 * 16^1 + 3 * 16^0` and the resulting value is `243`

  Examples of octal and hexadecimal data types:

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> n3 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0377</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> n3</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> n3</span><span class="pun">;</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="lit">255</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> n4 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0x00</span><span class="pun">;</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> n4</span><span class="pun">;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> n4</span><span class="pun">;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="lit">0</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> n5 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0xFF</span><span class="pun">;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> n5</span><span class="pun">;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> n5</span><span class="pun">;</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="lit">255</span></li>
  </ol></div>

+ __Special values:__
  + `+Infinity`
  + `-Infinity`
  + `NaN` (Not a Number)

The value `Infinity` (or `+Infinity`) represents all number values greater than `1.79769313486231570e+308` and `-Infinity` represents values smaller than `-1.79769313486231570e+308`.

Finally, `Nan` represents _not-a-number_ values, for example if you try to divide 0 by 0 (type 0/0 in the devtool console).

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">NaN</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">3</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">Infinity</span></li>
</ol></div>

Examples:

  Any operation with Infinity gives Infinity as a result:

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="kwd">Infinity</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">1e309</span><span class="pun">;</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="kwd">Infinity</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">1e308</span><span class="pun">;</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="lit">1e+308</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="lit">6</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="kwd">Infinity</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="pun">-</span><span class="kwd">Infinity</span><span class="pun">;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> i</span><span class="pun">;</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pun">-</span><span class="kwd">Infinity</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> i</span><span class="pun">;</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  </ol></div><br/>

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="kwd">NaN</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="pun">-</span><span class="kwd">Infinity</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="kwd">NaN</span></li>
  </ol></div><br/>

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> </span><span class="lit">20</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="kwd">Infinity</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="pun">-</span><span class="kwd">Infinity</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="pun">-</span><span class="kwd">Infinity</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="kwd">Infinity</span></li>
  <li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L9" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">Infinity</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> </span><span class="lit">9999999999999</span><span class="pun">;</span></li>
  <li class="L0" style="margin-bottom: 0px;"><span class="kwd">Infinity</span></li>
  </ol></div>

Examples with `NaN`:

  `NaN` is a special value and its type is "Number"!

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> </span><span class="kwd">NaN</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="str">"number"</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">NaN</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="kwd">NaN</span></li>
  </ol></div><br/>

  <div class="source-code"><ol style="list-style-type: decimal;" class="linenums">
  <li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> a </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pln"> </span><span class="pun">*</span><span class="pln"> </span><span class="str">"f"</span><span class="pun">;</span></li>
  <li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
  <li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> a</span><span class="pun">;</span></li>
  <li class="L4" style="margin-bottom: 0px;"><span class="kwd">NaN</span></li>
  <li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
  <li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">2</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> a</span><span class="pun">;</span></li>
  <li class="L7" style="margin-bottom: 0px;"><span class="kwd">NaN</span></li>
  </ol></div>

#### [ADVANCED] Optional explanations about numbers

In JavaScript, numbers are represented with a double-precision 64-bit format (IEEE 754). These 64 bits are used with this table:

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 50vw;" cellspacing="0" cellpadding="5" border="1">
  <thead>
  <tr style="font-size: 1.2em; vertical-align:middle"">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Total bits</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Sign</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">Exponent</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Significant</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="font-family: Verdana; padding-left: 0px; word-wrap: break-word; text-align: center;">
  <p style="margin: 0px 0px 10px;">64</p>
  </td>
  <td style="font-family: Verdana; padding-left: 20px; word-wrap: break-word; text-align: center;">
  <p style="margin: 0px 0px 10px;">1</p>
  </td>
  <td style="font-family: Verdana; padding-left: 20px; word-wrap: break-word; text-align: center;">
  <p style="margin: 0px 0px 10px;">11</p>
  </td>
  <td style="font-family: Verdana; padding-left: 20px; word-wrap: break-word; text-align: center;">
  <p style="margin: 0px 0px 10px;">52</p>
  </td>
  </tr>
  </tbody>
</table>

What does it mean?

First, each number is represented as a float. For example, `1` equals `1.0`. But there are approximation errors that are well-known in float calculations. One common example of errors due to the approximation of floating point numbers is that `0.1 + 0.2` does not equal `0.3`.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">0.1</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">0.2</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="lit">0.30000000000000004</span></li>
</ol></div>

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y6penhc3')"
    src    ="https://tinyurl.com/y4w3xj37"
    alt    ="devtool console 0.1 + 0.2 is not equal to 0.3 but to 0.30000000000000004"
    title  ="devtool console 0.1 + 0.2 is not equal to 0.3 but to 0.30000000000000004"
  />
</figure>


Second, an integer has `2^52` relevant bits, so the biggest integer is `2^53`. There is one bit that determines the sign of the number, so the smallest signed integer is `-2^53`.

Note: Some arithmetic functions use only numbers with a 32-bit format. Larger numbers will be converted...

(Advanced) For more information about floating point numbers, [follow this link at Wikipedia](https://en.wikipedia.org/wiki/IEEE_floating_point).

#### Notes for 1.5.4 Numbers

+ Number values in JS
  + __integer__: `1`, `23865`; not starting w/ `0` but `089 = 89`
  + __signed integer__: `-17`
  + __decimal__: `3.46`, `-466.877`
  + __scientific notation__: `3.46e4`, `5.3e+6`, `5344000e-5`
  + __octal__: `010 = 8`, `0456 = 4 * 8^2 + 5 * 8^1 + 6 * 8^0`; starting w/ `0` w/ all numbers `0`~`7`
  + __hexadecimal__: `0xF3`
  + special values
    + `+Infinity`
      + all number values greater than `1.79769313486231570e+308`
      + `1/0` $\to$ `Infinity`
      + `typeof(Infinity)` $\to$ number
    + `-Infinity`: all number values smaller than `-1.79769313486231570e+308`, `-1/0`
    + `NaN` (Not a Number): `0/0`

+ Precision of numbers
  + a double-precision 64-bit format
    + total bits: 64
    + sign: 1 bit
    + exponent: 11 bits
    + significant: 52 bits
  + following IEEE 754 standard
  + each number represented as a float
  + an integer:
    + $2^{52}$ relevenat bits
    + biggest number: $2^{53}$
    + smallest number: $-2^{53}$
  + some arithmetic function only w/ 32-bit format


#### Knowledge check 1.5.4

1. What is the value of a after the execution of `var a = 18 / 0`;?

  a. `Infinity`<br/>
  b. `0`<br/>
  c. `undefined`<br/>
  d. `NaN`<br/>

  Ans: a<br/>


2. What is the value of a after the execution of `var a = 0 / 0;`?

  a. `undefined`<br/>
  b. `NaN`<br/>
  c. `0`<br/>
  d. `Infinity`<br/>

  Ans: b<br/>
  Explanation: Something not null divided by zero is infinity, but 0 divided by zero means nothing. So, the result is `NaN` (Not a Number)


### 1.5.5 JS operators and expressions

__An expression__ is a small piece of code used to produce a value.

For example, the expression 3 + 5 produces the value 8, and the value 11 alone is also an expression. Within an expression, we can find values, variables, operators, and expressions. The first two have been already described above, so all that's left are __operators__.

In JavaScript, __an operator__ can be unary or binary (plus one ternary operator). A unary operator is applied to one expression. It can be prefixed or suffixed.

__Unary operator example:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">typeof</span><span class="pln"> </span><span class="str">'world'</span><span class="pun">;</span></li>
</ol></div>

A binary operator is applied to two different expressions, and is both prefixed and suffixed.

__Binary operator example:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="lit">var x = 45</span><span class="pln"> </span><span class="pun">/</span><span class="pln"> </span><span class="lit">32</span><span class="pun">;</span></li>
</ol></div>

The division operator is binary.

Within an expression, we can also use parentheses to force the execution of the expression inside. Parentheses can be used to indicate precedence.

For example, this is an expression: `(3 + 2)`. And the expression `(3 + 2) * 4`, which equals 20, depends on the expression within the parentheses.

In JavaScript, expressions can evaluate to four types, which are: `numbers`, `strings`, `booleans`, and `objects`. For example, an expression with the operator - will evaluate to a `number`. But an expression with the operator + can evaluate to a `number` or a `string` (for addition or concatenation).


#### Notes for 1.5.5 JS operators and expressions






