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
  + changing the CSS property names to CamelCase as JaVaScript variable names
  + position values (height & width): string values w/ "px" and "%"
  + changing common properties (color, border, background color), e.g.,
    + select element: `divElem = document.querySelector("#theDiv");`
    + modify CSS: `divElem.style.border = "5px dashed purple"; divElem.style.padding = "10px"; divElem.style.backgroundColor = "lightGreen";`
  + changing the background image property w/ external image, e.g.,
    + select element: `divElem = document.querySelector("#theDiv");`
    + modify background: `divElem.innerHTML = ""; divElem.style.width = "100%"; divElem.style.height = "300px"; divElem.style.backgroundImage = "url(https://mainline.i3s.unice.fr/mooc/marioSprite.png)";`
  + using the background image as sprite sheet
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
      + listen to mouse position winthin canvas:

        ```js
        window.onload = function init() {
            canvas = document.getElementById('myCanvas');
            ctx = canvas.getContext('2d');

            canvas.addEventListener('mousemover', function (evt) {
                mousePos = getMousePos(canvas, evt);
                var message = 'Mouse position: ' + mousePos.x + ',' + mousePos.y;
                writeMessage(canvas, message);
            }, false);

            ...
        }
        ```

    + right/left arrow key movement: `window.addEventListener('keydown', handleKeydown, false);  window.addEventListener('keyup', handleKeyup, false);`


### 1.6.6 Using built-in HTML5 APIs

Your browser comes with a lot of standard W3C APIs. By standard, we mean "parts of HTML5" or real Web standards that will still work in 10 years. In contrast to "industry standards", W3C standards are meant to be supported by browsers for years to come. These standards are a joint effort by the industry, the community, and W3C to develop stable, reliable standards.

The following example uses some of these APIs, simply to "show the possibilities". Others will be discussed later on in the course, or in other W3Cx courses.


#### Examples

__Example #1: using the WebCam__

CLICK ON THE TOP RIGHT OF THE BELOW WINDOW (on the "Codepen" logo) to see this example running. 

Due to security restrictions, the webcam image cannot be seen in this embedded example anymore.

