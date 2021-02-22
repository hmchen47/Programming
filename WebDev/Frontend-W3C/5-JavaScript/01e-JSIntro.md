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

<div><ol>
<li style="margin-bottom: 0px;" value="1">var myVar;</li>
<li style="margin-bottom: 0px;">let x;</li>
</ol></div><br/>

The first letter of a variable can only be "$", "_", "a" to "z", or "A" to "Z". The other characters in a name must be any of these, or numeric digits. The name is case sensitive. __So variables "myVar" and "MyVar" are different variables.__

There are some reserved names that you can't use as a variable name: `boolean`, `if`, `delete`, `var`, `function`, etc. as they are reserved words of the JavaScript language.


##### Give a value to a variable (assign a value to a variable)

A value can be assigned to a declared variable, or even directly in the variable declaration. For this, we use the equal character, also called "the assignment operator".

Example:

(notice at _line 4_ one way to introduce comments in your code: start a line with "//"!)

<div><ol>
<li style="margin-bottom: 0px;" value="1">var myValue;</li>
<li style="margin-bottom: 0px;">myValue = 78;</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">// With the ES2015 syntax. BTW, lines staring with // are comments!</li>
<li style="margin-bottom: 0px;">let myNumber = 1.34;</li>
</ol></div><br/>

At _line 2_, we are not saying that "myValue" and "78" are the same, we're saying "hey, I want to store the value 78, and I'm putting it in a variable whose name is "myValue". It's like giving an id to a location somewhere in the memory of the computer.

Using the id "myValue", we store 78 into a memory location identified by the name "myValue": a variable, or if you prefer, a value that can vary over time if we assign a new value to the variable "myValue" (for example by executing `myValue = 5;`).

You can also declare many variables at once by separating them with a comma. Always end each instruction line with a semi colon.

Example:

<div><ol>
<li style="margin-bottom: 0px;" value="1">var myNumber1, myNumber2 = 34, myNumber3;</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">// Or with the ES2015 syntax, you can also use "let"</li>
<li style="margin-bottom: 0px;">let x = 1, y = 3, z = 12;</li>
</ol></div><br/>


##### Try the devtool console - you can type code in there too!

Reminder: you can always open the devtool console using F12 on windows, or ctrl-shift i, or cmd-alt-i on other computers.

If we copy and paste the variable declarations from the previous example, and type myNumber2 in the devtool console, it will display 34 (while `myNumber1` will have an undefined value):

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var myNumber1, myNumber2 = 34, myNumber3;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; // Or with the ES6 syntax you can also use "let"</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; let x=1, y=3, z=12;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; x;</li>
<li style="margin-bottom: 0px;">1</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; z;</li>
<li style="margin-bottom: 0px;">12</li>
<li style="margin-bottom: 0px;">&gt; myNumber2;</li>
<li style="margin-bottom: 0px;">34</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; myNumber1;</li>
<li style="margin-bottom: 0px;">undefined</li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1">var&nbsp;myModel;</li>
<li style="margin-bottom: 0px;"><span style="color: #000000;" color="#000000">// ES2015 syntax</span></li>
<li style="margin-bottom: 0px;">let michelBuffaAge = 51;</li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1">var TIME_LIMIT;</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">// ES2015 Syntax</li>
<li style="margin-bottom: 0px;">const MAX_GRADE = 20;</li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1">let a;</li>
<li style="margin-bottom: 0px;">let thisIsAVariable;</li>
<li style="margin-bottom: 0px;">let and_this_too; // but <strong>does not respect the usual naming convention</strong></li>
<li style="margin-bottom: 0px;">let mix12three;</li>
<li style="margin-bottom: 0px;">// invalid!</li>
<li style="margin-bottom: 0px;">let 2three4five; // <strong>can't start with a digit!</strong></li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">let a = 1</li>
<li style="margin-bottom: 0px;">let v1, v2, v3 = 'hello', v4 = 4, v5;</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">// Beware with lowercase / uppercase</li>
<li style="margin-bottom: 0px;">let case_matters = 'lower';</li>
<li style="margin-bottom: 0px;">let CASE_MATTERS = 'upper';</li>
</ol></div><br/>

#### Notes for 1.5.1 JS variables and values

+ JavaScript common syntax and devtool console
  + `//` and `/* (code block) */`: comments
  + devtools console: able to type and execute JavaScript Code as an interperter

+ Variables
  + used to "store values"
  + declaration
    + `var`
      + 'variable'; the only keyword to declare a variable before version 5 (2015)
      + example: `var myVar;`
    + `let` & `const`
      + allowed in subsequent versions (ES2015/ES2016 or JavaScript 6/7)
      + example: `let x;`
  + naming rules
    + first letter only "$", "_", "a" to "z", or "A" to "Z" allowed
    + other letters: "$", "_", "a" to "z", "A" to "Z", or "0" to "9"
    + case sensitive
    + reserved names: `boolean`, `if`, `delete`, `var`, `function`, etc.
  + assigning value
    + `=`: the assignment operator
    + example: `var myValue; myValue = 78;`
      + store the value 78 and put it in a variable named "muValue"
      + given an id to a location somewhere in the memory of the computer
      + using the id "myValue", store 78 into a memory location identified by the name "myValue"
      + a value able to vary over time if assigning a new value to the variable "myValue", e.g., `myValue = 5;`
    + multiple variables allowed and saparated by ";", eg, `var myNumber1, myNumber2 = 34, myNumber3;`
  + using a variable never assigning a value: error message, eg, `Uncaught ReferenceError: k is not defined`
  + naming conventions
    + CamelCase notation preferred
    + 1st letter is lowercase and each 1st letter of each word is capitalized

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
      + used anywhere in the code
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
    + `let` keyword to declare variables
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
    + example: `var michel = {firstName:'Michel', lastName:'Buffa'};`
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

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; var n=1;</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof n;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; n=1234;</li>
  <li style="margin-bottom: 0px;">1234</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof n;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; n=1.23;</li>
  <li style="margin-bottom: 0px;">1.23</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof n;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof 123;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  </ol></div>

