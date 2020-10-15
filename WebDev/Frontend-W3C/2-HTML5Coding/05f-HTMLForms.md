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
      + The value must be the `id` of a form in the same document
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
  + not be used to indicate progress, using a `<progress>` element instead
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
        <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
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
    <ul class="column">
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
    <ul class="column">
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;form</span><span class="pln"> </span><span class="atn">oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">o</span><span class="pun">.</span><span class="pln">value</span><span class="pun">=</span><span class="pln">a</span><span class="pun">.</span><span class="pln">value</span><span class="pun">*</span><span class="pln">b</span><span class="pun">.</span><span class="pln">value</span><span class="atv">"</span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"number"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"a"</span><span class="pln">&nbsp;<span class="atn" style="line-height: 25.6000003814697px;">id</span><span class="pun" style="line-height: 25.6000003814697px;">=</span><span class="atv" style="line-height: 25.6000003814697px;">"a"</span>&nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"2"</span><span class="tag">&gt;</span><span class="pln"> x</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"number"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"b"</span><span class="pln">&nbsp;<span class="atn" style="line-height: 25.6000003814697px;">id</span><span class="pun" style="line-height: 25.6000003814697px;">=</span><span class="atv" style="line-height: 25.6000003814697px;">"b"</span>&nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"3"</span><span class="tag">&gt;</span><span class="pln"> =</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"a b"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"o"</span><span class="tag">&gt;</span><span class="pln">6</span><span class="tag">&lt;/output&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/form&gt;</span></li>
</ol></div>

The `oninput` event handler directly uses the `<output>` element using the value of its name attribute.

Result (do change the input field values):

<div class="exampleHTML"><form oninput="o.value=a.value*b.value"><input name="a" value="2" type="number"> x <input name="b" value="3" type="number"> = <output for="a b" name="o">6</output></form></div>


__Explanations about the attributes specific to the `<output>` element:__

+ `for`: a space-separated list containing the elements' ids whose values went into the calculation.
+ `name`: the name of the element.
+ `form`:  associates the `<output>` element with its form owner. The value must be the id of a form in the same document. This allows you to place an `<output>` element outside of the `<form>` with which it is associated.


__Example #2__

<div class="exampleHTML"><form><input name="a" oninput="x.value = a.valueAsNumber + b.valueAsNumber; y.value = this.value;" value="50" type="range"><output id="y">50</output> +<input name="b" value="50" type="number"> =<output id="x" for="a b" name="x"></output></form></div>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;form</span><span class="pln"> </span><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;input</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"a"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"50"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">x</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> a</span><span class="pun">.</span><span class="pln">valueAsNumber </span><span class="pun">+</span><span class="pln"> b</span><span class="pun">.</span><span class="pln">valueAsNumber</span><span class="pun">;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; y</span><span class="pun">.</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span><span class="atv">"</span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"y"</span><span class="tag">&gt;</span><span class="pln">50</span><span class="tag">&lt;/output&gt;</span><span class="pln"> + </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;input</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"b"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"50"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"number"</span><span class="pln"> </span><span class="tag">/&gt;</span><span class="pln"> = </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;output</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"x"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"x"</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"a b"</span><span class="tag">&gt;&lt;/output&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/form&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">Storage space used: <strong>&lt;meter</strong></span><strong><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">75</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">0</span><span class="pln">&nbsp;</span><span class="atn"><span class="atn">low</span><span class="pun">=</span><span class="atv">20&nbsp;</span><span class="atn">high</span><span class="pun">=80</span><span class="atv">&nbsp;</span>max</span><span class="pun">=</span><span class="atv">100</span><span class="pln"> </span><span class="pln">optimum</span><span class="tag"><strong style="color: #3c3c3c; line-height: 25.6px;"><span class="pun"><span color="#3c3c3c" style="color: #3c3c3c;">=</span><span color="#008800" style="color: #008800;">50</span></span></strong>&gt;&lt;/meter&gt;</span></strong></li>
</ol></div>

