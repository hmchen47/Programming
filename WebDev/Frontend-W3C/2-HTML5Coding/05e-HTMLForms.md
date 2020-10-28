# Week 5: HTML5 Forms


## 5.5 Form attributes


### 5.5.0 Lecture Notes

+ [HTML5 form attributes](https://tinyurl.com/j7gv3y6)

+ [form element](#552-form)
  + useful for putting input fields outside the form itself
  + useful when using `<fieldset>` elements for making the page/form layout easier 
  + sharing the same value as the `id` of the form the field belongs to
  + typical use:

    ```html
    <label for="yourName">Enter your name:</label>
    <input type="text" id="yourName" name="yourName" form="form1"/>

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
  + input fields auto-completing the user's input based on the user's typing history
  + possible values: `on`/`off`
  + applied to the `<form>` element
    + all input fields attached to the form (inside or linked to it using the form attribute)
    + auto-completion set by default to the value of the `autocomplete` attribute of the form
  + default behavior able to be overridden by setting it individually to any input field inside
  + auto-complete "on" for the form, and "off" for specific input fields, or vice-versa
  + disabled by default in some Web browsers $\to$ adjusted in the preferences/settings
  + target most input types
  + example: `<form submit="test.php" method="post" autocomplete="on">`

+ [autofocus attribute](#554-autofocus)
  + useful for transferring the focus to a field other than the first field in a page/form
  + default: the first input field w/ the focus
  + no more than one element in the document w/ the `autofocus` attribute specified
  + use of the `autofocus` attribute: put the focus on the specific input field of the page
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

+ [pattern attribute](#556-pattern)
  + enables the validation of the user's input on the fly (also at submission time)
  + based on regular expressions
  + apply to the `text`, `search`, `url`, `tel`, `email`  and `password` input types
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

+ [multiple attribute](#558-multiple)
  + used with email and file input types
  + a Boolean attribute
  + different syntax possibilities
    + `<input type="email|file" multiple>`
    + `<input type="email|file" multiple="multiple">`
    + `<input type="email|file" multiple="">`
  + typical usage w/ email: `<input type="email" name="myemail" title="you can enter multiple emails addresses, separated by a comma" multiple>`
    + enabling the user to enter a set of addresses
    + separated by a comma instead of a single address to enter several addresses keep the input field valid
  + __best practice__: add a `title` attribute indicating what you expect as a valid entry
  + typical usage w/ file: `<input type=file multiple>`
    + able to choose multiple files
    + w/o the multiple attribute, select only one file
    + using the standard key modifiers (shift, control, command) for selecting multiple files

+ [formaction and formmethod attributes](#5510-formaction-and-formmethod)
  + targeted to the `<input type="submit">` input fields
  + rarely used
  + typical usage: `<input type="submit" formaction="preview.php" formmethod="get" value="Preview">`
  + `formaction` attribute:
    + the action attribute value of the form overridden
    + form submitted to the URL / value of the `<input type="submit">` field
  + `formmethod` attribute
    + the same with the `POST/GET method` attribute of the form
    + override the value of the `method` attribute of the form
    + e.g., `<input type="submit" formaction="preview.php" formmethod="get" value="Preview">`
  + example: submit to the default URL:

    ```html
    <form action="defaultAction.php">
      <label for="givenName">Given name:</label> 
      <input type="text" name="givenName" id="givenName"><br>
      <label for="familyName">Family name:</label> 
      <input type="text" name="familyName" id="familyName"><br>
      <input type="submit" value="Submit"><br>
      <input type="submit" formaction="otherAction.php" value="Submit to another URL than default">
    </form>
    ```

+ [formnovalidate attribute](#5511-formnovalidate)
  + targeted to the `<input type="submit">` input fields
  + rarely used
  + allowing the submission of a form even if it contains invalid fields
  + example: not filled $\to$ a form w/ `<input type="email">` field or a field `required`
  + forms w/ two submit buttons: one w/ the `formnovalidate` attribute set to a non null value and one w/o
  + example:

    ```html
    <input type="submit"
          formnovalidate 
          value="Submit without validation" />
    ```

+ [formtarget attribute](#5512-formtarget)
  + targeted to the `<input type="submit">` input fields
  + possible values:
    + `_blank`: the response displayed in a new window or tab
    + `_self`: the response displayed in the same frame (this is default)
    + `_parent`: the response displayed in the parent frame
    + `_top`: the response displayed in the full body of the window
    + `framename`: the response displayed in a named iframe 
  + rarely used
  + value indicating where the response from the form submission should be displayed
  + typical usage:

    ```html
    <input type="submit" formtarget="_blank"
        value="Submit but show results in a new window/tab">
    ```

+ [formenctype attribute](#5513-formenctype)
  + the `enctype` attribute of the `<form>` element
  + form data set encoding type to use for form submission
  + used together with forms containing file input fields
  + using `"multipart"` forms for sending files to a remote server
  + example: `<form action="default.php" method="post" enctype="multipart/form-data">`
  + an attribute of the `<input type="submit" enctype=...>` element
  + when submitted using `method=POST`, the browser will send the form content encoded with the method specified by the `formenctype` attribute
  + overriding the value of the `enctype` attribute specified in the `<form enctype=...>` element
  + typical usage: `<input type="submit" formenctype="multipart/form-data" value="Submit as Multipart/form-data">`
  + possible values
    + `application/x-www-form-urlencoded`: all characters escaped/encoded before submission
    + `multipart/form-data`: encoding not done, using this value for submitting binary data such as images, files, etc.
    + `text/plain`: encoding done on standard characters like space


+ Reference: [Methods of regular expressions in JavaScript](https://tinyurl.com/y22np4b5)



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
  <ul style="padding-left: 0px; margin-top: 0px; margin-bottom: 10px; margin-left: 25px;">
  <li><strong>name</strong></li><li><strong><span style="color: #ff0000; font-family: 'courier new', courier;">disabled*</span></strong></li>
  <li><strong>type</strong></li><li><strong>maxlength</strong></li><li><strong>readonly</strong></li><li><strong>size</strong></li><li><strong>value</strong></li><li><strong>alt</strong></li><li><strong>src</strong></li><li><strong>height</strong></li><li><strong>width</strong></li>
  <li><strong><span style="color: #ff0000; font-family: 'courier new', courier;">checked*</span></strong></li>
  <li><strong><span style="color: #ff0000; font-family: 'courier new', courier;">align&nbsp;**</span></strong></li>
  </ul></td>
  <td>
  <ul style="padding-left: 0px; margin-top: 0px; margin-bottom: 10px; margin-left: 25px;">
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

<div><label for="yourName">Enter your name (field outside the form):</label> <input id="yourName" name="yourName" form="form1" type="text"><form id="form1" action="sumit.php" method="post"><fieldset><legend>Choose option</legend> <label for="free">Free registering</label> <input id="free" type="checkbox"> <label for="premium">Premium</label> <input id="premium" type="checkbox"> <button type="submit">Send form</button></fieldset></form></div>

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp; &nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp; &lt;title&gt;Example of input type=tel&lt;/title&gt;</li>
<li>&nbsp;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp; &nbsp; &lt;label for="yourName"&gt;Enter your name:&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &lt;input type="text" id="yourName" name="yourName" form="form1"/&gt;</li>
<li>&nbsp; &nbsp; &lt;p&gt;</li>
<li>&nbsp; &nbsp; &lt;form id="form1" action="sumit.php" method="post"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;fieldset&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;legend&gt;Choose option&lt;/legend&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;label for="free"&gt;Free registering&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;input type="checkbox" id="free"/&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;label for="premium"&gt;Premium&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;input type="checkbox" id="premium"/&gt;</li>
<li> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &lt;button type="submit"&gt;Send form&lt;/button&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;/fieldset&gt;</li>
<li>&nbsp; &nbsp; &lt;/form&gt;</li>
<li>&nbsp; &lt;/body&gt;</li>
<li> &lt;/html&gt;</li>
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

<div><form method="post" submit="test.php" autocomplete="on"><fieldset><legend>Examples of use of the <span style="font-family: 'courier new', courier;">autocomplete</span> attribute</legend> <label for="address">Enter your email (<span style="font-family: 'courier new', courier;">autocomplete=off</span>, this overrides the form's <span style="font-family: 'courier new', courier;">autocomplete=on</span> attribute):</label> <input id="address" autocomplete="off" type="email">
<p><label for="address1">Enter your address (<span style="font-family: 'courier new', courier;">autocomplete=on</span> by inheritance of the form's <span style="font-family: 'courier new', courier;">autocomplete=on</span> attribute):</label> <input id="address1" type="email"></p>
<p><button type="button">Submit</button></p>
</fieldset></form>
<p>To see auto-completion in action: enter something in both fields and submit the form. Then enter the same thing: you will see that only the second input field offers auto-completion.</p>
</div>

Source code extract:

<div><ol>
<li value="1"> &lt;form submit="test.php" method="post" <strong>autocomplete="on"</strong>&gt;</li>
<li>&nbsp; &nbsp;&nbsp;...</li>
<li>&nbsp; &nbsp;&nbsp;&lt;label for="address"&gt;Enter your address (autocomplete off, <strong>overrides the </strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>form's autocomplete=on attribute</strong>):&lt;/label&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;input type="text" id="address" <strong>autocomplete="off"</strong>&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;p&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;label for="address1"&gt;Enter your address (<strong>autocomplete on by inheritance</strong> of</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;the form's autocomplete=on attribute):&lt;/label&gt; </li>
<li>&nbsp; &nbsp;&nbsp;&lt;input type="text" id="address1"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;p&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;button type="submit"&gt;Submit&lt;/button&gt;</li>
<li>&nbsp;<span style="color: #000088;" color="#000088">&nbsp; &nbsp;...</span></li>
<li> &lt;/form&gt;</li>
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

<div><form><fieldset><legend>Example of use of the <span style="font-family: 'courier new', courier;">autofocus</span> attribute</legend> <label for="test">This is an input field:</label> <input id="test" type="text">
<p><label for="name">Enter at least 6 chars, max 9 chars (this field has the <span style="font-family: 'courier new', courier;">autofocus</span> attribute): </label> <input name="inputName" id="name" autofocus="" required="" placeholder="6 to 9 chars please..." pattern="\w{6,9}" type="text"></p></fieldset></form>
<p><strong>Notice that the focus in on the second input field, thanks to the <span style="font-family: 'courier new', courier;">autofocus</span>&nbsp;attribute.</strong></p>
</div>

Extract from source code:

<div><ol>
<li value="1"> &lt;form&gt;</li>
<li>&nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp;&nbsp;&lt;input type="text" id="test"/&gt;&lt;p&gt;</li>
<li>&nbsp; &nbsp; ... </li>
<li>&nbsp; &nbsp;&nbsp;&lt;input id="name" name="inputName" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;placeholder="6 to 9 chars please..." </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;pattern="\w{6,9}" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;required</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>autofocus</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;type="text"/&gt;</li>
<li>&nbsp; &nbsp; ...</li>
<li> &lt;/form&gt;</li>
</ol></div>


#### Note about Boolean attributes syntax

<p><strong>Important: </strong>: <span style="color: #ff0000;">For "Boolean" attributes, such as <span style="font-family: 'courier new',courier;">autofocus</span>, <span style="font-family: 'courier new',courier;">required</span>, <span style="font-family: 'courier new',courier;">optional</span>, etc., you are able to either write <span style="font-family: 'courier new',courier;">autofocus="autofocus"</span>, or just use the attribute name "<span style="font-family: 'courier new',courier;">autofocus</span>" without setting a value. </span></p>

Read [these explanations](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attributes) for a complete description of the syntax of Boolean attributes.


#### Knowledge check 5.5.4

__Source code for the knowledge check 5.5.4__

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt; </li>
<li>&lt;html lang="en"&gt; </li>
<li>&lt;head&gt;&lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Example for a knowledge check&lt;/title&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li> &lt;form&gt;</li>
<li>&nbsp; &nbsp;&lt;label for="studentID"&gt;Student ID (disabled field, cannot type in it): &lt;/label&gt; </li>
<li>&nbsp; &nbsp;&lt;input type="text" value="S134356" id="studentID" disabled/&gt;&lt;p&gt;</li>
<li> </li>
<li>&nbsp; &nbsp;&lt;label for="name"&gt;First name: &lt;/label&gt; </li>
<li>&nbsp; &nbsp;&lt;input type="text" id="firstName" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; placeholder="John" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;autofocus</li>
<li>&nbsp; &nbsp;/&gt;</li>
<li></li>
<li>&nbsp; &nbsp;&lt;label for="lastName"&gt;Last name: &lt;/label&gt; </li>
<li>&nbsp; &nbsp;&lt;input type="text" id="lastName" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;placeholder="Smith" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;autofocus</li>
<li>&nbsp; &nbsp;/&gt;</li>
<li> &lt;/form&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
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

<div><form><fieldset><legend>List attribute</legend> <label for="mybrowser">Preferred browser</label> <input id="mybrowser" list="browsers" type="text">
<datalist id="browsers">
<option value="Internet Explorer"></option>
<option value="Firefox"></option>
<option value="Chrome"></option>
<option value="Opera"></option>
<option value="Safari"></option>
</datalist>
<input value="Submit Query" type="submit"></fieldset></form></div>
 
Source code extract:

<div><ol>
<li value="1"> &lt;form&gt;</li>
<li>&nbsp; &nbsp; ...</li>
<li>&nbsp; &nbsp; &lt;input <strong>list="browsers"</strong> id="mybrowser" /&gt;</li>
<li> </li>
<li>&nbsp; &nbsp; &lt;datalist <strong>id="browsers"</strong>&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Internet Explorer"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Firefox"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Chrome"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Opera"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&lt;option value="Safari"&gt;</li>
<li>&nbsp; &nbsp;&nbsp;&lt;/datalist&gt;</li>
<li>...</li>
<li>&lt;/form&gt;</li>
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

<div><ol>
<li value="1">&lt;input type="text" name="country_code" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>pattern="[A-Za-z]{3}"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;title="3 letter country code" </li>
<li>/&gt;</li>
</ol></div>


#### Examples

__Example #1__

Try this [online example at JSBin](https://jsbin.com/xeyuqux/1/edit?html,output) or directly in your browser below: ([Local Example - Country Code](src/5.5.6-example1.html))

<div><label for="code">Please enter a 3 letter country code (green = valid, pink = invalid):</label> <input name="country_code" title="3 letter country code" id="code" pattern="[A-Za-z]{3}" type="text"></div>

With the previous example, until the value of the input field is equal to 3 alphabetic characters, the field is invalid.

As seen in the previous examples, we used some CSS pseudo classes for automatically setting the background-color of the input field as we type.

Complete source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt;</li>
<li> &lt;meta charset="utf-8"&gt;</li>
<li> &lt;title&gt;Example of the pattern attribute&lt;/title&gt;</li>
<li> &lt;style&gt;</li>
<li>&nbsp; &nbsp; <strong>input</strong><strong>:invalid {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>background</strong><strong>-color: lightPink;</strong></li>
<li>&nbsp; &nbsp;&nbsp;<strong>}</strong></li>
<li>&nbsp; &nbsp; <strong>input</strong><strong>:valid {</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; <strong>background</strong><strong>-color: lightGreen;</strong></li>
<li>&nbsp; &nbsp;&nbsp;<strong>}</strong></li>
<li> &lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&nbsp;&nbsp;&lt;label for="code"&gt;Please enter a 3 letter country code:&lt;/label&gt;</li>
<li>&nbsp; &lt;input type="text" name="country_code"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>pattern="[A-Za-z]{3}"</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;title="3 letter country code"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;id="code"/&gt;</li>
<li>&lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


__Example #2: mixing several other attributes with the pattern attribute__

Try this [example online](https://jsbin.com/bozudeg/1/edit?html,output) or in your browser below: ([Local Example - Pattern Attr.](src/5.5.6-example2.html))

Attributes used: placeholder (for displaying a ghost example value), pattern, required (empty field = invalid)...

<div>
<p>Attributes used: <span style="font-family: 'courier new', courier;">placeholder</span> (for displaying a ghost example value), <span style="font-family: 'courier new', courier;">pattern</span>, <span style="font-family: 'courier new', courier;">required</span> (empty field = invalid)...</p>
<p><label for="inputID">Enter a pseudo (6-12 characters): </label> <input name="Name" id="inputID" required="" placeholder="Name" pattern="\w{6,12}" type="text"></p>
</div>

Complete source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&lt;head&gt; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &lt;title&gt;Example of use of new HTML5 input field attributes&lt;/title&gt;</li>
<li>&nbsp; &lt;style&gt; </li>
<li>&nbsp; &nbsp; &nbsp; input:focus:invalid { background-color: lightPink;}</li>
<li>&nbsp; &nbsp; &nbsp; input:valid { background-color:lightGreen; }</li>
<li>&nbsp; &nbsp; &nbsp; input:required {border: 2px solid red; }</li>
<li>&nbsp; &nbsp; &nbsp; input:optional {border: 2px solid green; }</li>
<li>&nbsp; &lt;/style&gt;</li>
<li>&lt;/head&gt;</li>
<li>&lt;body&gt;</li>
<li>&lt;p&gt;Attributes used: placeholder (for displaying a ghost example value), pattern, required (empty = invalid)...</li>
<li>&lt;p&gt;</li>
<li>&lt;label for="inputID"&gt;Enter a pseudo (6-12 characters): &lt;/label&gt; </li>
<li>&lt;input id="inputID" name="Name" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>placeholder="Name"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>pattern="\w{6,12}"</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>required</strong></li>
<li><strong>&nbsp; &nbsp; &nbsp; &nbsp;title="6-12 characters allowed please"</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;type="text" /&gt;</li>
<li> &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


__Example #3: an `<input type="url">` element with a pattern attribute allowing only certain protocols__

[Online example at JSBin](https://jsbin.com/nulahey/1/edit?html,output) or try it in your browser: ([Local Example - URL w/ Pattern](src/5.5.6-example3.html))

<div><label for="website">Enter the URL of your repository (http, https or ftp): </label> <input name="url" id="website" placeholder="http://www.domain.com" pattern="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*" type="url"></div>

Source code extract:

<div><ol>
<li value="1">&lt;input </li>
<li>&nbsp; &nbsp; id="website" </li>
<li>&nbsp; &nbsp; name="url" </li>
<li>&nbsp; &nbsp; type="url"</li>
<li>&nbsp; &nbsp; placeholder="http://www.domain.com" </li>
<li>&nbsp; &nbsp; title="http, https or ftp allowed"</li>
<li>&nbsp; &nbsp; <strong>pattern</strong><strong>="(http|https|ftp)\:\/\/[a-zA-Z0-9\-\.\/]*"</strong></li>
<li><strong></strong>/&gt;</li>
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

<div><ol>
<li value="1">&lt;input id="mydate" name="mydate" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;type="date" </li>
<li>&nbsp; &nbsp; &nbsp; <strong>&nbsp;</strong><strong>min="2012-01-01"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>max="2013-01-01"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;value="2012-01-01"</li>
<li> /&gt;</li>
<li>&nbsp;</li>
<li> &lt;input name="time" id="time" type="time" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>min="09:00"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>max="17:00"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;value="12:00" </li>
<li>/&gt; </li>
<li>&nbsp;</li>
<li>&lt;input id="range" name="range" type="range" <strong>min="0" max="100" step="5"</strong>/&gt; </li>
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

<div>
<p>This form uses: <code>&lt;input type="email" name="myemail" <b>multiple</b>&gt;</code></p>
<form><fieldset><legend>With the mult<span style="font-family: 'courier new', courier;">i</span>ple attribute </legend> <label for="emailmultiple">Enter several email addresses: </label> <input id="myemail" name="myemail" title="you can enter multiple emails addresses, separated by a comma" multiple="multiple" type="email"> <button>Submit</button></fieldset></form>
<p></p>
<p>This form does not use the <span style="font-family: 'courier new', courier;">multiple</span> attribute:</p>
<form><fieldset><legend>Without the multiple attribute </legend> <label>Enter several email addresses: </label> <input id="myemail2" name="myemail" title="only one address please!" type="email"> <button>Submit</button></fieldset></form></div>


Complete source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp;&nbsp; &lt;head&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;title&gt;Jsbin&lt;/title&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;style&gt; </li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; input:invalid {</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; background-color: lightPink;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; input:valid {</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; background-color: lightGreen;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; fieldset {</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; border:1px solid;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; padding:20px;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; }</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;/style&gt;</li>
<li>&nbsp;&nbsp; &lt;/head&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &lt;body&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;p&gt;This form uses: &lt;code&gt;&lt;input type="email" name="myemail" &lt;b&gt;multiple&lt;/b&gt;&amp;gt;&lt;/code&gt;&lt;/p&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;form&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;fieldset&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;legend&gt;With the multiple attribute &lt;/legend&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;label&gt;Enter several email addresses: &lt;/label&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;input type="email" name="myemail" title="you can enter multiple emails addresses, separated by a comma" multiple/&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;button&gt;Submit&lt;/button&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/fieldset&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;/form&gt;</li>
<li>&nbsp;&nbsp; &lt;p&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;p&gt;This form does not use the multiple attribute:&lt;/p&gt;</li>
<li> </li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;form&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;fieldset&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;legend&gt;Without the multiple attribute &lt;/legend&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;label&gt;Enter several email addresses: &lt;/label&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;input type="email" name="myemail" title="only one address please!"/&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;button&gt;Submit&lt;/button&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &lt;/fieldset&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; &lt;/form&gt;</li>
<li>&nbsp;&nbsp; &lt;p&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&nbsp; Type in a list of email addresses separated by a comma. Look at the input field background color (pink = invalid, green = valid), try to submit. &lt;/p&gt;</li>
<li>&nbsp;&nbsp; &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
<li>&nbsp;</li>
</ol></div>
 
<p style="border: 1px solid red; margin: 20px; padding: 20px;"><strong>Best&nbsp;practice: &nbsp;add a <span style="font-family: 'courier new', courier;">title</span> attribute indicating what you expect as a valid entry</strong> (<em>lines 25</em> and <em>38</em>). If you enter bad values and submit, you will see in the error message the string value of the <span style="font-family: 'courier new', courier;">title</span> attribute.</p>


#### With `<input type="file">`

With this type of input field, multiple files can be chosen (whereas before HTML5, only a single file could be chosen).

Typical use: `<input type=file multiple>`

Try these in your browser, look at the small variations (text in the buttons, messages):

<div>
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

  Ans: ac<br/>
  Explanation; The multiple attribute can be used with email and file input types.


### 5.5.9 A warning

In the following pages, we present a set of rarely used attributes introduced by HTML5. There will be no questions about them in the exercises at the end of the week.

You might just glance at them and/or try the examples. The next pages cover their usage and you are welcome to use them for future reference (for those of you who like to cover the topics completely).


### 5.5.10 formaction and formmethod

These attributes are targeted to the `<input type="submit">` input fields. They are rarely used, so no questions about them will be asked in the quizzes of Week 5.

<div><ol>
<li value="1">&lt;input type="submit"</li>
<li> formaction="preview.php" formmethod="get" value="Preview"&gt;</li>
</ol></div>

When you use an `<input type="submit">` field with the formaction attribute, the action attribute value of the form is overridden. The form will be submitted to the URL / value of the formaction attribute of the  `<input type="submit">` field.

The formmethod attribute does the same with the POST/GET method attribute of the form. If an `<input type="submit">` has a formmethod attribute, it overrides the value of the method attribute of the form.


#### Typical use

<div><ol>
<li value="1"> &lt;form action="post.php" method="post"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="submit" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<strong>formaction="preview.php" formmethod="get"</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;value="Preview"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="submit" value="Send"&gt; </li>
<li>&lt;/form&gt;</li>
</ol></div>

Line 3 overrides the values set in line 1. 


#### Examples

Here are two online examples at JSBin:

+ [Example 1](https://jsbin.com/tequkak/2/edit?html,output) ([Local Example - URL submit](src/5.5.10-example1.html))
+ [Example 2](https://jsbin.com/tequkak/2/edit?html,output) ([Local Example - POST/GET submit](src/5.5.10-example2.html))

The first shows a form with two submit buttons: 

+ the first button submits to the default URL specified by the `action` attribute of the form,
+ the second button submits to another action specified by its `formaction` attribute.

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y348w7rn')"
    src    ="https://tinyurl.com/y45jkfoh"
    alt    ="example of use of formaction attribute"
    title  ="example of use of formaction attribute"
  />
</figure>


The second example shows a form with two submit buttons:

+ the first button submits using a GET,
+ the second button using a POST:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y348w7rn')"
    src    ="https://tinyurl.com/yxca5b7r"
    alt    ="example of use of the formmethod attribute"
    title  ="example of use of the formmethod attribute"
  />
</figure>


### 5.5.11 formnovalidate

The `formnovalidate` attribute is targeted to the `<input type="submit">` input fields. This attribute is rarely used, so there will be no questions about it in the end of the week's exercises.

This atrribute allows the submission of a form even if it contains _invalid_ fields. For example: a form that has an `<input type="email">` field or a field `required` and which are not filled. 

In general, such forms have two submit buttons, one with the `formnovalidate` attribute set to a non null value and one without.

Typical use ([online example at JSBin](https://jsbin.com/doceje/1/edit?html,output)): ([Local Example - formnovalidate](src/5.5.11-example1.html))

<div><ol>
<li value="1">&lt;form action="form.php"&gt;</li>
<li>&nbsp; &nbsp;&lt;fieldset&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;legend&gt;Example of formnovalidate attribute&lt;/legend&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;label for="email"&gt;E-mail:&lt;/label&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="email" name="email" id="email"/&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="submit" value="Submit" /&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp;<strong>&lt;input type="submit"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>formnovalidate</strong>&nbsp;</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>value</strong><strong>="Submit without validation" /&gt;</strong></li>
<li> &lt;/fieldset&gt;</li>
<li>&lt;/form&gt;</li>
</ol></div>

Try this code it in your browser:

<div>
<p>Enter a bad email address, then submit -&nbsp;you should see an error message. Using the other submit button will submit the form anyway.</p>
<form action="form.php"><fieldset><legend>Example of <span style="font-family: 'courier new', courier;">formnovalidate</span> attribute</legend> <label for="email">E-mail:</label> <input name="email" id="email" type="email"><br> <input value="Submit" type="submit"><br> <input formnovalidate="formnovalidate" value="Submit without validation" type="submit"></fieldset></form></div>
 
 
### 5.5.12 formtarget

The formtarget attribute is targeted to the `<input type="submit">` input fields. This attribute is rarely used, so there will be no questions about it in the exercises - Week 5.

This attribute's value indicates where the response from the form submission should be displayed.


#### Typical use

<div><ol>
<li value="1">&lt;input type="submit"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;<strong>formtarget="_blank"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp;value="Submit but show results in a new window/tab"&gt;</li>
</ol></div>

Possible values for the `formtarget` attributes are:

+ `_blank`: the response is displayed in a new window or tab
+ `_self`: the response is displayed in the same frame (this is default)
+ `_parent`: the response is displayed in the parent frame
+ `_top`: the response is displayed in the full body of the window
+ `framename`: the response is displayed in a named iframe


#### Complete example

[Online example at JSBin](https://jsbin.com/godice/2/edit?html,output) or try it in your browser below: ([Local Example - formtarget](src/5.5.12-example1.html))


<div><form action="getAction.php" method="get">Given name: <input name="givenName" type="text"><br> Family name: <input name="familyName" type="text"><br> <input value="Submit as usual" type="submit"> <input formtarget="_blank" value="Submit but show results in a new window/tab" type="submit"></form></div>
 
Source code:

<div><ol>
<li value="1">&lt;form action="defaultAction.php"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;label for="givenName"&gt;Given name:&lt;/label&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="text" name="givenName" id="givenName"&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;label for="familyName"&gt;Family name:&lt;/label&gt; </li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="text" name="familyName" id="familyName"&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="submit" value="Submit as usual"&gt;</li>
<li>&nbsp; &nbsp; &nbsp;&lt;input type="submit" </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>formtarget</strong><strong>="_blank"</strong> </li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;value="Submit but show results in a new window/tab"&gt;</li>
<li>&lt;/form&gt;</li>
</ol></div>



### 5.5.13 formenctype

#### A word about the enctype attribute of the `<form>` element

The enctype attribute existed before HTML5. It is often used together with forms that contain file input fields. For sending files to a remote server, we use <strong>"<i>multipart</i>"</strong> forms. This special encoding of forms needs to be specified using the `enctype` attribute, as shown in the example below:

[Online example at JSBin](https://jsbin.com/magexat/3/edit?html,output):  ([Local Example - formenctype](src/5.5.13-example1.html))

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp; &nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp; &lt;title&gt;Jsbin&lt;/title&gt;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp; &nbsp; &lt;form action="default.php" method="post" enctype="multipart/form-data"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; Given name: &lt;input type="text" name="gname"&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp; Family name: &lt;input type="text" name="fname"&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;input type="submit" value="Submit"&gt;</li>
<li>&nbsp; &nbsp; &lt;/form&gt;</li>
<li>&nbsp; &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>

Note that when you send form content using Ajax, this attribute is not needed, as you will specify the type of data sent to the remote server in JavaScript, using the [FormData object](https://tinyurl.com/pbtpfea).


#### As an attribute of the `<input type="submit" enctype=...>` element

Since HTML5, this attribute can also be used in `<input type="submit">` input fields.

If an `<input type="submit">` field has this attribute, then, __when submitted using method=POST__, the browser will send the form content encoded with the method specified by the `formenctype` attribute. And this overrides the value of the enctype attribute specified in the `<form enctype=...>` element (or its default value, if not present).


#### Typical use

<div><ol>
<li value="1">&lt;form action="defaultAction.php"&gt;</li>
<li>&nbsp; &nbsp;...</li>
<li>&nbsp; &nbsp;<strong>&lt;input type="submit" formenctype="multipart/form-data"</strong></li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <strong>value</strong><strong>="Submit as Multipart/form-data"&gt;</strong></li>
<li>&lt;/form&gt;</li>
</ol></div>

The possible values for this field are:

+ `application/x-www-form-urlencoded`: all characters are escaped/encoded before submission, for example, spaces become "+", accentuated characters are transformed into hexadecimal, etc.
+ `multipart/form-data`: encoding is not done. Usually we use this value for submitting binary data such as images, files, etc.
+ `text/plain`: some encoding is done on standard characters like space (that becomes a "+"), nothing is done for special characters.


#### Example

[Try this online example at JSBin](https://jsbin.com/lokukam/4/edit?html,output)  ([Local Example - multiple given names formenctype](src/5.5.13-example2.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 20vw;"
    onclick="window.open('https://tinyurl.com/y3z64jpt')"
    src    ="https://tinyurl.com/y4aegvbz"
    alt    ="example of use of the formenctype attribute"
    title  ="example of use of the formenctype attribute"
  />
</figure>


Source code:

<div><ol>
<li value="1">&lt;!DOCTYPE html&gt;</li>
<li>&lt;html lang="en"&gt;</li>
<li>&nbsp; &lt;head&gt;</li>
<li>&nbsp; &nbsp; &lt;meta charset="utf-8"&gt;</li>
<li>&nbsp; &nbsp; &lt;title&gt;Jsbin&lt;/title&gt;</li>
<li>&nbsp; &lt;/head&gt;</li>
<li>&nbsp; &lt;body&gt;</li>
<li>&nbsp; &nbsp; &lt;form action="defaultAction.php" method="post"</li>
<li>&nbsp; &nbsp; &nbsp; enctype="application/x-www-form-urlencoded"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;label for="givenName"&gt;Given name:&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;input type="text" name="givenName" id="givenName"&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;label for="familyName"&gt;Family name:&lt;/label&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;input type="text" name="familyName" id="familyName"&gt;&lt;br&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;input type="submit" value="Submit"&gt;</li>
<li>&nbsp; &nbsp; &nbsp; &lt;input type="submit"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; formenctype="multipart/form-data"</li>
<li>&nbsp; &nbsp; &nbsp; &nbsp; value="Submit as Multipart/form-data"&gt;</li>
<li>&nbsp; &nbsp; &lt;/form&gt;</li>
<li>&nbsp;&nbsp; &nbsp;&lt;p&gt;&lt;b&gt;Note:&lt;/b&gt; The formenctype attribute is not supported by all browsers.&lt;/p&gt;</li>
<li>&nbsp; &lt;/body&gt;</li>
<li>&lt;/html&gt;</li>
</ol></div>


__Explanations and how to see the difference between the two kinds of formenctype values__

If you run [this example in the JSBin](https://jsbin.com/lokukam/4/edit?html,output) standalone mode (click the black arrow on the top right of the output tab, in JSBin), you should see this: ([Local Example - two kinds of formenctype](src/5.5.13-example3.html))

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y3z64jpt')"
    src    ="https://tinyurl.com/y582z8s3"
    alt    ="js bin screenshot of the above example"
    title  ="js bin screenshot of the above example"
  />
</figure>


Then, open the devtools and go to the "Network" tab, click on the POST request. Once done, click on the right on the "Header" tab to see the HTTP headers, and scroll down, you should see the form-data entries in the header, like in this screenshot:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 40vw;"
    onclick="window.open('https://tinyurl.com/y3z64jpt')"
    src    ="https://tinyurl.com/yyvkcxqe"
    alt    ="HTTP header showing form-data entries"
    title  ="HTTP header showing form-data entries"
  />
</figure>


And if you start again and click on the left submit button, the one without the formenctype attribute, you should see that the form content has been submitted "normally" (default value is "urlencoded", spaces are replaced by "+", etc.). Here is a screenshot of what you should see:

<figure style="margin: 0.5em; text-align: center;">
  <img style="margin: 0.1em; padding-top: 0.5em; width: 30vw;"
    onclick="window.open('https://tinyurl.com/y3z64jpt')"
    src    ="https://tinyurl.com/y5lmnpog"
    alt    ="form content send "normally", urlencoded"
    title  ="form content send "normally", urlencoded"
  />
</figure>


### 5.5.14 Discussion

Here is the discussion forum for this part of the course. You can post your comments and share your creations here, and of course ask questions.

#### Suggested topics:

+ Had you previously heard of the last attributes we presented or were they new to you?
+ Do you know some good tutorials about JavaScript regexps or online tools for creating regexps interactively?



