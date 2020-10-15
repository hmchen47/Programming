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