The `<meter>` element uses the easy-to-understand value, `min`, `max`, `low`, `high` and `optimum` attributes. The `optimum` attribute, along with `min`, `low`, `high` and `max` attributes will affect the color of the bar, and of course the constraint `min < low < high < max` should be respected.

More explanations about the colors and the meaning of the `optimum` attribute will come further in this lesson.


#### Interactive example

[Try the next example online at JSBin](https://jsbin.com/jumahox/1/edit?html,output) or just play with it in your browser by dragging the slider below: ([Local Example - meter](src/5.6.3-example1.html))

<div class="exampleHTML">
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;p&gt;</span><span class="pln">Grades: </span><strong><span class="tag">&lt;meter</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"meter2"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"75"</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln">&nbsp;</span><span class="atn"><span class="atn">low</span><span class="pun">=</span><span class="atv">"20"&nbsp;</span><span class="atn">high</span><span class="pun">=</span><span class="atv">"80"&nbsp;</span>max</span><span class="pun">=</span><span class="atv">"100"</span><span class="tag">&gt;</span><span class="tag">&lt;/meter&gt;</span></strong><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"100"</span><span class="pln">&nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"75"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"meter2range"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp;oninput</span><span class="pun">=</span><span class="atv">"</span><span class="pln">effect</span><span class="pun">(</span><span class="str">'meter2'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'meter2range'</span><span class="pun">)</span><span class="atv">"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;output</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"meter2val"&nbsp;<span style="color: #660066; line-height: 25.6000003814697px;">for</span>="meter2range"</span><span class="tag">&gt;&lt;/output&gt;&lt;/p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">function</span><span class="pln"> effect</span><span class="pun">(</span><span class="pln">meter</span><span class="pun">,</span><span class="pln"> meterrange</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> currVal </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="pln">meterrange</span><span class="pun">).</span><span class="pln">value</span><span class="pun">;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="pln">meter</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> currVal</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="pln">meter</span><span class="pun">+</span><span class="pln"> </span><span class="str">"val"</span><span class="pun">).</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> currVal</span><span class="pun">;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
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

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;progress</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">pr</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">50</span><span class="pln"> </span><span class="atn">min</span><span class="pun">=</span><span class="atv">0</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">100</span><span class="tag">&gt;</span></li>
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

<div class="exampleHTML">This example uses some JavaScript to simulate a download progress by changing in real time the <span style="font-family: 'courier new', courier;">value</span> attribute.
<p>The progress below is defined like this:</p>
<pre>&lt;progress id=pr value=100 max=1000&gt;</pre>
<p>Download progress: <progress id="pr" value="331" max="1000" min="0"></progress></p>
</div>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="typ">Download</span><span class="pln"> progress</span><span class="pun">:</span><span class="pln"> </span><strong><span class="pun">&lt;</span><span class="pln">progress id</span><span class="pun">=</span><span class="pln">pr value</span><span class="pun">=</span><span class="lit">100</span><span class="pln"> min</span><span class="pun">=</span><span class="lit">0</span><span class="pln"> max</span><span class="pun">=</span><span class="lit">1000</span><span class="pun">&gt;&lt;/</span><span class="pln">progress</span><span class="pun">&gt;</span></strong><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="str">&lt;script&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> i</span><span class="pun">=</span><span class="lit">0</span><span class="pun">;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pln">setInterval</span><span class="pun">(</span><span class="kwd">function</span><span class="pln"> </span><span class="pun">(</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;i </span><span class="pun">=</span><span class="pln"> </span><span class="pun">(</span><span class="pln">i</span><span class="pun">+</span><span class="lit">1</span><span class="pun">)</span><span class="pln"> </span><span class="pun">%</span><span class="lit">1000</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;document</span><span class="pun">.</span><span class="pln">getElementById</span><span class="pun">(</span><span class="str">'pr'</span><span class="pun">).</span><span class="pln">value </span><span class="pun">=</span><span class="pln"> i</span><span class="pun">;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp;},</span><span class="lit">1</span><span class="pun">);</span></li>
<li class="L7" style="margin-bottom: 0px;"><span style="color: #008800; line-height: 25.6000003814697px;">&lt;/script&gt;</span></li>
</ol></div>




