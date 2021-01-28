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


### 1.7.2 Exercises (7-12)

7. Correct usage of the script tag

  We use the `script` HTML tag for inserting/embedding JavaScript code in an HTML document. Below, we describe different uses of this tag. Please check the ones that are <span style="color: brown;">incorrect</span>. (3 answers are incorrect!)

  a. `<script src="myScript.js">`<br/>
  b. `<script src="myScript.js"/>`<br/>
  c. `<script src="myScript.js"> </script>`<br/>
  d. `<script src="../utils.html"> </script>`<br/>
  e. `<script src="http://myServer.com/js/math.js"> </script>`<br/>
  f. `<script src="https://myServerSecure.com/js/math.js"> </script>`<br/>

  Ans: abd<br/>
  Explanation: The script tag always comes with a closing tag. It can only be used to include js code, not html. Finally it can be used to include external js source files using http or https URLs.


8. Where are my files?

  Only one of these is true:

  a. JavaScript code can be located in external JS files, using a relative or absolute URL (they can be on the same hard disk as the html file that includes them or on any external HTTP server). <br/>
  b. JavaScript code can be located in external JS files, but on the same server as the HTML file that includes them<br/>
  c. JavaScript code should be always located between `<script>...</script>` tags in an HTML document<br/>
  
  Ans: a<br/>
  Explanation: JavaScript code can be located in different places, in HTML between script tags, in local or external files, using relative or absolute URLs.


9. How many files?

  Can we include more than one JavaScript file in an HTML document? (Yes/No)
  
  Ans: Yes<br/>
  Explanation: It it possible to use more than one JavaScript file, just use multiple `<script src="..."></script>`



10. Debug me!

  How do you print a debug message in the devtool console?

  a. Execute `console.log(...)` in your code.<br/>
  b. Execute `alert(...)` in your code.<br/>

  Ans: a<br/>
  Explanation: `console.log("value of x: " + x);` will display in the console the value of the variable x. This is the best way to display messages in the console.
  
<hr>

__Source code for the next 2 questions (11 and 12)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> x1 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">10</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> x2 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">12</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> x3 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">9.5</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> x4 </span><span class="pun">=</span><span class="pln"> </span><span class="lit">15</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> compute</span><span class="pun">(</span><span class="pln">x1</span><span class="pun">,</span><span class="pln"> x2</span><span class="pun">,</span><span class="pln"> x3</span><span class="pun">,</span><span class="pln"> x4</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> m </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">x1 </span><span class="pun">+</span><span class="pln"> x2 </span><span class="pun">+</span><span class="pln"> x3 </span><span class="pun">+</span><span class="pln"> x4</span><span class="pun">)/</span><span class="lit">5.0</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> n </span><span class="pun">=</span><span class="pln"> m</span><span class="pun">*</span><span class="lit">12</span><span class="pun">*</span><span class="pln">m</span><span class="pun">/</span><span class="lit">2.</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> o </span><span class="pun">=</span><span class="pln"> n</span><span class="pun">-</span><span class="lit">0.94</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; return</span><span class="pln"> o</span><span class="pun">/</span><span class="lit">518</span><span class="pun">;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="com">// Call the above function with x1, x2, x3, x4</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="com">// What is the result, add here a mean to display </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// the result in the console</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com" style="color: brown;">var result = compute(x1, x2, x3, x4);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com" style="color: brown;">console.log(result);</span></li>
</ol></div>

11. Get the result!

  Ty  pe the above source code in CodePen or in the devtool console and execute it, a result will be printed in the devtool console. Try to understand where it comes from? what is the value of m, of n, of o, etc.

  Once you have executed the code, please type the result in the text field below:

  Ans: 1<br/> 



12. Print me but I'm lazy

  Is it possible to see the value of the global variables `x1, x2, x3, x4` without adding any source code?

  a. Yes. `x1, x2, x3, x4` are global variables declared with the keyword var, outside any function. They can be accessed from the devtool console. Just type their name in the console.<br/>
  b. No, variable values cannot be accessed without using an instruction such as `alert(...)`, `console.log(...)` or the DOM API to display their value in the HTML document.<br/>
  
  Ans: a<br/>
  Explanation: Indeed, `x1, x2, x3, x4` are global variables. Their value can be printed in the console just by typing their name.


