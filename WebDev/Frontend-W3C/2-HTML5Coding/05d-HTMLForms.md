# Week 5: HTML5 Forms


## 5.4 Input types


### 5.4.0 Lecture Notes

+ Ref: [`<input>` types](https://tinyurl.com/yxud45vl)

 
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

+ [email type](#input-typeemail)
  + syntax: `<input type="email">`
  + mobile applications: pop up a keyboard layout adapted to email input
  + default validation behaviors
    + `:valid` pseudo CSS class: the value entered looks like an email address (contains a "@"...)
    + `:invalid` pseudo CSS class: value entered not containing an "@" or not looking like an email address
  + e.g.,  `input:invalid { background-color:pink; }`

+ [tel type](#input-typetel)
  + syntax: `<input type="tel">`
  + useful on smartphones and tablets
  + making the browser pop up a keyboard layout suitable for entering phone numbers
  + used with the new `placeholder` and `pattern` attributes
  + supported by all recent major Web browsers, on mobile devices and desktops
  + CSS `:invalid` pseudo code: `input:invalid { background-color:pink; }`
  + example

    ```js
    <input type="tel" id="tel"
            placeholder="(555) 555-5555"
            pattern="^(?\d{3})?[-\s]\d{3}[-\s]\d{4}.*?\)"/>
    ```

+ [URL type](#input-typeurl)
  + syntax: `<input type="URL">`
  + useful on smartphones and tablets
  + making the browser pop up a keyboard layout suitable for entering URLs
  + compatible with the validation API
  + using the `placeholder` and `pattern` attributes for entering only URLs that start with `ftp://` or `https://`
  + example:

    ```js
    <body>
      <label for="url1">Enter a URL (default validation):</label>
      <input type="url" id="url1"/>
      <p>
        <label for="url2">Enter a URL (custom validation, must start with http, https or ftp):</label>
          <input id="url2" type="url" placeholder="https://www.domain.com"
          pattern="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*"/>
      <p>
    </body>
    ```

    + `pattern` attribute with a JavaScript regexp that accepts only URLs starting with http, https or ftp

+ [search type](#input-typesearch)
  + syntax: `<input type="search">`
  + used for search fields (i.e., for a search engine)
  + behave like a regular text field
  + probably providing some feedback GUI for stopping the current request and emptying the search field
  + probably providing a drop-down list of recent search results
  + specification not stated what the GUI should look like
  + typical example:

    ```html
    <label for="search1">Simple search: </label>
    <input type=search id="search1">
 
    <label for="search2">Search with attribute <code>results=5</code> (try with Safari): </label>
    <input type=search id="search2" results=5>
    ```
  
+ [number type](#545-number)
  + syntax: ` <input type="number">`
  + useful for entering numerical values (integer or float)
  + providing a user interface with small vertical arrows for incrementing / decrementing the current value, while on mobiles it will display a numeric keyboard
  + zip codes: `<input type="text" pattern="......">`
  + typical usage: `<input type="number" value="25" min="0" step="5" max="500"/>`
    + specific attributes: `max`, `min`, `step`, `value`
    + default displayed value: `value`
  + `step` attribute w/ an integer value:
    + make the arrows increment/decrement the current value with the step value
    + make the input field valid only when the difference between the value you enter and min is a multiple of step
    + by default, omitting the step attribute is equivalent to step="1"
  + float values
    + use `step="any"` or step equal to a floating point value such as `step="0.1"`
    + `step="any"`: vertical arrows w/ increment/decrement the value by one
    + `step="0.1"`: arrows increment/decrement by 0.1, etc.
  + default validation behaviors
    + invalid field to get `:invalid` pseudo CSS class: not a valid number or not in the range
    + `valid` pseudo CSS class: difference between the value you enter and min is a multiple of step
      + `min=1` and `step=5`: valid w/ value=1, 6, 11, 16 etc.
      + `min=0` and `step=5`: valid w/ value=0, 5, 10, 15 etc.
    + example:
      + between 0 and 500, a multiple of 5 otherwise it's invalid: `<input type="number" id="number" value="25" min="0" step="5" max="500"/>`
      + CSS style:

        ```js
        #number:invalid {
          background-color:pink;
        }
        #number:valid {
          background-color:lightGreen;
        }
        ```

+ [range type](#546-range)
  + syntax: `<input type="range">`
  + render as a slider
  + attributes: `min`, `max`, `step` and `value`
  + typical usage: `<input id="slider6" type="range" min="0" max="10" step="2" value="5">`
  + example:
    + HTML code

      ```html
      <form >
        <label for="slider1">Select a value:</label>
        <input id="slider1" type="range" min="100" max="500" step="10" value="150"
          oninput="printValue('slider1','rangeValue1')"/>
        <output id="rangeValue1"></output>
      </form>
      ```

    + JS code

      ```js
      function printValue(sliderId, outputId) {
          var x = document.getElementById(outputId);
          var y = document.getElementById(sliderId);
          x.value = y.value;
      }
      ```

+ [`step` attribute w/ `range` type](#snapping-behavior-and-the-step-attribute)
  + click and drag the slider: "jump" to some snap points corresponding to the integer values of the range defined by the `min` and `max` attributes
  + size of the jumps: depend on the value of the step attribute
  + `step` attribute with an integer value: make the slider jump corresponding to the step value 
  + default: omitting the `step` attribute is equivalent to `step="1"`
  + float values: use `step="any"`, or step equal to a floating point value, such as `step="0.5"`

+ [slider ticks w/ `details` attribute](#adding-ticks-to-the-range-slider-using-a-datalist-element)
  + using the `<datalist>` element to display "ticks" above the range slider, at given positions
  + example: value=5 min=0, max=10 step=1, ticks at 2, 4, 6, 8 and 10

    ```html
    <input id="slider2" type="range"
          list="ticks2"
          min="0" max="10" step="1" value="5"/>
    <datalist id=ticks2>
        <option>0</option>
        <option>2</option>
        ...
    </datalist>
    ```

  + references
    + use CSS for "standard" styling: [CSS tricks](https://css-tricks.com/styling-cross-browser-compatible-range-inputs-css/)
    + automatically generates ticks: [Auto-Generated HTML5 range input Ticks](https://codepen.io/dudleystorey/pen/Klnzy)
    + MDN's Web Docs: [`<input type=range>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range)




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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &nbsp; Choose a color : <strong>&lt;input type="color" value="#FF00FF"/&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;&lt;head&gt;&lt;/head&gt;</li>
<li>&lt;body&gt; </li>
<li>&nbsp; Select a color : &lt;input type="color" id="colorChooser"/&gt;</li>
<li>&nbsp;&nbsp;&lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp;var colorInputField = document.querySelector("#colorChooser");<br></li>
<li></li>
<li>&nbsp; &nbsp; &nbsp;<strong>colorInputField</strong><strong>.addEventListener('input', function(evt) {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; document.body.style.backgroundColor = this.value;</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;&nbsp;}, false);</strong></li>
<li><strong> &lt;/script&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
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

<div><ol>
<li value="1"> &lt;input type="color" value="#333333" <strong>list="colors"</strong>&gt;</li>
<li> </li>
<li> &lt;datalist <strong>id="colors"</strong>&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;option&gt;#0000FF&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;option&gt;#00FF00&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;option&gt;#FF0000&lt;/option&gt;</li>
<li> &lt;/datalist&gt;</li>
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

<p>Why don't you try it yourself? Just click on this input field: &nbsp; &nbsp;<input type="date"></p>

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

<div><ol>
<li value="1">&lt;label for="birthday"&gt;Choose birthday party date: &lt;/label&gt;</li>
<li>&lt;input type="date" id="birthday"&gt;</li>
</ol></div>


<p>Result: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<label for="birthday">Choose birthday party date: &nbsp; &nbsp;&nbsp;</label> <input id="birthday" type="date"></p>

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

<div><ol>
<li value="1">...</li>
<li> &lt;input type="date" </li>
<li>&nbsp; &nbsp; &nbsp;id="birthdayParty" </li>
<li>&nbsp; &nbsp; &nbsp;<strong>value="2015-06-20"</strong> </li>
<li>&nbsp; &nbsp; &nbsp;<strong>min="2015-06-20"</strong> </li>
<li>&nbsp; &nbsp; &nbsp;<strong>max="</strong><strong>2015-06-30"</strong>&gt;</li>
<li>...</li>
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

<div><ol>
<li value="1">&lt;input type="date" </li>
<li>&nbsp; &nbsp;&nbsp;id="birthdayParty" </li>
<li>&nbsp; &nbsp;&nbsp;value="2015-06-20" </li>
<li>&nbsp; &nbsp;&nbsp;min="2015-06-20" </li>
<li>&nbsp; &nbsp;&nbsp;max="2015-06-30"</li>
<li>&nbsp; &nbsp;&nbsp;<strong>step="7"</strong>&gt;</li>
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

<div><ol>
<li value="1"> &lt;input type="date" </li>
<li>&nbsp; &nbsp;&nbsp;id="birthdayParty" </li>
<li>&nbsp; &nbsp;&nbsp;<strong>list="birthdayPartyPossibleDates"</strong></li>
<li>&nbsp; &nbsp;&nbsp;value="2015-06-20"&gt;</li>
<li> </li>
<li> &lt;datalist <strong>id="birthdayPartyPossibleDates"</strong>&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;option label="Best for me"&gt;2015-06-20&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;option label="Ok for me too "&gt;2015-06-27&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;option label="This one is a sunday, hmmm"&gt;2015-06-28&lt;/option&gt;</li>
<li> &lt;/datalist&gt;</li>
</ol></div>

__The list attribute of the input element must match the id attribute of the datalist element.__

__If you use the min, max, or step attributes with a list attribute, it may filter the restricted list even more.__ Check [this example on JSBin](https://jsbin.com/gucuxon/1/edit?html,output) (tested with Google Chrome), that has a restricted list of three elements, one of which is filtered because it is not in in the min/max range. ([Local Example - Filtered](src/5.4.3-example4.html))


#### Responding to date changes, trying date/time and other variants

__Listening to the input event__

Here is [an interactive example at JSBin](https://jsbin.com/ganipuv/edit?html,output) where you can change the type of date/time chooser. It also shows how to listen to the input event when a date/time is chosen. ([Local Example - Input Event](src/5.4.3-example5.html))

Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;&lt;head&gt;...&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>Testing the new date input field.&lt;p&gt;</li>
<li> Choose a date/time : <strong>&lt;input type="date" id="date" </strong><strong>/&gt;</strong>&lt;/p&gt;</li>
<li>&lt;p&gt; </li>
<li> You picked: &lt;span id="pickedDate"&gt;&lt;/span&gt;</li>
<li> &lt;/p&gt;</li>
<li>After you have tried the first example, change the value of the "type" attribute to:</li>
<li>&lt;ul&gt;</li>
<li>&lt;li&gt;datetime&lt;/li&gt;</li>
<li>&lt;li&gt;datetime-local&lt;/li&gt;</li>
<li>&lt;li&gt;time&lt;/li&gt;</li>
<li>&lt;li&gt;week&lt;/li&gt;</li>
<li>&lt;li&gt;month&lt;/li&gt;</li>
<li>&lt;/ul&gt;</li>
<li>And see the result.</li>
<li> </li>
<li>&lt;script&gt;</li>
<li> <strong>var field = document.querySelector("#date");</strong></li>
<li> var result = document.querySelector("#pickedDate");</li>
<li> </li>
<li><strong> field.oninput </strong>= function(evt) {</li>
<li>&nbsp; &nbsp;var date = <strong>this.value;</strong></li>
<li>&nbsp; &nbsp;pickedDate.innerHTML = "&lt;b&gt;"+date+"&lt;/b&gt;";</li>
<li>}</li>
<li> &lt;/script&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
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

<div><ol>
<li value="1">&lt;body&gt;</li>
<li>&lt;label for="birthDate"&gt;Enter your birth date: &lt;/label&gt;&lt;p&gt;</li>
<li> <strong>&lt;input type="date" id="birthDate" &gt;</strong></li>
<li> &lt;p&gt;</li>
<li> You picked: &lt;span id="pickedDate"&gt;&lt;/span&gt;&lt;p&gt;</li>
<li> &lt;span id="pastFuture"&gt;&lt;/span&gt;</li>
<li> &lt;/p&gt; </li>
<li> &lt;script&gt;</li>
<li> var field = document.querySelector("#birthDate");</li>
<li> var result = document.querySelector("#pickedDate");</li>
<li> var pastFuture = document.querySelector("#pastFuture");</li>
<li> </li>
<li><strong> field.oninput </strong>= function(evt) {</li>
<li>&nbsp; &nbsp;<strong>var date = this.value;</strong></li>
<li>&nbsp; &nbsp;pickedDate.innerHTML = "&lt;b&gt;"+date+"&lt;/b&gt;";</li>
<li> </li>
<li>&nbsp; &nbsp;<strong>if(date.valueAsDate &lt;= new Date())</strong> {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;pastFuture.style.color = 'green';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;pastFuture.innerHTML = "&lt;b&gt;Date in the past, ok!&lt;/b&gt;" </li>
<li>&nbsp; &nbsp;} else {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;pastFuture.style.color = 'red';</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; pastFuture.innerHTML = "&lt;b&gt;Date in the future, you're not even born!&lt;/b&gt;"</li>
<li>&nbsp; &nbsp;}</li>
<li> }</li>
<li> &lt;/script&gt;</li>
<li>&lt;/body&gt;</li>
</ol></div>

_Lines 17-23_ show how we can compare the date picked in the calendar widget with the current date. Note that we can compare any given dates using JavaScript. To check that the chosen date is before 2000 we would do this:

<div><ol>
<li value="1">if(this.valueAsDate &lt;= new Date(2000,1,1)) {</li>
<li>...</li>
<li>}</li>
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


#### `<input type="email">`

This input type is relatively straightforward to use. In mobile applicat ions, this new input type pops up a keyboard layout adapted to email input. Note the "@" key, the "." key, etc.

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

<p>Try it on your browser: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<label for="email">Enter your email: </label> <input id="email2" type="email"></p>

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Example of input type=email&lt;/title&gt;</li>
<li> &lt;style&gt;</li>
<li>&nbsp; &nbsp; <strong>input</strong><strong>:invalid {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>background</strong><strong>-color:pink;</strong></li>
<li>&nbsp; &nbsp; <strong>}</strong></li>
<li> &lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&lt;label for="email"&gt;Enter your email &lt;/label&gt;</li>
<li><strong>&lt;input type="email" id="email"&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

Note the CSS rule that turns the background color of the email input field to pink if a user enters an invalid address (lines 7-8). Also note that the validation is based only on matching a regular expression (the address should contain a "@",  a ".", etc.). It does not check if the address is an existing one.


#### `<input type="tel">`

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

<div><label for="tel">Enter a telephone number:</label> <input id="tel" placeholder="(555) 555-5555" pattern="^\(?\d{3}\)?[-\s]\d{3}[-\s]\d{4}.*?$" type="tel"></div>

Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html <strong>lang="en"</strong>&gt;</li>
<li>&lt;head&gt;</li>
<li>&lt;meta <strong>charset="utf-8"</strong>&gt;</li>
<li> &lt;title&gt;Example of input type=tel&lt;/title&gt;</li>
<li>&lt;style&gt; </li>
<li>&nbsp; input:invalid { </li>
<li>&nbsp; &nbsp; &nbsp; background-color:pink;</li>
<li>&nbsp; }</li>
<li>&lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt; </li>
<li> &lt;label for="tel"&gt;Enter a telephone number:&lt;/label&gt;</li>
<li> <strong>&lt;input type="tel" id="tel"</strong> </li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; placeholder="(555) 555-5555"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>pattern</strong><strong>="<strong style="font-family: 'Courier New'; line-height: 23.2727279663086px;">^(?<strong style="color: #3c3c3c; line-height: 23.2727279663086px;">\</strong>d{3})?[-<strong style="color: #3c3c3c; line-height: 23.2727279663086px;">\</strong>s]\d{3}[-<strong style="color: #3c3c3c; line-height: 23.2727279663086px;">\</strong>s]<strong style="color: #3c3c3c; line-height: 23.2727279663086px;">\</strong>d{4}.*?</strong><strong style="font-family: 'Courier New'; line-height: 23.2727279663086px;"><strong style="color: #3c3c3c; line-height: 23.2727279663086px;">\)</strong></strong>"/&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt; </li>
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

<div><label for="url1">Enter a URL (default validation):</label> <input id="url" type="url">
<p><label for="url2">Enter a URL (custom validation, must start with http, https or ftp):</label> <input id="url2" placeholder="https://www.domain.com" pattern="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*" type="url"></p>
</div>

Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head &gt;</li>
<li>&nbsp;&nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp;&lt;title&gt;Example of input type=url&lt;/title&gt;</li>
<li>&lt;style&gt;</li>
<li>&nbsp; &nbsp; input:invalid { </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; background-color: lightPink;</li>
<li>&nbsp; &nbsp; }</li>
<li>&lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;label for="url1"&gt;Enter a URL (default validation):&lt;/label&gt;</li>
<li> <strong>&lt;input type="url" id="url1"/&gt;</strong></li>
<li>&nbsp;&lt;p&gt;</li>
<li> &lt;label for="url2"&gt;Enter a URL (custom validation, must start with http, https or ftp):&lt;/label&gt; </li>
<li>&nbsp; &nbsp; <strong>&lt;input<span style="color: #000000;" color="#000000">&nbsp;</strong><strong>id="url2"&nbsp;type="url"&nbsp;placeholder="https://www.domain.com"</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>pattern</strong><strong>="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*"/&gt;&lt;p&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
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

<div><ol>
<li value="1">&lt;label for="search1"&gt;Simple search: &lt;/label&gt;</li>
<li><strong>&lt;input type=search id="search1"&gt;</strong></li>
<li>&lt;p&gt;</li>
<li>&lt;label for="search2"&gt;Search with attribute &lt;code&gt;results=5&lt;/code&gt; (try with Safari): &lt;/label&gt;</li>
<li><strong>&lt;input type=search id="search2" results=5&gt;</strong></li>
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

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Example of input type=email&lt;/title&gt;</li>
<li> &lt;style&gt;</li>
<li>&nbsp; &nbsp; input:<strong>?</strong><strong>&nbsp;</strong>{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; background-color:pink;</li>
<li>&nbsp; &nbsp;&nbsp;}</li>
<li>&nbsp; &nbsp; input:<strong>??</strong><strong>&nbsp;</strong>{</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; background-color:lightGreen;</li>
<li>&nbsp; &nbsp; }</li>
<li> &lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &nbsp;&lt;label for="email"&gt;Enter your email:&lt;/label&gt;</li>
<li>&nbsp; &nbsp;&lt;input type="email" id="email"&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


1. How could you fix the above code so that an invalid email address entered in the input field would turn its background color to pink?

  a. Instead of "?", I would put the string "invalid" and instead of "??", I would put the string "valid"<br/>
  b. Instead of "?", I would put the string "valid" and instead of "??", I would put the string "invalid"<br/>

  Ans: a<br/>
  Explanation: Indeed, the first answer is correct. The complete CSS code is:

    ```css
    input:invalid {
      background-color:pink;
    }
    input:valid {
      background-color:lightGreen;
    }
    ```

### 5.4.5 "number"

This input field is useful for entering numerical values (integer or float), but not for entering zip codes. On desktop implementations and on some mobile implementations, it provides a user interface with small vertical arrows for incrementing/decrementing the current value, while on mobiles it will display a numeric keyboard.

For zip codes, a `<input type="text" pattern="......">` is preferable. See examples given in the `pattern` attribute section of this course.

<p>Example:&nbsp;<span style="font-family: 'courier new', courier;"><strong>&lt;input&nbsp;type="number"&nbsp;value="25"&nbsp;min="0"&nbsp;step="5"&nbsp;max="500"</strong><strong>/&gt;</strong></p>

Screenshot example taken with a mobile device :

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 10vw;"
    onclick="window.open('https://tinyurl.com/yxdk64l8')"
    src    ="https://tinyurl.com/y53qrnb9"
    alt    ="numeric keyboard on safari IOS"
    title  ="numeric keyboard on safari IOS"
  />
</figure>


Examples on desktop (the width will be adjusted depending on the `min` and `max` attributes):

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/yxdk64l8')"
    src    ="https://tinyurl.com/yxb32cvd"
    alt    ="input type=number example"
    title  ="input type=number example"
  />
</figure>



#### Typical usage

<p><strong style="font-family: 'courier new', courier;">&lt;input&nbsp;type="number"&nbsp;value="25"&nbsp;min="0"&nbsp;step="5"&nbsp;max="500"</strong><span style="font-family: 'courier new', courier;"><strong>/&gt;</strong></span></p>

This field accepts specific attributes `max`, `min`, `step`, `value` (default displayed value). 

This input type is very interesting as it provides default validation behaviors:

+ If the value entered using a keyboard is not a valid number, or is not in the range defined by the `min` and `max` attributes, the field is _invalid_ and gets the pseudo CSS class `:invalid`.
+ If the difference between the `value` you enter and `min` is a multiple of `step`, then it gets the CSS pseudo class `:valid`, otherwise it will be _invalid_. Example: if `min=1` and `step=5`, the field will be valid with `value=1, 6, 11, 16` etc. if `min=0`, with `value=0, 5, 10, 15` etc.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><span style="color: #ff0000;"><strong>WARNING 1</strong></span>: <strong>Using a <span style="font-family: 'courier new', courier;">step</span>&nbsp;attribute with an integer&nbsp;value will make the arrows increment/decrement the current value with the <span style="font-family: 'courier new', courier;">step</span> value, and <span style="text-decoration: underline;">make the input field valid only when&nbsp;</span>the difference between the&nbsp;<span style="font-family: 'courier new', courier;">value</span>&nbsp;you enter and&nbsp;<span style="font-family: 'courier new', courier;">min</span> is&nbsp;a multiple of&nbsp;<span style="font-family: 'courier new', courier;"><strong>step.</strong>&nbsp;</span></strong></p>

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong><span style="color: #ff0000;">WARNING&nbsp;2</span>: by default, omitting the <span style="font-family: 'courier new', courier;">step</span> attribute is equivalent to<span style="font-family: 'courier new', courier;"> step="1"</span>, <span style="text-decoration: underline;">so for entering float values, it is necessary to use <span style="font-family: 'courier new', courier;">step="any"<span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;"> or step equal to a floating point value such as</span> step="0.1"</span></span><span style="font-family: 'courier new', courier;"><span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">. <br><br>With</span></span><span style="font-family: 'courier new', courier;"> step="any", <span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">floating point values are valid, but vertical arrows will increment/decrement the value by one. If </span>step="0.1"<span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">, arrows will increment/decrement by</span> 0.1<span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">, etc.</span></span></strong></p>

With step="any", floating point values are valid, but vertical arrows will increment/decrement the value by one. If step="0.1", arrows will increment/decrement by 0.1, etc.

[Online example in CodePen](https://codepen.io/w3devcampus/pen/GJrQzP):  (try changing the attribute values, use step="any" and try float values, etc). ([Local Example - Number](src/5.4.5-example1.html))


Or, do it here in your browser (Manually enter a value that is not in the range, or not a multiple of 5, try the up and down arrows, etc.):

<div style="border: 1px solid black; margin 20px; padding: 20px;"><label for="number">Quantity (between 0 and 500, should be a multiple of 5 otherwise it's invalid): </label> <input id="number" min="0" max="500" step="5" value="25" type="number"></div>

Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li value="1">....</li>
<li> &lt;style&gt;</li>
<li>&nbsp; &nbsp;<strong>#number:invalid {</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong>background</strong><strong>-color:pink;</strong></li>
<li>&nbsp; &nbsp;<strong>}</strong></li>
<li>&nbsp; &nbsp;<strong>#number:valid {</strong></li>
<li>&nbsp; &nbsp; &nbsp; <strong>background</strong><strong>-color:lightGreen;</strong></li>
<li>&nbsp; &nbsp;<strong>}</strong></li>
<li> &lt;/style&gt;</li>
<li> &lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> Example of &lt;code&gt;&lt;input type=number&gt;&lt;/code&gt;:&lt;p&gt;</li>
<li>&nbsp; &nbsp;&lt;label for="number"&gt;Quantity (between 0 and 500, should be a multiple of 5 otherwise it's invalid): &lt;/label&gt; </li>
<li><strong>&lt;input type="number" id="number" value="25" min="0" step="5" max="500"</strong><strong>/&gt;</strong></li>
<li>&lt;p&gt;</li>
<li> </li>
<li>Change the different values for attributes step, max, min, value. Don't forget to try step="any" for float values...</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


#### Knowledge check 5.4.5

__Source code for the knowledge check__

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Example type=number&lt;/title&gt;</li>
<li> &lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp;<strong>#myField:valid {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;background-color:lightGreen;</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;}</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;#myField:invalid {</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;background-color:pink;</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp;}</strong></li>
<li> &lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp; &nbsp;&lt;label for="myField"&gt;Please enter a number between 0 and 30: &lt;/label&gt;</li>
<li><strong>&nbsp; &nbsp;&lt;input type="number" id="myField" min="0" step="5" max="30"/&gt;</strong></li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


1. Suppose we enter the value 17 in the input field defined by the above code. What will the background color be?

  a. lightGreen<br/>
  b. pink<br/>
  c. red<br/>

  Ans: b<br/>
  Explanation: 17 is between `min=0` and `max=30` but is not a multiple of 5 (defined by `step=5`). The field is invalid, and will get the CSS pseudo class :invalid, so the background will turn pink! The online example is here: http://jsbin.com/mifuwu/edit


### 5.4.6 "range"

This input type renders as a slider. It accepts the same attributes as the `<input type="number">` : min, max, step and value.

Example of rendering on a desktop:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y6pnnfeu')"
    src    ="https://tinyurl.com/yyahxxko"
    alt    ="input type=range"
    title  ="input type=range"
  />
</figure>


And on mobile devices:

<div style="margin: 0.5em; display: flex; justify-content: center; align-items: center; flex-flow: row wrap;">
  <a href="https://tinyurl.com/y6pnnfeu" ismap target="_blank">
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y6moxfx5"
      alt  ="ios range input input type=range android"
      title="ios range input input type=range android"
    >
    <img style="margin: 0.1em;" height=250
      src  ="https://tinyurl.com/y29gnowu"
      alt  ="ios range input input type=range android"
      title="ios range input input type=range android"
    >
  </a>
</div>


Typical use

The basic use is to specify at least the `value`, `min` and `max` attributes, and eventually the `step` attribute, too:

<div><ol>
<li value="1">&lt;input id="slider6" type="range" min="0" max="10" step="2" value="5"&gt;</li>
</ol></div>

But most of the time, you will need a visual feedback that shows the current value selected by the slider.

[This online example on CodePen](https://codepen.io/w3devcampus/pen/BRMVGW) shows how to add a visual feedback using a very short JavaScript function and an <output> element. Just click and drag the small cursor of the slider (or use up and down arrow keys when the field has the focus): ([Local Example - Range](src/5.4.6-example1.html))


Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp; &nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp; &lt;title&gt;Example of input type=tel&lt;/title&gt;</li>
<li>&nbsp; &nbsp; &lt;style&gt;</li>
<li>&nbsp; &nbsp; &nbsp; #rangeValue1 {</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; border:1px solid black;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; padding:2px;</li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; &lt;/style&gt;</li>
<li>&nbsp; &nbsp; &lt;script&gt;</li>
<li>&nbsp; &nbsp; &nbsp; window.onload = function() {</li>
<li> // Called when the page is loaded, for displaying initial value in the output</li>
<li>&nbsp; &nbsp; &nbsp; printValue('slider1','rangeValue1');</li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; &nbsp; function printValue(sliderId, outputId) {</li>
<li>&nbsp; &nbsp; &nbsp; var x = document.getElementById(outputId);</li>
<li>&nbsp; &nbsp; &nbsp; var y = document.getElementById(sliderId);</li>
<li>&nbsp; &nbsp; &nbsp; x.value = y.value;</li>
<li>&nbsp; &nbsp; &nbsp; }</li>
<li>&nbsp; &nbsp; &lt;/script&gt;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp; &nbsp; &lt;form &gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;label for="slider1"&gt;Select a value:&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;input id="slider1" type="range"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; min="100" max="500" step="10" value="150"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; oninput="printValue('slider1','rangeValue1')"/&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;output id="rangeValue1"&gt;&lt;/output&gt;</li>
<li>&nbsp; &nbsp; &lt;/form&gt;</li>
<li>&nbsp; &nbsp; &lt;br/&gt;</li>
<li>&nbsp; &nbsp; &nbsp; Play with attributes: value, min, max, step...</li>
<li>&nbsp; &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


#### Snapping behavior and the step attribute


When you click and drag the slider, it "jumps" to some snap points corresponding to the integer values of the range defined by the min and max attributes. The "size of the jumps" depends on the value of the step attribute.

Try these examples in your browser and look at their behavior:

<div style="border: 1px solid black; margin: 20px; padding: 20px;">
<p><label for="slider2"><span style="font-family: 'courier new', courier;">value=5 min=0, max=10 step=1</span>: </label> <input id="slider2" oninput="printValue('slider2','rangeValue2')" min="0" max="10" step="1" value="5" type="range">&nbsp;<output id="rangeValue2"></output></p>
<p><label for="slider3"><span style="font-family: 'courier new', courier;">value=12 min=10, max=50 step=4</span>: </label> <input id="slider3" oninput="printValue('slider3','rangeValue3')" min="10" max="50" step="4" value="12" type="range">&nbsp;<output id="rangeValue3"></output></p>
Note that in the previous example, the default value displayed is 14, not 12 (the value just above <span style="font-family: 'courier new', courier;">min</span> plus an integer <span style="font-family: 'courier new', courier;">step</span> value). 12 is not possible so it's been "snapped" to 14.
<p><label for="slider4"><span style="font-family: 'courier new', courier;">value=5 min=0, max=10 step="0.5"</span>: </label> <input id="slider4" oninput="printValue('slider4','rangeValue4')" min="0" max="10" step="0.5" value="5" type="range">&nbsp;<output id="rangeValue4"></output></p>
In the previous example, it's necessary to add quotes for setting <span style="font-family: 'courier new', courier;">step="0.5"</span> (while HTML5 authorizes not using quotes for setting integer values to attributes).
<p><label for="slider5"><span style="font-family: 'courier new', courier;">value=5 min=0, max=10 step="any"</span>: </label> <input id="slider5" oninput="printValue('slider5','rangeValue5')" min="0" max="10" step="any" value="5" type="range">&nbsp;<output id="rangeValue5"></output></p>
</div>


<p style="border: 1px solid red; margin: 20px; padding: 20px;"><span style="color: #ff0000;"><strong>WARNING</strong></span>: Using a <span style="font-family: 'courier new', courier;">step</span>&nbsp;attribute with an integer&nbsp;value will make the slider&nbsp;jump corresponding to&nbsp;the <span style="font-family: 'courier new', courier;">step</span> value. By default, omitting the <span style="font-family: 'courier new', courier;">step</span> attribute is equivalent to<span style="font-family: 'courier new', courier;"> step="1".</span> <br>So, for accepting float values, it is necessary to use <span style="font-family: 'courier new', courier;">step="any"<span style="font-family: 'Open Sans', Verdana, Arial, Helvetica, sans-serif;">, or step equal to a floating point value, such as</span> step="0.5".</span></p>

#### Adding "ticks" to the range slider using a `<datalist>` element

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y6pnnfeu')"
    src    ="https://tinyurl.com/y6qtglqc"
    alt    ="complicated ticks on a rule"
    title  ="complicated ticks on a rule"
  />
</figure>


Using the `<datalist>` element, it's possible to display "ticks" above the range slider, at given positions.

<div><ol>
<li value="1">&lt;label for="slider2"&gt;value=5 min=0, max=10 step=1, ticks at 2, 4, 6, 8 and 10:&lt;/label&gt;</li>
<li><strong>&lt;input id="slider2" type="range"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>list</strong><strong>="ticks2"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;min="0" max="10" step="1" value="5"/&gt;</li>
<li><strong>&lt;datalist id=ticks2&gt;</strong></li>
<li>&nbsp; &nbsp; &lt;option&gt;0&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &lt;option&gt;2&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &lt;option&gt;4&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &lt;option&gt;6&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &lt;option&gt;8&lt;/option&gt;</li>
<li>&nbsp; &nbsp; &lt;option&gt;10&lt;/option&gt;</li>
<li>&lt;/datalist&gt;</li>
</ol></div>

Try the sliders below:

<div style="border: 1px solid black; margin: 20px; padding: 20px;">
<p><label for="slider6"><span style="font-family: 'courier new', courier;">value=5 min=0, max=10 step=1</span>, ticks at 2, 4, 6, 8 and 10: </label> <input id="slider6" oninput="printValue('slider6','rangeValue6')" min="0" max="10" step="1" list="ticks6" value="5" type="range">&nbsp;
<datalist id="ticks6">
<option>0</option><option>2</option><option>4</option><option>6</option><option>8</option><option>10</option>
</datalist>
<output id="rangeValue6"></output></p>
<p><label for="slider7"><span style="font-family: 'courier new', courier;">value=20 min=10, max=50 step=5</span>, ticks at 0, 10, 20, 30, 40 and 50: </label> <input id="slider7" oninput="printValue('slider7','rangeValue7')" min="10" max="50" step="5" list="ticks7" value="20" type="range">&nbsp;
<datalist id="ticks7">
<option>0</option> <option>10</option> <option>20</option> <option>30</option> <option>40</option> <option>50</option>
</datalist>
<output id="rangeValue7"></output></p>
<p><label for="slider8"><span style="font-family: 'courier new', courier;">value=5 min=0, max=10 step="0.5"</span>, ticks at 0, 0.5, 1, 2, 4, 8: </label> <input id="slider8" oninput="printValue('slider8','rangeValue8')" min="0" max="10" step="0.5" list="ticks8" value="5" type="range">&nbsp;
<datalist id="ticks8">
<option>0</option> <option>0.5</option> <option>1</option> <option>2</option> <option>4</option> <option>8</option> <option>10</option>
</datalist>
<output id="rangeValue8"></output></p>
<p><label for="slider9"><span style="font-family: 'courier new', courier;">value=5 min=0, max=10 step="any"</span>, ticks at 0, 5 and 10: </label> <input id="slider9" oninput="printValue('slider9','rangeValue9')" min="0" max="10" step="any" list="ticks9" value="0.5" type="range">&nbsp;
<datalist id="ticks9">
<option>0</option> <option>5</option> <option>10</option>
</datalist>
<output id="rangeValue9"></output></p>
</div>
 

#### External resources

+ You can use CSS for "standard" styling (size, color, background color, etc.) . However, some custom attributes are available. Check [this article from CSS tricks](https://css-tricks.com/styling-cross-browser-compatible-range-inputs-css/).
+ A script that automatically generates ticks, depending on the min, max and step attributes (Codepen from Dudley Storey): [Auto-Generated HTML5 range input Ticks](https://codepen.io/dudleystorey/pen/Klnzy)
+ From CSS{Portal}, a CSS generator help you style the html input range tag, very easy to use: [Style Input Range](https://www.cssportal.com/style-input-range/)
+ MDN's Web Docs: [`<input type=range>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range)


#### Knowledge check 5.4.6

1. How do you add "ticks" along a slider created with the `<input type=range>` element?

  a. Use the step attribute<br/>
  b. Use the datalist element<br/>
  c. Use only CSS<br/>

  Ans: b<br/>
  Explanation: It is possible to display "ticks" above the range slider, at given positions, using the `<datalist>` element. The course shows several examples of how to do this.


### 5.4.7 Discussion and projects

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

Let us suggest some topics of discussion and optional projects:


#### Suggested topics

+ Did you work out how to make stylish forms with CSS3? Please share any good resources about form styling and layout?


#### Optional projects

Here are a few project ideas. Your classmates and the team who prepared the course will be glad to try them and offer feedback. Please post URLs in this discussion forum. These projects are optional, meaning that they won't be graded.

+ __Project 1 (easy):__ add some sliders and a color chooser to control one of the projects you wrote for Week 3 and Week 4. Change the color, size, speed, rotation, etc. of your monster/chart/graphics. Make your demo a customizable Web app! Videos 1 and 2 are good starting points.
+ __Project 2 (easy):__ Provide an HTML5 form for registering in an imaginary forum. The form asks for a first name, a last name, an email, a phone number, a postal address, a password, etc. Please use as many features as possible, to put into action all the features described in this section of the course. If you form is long, regroup the different input elements into fieldsets. Look at the examples given in section 5.2.2, and in the live coding video #3. Have a look at external resources at the end of section 5.2.4 (put sections, headings, etc. in a long form).
+ __Project 3 (easy):__ make it stylish!
+ __Project 4 (a bit harder):__ Same as above, but please include a way to add a picture using an input=file element or the webcam + canvas. We will discuss in the forum how we can add the image to the data that the form will send once submitted.


