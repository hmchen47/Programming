# Module 1: Introduction to JavaScript

## 1.3 JavaScript overview


### 1.3.1 The best way to learn JavaScript

#### Live coding video: learn by the examples

<a href="https://edx-video.net/W3CJSIXX2016-V000600_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y4byq56f)


#### Best Practice to learn JavaScript

What is the best method to learn JavaScript?

__FIRST: learn by looking at and tweaking the code in the examples__

Well, there is no definitive answer to this question, but I'd recommend firstly looking at small examples, tweaking them and trying to guess what they do. You will rapidly discover that you can learn a lot just by modifying a few lines of JavaScript code, even if you do not understand the whole thing. 

During module 1, we give you some basics:

+ How to write a simple HTML/CSS/JS page,
+ Suggest some regular source code editors to use,
+ How to use online environments that run in the browser, and offer an "instant preview" of your creations. These tools are generally not suited for full scale projects, but are really valuable for testing and learning.
+ We present many examples (some short and some bigger ones) that will show what can be done with JavaScript. We strongly encourage you to tweak them, look at the code, download them on your hard disk, etc. Even if you do not understand everything, have a go at modifying them; further down this page we outline such an exercise.
+ In further modules, we will be revisiting the examples, and discussing them in greater detail and with fuller explanations.

__SECOND: take some time to carefully read the sections titled "What you've learnt / let's detail ...."__

During the course, we provide extra "reference pages" that detail some important parts of the language. For example, in a later section this week, we explain the concepts of "variables", "values", "operators", "output", etc.

__Here is an example - we provide some clues, but it's your job to tweak it!__

Here is an example that uses an external JavaScript library useful for plotting math functions. Look at the JavaScript code (click on the JS button) and try to guess where the function is specified, where the range for the x and y values is set, etc. Notice that you can use your mouse wheel to zoom in/out the function plot.

