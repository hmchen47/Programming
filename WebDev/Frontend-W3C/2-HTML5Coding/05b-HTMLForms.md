# Week 5: HTML5 Forms


## 5.2 Elements and attributes


### 5.2.0 Lecture Notes

+ [HTML5 Forms](#521-introduction)
  + a set of input fields including a validation API and visual feedback, contextualized keyboards, etc.
    + 13 HTML5 new `<input type=.../>` fields: email, tel, color, url, date, datetime, datetime-local, month, week, time, range, number and search
  + built-in validation system
    + JavaScript API for custom validation
    + CSS pseudo classes useful for changing an input field style depending on the validity of the input
  + other goodies
    + the option to set an input field out of a `<form>`
    + new elements such as `<datalist>` for autocompletion
    + `<output>` for feedback
    + etc.
 
+ [Reference of Form elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms)<br/><br/>

+ [Manipulating HTML elements w/ JavaScript](#523-input-elements-and-attributes)
  + HTML initializing the process: `<body onload="init();">`
  + example: shape and movement control
    + called after the DOM ready (page loaded): `function init() {...}`
      + init the different variables:
        + get canvas & context: `canvas = document.querySelector("#mycanvas"); ctx = canvas.getContext('2d');`
        + specify canvas weight & height: `width = canvas.width; height = canvas.height;`
      + default values: `x=10; y = 10; ctx.canvas.fillStyle = 'red';`
      + start animation: `animationLoop();`
    + specify canvas in HTML: `<canvas id="mycanvas" width="200" height="50" style="border: 2px solid black"></canvas>`
    + process animation: 1) clear canvas; 2) draw shapes; 3) move shapes; 4) recall the loop w/ requestAnimationFrame
      + clear canvas: `ctx.clearRec(0, 0, width, height);`
      + draw shapes: `ctx.fillRect(x, y, size, size); ctx.strokeRect(x, y, size, size);`
      + move rectangle: `x += incX;`
      + check collision on left or right

        ```js
        if (((x+size) > width || (x <= 0)) {
            // cancel move + inverse speed
            x -= incX; incX = -incX;
        }
        ```

      + animate again at 60 frames/sec: `requestAnimationFrame(animationLoop);`
  + example: data visualization control
    + HTML code
      + initialize shapes after page load: `<body onload="init()">`
      + specify canvas: `<canvas id="canvas" width="400" height="400" style="border:solid 2px black"></canvas>`
    + data to be visualized: `var values = [1, 10, 2, 7, 9, 2, 34, 100, 12, 14, 19];`
    + init function after the page loaded: `function init() {...}`
      + get canvas & context: `canvas = document.getElementById('canvas'); ctx = canvas.getContext('2d');`
      + create sliders and set max values:

        ```js
        var list =  document.getElementById('sliders');
        var max = getMax(values);
        // create list of sliders
        for (i=0; i < values.length; i++) {
          var input = document.createElement('input');
          var li = document.createElement('li');
          var label = document.createElement('label');
          label.setAttribute('for', 'id'+i);
          label.textContent = 'value' + i + ' ';

          li.appendChild(label);

          input.setAttribute('type', 'range');
          input.setAttribute('id', 'id' + i);
          // Set their value and max attributes correctly
          input.setAttribute('max', max);
          input.value = values[i];
          // Add an onchange event listener and pass the
          // index of the slider to the callback
          input.setAttribute('oninput', 'changeValue(' + i + ')');
          li.appendChild(input);

          list.appendChild(li);
        }
        ```

    + plot histogram: `makeHistogram(x, y, width, height, values);`
    + plot pie chart w/ center (x, y) and radius: `makePieChart(300, 100, 90, values);`
    + plot line chart: `makeBrokenLines(40, 370, width, height, values);`
    + callback for sliders' `onchange` events: `function changeValue(index) {...}`
      + associate variable to a specified slider element: `var value = document.getElementById("id"+index).value;`
      + put the slider value in the values array: `values[parseInt(index)] = parseInt(value);`
      + clear the canvas: `ctx.clearRect(0, 0, canvas.width, canvas.height);`
      + redraw the chart: `makeHistogram(x, y, width, height, values);  makePieChart(300, 100, 90, values); makeBrokenLines(40, 370, width, height, values);`
    + get the max from the elements of the values array: `function getMax(values) {...}`
    + draw axes for bar chart and line chart: `function drawAxis(width, height,  values, maxValue) {...}`