+ __Scientific notation:__ `3.46e4`, `5.3e+6`, `5344000e-5`

  `3.46e4` equals `3.46 x 10^4` equals `34600`

  Examples:

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; 1e1;</li>
  <li style="margin-bottom: 0px;">10</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; 1e+1;</li>
  <li style="margin-bottom: 0px;">10</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; 2e+3;</li>
  <li style="margin-bottom: 0px;">2000</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof 2e+3;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; 2e-3;</li>
  <li style="margin-bottom: 0px;">0.002</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; 123.456E-3;</li>
  <li style="margin-bottom: 0px;">0.123456</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof 2e-3;</li>
  <li style="margin-bottom: 0px;">"number"</li>
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

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; var n3 = 0377;</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof n3;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; n3;</li>
  <li style="margin-bottom: 0px;">255</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; var n4 = 0x00;</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof n4;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; n4;</li>
  <li style="margin-bottom: 0px;">0</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; var n5 = 0xFF;</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof n5;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; n5;</li>
  <li style="margin-bottom: 0px;">255</li>
  </ol></div>

+ __Special values:__
  + `+Infinity`
  + `-Infinity`
  + `NaN` (Not a Number)

The value `Infinity` (or `+Infinity`) represents all number values greater than `1.79769313486231570e+308` and `-Infinity` represents values smaller than `-1.79769313486231570e+308`.

Finally, `Nan` represents _not-a-number_ values, for example if you try to divide 0 by 0 (type 0/0 in the devtool console).

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; 0 / 0;</li>
<li style="margin-bottom: 0px;">NaN</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; 3 / 0;</li>
<li style="margin-bottom: 0px;">Infinity</li>
</ol></div>

Examples:

  Any operation with Infinity gives Infinity as a result:

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; Infinity;</li>
  <li style="margin-bottom: 0px;">Infinity</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof Infinity;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; 1e309;</li>
  <li style="margin-bottom: 0px;">Infinity</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; 1e308;</li>
  <li style="margin-bottom: 0px;">1e+308</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; var a = 6 / 0;</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; a;</li>
  <li style="margin-bottom: 0px;">Infinity</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; var i = -Infinity;</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; i;</li>
  <li style="margin-bottom: 0px;">-Infinity</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; typeof i;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  </ol></div><br/>

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; Infinity - Infinity;</li>
  <li style="margin-bottom: 0px;">NaN</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; -Infinity + Infinity;</li>
  <li style="margin-bottom: 0px;">NaN</li>
  </ol></div><br/>

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; Infinity - 20;</li>
  <li style="margin-bottom: 0px;">Infinity</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; -Infinity * 3;</li>
  <li style="margin-bottom: 0px;">-Infinity</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; Infinity / 2;</li>
  <li style="margin-bottom: 0px;">Infinity</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; Infinity - 9999999999999;</li>
  <li style="margin-bottom: 0px;">Infinity</li>
  </ol></div>

Examples with `NaN`:

  `NaN` is a special value and its type is "Number"!

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; typeof NaN;</li>
  <li style="margin-bottom: 0px;">"number"</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; var a = NaN;</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; a;</li>
  <li style="margin-bottom: 0px;">NaN</li>
  </ol></div><br/>

  <div><ol style="list-style-type: decimal;">
  <li style="margin-bottom: 0px;" value="1">&gt; var a = 10 * "f";</li>
  <li style="margin-bottom: 0px;">undefined</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; a;</li>
  <li style="margin-bottom: 0px;">NaN</li>
  <li style="margin-bottom: 0px;">&nbsp;</li>
  <li style="margin-bottom: 0px;">&gt; 1 + 2 + a;</li>
  <li style="margin-bottom: 0px;">NaN</li>
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

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; 0.1 + 0.2;</li>
<li style="margin-bottom: 0px;">0.30000000000000004</li>
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
  + __octal__: `010 = 8`, `0456 = 4 * 8^2 + 5 * 8^1 + 6 * 8^0`; starting w/ `0` w/ all numbers `0` ~ `7`
  + __hexadecimal__: `0xF3`
  + special values
    + `+Infinity`
      + all number values greater than `1.79769313486231570e+308`
      + `1/0` $\to$ `Infinity`, `-1/0` $\to$ `-Infinity`
      + `typeof Infinity` $\to$ number
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

<div><ol>
<li style="margin-bottom: 0px;" value="1">typeof 'world';</li>
</ol></div>

A binary operator is applied to two different expressions, and is both prefixed and suffixed.

__Binary operator example:__

<div><ol>
<li style="margin-bottom: 0px;" value="1">var x = 45 / 32;</li>
</ol></div>

The division operator is binary.

Within an expression, we can also use parentheses to force the execution of the expression inside. Parentheses can be used to indicate precedence.

For example, this is an expression: `(3 + 2)`. And the expression `(3 + 2) * 4`, which equals 20, depends on the expression within the parentheses.

In JavaScript, expressions can evaluate to four types, which are: `numbers`, `strings`, `booleans`, and `objects`. For example, an expression with the operator - will evaluate to a `number`. But an expression with the operator + can evaluate to a `number` or a `string` (for addition or concatenation).


#### Notes for 1.5.5 JS operators and expressions

