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


### 1.6.3 Modifying an HTML document

Don't worry if we do not explain all the details of this example. In the first module, we're giving you "a taste" of what we can do with JavaScript. Over the following modules, we'll delve deeper into the details... 

We've already seen some examples that modify the content of the document __dynamically__. We changed a title by clicking on a button, we displayed the value of a variable named x in the previous section, etc.

The browser comes with some very powerful APIs (Application Programming Interfaces - a set of predefined objects/functions/variables you can use):

1. "The selection API" is used for "selecting elements in the document". It uses the same syntax as CSS selectors. 
1. The "DOM API" for "Document Object Model" API. When we used `document.body.innerHTML += "<p>The value of x is " + x + "</p>";` in a previous example, we used the DOM API for adding content to the body of the page (page = document).
1. Another API is called the HTML Table JavaScript API, and is useful for building tables on the fly.
1. etc.

[CodePen Demo](https://codepen.io/w3devcampus/pen/pRmZqY)

[Local Demo](src/01f-example05.html)

Just click the button to build the HTML table dynamically. You should see this:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y5k2vnul')"
    src    ="https://tinyurl.com/y6cjnbdg"
    alt    ="Dynamic table"
    title  ="Dynamic table"
  />
</figure>


#### Notes for 1.6.3 Modifying an HTML document

+ Modifying HTML document
  + selection API: used for "selecting elements in the document", e.g., `var tableBody = document.querySelector("#tableContactBody");`
  + DOM API: used for adding content to the body of the page (page = document), e.g., `document.body.innerHTML += "<p>The value of x is " + x + "</p>";`
  + HTML Table JavaScript API: useful for building tables on the fly; e.g.,
    + add new row to end of the table: `var newRow   = tableBody.insertRow();`
    + add cell for the row: `var firstNameCell  = newRow.insertCell(); firstNameCell.innerHTML = firstName;`


### 1.6.4 Modifying CSS styles on the fly

We've already seen some examples in which we modify the style of some parts of a document using JavaScript. Here we show another example of what can be done.

#### Examples

__Example #1: change common properties (color, border, background color)__

[CodePen Demo](https://codepen.io/w3devcampus/pen/rjgQgN)

[Local Demo](src/01f-example06.html)


__Example #2: change the background image property using an external image__

[CodePen Demo](https://codepen.io/w3devcampus/pen/MJdzMM)

[Local Demo](src/01f-example07.html)


__Example #3: Use the background image as a sprite sheet - animate Mario!__

[CodePen Demo](https://codepen.io/w3devcampus/pen/ygWGBd)

[Local Demo](src/01f-example08.html)

Notice how the CSS properties change when we use them from JavaScript:

+ `background-color` (CSS) becomes `backgroundColor` (JS)
+ `margin-left` (CSS) becomes `marginLeft` (JS)
+ etc.

And the positions, widths and heights are always string values. In our example we used pixel units and a percentage, so we need to add the "px" and "%" character(s) when we manipulate these properties from JavaScript.


#### Notes for 1.6.4 Modifying CSS styles on the fly

+ Modifying CSS style
  + change the CSS property names to CamelCase as JaVaScript variable names
  + position values (height & width): string values w/ "px" and "%"
  + change common properties (color, border, background color), e.g.,
    + select element: `divElem = document.querySelector("#theDiv");`
    + modify CSS: `divElem.style.border = "5px dashed purple"; divElem.style.padding = "10px"; divElem.style.backgroundColor = "lightGreen";`
  + change the background image property w/ external image, e.g.,
    + select element: `divElm = document.querySelector("#theDiv");`
    + modify background: `divElem.innerHTML = ""; divElem.style.width= "100%"; divElem.style.height = "300px"; divElem.style.backgroundImage = "url(https://mainline.i3s.unice.fr/mooc/marioSprite.png)";`
  + use the background image as sprite sheet
    + select element: `divElem = document.querySelector("#theDiv");`
    + animate images: `drawMario(currentImage); currentImage = (currentImage +1) % 3;`
    + draw images

      ```js
      function drawMario(indexImage) {
        // set the left pos of the div using the left margin
        divElem.style.marginLeft = leftPos + "px";
        // change the width and height of the div
        divElem.style.width = "22px";
        divElem.style.height = "32px";
        // remove the text inside the div
        divElem.innerHTML = "";
        // set the background image
        divElem.style.backgroundImage = "url(https://mainline.i3s.unice.fr/mooc/marioSprite.png)";
        // remove the background color
        divElem.style.backgroundColor = "transparent";
        // select the starting pos in the background image
        var offset = indexImage * 24;
        divElem.style.backgroundPosition  = offset + "px";
      }
      ```


### 1.6.5 Adding interactivity with events

With JavaScript, you can react to user interactions (keyboard, mouse, gamepad), to changes in the lifecycle of your document (page has just loaded or resized, screen has been rotated on a mobile device), or to be notified when a long process has been completed (loading a large image or sound from the network).

We've already seen how we can make a `<button>` react to a mouse click with `<button onclick="...">Click me</button>`

Below, we outline some extra examples. In the next course module, we will go into detail about events, and in the following modules, we will study some of the most useful events in even greater depth.


#### Examples

__Example #1: use input events on an HTML input field__

[CodePen Demo](https://codepen.io/w3devcampus/pen/jyoXGN)

[Local Demo](src/01f-example09.html)


__Example #2: listen to mouse events in an HTML5 canvas__

The HTML5 canvas is useful for drawing and animating at 60 frames/second. Very detailed tutorials are provided in the W3C [HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-coding-essentials-and-best-practices) course, while the W3Cx [HTML5 Apps and Games](https://www.edx.org/course/html5-apps-and-games) MOOC addresses how to write video games using the canvas 2D API.

In this JS introductory course, we use HTML5 canvas to draw curves, to make a small game, etc. Small and diverse examples for illustrating some JavaScript data structures such as Arrays or Objects are going to be presented.

[CodePen Demo](https://codepen.io/w3devcampus/pen/QdRzJw)

[Local Demo](src/01f-example10.html)


__Example #3: a paint program - click and drag mouse, then release__

[CodePen Demo](https://codepen.io/w3devcampus/pen/VPOqJG)

[Local Demo](src/01f-example11.html)


__Example #5: move a monster in an HTML5 canvas using left and right arrow keys__

[CodePen Demo](https://codepen.io/w3devcampus/pen/ygWZEP)

[Local Demo](src/01f-example12.html)


#### Notes for 1.6.5 Adding interactivity with events

+ Interaction w/ events
  + possible actions able to react to
    + user interactions (keyboard, mouse, gamepad)
    + changes in the lifecycle of document, e.g., pages loading or resizing, screen rotation on a mobile device
    + notified after compeltion of a long process; e.g. loading a large image or source track from the network
  + examples:
    + react to a mouse click w/ `<button onclick="...">Click me</button>`
    + react to keyboard typing: `<input type="text" oninput="showWhatWeTyped();" id="inputField" />`, `theDiv.innerHTML = field.value;`
    + HTML Canvas
      + useful for drawing and animating at 60 frames/second
      + create canvas: `<canvas id="myCanvas" width="578" height="200"></canvas>`
      + liesten mouse position winthin canvas:

        ```js
        window.onload = function init() {
            canvas = document.getElementById('myCanvas');
            ctx = canvas.getContext('2d');

            canvas.addEventListener('mousemove', function (evt) {
                mousePos = getMousePos(canvas, evt);
                var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;
                writeMessage(canvas, message);
            }, false);

            ...
        }
        ```

    + right/left key movement: `window.addEventListener('keydown', handleKeydown, false);  window.addEventListener('keyup', handleKeyup, false);`





