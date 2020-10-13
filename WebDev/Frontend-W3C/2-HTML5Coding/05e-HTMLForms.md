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

  Ans: ;