+ Expression
  + a small piece of code used to produce a value, eg,. `3 + 5` & `11`
  + within an expression, find values, variables, operators, and expressions
  + using parentheses to force the execution of the expression inside
  + parentheses used to indicate precedence, eg, `(3 + 2)`, `(3 + 2) * 4`
  + evaluate to four types: `numbers`, `strings`, `booleans`, and `objects`

+ Operators
  + unary operator
    + applied to one expression
    + prefixed or suffixed
    + example: `typeof 'world';`
  + binary operator
    + applied to different expressions
    + both prefixed and suffixed
    + example: `var x = 45/32;`
  + ternary  operator
    + `(condition) ? 'something' : 'others'`
    + example: `var kindergarten_eligible = (age < 5) ? "Too young" : socially_ready`


### 1.5.6 Number operators

#### Live coding video: number operators

<a href="https://edx-video.net/W3CJSIXX2016-V001800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y4vjwthw)


The following arithmetic operators are __binary__:

`+`, `-` , `/`, `*`, `%` (modulo)

Example: 7 % 5 equals 2, which is the remainder of the integer division of 7 by 5

Note: (7 / 5 = 5 * 1 + 2 ).


And there are also __unary__ operators:

`++`, `--`, `-` (the opposite of a number)

`++` and `--` operators increment or decrement the value of a variable. They can be both prefixed or suffixed, which have different effects:

+ Suffixed `++` adds one to the value of the variable, then returns the old value.
+ Prefixed `++` also adds one to the value, but returns the new value. Both of these must be used with variables.

#### Examples typed in the devtool console of a browser

__Example #1: simple operator use__

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; 1 + 2;</li>
<li style="margin-bottom: 0px;">3</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var a = 1;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var b = 2;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a + 1;</li>
<li style="margin-bottom: 0px;">2</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; b + 2;</li>
<li style="margin-bottom: 0px;">4</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a + b;</li>
<li style="margin-bottom: 0px;">3</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var c = a + b;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; c;</li>
<li style="margin-bottom: 0px;">3</li>
</ol></div>

__Example #2: more operators__

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; 1 + 2;</li>
<li style="margin-bottom: 0px;">3</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; 99.99 - 11;</li>
<li style="margin-bottom: 0px;">88.99</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; 2 * 3;</li>
<li style="margin-bottom: 0px;">6</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; 6 / 4;</li>
<li style="margin-bottom: 0px;">1.5</li>
</ol></div>

__Example #3: pre and post increments__

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var m = 0;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; m;</li>
<li style="margin-bottom: 0px;">0</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; // regular use of the + operator</li>
<li style="margin-bottom: 0px;">m = m + 1;</li>
<li style="margin-bottom: 0px;">1</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; m;</li>
<li style="margin-bottom: 0px;">1</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; m = m + 1;</li>
<li style="margin-bottom: 0px;">2</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; m;</li>
<li style="margin-bottom: 0px;">2</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; // post increment</li>
<li style="margin-bottom: 0px;">m++;</li>
<li style="margin-bottom: 0px;">2</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; m;</li>
<li style="margin-bottom: 0px;">3</li>
<li style="margin-bottom: 0px;">&gt; console.log(m++); // will display 3 but after that m is incremented</li>
<li style="margin-bottom: 0px;">3</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; m;</li>
<li style="margin-bottom: 0px;">4</li>
</ol></div>

Below is snapshot with explanations:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2wd75ds')"
    src    ="https://tinyurl.com/y54daal5"
    alt    ="pre and post increments, image with the code above, but with arrows pointing to each line and comments associated (same comments are in the code above)"
    title  ="pre and post increments, image with the code above, but with arrows pointing to each line and comments associated (same comments are in the code above)"
  />
</figure>


__Example #4: other versions of post and pre increments__

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var a = 123; var b = a++;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; b;</li>
<li style="margin-bottom: 0px;">123</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a;</li>
<li style="margin-bottom: 0px;">124</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var a = 123; var b = ++a;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; b;</li>
<li style="margin-bottom: 0px;">124</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a;</li>
<li style="margin-bottom: 0px;">124</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var a = 123; var b = a--;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; b;</li>
<li style="margin-bottom: 0px;">123</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a;</li>
<li style="margin-bottom: 0px;">122</li>
</ol></div>

__Example #5: short variant that mixes assignment and execution of an operator__

Binary operators can be used with a shorter syntax when we want to assign the resulting value to a variable at the same time.

Code below (try it in the devtool console of your browser):

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt;&nbsp;var a = 10;</li>
<li style="margin-bottom: 0px;">&gt;&nbsp;a *= 5; // equivalent to a = a * 5;</li>
<li style="margin-bottom: 0px;">&gt;&nbsp;console.log(a);</li>
<li style="margin-bottom: 0px;">&gt;&nbsp;50</li>
</ol></div>

__Example #6: more with pre operators +=, -=, *=, /=__

There are good chances you will encounter such code:

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var a = 5;</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a += 3 // equivalent to a = a + 3;</li>
<li style="margin-bottom: 0px;">8</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a -= 2; // equivalent to a = a - 2;</li>
<li style="margin-bottom: 0px;">6</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a *= 10; // equivalent to a = a * 10;</li>
<li style="margin-bottom: 0px;">60</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a /= 5; // equivalent to a = a / 5;</li>
<li style="margin-bottom: 0px;">12</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; a %= 2; // equivalent to a = a % 2;</li>
<li style="margin-bottom: 0px;">0</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; // this is normal, as a is even</li>
</ol></div>


#### Notes for 1.5.6 Number operators