### 1.7.3 Exercices (13-20)

13. You don't like my name?

  Check the valid variable declarations: (3 correct answers.)

  a. `var 1x = 10;`<br/>
  b. `var for=2;`<br/>
  c. `let $name = "Michel";`<br/>
  d. `const #x = 5;`<br/>
  e. `var x = 0xFF;`<br/>
  f. `var x=1, y=2, z;`<br/>

  Ans: cef<br/>
  Explanation: <br/>
    + The first letter of a variable can only be "$", "_", "a" to "z", or "A" to "Z". The other characters in a name must be any of these, or numeric digits.
    + There are some reserved names that you can't use as a variable name: for, boolean, if, delete, var, function, etc. They are reserved words of the JavaScript language. 1x, for, #x are not valid names.


14. Case sensitive?

  Are variable names case sensitive? (i.e: `var x=10; console.log(X);` will give an error) (Yes/No)

  Ans: Yes


15. Naming conventions

  There are naming rules and conventions for JavaScript variable and constant names, that we presented in the course. Check the names that follow these conventions: (3 correct answers.)

  a. `var bestGrade = 10;`<br/>
  b. `let name = "Michel";`<br/>
  c. `const FAMILY_NAME = "Buffa";`<br/>
  d. `var final_result;`<br/>
  e. `var _myCar = "Ferrari";`<br/>

  Ans: abc<br/>
  Explanation: The JavaScript community has some conventions about naming variables:
    + The camelCase notation is preferred: mySpaceShip, sumOfAllGrades, etc. If a variable name is a single word, use lowercase.
    + For a variable with a composed name, the first letter is lowercase and each first letter of every word is capitalized. Example: var myVariableName


<hr>

__Source code for the next 3 questions (16, 17 and 18)__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> name </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Zorro"</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayName</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">name</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">displayName</span><span class="pun">();</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayName1</span><span class="pun">(</span><span class="pln">name</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">name</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">displayName1</span><span class="pun">(</span><span class="str">"Indiana Jones"</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="com">// local scope again</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="kwd">function</span><span class="pln"> displayName2</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> name </span><span class="pun">=</span><span class="pln"> </span><span class="str">"Batman"</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="pln">name</span><span class="pun">);</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">displayName2</span><span class="pun">();</span><span class="pln"> </span></li>
</ol></div>

16. Check my scope (part 1)

  What value will be displayed in the devtool console after the execution of line 7?

  a. Zorro<br/>
  b. Batman<br/>
  c. Indiana Jones<br/>

  Ans: a<br/>
  Explanation: The execution of the function `displayName` will display the value of the global variable name: Zorro


17. Check my scope (part 2)

  What value will be displayed in the devtool console after the execution of _line 13_?

  a. Batman<br/>
  b. Indiana Jones<br/>
  c. Zorro<br/>

  Ans: b<br/>
  Explanation: The execution of the function `displayName1` will display the value of the call parameter, that will mask the global variable that has the same name. The displayed value will be "Indiana Jones".


18. Check my scope (part 3)

  What value will be displayed in the devtool console after the execution of line 21?

  a. Zorro<br/>
  b. Batman<br/>
  c. Indiana Jones<br/>

  Ans: b<br/>
  Explanation: The execution of the function `displayName2` will display the value of the local variable at line 17, that will mask the global variable that has the same name. The displayed value will be "Batman".



19. Are you crazy?

  ```js
  var name = "Michel";
  var result = name/3;
  console.log(result);
  ```

  What will be printed in the devtool console?

  a. NaN<br/>
  b. Infinity<br/>
  c. An error<br/>

  Ans: a<br/>
  Explanation: NaN means "Not a Number". As we cannot divide a string value by a number (it's Not A Number!), NaN will be displayed.



20. Can you compute this?

  ```js
  var x = 125;
  var result = x/0;
  console.log(result);
  ```

  What will be printed in the devtool console?

  a. Nan<br/>
  b. Infinity<br/>
  c. An error<br/>

  Ans: b<br/>
  Explanation: Divide 125 by zero and you will get Infinity!









