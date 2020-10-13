# Week 5: HTML5 Forms


## 5.4 Input types


### 5.4.0 Lecture Notes

+ [`color` type for `<input>` element](#542-color)
  + typical use: `<input type="color" value="#FF00FF"/>`
  + example: changing background color
    + `<input type="color">`: fire `change` or `input` events
    + HTML code to select color: `<input type="color" id="colorChooser"/>`
    + add listener: `colorInputField.addEventListener('input', function(evt) { document.body.style.backgroundColor = this.value; }, false);`
  + color selector
    + default: all colors
    + restricting the choices by using a `<datalist>` with some `<option>` elements inside
    + the `id` of the `<datalist>` element: the same as the value of the `list` attribute of the input field
    + e.g., `<datalist id="colors"> <option>#0000FF</option> <option>#00FF00</option> <option>#FF0000</option> </datalist>`
  + main criticism
    + default appearance
      + related to its default appearance being strongly dependent on the browser and its underlying operating system
      + not possible changing the look and feel, except with the use of the options
    + no way to control where the color chooser appears
      + not possible for positioning via CSS or JavaScript
      + specification not saying anything about how to position it over the page
      + vendor specific
      + web components: a new approach for designing HTML5 widgets proposed by the W3C

+ [`<input>` types](https://tinyurl.com/yxud45vl)

+ [`date` type of `<input>` element](#543-date)
  + HTML5 providing a special control to handle date and time pickers in HTML forms
  + desktop applications: Web developers would sometimes prefer 100% control over the look and feel of the date picker widget
  + solution: Web Components - a way to make custom reusable widgets in HTML/CSS/JS
  + non-supported browsers: default to an `<input type="text">` input field
  + default usage: `<label for="birthday">Choose birthday party date: </label> <input type="date" id="birthday">`
  + limiting choice: attributes `min`, `max` and `value`
    + used to propose a default date, a min and a max date, or for defining an interval of acceptable values
    + e.g., `<input type="date" id="birthdayParty" value="2015-06-20" min="2015-06-20" max="2015-06-30"> ...`
  + choosing one day in a given week, etc.: the `step:` attribute
    + `step=7`: make acceptable only the day of the week that corresponds to the value's day, e.g., only Monday
    + `step=2`: make acceptable only every other day
    + e.g., `<input type="date" id="birthdayParty" value="2015-06-20" min="2015-06-20" max="2015-06-30" step="7">`
  + restricting the choice of possible values
    + combining with the `<datalist>` element
    + `list` attribute of the `input` element must match the `id` attribute of the datalist element
    + example

    ```js
    <input type="date"
        id="birthdayParty"
        list="birthdayPartyPossibleDates"
        value="2015-06-20">
    <datalist id="birthdayPartyPossibleDates">
        <option label="Best for me">2015-06-20</option>
        <option label="Ok for me too ">2015-06-27</option>
        <option label="This one is a sunday, hmmm">2015-06-28</option>
    </datalist>
    ```

  + [changing date/time and others](#responding-to-date-changes-trying-datetime-and-other-variants)
    + `date` type: <input type="date" id="date" />
    + `datetime` type: <input type="time" id="date" />
    + `datetime-local` type: <input type="datetime-local" id="datetime-local" />
    + `time` type: <input type="time" id="time" />
    + `week` type: <input type="week" id="week" />
    + `month` type: <input type="month" id="month" />

  + [valueAsDate property](#checking-if-the-chosen-date-is-in-the-past-or-in-the-future-using-the-valueasdate-property)
    + a JavaScript date object compared to other JavaScript date objects
    + the date of the day: `var date = new Date();`
    + example: compare the date picked in the calendar widget with the current date

      ```js
      if(date.valueAsDate <= new Date()) {
          pastFuture.style.color = 'green';
          pastFuture.innerHTML = "<b>Date in the past, ok!</b>"
      } else {
          pastFuture.style.color = 'red';
            pastFuture.innerHTML = "<b>Date in the future, you're not even born!</b>"
      }
      ```




### 5.4.1 Input types

In this section, we briefly present the input types, attributes, and elements related to the forms that came with HTML5. Details are given later, illustrated by multiple interactive examples.

Compared to HTML4, HTML5 introduced 13 new input types, covering most of the needs of  Web developers. HTML5 packages some of the "form best practices" in its specification. Web browsers providing native implementation give a boost in performance, and reduce the size of JavaScript embedded in complex Web pages.

MDN's Web docs [article on `<input>` types](https://tinyurl.com/yxud45vl) lists all input types and highlights those that came with HTML5.

Now, let's play with some of these input types and attributes.


### 5.4.2 "color"

For years, we used hundreds of lines of JavaScript for selecting colors. Now, it's bundled in the browser!

Here is how it looks on some mobile devices:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/yxnpbsf2"
    alt    ="HTML5 input type=color on an android phone"
    title  ="HTML5 input type=color on an android phone"
  />
</figure>


#### Typical use

Inserting a color chooser is as simple as:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; Choose a color : </span><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"color" value="#FF00FF"</span><span class="tag">/&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Note: In this chapter we are simplifying the examples, as we usually embed input elements in a `<form>`...`</form>`.

Try `<input type="color">` online with this [JSBin example](https://jsbin.com/cajuzob/1/edit?html,output). Or do it here in your browser: just click on the purple square below : <input value="#FF00FF" type="color"> ([Local Example - Color Plate](src/5.4.2-example1.html))

Here is the result on Google Chrome (works with other browsers too, though the look and feel may differ):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/y2spxe7s"
    alt    ="input type=color in google chrome"
    title  ="input type=color in google chrome"
  />
</figure>


__Example: changing the background color of the page__

The `<input type="color">` can fire `change` or `input` events. Here is an example that changes the background color of the page when a color is chosen. [Try it online at JSBin](https://jsbin.com/jozuter/1/edit?html,css,js,console,output). ([Local Example - Background Color](src/5.4.2-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/y4fhse8z"
    alt    ="change background color of the body"
    title  ="change background color of the body"
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;&lt;head&gt;&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; Select a color : </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"color"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"colorChooser"</span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> colorInputField </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#colorChooser"</span><span class="pun">);<br></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;<strong>colorInputField</strong></span><strong><span class="pun">.</span><span class="pln">addEventListener</span><span class="pun">(</span><span class="str">'input'</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document</span><span class="pun">.</span><span class="pln">body</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">backgroundColor </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><strong><span class="pln">&nbsp; &nbsp; &nbsp;&nbsp;</span><span class="pun">},</span><span class="pln"> </span><span class="kwd">false</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><strong><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


#### Offer a limited choice of colors

By default, the color selector offers many options that may either frighten some users or just not be appropriate for the purpose of the application.

Good news: it is possible to restrict the choices, and also simplify the user interface, by using a `<datalist>` with some `<option>` elements inside. 

Example: click the black rectangle on the right: <input list="colors" value="#333333" type="color">. The following should be displayed:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/y452y3ur')"
    src    ="https://tinyurl.com/y4wpv7ne"
    alt    ="restricted choice of color"
    title  ="restricted choice of color"
  />
</figure>


[Online example at JSBin](https://jsbin.com/lahapu/edit?html,output) ([Local Example - Limited Colors](src/5.4.2-example3.html))

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"color"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"#333333"</span><span class="pln"> </span><strong><span class="atn">list</span><span class="pun">=</span><span class="atv">"colors"</span></strong><span class="tag">&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;datalist</span><span class="pln"> </span><strong><span class="atn">id</span><span class="pun">="</span><span class="atv">colors"</span></strong><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option&gt;</span><span class="pln">#0000FF</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option&gt;</span><span class="pln">#00FF00</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option&gt;</span><span class="pln">#FF0000</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/datalist&gt;</span></li>
</ol></div>

Note that the `id` of the `<datalist>` element should be the same as the value of the `list` attribute of the input field.


#### What are the main problems with this element?

The main criticism that Web designers make about this element is related to its default appearance being strongly dependent on the browser and its underlying operating system. Changing the look and feel is not possible, except with the use of the options we saw in the previous sections of this page. This problem is also true for other input elements that renders as complex widgets, like `<input type="date">` and its variants.

Another problem is that there is no way to control where the dialog that contains the color chooser will appear - no positioning via CSS or JavaScript is possible. The specification does not say anything about how to position it over the page, thus the result is vendor specific.

The solution proposed by the W3C and its contributors is called _Web Components_, a new approach for designing HTML5 widgets, that is covered in the W3Cx HTML5 Apps and Games course.


#### Knowledge check 5.4.2 

1. On mobile devices, `<input type=color>` pops up a dialog that is adapted to each operating system (IOS, Android, etc.). On desktops, the native implementations differ in their look'n'feel. Is it possible to thoroughly customize the look'n'feel of this input type using only CSS and HTML attributes? (Yes/No)

  Ans: No <br/>
  Explanation: No, while having adapted look and feels on mobile is appreciated, this is not the case on desktops. Web developers would like greater control over where the dialog pops up, about the user interface, etc. The solution comes with Web Components that will be studied in another course. Correct answer is NO.


### 5.4.3 "date"

For years, date and time pickers in HTML forms made Web developers rely heavily on JavaScript based widgets. The process is simpler in HTML5, which provides a special control to handle this specific kind of data natively.

Below are a few screenshots of the HTML5 date picker on several mobile devices. Note that the native date pickers of the operating systems are used:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2phefal" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y4pt9mfx"
      alt  ="JavaScript date picker, barred"
      title="JavaScript date picker, barred"
    >
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y36pz4e2"
      alt  ="date picker 1 date picker 2 on mobile date picker 3 on mobile"
      title="date picker 1 date picker 2 on mobile date picker 3 on mobile"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yxshef7n"
      alt  ="date picker 1 date picker 2 on mobile date picker 3 on mobile"
      title="date picker 1 date picker 2 on mobile date picker 3 on mobile"
    >
  </a>
</div>


The problem is different on a desktop. While it's great to have native support for a date picker, Web developers would sometimes prefer 100% control over the look and feel of the date picker widget. For this purpose, the solution undoubtedly lies with the new [Web Components](https://webcomponents.org/) (a way to make custom reusable widgets in HTML/CSS/JS), to be detailed in the W3Cx HTML5 Apps and Games course

<p class="exampleHTML">Why don't you try it yourself? Just click on this input field: &nbsp; &nbsp;<input type="date"></p>

With Firefox, it shows this date picker widget:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y2phefal')"
    src    ="https://tinyurl.com/y553k8he"
    alt    ="Firefox desktop date picker"
    title  ="Firefox desktop date picker"
  />
</figure>

On non-supported browsers, it defaults to an `<input type="text">` input field.


#### Typical use of `<input type="date">`

__Default use__

The default usage is something like:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"birthday"</span><span class="tag">&gt;</span><span class="pln">Choose birthday party date: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"birthday"</span><span class="tag">&gt;</span></li>
</ol></div>


<p class="exampleHTML">Result: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<label for="birthday">Choose birthday party date: &nbsp; &nbsp;&nbsp;</label> <input id="birthday" type="date"></p>

Most of the time you will add other attributes to give some restrictions (choose a date in the past, in the future, only on a Saturday, etc.).

__Restrict choice to an interval of dates: attributes `min`, `max` and `value`__

The `<input type="date">` comes with several useful attributes. In particular the `value`, `min` and `max` attributes are used to propose a default date, a min and a max date, or for defining an interval of acceptable values.

Try this example: just click the next input field: <input id="birthday party" min="2015-06-20" max="2015-31-06" value="2015-06-30" type="date">, or [try it online on JSBin](https://jsbin.com/faluta/1/edit?html,output) if you want to tweak the source code: ([Local Example - Limited](src/5.4.3-example1.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y2phefal')"
    src    ="https://tinyurl.com/y5y2whzt"
    alt    ="input type = date with min and max attributes. This will render two non selectable areas (dates before min and dates after max). Only the dates between min and max are selectable in the displayed calendar."
    title  ="input type = date with min and max attributes. This will render two non selectable areas (dates before min and dates after max). Only the dates between min and max are selectable in the displayed calendar."
  />
</figure>


Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1">...</li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"birthdayParty"</span><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="atn">value</span><span class="pun">=</span><span class="atv">"2015-06-20"</span></strong><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="atn">min</span><span class="pun">=</span><span class="atv">"2015-06-20"</span></strong><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><strong><span class="atn">max</span><span class="pun">=</span><span class="atv">"</span></strong><strong><span class="atv">2015-06-30"</span></strong><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;">...</li>
</ol></div>


__Choosing one day in a given week, etc. with the `step:` attribute__

Using the value attribute for setting a date, and using step=7 for example, will make acceptable only the day of the week that corresponds to the value's day (e.g.: only Mondays). Using step=2 will make acceptable only every other day, etc.

Example: we want to celebrate birthday parties only on Saturdays, [check this on JSBin](https://jsbin.com/hudafo/1/edit?html,output)! (screenshot from Chrome). ([Local Example - Multiplicated](src/5.4.3-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y2phefal')"
    src    ="https://tinyurl.com/y5lh8s4l"
    alt    ="use of the step attribute, select only saturdays"
    title  ="use of the step attribute, select only saturdays"
  />
</figure>


Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"birthdayParty"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"2015-06-20"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="atn">min</span><span class="pun">=</span><span class="atv">"2015-06-20"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="atn">max</span><span class="pun">=</span><span class="atv">"</span><span class="atv">2015-06-30"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="atn">step</span><span class="pun">=</span><span class="atv">"7"</span></strong><span class="tag">&gt;</span></li>
</ol></div>

Combining with the `<datalist>` element to restrict the choice of possible values

[Online example at JSBin](https://jsbin.com/gezawe/1/edit?html,output) (screenshot from Chrome). ([Local Example - Restricted](src/5.4.3-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y2phefal')"
    src    ="https://tinyurl.com/y2yhjjc2"
    alt    ="restrict choices using a datalist element"
    title  ="restrict choices using a datalist element"
  />
</figure>


Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"birthdayParty"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="atn">list</span><span class="pun">=</span><span class="atv">"birthdayPartyPossibleDates"</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"2015-06-20"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;datalist</span><span class="pln"> </span><strong><span class="atn">id</span><span class="pun">=</span><span class="atv">"birthdayPartyPossibleDates"</span></strong><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Best for me"</span><span class="tag">&gt;</span><span class="pln">2015-06-20</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp;&lt;option</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"Ok for me too "</span><span class="tag">&gt;</span><span class="pln">2015-06-27</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &nbsp;&lt;option</span><span class="pln"> </span><span class="atn">label</span><span class="pun">=</span><span class="atv">"This one is a sunday, hmmm"</span><span class="tag">&gt;</span><span class="pln">2015-06-28</span><span class="tag">&lt;/option&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/datalist&gt;</span></li>
</ol></div>

__The list attribute of the input element must match the id attribute of the datalist element.__

__If you use the min, max, or step attributes with a list attribute, it may filter the restricted list even more.__ Check [this example on JSBin](https://jsbin.com/gucuxon/1/edit?html,output) (tested with Google Chrome), that has a restricted list of three elements, one of which is filtered because it is not in in the min/max range. ([Local Example - Filtered](src/5.4.3-example4.html))


#### Responding to date changes, trying date/time and other variants

__Listening to the input event__

Here is [an interactive example at JSBin](https://jsbin.com/ganipuv/edit?html,output) where you can change the type of date/time chooser. It also shows how to listen to the input event when a date/time is chosen. ([Local Example - Input Event](src/5.4.3-example5.html))

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">Testing the new date input field.</span><span class="tag">&lt;p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> Choose a date/time : </span><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span></strong><span class="tag"><strong>/&gt;</strong>&lt;/p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> You picked: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"pickedDate"</span><span class="tag">&gt;&lt;/span&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/p&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">After you have tried the first example, change the value of the "type" attribute to:</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;ul&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;li&gt;</span><span class="pln">datetime</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;li&gt;</span><span class="pln">datetime-local</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;li&gt;</span><span class="pln">time</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;li&gt;</span><span class="pln">week</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;li&gt;</span><span class="pln">month</span><span class="tag">&lt;/li&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/ul&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">And see the result.</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;script&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="kwd">var</span><span class="pln"> field </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#date"</span><span class="pun">);</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> result </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#pickedDate"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln"> field</span><span class="pun">.</span><span class="pln">oninput </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="kwd">var</span><span class="pln"> date </span><span class="pun">=</span><span class="pln"> </span><strong><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;pickedDate</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;b&gt;"</span><span class="pun">+</span><span class="pln">date</span><span class="pun">+</span><span class="str">"&lt;/b&gt;"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

_Lines 20-26_ show how we can detect a date change using JavaScript.


#### Checking if the chosen date is in the past or in the future using the valueAsDate property

The object returned to the input event handler has a useful property named valueAsDate. This is a JavaScript date object that can be compared to other JavaScript date objects, in particular to the date of the day we can get with `var date = new Date();`

[The following example at JSBin](https://jsbin.com/renevaf/edit?html,output) shows how to ascertain whether a date is in the past or in the future: (left diagram) ([Local Example - valueAsDate](src/5.4.3-example6.html)) & While if we enter a date in the future: (right diagram)

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2phefal" ismap target="_blank">
    <img style="margin: 0.1em;" height=350
      src  ="https://tinyurl.com/yyp69h86"
      alt  ="date in the past, it's ok"
      title="date in the past, it's ok"
    >
    <img style="margin: 0.1em;" height=100
      src  ="https://tinyurl.com/yyxp2ggc"
      alt  ="date in the future: bad"
      title="date in the future: bad"
    >
  </a>
</div>


Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"birthDate"</span><span class="tag">&gt;</span><span class="pln">Enter your birth date: </span><span class="tag">&lt;/label&gt;&lt;p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"birthDate"</span><span class="pln"> </span><span class="tag">&gt;</span></strong></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> You picked: </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"pickedDate"</span><span class="tag">&gt;&lt;/span&gt;&lt;p&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;span</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"pastFuture"</span><span class="tag">&gt;&lt;/span&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/p&gt;</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;script&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> field </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#birthDate"</span><span class="pun">);</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> result </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#pickedDate"</span><span class="pun">);</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="kwd">var</span><span class="pln"> pastFuture </span><span class="pun">=</span><span class="pln"> document</span><span class="pun">.</span><span class="pln">querySelector</span><span class="pun">(</span><span class="str">"#pastFuture"</span><span class="pun">);</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><strong><span class="pln"> field</span><span class="pun">.</span><span class="pln">oninput </span></strong><span class="pun">=</span><span class="pln"> </span><span class="kwd">function</span><span class="pun">(</span><span class="pln">evt</span><span class="pun">)</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">var</span><span class="pln"> date </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">this</span><span class="pun">.</span><span class="pln">value</span><span class="pun">;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;pickedDate</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;b&gt;"</span><span class="pun">+</span><span class="pln">date</span><span class="pun">+</span><span class="str">"&lt;/b&gt;"</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><strong><span class="kwd">if</span><span class="pun">(date</span><span class="pun">.</span><span class="pln">valueAsDate </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Date</span><span class="pun">())</span></strong><span class="pln"> </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;pastFuture</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'green'</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;pastFuture</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;b&gt;Date in the past, ok!&lt;/b&gt;"</span><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;pastFuture</span><span class="pun">.</span><span class="pln">style</span><span class="pun">.</span><span class="pln">color </span><span class="pun">=</span><span class="pln"> </span><span class="str">'red'</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; pastFuture</span><span class="pun">.</span><span class="pln">innerHTML </span><span class="pun">=</span><span class="pln"> </span><span class="str">"&lt;b&gt;Date in the future, you're not even born!&lt;/b&gt;"</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="pun">}</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="pun">}</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/script&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
</ol></div>

_Lines 17-23_ show how we can compare the date picked in the calendar widget with the current date. Note that we can compare any given dates using JavaScript. To check that the chosen date is before 2000 we would do this:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="kwd">if</span><span class="pun">(</span><span class="kwd">this</span><span class="pun">.</span><span class="pln">valueAsDate </span><span class="pun">&lt;=</span><span class="pln"> </span><span class="kwd">new</span><span class="pln"> </span><span class="typ">Date</span><span class="pun">(</span><span class="lit">2000</span><span class="pun">,</span><span class="lit">1</span><span class="pun">,</span><span class="lit">1</span><span class="pun">))</span><span class="pln"> </span><span class="pun">{</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pun">...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pun">}</span></li>
</ol></div>


__`<input type="datetime">`, "week", "month", "datetime-local", etc.__

The HTML5 specification indicates that we can use <input type="date"> and <input type="time"> while for some years (before the specification became a frozen standard in October 2014), other variants were also present, such as type=datetime, datetime-local, month and week.

[Here is an interactive example at JSBin](https://jsbin.com/supope/1/edit) where you can change the type of date chooser and try all the different possible values for the type attribute of date pickers. ([Local Example - datetime type](src/5.4.3-example7.html))

Some screenshots from Opera desktops and Safari IOS:

`<input type="time">`:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2phefal" ismap target="_blank">
    <img style="margin: 0.1em;" height=30
      src  ="https://tinyurl.com/y4q5dj5x"
      alt  ="time"
      title="time"
    >
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y5hcnldd"
      alt  ="input type=time safari IOS"
      title="input type=time safari IOS"
    >
  </a>
</div>

`<input type="datetime">`:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2phefal" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yyv5mz4n"
      alt  ="datetime"
      title="datetime"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y3rgozpn"
      alt  ="input type=datetime on safari IOS"
      title="input type=datetime on safari IOS"
    >
  </a>
</div>


`<input type="datetime-local">` & `<input type="week">`: 

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2phefal" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y6kaksqq"
      alt  ="datetime-local example"
      title="datetime-local example"
    >
    <img style="margin: 0.1em;" height=100
      src  ="https://tinyurl.com/y2k5r43b"
      alt  ="week"
      title="week"
    >
  </a>
</div>


`<input type="month">`:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y2phefal" ismap target="_blank">
    <img style="margin: 0.1em;" height=100
      src  ="https://tinyurl.com/y2gxpgol"
      alt  ="month"
      title="month"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y3t73mbt"
      alt  ="input type=month safari IOS"
      title="input type=month safari IOS"
    >
  </a>
</div>



#### Knowledge check 5.4.3

1. Which attributes are useful to constrain the user to choose a specific day in the week, such as Monday, Tuesday, etc.? (two correct answers)

  a. min<br/>
  b. max<br/>
  c. step<br/>
  d. only<br/>
  e. value<br/>

  Ans: ae<br/>
  Explanation: The value and step attributes, when used together, restrict the user to pick only one day of the week. For example `<input type="date" value="2015-06-21" step="7">` will pick only Sundays, such as the 21st of June 2015 which is a Sunday. Try it!


### 5.4.4 "email", "tel", "URL" and "search"

Let's study 4 input types: email", "tel", "URL" and "search".

`<input type="email">`

This input type is relatively straightforward to use. In mobile applications, this new input type pops up a keyboard layout adapted to email input. Note the "@" key, the "." key, etc.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y5ma3qeo')"
    src    ="https://tinyurl.com/y3cv7hu4"
    alt    ="contextual mobile keyboard for entering an email address"
    title  ="contextual mobile keyboard for entering an email address"
  />
</figure>


This input type is very interesting as it provides default validation behaviors:

+ If the value entered looks like an email address (contains a "@"...), the field is valid, and gets the pseudo CSS class `:valid`
+ If the value entered does not contain an "@", and does not look like an email address, the field is invalid and gets the pseudo CSS class `:invalid`

See the next example to see this in action. More details will be presented in a later section dedicated to form validation.

Typical use:

[Online example at CodePen](https://codepen.io/w3devcampus/pen/aWXKWR) ([Local Example - Email](src/5.4.4-example1.html))

<p class="exampleHTML">Try it on your browser: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<label for="email">Enter your email: </label> <input id="email2" type="email"></p>

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of input type=email</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;style&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>input</strong></span><strong><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>background</strong></span><strong><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">pink</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><strong><span class="pun">}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/style&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"email"</span><span class="tag">&gt;</span><span class="pln">Enter your email </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"email"</span><span class="tag">&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Note the CSS rule that turns the background color of the email input field to pink if a user enters an invalid address (lines 7-8). Also note that the validation is based only on matching a regular expression (the address should contain a "@",  a ".", etc.). It does not check if the address is an existing one.

`<input type="tel">`

This input field is really useful on smartphones and tablets, as it makes the browser pop up a keyboard layout suitable for entering phone numbers:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y5ma3qeo" ismap target="_blank">
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/y6buy7rm"
      alt  ="mobile keyboard 1 for input type=tel other mobile keyboard for input type=tel"
      title="mobile keyboard 1 for input type=tel other mobile keyboard for input type=tel"
    >
    <img style="margin: 0.1em;" height=150
      src  ="https://tinyurl.com/yxzjyts9"
      alt  ="mobile keyboard 1 for input type=tel other mobile keyboard for input type=tel"
      title="mobile keyboard 1 for input type=tel other mobile keyboard for input type=tel"
    >
  </a>
</div>


This input type is often used with the new `placeholder` and `pattern` attributes that are detailed in another section of this course. It is supported by all recent major Web browsers, on mobile devices and desktops.

[Online example on CodePen](https://codepen.io/w3devcampus/pen/Njozvd) ([Local Example - Telephone](src/5.4.4-example2.html))


Try it in your browser (we used the same CSS for changing the background-color when the input value is invalid):

<div class="exampleHTML"><label for="tel">Enter a telephone number:</label> <input id="tel" placeholder="(555) 555-5555" pattern="^\(?\d{3}\)?[-\s]\d{3}[-\s]\d{4}.*?$" type="tel"></div>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html </span><span class="tag"><strong><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span></strong>&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;meta </span><span class="tag"><strong><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span></strong>&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of input type=tel</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;style&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; input</span><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">pink</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pun">&nbsp; }</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&lt;/style&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"tel"</span><span class="tag">&gt;</span><span class="pln">Enter a telephone number:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"tel"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"tel"</span></strong><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; placeholder</span><span class="pun">=</span><span class="atv">"(555) 555-5555"</span></strong><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; <strong>pattern</strong></span><strong><span class="pun">=</span><span class="atv">"<strong style="font-family: 'Courier New'; line-height: 23.2727279663086px;"><span class="atv">^(?<strong style="color: #3c3c3c; line-height: 23.2727279663086px;"><span class="atv">\</span></strong>d{3})?[-<strong style="color: #3c3c3c; line-height: 23.2727279663086px;"><span class="atv">\</span></strong>s]\d{3}[-<strong style="color: #3c3c3c; line-height: 23.2727279663086px;"><span class="atv">\</span></strong>s]<strong style="color: #3c3c3c; line-height: 23.2727279663086px;"><span class="atv">\</span></strong>d{4}.*?</span></strong><strong style="font-family: 'Courier New'; line-height: 23.2727279663086px;"><span class="atv"><strong style="color: #3c3c3c; line-height: 23.2727279663086px;"><span class="atv">\)</span></strong></span></strong>"</span><span class="tag">/&gt;</span></strong></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span><span class="pln"> </span></li>
</ol></div>


#### `<input type="URL">`

This input field is really useful on smartphones and tablets, as it makes the browser pop up a keyboard layout suitable for entering URLs:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y5ma3qeo')"
    src    ="https://tinyurl.com/y4xbpxhf"
    alt    ="mobile keyboard for entering URLs"
    title  ="mobile keyboard for entering URLs"
  />
</figure>


This field is also compatible with _the validation API_ (more on this in another section).

Here is an online example that shows the use of the `placeholder` and `pattern` attributes for entering only URLs that start with `ftp://` or `https://`

Or try it here in your browser:

Enter a URL (default validation):

<div class="exampleHTML"><label for="url1">Enter a URL (default validation):</label> <input id="url" type="url">
<p><label for="url2">Enter a URL (custom validation, must start with http, https or ftp):</label> <input id="url2" placeholder="https://www.domain.com" pattern="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*" type="url"></p>
</div>

Source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html </span><span class="tag"><span class="tag">lang="en"</span>&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head &gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp;&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;title&gt;</span><span class="pln">Example of input type=url</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;style&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; input</span><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightPink</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pun">&nbsp; &nbsp; }</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/style&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"url1"</span><span class="tag">&gt;</span><span class="pln">Enter a URL (default validation):</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"url"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"url1"</span><span class="tag">/&gt;</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp;&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"url2"</span><span class="tag">&gt;</span><span class="pln">Enter a URL (custom validation, must start with http, https or ftp):</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; <strong>&lt;input<span style="color: #000000;" color="#000000">&nbsp;</span></strong></span><strong><span class="atn">id</span><span class="pun">=</span><span class="atv">"url2"&nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"url"&nbsp;</span><span class="atn">placeholder</span><span class="pun">=</span><span class="atv">"https://www.domain.com"</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>pattern</strong></span><strong><span class="pun">=</span><span class="atv">"(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*"</span><span class="tag">/&gt;&lt;p&gt;</span></strong></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

_Lines 16-17_ show the use of a pattern attribute with a JavaScript regexp that accepts only URLs starting with http, https or ftp. More details on the pattern attribute are given in the section that presents the new HTML5 form attributes.


#### `<input type="search">`

The search type is used for search fields (i.e., for a search engine). A search field behaves like a regular text field, except that it may provide some feedback GUI for stopping the current request and emptying the search field, or it may provide a drop-down list of recent search results.

The specification does not state what the GUI should look like, so current implementations show variations in the look and feel.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5ma3qeo')"
    src    ="https://tinyurl.com/y2wgkp54"
    alt    ="input type=search rendered on a smartphone"
    title  ="input type=search rendered on a smartphone"
  />
</figure>


Typical use:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"search1"</span><span class="tag">&gt;</span><span class="pln">Simple search: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">search</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"search1"</span><span class="tag">&gt;</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"search2"</span><span class="tag">&gt;</span><span class="pln">Search with attribute </span><span class="tag">&lt;code&gt;</span><span class="pln">results=5</span><span class="tag">&lt;/code&gt;</span><span class="pln"> (try with Safari): </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><strong><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">search</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"search2"</span><span class="pln"> </span><span class="atn">results</span><span class="pun">=</span><span class="atv">5</span><span class="tag">&gt;</span></strong></li>
</ol></div>

Results on Chrome and Opera desktop - notice the small cross on the right when one enters a value:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5ma3qeo')"
    src    ="https://tinyurl.com/y2nvzuhf"
    alt    ="input type=search in google chrome and opera"
    title  ="input type=search in google chrome and opera"
  />
</figure>


Same example with Safari desktop, this time the second line with an attribute results=5 shows a small icon on the left:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y5ma3qeo')"
    src    ="https://tinyurl.com/yxan4tbr"
    alt    ="input type=search on safari"
    title  ="input type=search on safari"
  />
</figure>


Example that shows a drop down list of recent searches (Safari screenshot borrowed from [this excellent site about HTML5 forms that is worth reading](https://www.wufoo.com/html5/types/5-search.html)):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/y5ma3qeo')"
    src    ="https://tinyurl.com/y2435jv8"
    alt    ="example 2 of input type=search on safari, shows recent results"
    title  ="example 2 of input type=search on safari, shows recent results"
  />
</figure>


#### Knowledge check 5.4.4

__Source code for the knowledge check below__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of input type=email</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;style&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; input</span><span class="pun">:<strong>?</strong></span><strong><span class="pln">&nbsp;</span></strong><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">pink</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; input</span><span class="pun">:<strong>??</strong></span><strong><span class="pln">&nbsp;</span></strong><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">lightGreen</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/style&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"email"</span><span class="tag">&gt;</span><span class="pln">Enter your email:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp;&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"email"</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


1. How could you fix the above code so that an invalid email address entered in the input field would turn its background color to pink?

  a. Instead of "?", I would put the string "invalid" and instead of "??", I would put the string "valid"<br/>
  b. Instead of "?", I would put the string "valid" and instead of "??", I would put the string "invalid"<br/>

  Ans: 