+ Numeric operators
  + binary
    + operators: `+`, `-` , `/`, `*`, `%`
    + example: `7 % 5;` $\to$ 2; `1 + 2;` $\to$ 3; 
  + unary operator
    + operators: `++`, `--`, `-` (opposite of a number, negative)
    + suffix `++`: adding one to the variable, then return the old value
    + prefix `++`: adding one tot he variable, then return the new value
    + example: `let x = 3; let a = 123;`
      + `console.log(x++); x;` $\to$ print 3 and x = 4
      + `console.log(++x); x;` $\to$ print 4 and x = 4
      + `var b = a++; b; a;` $\to$ 123, 124
      + `var b = ++a; b; a;` $\to$ 124, 124
      + `var b = a--; b; a;` $\to$ 123, 122
  + mixing assignment
    + binary operator used w/ a shorter syntax when assigning the resulting value to a variable
    + pre operators: `+=`, `-=`, `*=`, `/=`, `%=`
    + example: `let a = 10; a *= 5;` equivalent to `a = a * 5`


### 1.5.7 Strings (part 1)

To declare or manipulate strings you must write them with __single quotes ' or double quotes "__ around them. Single quotes or double quotes are both accepted, and there is no difference between them in JavaScript. However, the community prefers to use single quote for string - this is not a convention, but a recommendation.

And finally, you cannot start a string with a single and end with a double quotes, or the opposite.

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; "Hello World";</li>
<li style="margin-bottom: 0px;">"Hello World"</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; "JavaScript Course";</li>
<li style="margin-bottom: 0px;">"JavaScript Course"</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; 'With simple quotes';</li>
<li style="margin-bottom: 0px;">"With simple quotes"</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; "Do not mix double and simple quotes'; // here we opened the string with double and closed with simple quotes</li>
<li style="margin-bottom: 0px;">VM24763:1 Uncaught SyntaxError: Invalid or unexpected token</li>
</ol></div>

Image from the devtool console, from the above example:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2exgnkp')"
    src    ="https://tinyurl.com/y4z2ll2x"
    alt    ="Snapshot of a devtool console: do not mix simple and double quotes"
    title  ="Snapshot of a devtool console: do not mix simple and double quotes"
  />
</figure>


There are many reasons to use simple quotes when possible:

1. Double quotes are used in HTML
1. You must hold the Shift key to type "
1. Single quotes are easier to read and to type
1. To output HTML in JavaScript, single quotes are more useful


#### Notes for 1.5.7 Strings (part 1)

+ Strings
  + text surrounded by single quote `'` or double quote `"`
  + no difference btw single quote and double quote
  + single and double quotes must be shown in pair
  + community preference: single quote for string
  + using double quote if text consisting at least a single quote
  + example: `"Hello World";`,  `'With simple quotes';`, `"It's my pleasure.";`


#### Knowledge check 1.5.7

1. How would you give this value to the string variable s: I'm the king of the world?

  a. 'I/'m the king of the world'<br/>
  b. "I'm the king of the world"<br/>
  c. I"'"m the king of the world<br/>

  Ans: b<br/>
  Explanation: When a string contains at least a single quote, use double quotes at the beginning and at the end of the string value.


### 1.5.8 String operators

#### Live coding video: strings and string operators

<a href="https://edx-video.net/W3CJSIXX2016-V002400_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y3cyzyr6)

#### Introduction to string operators

##### The concatenation operator (`+`)

The operator (`+`) used with strings is called the concatenation operator, and it allows you to concatenate strings.

<div><ol>
<li style="margin-bottom: 0px;" value="1">//the operator (+)</li>
<li style="margin-bottom: 0px;">var s1 = 'one';</li>
<li style="margin-bottom: 0px;">var s2= 'two';</li>
<li style="margin-bottom: 0px;">var s = s1 + s2;</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">s;</li>
<li style="margin-bottom: 0px;">// returns 'onetwo'</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">typeof s; </li>
<li style="margin-bottom: 0px;">//'string'</li>
</ol></div>

##### The shorthand assignment operator (`+=`)

The shorthand assignment operator (`+=`) can also be used to concatenate strings.

<div><ol>
<li style="margin-bottom: 0px;" value="1">//the assignment operator (+=)</li>
<li style="margin-bottom: 0px;">var s1 = 'one';</li>
<li style="margin-bottom: 0px;">var s2 = 'two';</li>
<li style="margin-bottom: 0px;">s1+= s2; // or directly s1+='two'</li>
<li style="margin-bottom: 0px;">s1; </li>
<li style="margin-bottom: 0px;">//returns 'onetwo'</li>
</ol></div>


##### The method `concat()`

Another way to concatenate strings is the method `concat()`.

<div><ol>
<li style="margin-bottom: 0px;" value="1">//the 'concat' method</li>
<li style="margin-bottom: 0px;">var s1 = 'one';</li>
<li style="margin-bottom: 0px;">var s2 ='two';</li>
<li style="margin-bottom: 0px;">var s = s1.concat(s2); </li>
<li style="margin-bottom: 0px;">s;</li>
<li style="margin-bottom: 0px;">//returns 'onetwo'</li>
</ol></div>

All the methods shown above can be used with a variable number of arguments:

<div><ol>
<li style="margin-bottom: 0px;" value="1">var s1 = 'Hello'; </li>
<li style="margin-bottom: 0px;">s1 = s1 + ' World' + ' JavaScript'; </li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">var s2 = 'Hello'; </li>
<li style="margin-bottom: 0px;">s2+= ' World' + ' JavaScript'; </li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">var s3 = 'Hello'; </li>
<li style="margin-bottom: 0px;">s3.concat(' World' , ' JavaScript' );</li>
<li style="margin-bottom: 0px;"> </li>
<li style="margin-bottom: 0px;">//s1,s2 and s3 return 'Hello World JavaScript'</li>
</ol></div>

