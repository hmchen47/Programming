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

##### Undefined and null values

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


#### Lazy evaluation or short-circuit evaluation

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

#### Implicit conversions of non boolean values in expressions

Used with logical operators or within statements, __non-boolean values are implicitly converted to booleans__.  

<span style="color: brown; font-weight: bold;">All the following values are evaluated as false:</span>

+ __false__
+ __undefined__
+ __null__
+ __0__
+ __NaN__
+ __the empty string ''__

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
    + part of rhe JS language
    + assigning a variable `undefined` allowed
    + `var foo;` and `var foo = undefined;`: equivalent but 1st recommended (shorter)
    + undeclared variable: `bar;`
      + accessing: raising `ReferenceError` error msg
      + typeof operator: return `undefined`



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

  Ans: <br/>
  Explanation: 







