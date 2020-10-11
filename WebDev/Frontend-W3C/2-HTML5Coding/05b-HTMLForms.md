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

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
    <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms">Elements of Forms</a></caption>
    <thead>
    <tr style="font-size: 1.2em;">
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:5%;">Element</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:40%;">Description</th>
    </tr>
    </thead>
  <tbody>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button" title="The HTML <button> element represents a clickable button, used to submit forms or anywhere in a document for accessible, standard button functionality."><code>&lt;button&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;button&gt;</code> element</strong> represents a clickable button, used to submit <a href="https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms">forms</a> or anywhere in a document for accessible, standard button functionality.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist" title="The HTML <datalist> element contains a set of <option> elements that represent the permissible or recommended options available to choose from within other controls."><code>&lt;datalist&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;datalist&gt;</code> element</strong> contains a set of <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option" title="The HTML <option> element is used to define an item contained in a <select>, an <optgroup>, or a <datalist>&nbsp;element. As such,&nbsp;<option>&nbsp;can represent menu items in popups and other lists of items in an HTML document."><code>&lt;option&gt;</code></a> elements that represent the permissible or recommended options available to choose from within other controls.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset" title="The HTML <fieldset> element is used to group several controls as well as labels (<label>) within a web form."><code>&lt;fieldset&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;fieldset&gt;</code> element</strong> is used to group several controls as well as labels (<a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label" title="The HTML <label> element represents a caption for an item in a user interface."><code>&lt;label&gt;</code></a>) within a web form.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form" title="The HTML <form> element represents a document section containing interactive controls for submitting information."><code>&lt;form&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;form&gt;</code> element</strong> represents a document section containing interactive controls for submitting information.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input" title="The HTML <input> element is used to create interactive controls for web-based forms in order to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. "><code>&lt;input&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;input&gt;</code> element</strong> is used to create interactive controls for web-based forms in order to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and <a href="https://developer.mozilla.org/en-US/docs/Glossary/user_agent">user agent</a>. </td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label" title="The HTML <label> element represents a caption for an item in a user interface."><code>&lt;label&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;label&gt;</code> element</strong> represents a caption for an item in a user interface.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend" title="The HTML <legend> element represents a caption for the content of its parent <fieldset>."><code>&lt;legend&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;legend&gt;</code> element</strong> represents a caption for the content of its parent <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset" title="The HTML <fieldset> element is used to group several controls as well as labels (<label>) within a web form."><code>&lt;fieldset&gt;</code></a>.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter" title="The HTML <meter> element represents either a scalar value within a known range or a fractional value."><code>&lt;meter&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;meter&gt;</code> element</strong> represents either a scalar value within a known range or a fractional value.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup" title="The HTML <optgroup> element creates a grouping of options within a <select> element."><code>&lt;optgroup&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;optgroup&gt;</code> element</strong> creates a grouping of options within a <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a> element.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option" title="The HTML <option> element is used to define an item contained in a <select>, an <optgroup>, or a <datalist>&nbsp;element. As such,&nbsp;<option>&nbsp;can represent menu items in popups and other lists of items in an HTML document."><code>&lt;option&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;option&gt;</code> element</strong> is used to define an item contained in a <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a>, an <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup" title="The HTML <optgroup> element creates a grouping of options within a <select> element."><code>&lt;optgroup&gt;</code></a>, or a <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist" title="The HTML <datalist> element contains a set of <option> elements that represent the permissible or recommended options available to choose from within other controls."><code>&lt;datalist&gt;</code></a>&nbsp;element. As such,&nbsp;<code>&lt;option&gt;</code>&nbsp;can represent menu items in popups and other lists of items in an HTML document.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output" title="The HTML Output element (<output>) is a container element into which a site or app can inject the results of a calculation or the outcome of a user action."><code>&lt;output&gt;</code></a></td>
    <td>The <strong>HTML Output element</strong> (<strong><code>&lt;output&gt;</code></strong>) is a container element into which a site or app can inject the results of a calculation or the outcome of a user action.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress" title="The HTML <progress> element displays an indicator showing the completion progress of a task, typically displayed as a progress bar."><code>&lt;progress&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;progress&gt;</code> element</strong> displays an indicator showing the completion progress of a task, typically displayed as a progress bar.</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select" title="The HTML <select> element represents a control that provides a menu of options"><code>&lt;select&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;select&gt;</code> element</strong> represents a control that provides a menu of options</td>
    </tr>
    <tr>
    <td style="vertical-align: top;"><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea" title="The HTML <textarea> element represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form."><code>&lt;textarea&gt;</code></a></td>
    <td>The <strong>HTML <code>&lt;textarea&gt;</code> element</strong> represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example a comment on a review or feedback form.</td>
    </tr>
  </tbody>
  </table>

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

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y5e6djuh')"
    src    ="https://tinyurl.com/yyoq59w7"
    alt    ="Small animation with GUI controls"
    title  ="Small animation with GUI controls"
  />
</figure>


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
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y38btue9"
      alt  ="chart with GUI"
      title="chart with GUI"
    >
    <img style="margin: 0.1em;" height=300
      src  ="https://tinyurl.com/y44rgu3k"
      alt  ="multiple charts with a GUI"
      title="multiple charts with a GUI"
    >
  </a>
</div>





