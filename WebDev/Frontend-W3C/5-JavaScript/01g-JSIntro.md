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

<div><ol>
<li" value="1"> &lt;!DOCTYPE html&gt;</li>
<li"> &lt;html lang="en"&gt;</li>
<li"> &lt;head&gt;</li>
<li"> &lt;title&gt;JavaScript and HTML&lt;/title&gt;</li>
<li"> &lt;meta charset="utf-8"/&gt;</li>
<li"> &lt;script&gt;</li>
<li"> function changeTitleCSSStyle() {</li>
<li"> var title = document.querySelector("#mainTitle");</li>
<li"> title.style.color = 'black';</li>
<li"> title.style.backgroundColor = "yellow";</li>
<li"> title.style.border = "5px dashed red";</li>
<li"> }</li>
<li"> &lt;/script&gt;</li>
<li"> &lt;/head&gt;</li>
<li"> &lt;body&gt;</li>
<li"> &lt;h1 id="mainTitle"&gt;My home page&lt;/h1&gt; </li>
<li"> </li>
<li"> &lt;p&gt;This is an example of interactivity between JavaScript and the HTML content of a document.&lt;/p&gt;</li>
<li"> &lt;button onclick="changeTheTitle();"&gt;Click me&lt;/button&gt;</li>
<li"> &lt;/body&gt;</li>
<li"> &lt;/html&gt;</li>
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

<div><ol>
<li" value="1">var parameters = {</li>
<li">&nbsp; &nbsp; target: '#myFunction',</li>
<li">&nbsp; &nbsp; data: [{</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; fn: 'sin(x)', </li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; color: 'red'</li>
<li">&nbsp; &nbsp; &nbsp; &nbsp; } </li>
<li">&nbsp; &nbsp; ],</li>
<li">&nbsp; &nbsp; grid: true,</li>
<li">&nbsp; &nbsp; yAxis: {domain: [-1, 1]},</li>
<li">&nbsp; &nbsp; xAxis: {domain: [0, 2*Math.PI]},</li>
<li">};</li>
<li">&nbsp;</li>
<li">functionPlot(parameters);</li>
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

  We use the `script` HTML tag for inserting/embedding JavaScript code in an HTML document. Below, we describe different uses of this tag. Please check the ones that are <span style="color: brown;">incorrect. (3 answers are incorrect!)

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

<div><ol>
<li" value="1">var x1 = 10;</li>
<li">var x2 = 12;</li>
<li">var x3 = 9.5;</li>
<li">var x4 = 15;</li>
<li">&nbsp;</li>
<li">function compute(x1, x2, x3, x4) {</li>
<li">&nbsp; &nbsp; var m = (x1 + x2 + x3 + x4)/5.0;</li>
<li">&nbsp; &nbsp; var n = m*12*m/2.;</li>
<li">&nbsp; &nbsp; var o = n-0.94;</li>
<li">&nbsp; &nbsp; return o/518;</li>
<li">}</li>
<li">&nbsp;</li>
<li">// Call the above function with x1, x2, x3, x4</li>
<li">// What is the result, add here a mean to display </li>
<li">// the result in the console</li>
<li"><span style="color: brown;">var result = compute(x1, x2, x3, x4);</li>
<li"><span style="color: brown;">console.log(result);</li>
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

<div><ol>
<li" value="1">var name = "Zorro"; </li>
<li">&nbsp;</li>
<li">function displayName() {</li>
<li">&nbsp; &nbsp;console.log(name); </li>
<li">}</li>
<li">&nbsp;</li>
<li">displayName();</li>
<li">&nbsp;</li>
<li">function displayName1(name) {</li>
<li">&nbsp; &nbsp;console.log(name); </li>
<li">}</li>
<li">&nbsp;</li>
<li">displayName1("Indiana Jones"); </li>
<li">&nbsp;</li>
<li">// local scope again</li>
<li">function displayName2() {</li>
<li">&nbsp; &nbsp;var name = "Batman"; </li>
<li">&nbsp; &nbsp;console.log(name); </li>
<li">}</li>
<li">&nbsp;</li>
<li">displayName2(); </li>
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


### 1.7.4 Exercises (21-26)

21. Find the intruder

  JavaScript is a weakly typed language. This means that you do not declare the type of the variables. However, variables do have a data type and JavaScript figures out this type for you (and you can know it using the `typeof` operator). Which of these data types does not exist in JavaScript?

  a. number<br/>
  b. boolean<br/>
  c. array<br/>
  d. object<br/>
  e. string<br/>

  Ans: c<br/>
  Explanation: 
    + JavaScript has a small set of primitive data types: `number`, `string`, `boolean`, `undefined` and `null`.
    + Anything that is not listed above is an object. Array or array is not a data type.


22. 10 or 010, that is the question!

  ```js
  var x = 010;
  var y = 10;

  console.log("x = " + x + " y = " + y);
  ```

  What will be displayed in the devtool console?

  a. `x = 8 y = 10`<br/
  b. `x = 10 y = 10`<br/

  Ans: a<br/>
  Explanation: 
    + Be careful: don't start an integer with 0 (zero), as JavaScript will understand it as an octal value.
    + 010 equals 8, which means 1 * 8^1 + 0 * 8^0


23. I like you

  ```js
  var a = 200; var b = a--;
  console.log("b = " + b + " a = " + a);
  ```

  What will be displayed in the devtool console?

  a. `b = 199 a = 199`<br/>
  b. `b = 200 a = 199`<br/>
  c. `b = 200 a = 200`<br/>

  Ans: b<br/>
  Explanation: The correct answer is "b = 200 a = 199", as a has been decremented AFTER its original value has been given to b.


24. Simple object

  ```js
  var john = {
      fullName='John Doe',
      city='New York',
      ssn="11-22-33-44"
  }
  ```

  Is the above code correct? (No/Yes)

  Ans: No<br/>
  Explanation: When declaring an object using { and }, the property name should be followed by a column, not the equal sign. The correct version is:
    ```js
    var john = {
        fullName:'John Doe',
        city: 'New York',
        ssn: "11-22-33-44" // no comma at the end of the last property
    }
    ```


25. Array length

  ```js
  var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
  ```

  What is the length of the array shown above?

  a. 6<br/>
  b. 7<br/>
  c. 8<br/>

  Ans: b<br/>
  Explanation: The length of an array is the number of elements it holds. console.log(daysOfWeek.length); will display 7 in the devtool console.


26. Array index

  ```js
  var daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
  ```

  What day corresponds to `daysOfWeek[2]`?

  a. 2 is not a correct index value<br/>
  b. 'Wednesday'<br/>
  c. 'Tuesday'<br/>

  Ans: b<br/>
  Explanation: Indexes start at 0. 'Monday' is at index 0, so 'Wednesday' is at index 2.