#### Converting strings

A String number in an arithmetic expression is converted to Number, unless the formula is a pure addition.

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var s = '1'; s = 3 * s; typeof s;</li>
<li style="margin-bottom: 0px;">"number"</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; s;</li>
<li style="margin-bottom: 0px;">3</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var s = '1'; s++; typeof s;</li>
<li style="margin-bottom: 0px;">"number"</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; s;</li>
<li style="margin-bottom: 0px;">2</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var s = "100"; typeof s;</li>
<li style="margin-bottom: 0px;">"string"</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; s = s * 1;</li>
<li style="margin-bottom: 0px;">100</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; typeof s;</li>
<li style="margin-bottom: 0px;">"number"</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; var d = "101 dalmatians";</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&nbsp;</li>
<li style="margin-bottom: 0px;">&gt; d * 1;</li>
<li style="margin-bottom: 0px;">NaN</li>
</ol></div>

The above example is shown in the devtools console:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y4c4q75a')"
    src    ="https://tinyurl.com/y4xth3vg"
    alt    ="Devtool console showing var s = '1'; s = 3 * s; typeof s; `number` s 3 var s = '1'; s++; typeof s; `number` s 2 var s = `100`; typeof s; `string` s = s * 1; 100 typeof s; `number` var d = '101 dalmatiens'; undefined d * 1 NaN"
    title  ="Devtool console showing var s = '1'; s = 3 * s; typeof s; `number` s 3 var s = '1'; s++; typeof s; `number` s 2 var s = `100`; typeof s; `string` s = s * 1; 100 typeof s; `number` var d = '101 dalmatiens'; undefined d * 1 NaN"
  />
</figure>


##### How to convert a Number into a String

There is trick for converting a Number into a String: we concatenate with an empty string, at the beginning of expression (type this in the devtools):

<div><ol>
<li style="margin-bottom: 0px;" value="1">var n = 1;</li>
<li style="margin-bottom: 0px;">typeof n;</li>
<li style="margin-bottom: 0px;">// returns "number"</li>
<li style="margin-bottom: 0px;">n = "" + n;</li>
<li style="margin-bottom: 0px;">// returns "1"</li>
<li style="margin-bottom: 0px;">typeof n;</li>
<li style="margin-bottom: 0px;">// returns "string"</li>
</ol></div>


#### Special characters

##### Special character: the "\\"

