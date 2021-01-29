# Module 2: Adding interactivity to HTML documents

## 2.3 Functions (part2): callbacks


### 2.3.1 Functions and callbacks

Let's see how to declare a function and a callback.


#### Functions

There are two ways to declare a function.

__1) Standard function declaration__

We've already seen that functions can be declared using this syntax:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> functionName</span><span class="pun">(</span><span class="pln">parameters</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="com">// code to be executed</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>

A function declared this way can be called like this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">functionName</span><span class="pun">(</span><span class="pln">parameters</span><span class="pun">);</span></li>
</ol></div>

Notice that we do not add a semicolon at the end of a function declaration. Semicolons are used to separate executable JavaScript statements, and a function declaration is not an executable statement.

Here is an example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/jmoBRj)

[Local Demo](src/02c-example01.html)

In the above example, the sum function returns a value, and the displayInPage function does not return anything.


__2) Use a function expression__

A JavaScript function can also be defined using an expression that can be stored in a variable. Then, the variable can be used as a function:

Here is a typical example:

[CodePen Demo](https://codepen.io/w3devcampus/pen/qmGmWj)

[Local Demo](src/02c-example02.html)

Notice how the `sum` and `displayInPage` functions have been declared. We used a variable to store the function expression, then we can call the functions using the variable name. And we added a semicolon at the end, since we executed a JavaScript instruction, giving a value to a variable.

The "function expression" is an "anonymous function", a function without a name, that represents a value that can be assigned to a variable. Then, the variable can be used to execute the function.

We say that functions are "first class objects" which can be manipulated like any other object/value in JavaScript.

This means that functions can also be used as parameters to other functions. In this case they are called "callbacks".


#### Callbacks

Indeed, as functions are first-class objects, we can pass a function as an argument, as a parameter to another function and later execute that passed-in function or even return it to be executed later. When we do this, we talk about callback functions in JavaScript: a function passed to another function, and executed inside the function we called.

All the examples of event listeners that you've seen used callback functions. Here is another one that registers mouse click listeners on the window object (the window objects represent the whole HTML document):

[CodePen Demo](https://codepen.io/w3devcampus/pen/OmYmVr)

[Local Demo](src/02c-example03.html)

In this case, the `processClick` function is passed as a parameter to the `addEventListener` method/function.

Callback functions are derived from a programming paradigm known as __functional programming__. They are very, very common in JavaScript. We'll use them a lot in the next section of the course, called "Handling events".


#### Notes for  2.3.1 Functions and callbacks

+ Functions
  + Syntax: two ways to declare function
    + standardard function declaration

      ```js
      function functionName(parameters) {
      // code to be executed
      }
      ```

    + using a function expression

      ```js
      var varName = function(parameters) {
        // code to be executed but not return anything
      };
      ```

  + standard declaration
    + not an executable statement
    + w/o semicolon at the end of a function declararion
    + semicolon used to separate executable JS statements
  + function expression
    + used a variable to store a function expression
    + calling the functions using the variable name
    + adding a semicolon at the end as a JS instruction
    + giving a value to a variable
    + an anonymous function
      + a function w/o function name
      + representing a value able to be assigned to a variable
      + variable able to be used to execute the function
    + 1st class object: manipulated like any other object/value in JS




