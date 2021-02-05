# Module 2: Adding interactivity to HTML documents

## 2.2 Conditional statements, loops and logical operators


### 2.2.1 Boolean values and logical operators

#### Live coding video: boolean value, if...else statement and comparison operators

<a href="https://edx-video.net/W3CJSIXX2016-V002500_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y479f5az)

##### Source code of the example shown in the video

[CodePen Demo](https://codepen.io/w3devcampus/pen/pPmqwq?editors=0012)

[Local Demo](src/js/02b-example01.js)

Before talking about how your JavaScript program can make decisions, such as "_if this condition is fulfilled then I'll do this, otherwise I'll do that..._", we need to define a few more concepts.

Let's tart with "boolean values" and "logical operators".


#### Boolean values

The __boolean__ type represents a logical entity having two values: `true` and `false`.

Use of the keywords true and false:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
</ol></div>

A boolean variable should not be enclosed in quotation marks, otherwise it becomes a string variable:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="str">'true'</span><span class="pun">;</span><span class="pln"> </span><span class="com">// b is not a boolean but a string</span></li>
</ol></div>

#### Undefined and null values

__Undefined__

undefined is returned when a variable has not been assigned:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> foo</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> foo</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> foo</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="str">'undefined'</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">foo </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'The variable foo has no value and is undefined'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="str">'The variable foo has no value and is undefined'</span></li>
</ol></div>

The above example shows how we can test whether a variable has a value (_line 8_ uses a conditional statement).

The keyword "__undefined__" is part of the JavaScript language, so you can assign the `undefined` value to a variable:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">var</span><span class="pln"> foo </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">undefined</span><span class="pun">;</span><span class="pln"> </span><span class="com">// equivalent to var foo; without giving any value</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> foo</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">undefined</span></li>
</ol></div>

`var foo;` and `var foo = undefined;` are equivalent but we recommend that you use the first version to declare the variable (it is shorter, and that reduces the code).

If you try to access a variable that has not been declared before, a `ReferenceError` will be raised. But the typeof operator will return "`undefined`":

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&gt;</span><span class="pln"> bar</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="typ">ReferenceError</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">&gt;</span><span class="pln"> </span><span class="kwd">typeof</span><span class="pln"> bar</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="str">'undefined'</span></li>
</ol></div>


#### Logical operators

The logical operators are: 

+ `&&` (AND): usage example: 

  ```js
  if ((x  > 0) && (x < 10)) {
      console.log('x is strictly positive and less than 10');
  }
  ```

+ `||` (OR): usage  example 

  ```js
  if ((x  > 0) || (x == -5)) { 
      console.log('x is positive or equal to -5'); 
  }
  ```

+ `!` (NOT): usage example

  ```js
  if (!(x  > 0)) { 
      console.log('x is not positive (x is less or equal to 0'); 
  }
  ```
            
+ `&&`, `||` operators are binary, `!` is unary.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="pun">!</span><span class="kwd">true</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">b</span><span class="pun">;</span><span class="pln"> </span><span class="com">//false</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="pun">!!</span><span class="kwd">true</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">b</span><span class="pun">;</span><span class="pln"> </span><span class="com">//true</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="str">"one"</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">!</span><span class="pln">b</span><span class="pun">;</span><span class="pln"> &nbsp; </span><span class="kwd">false</span><span class="pln"> </span><span class="com">// implicit conversion of "one" to a boolean value</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="str">"one"</span><span class="pun">;</span><span class="pln"> </span><span class="com">// implicit conversion of "one" to a boolean value</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">!!</span><span class="pln">b</span><span class="pun">;</span><span class="pln"> </span><span class="com">//true</span></li>
</ol></div>

In an expression with logical operators, as shown in _lines 8_ and _11_ of the previous example, non-boolean values are implicitly converted to boolean.


##### Lazy evaluation or short-circuit evaluation

Logical expressions are evaluated from left to right. JavaScript uses a mechanism known as "short-circuit evaluation" to prevent the second, third, and nth conditions from being tested in certain cases: 

+ `false &&` something (an expression)  is always false, and the part to the right of `&&` operator is not tested.
+ `true ||` something (an expression) is evaluated to true, and the part to the right of the `||` operator is not tested.

Examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> b </span><span class="pun">=</span><span class="pln"> </span><span class="lit">5</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> c </span><span class="pun">=</span><span class="pln"> </span><span class="lit">6</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">((</span><span class="pln">b </span><span class="pun">===</span><span class="pln"> </span><span class="lit">5</span><span class="pun">)</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> </span><span class="pun">(</span><span class="pln">b </span><span class="pun">===</span><span class="pln"> </span><span class="lit">6</span><span class="pun">))</span><span class="pln"> &nbsp;</span><span class="pun">{</span><span class="pln"> </span><span class="com">//the second part is never tested</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'b is equal to 5 or equal to 6'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">((</span><span class="pln">b </span><span class="pun">===</span><span class="pln"> </span><span class="lit">5</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="pun">(</span><span class="pln">c </span><span class="pun">===</span><span class="pln"> </span><span class="lit">6</span><span class="pun">)</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> &nbsp;</span><span class="com">// second part is evaluated</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'b &nbsp;is equal to 5 and c is equal to 6'</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">((</span><span class="pln">b </span><span class="pun">===</span><span class="pln"> </span><span class="lit">15</span><span class="pun">)</span><span class="pln">&nbsp;</span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="pun">(</span><span class="pln">c </span><span class="pun">===</span><span class="pln"> </span><span class="lit">6</span><span class="pun">)</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> &nbsp;</span><span class="com">// second part is&nbsp;never evaluated</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'b &nbsp;is equal to 5 and c is equal to 6'</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'b not equal to&nbsp;15 or c not equal&nbsp;to 6'</span><span class="pun">);</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

##### Implicit conversions of non boolean values in expressions

Used with logical operators or within statements, __non-boolean values are implicitly converted to booleans__.  

<span style="color: brown; font-weight: bold;">All the following values are evaluated as false:</span>

+ __false__
+ __undefined__
+ __null__
+ __0__
+ __NaN__
+ __the empty string: '' or ""__

<span style="color: brown; font-weight: bold;">Everything else is evaluated as true!</span>

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> boo </span><span class="pun">=</span><span class="pln"> </span><span class="str">'hello'</span><span class="pln"> </span><span class="pun">&amp;&amp;</span><span class="pln"> </span><span class="str">'world'</span><span class="pun">; // boo is equal to 'world' that is 'true'.</span></li>
</ol></div>

In the above example, `'hello' && 'world'` is evaluated as `true` but will return a value! Indeed, `boo` will equal `'world'` because `'hello'` is a string value that is evaluated as `true`. And 'world' is in also true as it's not one of the value cited in the previous paragraph. If we do : if (boo) then.... we will enter the if statement.

The rule is that both `&&` and `||` result in the value of (exactly) one of their operands:

+ A && B returns the value A if A can be coerced into false; otherwise, it returns B.
+ A || B returns the value A if A can be coerced into true; otherwise, it returns B.

External resource: [The && and || Operators in JavaScript](https://mariusschulz.com/blog/the-and-and-or-operators-in-javascript)

__TO SUM UP: it works "normally" if you just think true/false, but the real value affected is not true false, it's one of the operands, that can be seen as true/false.__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">var</span><span class="pln"> boo2 </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="lit">0</span><span class="pun">/</span><span class="lit">0</span><span class="pun">)</span><span class="pln"> </span><span class="pun">||</span><span class="pln"> </span><span class="lit">43.2</span><span class="pln"> </span><span class="pun">;</span></strong></li>
</ol></div>

`boo2` equals 43.2 because the expression 0/0 equals NaN, which is evaluated as `false`.

__Question:__

What is the value of the variable myNumber after the execution of this code?

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> myNumber </span><span class="pun">=</span><span class="pln"> </span><span class="pun">!</span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pun">(</span><span class="pln">myNumber </span><span class="pun">==</span><span class="pln"> </span><span class="kwd">null</span><span class="pun">){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; myNumber </span><span class="pun">=</span><span class="pln"> </span><span class="lit">3</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">myNumber </span><span class="pun">=</span><span class="pln"> myNumber </span><span class="pun">||</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
</ol></div>

__Explanation:__ after the first line, myNumber equals false. In the if statement, at line 3, false does not equal null. Therefore, the value 3 is not assigned to the var myNumber. In the last line, myNumber is evaluated as false, then the value 2 is given to the variable myNumber.


#### Comparison operators

+ Equal `==`
+ Not equal `!=`
+ Greater than `>`
+ Greater than or equal `>=`
+ Less than `<`
+ Less than or equal to `<=`
+ Strict equal `===`
+ Strict not equal `!==`

##### What is the difference between == and === in JavaScript?

__Equal (`==`)__<br/>
  Returns `true` if the operands are strictly equal __with type conversion__.

__Strict equal (`===`)__<br/>
  Returns `true` if the operands are strictly equal __with no type conversion__.

The triple-equals operator never does type coercion. It returns `true` if both operands reference the same object, or in the case of value types, have the same value.

Some examples:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="lit">1</span><span class="pln"> </span><span class="pun">==</span><span class="pln"> </span><span class="lit">1</span><span class="pln"> </span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">//true</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="lit">1 </span><span class="pun">== </span><span class="lit">2</span><span class="pln"> </span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">//false</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">/* Here, the interpreter will try to convert the string ‘1’ </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com"> into a number before doing the comparison */</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="lit">1 </span><span class="pun">== </span><span class="str">'1'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">//true : </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">//with strict equal, no conversion:</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="lit">1 </span><span class="pun">=== </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">//true</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="lit">1 </span><span class="pun">=== </span><span class="str">'1'</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">//false</span></li>
</ol></div>

<div style="border: 1px solid; margin: 20px; padding: 20px; text-align: center;">
<p><strong><span style="color: #ff0000;">Depending on the context, generally strict equal (or strict not equal)&nbsp;is preferred.&nbsp;</span></strong></p>
<p><strong><span style="color: #ff0000;"><span style="text-decoration: underline;">Best practice for beginners</span>: always use === or !== for comparisons.</span></strong></p>
</div>

Here are interesting articles:

+ [Why you should use strict equal](https://www.impressivewebs.com/why-use-triple-equals-javascipt/)
+ [Equality comparisons and sameness](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness)


#### Specific case of NaN

As we have already seen, JavaScript has some special values. One of them is `NaN`: “Not-a-Number”. 

`NaN` has this special property:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">NaN</span><span class="pln"> </span><span class="pun">==</span><span class="pln"> </span><span class="kwd">NaN</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// false</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">NaN</span><span class="pln"> </span><span class="pun">===</span><span class="pln"> </span><span class="kwd">NaN</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// false</span></li>
</ol></div>

__`Nan` is equal to nothing - not even to itself!__ But you do have a function to check the `NaN` value: `isNaN(expr)`

+ `isNaN`: returns true if the argument coerces to NaN, and otherwise returns false.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">isNaN</span><span class="pun">(</span><span class="kwd">NaN</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="com">// true </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">isNaN</span><span class="pun">(</span><span class="lit">0</span><span class="pun">/</span><span class="lit">0</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// true</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">isNaN</span><span class="pun">(</span><span class="lit">12</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">// false</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">isNaN</span><span class="pun">(</span><span class="str">'foo'</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">// true</span></li>
</ol></div>

"A reliable way for ECMAScript code to test if a value X is a `NaN`, is an expression of the form `X !== X`. The result will be `true` if, and only if, X is a `NaN`. " (see [the `isNan` documentation](https://www.ecma-international.org/ecma-262/5.1/#sec-15.1.2.4)).

__A complete example with isNaN:__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> num </span><span class="pun">=</span><span class="lit">0</span><span class="pun">/</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pun">(</span><span class="pln">isNaN</span><span class="pun">(</span><span class="pln">num</span><span class="pun">)){</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; num </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="com">//shortened version with the conditional operator</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> num </span><span class="pun">=</span><span class="pln"> isNaN</span><span class="pun">(</span><span class="pln">num</span><span class="pun">)</span><span class="pln"> </span><span class="pun">?</span><span class="pln"> </span><span class="lit">0</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> num</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="com">//version with logical operator (implicit conversion) </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> num </span><span class="pun">=</span><span class="pln"> num </span><span class="pun">||</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">/*</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">&nbsp;&nbsp; &lt;=&gt; num = NaN || 0 </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="com">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">&nbsp;&nbsp; &lt;=&gt; num = false || 0</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">*/</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">num</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">//returns 0 in this three cases</span></li>
</ol></div>

Of course 0/0 rarely happens, but there are other cases where `NaN` can appear, for example:

+ `parseInt('foo');`  returns `NaN`   //parseInt tries to convert a String to a Number 
+ `Math.sqrt(-1);` return `NaN`


#### Notes for 2.2.1 Boolean values and logical operators

+ Special values
  + boolean values
    + two values: `true` and `false`
    + no quotation marks for these values
  + undefined
    + a variable not been assigned
    + part of the JS language
    + assigning a variable `undefined` allowed
    + `var foo;` and `var foo = undefined;`: equivalent but 1st recommended (shorter)
    + undeclared variable: `bar;`
      + accessing: raising `ReferenceError` msg
      + typeof operator: return `undefined`
  + `NaN` (Not-a-Number)
    + equal to nothing: `NaN == NaN; // false`, `NaN === NaN; // false`
    + checking w/ `isNaN(expr)`
      + examples: `isNaN(0/0); //true`, `isNaN(NaN); // true`, `isNaN(12); // false`
      + `X = NaN;` $\implies$ `X != X; // true`
    + possible ways to produce `NaN`
      + `(0/0) || 0` $\iff$ `NaN || 0` $\iff$ `false || 0`
      + `parseInt('foo');`: converting a String to a Number
      + `Math.sqrt(-1);`: returning `NaN`

+ Logical operators
  + `&&` (AND): binary
  + `||` (OR): binary
  + `!` (NOT): unary, e.g., `!true // false`
  + implicit conversion
    + expression w/ logical operators
    + non-boolean value implicitly converted to boolean
    + example: `var b = "one"; !b; // false`
  + lazy / short-circuit evaluation
    + `false &&`: always false, `&&` not tested
    + `true ||`: always true, `||` not tested
  + values evaluated as false: `false`, `undefined`, `null`, `0`, `NaN`, the empty string
  + everything else evaluated as true
  + `&&` and `||` evaluation rules
    + `A && B`: return A if A = false, otherwise return B
    + `A || B`: return A if A = true, otherwise return B
    + examples:
      + `var boo = (0/0) || 43.2;   // 43.2`
      + `var myNum = !1; if (myNum == null){ myNum = 3; } myNum = myNum || 2; // 2`

+ Comparison operators
  + Equal `==`
  + Not equal `!=`
  + Greater than `>`
  + Greater than or equal `>=`
  + Less than `<`
  + Less than or equal to `<=`
  + Strict equal `===`
  + Strict not equal `!==`

+ Equal vs. strict equal
  + Equal `==`: return true if strictly equal __w/ type conversion__
  + Strict equal `===`: return true if strictly equal __w/o type conversion__
  + triple-equals operator never doing type coercion
  + examples: `1 == 1; // true`, `1 == '1'; // true`, `1 === 1; // true`, `1 === '1'; // false`
  + best practice: always use `===` or `!==` for comparisons


#### Knowledge check 2.2.1

```js
var a = 5;
 
if ((a === 5) || (a === 6))  { 
    console.log('a is equal to 5 or equal to 6');
}
```

1. When will the expression (`a === 6`) be evaluated?

  a. never<br/>
  b. before (`a === 5`)<br/>
  c. after (`a === 5`)<br/>

  Ans: a<br/>
  Explanation: As a equals 5, the (`a === 5`) expression will be true. With the || binary operator, if the left part is true, then the right part is never evaluated. true || something (an expression) is evaluated to true, and the part to the right of the || operator is not tested.


### 2.2.2 Conditional statements

#### Live coding video: switch statement

<a href="https://edx-video.net/W3CJSIXX2016-V002600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y6p9tozl)


##### Example from the video

[CodePen Demo](https://codepen.io/w3devcampus/pen/jmoJRZ)

[Local Demo](src/js/02b-example02.js)

JavaScript source code is a set of statements. There are a couple of different statement types. We have already seen one of them, the variable statement:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> myVar </span><span class="pun">=</span><span class="pln"> </span><span class="str">'hello '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">'world'</span><span class="pun">;</span></li>
</ol></div>

We've also seen the expression statement:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="lit">3</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">4</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// more often like this</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="lit">3</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="lit">4</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="lit">5</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> x</span><span class="pun">);</span></li>
</ol></div>

A statement closes with a semicolon, but we will see later that missing semicolons are automatically inserted (for readability reasons, we highly recommend systematically adding a semicolon at the end of all statements).

Statements are generally executed sequentially from top to bottom of the script. However, this flow can be modified by statements such as conditional statements and iteration statements.


#### The block statement

The block statement is a simple statement which allows us to group a set of statements wrapped in curly braces. 

Block statement:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="kwd">var</span><span class="pln"> result </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'i = '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

The block statement is used by other statements such as the if-statement or for-statement. We will see these statements below.


#### Conditional statements

All the examples for this section are in this codepen (<span style="color: brown;">to run it: click on the "edit on CodePen" label, and once in CodePen, open the devtool console to see the outputs of this program</span>):

(Please look, edit and try whatever you want. There are parts that are commented - please remove comments and try to understand the results).

[CodePen Demo](https://codepen.io/w3devcampus/pen/qrjdza)

[Local Demo](src/02b-example05.html)


<p class="exampleHTML" style="text-align: center;"><strong>Conditional statements are used to execute a unit of code <br>only if a condition is evaluated as <span style="font-family: 'courier new', courier;">true.</span></strong></p>


##### The `if` statement

__Syntax:__

<div class="exampleHTML">
<p style="padding-left: 30px;"><span style="color: #ff0000;"><strong><span style="font-family: 'courier new', courier;">if</span></strong></span> ( Expression ) Statement <span style="color: #ff0000;"><strong><span style="font-family: 'courier new', courier;">else</span></strong></span> Statement</p>
<p style="padding-left: 30px;"><span style="color: #ff0000;"><strong><span style="font-family: 'courier new', courier;">if</span></strong></span> ( Expression ) Statement</p>
</div>

__The expression may include:__

+ logical operators ( `! && ||` )
+ comparison operators ( `==`, `===`, `>`, `>=`, `<`, `<=`)
+ any values or expressions which can be converted to boolean

__Example #1: if-statement__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> num </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">if</span></strong><span class="pln"> </span><span class="pun">(</span><span class="pln">num </span><span class="pun">===</span><span class="pln"> </span><span class="lit">10</span><span class="pun">)</span><span class="pln"> </span><strong><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; num </span><span class="pun">=</span><span class="pln"> </span><span class="lit">20</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="com">// num equals 20</span></li>
</ol></div>


__Example #2: if-else statement__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> num </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">if</span></strong><span class="pln"> </span><span class="pun">(</span><span class="pln">num </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">10</span><span class="pun">)</span><span class="pln"> </span><strong><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; num </span><span class="pun">=</span><span class="pln"> </span><span class="lit">20</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong><span class="pln"> </span><strong><span class="kwd">else</span></strong><span class="pln"> </span><strong><span class="pun">{</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; num </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// num equals 0</span></li>
</ol></div>


__Reminder:__

The following values will evaluate to false:

+ `false`
+ `undefined`
+ `null`
+ `0`
+ `NaN`
+ `""` or `''` (empty string)

All other values, including all objects, evaluate to true when passed to a conditional statement.

##### The if-then-else ternary operator

This ternary operator is a shortcut version of `if...then...else`.

Let's look at this code example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> max</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> min </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">min </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">10</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; max </span><span class="pun">=</span><span class="pln"> min </span><span class="pun">+</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; max </span><span class="pun">=</span><span class="pln"> min</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

_Explanation_: You can replace this "if-then-else" statement with the ternary operator that uses a syntax with "?" and ":"

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> max</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> min</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">max </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">min </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">10</span><span class="pun">)?</span><span class="pln"> min</span><span class="pun">+</span><span class="lit">10</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> min</span><span class="pun">;</span></li>
</ol></div>


_Line 3_ can be read as if `(min < 10)` then `max = min+10`, else `max = min`. The "then" part is after the "?" and the "else" part is after the ":" part.

This "short" version is not recommended except for very simple statements that involve a very obvious block of instructions for the "then" and the "else". Usually this syntax is much harder to read for beginners.


#### Curly braces

Should we use them in if-then-else statements? There are examples without curly braces on the Web: what does this mean?

Here are two versions of the same code.

__Version 1:__ `no curly` braces

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">if</span></strong><span class="pln"> </span><span class="pun">(</span><span class="pln">a </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">2</span><span class="pun">)</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; result </span><span class="pun">=</span><span class="pln"> </span><span class="str">'a is bigger than 2'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">else</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; result </span><span class="pun">=</span><span class="pln"> </span><span class="str">'a is not bigger than 2'</span><span class="pun">;</span></li>
</ol></div>

__Version 2:__ with curly braces for delimiting the "then" and "else" blocks

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">if</span></strong><span class="pln"> </span><span class="pun">(</span><span class="pln">a </span><span class="pun">&gt;</span><span class="pln"> </span><span class="lit">2</span><span class="pun">)</span><span class="pln"> </span><strong><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; result </span><span class="pun">=</span><span class="pln"> </span><span class="str">'a is bigger than 2'</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; result </span><span class="pun">=</span><span class="pln"> </span><span class="str">'a is not bigger than 2'</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
</ol></div>

Version 1 and version 2 are equivalent. Indeed, version 1 is correct: you can omit curly braces if the "then" or "else" blocks are made of only one statement (one line of code).

But version 2 is cleaner and more readable, and, in particular, it is much better for maintainability (because you can add a statement just by pressing the enter key. And you can add some extra lines of code without worrying about adding curly braces because you broke the "1 line statement rule").

<p class="exampleHTML" style="text-align: center;"><strong>So it is strongly recommended that you&nbsp;always use if-statements <br>enclosed in curly braces.&nbsp;</strong></p>

Of course, one-line if-statements like this :

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">true</span><span class="pun">)</span><span class="pln"> doSomething</span><span class="pun">();</span></li>
</ol></div>

...are really fast to write, but if you want to add a second statement later it will become more time consuming.

__Conclusion: <span style="color: brown;">always use curly braces!</span>__


#### The switch statement

In order to avoid having a series of ifs and elses, it is possible to use a __`switch`__ statement. 

The syntax of the `switch` statement is:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><strong><span class="kwd">switch</span></strong><span class="pln"> </span><span class="pun">(</span><span class="pln">expression</span><span class="pun">)</span><span class="pln"> </span><strong><span class="pun">{</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> value1</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; statement</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><strong><span class="kwd">break</span></strong><span class="pun">; &nbsp; &nbsp; &nbsp; // break can be omitted in that case</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// the second test case will be executed</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// most of the time we add a break; at the end</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// of a "case"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> value2</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; statement</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><strong><span class="kwd">break</span></strong><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> value3</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; statement</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><strong><span class="kwd">break</span></strong><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">default</span></strong><span class="pun">: &nbsp; &nbsp; &nbsp; &nbsp; // if no case tested true</span><span class="pln"></span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; statement</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><strong><span class="kwd">break</span></strong><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

If the value of an expression equals one of the cases (the equality operator evaluated is ===), all the statements next to this case block are executed sequentially until the keyword break is reached.

__Example #1: a common switch/case/default example__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> gear </span><span class="pun">=</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">switch</span></strong><span class="pln"> </span><span class="pun">(</span><span class="pln">cloudColor</span><span class="pun">)</span><span class="pln"> </span><strong><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'green'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">=</span><span class="pln"> </span><span class="str">'spacesuit'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="kwd">break</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'black'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">=</span><span class="pln"> </span><span class="str">'boots'</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>break</strong></span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'grey'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">=</span><span class="pln"> </span><span class="str">'umbrella'</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>break</strong></span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'white'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">=</span><span class="pln"> </span><span class="str">'jacket'</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>break</strong></span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">default</span></strong><span class="pun">:</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">=</span><span class="pln"> </span><span class="str">'watch'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; <strong>break</strong></span><span class="pun">;</span><span class="pln"> </span><span class="com">// useless if in the last case</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun"><strong>}</strong> // end of the switch statement</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div>

In this example, if the clouds are grey, then my gear will be just an umbrella. If they are white, I'll wear only a jacket, if they are black I'll be nude with just boots (!), and if they are green I'll get a spacesuit. And if the cloud color is none of these, then I'll only wear a watch. The presence of the __`break`__ keyword at the end of the different cases make the choices 100% exclusive. Only one case can be executed!

__Example 2#: a switch without "breaks" at the end of each cas__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> gear </span><span class="pun">=</span><span class="pln"> </span><span class="str">''</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">switch</span></strong><span class="pln"> </span><span class="pun">(</span><span class="pln">cloudColor</span><span class="pun">)</span><span class="pln"> </span><strong><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'green'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'spacesuit'</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><strong><span class="kwd">break</span></strong><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'black'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'boots, '</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'grey'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'umbrella, '</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">case</span></strong><span class="pln"> </span><span class="str">'white'</span><span class="pun">:</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'jacket, '</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="kwd">default</span></strong><span class="pun">:</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; gear </span><span class="pun">+=</span><span class="pln"> </span><span class="str">'watch'</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun"><strong>}</strong> // end of the switch statement</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div>


_Explanation_: if the clouds are black, then my gear will be 'boots, umbrella, jacket, watch'. If the clouds are green, my gear is a spacesuit (because of the `break` keyword, other cases will not be tested). If the cloud color is not in the listed colors, then my gear is only a watch (default case).

__Example #3: three ways to do condition statements__

To finish up this section, here is a complete example (<span style="color: brown;">to run it: click on the "edit on codepen" label and once in codepen, open the devtool console to see the outputs of this program</span>):

[CodePen Demo](https://codepen.io/w3devcampus/pen/PpjPKy)

[Local Demo](src/02b-example04.html)


#### Notes for 2.2.2 Conditional statements

+ Expressions
  + a statement closed w/ semicolon (`;`)
  + missing semicolon automatically inserted
  + readability: always recommended adding a semicolon at the end of all statements
  + flow of program
    + statement executed sequentially from top to bottom
    + modified by statements such as conditional statements or iteration statement
  + conditional statements: used to execute a unit of code only if a condition is evaluated as `true`
  + loop statement
    + used to run the block of code several times while a condition satisfied
    + [slowmoJS](https://toolness.github.io/slowmo-js/): online tool to check how the loop executed

+ Block statement
  + a simple statement allowing to group a set of statements wrapped in curly braces`{` & `}`
  + used by other statements including if-statement or for-statement
  + example: 

    ```js
    {
        var i = 0; var result = false;
        console.log('i = ' + i);
    }
    ```

+ The `if` statement
  + syntax:
    + <code><span style="color: brown; font-weight: bold;">if</span> (Expr1) <span style="color: brown; font-weight: bold;">else</span> (Expr1)</code>
    + <code><span style="color: brown; font-weight: bold;">if</span> (Expr1)</code>
  + `Expr1` possibly including
    + logical operators: `&&`,. `||`, & `!`
    + comparison expressions: `==`, `===`, `>`, `>=`, `<`, `<=`
    + any values or expressions able to converted to boolean
  + curly brace
    + `Expr1` and `Expr2` possible block statements w/ curly braces
    + omitted curly braces allowed if only one statement in the block
    + strongly recommended enclosing if-statement in curly braces
  + example:

    ```js
    var num = 10;
    
    if (num === 10) { num = 20; } // num = 10

    if (num > 10) { num = 20; } else { num = 0; } // num = 0
    ```

+ The if-then-else ternary operator
  + ternary operator:
    + using a syntax w/ "?" and ":"
    + statement: `(expr1) ? (expr2) : (expr3)`
  + a shortcut version of `if...then...else`
  + read as `if (expr1) then (expr2) else (expr3)`
  + short version not recommended except for very simple statement
  + example: equivalent

    ```js
    var max; var min = 2;
    
    if (min < 10) {     // if...then...else
        max = min + 10;
    } else {
        max = min;
    }

    max = (min < 10)? min+10 : min; // ternary
    ```

+ The switch statement
  + syntax:

    ```js
    switch (expression) {
        case value1:
            statement;
            break;      
            // break can be omitted in that case the second test case will be executed
            // most of the time we add a break; at the end of a "case"
    
        case value2:
            statement;
            break;
    
        case value3:
            statement;
            break;
    
        default:         // if no case tested true
            statement;
            break;
    }
    ```
  
  + the equality operator evaluated w/ `===`
  + all statements next to the `case` block executed sequentially until `break` keyword reached


#### Knowledge check 2.2.2

```js
var x = 2;
var y = 5;

if(y > 0) {
    if ((x > 2) && (y < 10)) {
        if(x === 2) console.log("YES");
    } else {
        if((x > 10) && (y === 5)) console.log("NO");
    }
} else {
    console.log("MAYBE");
}
console.log(" THE END");
```

1. What will be printed in the devtool console?

  a. THE END<br/>
  b. NO THE END<br/>
  c. YES THE END<br/>

  Ans: a<br/>
  Explanation: y is 5 so the first if statement will be true. The second if statement tests the condition (x > 2) that is false. The execution will continue to the else. The next test is ((x > 10) && (y === 5)), where (x > 10) is false, the right part of the expression will not be evaluated because of the && operator and "NO" will never been printed.<br/>So, neither YES or NO will be printed. Only THE END will be printed.


### 2.2.3 Loop statements


#### Live coding video: loop statements

<a href="https://edx-video.net/W3CJSIXX2016-V002700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y5ubn8ad)

Example from the video

[CodePen Demo](https://codepen.io/w3devcampus/pen/qmGeYZ?editors=0012)

[Local Demo](src/js/02b-example06.js)


#### Loops

A loop is used to run the same block of code several times while a condition is satisfied.

If you have trouble with loops, the online tool [slowmoJS](https://toolness.github.io/slowmo-js/) can be really useful: you just have to copy and paste an example into it to run it step by step and see how your program executes loops.

##### The while statement

With a `while` statement, a block of code is executed repeatedly while the specified condition is satisfied (evaluates to true).

Syntax:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="pln"> condition </span><span class="pun">)</span><span class="pln"> statement</span></li>
</ol></div>

The condition is an expression, and the statement can be a block statement.

Typical example of a while statement:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> j </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">4</span><span class="pln"> </span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; j </span><span class="pun">+=</span><span class="pln"> i</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; i +</span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span style="color: #666600;" color="#666600">...</span></li>
</ol></div>

The block inside the while (_lines 4 and 5_) will be executed three times:

+ _Line 1_ initializes i with a value of 1.
+ We enter the while statement at _line 3_. Is the value of `i` strictly less than 4?
+ Yes, the variable `i` is equal to 1, we enter the statement inside the `while`.
+ __Run 1:__
  + We execute _line 4_: `j += i;` (equivalent to `j = j + i`). As `j` was set to 1 at _line 1_, `j` is now equal to 2.
  + We execute _line 5_ and increment `i` by one. The variable i is now equal to 2.
  + We go back to the while at _line 3_. Is `i < 4`? Yes, we execute lines 3 and 4 again.
+ __Run 2:__
  + Now at the end of _line 5_, `j` is equal to "old j value" + "new i value", so `j = 2 + 2 = 4`, i has been incremented and is now equal to 3.
  + We go back to the while at _line 3_. Is `i < 4`? Yes, we execute lines 3 and 4 again.
+ __Run 3:__
  + Now at the end of _line 5_, `j` is equal to "old j value" + "new i value", so `j = 4 + 3 = 7`, `i` has been incremented and is now equal to 4.
  + We go back to the while at _line 3_. Is `i < 4`? No! The value of `i` is now 4, which is not less than 4. We continue the execution of the program at line 7 with `i = 4` and `j = 7`.

Of course, if the condition never evaluates to false, the block will be executed infinitely until the machine crashes... a test like `while (i > 0) { .....}` will never stop and will eat all the CPU.

Try this example now with [slowmoJS](https://tinyurl.com/y56ntfz4)!


##### The do-while statement

The do-while statement is very similar to the while statement, but its syntax is different:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">do</span><span class="pln"> statement </span><span class="kwd">while</span><span class="pln"> </span><span class="pun">(</span><span class="pln"> condition </span><span class="pun">)</span></li>
</ol></div>

Typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="kwd">do</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'i = '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i</span><span class="pun">);</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; i</span><span class="pun">++;</span></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pun">}</span><span class="pln"> </span><span class="kwd">while</span><span class="pun">(</span><span class="pln">i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">20</span><span class="pun">);</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'Value of i after the do-while statement: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i</span><span class="pun">);</span></li>
</ol></div>

The <span style="color: brown; font-weight: bold;">do-while statement executes the content of the loop once before checking the condition of the while</span>, whereas a <span style="color: cyan; font-weight: bold;">while statement will check the condition first before executing the content.</span>

A do-while is used for a block of code that must be executed at least once.These situations tend to be relatively rare, thus the simple while-statement is more commonly used. 

If you want to "see" the difference, [look at the "do-while" statement with slowmoJS](https://tinyurl.com/y3a963y4) and [the "while" statement slowmoJS](https://tinyurl.com/yy7j48fe).


##### The `for` statement

This statement adds some things to the while and do-while statements: an initialization expression and an incrementing expression.

Its syntax is:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="pln">initialization</span><span class="pun">;</span><span class="pln"> condition</span><span class="pun">;</span><span class="pln"> incrementation</span><span class="pun">)</span><span class="pln"> statement</span></li>
</ol></div>

The three expressions within the parentheses are optional. If the condition is omitted, it is replaced by true (infinite loop).

Typical example (counting from 0 to 10):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'i = '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

We can have more than one instruction in the "initialization part" (var i = 0), and more than one instruction in the "incrementation part" (i++). Here is another example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><strong><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> j </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">;</span></strong><span class="pln"> i </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span><strong><span class="pln"> i</span><span class="pun">++,</span><span class="pln">&nbsp;j</span><span class="pun">+=</span><span class="lit">2</span></strong><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'i = '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i </span><span class="pun">+</span><span class="pln"> </span><span class="str">' j = '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> j</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

In this example, two variables are defined and assigned within the initialization expression. Before each execution of the block statement, the condition is checked; here we need `i <=10`. After each execution of the block statement, the @@incrementation expression is executed to increment the variables `i` by 1 and `j` by 2.

Open the devtool console of your browser and copy and paste the above code, or [look at the slowmoJS execution](https://tinyurl.com/y5ucfaq2).


##### The `for-in` statement

The for-in statement is used to iterate through an object (or through an array, which is also an object). 

Its syntax is:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="pln"> variable </span><span class="kwd">in</span><span class="pln"> expression </span><span class="pun">)</span><span class="pln"> statement</span></li>
</ol></div>

Typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> michel </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// michel&nbsp;is an object</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; familyName</span><span class="pun">:</span><span class="str">'Buffa'</span><span class="pun">, &nbsp; &nbsp; // familyName, givenName, age </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // are its properties</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; givenName</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Michel'</span><span class="pun">,</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; age</span><span class="pun">:</span><span class="pln"> </span><span class="lit">51</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> </span><span class="kwd">property</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> michel</span><span class="pun">)</span><span class="pln"> </span></strong><span class="pun"><strong>{</strong> &nbsp; // the for-in will </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // enumerate properties</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; console.log(property); &nbsp; &nbsp; &nbsp;// will print "familyName", </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // "givenName", </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // "age"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">michel</span><span class="pun">[</span><span class="kwd">property</span><span class="pun">]);</span><span class="pln">&nbsp; // michel['givenName'] same&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // as michel.givenName</span></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pun">}</span></strong></li>
</ol></div>

Before each execution of the block statement, the variable named "property" is assigned with the name of one of the properties (the keys) of the object.

We will see further examples of this statement in module 4, which is devoted to the study of JavaScript objects.


#### [ADVANCED] Other statements


##### The `continue` statement

The `continue` statement is used to stop the execution of a block and start the next iteration of the loop. The difference from the "`break`" statement is that the loop continues.

Syntax:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">continue</span><span class="pln"> </span><span class="pun">[</span><span class="pln">label</span><span class="pun">]</span></li>
</ol></div>

The label is optional.

Typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i </span><span class="pun">=</span><span class="pln"> </span><span class="lit">1</span><span class="pun">,</span><span class="pln"> k </span><span class="pun">=</span><span class="pln"> </span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> </span><span class="lit">5</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">i </span><span class="pun">===</span><span class="pln"> </span><span class="lit">3</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; </span><span class="kwd">continue</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; k </span><span class="pun">+=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="pln">i</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;&nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'k += '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="pun">(</span><span class="lit">2</span><span class="pun">*</span><span class="pln">i</span><span class="pun">));</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'Final k value:'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> k</span><span class="pun">)</span></li>
</ol></div>


Copy and paste this example in your devtool console, but first, try to guess what the value of `k` will be!

Hint: _lines 2-4_ mean that _line 6_ will never be executed for `i = 3`. That means that `i*2` will only be added to k for i = 1, 2 and 4...


##### The `break` statement

The `break` statement is used to stop an iteration, a switch or a labelled statement.

Syntax:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">break</span><span class="pln"> </span><span class="pun">[</span><span class="pln">label</span><span class="pun">]</span></li>
</ol></div>

Typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> tab </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[</span><span class="str">'michel'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'john'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'donald'</span><span class="pun">,<span style="color: #000000;" color="#000000">&nbsp;</span></span><span class="str">'paul'</span><span class="pun">]; // johh at index = 1</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> isNameInTheArray</span><span class="pun">(</span><span class="pln">name</span><span class="pun">,</span><span class="pln"> theArray</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"Number of elements in the array : "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> theArray</span><span class="pun">.</span><span class="pln">length</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; for</span><span class="pun">(</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span><span class="pln"> i </span><span class="pun">&lt;</span><span class="pln"> theArray</span><span class="pun">.</span><span class="pln">length</span><span class="pun">;</span><span class="pln"> i</span><span class="pun">++)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'comparing with element in the array at pos '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; if</span><span class="pun">(</span><span class="pln">theArray</span><span class="pun">[</span><span class="pln">i</span><span class="pun">]</span><span class="pln"> </span><span class="pun">===</span><span class="pln"> name</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">'the name '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> name </span><span class="pun">+</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"></span><span class="str">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;' is in the array at pos: '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>break</strong></span><strong><span class="pun">;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; }</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">name </span><span class="pun">+</span><span class="pln"> </span><span class="str">' is not at pos '</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> i</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; }</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="com">// Execute the function</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">isNameInTheArray</span><span class="pun">(</span><span class="str">'john'</span><span class="pun">,</span><span class="pln"> tab</span><span class="pun">);</span></li>
</ol></div>

Copy and paste in the devtool console. You'll see that the function that compares each element in the array passed as the second parameter with the name 'john', will stop looping after 'john' has been found at index = 1.

__Detailed explanations:__

+ _Line 20_ executes the function
+ _Line 6_: The `for` statement loops on all existing indexes in the `tab`, from 0 to `tab.length`
+ _Line 9_: if the condition is `true`, we enter the block and execute _lines 10-12_
+ The `break` statement at _line 12_ will exit from the loop, it "breaks" the loop.
+ The different `console.log(...)` will never display the message "comparing with elements..." with indexes greater than 1: the loop exists when 'john' is found at index 1 (i equal to 1).


#### Notes for 2.2.3 Loop statements

+ `while` loop
  + `while` statement
    + a block of code executed repeatedly while the specified conditionsatisfied
    + syntax: `while (condition) statement`
      + condition: a logical expression; true to execute the statement, otherwise exit
      + statement: probably a block statement
    + checking the condition first before executing the content
  + `do-while` statement
    + syntax: `do statement while (condition)`
    + executing the content of the loop once before checcking the condition of the while
    + used for a block of code executed at least once
    + rarely used
  + examples

    ```js
    var i = 1, j = 1;
    while (i < 4) {
        j += i;
        i += 1; 
    }

    var i = 0;
    do {
        console.log('i = ' + i);
        i++;
    } while(i < 20);
    ```

+ `for` loop
  + `for` statement
    + adding an initialization expression and an incrementing expression to `while` or `do-while` statements
    + syntax: `for (initialization; condition; incrementation) statement`
    + `condition` omitted $\to$ replaceing w/ `true` $\to$ infinity loop
    + examples: 

      ```js
      for (var i = 0; i <= 10; i++) {
        console.log('i = ' + i);
      }

      for (var i = 1, j = 1; i <= 10; i++, j+=2) {
          console.log('i = ' + i + ' j = ' + j);
      }
      ```

  + `for-in` statement
    + used to iterate through an object
    + syntax: `for (variable in expression) statement`
    + example

      ```js
      var michel = {
          familyName:'Buffa',   // michel is an object
          givenName: 'Michel',  // familyName, givenName, age
          age: 51               // are its properties
      }
      
      for(var property in michel) {
          // the for-in will enumerate properties will print 
          // "familyName", "givenName", "age"
          console.log(property); 
          // michel['givenName'] same as michel.givenName
          console.log(michel[property]); 
      }
      ```

+ Loop interrruption sattement
  + `continue` statement
    + used to stop the execution of a block and starting the next iteration of the loop
    + syntax: `continue [label]`
    + label optional
    + example

      ```js
      for(var i = 1, k = 0; i < 5; i++) {
          if (i === 3) {
              continue;
          }
      
          k += 2*i;
          console.log('k += ' + (2*i));
      }
      ```

  + `break` statement
    + used to stop an iteration, a switch or a labelled statement
    + syntax: `break [label]`
    + example

      ```js
      for(var i=0; i < theArray.length; i++) {
          console.log('comparing with element in the array at pos ' + i);

          if(theArray[i] === name) {
            console.log('the name ' + name + ' is in the array at pos: ' + i);
            break;
          } else {
            console.log(name + ' is not at pos ' + i);
          }
      }
      ```


### 2.2.4 Discussion and projects

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.

#### Suggested topic of discussion

+ Did you know about the `===` and `!==` operators we recommend you to use?


#### Optional projects

+ If not allergic to High School math: please write a piece of code that solves second degree equations. You pass the a, b, c parameters of: $ax^2 + bx + c$, and the solve function will compute delta = $b^2 - 4a*c$. Test the sign of delta, and if it's equal to zero, then display (in the console, or better, in the page) the roots of the equation.
+ Try to write a small program that asks you to guess a number. It will choose randomly a number, and will ask you to enter a value in an input field. Then it will display "too small" or "too big", until you find the number.

  _Hint:_ use the `Math.random` and `Math.round` methods, such as in `let randomNumber = Math.round(Math.random() * 10);` to get a random value between 0 and 10.

+ For working with input fields, look at section 1.4 from the first module, the math function plotter example used input fields. Or look at the section about DOM in this module.
+ quizzTry to make a quiz using the DOM and buttons, checkboxes, etc.
+ Display a question, for example "Which actor played in Titanic?", and display two or three buttons ("Leonardo Di Caprio", "Christian Bale", "Nicolas Cage"). Then, when the user presses a button, you must check the answer and display the next question, etc.
+ Use CSS with an image background for the buttons.
+ Or use images with click listeners - we saw this in the section about the DOM and events.
+ A bit more challenging: use checkboxes instead of a set of buttons (we've done an example close to this in the section that presented the DOM).





