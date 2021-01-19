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

[Demo - Sine function](src/01c-example01.html)

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


[Demo - Sine & Cosine functions](src/01c-example02.html)

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






#### Knowledge check 1.3.1

1. Which of these is a JavaScript array?

  a. var c = 10;<br/>
  b. var a = ['sin', 'cos', 'tan'];<br/>
  c. var b = {min:-1, max:1};<br/>

  Ans: <br/>
  Explanation: 