+ [HTML5 forms](#524-best-practices)
  + form: a way to get user input sent to a remote server
  + several ways to collect server-side data from a form in a Web page: REST Web services, servlets, Microsoft ASP pages, etc.
  + form of the client side: 
    + indicating to which server and how the data should be sent, using the action and method attributes respectively
    + use JavaScript for sending the form content with Ajax
    + example: `<form action="myServerCode.php" method="POST">...</form>`
      + set the URL of the server side code `(myServerCode.php)`
      + the HTTP method used by the browser for sending the form content (POST)
  + example:

    ```html
    <form id="myForm">
      <fieldset>
        <legend>Personal information</legend>
        <label for="firstName">First name:</label>
        <input type="text" id="firstName" required name="firstName"> <br>
        <label for="lastName">Last name:</label>
        <input type="text" id="lastName" required name="lastName"> <br>
        <label for="email">Email:</label>
        <input type="email" id="email" required name="email"> <br>
        <label for="age">Age:</label>
        <input type="number" min=0 max=120  step=5 id="age" required name="age"> <br>
        <label for="date">Birth date:</label>
        <input type="date"  id="date" required name="date">
      </fieldset>
      <button>Submit form</button>
    </form>
    ```

### 5.2.1 Introduction

With HTML5, forms, which had shown little improvement since 1997, evolved considerably.  To achieve this, Web developers relied on many popular JavaScript frameworks for validating input formats, providing various input GUIs, such as calendars for dates, sliders, etc. Frameworks such as jQueryUI, Dojo, and Sencha, all provide a widget set for improving forms. Furthermore, it was time to take into account the specifics of mobile web applications, where the GUI of a date chooser cannot be the same as a 400x400 pixel wide calendar on a desktop. Contextual virtual keyboards provided the way forward on smartphones and tablets thanks to Apple, Google and others.

__HTML5 took all this into account and thus provides:__

+ A set of input fields that include a validation API and visual feedback, contextualized keyboards, etc. Of course the look and feel depends on the web browser's implementations, but the HTML5 forms specification introduced 13 new `<input type=.../>` fields:  `email`, `tel`, `color`, `url`, `date`, `datetime`, `datetime-local`, `month`, `week`, `time`, `range`, `number` and `search`.
+ Built-in validation system: JavaScript API for custom validation, CSS pseudo classes that are useful for changing an input field style depending on the validity of the input.
+ Other goodies, such as the option to set an input field out of a `<form>`, new elements such as `<datalist>` for autocompletion, `<output>` for feedback, etc.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://developer.mozilla.org/https://tinyurl.com/y4u8ud5e" ismap target="_blank">
    <img style="margin: 0.1em;" height=200 
      src  ="https://tinyurl.com/y5a9kwn5" 
      alt  ="contextual keyboards" 
      title="contextual keyboards"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yypemwax" 
    alt    ="date picker on a smartphone"
    title  ="date picker on a smartphone"
    >
  </a>
</div>


Examples of contextual keyboards are shown above; they differ depending on the type of  `<input>` fields in the `<form>`.

In the examples, we can see: email, URL, and phone number. Look at the different keyboard layouts. The last picture is a date picker from an IOS phone.


#### External resources:

+ From the specification: [Forms](https://html.spec.whatwg.org/multipage/forms.html)
+ From MDN's Web Docs: [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)


#### Knowledge check 5.2.1

1. Which of the following statements is true about HTML5 forms? (2 correct answers)

  a. On mobile devices, contextual keyboard will appear when a user interacts with the new input types<br/>
  b. HTML5 introduced 25 new input types which replace all the old ones from HTML4<br/>
  c. There is a built-in validation system for input elements<br/>
  d. Some HTML5 input types work only on mobile devices<br/>

  Ans: ac<br/>
  Explanation: The new input types (email, url, tel etc.) will indeed pop up a contextual keyboard on mobile devices. HTML5 introduced new input types but they do not replace the old ones, they complete them. There is a built-in validation system. And no, no specific input types work only on mobile devices. Correct answers are 1 and 3.


### 5.2.2 Example

There is a lot of course content covered this week, and before we get into all the details of the elements and attributes introduced by HTML5, we suggest playing with running examples of full featured forms.

This example was created by a learner (by Mels Le N.) from a previous version of this course.
It uses the geolocation API presented in Week 6 for auto-filling the address input fields.

Feel free to look at the source code in the [online example](https://jsbin.com/sivula/edit): ([Local Example - Input Forms](src/5.2.2-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yxzho2te')"
    src    ="https://tinyurl.com/y69x4nty"
    alt    ="Example of input forms"
    title  ="Example of input forms"
  />
</figure>


### 5.2.3 Input elements and attributes

#### Live coding video 1: using input elements as widgets to control a Web application

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V001800_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y3onhnvf)


#### Live coding video 2: creating GUI elements dynamically

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V002000_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/yycy4xmw)


Input elements, in particular the elements introduced by HTML5, can be used as widgets to control the behavior of a Web application. In this situation, they do not need to be inside a `<form>` element. We just bind event listeners to them and we use them as client-side widgets.



#### Examples

GUI: Graphical User Interface

__Example #1: choose the color, line width and speed of an animation__

+ [Bouncing rectangle without GUI](https://jsbin.com/ciwefo/1/edit?html,css,output) ([Local Example - Fix Rectangle](src/5.2.3-example1.html))
+ [Bouncing rectangle with GUI](https://jsbin.com/newojij/1/edit?html,css,output) (see screenshot at the top right of this page) ([Local Example - Variate Rectangle](src/5.2.3-example2.html))

__Example #2: data visualization control__

+ [Simple chart without a GUI](https://jsbin.com/UxuCOPa/3/edit?html,js,output) ([Local Example - Fix Chart](src/5.2.3-example3.html))
+ [Simple chart with a GUI](https://jsbin.com/gesive/edit?html,js,console,output) (see screenshot on the right) ([Local Example - Variate Chart](src/5.2.3-example4.html))
+ [Final version with different types of charts and a GUI](https://jsbin.com/ralonem/1/edit?html,js,output) (see screenshot below) ([Local Example - Multiple Charts](src/5.2.3-example5.html))


<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5e6djuh" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
    src    ="https://tinyurl.com/yyoq59w7"
    alt    ="Small animation with GUI controls"
    title  ="Small animation with GUI controls"
    >
    <img style="margin: 0.1em;" height=350
      src  ="https://tinyurl.com/y44rgu3k"
      alt  ="multiple charts with a GUI"
      title="multiple charts with a GUI"
    >
  </a>
</div>


### 5.2.4 Best practices


#### Live coding video 3: HTML5 forms - best practices

<a href="https://edx-video.net/W3CHTML5/W3CHTML5T315-V001900_DTH.mp4" target="_BLANK">
  <img style="margin-left: 2em;" src="https://bit.ly/2JtB40Q" alt="lecture video" width=150/>
</a><br/><br/>

[Transcript](https://tinyurl.com/y598luwv)


The example used in the video is available [online at JSBin](https://jsbin.com/jagodi/edit?html,css,output). A screenshot of the resulted form is shown on the right. ([Local Example - Best Practice](src/5.2.4-example1.html))

Forms are a way to get user input which is sent to a remote server. This section of the course focuses on the HTML5 additions to forms, and as such will only cover the client-side part.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3faoc35')"
    src    ="https://tinyurl.com/yxn3h94g"
    alt    ="screenshot of the HTML5 forms example from the video"
    title  ="screenshot of the HTML5 forms example from the video"
  />
</figure>


On the server side, you may have PHP, Java, C#, Ruby, Python, etc. components. There are several ways to collect server-side data from a form in a Web page: REST Web services, servlets, Microsoft ASP pages, etc.

On the client side, the forms indicate to which server and how the data should be sent,  using the action and method attributes respectively. A `<button type="submit">` or an `<input type=submit>` field is used to submit the form content.

For example: `<form action="myServerCode.php" method="POST">...</form>`. Here, we set the URL of the server side code (myServerCode.php), and the HTTP method that will be used by the browser for sending the form content (POST).

Another approach is to use JavaScript for sending the form content with [Ajax](https://en.wikipedia.org/wiki/Ajax_(programming)). This is covered in W3Cx HTML5 Apps and Games course.

This week, let's study the elements and attributes offered by HTML5, as well the HTML5 form validation API. 

The example shown in the video shows some best practices for writing accessible forms and does some basic layout using CSS.

The following additional example shows the same best practices but presents a more complete form with CSS rules to make a nice layout. See it [online](https://jsbin.com/zubitex/1/edit?html,output), and illustrated with the screenshot below. It is adapted from [this very good MDN's article "How to structure a web form"](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/How_to_structure_an_HTML_form). ([Local Example - Payment Form](src/5.2.4-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3faoc35')"
    src    ="https://tinyurl.com/y2atwyjb"
    alt    ="Form layout example"
    title  ="Form layout example"
  />
</figure>


### 5.2.5 Discussion

Here is the discussion forum for this part of the course. You can post your comments and of course ask questions.

Let us suggest some topics of discussion:


#### Suggested topics

+ Did you run the given examples on different browsers? You might have encountered problems with Safari or Internet Explorer.
+ Did you know that HTML5 input elements and other new features related to forms could be used for building a GUI client-side, with no need to send data to a remote server?





