# Week 5: HTML5 Forms


## 5.5 Form attributes


### 5.5.0 Lecture Notes

+ [HTML5 form attributes](https://tinyurl.com/j7gv3y6)

  <table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 55vw;" cellspacing="0" cellpadding="5" border="1">
    <caption style="font-size: 1.5em; margin: 0.2em;"><a href="https://tinyurl.com/j7gv3y6">Attributes for the &lt;input&gt; element include global HTML attributes</a></caption>
    <thead>
    <tr style="font-size: 1.2em;">
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width: 5%;">Attribute</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:10%;">Type or Types</th>
      <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:30%;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefaccept">accept</a></td><td>file</td><td>Hint for expected file type in file upload controls</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefalt">alt</a></td><td>image</td><td>alt attribute for the image type. Required for accessibility</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefautocomplete"><strong style="color: cyan;">autocomplete</strong></a></td><td>all</td><td>Hint for form autofill feature</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefautofocus"><strong style="color: cyan;">autofocus</strong></a></td><td>all</td><td>Automatically focus the form control when the page is loaded</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefcapture">capture</a></td><td>file</td><td>Media capture input method in file upload controls</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefchecked">checked</a></td><td>radio, checkbox</td><td>Whether the command or control is checked</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefdirname">dirname</a></td><td>text, search</td><td>Name of form field to use for sending the element's directionality in form submission</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefdisabled">disabled</a></td><td>all</td><td>Whether the form control is disabled</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefform"><strong style="color: cyan;">form</strong></a></td><td>all</td><td>Associates the control with a form element</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformaction"><strong style="color: cyan;">formaction</strong></a></td><td>image, submit</td><td>URL to use for form submission</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformenctype"><strong style="color: cyan;">formenctype</strong></a></td><td>image, submit</td><td>Form data set encoding type to use for form submission</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformmethod"><strong style="color: cyan;">formmethod</strong></a></td><td>image, submit</td><td>HTTP method to use for form submission</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformnovalidate"><strong style="color: cyan;">formnovalidate</strong></a></td><td>image, submit</td><td>Bypass form control validation for form submission</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefformtarget"><strong style="color: cyan;">formtarget</strong> </a></td><td>image, submit</td><td>Browsing context for form submission</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefheight">height</a></td><td>image</td><td>Same as <code>height</code> attribute for <a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document."><code>&lt;img&gt;</code></a>; vertical dimension</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdeflist"><strong style="color: cyan;">list</strong></a></td><td>almost all</td><td>Value of the id attribute of the <a href="/en-US/docs/Web/HTML/Element/datalist" title="The HTML <datalist> element contains a set of <option> elements that represent the permissible or recommended options available to choose from within other controls."><code>&lt;datalist&gt;</code></a> of autocomplete options</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmax"><strong style="color: cyan;">max</strong></a></td><td>numeric types</td><td>Maximum value</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmaxlength">maxlength</a></td><td>password, search, tel, text, url</td><td>Maximum length (number of characters) of <code>value</code></td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmin"><strong style="color: cyan;">min</strong></a></td><td>numeric types</td><td>Minimum value</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefminlength">minlength</a></td><td>password, search, tel, text, url</td><td>Minimum length (number of characters) of <code>value</code></td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmultiple"><strong style="color: cyan;">multiple</strong></a></td><td>email, file</td><td>Boolean. Whether to allow multiple values</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefname">name</a></td><td>all</td><td>Name of the form control. Submitted with the form as part of a name/value pair.</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefpattern"><strong style="color: cyan;">pattern</strong></a></td><td>password, text, tel</td><td>Pattern the <code>value</code> must match to be valid</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefplaceholder"><strong style="color: cyan;">placeholder</strong></a></td><td>password, search, tel, text, url</td><td>Text that appears in the form control when it has no value set</td></tr>
    <tr><td><a href="/en-US/docs/Web/HTML/Attributes/readonly"><strong style="color: cyan;">readonly</strong></a></td><td>almost all</td><td>Boolean. The value is not editable</td></tr>
    <tr><td><a href="/en-US/docs/Web/HTML/Attributes/required"><strong style="color: cyan;">required</strong></a></td><td>almost all</td><td>Boolean. A value is required or must be check for the form to be submittable</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefsize">size</a></td><td>email, password, tel, text</td><td>Size of the control</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefsrc">src</a></td><td>image</td><td>Same as <code>src</code> attribute for <a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document."><code>&lt;img&gt;</code></a>; address of image resource</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefstep"><strong style="color: cyan;">step</strong></a></td><td>numeric types</td><td>Incremental values that are valid.</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdeftype">type</a></td><td>all</td><td>Type of form control</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefvalue">value</a></td><td>all</td><td>Current value of the form control. Submitted with the form as part of a name/value pair.</td></tr>
    <tr><td><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefwidth">width</a></td><td>image</td><td>Same as <code>width</code> attribute for <a href="/en-US/docs/Web/HTML/Element/img" title="The HTML <img> element embeds an image into the document."><code>&lt;img&gt;</code></a></td> </tr>
  </tbody>
  </table>

+ [form attribute](#552-form)
  + useful for putting input fields outside the form itself
  + useful when using `<fieldset>` elements for making the page/form layout easier
  + sharing the same value as the `id` of the form the field belongs to
  + Typical use:

    ```html
    <label for="yourName">Enter your name:</label>
    <input type="text" id="yourName" name="yourName" form="form1"/>
    <p>
    <form id="form1" action="sumit.php" method="post">
      <fieldset>
        <legend>Choose option</legend>
        <label for="free">Free registering</label>
        <input type="checkbox" id="free"/>
        <label for="premium">Premium</label>
        <input type="checkbox" id="premium"/>
        <button type="submit">Send form</button>
      </fieldset>
    </form>
    ```

+ [autocomplete attribute](#553-autocomplete)
  + apply either to the `<form>` element or on individual `<input>` elements
  + input fields autocompleting the user's input based on the user's typing history
  + possible values: `on`/`off`
  + applied to the `<form>` element
    + all input fields attached to the form (inside or linked to it using the form attribute)
    + auto-completion set by default to the value of the `autocomplete` attribute of the form
  + default behavior able to be overridden by setting it individually to any input field inside
  + autocomplete "on" for the form, and "off" for specific input fields, or vice-versa
  + disabled by default in some Web browsers $\to$ adjusted in the preferences/settings
  + target most input types
  + example: `<form submit="test.php" method="post" autocomplete="on">`

+ [autofocus attribute](#554-autofocus)
  + useful for transferring the focus to a field other than the first field in a page/form
  + default: the first input field w/ the focus
  + not more than one element in the document w/ the `autofocus` attribute specified
  + use of the `autofocus` attribute: put the focus on the second input field of the page
  + `required` attribute: make the input field invalid if kept empty
  + example: 

    ```html
    <form>
        ...
        <input type="text" id="test"/><p>
        ...
        <input id="name" name="inputName"
              placeholder="6 to 9 chars please..."
              pattern="\w{6,9}"
              required
              autofocus
              type="text"/>
        ...
    </form>
    ```

+ [Boolean attributes syntax](#note-about-boolean-attributes-syntax)
  + Boolean attributes: `autofocus`, `required`, `optional`, etc.
  + true value: presence of a Boolean attribute
  + false value: the absence of the attribute represent
  + able to either write `autofocus="autofocus"`, or just use the attribute name `"autofocus"` without setting a value

+ [list attribute](#555-list)
  + working together w/ the new `<datalist>` element
  + value matching the `id` of a `<datalist>` element
  + useful for providing local auto-completion to some input fields
  + restricting the possible values on some others like `<input type=date>` or `<input type=color>`
  + click inside the field or use the the drop down menu
  + entering any value: not start w/ one of these letters accepted but not trigger auto-completion
  + typical usage: the value of the `list` attribute of the `input` field must match the one of the `id` of the `<datalist>` element
  
    ```html
    <input list="browsers" id="mybrowser" />
    <datalist id="browsers">
       <option value="Internet Explorer">
       <option value="Firefox">
       <option value="Chrome">
       <option value="Opera">
       <option value="Safari">
    </datalist>
    ```
+ Reference: [Methods of regular expressions in JavaScript](https://tinyurl.com/y22np4b5)

+ [pattern attribute](#556-pattern)
  + enables the validation of the user's input on the fly (also at submission time)
  + based on regular expressions
  + apply to the `text`, `search`, `url`, `tel`, `email`, and `password` input types
  + ref: [Categories of HTML5 Pattern](http://html5pattern.com/)
  + a `pattern` attribute w/ a value: the JavaScript regular expression matching the entire string entered in the field
  + the empty string valid by default, except if the required attribute used
  + __best practice:__ systematically add a `title` attribute with a value that indicates what constitutes a valid entry
  + example: 3-letter country code

    ```html
    <label for="code">Please enter a 3 letter country code:</label>
    <input type="text" name="country_code"
            pattern="[A-Za-z]{3}"
            title="3 letter country code"
            id="code"/>
    ```

  + example: mixing several other attributes with the pattern attribute

    ```html
    <label for="inputID">Enter a pseudo (6-12 characters): </label> 
    <input id="inputID" name="Name" 
      placeholder="Name" 
      pattern="\w{6,12}"
      required
      title="6-12 characters allowed"
      type="text" />
    ```

  + example: `<input type="url">` element with a pattern attribute

    ```html
    <input
        id="website"
        name="url"
        type="url"
        placeholder="http://www.domain.com"
        title="http, https or ftp allowed"
        pattern="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*"
    />
    ```

+ [min, max, and step attributes](#557-min-max-and-step)
  + useful for several input types: `number`, `range`, `date` and `time`
  + `min` and `max` attributes: used to set ranges to input fields that accept numerical values or a date/time
  + example

    ```html
    <input id="mydate" name="mydate"
          type="date"
          min="2012-01-01"
          max="2013-01-01"
          value="2012-01-01"
    />
    
    <input name="time" id="time" type="time"
            min="09:00"
            max="17:00"
            value="12:00"
    />
    ```






### 5.5.1 Form attributes

In this chapter, we go over the form attributes that have been introduced by HTML5.

<table style="font-family: Arial,Helvetica,Sans-Serif; margin: 0 auto; width: 50vw;" cellspacing="0" cellpadding="5" border="1">
  <thead>
  <tr style="font-size: 1.2em;">
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">HTML4</th>
    <th style="text-align: center; background-color: #3d64ff; color: #ffffff; width:20%;">HTML5</th>
  </tr>
  </thead>
  <tbody style="font-family: 'courier new', courier;">
  <tr>
  <td>
  <ul class="column" style="padding-left: 0px; margin-top: 0px; margin-bottom: 10px; margin-left: 25px;">
  <li><strong>name</strong></li><li><strong><span style="color: #ff0000; font-family: 'courier new', courier;">disabled*</span></strong></li>
  <li><strong>type</strong></li><li><strong>maxlength</strong></li><li><strong>readonly</strong></li><li><strong>size</strong></li><li><strong>value</strong></li><li><strong>alt</strong></li><li><strong>src</strong></li><li><strong>height</strong></li><li><strong>width</strong></li>
  <li><strong><span style="color: #ff0000; font-family: 'courier new', courier;">checked*</span></strong></li>
  <li><strong><span style="color: #ff0000; font-family: 'courier new', courier;">align&nbsp;**</span></strong></li>
  </ul></td>
  <td>
  <ul class="column" style="padding-left: 0px; margin-top: 0px; margin-bottom: 10px; margin-left: 25px;">
  <li><strong>form</strong></li><li><strong>readonly</strong></li><li><strong>autocomplete</strong></li><li><strong>autofocus</strong></li><li><strong>list</strong></li><li><strong>pattern</strong></li><li><strong>required*</strong></li><li><strong>placeholder</strong></li><li><strong>multiple</strong></li><li><strong>list</strong></li><li><strong>min</strong></li><li><strong>max</strong></li><li><strong>step</strong></li><li><strong>formaction</strong></li><li><strong>formenctype</strong></li><li><strong>formmethod</strong></li><li><strong>formtarget</strong></li><li><strong>formnovalidate</strong></li>
  </ul></td>
  </tr>
  <tr>
  <td colspan="2"><p style="margin: 0px 0px 10px;"><span style="color: #ff0000;">* &nbsp; pseudoclasses CSS target with :disabled and :checked or&nbsp;:required&nbsp;selectors</span></p><p style="margin: 0px 0px 10px;"><span style="color: #ff0000;">** align is deprecated, CSS rules should be used instead</span></p></td>
  </tr>
  </tbody>
</table>

We have already seen the use of pseudo CSS classes used together with the input field and form validation (`pattern` attribute, `input:invalid` CSS rule). We also briefly looked at the use of the `placeholder` attributes for displaying a helper message in the input field.

In this section, we cover the rest of the form attributes and provide further examples of using the previously discussed attributes. 

In another part of the course, about form validation and visual feedback using CSS, we examine some of the most useful attributes in even greater detail.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 15vw;"
    onclick="window.open('https://tinyurl.com/y5eese3q')"
    src    ="https://tinyurl.com/yy3twz2j"
    alt    ="html5 form attributes"
    title  ="html5 form attributes"
  />
</figure>


### 5.5.2 form

This attribute is useful for putting input fields outside the form itself. The `form` attribute of an external input field must share the same value as the id of the form the field belongs to. This is useful when using `<fieldset>` elements for making the page/form layout easier.


#### Typical use

[Try this interactive example in CodePen](http://codepen.io/w3devcampus/pen/jmdpyv),  or try it directly in your browser: ([Local Example - form Attr.](src/5.2.2-example1.html))

<div class="exampleHTML"><label for="yourName">Enter your name (field outside the form):</label> <input id="yourName" name="yourName" form="form1" type="text"><form id="form1" action="sumit.php" method="post"><fieldset><legend>Choose option</legend> <label class="label" for="free">Free registering</label> <input id="free" type="checkbox"> <label class="label" for="premium">Premium</label> <input id="premium" type="checkbox"> <button type="submit">Send form</button></fieldset></form></div>

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"><span class="tag">&nbsp; </span></span><span class="tag"><span class="tag"><span class="tag">&nbsp; </span></span>&lt;title&gt;</span><span class="pln">Example of input type=tel</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag"><span class="tag">&nbsp; </span>&lt;/head&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;body&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"yourName"</span><span class="tag">&gt;</span><span class="pln">Enter your name:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"yourName"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"yourName"</span><span class="pln"> </span><span class="atn">form</span><span class="pun">=</span><span class="atv">"form1"</span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;form</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"form1"</span><span class="pln"> </span><span class="atn">action</span><span class="pun">=</span><span class="atv">"sumit.php"</span><span class="pln"> </span><span class="atn">method</span><span class="pun">=</span><span class="atv">"post"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;legend&gt;</span><span class="pln">Choose option</span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"free"</span><span class="tag">&gt;</span><span class="pln">Free registering</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"free"</span><span class="tag">/&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"premium"</span><span class="tag">&gt;</span><span class="pln">Premium</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"checkbox"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"premium"</span><span class="tag">/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"submit"</span><span class="tag">&gt;</span><span class="pln">Send form</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&nbsp; </span><span class="tag">&lt;/form&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&nbsp; </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/html&gt;</span></li>
</ol></div>

Lines 12 and 22 shows the form attribute. Make sure that its value matches the `id` of the form!


### 5.5.3 autocomplete

This attribute applies either to the `<form>` element or on individual `<input>` elements. It specifies when input fields must autocomplete the user's input based on the user's typing history. 

Possible values of this attribute: `on/off`.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 8vw;"
    onclick="window.open('https://tinyurl.com/yyhzm6ua')"
    src    ="https://tinyurl.com/y592awug"
    alt    ="on off funny picture"
    title  ="on off funny picture"
  />
</figure>


If applied to the `<form>` element, all input fields attached to the form (inside or linked to it using the form attribute), will have auto-completion set by default to the value of the `autocomplete` attribute of the form.

This default behavior can be overridden by setting it individually to any input field inside. In other words: it is possible to have autocomplete "on" for the form, and "off" for specific input fields, or vice-versa.

Sometimes this autocomplete behavior is disabled by default in some Web browsers, and will need to be adjusted in the preferences/settings. 

This attribute targets most input types (those that allow typing in them).


#### Typical use

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/yyhzm6ua')"
    src    ="https://tinyurl.com/y2jglzyr"
    alt    ="example of use of the autocomplete attribute"
    title  ="example of use of the autocomplete attribute"
  />
</figure>


Try it in your browser here:

<div class="exampleHTML"><form method="post" submit="test.php" autocomplete="on"><fieldset><legend>Examples of use of the <span style="font-family: 'courier new', courier;">autocomplete</span> attribute</legend> <label for="address">Enter your email (<span style="font-family: 'courier new', courier;">autocomplete=off</span>, this overrides the form's <span style="font-family: 'courier new', courier;">autocomplete=on</span> attribute):</label> <input id="address" autocomplete="off" type="email">
<p><label for="address1">Enter your address (<span style="font-family: 'courier new', courier;">autocomplete=on</span> by inheritance of the form's <span style="font-family: 'courier new', courier;">autocomplete=on</span> attribute):</label> <input id="address1" type="email"></p>
<p><button type="button">Submit</button></p>
</fieldset></form>
<p>To see auto-completion in action: enter something in both fields and submit the form. Then enter the same thing: you will see that only the second input field offers auto-completion.</p>
</div>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;form</span><span class="pln"> </span><span class="atn">submit</span><span class="pun">=</span><span class="atv">"test.php"</span><span class="pln"> </span><span class="atn">method</span><span class="pun">=</span><span class="atv">"post"</span><span class="pln"> </span><strong><span class="atn">autocomplete</span><span class="pun">=</span><span class="atv">"on"</span></strong><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"address"</span><span class="tag">&gt;</span><span class="pln">Enter your address (autocomplete off, <strong>overrides the </strong></span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>form's autocomplete=on attribute</strong>):</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"address"</span><span class="pln"> </span><strong><span class="atn">autocomplete</span><span class="pun">=</span><span class="atv">"off"</span></strong><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;p&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"address1"</span><span class="tag">&gt;</span><span class="pln">Enter your address (<strong>autocomplete on by inheritance</strong> of</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;the form's autocomplete=on attribute):</span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"address1"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;button</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"submit"</span><span class="tag">&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;<span style="color: #000088;" color="#000088">&nbsp; &nbsp;...</span></span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/form&gt;</span></li>
</ol></div>


#### Knowledge check 5.5.3

1. The `<autocomplete>` attribute of the `<form>` or of the `<input>` elements proposes auto-completions from a dataset provided by the Web developer (locally or from a remote server)? (True/False)

  Ans: False<br/>
  Explanation: This `<autocomplete>` attribute applies to the `<form>` element or on individual `<input>` elements. It specifies that input fields must try to autocomplete the user's input based on the user's typing history. The second answer, FALSE, is correct.


### 5.5.4 autofocus

This attribute is useful for transferring the focus to a field other than the first field in a page/form (by default the first input field has the focus).

_Attention_: there must not be more than one element in the document with the `autofocus` attribute specified!

This example below illustrates the use of the `autofocus` attribute: the focus is put on the second input field of the page. It also shows the use of `required`, `placeholder` and `pattern` attributes.

The `required` attribute makes the input field invalid if kept empty. 

Here is the result in your browser:

<div class="exampleHTML"><form><fieldset><legend>Example of use of the <span style="font-family: 'courier new', courier;">autofocus</span> attribute</legend> <label for="test">This is an input field:</label> <input id="test" type="text">
<p><label for="name">Enter at least 6 chars, max 9 chars (this field has the <span style="font-family: 'courier new', courier;">autofocus</span> attribute): </label> <input name="inputName" id="name" autofocus="" required="" placeholder="6 to 9 chars please..." pattern="\w{6,9}" type="text"></p></fieldset></form>
<p><strong>Notice that the focus in on the second input field, thanks to the <span style="font-family: 'courier new', courier;">autofocus</span>&nbsp;attribute.</strong></p>
</div>

Extract from source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;form&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"test"</span><span class="tag">/&gt;&lt;p&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ... </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"name"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"inputName"</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">placeholder</span><span class="pun">=</span><span class="atv">"6 to 9 chars please..."</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">pattern</span><span class="pun">=</span><span class="atv">"\w{6,9}"</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">required</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">autofocus</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/form&gt;</span></li>
</ol></div>


#### Note about Boolean attributes syntax

<p class="exampleHTML"><strong>Important: </strong>: <span style="color: #ff0000;">For "Boolean" attributes, such as <span style="font-family: 'courier new',courier;">autofocus</span>, <span style="font-family: 'courier new',courier;">required</span>, <span style="font-family: 'courier new',courier;">optional</span>, etc., you are able to either write <span style="font-family: 'courier new',courier;">autofocus="autofocus"</span>, or just use the attribute name "<span style="font-family: 'courier new',courier;">autofocus</span>" without setting a value. </span></p>

Read [these explanations](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attributes) for a complete description of the syntax of Boolean attributes.


#### Knowledge check 5.5.4

__Source code for the knowledge check 5.5.4__

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;&lt;meta charset="utf-8"&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example for a knowledge check</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;form&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"</span><span class="atv"><span class="atv">studentID</span>"</span><span class="tag">&gt;</span><span class="pln">Student ID (disabled field, cannot type in it): </span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"S134356"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"studentID"</span><span class="pln"> </span><span class="atn">disabled</span><span class="tag">/&gt;&lt;p&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"name"</span><span class="tag">&gt;</span><span class="pln">First name: </span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"firstName"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span><span class="atn">placeholder</span><span class="pun">=</span><span class="atv">"John"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">autofocus</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">/&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag"></span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"lastName"</span><span class="tag">&gt;</span><span class="pln">Last name: </span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"lastName"</span><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">placeholder</span><span class="pun">=</span><span class="atv">"Smith"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">autofocus</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;</span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/form&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


1. Help us fix the above form's source code. What are the errors in it? (2 correct answers.)

  a. The `disabled` attribute at line 9 does not exist in HTML.<br/>
  b. The value of the `for` attribute of the label at _line 11_ does not match the value of the `id` attribute of the input field at _line 12_.<br/>
  c. There are no errors in it.<br/>
  d. There are two input fields with an `autofocus` attribute, and this is not correct.<br/>
  e. _At line 9_, the value of the student ID cannot contain letters, this will make this field invalid.<br/>

  Ans: <span color="color: magenta;">bd</span>, xde<br/>
  Explanation: The `for` and `id` attributes must match between a label and its associated input field. And you should never have more than one input field with the `autofocus` attribute.



### 5.5.5 list

This attribute works together with the new `<datalist>` element we already studied when we saw the color and date input fields.

This attribute's value must match the id of a `<datalist>` element. __It is useful for providing local auto-completion to some input fields, or for restricting the possible values on some others like `<input type=date>` or `<input type=color>`.__

Here is a small code extract from a more complete example shown in the section about the new `<datalist>` element (see next unit).

Please try it in your  browser (Type "F", "E", "O", C" etc., or just click inside the field and use the drop down menu). Note that you can also enter any value; if it does not start with one of these letters it will be accepted but will not trigger auto-completion.

<div class="exampleHTML"><form><fieldset><legend>List attribute</legend> <label for="mybrowser">Preferred browser</label> <input id="mybrowser" list="browsers" type="text">
<datalist id="browsers">
<option value="Internet Explorer"></option>
<option value="Firefox"></option>
<option value="Chrome"></option>
<option value="Opera"></option>
<option value="Safari"></option>
</datalist>
<input value="Submit Query" type="submit"></fieldset></form></div>
 
Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="pln"> </span><span class="tag">&lt;form&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; ...</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; </span><span class="tag">&lt;input</span><span class="pln"> </span><strong><span class="atn">list</span><span class="pun">=</span><span class="atv">"browsers"</span></strong><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mybrowser"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &nbsp; &lt;datalist</span><span class="pln"> </span><strong><span class="atn">id</span><span class="pun">=</span><span class="atv">"browsers"</span></strong><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"Internet Explorer"</span><span class="tag">&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"Firefox"</span><span class="tag">&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"Chrome"</span><span class="tag">&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"Opera"</span><span class="tag">&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="tag">&lt;option</span><span class="pln"> </span><span class="atn">value</span><span class="pun">=</span><span class="atv">"Safari"</span><span class="tag">&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><span class="tag">&lt;/datalist&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">...</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/form&gt;</span></li>
</ol></div>

At _lines 3_ and _5_, the value of the `list` attribute of the input field must match the one of the id of the `<datalist>` element.


#### Knowledge check 5.5.5

1. The list attribute works together with?

  a. The `form` attribute<br/>
  b. The `datalist` element<br/>
  c. The `autocomplete` attribute<br/>

  Ans: b<br/>
  Explanation: The list attribute works together with the new `<datalist>` element. This attribute's value must match the id of a `<datalist>` element. It is useful for providing local auto-completion to some input fields, or for restricting the possible values on some others like `<input type=date>` or `<input type=color>`.


### 5.5.6 pattern

Cartoon from [xkcd #1171: Perl Problems](http://xkcd.com/1171/)

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2d7yy3d')"
    src    ="https://tinyurl.com/yxbq6fyd"
    alt    ="Comics stripe representing 2 figures standing facing each other. One is wearing sunglasses. First image: figure with sunglasses says 'If you're having Perl problems I feel bad for you, son'. Second image: figure with sunglasses says 'I got 99 problems'. Third image: figure with sunglasses says 'so I used regular expressions'. Final image: figure with sunglasses says 'Now I have 100 problems'."
    title  ="Comics stripe representing 2 figures standing facing each other. One is wearing sunglasses. First image: figure with sunglasses says 'If you're having Perl problems I feel bad for you, son'. Second image: figure with sunglasses says 'I got 99 problems'. Third image: figure with sunglasses says 'so I used regular expressions'. Final image: figure with sunglasses says 'Now I have 100 problems'."
  />
</figure>


The `pattern` attribute enables the validation of the user's input on the fly (also at submission time), based on __regular expressions__. It applies to the `text`, `search`, `url`, `tel`, `email`, and `password` input types. 

The `pattern` attribute follows the syntax of [JavaScript regular expressions](https://tinyurl.com/p6cw9hr).

A __must read:__ a good catalog of ready-to-go patterns is available at html5pattern.com, an excellent Web site that proposes plenty of JavaScript patterns for the `pattern` attribute of HTML5 forms. The left hand menu proposes categorized patterns for [postal codes](http://html5pattern.com/Postal_Codes), [dates](http://html5pattern.com/Dates), [phones](http://html5pattern.com/Phones), etc.

<p style="border: 1px solid red; margin: 20px; padding: 20px;"><span style="line-height: 1.6;">You can also try </span><a href="https://regex101.com/#javascript" target="_blank" style="line-height: 1.6;">this online JavaScript RegExps tester</a>, and follow <a href="https://regexone.com/" target="_blank">this tutorial about "using JavaScript RegExps"</a>&nbsp;that has step by step exercises and explanations.</p>


#### Typical use


<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y2d7yy3d')"
    src    ="https://tinyurl.com/y4x8nqud"
    alt    ="html5patterns.com screenshot that shows a menu on the left with categories and patterns on the right"
    title  ="html5patterns.com screenshot that shows a menu on the left with categories and patterns on the right"
  />
</figure>


Just add a `pattern` attribute with a value that is the JavaScript regular expression that must match the entire string entered in the field. Note that the empty string is valid by default (except if the `required` attribute is used - this makes empty fields invalid).

__It's best practice to systematically add a `title` attribute with a value that indicates what constitutes a valid entry.__ More on this in the section of this course dedicated to form validation.

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"country_code"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">pattern</span><span class="pun">=</span><span class="atv">"[A-Za-z]{3}"</span></strong><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">title</span><span class="pun">=</span><span class="atv">"3 letter country code"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">/&gt;</span></li>
</ol></div>


#### Examples

__Example #1__

Try this [online example at JSBin](https://jsbin.com/xeyuqux/1/edit?html,output) or directly in your browser below: ([Local Example - Country Code](src/5.5.6-example1.html))

<div class="exampleHTML"><label for="code">Please enter a 3 letter country code (green = valid, pink = invalid):</label> <input name="country_code" title="3 letter country code" id="code" pattern="[A-Za-z]{3}" type="text"></div>

With the previous example, until the value of the input field is equal to 3 alphabetic characters, the field is invalid.

As seen in the previous examples, we used some CSS pseudo classes for automatically setting the background-color of the input field as we type.

Complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;title&gt;</span><span class="pln">Example of the pattern attribute</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;style&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>input</strong></span><strong><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span></strong></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>background</strong></span><strong><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightPink</span><span class="pun">;</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="pun">}</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; <strong>input</strong></span><strong><span class="pun">:</span><span class="pln">valid </span><span class="pun">{</span></strong></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; <strong>background</strong></span><strong><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightGreen</span><span class="pun">;</span></strong></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp;&nbsp;</span><strong><span class="pun">}</span></strong></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/style&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp;</span><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"code"</span><span class="tag">&gt;</span><span class="pln">Please enter a 3 letter country code:</span><span class="tag">&lt;/label&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"country_code"</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">pattern</span><span class="pun">=</span><span class="atv">"[A-Za-z]{3}"</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">title</span><span class="pun">=</span><span class="atv">"3 letter country code"</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">id</span><span class="pun">=</span><span class="atv">"code"</span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


__Example #2: mixing several other attributes with the pattern attribute__

Try this [example online](https://jsbin.com/bozudeg/1/edit?html,output) or in your browser below: ([Local Example - Pattern Attr.](src/5.5.6-example2.html))

Attributes used: placeholder (for displaying a ghost example value), pattern, required (empty field = invalid)...

<div class="exampleHTML">
<p>Attributes used: <span style="font-family: 'courier new', courier;">placeholder</span> (for displaying a ghost example value), <span style="font-family: 'courier new', courier;">pattern</span>, <span style="font-family: 'courier new', courier;">required</span> (empty field = invalid)...</p>
<p><label for="inputID">Enter a pseudo (6-12 characters): </label> <input name="Name" id="inputID" required="" placeholder="Name" pattern="\w{6,12}" type="text"></p>
</div>

Complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html lang="en"&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;head&gt; &lt;meta charset="utf-8"&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;title&gt;</span><span class="pln">Example of use of new HTML5 input field attributes</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;style&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; input</span><span class="pun">:</span><span class="pln">focus</span><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightPink</span><span class="pun">;}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; input</span><span class="pun">:</span><span class="pln">valid </span><span class="pun">{</span><span class="pln"> background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln">lightGreen</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; input</span><span class="pun">:</span><span class="pln">required </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid red</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; input</span><span class="pun">:</span><span class="pln">optional </span><span class="pun">{</span><span class="pln">border</span><span class="pun">:</span><span class="pln"> </span><span class="lit">2px</span><span class="pln"> solid green</span><span class="pun">;</span><span class="pln"> </span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag">&nbsp; &lt;/style&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag">&lt;/head&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;body&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span><span class="pln">Attributes used: placeholder (for displaying a ghost example value), pattern, required (empty = invalid)...</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;p&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;label</span><span class="pln"> </span><span class="atn">for</span><span class="pun">=</span><span class="atv">"inputID"</span><span class="tag">&gt;</span><span class="pln">Enter a pseudo (6-12 characters): </span><span class="tag">&lt;/label&gt;</span><span class="pln"> </span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"inputID"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"Name"</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">placeholder</span><span class="pun">=</span><span class="atv">"Name"</span></strong><span class="pln"> </span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">pattern</span><span class="pun">=</span><span class="atv">"\w{6,12}"</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">required</span></strong></li>
<li class="L8" style="margin-bottom: 0px;"><strong><span class="atn">&nbsp; &nbsp; &nbsp; &nbsp;title="6-12 characters allowed please"</span></strong></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text"</span><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;/body&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
</ol></div>


__Example #3: an `<input type="url">` element with a pattern attribute allowing only certain protocols__

[Online example at JSBin](https://jsbin.com/nulahey/1/edit?html,output) or try it in your browser: ([Local Example - URL w/ Pattern](src/5.5.6-example3.html))

<div class="exampleHTML"><label for="website">Enter the URL of your repository (http, https or ftp): </label> <input name="url" id="website" placeholder="http://www.domain.com" pattern="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*" type="url"></div>

Source code extract:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;input</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; id</span><span class="pun">=</span><span class="atv">"website"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; name</span><span class="pun">=</span><span class="atv">"url"</span><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; type</span><span class="pun">=</span><span class="atv">"url"</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; placeholder</span><span class="pun">=</span><span class="atv">"http://www.domain.com"</span><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="atv">&nbsp; &nbsp; title="http, https or ftp allowed"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="atn">&nbsp; &nbsp; <strong>pattern</strong></span><strong><span class="pun">=</span><span class="atv">"(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*"</span></strong></li>
<li class="L5" style="margin-bottom: 0px;"><strong><span class="atv"></span></strong><span class="tag">/&gt;</span></li>
</ol></div>


#### Knowledge check 5.5.6

<pre>&lt;label for="name"&gt;Please enter value: &lt;/label&gt;
&lt;input type="text" id="name" pattern="[a-zA-Z0-9]+" required&gt;
</pre>

1. What kind of values are allowed in this input field (if you wish, get help by visiting the html5pattern.com Web site)?

  a. A lowercase char followed by an uppercase char followed by "0", followed by "-", followed by "9".<br/>
  b. Alphanumeric, no constraint on the length.<br/>
  c. A string between 0 and 9 characters long (lowercase or uppercase).<br/>

  Ans: b<br/>
  Explanation: The proposed regular expression means "any alphanumeric characters of length superior or equal to 1 char", in the JavaScript syntax for regular expressions. However, if the field did not have a required attribute, it would also be valid if left empty. That's why we added this attribute. The check against the regexp is done only when the field is not empty. This is one of the examples proposed for entering names, on the html5pattern.com Web site.  You can try it with this [JSBin](https://jsbin.com/lukele/edit?html,css,output).


### 5.5.7 min, max and step

These attributes are useful for several input types such as `number`, `range`, `date` and `time` (and other variants).

The `min` and `max` attributes are used to set ranges to input fields that accept numerical values or a date/time.

__Their detailed use with these input fields have already been explained in section 5.4 of this course dedicated to these particular input field types.__


#### Typical use

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"mydate"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"mydate"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">type</span><span class="pun">=</span><span class="atv">"date"</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; <strong>&nbsp;</strong></span><strong><span class="atn">min</span><span class="pun">=</span><span class="atv">"2012-01-01"</span></strong><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><strong><span class="atn">max</span><span class="pun">=</span><span class="atv">"2013-01-01"</span></strong><span class="pln"> </span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"2012-01-01"</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">/&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"> </span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"time"</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"time"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"time"</span><span class="pln"> </span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><strong><span class="atn">min</span><span class="pun">=</span><span class="atv">"09:00"</span></strong><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><strong><span class="atn">max</span><span class="pun">=</span><span class="atv">"17:00"</span></strong><span class="pln"> </span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span><span class="atn">value</span><span class="pun">=</span><span class="atv">"12:00"</span><span class="pln"> </span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">/&gt;</span><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"range"</span><span class="pln"> </span><strong><span class="atn">min</span><span class="pun">=</span><span class="atv">"0"</span><span class="pln"> </span><span class="atn">max</span><span class="pun">=</span><span class="atv">"100"</span><span class="pln"> </span><span class="atn">step</span><span class="pun">=</span><span class="atv">"5"</span></strong><span class="tag">/&gt;</span><span class="pln"> </span></li>
</ol></div>


### 5.5.8 multiple

The `multiple` attribute is used with `email` and `file` input types. It's a Boolean attribute, so here are the different syntax possibilities:

+ `<input type="email|file" multiple>`
+ `<input type="email|file" multiple="multiple">`
+ `<input type="email|file" multiple="">`



#### With `<input type="email">`

With the `<input type="email">`, this attribute enables the user to enter a set of addresses, separated by a comma instead of a single address. Entering several addresses will keep the input field valid.

[Online example at JSBin](https://jsbin.com/mexirif/1/edit?html,output) ([Local Example - Email](src/5.5.8-example1.html))

Or try it below in your browser: type in a list of email addresses separated by a comma, then look at the input field background color (pink = invalid, green = valid), and then submit:

<div class="exampleHTML">
<p>This form uses: <code>&lt;input type="email" name="myemail" <b>multiple</b>&gt;</code></p>
<form><fieldset><legend>With the mult<span style="font-family: 'courier new', courier;">i</span>ple attribute </legend> <label for="emailmultiple">Enter several email addresses: </label> <input id="myemail" name="myemail" title="you can enter multiple emails addresses, separated by a comma" multiple="multiple" type="email"> <button>Submit</button></fieldset></form>
<p></p>
<p>This form does not use the <span style="font-family: 'courier new', courier;">multiple</span> attribute:</p>
<form><fieldset><legend>Without the multiple attribute </legend> <label>Enter several email addresses: </label> <input id="myemail2" name="myemail" title="only one address please!" type="email"> <button>Submit</button></fieldset></form></div>


Complete source code:

<div class="source-code"><ol class="linenums">
<li class="L0" style="margin-bottom: 0px;" value="1"><span class="dec">&lt;!DOCTYPE html&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="tag">&lt;html</span><span class="pln"> </span><span class="atn">lang</span><span class="pun">=</span><span class="atv">"en"</span><span class="tag">&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag">&lt;head&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;meta</span><span class="pln"> </span><span class="atn">charset</span><span class="pun">=</span><span class="atv">"utf-8"</span><span class="tag">&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;title&gt;</span><span class="pln">Jsbin</span><span class="tag">&lt;/title&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>&lt;style&gt;</span><span class="pln"> </span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>input</span><span class="pun">:</span><span class="pln">invalid </span><span class="pun">{</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightPink</span><span class="pun">;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>input</span><span class="pun">:</span><span class="pln">valid </span><span class="pun">{</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>background</span><span class="pun">-</span><span class="pln">color</span><span class="pun">:</span><span class="pln"> lightGreen</span><span class="pun">;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>fieldset </span><span class="pun">{</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>border</span><span class="pun">:</span><span class="lit">1px</span><span class="pln"> solid</span><span class="pun">;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span><span class="pln"><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span></span>padding</span><span class="pun">:</span><span class="lit">20px</span><span class="pun">;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pun">}</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>&lt;/style&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/head&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span>&lt;body&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;p&gt;</span><span class="pln">This form uses: </span><span class="tag">&lt;code&gt;</span><span class="pln">&lt;input type="email" name="myemail" </span><span class="tag">&lt;b&gt;</span><span class="pln">multiple</span><span class="tag">&lt;/b&gt;</span><span class="pln">&amp;gt;</span><span class="tag">&lt;/code&gt;&lt;/p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>&lt;form&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;legend&gt;</span><span class="pln">With the multiple attribute </span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;label&gt;</span><span class="pln">Enter several email addresses: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"myemail"</span><span class="pln"> </span><span class="atn">title</span><span class="pun">=</span><span class="atv">"you can enter multiple emails addresses, separated by a comma"</span><span class="pln"> </span><span class="atn">multiple</span><span class="tag">/&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;button&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>&lt;/form&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag">&lt;p&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;p&gt;</span><span class="pln">This form does not use the multiple attribute:</span><span class="tag">&lt;/p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"> </span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span></span>&lt;form&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;fieldset&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;legend&gt;</span><span class="pln">Without the multiple attribute </span><span class="tag">&lt;/legend&gt;</span></li>
<li class="L6" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;label&gt;</span><span class="pln">Enter several email addresses: </span><span class="tag">&lt;/label&gt;</span></li>
<li class="L7" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;input</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"email"</span><span class="pln"> </span><span class="atn">name</span><span class="pun">=</span><span class="atv">"myemail"</span><span class="pln"> </span><span class="atn">title</span><span class="pun">=</span><span class="atv">"only one address please!"</span><span class="tag">/&gt;</span></li>
<li class="L8" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;button&gt;</span><span class="pln">Submit</span><span class="tag">&lt;/button&gt;</span></li>
<li class="L9" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;/fieldset&gt;</span></li>
<li class="L0" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span></span><span class="tag"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span></span>&lt;/form&gt;</span></li>
<li class="L1" style="margin-bottom: 0px;"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span><span class="tag">&lt;p&gt;</span></li>
<li class="L2" style="margin-bottom: 0px;"><span class="pln"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span></span><span class="pln"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span></span>Type in a list of email addresses separated by a comma. Look at the input field background color (pink = invalid, green = valid), try to submit. </span><span class="tag">&lt;/p&gt;</span></li>
<li class="L3" style="margin-bottom: 0px;"><span class="tag"><span class="pln">&nbsp;&nbsp; </span><span class="tag"></span><span class="tag"></span>&lt;/body&gt;</span></li>
<li class="L4" style="margin-bottom: 0px;"><span class="tag">&lt;/html&gt;</span></li>
<li class="L5" style="margin-bottom: 0px;"><span class="pln">&nbsp;</span></li>
</ol></div>
 
<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>Best&nbsp;practice: &nbsp;add a <span style="font-family: 'courier new', courier;">title</span> attribute indicating what you expect as a valid entry</strong> (<em>lines 25</em> and <em>38</em>). If you enter bad values and submit, you will see in the error message the string value of the <span style="font-family: 'courier new', courier;">title</span> attribute.</p>


#### With `<input type="file">`

With this type of input field, multiple files can be chosen (whereas before HTML5, only a single file could be chosen).

Typical use: `<input type=file multiple>`

Try these in your browser, look at the small variations (text in the buttons, messages):

<div class="exampleHTML">
<p>Example with <span style="font-family: courier new,courier;"><code>&lt;input type=file multiple&gt;</code></span></p>
<p><label for="multipleFiles">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Select one or more files: </label><input id="multipleFiles" multiple="multiple" type="file"></p>
<p></p>
<p>Example without the <span style="font-family: 'courier new', courier;">multiple</span> attribute:</p>
<p><label for="singleFile">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Select only one file: </label><input id="singleFile" type="file"></p>
</div>

Use the standard key modifiers (shift, control, command) for selecting multiple files when the file chooser dialog popup.


#### Knowledge check 5.5.8

1. The multiple attribute can be used with several input types. Which ones? (2 correct answers.)

  a. email<br/>
  b. tel<br/>
  c. file<br/>
  d. number<br/>
  e. color<br/>

  Ans: 




