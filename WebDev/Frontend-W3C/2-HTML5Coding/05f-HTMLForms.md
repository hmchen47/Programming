# Week 5: HTML5 Forms


## 5.6 Elements related to forms


### 5.6.0 Lecture Notes

+ [&lt;output&gt; tag](#562-output)
  + syntax: `<output name="x" for="a b"></output>`
  + represent the result of a computation or user action
  + `oninput` event handler of `<form>` element directly uses the `<output>` element using the value of its `name` attribute
  + element & attributes
    + `for`: a space-separated list containing the elements' ids whose values went into the calculation.
    + `name`: the name of the element.
    + `form`: associate the `<output>` element w/ its form owner
      + the value must be the `id` of a form in the same document
      + place an `<output>` element outside of the `<form>` w/ which it is associated
  + example: perform multiplication
 
    ```html
    <form oninput="o.value=a.value*b.value">
        <input type="number" name="a" id="a" value="2"> x
        <input type="number" name="b" id="b" value="3"> =
        <output for="a b" name="o">6</output>
    </form>
    ```

  + example: perform addition w/ slide bar

    ```html
    <form >
      <input name="a" value="50" type="range"
          oninput="x.value = a.valueAsNumber + b.valueAsNumber; y.value = this.value;"/>
      <output id="y">50</output> +
      <input name="b" value="50" type="number" /> =
      <output name="x" id="x" for="a b"></output>
    </form>
    ```

    + new input field properties: `valueAsNumber` and `valueAsDate`
    + input field values considered as strings by JavaScript
    + using `x.value = a.value + b.value` would result in a string concatenation instead of an addition
    + using the `valueAsNumber` property to convert as the number

+ [&lt;meter&gt; tag](#563-meter)
  + display colored bars to represent numeric values
    + to display a colored gauge to show disk usage
    + to highlight the relevance of a query result
    + the fraction of a voting population that favours a particular candidate, etc.
  + used w/ the `<input type="range">` field as an instant feedback indicator
  + not used to indicate progress, using a `<progress>` element instead
  + typical usage: `<meter value=75 min=0 low=20 high=80 max=100 optimum=50></meter>`
    + using the easy-to-understand value, `min`, `max`, `low`, `high` and `optimum` attributes
    + `optimum` attribute along w/ `min`, `low`, `high` and `max` attributes
    + the constraint `min < low < high < max` respected
    + affecting the color of the bar
  + the `<meter>` ranges
    + Range 1: between `min` and `low`
    + Range 2: between `low` and `high`
    + Range 3: between `high` and `max`

      <figure style="margin: 0.5em; text-align: center;">
        <img style="margin:  0.1em; padding-top: 0.5em; width: 30vw;"
          onclick="window.open('https://tinyurl.com/y5wqfrhe')"
          src    ="https://tinyurl.com/yxrdyljn"
          alt    ="an image visualizing the regions"
          title  ="an image visualizing the regions"
        />
      </figure>

  + example:

    ```html
    <p>Grades: <meter id="meter2" value="75" min="0" low="20" high="80" max="100"></meter>
    <input min="0" max="100" value="75" id="meter2range"
          oninput="effect('meter2', 'meter2range')" type="range">
    <output id="meter2val" for="meter2range"></output></p>
    <script>
    function effect(meter, meterrange) {
         var currVal = document.getElementById(meterrange).value;
         document.getElementById(meter).value = currVal;
         document.getElementById(meter+ "val").innerHTML = currVal;
    }
    </script>
    ```

    + the link btw the slider (an `<input type=range>`) and the `meter` element: using an input event handler (`oninput="effect(...)"`)
    + change the current value of the `<meter>` element (`document.getElementById(meter).value = currVal;`) and update the displayed html content of the `<output>` element (`document.getElementById(meter+"val").innerHTML = currVal;`)

+ [optimum attribute](#563-meter)
  + color of the gauge changes depending on the attribute's values
  + indicating the optimal numeric value
  + an indication where along the range is considered preferable
  + depending on the value set to optimum attribute, one of the ranges above becomes the "good (optimum)" range

+ [&lt;progress&gt; tag](#564-progress)
  + used for progress bars (i.e., the percentage of a file being uploaded, etc.)
  + similar to `<meter>`
  + typical usage: `<progress id=pr value=50 min=0 max=100>`
  + calculate the percentage corresponding to the `value`, `min` and `max` attributes
  + adjust the length of the progress bar accordingly
  + no value attribute: the progress bar displaying an "indeterminate look"
  + example

    ```html
    Download pro gress: <progress id=pr value=100 min=0 max=1000></progress>
    <script>
      var i=0;
      setInterval(function () {
          i = (i+1) %1000;
          document.getElementById('pr').value = i;
      },1);
    </script>
    ```

+ [`<datalist>` tag](#565-datalist)
  + useful for linking a list of choices to an input element
  + input fields for restricting the value set proposed
    + restricted set of colors or possible dates
    + displaying slider ticks
  + used in a more general way, for providing client-side auto-completion w/o the need to use JavaScript
  + the `id` of the `<datalist>` must match the value of the list attribute in the input field
  + able to be shared by several input fields
  + `list` attribute matching the `id` of the `datalist` element
  + `input` field related to the `datalist` proposing auto-completion based on `<datalist>` values



### 5.6.1 HTML5 forms elements

Let's look at the HTML5 elements related to forms (specifically: `<datalist>`, `<output>`, `<meter>`  and `<progress>` elements).


<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 40vw;" cellspacing="0" cellpadding="5" border="1">
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">HTML4</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">HTML5</th>
  </tr>
  </thead>
  <tbody style="font-family: 'courier new', courier;">
    <tr>
    <td>
    <ul>
    <li><strong>&lt;form&gt;</strong></li>
    <li><strong>&lt;fieldset&gt;</strong></li>
    <li><strong>&lt;legend&gt;</strong></li>
    <li><strong>&lt;textarea&gt;</strong></li>
    <li><strong>&lt;label&gt;</strong></li>
    <li><strong>&lt;select&gt;</strong></li>
    <li><strong>&lt;option&gt;</strong></li>
    <li><strong>&lt;optgroup&gt;</strong></li>
    <li><strong>&lt;input&gt;</strong></li>
    <li><strong>&lt;button&gt;</strong></li>
    </ul>
    </td>
    <td>
    <ul>
    <li><strong>&lt;datalist&gt;</strong></li>
    <li><strong>&lt;output&gt;</strong></li>
    <li><strong>&lt;meter&gt;</strong></li>
    <li><strong>&lt;progress&gt;</strong></li>
    <li><strong><span style="color: #ff0000; font-family: 'courier new', courier;">&lt;keygen&gt; *</span></strong></li>
    </ul>
    </td>
    </tr>
    <tr>
    <td colspan="2">
    <p><span style="color: #ff0000;">* Not really useful for most developers.</span></p>
    </td>
    </tr>
  </tbody>
</table>


### 5.6.2 `<output>`

The output element represents the result of a computation or user action. You can see it as a "specialized `<div>` or `<span>`" for displaying interactive results.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y5ylssnu')"
    src    ="https://tinyurl.com/y3aose7z"
    alt    ="example of output element use"
    title  ="example of output element use"
  />
</figure>


#### Typical use / interactive examples

[Do not hesitate to play with the source code of these examples online at JSBin.](https://jsbin.com/yuvani/1/edit?html,output) ([Local Example - Output](src/5.6.2-example1.html))

__Example #1__

<div><ol>
<li value="1">&lt;form oninput="o.value=a.value*b.value"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="number" name="a"&nbsp;<span style="line-height: 25.6000003814697px;">id<span style="line-height: 25.6000003814697px;">=</span><span style="line-height: 25.6000003814697px;">"a"</span>&nbsp;</span>value="2"&gt; x</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="number" name="b"&nbsp;<span style="line-height: 25.6000003814697px;">id<span style="line-height: 25.6000003814697px;">=</span><span style="line-height: 25.6000003814697px;">"b"</span>&nbsp;</span>value="3"&gt; =</li>
<li>&nbsp; &nbsp; &nbsp;<strong>&lt;output for="a b" name="o"&gt;6&lt;/output&gt;</strong></li>
<li>&lt;/form&gt;</li>
</ol></div>

The `oninput` event handler directly uses the `<output>` element using the value of its name attribute.

Result (do change the input field values):

<div><form oninput="o.value=a.value*b.value"><input name="a" value="2" type="number"> x <input name="b" value="3" type="number"> = <output for="a b" name="o">6</output></form></div>


__Explanations about the attributes specific to the `<output>` element:__

+ `for`: a space-separated list containing the elements' ids whose values went into the calculation.
+ `name`: the name of the element.
+ `form`:  associates the `<output>` element with its form owner. The value must be the id of a form in the same document. This allows you to place an `<output>` element outside of the `<form>` with which it is associated.


__Example #2__

<div><form><input name="a" oninput="x.value = a.valueAsNumber + b.valueAsNumber; y.value = this.value;" value="50" type="range"><output id="y">50</output> +<input name="b" value="50" type="number"> =<output id="x" for="a b" name="x"></output></form></div>

Source code:

<div><ol>
<li value="1">&lt;form &gt;</li>
<li>&nbsp; &nbsp;&lt;input name="a" value="50" type="range" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;oninput="x.value = a.valueAsNumber + b.valueAsNumber; </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; y.value = this.value;"/&gt;</li>
<li>&nbsp; &nbsp;&lt;output id="y"&gt;50&lt;/output&gt; + </li>
<li>&nbsp; &nbsp;&lt;input name="b" value="50" type="number" /&gt; = </li>
<li>&nbsp; &nbsp;&lt;output name="x" id="x" for="a b"&gt;&lt;/output&gt;</li>
<li>&lt;/form&gt;</li>
</ol></div>

HTML5 has introduced new input field properties: `valueAsNumber` and `valueAsDate`.The last example is similar to the previous one except that we use an addition instead of a multiplication.

As input field values are considered as strings by JavaScript, using `x.value = a.value + b.value` would result in a string concatenation instead of an addition. That's why we use the `valueAsNumber` property.

This is why we used the `valueAsNumber` property also introduced by HTML5 for some input fields such as `<input type="range">` and `<input type="number">`, we also encountered the valueAsDate properties when we studied `<input type="date">`.


### 5.6.3 `<meter>`

The `<meter>` element displays colored bars to represent numeric values.

It can be useful to display a colored gauge to show disk usage, to highlight the relevance of a query result, or the fraction of a voting population that favors a particular candidate, etc. This element is often used with the `<input type="range">` field as an instant feedback indicator.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3ougvam')"
    src    ="https://tinyurl.com/y2y9pt24"
    alt    ="picture of a meter example"
    title  ="picture of a meter example"
  />
</figure>


The `<meter>` element should not be used to indicate progress. You should instead use a `<progress>` element.


#### Typical use

<div><ol>
<li value="1">Storage space used: <strong>&lt;meter</strong><strong> value=75 min=0&nbsp;low=20&nbsp;high=80&nbsp;max=100 optimum<strong style="color: #3c3c3c; line-height: 25.6px;"><span color="#3c3c3c" style="color: #3c3c3c;">=</span><span color="#008800" style="color: #008800;">50</span></span></strong>&gt;&lt;/meter&gt;</span></strong></li>
</ol></div>

The `<meter>` element uses the easy-to-understand value, `min`, `max`, `low`, `high` and `optimum` attributes. The `optimum` attribute, along with `min`, `low`, `high` and `max` attributes will affect the color of the bar, and of course the constraint `min < low < high < max` should be respected.

More explanations about the colors and the meaning of the `optimum` attribute will come further in this lesson.


#### Interactive example

[Try the next example online at JSBin](https://jsbin.com/jumahox/1/edit?html,output) or just play with it in your browser by dragging the slider below: ([Local Example - meter](src/5.6.3-example1.html))

<div>
<pre>&lt;meter value=75 min=0&nbsp;<span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif; line-height: 1.6;">low=20&nbsp;</span><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif; line-height: 1.6;">high=80 </span><span style="font-size: 1em; line-height: 1.6;">max=100 optimum=19&gt;&lt;/meter&gt;</span></pre>
<p>Grades: <meter id="meter2" value="75" optimum="19" high="80" low="20" max="100" min="0">75%</meter> <input id="meter2range" oninput="effect('meter2', 'meter2range')" min="0" max="100" value="75" high="80" low="20" type="range"> <output id="meter2val"></output></p>
<script>// <![CDATA[
function effect(meter, meterrange) {
	var currVal = document.getElementById(meterrange).value;
	document.getElementById(meter).value =  currVal;
	document.getElementById(meter+ "val").innerHTML = currVal;
 }
// ]]></script>
</div>


Source code of the example:

<div><ol>
<li value="1">&lt;p&gt;Grades: <strong>&lt;meter id="meter2" value="75" min="0"&nbsp;low="20"&nbsp;high="80"&nbsp;max="100"&gt;&lt;/meter&gt;</strong> </li>
<li> </li>
<li>&lt;input min="0" max="100"&nbsp;value="75" id="meter2range" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;oninput="effect('meter2', 'meter2range')" type="range"&gt; </li>
<li> &lt;output id="meter2val"&nbsp;<span style="color: #660066; line-height: 25.6000003814697px;">for</span>="meter2range"&gt;&lt;/output&gt;&lt;/p&gt;</li>
<li> &lt;script&gt;</li>
<li> function effect(meter, meterrange) {</li>
<li>&nbsp; &nbsp; &nbsp;var currVal = document.getElementById(meterrange).value;</li>
<li>&nbsp; &nbsp; &nbsp;document.getElementById(meter).value = currVal;</li>
<li>&nbsp; &nbsp; &nbsp;document.getElementById(meter+ "val").innerHTML = currVal;</li>
<li> }</li>
<li> &lt;/script&gt;</li>
</ol></div>


__Explanations:__

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3ougvam')"
    src    ="https://tinyurl.com/y2q72j6a"
    alt    ="illustration associates w/ HTML code"
    title  ="illustration associates w/ HTML code"
  />
</figure>

The link between the slider (an `<input type=range>`) and the meter element is done using an input event handler (oninput="effect(...)" line 4. The effect JavaScript function will change the current value of the `<meter>` element (line 9) and update the displayed html content of the `<output>` element (line 10)

The link between the slider (an `<input type=range>`) and the meter element is done using an input event handler (oninput="effect(...)") at line 4.

The effect JavaScript function will change the current value of the `<meter>` element (line 9) and update the displayed html content of the `<output>` element (_line 10_).


__The color of the gauge changes depending on the attribute's values__

The optimum attribute indicates the optimal numeric value and gives an indication where along the range is considered preferable. Just think of the `<meter>` ranges as follows:

+ Range 1: between `min` and `low`
+ Range 2: between `low` and `high`
+ Range 3: between `high` and `max`

... and depending on the value you set to optimum attribute, one of the ranges above becomes the "good (optimum)" range.

So in the previous example, with the value of the optimum attribute set to 19, a number between min and low (not inclusive), the Range 1 (between min=0 and low=20) becomes the "good (optimum)" range (displayed in green), the Range 3 (between high=80 and max=100) becomes the "bad" (displayed in red color) range, and the Range 2, in the middle, will be displayed in yellow (not optimum, not bad).

So, a `<meter>` element used for displaying blood pressure might be a good candidate for setting the optimum value to "Range 2", and a `<meter>` element used for displaying memory usage might be a good candidate for setting the optimum value to "Range 1", meaning that a low memory usage is "good".


#### External resources

+ From MDN's Web  Docs: [The HTML Meter element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
+ Good blog post: [How to use and style the meter element](https://www.hongkiat.com/blog/style-html5-meter/)


### 5.6.4 `<progress>`

The `<progress>` element is similar to `<meter>` but it is used for progress bars (i.e., the percentage of a file being uploaded, etc.):

<div><ol>
<li value="1">&lt;progress id=pr value=50 min=0 max=100&gt;</li>
</ol></div>


<p>Gives:&nbsp; <progress id="pr1" value="50" max="100" min="0"></progress></p>

The browser calculates the percentage corresponding to the `value`, `min` and `max` attributes and adjusts the length of the progress bar accordingly.

If no `value` attribute is set, the progress bar will display an "indeterminate look", that may slightly vary among different browser implementations.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yxbg23pf')"
    src    ="https://tinyurl.com/y6pqbvzj"
    alt    ="indeterminate progress bar screenshot"
    title  ="indeterminate progress bar screenshot"
  />
</figure>


#### Typical use

[Here is an online example at JSBin](https://jsbin.com/hebiju/edit?html,output), or try it below in your browser:  ([Local Example - progress](src/5.6.4-example1.html))

<div>This example uses some JavaScript to simulate a download progress by changing in real time the <span style="font-family: 'courier new', courier;">value attribute.
<p>The progress below is defined like this:</p>
<pre>&lt;progress id=pr value=100 max=1000&gt;</pre>
<p>Download progress: <progress id="pr" value="331" max="1000" min="0"></progress></p>
</div>

Source code:

<div><ol>
<li value="1">Download progress: <strong>&lt;progress id=pr value=100 min=0 max=1000&gt;&lt;/progress&gt;</strong> </li>
<li> &lt;script&gt;</li>
<li>&nbsp; &nbsp;var i=0;</li>
<li>&nbsp; &nbsp;setInterval(function () {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;i = (i+1) %1000;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;document.getElementById('pr').value = i;</li>
<li>&nbsp; &nbsp;},1);</li>
<li><span style="color: #008800; line-height: 25.6000003814697px;">&lt;/script&gt;</span></li>
</ol></div>


### 5.6.5 `<datalist>`

The `<datalist>` form element is useful for linking a list of choices to an input element.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y42x6msa" ismap target="_blank">
    <img style="margin: 0.1em;" height=100
      src  ="https://tinyurl.com/y23befde"
      alt  ="example of datalist for autocompletion"
      title="example of datalist for autocompletion"
    >
    <img style="margin: 0.1em;" height=50
      src  ="https://tinyurl.com/y6l5qqnt"
      alt  ="Another example of use of datalist"
      title="Another example of use of datalist"
    >
  </a>
</div>


We have already seen this element in action with different `<input>` elements, such as `<input type="color">`, `<input type="date">`, or `<input type="range">`.

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y42x6msa" ismap target="_blank">
    <img style="margin: 0.1em;" height=80
      src  ="https://tinyurl.com/y4wpv7ne"
      alt  ="restricted choice of colorrestrict"
      title="restricted choice of colorrestrict"
    >
    <img style="margin: 0.1em;" height=200
      src  ="https://tinyurl.com/y2yhjjc2"
      alt  ="choices using a datalist element"
      title="choices using a datalist element"
    ><br/>
    <img style="margin: 0.1em;" height=30
      src  ="https://tinyurl.com/y5yg7dak"
      alt  ="example of datalist for sliders ticks"
      title="example of datalist for sliders ticks"
    >
  </a>
</div>


It is often "linked" to input fields either for restricting the value set that can be proposed  (i.e., restricted set of colors or possible dates, or for displaying slider ticks, as shown above), __but it may also be used in a more general way, for providing client-side auto-completion without the need to use JavaScript.__

It works with the new list attribute of input fields introduced by HTML5. __The id of the `<datalist>` must match the value of the `list` attribute in the input field. A datalist can be shared by several input fields.__ It suffices that their list attribute matches the id of the datalist element.

The input field is related to the datalist that will propose auto-completion based on `<datalist>` values.


#### Typical use for auto-completion

Here is an [online example at JSBin](https://jsbin.com/tiqexel/1/edit?html,output), or try it here in your browser (type the name of your favorite browser): ([Local Example - Auto-completion](src/5.6.5-example1.html))

<div><form action="demo_form.asp" method="get">What is your favorite browser: <input name="browser" list="browsers" type="text">
<datalist id="browsers">
<option value="Internet Explorer"></option>
<option value="Firefox"></option>
<option value="Chrome"></option>
<option value="Opera"></option>
<option value="Safari"></option>
</datalist>
<input value="Submit Query" type="submit"></form></div>
 
Source code of this example:

<div><ol>
<li value="1">&lt;form action="demo_form.asp" method="get"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input <strong>list="browsers"</strong> name="browser" /&gt;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp;&lt;datalist <strong>id="browsers"</strong>&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Internet Explorer"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Firefox"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Chrome"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Opera"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Safari"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;/datalist&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="submit" /&gt;</li>
<li>&lt;/form&gt;</li>
</ol></div>

As you can see at lines 2 and 4, the id and list attributes match. The `<datalist>` element is wrapped around a set of `<option>` that are available for selection by another form control (in this example the input field from line 2).


### 5.6.6 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions


#### Optional projects

Why don't you add some of these elements to the projects suggested earlier (GUI for a Web app. or a form for registering in a forum)? The best way to learn how to use them is to try them in your own projects.