[CodePen Demo](https://codepen.io/w3devcampus/pen/PpYpjJ)

[Local Demo - Sine function](src/01c-example01.html)

By looking at this example (HTML and JS code), you note a few things:

Two lines in the HTML code that correspond to the inclusion in the document of some external JavaScript code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://d3js.org/d3.v3.min.js"</span><span class="tag">&gt;&lt;/script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://mauriciopoppe.github.io/function-plot/js/function-plot.js"</span><span class="tag">&gt;&lt;/script&gt;</span></li>
</ol></div><br/>

We will examine this soon in a later section of the course, but, in brief, it means that we will use the [d3js plotting library](https://d3js.org/), and another from github (a famous repository for open source contributions), and located in the github account of a person named "mauriciopoppe", the repository is named "function plot" ("[function plot JavaScript library](https://mauriciopoppe.github.io/function-plot/)").

Then, looking at the JavaScript code of the example (click the JS button on the [CodePen example](https://codepen.io/w3devcampus/pen/PpYpjJ)), we see:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">functionPlot</span><span class="pun">(<strong>{</strong></span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;target</span><span class="pun">:</span><span class="pln"> </span><span class="str">'#myFunction'</span><span class="pun">,</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;data</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;fn</span><span class="pun">:</span><span class="pln"> </span><span class="str">'sin(x)'</span><span class="pun">,</span><span class="pln"> </span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln"> </span><span class="str">'red'</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; }],</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; grid</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; yAxis</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln">domain</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[-</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">]},</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; xAxis</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span><span class="pln">domain</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">]}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun"><strong>}</strong>);</span></li>
</ol></div><br/>

Ok, the syntax looks strange if you are not used to JavaScript, but I bet that you guessed that the function plotted is "sin(x)", that the color of the curve is "red", that the range of the x values is [0, 2*PI], and the range of the y values is [-1, 1].

__Your job:__

1. try to plot sin(x^2),
1. try to change the domain for the x and y values,
1. try to change the color of the curve, etc.

To do this:

+ Edit directly the JS code in the embedded example, after a few seconds, you should see the updated result in the "Results" tab,
+ ...or just click on the "Edit on CodePen" title on the top right of the embedded example, then change  the code. Normally you should see the results of your modifications as soon as you stop typing (we call this "live coding"). (Here is [an example of what you can obtain](https://codepen.io/w3devcampus/pen/dvpEPZ) as a result).


__What can you guess from this example?__

#### A function call

You can think of this code in this way:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">functionPlot</span><span class="pun">(...);</span></li>
</ol></div><br/>

Where the "..." corresponds to some sort of parameter. When you see a name followed by two parentheses (maybe with something in between) followed by a ";", this is "__a function call__". 

A function is a piece of code defined somewhere else, that can accept parameters (the "thing" between the parentheses), and that will do something. In our case the function's name is "functionPlot" and we can assume (or we read the documentation of the library) that the goal of this function is to plot a mathematical function, as its name tells us.


#### Function parameters

The "thing" between parentheses is what we call "the parameters of the function": the data we pass to the function so that it can plot different math functions, with different colors, with different ranges for the x and y values, with or without a grid, etc.

Let's have a look at the parameters we used in our example (the ones you tweaked). They are in bold in the source code we saw earlier:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>target</strong></span><span class="pun">:</span><span class="pln"> </span><span class="str">'#myFunction'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>data</strong></span><span class="pun">:</span><span class="pln"> </span><span class="pun">[{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;fn</span><span class="pun">:</span><span class="pln"> </span><span class="str">'sin(x)'</span><span class="pun">,</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln"> </span><span class="str">'red'</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }],</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>grid</strong></span><span class="pun">:</span><span class="pln"> </span><span class="kwd">true</span><span class="pun">,</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>yAxis</strong></span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;domain</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[-</span><span class="lit">1</span><span class="pun">,</span><span class="pln"> </span><span class="lit">1</span><span class="pun">]</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; },</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>xAxis</strong></span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;domain</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">]</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>


#### JavaScript object

In JavaScript you can have simple values like: 2, 5, "hello", "3.14", and you may also encounter more "structured" values that we call "objects". In week 3 we will address JavaScript objects, but for the moment we will just present them through examples, without too much detail.

A JavaScript object can be defined by two braces with a set of properties/values inside, separated by a comma. Here is a simple object:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;givenName</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Michel"</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;familyName</span><span class="pun">:</span><span class="pln"> </span><span class="str">"Buffa"</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>

We use the ":" separator between the property name and its value. We use a comma between two properties, and we omit the comma after the last property (or before the ending brace).

In our examples, the properties of the object that is passed as a parameter to the functionPlot(...) call are in bold.

They are respectively:

+ __target:__ the CSS selector that corresponds to the HTML element that will contain the plot. Look at the HTML code (`<div id="myFunction"></div>`), the id value corresponds to `target`: "#myFunction" in the object.
+ __data:__ this is where we indicate the value of the function(s) to be plotted. We talk about this in greater detail below.
+ __grid:__ this can be true or false (we call these "boolean values") and indicates whether or not we want a grid to be drawn in the background.
+ __xAxis:__ the value specifies the domain (range) for the x values...
+ __yAxis:__ the value specifies the domain (range) for the y values...

Notice that after each property (`color`, `grid`, etc.) there is a ",". Notice that between the name of the properties and the value there is a ":", etc...


#### Embedded objects

If we look at the values of the `xAxis` and `yAxis` properties, they are also objects.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">xAxis</span><span class="pun">:</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; domain</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[</span><span class="lit">0</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">*</span><span class="typ">Math</span><span class="pun">.</span><span class="pln">PI</span><span class="pun">]</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div><br/>

The `data` object is even more complicated:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> data</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;fn</span><span class="pun">:</span><span class="pln"> </span><span class="str">'sin(x)'</span><span class="pun">,</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln"> </span><span class="str">'red'</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}],</span></li>
</ol></div><br/>

Instead of containing another object like `xAxis` or `yAxis`, it contains another sort of object, but inside brackets! __In JavaScript, brackets are used to create *arrays*__ of "things" (multiple, enumerable things). In this example, the array contains one single object that has two properties:

+ `fn`: the value of the function to be plotted, in this case sin(x),
+ `color`: the color of the curve

__In arrays, the different elements are separated by commas.__ Let's try to plot an additional function in our example. We will add f(x) = cos(x) to our example, with a different color:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">data</span><span class="pun">:</span><span class="pln"> </span><span class="pun">[</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pun">&nbsp; &nbsp; {</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;fn</span><span class="pun">:</span><span class="pln"> </span><span class="str">'sin(x)'</span><span class="pun">, &nbsp;// First function</span><span class="pln"></span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln"> </span><span class="str">'red'</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; },</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; {</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;fn</span><span class="pun">:</span><span class="pln"> </span><span class="str">'cos(x)'</span><span class="pun">, &nbsp;// second function</span><span class="pln"></span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln"> </span><span class="str">'blue'</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"></span><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pun">]</span></li>
</ol></div><br/>

[CodePen Demo - Sine & Cosine functions](https://codepen.io/w3devcampus/pen/KWPyeX)

[Local Demo - Sine & Cosine functions](src/01c-example02.html)

#### Conclusion

Just by looking at one example, and without going into the boring details, you saw:

+ How to plot a function using a third party library and how to include it in your code,
+ How to change some parameters without knowing JavaScript in depth,
+ You had a first encounter with concepts such as: "a function call", "function parameters", simple objects, embedded objects and arrays (we will discuss them as we move through the course, beginning in week 1 - as you will see very soon!).

Not bad ;-)


#### Notes for 1.3.1 The best way to learn JavaScript

+ Learning JavaScript
  + Best practice
    + read and tweak small JavaScript code snippet
    + carfully read the references that details some important parts of the language
  + example: external JavaScript code
    + [d3js plotting library](https://d3js.org/): `<script src="https://d3js.org/d3.v3.min.js"></script>`
    + [function plot JavaScript library](https://mauriciopoppe.github.io/function-plot/): `<script src="https://mauriciopoppe.github.io/function-plot/js/function-plot.js"></script>`
  + example: JavaScript code

    ```js
    functionPlot({
           target: '#myFunction',
           data: [{
           fn: 'sin(x)',
           color: 'red'
        }],
        grid: true,
        yAxis: {domain: [-1, 1]},
        xAxis: {domain: [0, 2*Math.PI]}
    });
    ```

    + `fn: 'sin(x)'`: function to plot
    + `color: 'red'`: curve line color
    + `xAxis: {domain: [0, 2*Math.PI]}`: range of the x values
    + `yAxis: {domain: [-1, 1]}`: range of the y values

+ JavaScript function
  + a piece of code defined somewhere else
  + accepting parameters to do something
  + function parameters: the data passed to the function
  + example: `functionPlot(...);`
    + function name: `functionPlot`
    + `...`: parametres
    + goal: plot a mathematical function

+ JavaScript object
  + defined by two braces `{...}` w/ a set of properties/values inside, separated by a comma
  + more structured values
  + example

    ```js
    {
       givenName: "Michel",
       familyName: "Buffa"
    }
    ```

    + `:`: seperator btw the property name and its value
    + `,`: separator btw two properties and omitting after the last property
  + example: passing parameter for `functionPlot(parameters)`

    ```js
    {
        target: '#myFunction',
        data: [{
                 fn: 'sin(x)',
                 color: 'red'
              }],
        grid: true,
        yAxis: {
             domain: [-1, 1]
        },
        xAxis: {
             domain: [0, 2*Math.PI]
        }
    }
    ```

    + `target`: the CSS selectorcorresponding to the HTML element that will contain the plot
    + `data`: the value of the function(s) to be plotted
    + `grid`: boolean value indicating whether or not a grid to be drawn iin the bacjkground
    + `xAxis`: specifying the domain (range) for the x values
    + `yAxis`: specifying the domain (range) for the y values

+ Embedded objects
  + arrays: using brackets to create arrays of things
  + different elements within an arrays seperated by commas `,`
  + example

    ```js
    data: [{
       fn: 'sin(x)',
       color: 'red'
    }],
    ```

#### Knowledge check 1.3.1

1. Which of these is a JavaScript array?

  a. var c = 10;<br/>
  b. var a = ['sin', 'cos', 'tan'];<br/>
  c. var b = {min:-1, max:1};<br/>

  Ans: b<br/>
  Explanation: In JavaScript, brackets are used to create arrays of "things" (multiple, enumerable things). __Braces__ are used to define JavaScript objects. The `var c = 10;` is a variable that contains a number, so it's neither an object nor an array.


### 1.3.2 What can be done with JavaScript

#### Live coding video: what can be done with JavaScript

<a href="https://edx-video.net/W3CJSIXX2016-V000900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y4jkxn7r)


What can be done with JavaScript:

#### Interact with the HTML and CSS content

__1) interact with the HTML and CSS content of a document, respond to events__

We have already seen three examples in previous parts of this week's course material.<hr/>

[CodePen Demo](https://codepen.io/w3devcampus/pen/pREjaE)

[Local Demo](src/01c-example03.html)

This first example used __the selector API__ for selecting a particular element in the document (the main title) and __*the DOM API*__ for modifying its content.

+ An API is an __*application programming interface*__. In the case of JavaScript, the DOM API is implemented natively by the browser, and you can call several functions/methods or access properties of the DOM:  an object that represents the document (the Web page).

It uses __the selector API__ to target a particular part of the DOM (in our case, the main title of the page), the HTML element with an `id` attribute equal to "mainTitle". The selector API uses the same syntax as CSS to select elements in the document. In our case, `"#mainTitle"` is a selector value that means "the element whose `id` is equal to `mainTitle`".

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> title </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#mainTitle"</span><span class="pun">);</span></li>
</ol></div><br/>

It uses __the DOM API__ to change the HTML content of the selected element:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">title</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"This new title has been changed from JavaScript!"</span><span class="pun">;</span></li>
</ol></div><br/>

__It listens to click events__ in order to call the `changeTitle()` function when we click on the button:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;button</span><span class="pln"> </span><span style="color: #ff0000;"><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">changeTitle</span><span class="pun">();</span></strong></span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Click me to change the title of the page</span><span class="tag">&lt;/button&gt;</span></li>
</ol></div><br/>

And it executes the whole action (changing the title text) in a _function_ (a block of code that is executed only when we call it by adding a parenthesis after its name, followed by a semi colon):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span style="color: #ff0000;"><strong><span class="kwd">function</span><span class="pln"> changeTitle</span><span class="pun">()</span></strong></span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> title </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#mainTitle"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; title</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"This new title has been changed from JavaScript!"</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div><hr/>

[CodePen Demo](https://codepen.io/w3devcampus/pen/bgwVvN)

[Local Demo](src/01c-example04.html)

The second example is nearly the same except that we changed the name of the function, and instead of using the DOM API to update the text content of the main title, __we use its `style` property to change its look and feel. Using the `style` property is a way of altering the CSS property values of this HTML element.__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> changeTitleCSSStyle</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp; var</span><span class="pln"> title </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#mainTitle"</span><span class="pun">);</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>title</strong></span><strong><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'black'</span><span class="pun">;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; title</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">backgroundColor </span><span class="pun">=</span><span class="pln"> </span><span class="str">"yellow"</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; title</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">border </span><span class="pun">=</span><span class="pln"> </span><span class="str">"5px dashed red"</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
</ol></div><br/>

`title` is in reality what we call "an object" and `style` is a property of the title object. The `style` is an object as well and has attributes that correspond to the different CSS properties we set. For example, `style.color` returns the color that element has set on it. By calling `title.style.color = "yellow";` you can apply the style change dynamically.

Some of you may be wondering what happens when the CSS property being set has a hyphen. The syntax has to be different here, because, for example, if you write `title.style.background-color`, JavaScript will try to subtract `color` from the `title.style.background` notation, which is not what you want to happen. To stop this problem from occurring, all the CSS properties are written out in CamelCase: the CSS name `background-color` becomes `backgroundColor`, `text-size` becomes `textSize`, `border-color` becomes `borderColor` etc.

Don't worry, we will return to this later in this course, these first examples are just here as an introduction.

The third example (outlined in the previous section), which showed how to plot math functions, illustrated that with a few lines of code you can reuse code from others (a third party JavaScript library).

#### Using Application APIs

__2) use numerous APIs in addition to the DOM and selector APIs: multimedia, drawing, animating, geolocation, webcam, etc.__

Your browser comes with a lot of different "libraries" that are called "standards APIs" for "application programming interfaces". Such APIs are "W3C standards" and are present in all Web browsers that follow the Web Standards. You will have APIs for manipulating multimedia (audio and video), geolocation (getting the longitude and latitude), orientation (on mobile devices), accessing the webcam or the microphone, etc. In a later section we will provide a set of examples that use some of the most useful APIs provided by your Web browser.

Example of an HTML page that embeds an interactive OpenStreet Map (you need to click the CodePen logo on top right to run this example. For security reasons it cannot be run inside this course page).

[CodePen Demo](https://codepen.io/w3devcampus/pen/LYVgyxE)

[Local Demo](src/01c-example05.html)


#### Working with remote HTTP server

__3) work with remote data / speak with a remote HTTP Web server__

You can also download or upload data from your browser to a remote Web server. When this is done from JavaScript the popular term to describe such operations is "AjaX" (Asynchronous JAvascript and Xml), even though XML is not used in any examples you'll see in this course (XML is a language for describing structured data that was very popular a few years ago).

Here is an example that will display the current and past members of famous rock bands:

[CodePen Demo](https://codepen.io/w3devcampus/pen/wJwpKq)

[Local Demo](src/01c-example06.html)


#### Notes for 1.3.2 What can be done with JavaScript

+ Interact w/ HTML and CSS
  + API: an application programming interface
  + DOM: an object representing the document
  + the selector API:
    + targeting the particular part of the DOM
    + using the same syntax as CSS to select element in the document
    + example: `var title = document.querySelector("#mainTitle");`
  + the DOM API:
    + modifying the HTML content or the style of HTML elements
    + `.innerHTML`
      + modifying content of a document
      + implemented natively by the browser
      + calling serval functions/methods or access properties of the DOM
      + example: `title.innerHTML = "This new title has been changed from JavaScript!";`
    + `onclick`
      + listening to click event to call a specific function
      + executing the whole action in the called function
      + example" `<button onclick="changeTitle();">Click me to change the title of the page</button>`

        ```js
        function changeTitle() {
            var title = document.querySelector("#mainTitle");
            title.innerHTML = "This new title has been changed from JavaScript!";
        }
        ```

  + `style` property
    + changing the look and feel of the document
    + `style`: an object w/ attributes corresponding to the different CSS properties
    + syntax different from CSS: instead of `-` in CSS and using CamelCase
    + example: `title.style.color = 'black';`, `title.style.backgroundColor = "yellow";`,  `title.style.border = "5px dashed red";`
      + `title`: an object
      + `style`: a property of the title object

+ Application APIs
  + bowsers w/ many different libraries as standard APIs
  + W3C standards
  + all browseers following the Web Standards
  + standard APIs
    + multimedia: audio & video
    + geolocation: getting the longitude and latitude
    + orientation: on mobile devices
    + accessing webcam or microphone, etc.

+ Remote HTTP server
  + download and upload data from browser to remote Web server
  + __AjaX__ (Asynchronous JAvascript and Xml): term used in JS to download & upload data


#### Knowledge check 1.3.2

1. In JavaScript, in order to change the content of an HTML document or the CSS style of HTML elements, we use:

  a. The selector and the DOM API<br/>
  b. The HTML API<br/>
  c. The CSS API<br/>

  Ans: a<br/>
  Explanation:
    + In JavaScript, in order to dynamically modify an HTML document (content or style), we use the selector API to target a particular part of the DOM, then the DOM API to modify the HTML content or the style of HTML elements.
    + For example:

      ```js
      var title = document.querySelector("#mainTitle");
      title.innerHTML = "This new title has been changed from JavaScript!";
      ```


### 1.3.3 Source code editors to use

#### Foreword

<p class="exampleHTML">Michel Buffa, author of this course: <br><br><em>"When I work locally, with files located on my computer hard drive, I use the Sublime Text source code editor, Visual Studio Code, WebStorm, NetBeans, depending on the size of the project I'm working on. <br>- For testing simple examples, I mainly use the JsBin.com online code editor.<br>- For embedding online examples in this course, I use the CodePen.io online code editor.<br>- For choosing a CSS color, shadow, text-shadow, gradients, etc. I use the LiveWeave online code editor."</em></p>


#### Traditional source code editors

You can use any source code editor that has good support for HTML, CSS and JavaScript files. For this course, you are free to use whichever you prefer. However, there are some in particular that we recommend.

##### Sublime Text

[Sublime Text](https://www.sublimetext.com/) is a very powerful, multi-platform source code editor, it's semi-free (you can use it without paying, it will pop up a dialog asking you to buy it once in a while, but not very often). Sublime text supports hundreds of plugins to enhance its features.

##### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a free, open source, multi-platform editor by Microsoft.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ged569" ismap target="_blank">
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y3x4goqr"
      alt  ="Snapshot of Sublime Text editing an html/css/js project"
      title="Snapshot of Sublime Text editing an html/css/js project"
    >
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y5d43x65"
      alt  ="Snapshot of a Visual Studio code editing an HTML/CSS/JS project"
      title="Snapshot of a Visual Studio code editing an HTML/CSS/JS project"
    >
  </a>
</div>

##### Other tools

Free of charge:

+ [Atom source](https://atom.io/) code editor (note that Visual Studio code is based on Atom).
+ [Brackets source](http://brackets.io/) code editor.
+ [NotePad++](https://notepad-plus-plus.org/) (Windows only)
+ [NetBeans](https://netbeans.org/) and [Eclipse](https://eclipse.org/): very powerful IDEs (integrated development environments), but heavier than all the "lightweight" source editors that we've talked about so far. More dedicated to "mid-size/large-size projects", more for pro developers that are also looking for good support for server-side languages such as Java, Python, PHP, etc.

Not free of charge:

+ [IDEs by JetBrains.com](https://www.jetbrains.com/) have a very good reputation and can be obtained for free if you are an academic customer (student or teacher). The [WebStorm](https://www.jetbrains.com/webstorm) IDE is a very good mid-weight tool for developing HTML/CSS/JS/NodeJS code.
+ [BBedit](https://www.barebones.com/products/bbedit/) (for Macs): source code editor for mac with support for Web languages.

#### Online editors/IDEs

To help you practice for the duration of the course, you will use the following tools. Pretty much all the course's examples will use these tools.

##### JsBin.com

[JS Bin](https://jsbin.com/) is an open source collaborative Web development debugging tool. Most of the examples you will find in this course are either on JsBin or on CodePen.

Tutorials can be found on the Web (such as [this one](https://code.tutsplus.com/tutorials/javascript-tools-of-the-trade-jsbin--net-36843)) or on YouTube. The tool is really simple: just open the link to the provided examples, look at the code, look at the result, etc. And you can modify the examples as you like, you can also modify / clone / save / share them. Keep in mind that it's always better to be logged in (it's free) if you do not want to lose your work.

In our opinion, JsBin is the best online IDE for "live coding": typing and seeing what you are doing in real time, monitoring error messages in the console tab, and debugging your code. We will mainly use this tool for the live coding videos.

##### CodePen.io

[CodePen](https://codepen.io/) is similar to JSBin except that its Web site includes a search engine, which is very useful for finding out what others  have developed. Looking for a nice HTML5/CSS button style? Just search for "button", etc. It's also easier for us to embed HTML/CSS/JS examples in this course with CodePen than with other online IDEs; this is why so many "pens" are embedded in the course pages.

##### Plunker

[Plunker](https://plnkr.co/) allows us to work online with separate files. So when we have no choice but to use separate files, we might use this tool.

##### LiveWeave

[LiveWeave](https://liveweave.com/) is great for writing CSS code or for embedding SVG Graphics in an HTML document, as it includes online wizards and interactive editors. We use it when we have problems with CSS shadows, CSS colors or gradients, or when we want to include an SVG arrow in a document.

##### JsFiddle

[JsFiddle](https://jsfiddle.net/) is very similar to JsBin and CodePen in terms of features. 


<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ged569" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yyegf3tm"
      alt  ="JSBin example"
      title="JSBin example"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yxzm2db2"
      alt  ="Snapshot of a CodePen example"
      title="Snapshot of a CodePen example"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y25ey7fo"
      alt  ="Snapshot of a Plunker example"
      title="Snapshot of a Plunker example"
    >
  </a>
</div>

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ged569" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/yxw374k2"
      alt  ="LiveWeave code editor"
      title="LiveWeave code editor"
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y4ayy6yd"
      alt  ="LiveWeave CSS editor"
      title="LiveWeave CSS editor"
    >
  </a>
</div>

##### Other tools

There are many other online IDEs and new ones appear each year. If you want a real, heavyweight online IDE that has nearly all the features offered by "big IDEs" such as Eclipse, NetBeans and WebStorm, take a look at the [Cloud9 IDE](https://c9.io/). It's free and will enable you to develop huge projects, that can include many files, it supports uploaded assets such as images, videos and sound files.  Furthermore, like Google Docs, it will support multiple users working at the same time on the same project, even on the same file. It's a real collaborative environment.

Michel Buffa, author of this course, developed a whole multitrack audio player this way. See these screenshots:

This application (available [online](https://mainline.i3s.unice.fr/)). And 100% of the development was done in a Web browser, by Michel Buffa and two friends, using the c9.io (Cloud 9) IDE (to see if online IDEs were a valuable approach):

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ged569" ismap target="_blank">
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y2daccc7"
      alt  ="multitrack audio player"
      title="multitrack audio player"
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y3eltq52"
      alt  ="C9 ide"
      title="C9 ide"
    >
  </a>
</div>

#### Note for 1.3.3 Source code editors to use

+ Source code editors / IDEs
  + traditional
    + [Sublime Text](https://www.sublimetext.com/)
    + [Visual Studio Code](https://code.visualstudio.com/)
    + [Atom source](https://atom.io/) code editor (based on Atom).
    + [Brackets source](http://brackets.io/) code editor.
    + [NotePad++](https://notepad-plus-plus.org/) (Windows only)
    + [NetBeans](https://netbeans.org/): big IDE
    + [Eclipse](https://eclipse.org/): big IDE
  + commercial
    + [IDEs by JetBrains.com](https://www.jetbrains.com/)
    + [BBedit](https://www.barebones.com/products/bbedit/) (for Macs)
    + [WebStorm](https://www.jetbrains.com/webstorm) IDE: mid-weight tool for HTML/CSS/JS/NodeJS
  + online editors / IDEs
    + [JS Bin](https://jsbin.com/): best online editor for "live coding"
    + [CodePen](https://codepen.io/): search engine to find examples
    + [Plunker](https://plnkr.co/): separate files
    + [LiveWeave](https://liveweave.com/): CSS code or embedding SVG Graphics in an HTML document
    + [JsFiddle](https://jsfiddle.net/)
    + [Cloud9 IDE](https://c9.io/): huge project


### 1.3.4 Where to put JavaScript code

#### Live coding video: where to put JavaScript code?

<a href="https://edx-video.net/W3CJSIXX2016-V000700_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y2ushwmy)


#### JavaScript code can be located in different places

1. In your HTML code between `<script>` and `</script>` tag
2. In local files, usually ending with the .js suffix (i.e: in a script.js file), and included using, for example, a syntax such as: `<script src="style.js"></script>` tag
3. In external files located on the Web, using their URLs, also using the `<script src="https://www.aserver.com/..../js/script.js"></script>` tag

Here are some examples:


#### Examples 

__Example #1:  the JavaScript code is included in an HTML file using the `<script>...</script>` tag__

__First variant: in the `<body>..</body>` of the HTML document__

Typically:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">...</span></li>
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&nbsp;&lt;script&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="kwd">&nbsp; &nbsp;var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// show a message in the body of the html document</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"&lt;b&gt;JavaScript code executed. The value of the variable x is: "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> x </span><span class="pun">+</span><span class="pln"> </span><span class="str">"&lt;/b&gt;"</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><span class="com">&nbsp; &nbsp;// also print a message in the devtool console</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"JavaScript code executed"</span><span class="pun">);</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp;&lt;/script&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">...</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZLBPpY)

[Local Demo](src/01c-example07.html)


Old JavaScript examples may use a `type` attribute: `<script type="text/javascript">.`

The type attribute is now obsolete and should be ignored.

__Second variant: in the `<head>...</head>` of the document__

In this example, the `<script>...</script>` element is placed in the `<head>..</head>` section of an HTML page.

This time, we placed a JavaScript function that is invoked (called) when a button is clicked:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; <strong>&lt;script&gt;</strong></span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="kwd">&nbsp; &nbsp; &nbsp;function</span><span class="pln"> addSomeText</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="com">&nbsp; &nbsp; &nbsp; &nbsp; // append a message in the body of the html document</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"&lt;br&gt;Function executed!"</span><span class="pun">;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="pun">&nbsp; &nbsp; &nbsp;}</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="tag">&nbsp; &lt;/script&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">addSomeText</span><span class="pun">();</span><span class="atv">"</span></strong><span class="tag">&gt;</span><span class="pln">Click me to call a JavaScript function that will add </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;some content to this document</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/button&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

Here is this second example on CodePen:

[CodePen Demo](https://codepen.io/w3devcampus/pen/apBMYJ)

[Local Demo](src/01c-example08.html)

__Example #2: put the JavaScript code in local `.js` files__

Putting JavaScript code in external scripts files is easy, and offers many advantages:

1. It separates HTML and code (and also CSS code, if you use external CSS files)
1. It makes HTML and JavaScript easier to read and maintain
1. JavaScript files can be reused more easily in other projects
1. Cached JavaScript files can speed up page loads

A typical example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"css/style.css"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;<strong>&lt;script</strong></span><strong><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/script.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
</ol></div><br/>

__To use an external JavaScript file:__

1. In the HTML, put the name of the script file in the `src` (source) attribute of a `<script>` tag, like in the typical example above,
1. JavaScript files must end with the `.js` extension,
1. Do no use any `<script>...</script>` tag in a `.js` file!
1. Using an external JavaScript file with `<script src="..."></script>` is 100% equivalent to using `<script>...</script>` with the file content between the opening and closing tags. 
1. It's possible to use more than one JavaScript file, just use multiple `<script src="..."></script>`

Example that uses more than one JavaScript file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"css/style.css"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"></span><span class="tag">&nbsp; &nbsp;<strong>&lt;script</strong></span><strong><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/script1.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="tag"><strong>&nbsp; &nbsp;&lt;script</strong><strong style="color: #3c3c3c;"><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/script2.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="tag"><strong style="color: #3c3c3c;"><span class="tag"><strong>&nbsp; &nbsp;&lt;script</strong><strong style="color: #3c3c3c;"><span class="pln">&nbsp;</span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/anotherOne.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong><br></span></strong></span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="tag"><strong style="color: #3c3c3c;"><span class="tag"><strong style="color: #3c3c3c;"><span class="tag">&nbsp; &nbsp;...</span></strong></span></strong></span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
</ol></div><br/>

#### A typical HTML/CSS/JS project folder structure, when working with external local files

It is good practice to locate CSS files in a `css` subfolder, and JavaScript files in a `js` subfolder.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/yyge6mgp')"
    src    ="https://tinyurl.com/y5q92um6"
    alt    ="A typical HTML/CSS/JS project folder structure"
    title  ="A typical HTML/CSS/JS project folder structure"
  />
</figure>

In this example, we have just one CSS file and one JavaScript file:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/yyge6mgp')"
    src    ="https://tinyurl.com/y5l8ok5h"
    alt    ="A typical HTML/CSS/JS project folder structure, with folders expanded"
    title  ="A typical HTML/CSS/JS project folder structure, with folders expanded"
  />
</figure>

Content of the index.html file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;">&nbsp; &nbsp;...</li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"></span><strong><span class="tag">&nbsp; &nbsp;&lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"css/style.css"</span><span class="tag">&gt;</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="pln"></span><span class="tag">&nbsp; &nbsp;&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"js/script.js"</span><span class="tag">&gt;&lt;/script&gt;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/head&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;h1&gt;</span><span class="pln">Example 3: JavaScript and CSS in local files!</span><span class="tag">&lt;/h1&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;button</span><span class="pln"> </span><strong><span class="atn">onclick</span><span class="pun">=</span><span class="atv">"</span><span class="pln">addSomeText</span><span class="pun">();</span></strong><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">Click me to call a JavaScript function that will add some content to this document</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div><br/>

Content of the js/script.js file (JavaScript file):

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">function</span><span class="pln"> addSomeText</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">+=</span><span class="pln"> </span><span class="str">"&lt;p&gt;Function executed!&lt;/p&gt;"</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>

Content of the style.css file:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln">p </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;color</span><span class="pun">:</span><span class="pln">green</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div><br/>

How to run this example:

1. Download the zip file of this project: [Example_3.zip](https://tinyurl.com/y5lcfxon)
1. Unzip/unarchive it somewhere
1. Double click the index.html file, this will open your Web browser and load the index.html file.
1. Click on the button in the page


__Example #3: use external references to JavaScript files/libraries located on the Web__

External JavaScript libraries (they are just big JS files) can be also referenced with a full URL, like in this example:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://cdnjs.cloudflare.com/ajax/libs/paper.js/0.22/paper.js"</span><span class="tag">&gt;&lt;/script&gt;</span></li>
</ol></div><br/>

Here, we just included in our HTML document the excellent [paperJS](http://paperjs.org/) library that can be used to make fancy animations in the HTML canvas element - we will use it later in the course. 

Once the library is included, the JavaScript code you will write can call functions located in this library. This "reuse existing" work made by others is really common when working on JavaScript projects.

Here is a running example that uses the paperJS library, included using an external URL:

[CodePen Demo](https://codepen.io/w3devcampus/pen/VPmNWg)

[Local Demo](src/01c-example09.html)


#### Notes for 1.3.4 Where to put JavaScript code

+ Locations of JavaScript Code
  + in HTML code between `<script>` and `</script>` tag, either within `<body>...</body>` or `<head>...</head>`
  + external file
    + in local files, usually ending w/ `.js` suffix, e.g., `<script src="style.js"></script>`
    + in external file located on the Web, e.g., `<script src="https://www.aserver.com/..../js/script.js"></script>`
    + advantages
      + separate HTML and code
      + easier to read and maintain
      + reuse JavaScript code
      + cached JavaScript files to speed up page loads
    + usage
      + link the script file w/ `src` attribute of `<script>` tag
      + JavaScript file must end w/ `.js`
      + no `<script>...</script>` in '`.js` file
      + external JavaScript file w/ `<script src="..."></script>` = `<script>...</script>` in HTML
      + multiple JavaScript allowed w/ `<script src="..."></script>`

+ Folder structure of Web project
  + CSS files in `css` subfolder
  + JavaScript file in `js` subfolder


#### Knowledge check 1.3.4

1. Which of these statements are correct? (two correct answers!)

  a. JavaScript code can only be located between the `<script>...</script>` tags<br/>
  b. JavaScript code can be located outside of the HTML file and included using `<script src=...>...</script>`<br/>
  c. The `<script>` opening tag always come with a `</script>` closing tag<br/>
  d. We cannot have more than one external JavaScript file<br/>
  
  Ans: bc<br/>
  Explanation:
    + JavaScript code, when located in external files, is not included inside `<script>...</script>` tags.
    + We can have as many external JS file as we like, just duplicate `<script src="file1.js"></script>`, `<script src="file2.js"></script>`, etc.
    + The `<script>` tag cannot be used without a closing `</script>` tag.


### 1.3.5 How to debug JavaScript

#### Live coding video: how to open the browser devtool console

<a href="https://edx-video.net/W3CJSIXX2016-V001100_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y4fqtb4b)

Let's introduce what is debugging.

#### You will make errors!

When you are developing a Web Application that contains JavaScript code, you will make errors. 

<span style="color: red;">Repeat after me: "I WILL MAKE ERRORS!" ; "I WILL MAKE ERRORS!"</span>

So there will be error messages, and you will need to print messages for debugging your code. We will see more advanced debugging techniques at different points in this course, but for the moment, let's see the basics of JavaScript debugging: seeing error messages in the devtool console, or in the "console tab" of your source code editor.

We will not look at the JavaScript syntax here, but more at "JavaScript in the browser", how it works, how to start writing code, etc.

First of all, you need to find a way to debug your code and see errors. If your work does not produce any results, you need to know why!

#### Browser devtools

__Your Swiss army knife: your browser devtools, especially the devtool console!__

For this you will use __the dev. tools of your browser__. Press _F12_ (or ctrl-shift-i) in Windows or cmd-option-i in MacOS to open the dev. tools, then go to the console tab: __this is where errors will be displayed__, or messages of your own (use the `console.log(string)` JavaScript function in the JavaScript code embedded in your html page). In the console, you will be able to type any JavaScript command.

Let's look at [this example on JS Bin](http://jsbin.com/moqimuz/edit?html,console,output):

<div class="rj_insertcode" style="color: #444444; font-family: 'PT Sans', Arial, Helvetica, sans-serif; font-size: 13px; line-height: 25px;">
<div class="rj_insertcode_html4strict" style="overflow: auto; width: 546.174987792969px; height: auto; border: 1px solid #054b6e; background: #f8f8f8;">
<table class="html4strict" style="max-width: 100%; border-spacing: 0px; width: 545.599975585938px; background-color: transparent;">
<tbody>
<tr class="li1">
<td style="width: 1px; vertical-align: top; color: #676f73; border-right-style: dotted; border-right-color: #dddddd; font-size: 12px; text-align: right; background: #f0f0f0;">
<pre style="padding: 0px 4px; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; color: #333333; border-radius: 4px; margin-top: 0px; margin-bottom: 0px; line-height: 20px; word-break: normal; border: 1px solid rgba(0, 0, 0, 0.14902); vertical-align: top; background: none;">1
2
3
4
5
6
7
8
9
10
11
12
13
</pre>
</td>
<td style="margin-top: 0px; margin-bottom: 0px; vertical-align: top; padding: 0px 4px; font-size: 12px; word-break: normal; background: none;">
<pre style="padding: 0px 4px; font-family: Monaco, Menlo, Consolas, 'Courier New', monospace; font-size: 12px; color: #333333; border-radius: 4px; margin-top: 0px; margin-bottom: 0px; line-height: 20px; word-break: normal; border: 1px solid rgba(0, 0, 0, 0.14902); vertical-align: top; background: none;"><span style="color: #00bbdd;">&lt;!DOCTYPE html&gt;</span>
<span style="color: #009900;">&lt;<span style="color: #000000; font-weight: bold;"><a style="color: purple;" href="http://december.com/html/4/element/html.html">html</a> lang="en</span>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="http://december.com/html/4/element/head.html"><span style="color: #000000; font-weight: bold;">head</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="http://december.com/html/4/element/meta.html"><span style="color: #000000; font-weight: bold;">meta</span></a> <span style="color: #000066;">charset</span><span style="color: #66cc66;">=</span>utf-<span style="color: #cc66cc;">8</span> <span style="color: #66cc66;">/</span>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="http://december.com/html/4/element/title.html"><span style="color: #000000; font-weight: bold;">title</span></a>&gt;</span>Web Audio API<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="http://december.com/html/4/element/title.html"><span style="color: #000000; font-weight: bold;">title</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a>&gt;</span>
&nbsp; &nbsp;console.log("Some JavaScript code has been executed");
&nbsp; <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="http://december.com/html/4/element/script.html"><span style="color: #000000; font-weight: bold;">script</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="http://december.com/html/4/element/head.html"><span style="color: #000000; font-weight: bold;">head</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="http://december.com/html/4/element/body.html"><span style="color: #000000; font-weight: bold;">body</span></a>&gt;</span>
&nbsp; &nbsp; <span style="color: #009900;">&lt;<a style="color: purple;" href="http://december.com/html/4/element/h1.html"><span style="color: #000000; font-weight: bold;">h1</span></a>&gt;</span>JavaScript debugging using the dev tool console<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="http://december.com/html/4/element/h1.html"><span style="color: #000000; font-weight: bold;">h1</span></a>&gt;</span>
&nbsp; <span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="http://december.com/html/4/element/body.html"><span style="color: #000000; font-weight: bold;">body</span></a>&gt;</span>
<span style="color: #009900;">&lt;<span style="color: #66cc66;">/</span><a style="color: purple;" href="http://december.com/html/4/element/html.html"><span style="color: #000000; font-weight: bold;">html</span></a>&gt;</span></pre>
</td>
</tr>
</tbody>
</table>
</div>
</div>

The simplest way to add JavaScript code in an HTML page is to use the `<script>...</script>` element.

__The code in this example is executed sequentially when the page is loaded:__ the JavaScript code is executed before the browser could see the rest of the page (as the `<script></script>` is located before the `<body>`).

The H1 element, for example, does not exist in the Document Object Model, and has not yet been displayed when the JavaScript code is executed. If we move the `<script></script>` at the end of the document, then the H1 would have been built before the JavaScript code is executed.

The only line of code we have is `console.log("Some JavaScript code has been executed");`

This means "display in the JavaScript console the message...". If we open the console tab provided by jsbin.com in a dedicated tab (that redirects all `console.log()` messages), and re-execute the page (just type a space at the end of a line to re-render the page and display the message in the console), we see the message in the console tab, as well as in the dev. tools console. This is illustrated by the image below:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y4x46h23')"
    src    ="https://tinyurl.com/yy3bdxlj"
    alt    ="Snapshot of a JavaScript console view (#1)"
    title  ="Snapshot of a JavaScript console view (#1)"
  />
</figure>

It is also possible to use the "real dev. tool console", and for this, I recommend running the application in a single window, not in the JsBin editor. Press the black arrow on the top right of the output window - this will render the page as a standalone Web page, then press F12. You should see:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y4x46h23')"
    src    ="https://tinyurl.com/yyjyhe5b"
    alt    ="View of the JavaScript console"
    title  ="View of the JavaScript console"
  />
</figure>

Ok, now, let's make an error: change `console.log()` into `consollle.log()`. Let's see what happens:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y4x46h23')"
    src    ="https://tinyurl.com/yyegf3tm"
    alt    ="View of the javascript console showing an error"
    title  ="View of the javascript console showing an error"
  />
</figure>

And if we run it standalone and use the dev. tool console:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y4x46h23')"
    src    ="https://tinyurl.com/y2cp227z"
    alt    ="View of the JavaScript console (showing the line that caused the error)"
    title  ="View of the JavaScript console (showing the line that caused the error)"
  />
</figure>

And if we click on the line number to the right, the dev. tool shows the source code centered on the line that caused the error:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 25vw;"
    onclick="window.open('https://tinyurl.com/y4x46h23')"
    src    ="https://tinyurl.com/y4xkv2jo"
    alt    ="View of the JavaScript console"
    title  ="View of the JavaScript console"
  />
</figure>

Without such tools, debugging JavaScript code is impossible. So you need to look at some basic tutorials on how to use the dev. tools of your browsers, since they differ from one another in the way they work - although the principles remain the same.


#### Note for 1.3.5 How to debug JavaScript

+ Debugging w/ JavaScript
  + error messages: printing message for debugging code
  + basics of debuging: seeing error messages
    + in the devtool console
    + in the "console tab" of source code editor


