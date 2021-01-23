# Module 1: Introduction to JavaScript

## 1.6 Simple JavaScript examples to play with

### 1.6.1 Introduction

This section does not detail the examples presented. Some of them are studied later in the course, some won't.

The examples are just here to bring some fun whilst making you play with some various uses of JavaScript. You are invited to look at their source code, and to tweak the examples. Do not worry if you don't understand how they work. We are just giving you "a taste" of JavaScript. There will be no graded exercises about them.


### 1.6.2 The devtool console

Using the `console.log(...)` instruction, you can __write messages to the devtool console__ of your browser. This is a common way to debug your code!

For example, let's say you added a button to your Web page, but nothing happens when you click on it.
It can be very difficult to spot your error without using the devtool console and `console.log(...)`!


#### Example

Let's check that some parts of the code you wrote are executed correctly.

[CodePen Demo](https://codepen.io/w3devcampus/pen/YNbvgP?editors=1000)

[Local Demo](src/01f-example01.html)

Normally, when the button is clicked, we should call the `addXToThePage()` function, which in turn should display the value of the variable x inside an HTML paragraph.

Let's check if the function is really executed. We need to add a `console.log("In the addXToThePage function");` as the first instruction of the function:

[CodePen Demo](https://codepen.io/w3devcampus/pen/YNbvoX)

[Local Demo](src/01f-example02.html)

And let's execute this with the devtool console open (use F12 on Windows, or Cmd-Alt-i on a Mac, or control-shift-i). First, as the provided example is located on CodePen, an online IDE, it's better to execute it in "debug mode". The online IDE will just display a page (see snapshot below) with the code running:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4n3srzt')"
    src    ="https://tinyurl.com/yx9v5zod"
    alt    ="CodePen debug mode"
    title  ="CodePen debug mode"
  />
</figure>

This action opens a new tab with only your code running in it (not the whole codepen IDE + your code!). Open the devtool console (F12 or control-shift-i or cmd-alt-i on Mac), and you should see this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y4n3srzt')"
    src    ="https://tinyurl.com/y6mwuy63"
    alt    ="Debug mode with console opened"
    title  ="Debug mode with console opened"
  />
</figure>

Now, press the button! An error message appears:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4n3srzt')"
    src    ="https://tinyurl.com/y4gehhvy"
    alt    ="Error message in the devtool console"
    title  ="Error message in the devtool console"
  />
</figure>

Apparently the function name is wrong, `addXToToThePage` does not exist. We can check the source code by clicking on the `YNbvoX:40` link on the right:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4n3srzt')"
    src    ="https://tinyurl.com/y2chtwgo"
    alt    ="Source code that fired the error"
    title  ="Source code that fired the error"
  />
</figure>

Ok, so our first error was that we typed the wrong name in the `onclick="..."`, the name we used : `AddXToToThePage` has "ToTo" instead of "To". Let's fix that now and try again:

[CodePen Demo](https://codepen.io/w3devcampus/pen/bgyjVo)

[Local Demo](src/01f-example03.html)

After we've changed the name of the function to the correct one, let's go in debug mode, open the devtool console and click the button. Here is what we get:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4n3srzt')"
    src    ="https://tinyurl.com/y3kjfv75"
    alt    ="console.log message displayed in the console, as well as another error"
    title  ="console.log message displayed in the console, as well as another error"
  />
</figure>

Ok, you understand the principle... by using `console.log(...)` with a string message as parameter, you can make the message appear in the devtool console, confirming that you have executed your code without error at least to this point...

Let's fix this "X"! We'll replace it with an "x" and everything should be ok now:

[CodePen Demo](https://codepen.io/w3devcampus/pen/egajBx)

[Local Demo](src/01f-example04.html)

You can click on the button now....


#### Going further with console.log

##### Displaying variable values

Instead of just displaying pure string messages, you can also use the "+" operator to concatenate variable values to the pure character strings.
Example :

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><strong><span class="str">"The value of x is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> x </span><span class="pun">+</span><span class="pln"> </span><span class="str">" and it's ok like that."</span></strong><span class="pun">);</span><span class="pln"> </span></li>
</ol></div>

We typed this code in the devtool console to check what it does:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4n3srzt')"
    src    ="https://tinyurl.com/y3m89wpy"
    alt    =Type js code into the console"
    title  =Type js code into the console"
  />
</figure>

You can use as many "+" as you like, the part right after the "+" will be turned into a string if the part in front is a string...

You can also use parentheses in order to display results of simple calculations:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">var</span><span class="pln"> x </span><span class="pun">=</span><span class="pln"> </span><span class="lit">2</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="kwd">var</span><span class="pln"> y </span><span class="pun">=</span><span class="pln"> </span><span class="lit">4</span><span class="pun">;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"x = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> x</span><span class="pun">);</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"y = "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> y</span><span class="pun">);</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">console</span><span class="pun">.</span><span class="pln">log</span><span class="pun">(</span><span class="str">"The value of (x+y) is "</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="pun">(</span><span class="pln">x</span><span class="pun">+</span><span class="pln">y</span><span class="pun">)</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> </span><span class="str">" and it's ok like that."</span><span class="pun">);</span><span class="pln"> </span></li>
</ol></div>

Result:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y4n3srzt')"
    src    ="https://tinyurl.com/y24ykgl4"
    alt    ="Expression displayed using console.log"
    title  ="Expression displayed using console.log"
  />
</figure>

You can use any operator (`+`, `-`, `/`, `*`, etc.), you are not limited to using the "+" operator.

And of course, you can use such code in your programs, not only in the devtool console :-)




#### Notes for 1.6.2 The devtool console

+ devtool console
  + a common way to debug JavaScript code
  + `console.log(...)`: instruction to write message to the devtool console
  + CodePen: click on the bottom left 'console' tab to display the console
  + Browser: open devtool, then click on 'cpnsole' tab
  + using concatentate operator `+` w/ `console.log(...)` for variable value