Look at the JavaScript tab! The [W3Cx HTML5 Coding Essentials and Best Practices](https://www.edx.org/course/html5-part-1-html5-coding-essentials-w3cx-html5-1x-2) course will provide many other examples that use the WebCam.

[CodePen Demo](https://codepen.io/w3devcampus/pen/ZLNwqx)

[Local Demo](src/01f-example13.html)

If you want to spend some time having fun with the WebCam, don't forget to try the WebCam Toy demo!


__Example #2: using the WebAudio API to build a small synthetizer__

Click on the piano keyboard. Use the different buttons, sliders, etc. This example uses the WebAudio API in order to synthesize sounds.

[CodePen Demo](https://codepen.io/w3devcampus/pen/oBRVgv)

[Local Demo](src/01f-example14.html)


#### Notes for 1.6.6 Using built-in HTML5 APIs

+ Built-in HTML5 APIs
  + standard
    + standard W3C APIs, part of HTML5
    + supported by browsers
    + joint effort by the industry, the community, and W3C
  + examples
    + access and display WebCam

      ```js
      navigator.mediaDevices.getUserMedia({
        audio: false,
        video: true
      }).then(function(stream) {
        var video = document.createElement('video');
        document.body.appendChild(video);
        video.srcObject = stream;
        video.play();
      }).catch(err => {
        console.log(err)
      })
      ```

    + WebAudio APIs: `oscillator.createOscillator(); oscillator.setFreq(freq);`


### 1.6.7 Using third-party JS APIs/libraries

Thousands of JavaScript libraries exist. Their purposes range from making it easier to plot a math function, playing [chiptune](https://fr.wikipedia.org/wiki/Chiptune) music, animating objects, through to visualizing data and much more.


#### Examples

We provide some examples below, but feel free to look on the Web for other external libraries.

__Example #1: plot mathematical functions using the [function plot JavaScript library](https://mauriciopoppe.github.io/function-plot/)__

There are numerous libraries for plotting math functions, but this one is pretty easy to use and very powerful. Here is an example that plots `f(x) = x^2`, then `f(x) = sin(x)` and finally a mix of fours functions: `f(x) = x^2` (in red), `f(x) = 3*x` (in green), `f(x) = cos(x)` (in blue) and `f(x) = -3*x^2 + x^2` (dashed)

[CodePen Demo](https://codepen.io/w3devcampus/pen/jyjEob)

[Local Demo](src/01f-example15.html)

Here is another much simpler example, please edit the code (click on "edit on codepen") and change the function for something like `f(x) = x^3` and look at the result (don't forget to change the xRange and yRange values). If you have trouble, [look here](https://codepen.io/w3devcampus/pen/MJMYNb) for a solution.

[CodePen Demo](https://codepen.io/w3devcampus/pen/NdVJvy)

[Local Demo](src/01f-example16.html)


__Example #2: plot a force directed graph using the d3.js JavaScript library__

Try to click and drag nodes... All the graphics, animation and force repulsion, is done using the very powerful [d3.js plotting library](https://d3js.org/). Look at the HTML source code to see how we included this library in our HTML page. Look at the JS part; it seems complicated, but hey! I guess you can make your own graph with your own colors and your own node labels, without mastering JavaScript ;-) The beauty of this language is that you can find so many examples on the Web that you can easily learn by copying and pasting, tweaking code you haven't even written, etc. Go to codepen.io and use the search button for "d3" and you will find plenty of examples that use that library.

[CodePen Demo](https://codepen.io/w3devcampus/pen/Bpgypq)

[Local Demo](src/01f-example17.html)


__Example #3: play chiptune songs using the chiptune.js library__

I really like this example, as it takes me back to my youth playing games on the Commodore 64, the Nintendo NES console, etc. In that prehistoric age, there weren't a lot of kilobytes available in the memory, and most sounds were synthesized, not audio samples. The audio resolution was low as CPUs were rather weaker than today. Musicians used tools called "mod players/editors" for creating the music score (you can [try a re-creation on the browser of a mod editor](https://mod.haxor.fi/Necros/point_of_departure.s3m) to see how it looked in the late 80's).

To try the example below, click on "load demo song", then on the play button. If you want to try other compatible songs, look for any .mod, .it, .xm song on the Web and drag and drop it into the example page. A good resource for such files is [The Mod Archive](https://modarchive.org/), you can download plenty of chiptune files from there.

[CodePen Demo](https://codepen.io/w3devcampus/pen/GrbgMB)

[Local Demo](src/01f-example18.html)


__Example #4: animate a sprite in an HTML5 canvas using the sprite.js library__

This is just a small example of the use of the [sprite.js library](https://github.com/IceCreamYou/Canvas-Sprite-Animations), which makes it easier to animate sprites (sub images from a big image called a "sprite sheet") in an HTML5 canvas. We will see how to use the HTML5 canvas later on in this course. The example is just here to illustrate what can be done using external libraries.

[CodePen Demo](https://codepen.io/w3devcampus/pen/dNBPQm)

[Local Demo](src/01f-example19.html)


#### Notes for 1.6.7 Using third-party JS APIs/libraries

+ 3rd-party JS APIs/Libraries
  + thousands of JavaScript linbraries existed w/ various purpose
  + examples
    + [function plot JavaScript library](https://mauriciopoppe.github.io/function-plot/): plotting mathematical functions
    + [d3.js JavaScript library](https://d3js.org/): plot a force directed graph
    + [chiptune.js library](https://rawgithub.com/deskjet/chiptune.js/): play chiptune songs, [mod archive](https://modarchive.org/) for demos
    + [sprite.js library](https://github.com/IceCreamYou/Canvas-Sprite-Animations): animate a sprite in an HTML5 canvas



### 1.6.8 Working with remote data

Let's see a few examples on how to work with remote data.

#### Examples

__Example #1: use remote structured data__

This example downloads and displays a list of users in a table (see remote data):

[CodePen Demo](https://codepen.io/w3devcampus/pen/xgoZdg)

[Local Demo](src/01f-example20.html)


__Example #2: load and decode remote sounds for use in a video game__

This example just shows how to use the HowlerJS external library to load remote sounds, decode them and play them as samples in memory (useful for video games):

[CodePen Demo](https://codepen.io/w3devcampus/pen/BWbNQG)

[Local Demo](src/01f-example21.html)


#### Notes for 1.6.8 Working with remote data

+ Accessing remote data
  + fetch library: `<script src="https://cdnjs.cloudflare.com/ajax/libs/fetch/0.10.1/fetch.js"></script>`
  + access remote data

    ```js
    function search() {
      var queryURL = "https://jsonplaceholder.typicode.com/users";

      fetch(queryURL)
        .then(function (response) {
            // response.json() returns a json string,
            // returning it will convert it 
            // to a pure JavaScript 
            // object for the next then's callback
            return response.json();
        })
        .then(function (users) {
            // users is a JavaScript object here
            displayUsersAsATable(users);
        })
        .catch(function (error) {
            console.log('Error during fetch: ' + error.message);
        });
    }
    ```


### 1.6.9 Discussion and project

Here is the discussion forum for this part of the course. Please either post your comments/observations/questions or share your creations.


#### Suggested topic

+ Please share any fun/interesting JS examples that could interest your fellow students.

#### Optional project

+ You can tweak and share some of the examples provided in this section. No need to understand the whole code...