The `\` is useful for "escaping" special characters. Here are a few examples:

<div><ol>
<li style="margin-bottom: 0px;" value="1">var s = 'I don\'t know';</li>
<li style="margin-bottom: 0px;">var s = "I don\'t know"; // here the&nbsp;\ is useless</li>
<li style="margin-bottom: 0px;">var s = "I don't know"; &nbsp;// same result as previous line</li>
<li style="margin-bottom: 0px;">var s = '"Hello", he said.'; // ok, double quotes inside single one will be displayed</li>
<li style="margin-bottom: 0px;">var s = "\"Hello\", he said."; // double quotes inside double quotes need to be escaped</li>
</ol></div>


##### Escaping the escape! Use a double "\\"

<div><ol>
<li style="margin-bottom: 0px;" value="1">var s = "1\\2"; s;</li>
<li style="margin-bottom: 0px;">// returns "1\2"</li>
</ol></div>

##### Special characters starting with "\\"

__"\n" for "next line":__

<div><ol>
<li style="margin-bottom: 0px;" value="1">var s = '\n1\n2\n3\n';</li>
<li style="margin-bottom: 0px;">s</li>
<li style="margin-bottom: 0px;">// returns "</li>
<li style="margin-bottom: 0px;"> 1</li>
<li style="margin-bottom: 0px;"> 2</li>
<li style="margin-bottom: 0px;"> 3</li>
<li style="margin-bottom: 0px;"> "</li>
</ol></div>

__"\r" for "carriage return":__

<div><ol>
<li style="margin-bottom: 0px;" value="1">var s = '1\r2';</li>
<li style="margin-bottom: 0px;">var s = '1\n\r2';</li>
<li style="margin-bottom: 0px;">var s = '1\r\n2';</li>
<li style="margin-bottom: 0px;">// the three previous lines give :</li>
<li style="margin-bottom: 0px;"> "1</li>
<li style="margin-bottom: 0px;"> 2"</li>
</ol></div>

__"\t" for "insert a tabulation":__

<div><ol>
<li style="margin-bottom: 0px;" value="1">var s = "1\t2"</li>
<li style="margin-bottom: 0px;">// s is equal to</li>
<li style="margin-bottom: 0px;"> "1 2"</li>
</ol></div>


#### Notes for 1.5.8 String operators

+ String concatentation
  + concatenation operator: `+`
    + used to concatenate two strings
    + examples
      + `let s1 = 'one'; let s2 = 'two'; let s = s1 + s2; s;` $\to$ `'onetwo'`
      + `let s1 = 'Hello'; let s1 = s1 + 'World' + 'JavaAScript'; s1` $\to$ `"Hello World JavaScript"`
  + shorthand assignment operator `+=`
    + used to concatenate strings
    + examples
      + `let s1 = 'one'; let s2 = 'two'; s1 += s2; s1;` $\to$ `'onetwo'`
      + `var s2 = 'Hello'; s2+= ' World' + ' JavaScript'; s2;` $\to$ `"Hello World JavaScript"`
  + method `concat()`
    + another way to concatentate strings
    + examples
      + `let s1 = 'one'; let s2 = 'two'; let s = s1.concat(s2); s;` $\to$ 'onetwo'
      + `var s3 = 'Hello'; s3.concat(' World' , ' JavaScript' );` $\to$ `"Hello World JavaScript"`

+ String Number conversion
  + string number to number
    + String number in an arithmetic expression converted  to Number
    + examples:
      + `var s = '1'; s = 3 * s; typeof s;` & `s;` $\to$ `"number"` & `3`
      + `var s = '1'; s++; typeof s;` & `s;` $\to$ `"number"` & `2`
      + `var s = "100"; typeof s;` & `s = s * 1;` $\to$ `"string"` & `100`
      + `var d = "101 dalmatians"; d * 1;` $\to$ `NaN`
  + converting number into a string
    + concatentate w/ an empty string at the beginning of expression
    + example: `var n = 1; typeof n;`, `n = "" + n;`, `typeof n;` $\to$ `"number"`, `"1"`, `"string"`

+ Special characters
  + escaping special character: `\`
    + examples: `var s = 'I don\'t know';`, `var s = "I don\'t know"; // here the \ is useless`, `var s = '"Hello", he said.';`, `var s = "\"Hello\", he said.";`
  + escaping the escape w/ double `\`: `\\`
    + example: `var s = "1\\2"; s;` $\to$ `"1\2"`
  + special characters starting w/ `\`
    + `\n` for next line
    + `\r` for carriage return
    + `\t` for inserting a tabulation


#### Knowledge check 1.5.8

```js
var s1 = "32";
var s2 = "32";
var sum = s1 + s2;
console.log(sum);
```

1. What value will be displayed in the devtools console?

  a. NaN<br/>
  b. 3232<br/>
  c. 64<br/>

  Ans: b<br/>
  Explanation: s1 and s2 are strings. The + operator will concatenate strings if one of the variables in the expression s1 + s2 is a string, and the result will be a string. The sum variable will be the value "3232" (concatenation of "32" and "32", and not 64 (the addition of two numbers).


### 1.5.9 Objects (part 1)

We have already encountered objects in different examples. You can easily recognize these objects:

+ They are declared using "{" and "}", such as in `var p = {givenName:'Michel', familyName: 'Buffa'}`, `givenName` and `familyName` are called "properties" and `Michel` and `Buffa` are their respective values.
+ We are using the "." operator to access their properties or methods. Example : `daysOfTheWeek.length` (arrays are objects too - special ones, but objects), or `document.body` or `window.innerWidth` (try typing that in the devtool console). There are plenty of predefined objects in JavaScript (`window`, `document`, `navigator`, etc.). We have also used `console.log(...)`, and indeed console is a predefined JavaScript object. With the object `var p = {givenName:'Michel', familyName: 'Buffa'}`, we can access the properties the same way, with: `p.givenName` and `p.familyName`.


#### Take a look at some common objects and properties!

Open your devtool console (F12 or ctrl-alt-i or cmd-alt-i on Mac), go to the console tab and type "window" followed by a ".", normally you should see an auto-completion menu. Start typing "inne" and you should see some possible completions.

Try looking at the values of the size of the current browser window (type `window.innerWidth` followed by the "enter/return" key, type `window.innerHeight`, etc.).

Try looking at the vendor of your browser: type `"navigator.vendor"`, try looking at the current URL displayed in your window: type `window.location`, etc.

We will study these objects later, but for the moment, just play with objects :-)

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; window.innerHeight</li>
<li style="margin-bottom: 0px;">217</li>
<li style="margin-bottom: 0px;">&gt; window.innerWidth</li>
<li style="margin-bottom: 0px;">1704</li>
<li style="margin-bottom: 0px;">&gt; navigator.vendor</li>
<li style="margin-bottom: 0px;">"Google Inc."</li>
</ol></div>


#### You can define your own objects

There are many ways to create your own JavaScript objects. For the moment, let's stick to the simplest one, "singleton objects", and for now all you need to know is that they can have properties that hold values. We will return to objects in Week 4 and cover them in further detail.

<div><ol>
<li style="margin-bottom: 0px;" value="1">var student1 = {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; fullName:'John Doe',</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; age: 23,</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; city: 'New York',</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; ssn: "11-22-33-44" // no comma at the end of the last property</li>
<li style="margin-bottom: 0px;">} &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// declaration</li>
</ol></div>

Accessing an object's properties: we use the operator "."

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; student1.ssn</li>
<li style="margin-bottom: 0px;">"11-22-33-44"</li>
<li style="margin-bottom: 0px;">&gt; student1.age</li>
<li style="margin-bottom: 0px;">23</li>
<li style="margin-bottom: 0px;">&gt; student1</li>
<li style="margin-bottom: 0px;">[object Object] {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; age: 23,</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; city: "New York",</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; fullName: "John Doe",</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; ssn: "11-22-33-44"</li>
<li style="margin-bottom: 0px;">}</li>
</ol></div>


#### Notes for 1.5.9 Objects (part 1)

+ Objects
  + declaration
    + using "{" and "}"
    + properties & values
    + example: `var p = {givenName:'Michel', familyName: 'Buffa'}`
      + property: `givenname` & `familyname`
      + values: `'Michel'` & `'Buffa'`
  + accessing properties or method
    + using `.` operator
    + pre-defined objects: `window`, `document`, `navigator`, `console`, etc.
    + examples
      + `daysOfTheWeek.length`: array property
      + `document.body` or `window.innerWidth`
      + `console.log(...)`

+ Common objects & properties
  + auto-completion w/ `.` to display options in devtools console tab
  + the size of current browser window: `window.innerWidth` & `window.innerHeight`
  + current URL w/ the page: `window.location`
  + vendor of browser: `navigator.vender`

+ Defining singleton objects

  ```js
  var student1 = {
      fullName:'John Doe',
      age: 23,
      city: 'New York',
      ssn: "11-22-33-44" // no comma at the end of the last property
  }

  student1.ssn;     // 11-22-33-44
  student1.age;     // 23
  student1
  // [object Object] {
  //     age: 23,
  //     city: "New York",
  //     fullName: "John Doe",
  //     ssn: "11-22-33-44"
  // }
  ```

#### Knowledge check 1.5.9

1. Which of these are predefined objects that you can use in your JS code when running in a browser environment (three correct answers!)

  a. browser<br/>
  b. navigator<br/>
  c. htmlDocument<br/>
  d. document<br/>
  e. window<br/>
  
  Ans: bde<br/>
  Explanation: If you type the names of these objects in the devtool console, you can easily check that `navigator`, `window` and `document` do exist, while `browser` and `htmlDocument` will give errors.


### 1.5.10 Arrays (part 1)

#### Definition: arrays are containers with indexes 

Arrays are a special datatype. You declare arrays using brackets, like this:

<div><ol>
<li style="margin-bottom: 0px;" value="1">var daysOfWeek = [];</li>
</ol></div>

You can fill them at declaration time:

<div><ol>
<li style="margin-bottom: 0px;" value="1">var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];</li>
<li style="margin-bottom: 0px;">var gradesInMaths = [12, 7, 14, 18, 9, 11];</li>
</ol></div>

#### Elements in an array can be accessed using indexes

Each element in an array has an index. <span style="color: brown; font-weight: bold;">The first element's index is 0, the second element's index is 1 etc.

To access an element, you use the array variable and "[" followed by the index value followed by "]", as shown in these examples:

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek[0]</li>
<li style="margin-bottom: 0px;">"Monday"</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek[1]</li>
<li style="margin-bottom: 0px;">"Tuesday"</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek[2]</li>
<li style="margin-bottom: 0px;">"Wednesday"</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek.length</li>
<li style="margin-bottom: 0px;">7</li>
</ol></div>

#### Use the length property of an array to know its length

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday'];</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek.<strong>length</strong></li>
<li style="margin-bottom: 0px;"><strong>7</strong></li>
</ol></div>

Indeed, there are seven days in a week and the daysOfWeek array has seven elements, indexed from 0 to __daysOfWeek.length -1__

<p style="border: 1px solid; text-align: center; margin: 20px; padding: 20px;"><strong><span style="color: #ff0000;">This way of enumerating all elements (from 0 to the length of the array -1) is very, very common, and will prove to be very useful when you learn how to iterate on an array's elements (Week 2).</span></strong></p>


#### You can add elements to an array using a new index

If you want to add a new element at the end of an array, use the index equal to the length of the array

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek.length</li>
<li style="margin-bottom: 0px;">6</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek[6]</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">// NO ELEMENT AT INDEX 6 in an array of 6 elements, first index is 0 // last 6-1 = 5</li>
<li style="margin-bottom: 0px;"><span style="color: #000088;" color="#000088">&gt;&nbsp;</span>daysOfWeek[6] = 'Sunday'</li>
<li style="margin-bottom: 0px;">"Sunday"</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek.length</li>
<li style="margin-bottom: 0px;">7</li>
<li style="margin-bottom: 0px;">// Sunday, the 7th day of week is at index 6 !</li>
</ol></div>


#### Arrays are JavaScript objects!

Well, this is not so important for the moment, but look:

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var a = [];</li>
<li style="margin-bottom: 0px;">&gt;&nbsp;<strong>typeof a;</strong></li>
<li style="margin-bottom: 0px;"> <strong>"object"</strong></li>
<li style="margin-bottom: 0px;">&gt; var a = [1,2,3];</li>
<li style="margin-bottom: 0px;">&gt;&nbsp;a</li>
<li style="margin-bottom: 0px;"> [1, 2, 3]</li>
<li style="margin-bottom: 0px;">&gt;&nbsp;a[0]</li>
<li style="margin-bottom: 0px;"> 1</li>
<li style="margin-bottom: 0px;">&gt; a[1]</li>
<li style="margin-bottom: 0px;"> 2</li>
</ol></div>

And indeed, when you write daysOfWeek.length, you are using the array as an object, and you are using the length property of array objects.


#### Add an element at the end of an array using the push method

Since arrays are objects, we can do much more with them - in particular, they have more properties and more methods than the push method. You will learn more about this in a later lesson (Arrays part 2), but for the moment, let's focus on the most useful features...

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];</li>
<li style="margin-bottom: 0px;">undefined</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek.length</li>
<li style="margin-bottom: 0px;">6</li>
<li style="margin-bottom: 0px;"><strong>&gt; daysOfWeek.push('Sunday');</strong></li>
<li style="margin-bottom: 0px;">7</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek</li>
<li style="margin-bottom: 0px;">["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]</li>
<li style="margin-bottom: 0px;">&gt; daysOfWeek.length</li>
<li style="margin-bottom: 0px;">7</li>
</ol></div>


#### Arrays and Strings

Strings are arrays of characters! 

Consequence:

1. They are objects too!
1. They have a length property,
1. Each individual character can be accessed using an index.

Examples:

<div><ol>
<li value="1">&gt; var s = 'one';</li>
<li>&gt; s[0]</li>
<li> "o"</li>
<li>&gt; s[1];</li>
<li> "n"</li>
<li>&gt; s[2];</li>
<li> "e"</li>
<li>&gt; s.length;</li>
<li> 3</li>
</ol></div>

#### Notes for 1.5.10 Arrays (part 1)

+ Arrays
  + definition: containers w/ indexes
  + declaration w/ `[]`
    + examples: `var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];`, `var gradesInMaths = [12, 7, 14, 18, 9, 11];`
  + access using indexes
    + 1st element index: 0
    + accessing w/ `[#]` where `#` as the index
    + example
      + `var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunda'];`
      + `daysOfWeek[0];`, `daysOfWeek[1];`, `daysOfWeek[2]` $\to$ `"Monday"`, `"Tuesday"`, `"Wednesday"`
  + array length
    + `length` property
    + example: `var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunda']; daysOfWeek.length` $\to$ `7`
  + index range: `[0, daysOfWeek.length - 1]`
  + strings: arrays of characters
    + objects
    + w/ length property
    + using index to access individual character


#### Knowledge check 1.5.10

`var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];`

1. Which element of the daysOfWeek array contains 'Wednesday'?

  a. `daysOfWeek[2]`<br/>
  b. `daysOfWeek['Wednesday']`<br/>
  c. `daysOfWeek[3]`<br/>

  Ans: a<br/>
  Explanation: In JavaScript, arrays have elements with an index starting at 0. So 'Wednesday' is in the third element, whose index is 3-1 = 2;


### 1.5.11 Functions (part 1)

#### Definition of a function
A function allows you to group code, give it a name and be able to execute it by calling it by name.

Functions always return a value:

+ Explicitly, using the keyword `return` followed by the value (_line 3_ of the next example),
+ Implicitly, in which case the return value is `undefined`.

#### Declaring a function

<div><ol>
<li style="margin-bottom: 0px;" value="1">function sum(a, b) {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; var c = a + b;</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; return c;</li>
<li style="margin-bottom: 0px;">} </li>
</ol></div>

#### Calling a function

<div><ol>
<li style="margin-bottom: 0px;" value="1"> var result = sum(1, 2);</li>
<li style="margin-bottom: 0px;">//result is equal to&nbsp;3</li>
<li style="margin-bottom: 0px;">console.log(result)</li>
<li style="margin-bottom: 0px;">&gt; 3</li>
</ol></div>


#### Function parameters

If parameters are omitted during the call, JavaScript gives them the value undefined:

<div><ol>
<li style="margin-bottom: 0px;" value="1">&gt; sum(1)</li>
<li style="margin-bottom: 0px;"> NaN </li>
</ol></div>


##### Functions with a variable number of parameters

An array named "arguments" is created automatically in each function, it contains all the call parameters of the function:

<div><ol>
<li style="margin-bottom: 0px;" value="1">function f() { </li>
<li style="margin-bottom: 0px;" value="1">&nbsp; &nbsp;return arguments; </li>
<li style="margin-bottom: 0px;" value="1">}</li>
<li style="margin-bottom: 0px;">...</li>
<li style="margin-bottom: 0px;"> f();</li>
<li style="margin-bottom: 0px;">// returns []</li>
<li style="margin-bottom: 0px;">...</li>
<li style="margin-bottom: 0px;"> f( 1, 2, 3, 4, true, 'Michel Buffa');</li>
<li style="margin-bottom: 0px;">// returns [1, 2, 3, 4, true, "Michel Buffa"]</li>
</ol></div>


##### Example of the sum with a variable number of arguments

<div><ol>
<li style="margin-bottom: 0px;" value="1">function newSum() {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; var i, res = 0;</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; var&nbsp;numberOfParameters&nbsp;= arguments.length;</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; for (i = 0; i &lt;&nbsp;numberOfParameters; i++) {</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; &nbsp;res += arguments[i];</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; }</li>
<li style="margin-bottom: 0px;">&nbsp; &nbsp; return res;</li>
<li style="margin-bottom: 0px;">}</li>
<li style="margin-bottom: 0px;">...</li>
<li style="margin-bottom: 0px;">&gt;&gt;&gt;&nbsp;newSum(1, 1, 1);</li>
<li style="margin-bottom: 0px;"> 3</li>
<li style="margin-bottom: 0px;">&gt;&gt;&gt;&nbsp;newSum(1, 2, 3, 4);</li>
<li style="margin-bottom: 0px;">10</li>
</ol></div>


#### Notes for 1.5.11 Functions (part 1)

+ Functions
  + grouping code, providing name and accessing by calling the given name
  + always returning a value
    + explicitly, using the keyword `return` followed by the value
    + implicitly, returning value is `undefined`
  + declaring a function, e.g.,

    ```js
    function sum(a, b) {
        var c = a + b;
        return c;
    }
    ```

  + calling a function: `var result = sum(1, 2);`, `console.log(result);` $\to$ `3`

+ Function parameters
  + __arguments__
    + an array created automatically in each function
    + containing all the call parameters of the function
  + omitted during the call, JavaScript providing the value `undefined`
  + a various number of parameters

    ```js
    function f() {
      return arguments;
    }
    ...
    f();    // returns []
    ...
    f( 1, 2, 3, 4, true, 'Michel Buffa');
    // returns [1, 2, 3, 4, true, "Michel Buffa"]
    ```


#### Knowledge check 1.5.11

```js
function f() {
  // get the parameters
  var allCallParameters = XXX;
  // do something with the parameters
  // ...
}
```

1. A JavaScript function can have a variable number of parameters. What is the name of the array that is created automatically in each function, and that contains the call parameters (what would you write instead of XXX in the code above)?

  a. arguments<br/>
  b. params<br/>
  c. parameters<br/>

  Ans: a<br/>
  Explanation: An array named arguments is created automatically in each function, it contains all the call parameters of the function.



